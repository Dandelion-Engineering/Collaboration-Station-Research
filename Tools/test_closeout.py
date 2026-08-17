#!/usr/bin/env python3
"""Tests for closeout.py, and the measurements that justify it.

    python Tools/test_closeout.py

Every scenario runs in a throwaway repo with its own bare remote, created in a
temp directory. This file never touches the real repository or its remote.

Sections A-C measure what `AgentPrompt.md` step 9 actually does when two agents
reach it at the same moment. Section D checks that closeout.py fixes each
measured failure. Section E measures what `--all` does with unrelated human
work in the tree. Section F holds `--dry-run` to being a preview rather than an
operation. Section G covers moved paths, including the exact one-sided commit
that can leave a closed claim in both `Work/Active/` and `Work/Done/`. Section H
proves that remote divergence refuses without an automatic rebase. The
measurements are kept in the test on purpose: if a future
version of git changes this behaviour, the tool should stop being justified
by a paragraph and start being questioned by a failing test.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "closeout.py")
WORK = tempfile.mkdtemp(prefix="closeouttest-")
PASS, FAIL = [], []


def git(repo, *args):
    p = subprocess.run(["git"] + list(args), cwd=repo, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return p.returncode, ((p.stdout or "") + (p.stderr or "")).strip()


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    print("  %s %s%s" % ("PASS" if condition else "FAIL", name,
                         ("  <- " + detail) if detail else ""))


def note(text):
    print("     %s" % text)


def write(repo, relpath, text):
    path = os.path.join(repo, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def new_repo(name, with_tool=False):
    """A clone with a bare remote. `with_tool` copies closeout.py into the
    same relative location it expects, so its repo_root() lands correctly."""
    bare = os.path.join(WORK, name + ".git")
    repo = os.path.join(WORK, name)
    subprocess.run(["git", "init", "--bare", "-b", "main", bare], capture_output=True, check=True)
    subprocess.run(["git", "clone", bare, repo], capture_output=True, check=True)
    git(repo, "config", "user.email", "test@example.com")
    git(repo, "config", "user.name", "Test")
    write(repo, "seed.md", "seed\n")
    if with_tool:
        os.makedirs(os.path.join(repo, "Tools"), exist_ok=True)
        shutil.copy(TOOL, os.path.join(repo, "Tools", "closeout.py"))
    git(repo, "add", "-A")
    git(repo, "commit", "-m", "Initial")
    git(repo, "push", "-u", "origin", "main")
    return repo


def raw_closeout(repo, agent, session, results, barrier=None):
    """Exactly the three commands AgentPrompt.md step 9 describes."""
    if barrier:
        barrier.wait()
    out = [git(repo, "add", "-A"),
           git(repo, "commit", "-m", "%s Session %d" % (agent, session)),
           git(repo, "push")]
    results[agent] = out


def tool_closeout(repo, agent, session, results, barrier=None, paths=None,
                  dry_run=False):
    if barrier:
        barrier.wait()
    cmd = [sys.executable, os.path.join(repo, "Tools", "closeout.py"),
           "--agent", agent, "--session", str(session), "--timeout", "60"]
    cmd += (["--paths"] + paths) if paths else ["--all"]
    if dry_run:
        cmd.append("--dry-run")
    p = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    results[agent] = (p.returncode, (p.stdout or "") + (p.stderr or ""))


def session_commits(repo):
    _, log = git(repo, "log", "--oneline")
    return [line for line in log.splitlines() if "Session" in line]


def files_in(repo, rev):
    _, out = git(repo, "show", "--stat", "--name-only", "--format=", rev)
    return [line.strip() for line in out.splitlines() if line.strip()]


def cross_attributed(repo):
    """Commits that contain the other agent's private workspace files."""
    bad = []
    for c in session_commits(repo):
        rev = c.split()[0]
        who = "Claude" if "Claude" in c else "Codex"
        other = "Codex" if who == "Claude" else "Claude"
        touched = files_in(repo, rev)
        note("%s (%s) -> %s" % (rev, who, touched))
        if any(("agents/%s/" % other) in f for f in touched):
            bad.append((who, touched))
    return bad


# ---------------------------------------------------------------- section A

