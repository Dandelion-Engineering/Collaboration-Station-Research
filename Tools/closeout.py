#!/usr/bin/env python3
"""
closeout.py - run AgentPrompt.md step 9 safely when two agents share one repo.

WHY THIS EXISTS

`AgentPrompt.md` step 9 tells every agent, every session, to stage everything
it changed, commit as `<Name> Session <#>`, and push. That is the last thing
each agent does. If Claude and Codex run in parallel for similar lengths of
time, they will reach it at roughly the same moment -- so this is not a rare
race, it is a scheduled one.

Measured on 2026-08-06, two simultaneous closeouts in one working tree:

  - Only ONE commit was created. The second agent's `git commit` failed with
    `index.lock`, so an entire session went uncommitted under its own name.
  - The first commit contained the other agent's files, under the wrong name.
  - The second `git push` was rejected non-fast-forward.
  - A file still being written was captured mid-write and committed empty.

A lock alone does not fix the attribution half, because `git add -A` sweeps
whatever is on disk -- including the other agent's finished work -- and
`git commit` commits the shared index rather than "what I staged." So this
tool does two things together:

  1. Serializes the whole stage/commit/push sequence with an exclusive lock,
     which removes the index.lock failures and the push race.
  2. Commits an explicit pathspec, so the commit contains your paths and not
     whatever your colleague happened to finish thirty seconds earlier.

WHAT IT DOES NOT DO

It does not decide what you changed. You pass that in, or you pass `--all` and
accept that a simultaneous closeout may put someone else's file in your commit.
`--all` is the honest default for a solo session and is what makes this tool a
drop-in replacement for the three commands it wraps.

It never force-pushes, amends, rebases, resets history, resolves conflicts, or
breaks a lock it did not create. If it cannot finish, it stops and prints the
exact state rather than improvising -- an agent guessing at git recovery is how
a repository loses history.

USAGE

    python Tools/closeout.py --agent Claude --session 4 --all
    python Tools/closeout.py --agent Claude --session 4 \
        --paths "agents/Claude" "Tools" ".gitignore"
    python Tools/closeout.py --agent Claude --session 4 --all --dry-run

`--dry-run` reports and changes nothing. It stages into a COPY of the git index
so that its answer comes from the same code path as a real run while the
repository's own index -- which may hold the other agent's staged work -- is
never written.

For a moved path, pass BOTH the source and destination to `--paths`. Missing
tracked source paths are staged as exact deletions. If only one endpoint of a
detected rename is selected, the tool refuses before commit rather than
publishing both the old and new path.

Standard library only. No credentials, no network beyond `git push`.
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import time

LOCK_NAME = ".closeout-session.lock"
OK = 0
PROBLEM = 1
LOCK_BUSY = 4

# This program handles Git mechanics only. It never infers approval or
# authority from file contents, commit authorship, or a token-like string.
# The project's work record and review procedure remain the authority layer.

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except (AttributeError, OSError):  # pragma: no cover
    pass


def repo_root():
    """The repository this tool will actually stage and commit in.

    Git's own top level is used first because it is authoritative for the thing
    this tool does: it is, by definition, the repository the commit would land
    in. AgentPrompt.md is the fallback for a project that is not a repository
    yet, so the error says "not a git repository" rather than something
    misleading about layout. Neither available is an error, never a guess.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    p = subprocess.run(["git", "-C", here, "rev-parse", "--show-toplevel"],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    if p.returncode == 0 and p.stdout.strip():
        return os.path.abspath(p.stdout.strip())
    d = here
    while True:
        if os.path.isfile(os.path.join(d, "AgentPrompt.md")):
            sys.stdout.write(
                "REFUSED: %s looks like a project root but is not a "
                "git repository, so there is nothing to commit to. Initialise "
                "it first.\n" % d)
            sys.exit(1)
        parent = os.path.dirname(d)
        if parent == d:
            sys.stdout.write(
                "REFUSED: %s is not inside a git repository and no "
                "AgentPrompt.md was found above it, so the project root cannot "
                "be determined\n" % here)
            sys.exit(1)
        d = parent


def git(root, *args, index=None):
    """Run git in `root`. `index` points GIT_INDEX_FILE at a scratch index.

    A dry run must not write the repository's index -- the other agent may have
    work staged in it, and unstaging that silently is a data loss the caller
    asked for a preview instead of.
    """
    env = dict(os.environ, GIT_INDEX_FILE=index) if index else None
    p = subprocess.run(["git"] + list(args), cwd=root, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", env=env)
    # Trim blank lines, not indentation: `git status --short` encodes state in
    # the first two columns, and a bare .strip() eats the leading space of the
    # first line, silently misreporting a modified file as something else.
    return p.returncode, ((p.stdout or "") + (p.stderr or "")).strip("\r\n")


def say(line=""):
    sys.stdout.write(line + "\n")
    sys.stdout.flush()


def pid_alive(pid):
    """Best-effort liveness check. Wrong answers must fail toward 'alive'."""
    try:
        if os.name == "nt":
            out = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid],
                                 capture_output=True, text=True).stdout
            return str(pid) in out
        os.kill(pid, 0)
        return True
    except Exception:
        return True


def acquire(lock_path, agent, timeout, poll=2):
    """Exclusive create. Returns True, or False if the window closes."""
    deadline = time.time() + timeout
    announced = False
    while True:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump({"agent": agent, "pid": os.getpid(),
                           "acquired": time.strftime("%Y-%m-%d %H:%M:%S %Z")}, fh)
            return True
        except FileExistsError:
            holder = read_lock(lock_path)
            if not announced:
                say("Closeout lock held by %s (pid %s, since %s). Waiting up to %ds."
                    % (holder.get("agent", "?"), holder.get("pid", "?"),
                       holder.get("acquired", "?"), timeout))
                announced = True
            if time.time() >= deadline:
                say("")
                say("Could not acquire the closeout lock within %ds." % timeout)
                pid = holder.get("pid")
                if isinstance(pid, int) and not pid_alive(pid):
                    say("The holding process (pid %s) is no longer running, so the lock is"
                        % pid)
                    say("probably stale. Confirm nothing else is committing, then delete")
                    say("this exact lock file manually: %s" % lock_path)
                    say("This tool will not break a lock on its own -- doing that")
                    say("automatically would reintroduce the race it exists to prevent.")
                else:
                    say("The other agent is still closing out. Wait and run this again.")
                return False
            time.sleep(poll)