print("\nA. Control: sequential closeout")
print("-" * 72)
repo = new_repo("sequential")
res = {}
write(repo, "agents/Claude/report.md", "Claude's work\n")
raw_closeout(repo, "Claude", 4, res)
write(repo, "agents/Codex/report.md", "Codex's work\n")
raw_closeout(repo, "Codex", 4, res)
check("sequential closeout is clean: two commits, correct attribution",
      len(session_commits(repo)) == 2 and not cross_attributed(repo))

# ---------------------------------------------------------------- section B

print("\nB. Measured: two raw closeouts at the same moment")
print("-" * 72)
repo = new_repo("parallel")
write(repo, "agents/Claude/report.md", "Claude's work\n")
write(repo, "agents/Codex/report.md", "Codex's work\n")
res = {}
barrier = threading.Barrier(2)
threads = [threading.Thread(target=raw_closeout, args=(repo, a, 4, res, barrier))
           for a in ("Claude", "Codex")]
for t in threads:
    t.start()
for t in threads:
    t.join()

commits = session_commits(repo)
note("commits created: %d (expected 2)" % len(commits))
cross = cross_attributed(repo)
failures = [(rc, out) for o in res.values() for rc, out in o if rc != 0]
lock_errs = [out for rc, out in failures if "index.lock" in out or "another git process" in out]
pushes = [o[-1] for o in res.values()]
rejected = [out for rc, out in pushes if rc != 0 and "up-to-date" not in out]

check("raw parallel closeout loses a session's own commit", len(commits) < 2,
      "%d commits" % len(commits))
check("raw parallel closeout misattributes files", bool(cross))
check("raw parallel closeout hits git's index.lock", bool(lock_errs),
      "%d index.lock error(s)" % len(lock_errs))
check("raw parallel closeout has its push rejected", bool(rejected),
      "%d rejected" % len(rejected))
note("(these four 'PASS' lines mean the problem reproduces, which is the point)")

# ---------------------------------------------------------------- section C

print("\nC. Measured: a file still being written when the other agent stages")
print("-" * 72)
repo = new_repo("torn")
write(repo, "agents/Claude/report.md", "Claude done\n")
target = os.path.join(repo, "agents", "Codex", "big.md")
os.makedirs(os.path.dirname(target), exist_ok=True)
stop = threading.Event()


def slow_writer():
    with open(target, "w", encoding="utf-8") as fh:
        for i in range(400):
            if stop.is_set():
                break
            fh.write("Codex report line %d\n" % i)
            fh.flush()
            time.sleep(0.002)


w = threading.Thread(target=slow_writer)
w.start()
time.sleep(0.05)
res = {}
raw_closeout(repo, "Claude", 4, res)
stop.set()
w.join()
rc_show, committed = git(repo, "show", "HEAD:agents/Codex/big.md")
in_commit = rc_show == 0
committed_lines = len([x for x in committed.splitlines() if x.startswith("Codex report")])
with open(target, encoding="utf-8") as fh:
    final_lines = len([x for x in fh if x.startswith("Codex report")])
note("committed %d of %d lines; present in commit: %s" % (committed_lines, final_lines, in_commit))
check("a mid-write file is captured incomplete under the other agent's name",
      in_commit and committed_lines != final_lines)
note("recoverable -- the next closeout commits the finished file -- but the")
note("pushed history contains a broken snapshot until then.")

# ---------------------------------------------------------------- section D

print("\nD. closeout.py against the same simultaneous case")
print("-" * 72)
repo = new_repo("tool", with_tool=True)
write(repo, "agents/Claude/report.md", "Claude's work\n")
write(repo, "agents/Codex/report.md", "Codex's work\n")
res = {}
barrier = threading.Barrier(2)
threads = [
    threading.Thread(target=tool_closeout, args=(repo, "Claude", 4, res, barrier),
                     kwargs={"paths": ["agents/Claude"]}),
    threading.Thread(target=tool_closeout, args=(repo, "Codex", 4, res, barrier),
                     kwargs={"paths": ["agents/Codex"]}),
]
for t in threads:
    t.start()
for t in threads:
    t.join()

commits = session_commits(repo)
note("commits created: %d" % len(commits))
cross = cross_attributed(repo)
combined = "".join(out for _rc, out in res.values())

check("both sessions get their own commit", len(commits) == 2, "%d commits" % len(commits))
check("attribution is exact: no agent commits the other's files", not cross, str(cross))
check("both invocations succeed", all(rc == 0 for rc, _ in res.values()),
      str({a: rc for a, (rc, _) in res.items()}))