def read_lock(lock_path):
    try:
        with open(lock_path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def scratch_index(root):
    """A throwaway copy of the repository's index, for --dry-run.

    Copied rather than started empty so the preview sees exactly what a real
    run would see, including anything already staged. Returns None if git
    cannot say where the index lives, which the caller treats as fatal for a
    dry run rather than falling back to the real one.
    """
    rc, path = git(root, "rev-parse", "--git-path", "index")
    if rc != 0 or not path.strip():
        return None
    real = os.path.join(root, path.strip())
    scratch = real + ".closeout-dryrun"
    try:
        shutil.copyfile(real, scratch)
    except FileNotFoundError:
        pass          # no index yet means nothing is staged; an empty one is right
    except OSError:
        return None
    return scratch


def run_closeout(root, args):
    """Dispatch, so the scratch index is always cleaned up."""
    if not args.dry_run:
        return _closeout(root, args, None)
    scratch = scratch_index(root)
    if scratch is None:
        say("Could not make a scratch copy of the git index, so this dry run")
        say("would have to write the real one. Refusing: a preview must not")
        say("unstage work you did not ask it to touch.")
        return PROBLEM
    try:
        return _closeout(root, args, scratch)
    finally:
        try:
            os.remove(scratch)
        except OSError:
            pass


def stage_explicit_paths(root, paths, index):
    """Stage exact caller paths, including tracked paths deleted by a move.

    Plain `git add <missing-path>` is an error, so the old endpoint of a move
    used to be impossible to pass to --paths. `git add -u -- <path>` stages
    only tracked modifications/deletions under that exact pathspec; it does
    not widen staging to the repository.
    """
    for path in paths:
        absolute = path if os.path.isabs(path) else os.path.join(root, path)
        if os.path.lexists(absolute):
            rc, out = git(root, "add", "--", path, index=index)
        else:
            # A half-committed move leaves the source deletion staged even
            # though the path is absent from both the working tree and index.
            # Re-adding that exact path is then a fatal pathspec error, but no
            # staging is needed: the requested deletion is already present.
            staged_rc, staged_out = git(
                root, "diff", "--cached", "--quiet", "--", path,
                index=index)
            if staged_rc == 1:
                rc, out = OK, ""
            elif staged_rc != 0:
                rc, out = staged_rc, staged_out
            else:
                rc, out = git(root, "add", "-u", "--", path,
                              index=index)
        if rc != 0:
            return rc, out
    return OK, ""


def path_is_requested(root, path, requested_paths):
    """Whether a repository-relative path is inside an explicit caller path."""
    endpoint = os.path.normcase(path).replace("\\", "/").lstrip("./")
    for requested in requested_paths:
        if os.path.isabs(requested):
            requested = os.path.relpath(requested, root)
        candidate = os.path.normcase(os.path.normpath(requested))
        candidate = candidate.replace("\\", "/").lstrip("./")
        if candidate in ("", "."):
            return True
        candidate = candidate.rstrip("/")
        if endpoint == candidate or endpoint.startswith(candidate + "/"):
            return True
    return False


def one_sided_renames(root, requested_paths, index):
    """Return detected renames with exactly one selected endpoint.

    Compare HEAD to the intended index + working-tree state rather than only
    the index. This catches both `git mv` (already staged) and an ordinary
    filesystem move whose destination was just staged by this tool.
    """
    rc, out = git(root, "diff", "HEAD", "--name-status", "-M", index=index)
    if rc != 0:
        return None, out
    one_sided = []
    for line in out.splitlines():
        parts = line.split("\t")
        if len(parts) >= 3 and parts[0].startswith("R"):
            source, destination = parts[1], parts[2]
            source_selected = path_is_requested(root, source, requested_paths)
            destination_selected = path_is_requested(root, destination,
                                                     requested_paths)
            if source_selected != destination_selected:
                one_sided.append((source, destination,
                                  source_selected, destination_selected))
    return one_sided, ""


def _closeout(root, args, index):
    label = "%s Session %s" % (args.agent, args.session)
    pathspec = ["--"] + list(args.paths) if args.paths else []

    tracked_lock_rc, _ = git(
        root, "ls-files", "--error-unmatch", "--", LOCK_NAME,
        index=index)
    if tracked_lock_rc == 0:
        say("REFUSED: %s is tracked. It is live runtime state and cannot be" %
            LOCK_NAME)
        say("safely separated from this closeout. Remove it from version control")
        say("and add the documented ignore entry before trying again.")
        return PROBLEM

    rc, before = git(root, "status", "--short", index=index)
    say("Working tree before:")
    say(before if before else "  (clean)")
    say("")

    if args.paths:
        say("Staging (explicit pathspec): %s" % ", ".join(args.paths))
        rc, out = stage_explicit_paths(root, args.paths, index)
    else:
        say("Staging: git add -A")
        rc, out = git(root, "add", "-A", index=index)
    if rc != 0:
        say("FAILED at stage:\n%s" % out)
        return PROBLEM

    # The live lock is never part of a commit, even in a copied project whose
    # ignore file is absent or wrong. `git rm --cached` changes only the chosen
    # index and avoids the prohibited `git reset` path. A tracked lock was
    # refused above rather than silently staged as a deletion.
    rc, out = git(root, "rm", "--cached", "-q", "--ignore-unmatch", "--",
                  LOCK_NAME, index=index)
    if rc != 0:
        say("FAILED while isolating the live closeout lock:\n%s" % out)
        return PROBLEM

    # Report the pathspec that will actually be committed, not the whole index.
    # `git commit -- <pathspec>` takes only those paths, so counting index-wide
    # would name the other agent's staged files as "would include" -- a preview
    # of a commit that is not the one about to be made.
    if pathspec:
        rc, staged = git(root, "diff", "--cached", "--name-only",
                         *pathspec, index=index)
    else:
        rc, staged = git(root, "diff", "--cached", "--name-only", index=index)
    if rc != 0:
        say("FAILED while reading staged paths:\n%s" % staged)
        return PROBLEM
    staged_files = [f for f in staged.splitlines() if f.strip()]

    if pathspec:
        one_sided, rename_error = one_sided_renames(
            root, args.paths, index)
        if one_sided is None:
            say("FAILED while checking moves:\n%s" % rename_error)
            return PROBLEM
        if one_sided:
            say("")
            say("REFUSED: a move has only one endpoint in --paths.")
            for source, destination, source_selected, destination_selected in one_sided:
                say("  source      : %s (%s)" %
                    (source, "selected" if source_selected else "missing"))
                say("  destination : %s (%s)" %
                    (destination, "selected" if destination_selected else "missing"))
            say("Pass both the source and destination paths. Committing one side")
            say("would leave both lifecycle paths in the pushed repository.")
            return PROBLEM

    if args.dry_run:
        say("")
        say("DRY RUN - nothing committed or pushed, and the index was not touched.")
        say("would commit : %s" % label)
        say("would include: %d file(s)" % len(staged_files))
        for f in staged_files:
            say("  %s" % f)
        return OK

    if not staged_files:
        say("Nothing staged. The other agent's closeout may have already swept these")
        say("files into its own commit -- that is not an error, and no work is lost.")
    else:
        say("Committing %d file(s) as: %s" % (len(staged_files), label))
        commit_args = ["commit", "-m", label] + pathspec
        rc, out = git(root, *commit_args)
        if rc != 0:
            if "nothing to commit" in out or "no changes added" in out:
                say("Nothing to commit.")
            else:
                say("FAILED at commit:\n%s" % out)
                return PROBLEM
        else:
            say(out.splitlines()[0] if out else "committed")

    say("")
    rc, out = git(root, "push")
    if rc == 0:
        say("Pushed.")
    elif "Everything up-to-date" in out:
        say("Nothing to push.")
    else:
        say("PUSH REFUSED. The remote differs from the local state.")
        say(out.splitlines()[-1] if out else "")
        say("This tool will not pull, rebase, merge, force-push, or resolve the")
        say("divergence. Inspect the remote and working tree, coordinate with the")
        say("other writer, then run a new closeout after the state is understood.")
        return PROBLEM

    rc, after = git(root, "status", "--short")
    say("")
    say("Working tree after:")
    say(after if after else "  (clean)")
    rc, log = git(root, "log", "--oneline", "-3")
    say("")
    say("Recent commits:")
    for line in log.splitlines():
        say("  %s" % line)
    return OK


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Serialized, attributable git closeout for parallel agent sessions.")
    parser.add_argument("--agent", required=True, help="Claude or Codex")
    parser.add_argument("--session", required=True, help="your session number")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--all", action="store_true",
                       help="stage everything (git add -A). Simple, but in a simultaneous "
                            "closeout your commit may contain the other agent's files.")
    group.add_argument("--paths", nargs="+", metavar="PATH",
                       help="stage and commit only these paths. Keeps attribution exact.")
    parser.add_argument("--timeout", type=int, default=600,
                        help="seconds to wait for the closeout lock (default 600)")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    root = repo_root()
    lock_path = os.path.join(root, LOCK_NAME)

    if not acquire(lock_path, args.agent, args.timeout):
        return LOCK_BUSY
    try:
        return run_closeout(root, args)
    finally:
        try:
            os.remove(lock_path)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