check("no index.lock failure", "index.lock" not in combined)
check("the second agent waited for the lock rather than colliding",
      "Closeout lock held by" in combined)
_, remote = git(repo, "log", "--oneline", "origin/main")
check("the remote received both commits", remote.count("Session 4") == 2,
      remote.replace("\n", " | ")[:160])

print("\n   --all mode, and the 'nothing left to stage' path")
repo = new_repo("tool-all", with_tool=True)
write(repo, "agents/Claude/report.md", "Claude's work\n")
write(repo, "agents/Codex/report.md", "Codex's work\n")
res = {}
barrier = threading.Barrier(2)
threads = [threading.Thread(target=tool_closeout, args=(repo, a, 4, res, barrier))
           for a in ("Claude", "Codex")]
for t in threads:
    t.start()
for t in threads:
    t.join()
combined = "".join(out for _rc, out in res.values())
check("--all: both invocations still succeed", all(rc == 0 for rc, _ in res.values()),
      str({a: rc for a, (rc, _) in res.items()}))
check("--all: the second agent is told plainly that nothing was lost",
      "no work is lost" in combined or "Nothing to commit" in combined)
_, status = git(repo, "status", "--short")
check("--all: working tree ends clean, everything committed", status.strip() == "",
      "left over: %s" % status)
_, remote = git(repo, "log", "--oneline", "origin/main")
check("--all: the remote has every file", "Session 4" in remote)
_, remote_tree = git(repo, "ls-tree", "-r", "--name-only", "origin/main")
check("the live closeout lock never enters a commit without relying on gitignore",
      ".closeout-session.lock" not in remote_tree, remote_tree)

print("\n   safety behaviours")
repo = new_repo("tool-safety", with_tool=True)
write(repo, "agents/Claude/report.md", "x\n")
res = {}
tool_closeout(repo, "Claude", 4, res, paths=["agents/Claude"])
rc, out = res["Claude"]
check("the lock is released after a successful run",
      not os.path.exists(os.path.join(repo, ".closeout-session.lock")))

with open(os.path.join(repo, ".closeout-session.lock"), "w", encoding="utf-8") as fh:
    fh.write('{"agent": "Codex", "pid": 999999, "acquired": "earlier"}')
write(repo, "agents/Claude/second.md", "y\n")
p = subprocess.run([sys.executable, os.path.join(repo, "Tools", "closeout.py"),
                    "--agent", "Claude", "--session", "5", "--all", "--timeout", "3"],
                   cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace")
out = (p.stdout or "") + (p.stderr or "")
check("a held lock blocks the run and names the holder",
      p.returncode == 4 and "Codex" in out, "rc=%s" % p.returncode)
check("a stale lock is diagnosed but never broken automatically",
      "probably stale" in out and "will not break a lock" in out)
check("the stale lock is still on disk afterwards",
      os.path.exists(os.path.join(repo, ".closeout-session.lock")))
os.remove(os.path.join(repo, ".closeout-session.lock"))

p = subprocess.run([sys.executable, os.path.join(repo, "Tools", "closeout.py"),
                    "--agent", "Claude", "--session", "5", "--all", "--dry-run"],
                   cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace")
out = (p.stdout or "") + (p.stderr or "")
_, staged = git(repo, "diff", "--cached", "--name-only")
check("--dry-run commits nothing and leaves the index clean",
      p.returncode == 0 and "DRY RUN" in out and staged.strip() == "",
      "staged after dry run: %s" % staged)
check("--dry-run still names what it would have committed", "second.md" in out)

# ---------------------------------------------------------------- section E
# This is a measurement, not an authority guard. With `--all`, unrelated work
# present in the shared tree can enter the agent's commit, and Git authorship
# may not distinguish who actually wrote it. Exact `--paths` remains the safe
# default for concurrent work.

print("\nE. What --all does with unrelated human work in the tree")
print("-" * 72)

repo = new_repo("human-raw")
write(repo, "shared/human-note.md", "A human's words, saved by hand.\n")
res = {}
raw_closeout(repo, "Claude", 4, res)

_, subjects = git(repo, "log", "-1", "--format=%s")
check("an --all closeout commits unrelated human work under the agent label",
      subjects.strip() == "Claude Session 4", "got %r" % subjects.strip())

_, authors = git(repo, "log", "--format=%an")
distinct = sorted(set(a for a in authors.splitlines() if a.strip()))
note("distinct commit authors in the whole repository: %s" % distinct)
check("agent commits and human commits share ONE author identity",
      len(distinct) == 1,
      "if this ever fails, the author field became usable and a guard over "
      "authorship could be reconsidered")

repo = new_repo("human-own", with_tool=True)
write(repo, "shared/human-note.md", "A human's words.\n")
git(repo, "add", "-A")
git(repo, "commit", "-m", "Human: record a project note")
git(repo, "push")
_, subjects = git(repo, "log", "-1", "--format=%s")
check("a human-labeled commit is legible in the log",
      subjects.startswith("Human:"), "got %r" % subjects.strip())

# ---------------------------------------------------------------- section F
# --dry-run must be a preview, not an operation.
#
# A file staged before a legacy dry run was silently unstaged because that
# branch ended in a bare `git reset`. It also enumerated the whole index, so an
# unrelated staged file was reported as "would include" in a commit that would
# not have contained it.
#
# Both matter here specifically because two agents share one working tree: the
# index a dry run wipes is not necessarily the dry-runner's.

print("\nF. --dry-run is a preview and touches nothing")
print("-" * 72)


def would_include(out):
    """The file list the dry run says it would commit.

    Parsed from the report rather than searched for in the whole output: the
    `Working tree before:` status legitimately names every dirty file in the
    shared tree, so a substring search over stdout cannot tell "reported as
    part of this commit" from "visible in the repository at all".
    """
    lines = out.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("would include:"):
            return [l.strip() for l in lines[i + 1:] if l.startswith("  ")]
    return None

repo = new_repo("dryrun-index", with_tool=True)
write(repo, "already-staged.md", "the OTHER agent's staged work\n")
write(repo, "agents/Claude/report.md", "my own unstaged work\n")
git(repo, "add", "already-staged.md")

_, before = git(repo, "diff", "--cached", "--name-only")
before_staged = sorted(f for f in before.splitlines() if f.strip())
note("staged before the dry run: %s" % before_staged)

res = {}
tool_closeout(repo, "Claude", 4, res, paths=["agents/Claude"], dry_run=True)
rc, out = res["Claude"]

_, after = git(repo, "diff", "--cached", "--name-only")
after_staged = sorted(f for f in after.splitlines() if f.strip())
note("staged after the dry run:  %s" % after_staged)

check("--dry-run preserves an index it did not stage",
      after_staged == before_staged == ["already-staged.md"],
      "before %s -> after %s" % (before_staged, after_staged))
reported = would_include(out)
note("reported as 'would include': %s" % reported)
check("--dry-run reports only the requested pathspec",
      reported == ["agents/Claude/report.md"],
      "got %s" % reported)
check("--dry-run says it committed nothing",
      rc == 0 and "DRY RUN" in out, "rc=%s" % rc)
check("--dry-run leaves no scratch index behind",
      not any(n.endswith(".closeout-dryrun")
              for n in os.listdir(os.path.join(repo, ".git"))),
      "found %s" % [n for n in os.listdir(os.path.join(repo, ".git"))
                    if "dryrun" in n])

# The same run, without a pathspec: --all commits the whole index, so reporting
# the whole index is correct there and the preview must still not write it.
repo = new_repo("dryrun-all", with_tool=True)
write(repo, "already-staged.md", "the OTHER agent's staged work\n")
write(repo, "agents/Claude/report.md", "my own unstaged work\n")
git(repo, "add", "already-staged.md")

res = {}
tool_closeout(repo, "Claude", 4, res, dry_run=True)
rc, out = res["Claude"]
_, after = git(repo, "diff", "--cached", "--name-only")
after_staged = sorted(f for f in after.splitlines() if f.strip())

check("--dry-run --all preserves the index too",
      after_staged == ["already-staged.md"], "after %s" % after_staged)
reported = would_include(out)
note("reported as 'would include': %s" % reported)
check("--dry-run --all does report the whole index, because --all commits it",
      sorted(reported or []) == ["agents/Claude/report.md", "already-staged.md"],
      "got %s" % reported)
check("--dry-run --all created no commit",
      session_commits(repo) == [], "got %s" % session_commits(repo))


# ---------------------------------------------------------------- section G

print("\nG. Explicit paths preserve both endpoints of a move")
print("-" * 72)

# The real failure: `git mv` stages both endpoints, but a destination-only
# pathspec used to commit only the addition. HEAD then contained both paths
# while the working tree looked correct and retained only the destination.
repo = new_repo("move-one-sided", with_tool=True)
write(repo, "Work/Active/claim.md", "closed claim\n")
git(repo, "add", "-A")
git(repo, "commit", "-m", "Add active claim")
git(repo, "push")
os.makedirs(os.path.join(repo, "Work", "Done"), exist_ok=True)
git(repo, "mv", "Work/Active/claim.md", "Work/Done/claim.md")

res = {}
tool_closeout(repo, "Codex", 16, res,
              paths=["Work/Done/claim.md"])
rc, out = res["Codex"]
check("one-sided move refuses before commit",
      rc == 1 and "REFUSED: a move has only one endpoint" in out,
      "rc=%s" % rc)
check("one-sided refusal names both endpoints",
      "Work/Active/claim.md" in out and "Work/Done/claim.md" in out)
check("one-sided refusal creates no session commit or push",
      session_commits(repo) == [] and
      files_in(repo, "origin/main") == ["Work/Active/claim.md"],
      "commits %s; remote %s" %
      (session_commits(repo), files_in(repo, "origin/main")))
_, staged = git(repo, "diff", "--cached", "--name-status", "-M")
check("one-sided refusal preserves the staged rename",
      staged.startswith("R100\tWork/Active/claim.md\tWork/Done/claim.md"),
      staged)

# Dry-run must make the same decision in its scratch index and preserve the
# already-staged real rename exactly.
res = {}
tool_closeout(repo, "Codex", 16, res,
              paths=["Work/Done/claim.md"], dry_run=True)
dry_rc, dry_out = res["Codex"]
_, staged_after = git(repo, "diff", "--cached", "--name-status", "-M")
check("dry-run also refuses the one-sided move without touching the real index",
      dry_rc == 1 and "REFUSED: a move has only one endpoint" in dry_out and
      staged_after == staged,
      "rc=%s; before %r; after %r" % (dry_rc, staged, staged_after))

# Passing both endpoints is exact: the missing source is staged as a tracked
# deletion, the destination is staged as an addition, and the path-limited
# commit lands as one rename with nothing else swept in.
repo = new_repo("move-two-sided", with_tool=True)
write(repo, "Work/Active/claim.md", "closed claim\n")
git(repo, "add", "-A")
git(repo, "commit", "-m", "Add active claim")
git(repo, "push")
os.makedirs(os.path.join(repo, "Work", "Done"), exist_ok=True)
shutil.move(os.path.join(repo, "Work", "Active", "claim.md"),
            os.path.join(repo, "Work", "Done", "claim.md"))

res = {}
tool_closeout(repo, "Codex", 16, res,
              paths=["Work/Active/claim.md", "Work/Done/claim.md"])
rc, out = res["Codex"]
check("two-sided move closeout succeeds", rc == 0, "rc=%s" % rc)
_, head_files = git(repo, "ls-tree", "-r", "--name-only", "HEAD")
_, remote_files = git(repo, "ls-tree", "-r", "--name-only", "origin/main")
check("two-sided move leaves only the destination locally and remotely",
      "Work/Done/claim.md" in head_files and
      "Work/Active/claim.md" not in head_files and
      remote_files == head_files,
      "HEAD %r; remote %r" % (head_files, remote_files))
_, status = git(repo, "status", "--short")
check("two-sided move ends with a clean working tree and index",
      status.strip() == "", status)

# A staged rename owned by the other agent must not block or enter a closeout
# whose requested paths select neither endpoint. It stays staged for its owner.
repo = new_repo("move-outside-scope", with_tool=True)
write(repo, "Work/Active/other.md", "other agent's claim\n")
git(repo, "add", "-A")
git(repo, "commit", "-m", "Add other claim")
git(repo, "push")
os.makedirs(os.path.join(repo, "Work", "Done"), exist_ok=True)
git(repo, "mv", "Work/Active/other.md", "Work/Done/other.md")
write(repo, "agents/Codex/report.md", "Codex's work\n")

res = {}
tool_closeout(repo, "Codex", 16, res, paths=["agents/Codex"])
rc, out = res["Codex"]
check("a rename with neither endpoint requested does not block closeout",
      rc == 0 and files_in(repo, "HEAD") == ["agents/Codex/report.md"],
      "rc=%s; files %s" % (rc, files_in(repo, "HEAD")))
_, staged_other = git(repo, "diff", "--cached", "--name-status", "-M")
check("the unrelated rename remains staged for its owner",
      staged_other.startswith("R100\tWork/Active/other.md\tWork/Done/other.md"),
      staged_other)
_, remote_files = git(repo, "ls-tree", "-r", "--name-only", "origin/main")
check("the unrelated rename does not enter the remote commit",
      "Work/Active/other.md" in remote_files and
      "Work/Done/other.md" not in remote_files,
      remote_files)

# Reproduce the already-pushed half move from the live failure, then prove the
# missing tracked source can be recovered as one exact deletion. At this point
# HEAD already contains both paths, so the remaining change is a deletion, not
# a rename, and passing the stranded source alone is correct.
git(repo, "commit", "-m", "Half-commit the move", "--", "Work/Done/other.md")
git(repo, "push")
res = {}
tool_closeout(repo, "Codex", 17, res, paths=["Work/Active/other.md"])
recovery_rc, recovery_out = res["Codex"]
check("a half-committed move recovers through the exact missing source",
      recovery_rc == 0, "rc=%s" % recovery_rc)
_, recovered_head = git(repo, "ls-tree", "-r", "--name-only", "HEAD")
_, recovered_remote = git(repo, "ls-tree", "-r", "--name-only", "origin/main")
_, recovered_status = git(repo, "status", "--short")
check("recovery leaves only the destination locally and remotely",
      "Work/Done/other.md" in recovered_head and
      "Work/Active/other.md" not in recovered_head and
      recovered_remote == recovered_head and recovered_status.strip() == "",
      "HEAD %r; remote %r; status %r" %
      (recovered_head, recovered_remote, recovered_status))


# ---------------------------------------------------------------- section H

print("\nH. Remote divergence refuses without rewriting history")
print("-" * 72)

repo = new_repo("push-divergence", with_tool=True)
_, remote_url = git(repo, "remote", "get-url", "origin")
other = os.path.join(WORK, "push-divergence-other")
subprocess.run(["git", "clone", remote_url, other], capture_output=True,
               check=True)
git(other, "config", "user.email", "other@example.com")
git(other, "config", "user.name", "Other Writer")
write(other, "remote-only.md", "other writer's committed work\n")
git(other, "add", "-A")
git(other, "commit", "-m", "Other writer commit")
git(other, "push")

write(repo, "agents/Codex/report.md", "local work\n")
res = {}
tool_closeout(repo, "Codex", 18, res, paths=["agents/Codex"])
rc, out = res["Codex"]
check("a non-fast-forward push refuses and names the boundary",
      rc == 1 and "PUSH REFUSED" in out and
      "will not pull, rebase, merge, force-push" in out,
      "rc=%s" % rc)
check("the refused closeout leaves no rebase or merge in progress",
      not os.path.exists(os.path.join(repo, ".git", "rebase-merge")) and
      not os.path.exists(os.path.join(repo, ".git", "rebase-apply")) and
      not os.path.exists(os.path.join(repo, ".git", "MERGE_HEAD")))
check("the closeout lock is released after push refusal",
      not os.path.exists(os.path.join(repo, ".closeout-session.lock")))
git(repo, "fetch", "origin")
_, remote_files = git(repo, "ls-tree", "-r", "--name-only", "origin/main")
_, local_files = git(repo, "ls-tree", "-r", "--name-only", "HEAD")
check("remote and local commits remain separate for explicit recovery",
      "remote-only.md" in remote_files and
      "agents/Codex/report.md" not in remote_files and
      "agents/Codex/report.md" in local_files and
      "remote-only.md" not in local_files,
      "remote %r; local %r" % (remote_files, local_files))


# ------------------------------------------------------------------ summary

print("\n" + "=" * 72)
print("PASSED %d   FAILED %d" % (len(PASS), len(FAIL)))
for name in FAIL:
    print("  FAILED: %s" % name)
shutil.rmtree(WORK, ignore_errors=True)
sys.exit(1 if FAIL else 0)
