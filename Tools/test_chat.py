#!/usr/bin/env python3
"""Tests for chat.py. Run before changing it; run again after.

    python -B Tools/test_chat.py

Optional historical controls can be supplied with `--old <legacy-chat.py>` and
`--post-old <legacy-chat.py>`. The default suite is self-contained and does
not require either snapshot. A supplied snapshot that does not contain the
named defect fails honestly.

Everything runs against throwaway copies in a temp directory. This file never
touches a real transcript, and the inbox tests use chat.py's `--root` override
so no state is written into the live repository.

Sections:
  A. The three verification defects Codex found on review, or that fall out of
     the same mistake he identified: judging an append by a property of the
     whole file.
  B. Regression: every guarantee the tool made before still holds.
  C. The inbox checkpoint and the bounded wait.
  D. Truncation recovery copy and end-of-inbox sentinel.
  E. The `post` checkpoint trap.
"""
import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
NEW = os.path.join(HERE, "chat.py")

# Historical controls authenticate normalized LF bytes so a normal Windows
# CRLF materialization of the same Git blob still passes, while a different
# script cannot masquerade as the defect-era control.
OLD_SHA256 = "5f29eaea5966dbb6c00b7df08aa2b7ee43a0757adff80c78636e9443fa893ebb"
POST_OLD_SHA256 = "286ef79c61027c7a0d424ebcca200b4db61daa96fb83721ee12ee52ca01ecab6"

parser = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--old", default=None,
                    help="legacy chat.py for the section A verification controls")
parser.add_argument("--post-old", default=None,
                    help="legacy chat.py for the section E checkpoint control")
ARGS = parser.parse_args()
OLD = os.path.abspath(ARGS.old) if ARGS.old else None
POST_OLD = os.path.abspath(ARGS.post_old) if ARGS.post_old else None

WORK = tempfile.mkdtemp(prefix="chattest-")
PASS, FAIL = [], []
OUTCOMES = []       # ordered (name, passed) -- see the SUITE IDENTITY line


def run(script, *args):
    p = subprocess.run([sys.executable, script] + list(args), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    return p.returncode, (p.stdout or "") + (p.stderr or "")


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    OUTCOMES.append((name, bool(condition)))
    print("  %s %s%s" % ("PASS" if condition else "FAIL", name,
                         ("  <- " + detail) if detail and not condition else ""))


def body(path, text):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


def make(path, text, eol="\n", trailing=True):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text.replace("\n", eol)
    if trailing and not data.endswith(eol):
        data += eol
    if not trailing:
        data = data.rstrip("\r\n")
    with open(path, "wb") as fh:
        fh.write(data.encode("utf-8"))
    return path


def raw(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    return path


def size(path):
    return os.path.getsize(path)


def counts(path):
    with open(path, "rb") as fh:
        d = fh.read()
    crlf = d.count(b"\r\n")
    return crlf, d.count(b"\n") - crlf, d.count(b"\r") - crlf


def snapshot_runs(script, expected_sha256):
    """True only for the named, runnable historical chat.py snapshot.

    Every historical control below reads a defect off a FAILURE of the old code:
    a non-zero exit, a specific complaint, or -- worst of all -- a message that
    never arrived. A snapshot that does not execute produces all three. So "the
    defect reproduced" and "nothing ran" are the same observation unless
    something separates them, and this is that something.

    Measured 2026-08-10: with `--post-old` pointed at a missing file this suite
    reported 35/35 and exit 0, and an empty file did the same. The control that
    exists to enforce *a fix nobody watched fail is not evidence* was itself
    passing without evidence. `--old` was partly shielded by having three checks
    where two demand specific output, but one of its three tests `rc == 2`
    alone -- and Python's own "can't open file" status is 2.

    The degenerate input is not exotic. The documented reproduction redirects
    `git show` into a file, the redirect creates that file whether or not the
    command succeeded, and neither commit exists in this repository's history.

    Merely proving that *some* runnable chat.py supports `check` is insufficient:
    `191500d` is runnable but has no `inbox`, and used to pass as `--post-old`
    because every scenario return code was discarded.  Bind the flag to the
    normalized Git-blob digest first, then use `check` as the positive execution
    control.  CRLF is normalized to LF so ordinary Windows materialization does
    not change the identity of the source snapshot.
    """
    try:
        data = open(script, "rb").read().replace(b"\r\n", b"\n")
    except OSError:
        return False
    if hashlib.sha256(data).hexdigest() != expected_sha256:
        return False
    probe = make(os.path.join(WORK, "snapshot-runs-probe.md"), "# T\n\nseed\n")
    rc, out = run(script, "check", probe)
    return rc == 0 and "pass this to --expect-bytes" in out


# ---------------------------------------------------------------- section A

print("\nA. Verification defects: judging an append by a whole-file property")
print("-" * 72)
if not OLD:
    print("  (--old not given; proving only that the current code is correct)")
else:
    check("the --old snapshot actually ran, so its failures below mean something",
          snapshot_runs(OLD, OLD_SHA256),
          "not the normalized 191500d chat.py blob, or it could not run")

# Defect 1 -- the mandated header has minute precision, so two legitimate posts
# by the same agent in the same minute are byte-identical. A whole-file count
# reads 2 and calls a correct append a failure.
for label, script in [(l, s) for l, s in (("OLD", OLD), ("NEW", NEW)) if s]:
    f = make(os.path.join(WORK, "dup-%s.md" % label), "# T\n\nseed\n")
    rc1, _ = run(script, "post", f, "--agent", "Claude", "--session", "9", "--body-file",
                 body(os.path.join(WORK, "b1.md"), "first message"),
                 "--expect-bytes", str(size(f)))
    rc2, out2 = run(script, "post", f, "--agent", "Claude", "--session", "9", "--body-file",
                    body(os.path.join(WORK, "b2.md"), "second message, same minute"),
                    "--expect-bytes", str(size(f)))
    if label == "OLD":
        check("two same-minute posts: OLD falsely reports 'header appears 2 times'",
              rc2 == 2 and "appears 2 times" in out2, "rc=%s" % rc2)
    else:
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        check("two same-minute posts both verify, and both bodies are present",
              rc1 == 0 and rc2 == 0 and "first message" in t and "second message" in t,
              "rc1=%s rc2=%s" % (rc1, rc2))

# Defect 2 -- str.index returns a CHARACTER offset and it was compared against a
# BYTE length. Every multibyte character in earlier messages widens the gap, so
# on real prose the check inverts. Codex hit this on his first real post.
PROSE = "# T\n\n**Human:**\n\n" + ("An em dash - no, an em dash — and a curly “quote”. " * 60) + "\n"
for label, script in [(l, s) for l, s in (("OLD", OLD), ("NEW", NEW)) if s]:
    f = make(os.path.join(WORK, "utf8-%s.md" % label), PROSE)
    rc, out = run(script, "post", f, "--agent", "Codex", "--session", "3", "--body-file",
                  body(os.path.join(WORK, "b3.md"), "reply after multibyte prose"),
                  "--expect-bytes", str(size(f)))
    if label == "OLD":
        check("append after multibyte prose: OLD falsely reports 'landed before EOF'",
              rc == 2 and "landed before" in out, "rc=%s" % rc)
    else:
        check("append after multibyte prose verifies clean", rc == 0, "rc=%s out=%s" % (rc, out[:200]))

# Defect 3 -- the same mistake, third instance. A CRLF transcript that already
# contains a bare LF (what a hand edit in the wrong editor leaves behind) made
# the next appender fail, though the appender did not cause it. A check that
# blames the innocent is a check agents learn to ignore.
DAMAGED = b"# T\r\n\r\nA human typed this\r\nand this line ends bare\nthen back to normal\r\n"
for label, script in [(l, s) for l, s in (("OLD", OLD), ("NEW", NEW)) if s]:
    f = raw(os.path.join(WORK, "mixed-%s.md" % label), DAMAGED)
    rc, out = run(script, "post", f, "--agent", "Claude", "--session", "4", "--body-file",
                  body(os.path.join(WORK, "b4.md"), "innocent append"),
                  "--expect-bytes", str(size(f)))
    if label == "OLD":
        check("pre-existing mixed endings: OLD blames the next writer",
              rc == 2, "rc=%s" % rc)
    else:
        check("pre-existing mixed endings are a note, not this post's failure",
              rc == 0 and "note" in out, "rc=%s out=%s" % (rc, out[:200]))

# The delta check must still catch damage this append really does cause.
f = raw(os.path.join(WORK, "guard.md"), b"# T\r\n\r\nclean crlf\r\n")
rc, out = run(NEW, "post", f, "--agent", "Claude", "--session", "4", "--body-file",
              body(os.path.join(WORK, "b4b.md"), "clean"), "--expect-bytes", str(size(f)))
_, bare_lf, bare_cr = counts(f)
check("relaxing that check did not stop the tool from keeping CRLF pure",
      rc == 0 and bare_lf == 0 and bare_cr == 0, "rc=%s bare_lf=%d" % (rc, bare_lf))

# ---------------------------------------------------------------- section B

print("\nB. Regression: the original guarantees still hold")
print("-" * 72)

reply = body(os.path.join(WORK, "b5.md"), "a reply with an em dash — here")

f = make(os.path.join(WORK, "crlf.md"), "# T\n\nseed\n", eol="\r\n")
rc, _ = run(NEW, "post", f, "--agent", "Claude", "--session", "4",
            "--body-file", reply, "--expect-bytes", str(size(f)))
crlf, bare_lf, bare_cr = counts(f)
check("CRLF transcript stays pure CRLF", rc == 0 and bare_lf == 0 and bare_cr == 0,
      "rc=%s bare_lf=%d bare_cr=%d" % (rc, bare_lf, bare_cr))

f = make(os.path.join(WORK, "lf.md"), "# T\n\nseed\n")
rc, _ = run(NEW, "post", f, "--agent", "Claude", "--session", "4",
            "--body-file", reply, "--expect-bytes", str(size(f)))
crlf, _, bare_cr = counts(f)
check("LF transcript gains zero CR", rc == 0 and crlf == 0 and bare_cr == 0,
      "rc=%s crlf=%d bare_cr=%d" % (rc, crlf, bare_cr))

f = make(os.path.join(WORK, "stale.md"), "# T\n\nseed\n")
run(NEW, "post", f, "--agent", "Codex", "--session", "3", "--body-file",
    body(os.path.join(WORK, "b6.md"), "arrived while you were composing"),
    "--expect-bytes", str(size(f)))
rc, out = run(NEW, "post", f, "--agent", "Claude", "--session", "4",
              "--body-file", reply, "--expect-bytes", "20")
check("stale post refused, and the refusal shows what arrived",
      rc == 1 and "REFUSED" in out and "arrived while you were composing" in out, "rc=%s" % rc)

f = make(os.path.join(WORK, "notrail.md"), "# T\n\nA human's last sentence", trailing=False)
rc, _ = run(NEW, "post", f, "--agent", "Claude", "--session", "4",
            "--body-file", reply, "--expect-bytes", str(size(f)))
with open(f, encoding="utf-8") as fh:
    lines = fh.read().split("\n")
check("missing trailing newline repaired; nothing welded onto the last line",
      rc == 0 and "A human's last sentence" in lines, "rc=%s" % rc)

f = make(os.path.join(WORK, "race.md"), "# T\n\nseed\n")
n = size(f)
procs = [subprocess.Popen(
    [sys.executable, NEW, "post", f, "--agent", "Claude", "--session", str(i), "--body-file",
     body(os.path.join(WORK, "race%d.md" % i), "concurrent writer %d" % i),
     "--expect-bytes", str(n)],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) for i in range(8)]
rcs = [p.wait() for p in procs]
with open(f, encoding="utf-8") as fh:
    t = fh.read()
landed = sum(1 for i in range(8) if "concurrent writer %d" % i in t)
check("8 racing writers on one stale count: exactly 1 posts, 7 refused",
      rcs.count(0) == 1 and rcs.count(1) == 7 and landed == 1, "rcs=%s landed=%d" % (rcs, landed))
check("racing writers destroyed nothing", "seed" in t)

# ---------------------------------------------------------------- section C

print("\nC. Inbox checkpoint and bounded wait")
print("-" * 72)

FAKE = os.path.join(WORK, "repo")
mine = os.path.join(FAKE, "chats", "Claude-Codex-Human", "Subject A", "Subject A - Active.md")
other = os.path.join(FAKE, "chats", "Codex-Human", "Subject B", "Subject B - Active.md")
old = os.path.join(FAKE, "chats", "Claude-Codex-Human", "Old", "Old - Concluded.md")
make(mine, "# A\n\nseed\n")
make(other, "# B\n\nnot Claude's channel\n")
make(old, "# Old\n\nconcluded\n")

rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("first inbox reports no checkpoint rather than inventing a diff",
      rc == 0 and "NO CHECKPOINT YET" in out and "Subject A" in out, "rc=%s" % rc)
check("inbox ignores channels that do not name the agent", "Subject B" not in out)
check("inbox ignores concluded transcripts", "Old - Concluded" not in out)

rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("an unchanged inbox says so plainly", rc == 0 and "Nothing new" in out, "rc=%s" % rc)

run(NEW, "post", mine, "--agent", "Codex", "--session", "4", "--body-file",
    body(os.path.join(WORK, "b7.md"), "Codex reply arriving mid-session"),
    "--expect-bytes", str(size(mine)), "--root", FAKE)
rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("inbox prints exactly what arrived since the checkpoint, and no more",
      rc == 0 and "Codex reply arriving mid-session" in out
      and "seed" not in out.split("NEW IN")[-1], "rc=%s" % rc)

rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("inbox advances, so one message is never reported twice",
      "Codex reply arriving mid-session" not in out)

run(NEW, "post", mine, "--agent", "Claude", "--session", "4", "--body-file",
    body(os.path.join(WORK, "b8.md"), "my own message"),
    "--expect-bytes", str(size(mine)), "--root", FAKE)
rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("my own post does not come back to me as unread mail",
      "my own message" not in out and "Nothing new" in out)

rc, out = run(NEW, "inbox", "--agent", "Codex", "--root", FAKE)
check("state is per agent: Codex's inbox is independent of Claude's",
      "NO CHECKPOINT YET" in out and "Subject A" in out)

with open(mine, "rb") as fh:
    data = fh.read()
raw(mine, data[:40] + b"\nsomeone rewrote this file\n")
rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("a rewritten transcript is reported, and the checkpoint does not advance",
      rc == 1 and "REWRITTEN" in out, "rc=%s" % rc)
rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE)
check("it keeps warning until a person actually looks", rc == 1 and "REWRITTEN" in out,
      "rc=%s" % rc)

FAKE2 = os.path.join(WORK, "repo2")
m2 = os.path.join(FAKE2, "chats", "Claude-Codex", "S", "S - Active.md")
make(m2, "# S\n\nseed\n")
rc, out = run(NEW, "inbox", "--agent", "Claude", "--mark", "--root", FAKE2)
check("--mark records a baseline without printing the transcript",
      rc == 0 and "Marked 1" in out and "seed" not in out, "rc=%s" % rc)

t0 = time.time()
rc, out = run(NEW, "wait", "--agent", "Claude", "--timeout", "4", "--interval", "1", "--root", FAKE2)
elapsed = time.time() - t0
check("wait times out cleanly and refuses to call silence an answer",
      rc == 3 and "Nothing arrived" in out and 3 <= elapsed < 15,
      "rc=%s elapsed=%.1f" % (rc, elapsed))


def delayed_post():
    time.sleep(2)
    run(NEW, "post", m2, "--agent", "Codex", "--session", "5", "--body-file",
        body(os.path.join(WORK, "b9.md"), "late arrival during wait"),
        "--expect-bytes", str(size(m2)), "--root", FAKE2)


threading.Thread(target=delayed_post, daemon=True).start()
t0 = time.time()
rc, out = run(NEW, "wait", "--agent", "Claude", "--timeout", "900", "--interval", "1", "--root", FAKE2)
elapsed = time.time() - t0
check("wait returns as soon as a reply lands, well inside its window",
      rc == 0 and "Waiting up to 900s" in out and "late arrival during wait" in out and elapsed < 20,
      "rc=%s elapsed=%.1f" % (rc, elapsed))

# ---------------------------------------- D — truncation recovery (2026-08-08)
#
# `inbox` displays and consumes in one step, so the printed report is the only
# copy of the new bytes. On 2026-08-08 `inbox | head -80` marked two
# transcripts read that were never displayed: the output fitted the pipe
# buffer, so nothing raised, nothing failed, and the state file advanced
# normally. These checks cover the recovery copy and the sentinel that makes
# the truncation visible in the first place.

FAKE3 = os.path.join(WORK, "repo3")
m3 = os.path.join(FAKE3, "chats", "Claude-Codex", "T", "T - Active.md")
make(m3, "# T\n\nseed\n")
run(NEW, "inbox", "--agent", "Claude", "--mark", "--root", FAKE3)

SECRET = "a message that must survive being truncated away"
run(NEW, "post", m3, "--agent", "Codex", "--session", "6", "--body-file",
    body(os.path.join(WORK, "b10.md"), SECRET),
    "--expect-bytes", str(size(m3)), "--root", FAKE3)

rc, out = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE3)
check("a consuming inbox ends with a sentinel, so a cut-off reader can tell",
      rc == 0 and out.rstrip().endswith("===") and "END OF INBOX" in out, "rc=%s" % rc)
check("the sentinel counts what was consumed", "END OF INBOX (1 new" in out)

recovery = os.path.join(FAKE3, "Tools", ".state", "last-inbox-claude.txt")
check("the report names its own recovery copy", "last-inbox-claude.txt" in out)
check("the recovery copy exists on disk", os.path.exists(recovery), recovery)
with open(recovery, "r", encoding="utf-8") as fh:
    saved = fh.read()
check("the recovery copy holds the bytes that were marked read", SECRET in saved)

# The real failure: the checkpoint has advanced, so the transcript will never
# report this message again. Without the recovery copy it would be gone.
rc, out2 = run(NEW, "inbox", "--agent", "Claude", "--root", FAKE3)
check("the message is genuinely unrecoverable from inbox after one read",
      SECRET not in out2 and "Nothing new" in out2)
check("...but is still recoverable from the file, which is the whole point",
      SECRET in open(recovery, encoding="utf-8").read())

# An unchanged inbox consumes nothing, so it must not overwrite the copy that
# still holds unread mail -- otherwise a routine mid-session check destroys it.
check("an inbox that consumed nothing leaves the previous recovery copy intact",
      SECRET in open(recovery, encoding="utf-8").read())

# ------------------------------------------ E — the `post` trap (2026-08-09)
#
# Worse than the truncation defect above, because nothing has to go wrong for
# it to fire. `post` advanced the poster's own checkpoint to the new end of
# file under the comment "We wrote it, so we have seen it." That premise is
# false: writing proves you have seen YOUR bytes and whatever you read at
# `check` time, not bytes the other agent appended in between.
#
# It fired in the incubator on 2026-08-09 and consumed a same-state approval.
# --expect-bytes cannot catch it: that proves the COUNT was current, not that
# the poster READ what the count covers, and `check` is exactly the command
# that hands you a current count with only a 400-byte tail.

print("\nE. The `post` checkpoint trap")
print("-" * 72)

APPROVAL = "I-APPROVE-THIS-MESSAGE-MUST-NOT-BE-LOST"


def post_trap_scenario(script, tag):
    """Codex posts while Claude composes; Claude posts on a current-but-unread
    count. Returns (survived, claude_post_output, scenario_valid, detail).

    `survived == False` means evidence of notification loss only when every
    command succeeded and both messages physically reached the transcript.
    Otherwise it means the scenario never ran, which is not evidence of the
    historical defect.
    """
    repo = os.path.join(WORK, "trap-%s" % tag)
    f = os.path.join(repo, "chats", "Claude-Codex", "S", "S - Active.md")
    make(f, "# S\n\nseed\n")
    # Claude actually reads the inbox, establishing a real checkpoint.
    inbox0_rc, _ = run(script, "inbox", "--agent", "Claude", "--root", repo)
    # Codex appends the message that must survive.
    codex_rc, _ = run(
        script, "post", f, "--agent", "Codex", "--session", "26", "--body-file",
        body(os.path.join(WORK, "trap-%s-codex.md" % tag), APPROVAL),
        "--expect-bytes", str(size(f)), "--root", repo)
    # Claude posts against the fresh count without ever reading those bytes.
    claude_rc, posted = run(
        script, "post", f, "--agent", "Claude", "--session", "25", "--body-file",
        body(os.path.join(WORK, "trap-%s-claude.md" % tag), "my reply"),
        "--expect-bytes", str(size(f)), "--root", repo)
    inbox1_rc, seen = run(script, "inbox", "--agent", "Claude", "--root", repo)
    try:
        transcript = open(f, encoding="utf-8").read()
    except OSError:
        transcript = ""
    scenario_valid = (
        inbox0_rc == codex_rc == claude_rc == inbox1_rc == 0
        and APPROVAL in transcript
        and "my reply" in transcript
    )
    detail = "rcs=%s approval_appended=%s reply_appended=%s" % (
        (inbox0_rc, codex_rc, claude_rc, inbox1_rc),
        APPROVAL in transcript,
        "my reply" in transcript,
    )
    return APPROVAL in seen, posted, scenario_valid, detail


if POST_OLD:
    # This check must come FIRST and must gate the one below it. Without it,
    # "the old code ate the message" and "the old code never started" are the
    # same observation, and the second one passes.
    post_old_ran = snapshot_runs(POST_OLD, POST_OLD_SHA256)
    check("the --post-old snapshot actually ran, so its silence means something",
          post_old_ran,
          "not the normalized 25b2e6a chat.py blob, or it could not run")
    survived_old, _, old_scenario_valid, old_detail = post_trap_scenario(
        POST_OLD, "old")
    check("the --post-old scenario completed before its silence was interpreted",
          post_old_ran and old_scenario_valid, old_detail)
    check("--post-old really did consume a message the agent never read",
          post_old_ran and old_scenario_valid and not survived_old,
          "the defect did not reproduce, so the fix proves nothing")

survived, posted_out, new_scenario_valid, new_detail = post_trap_scenario(NEW, "new")
check("a post on a current-but-unread count no longer consumes the other "
      "agent's message", new_scenario_valid and survived, new_detail)
check("and `post` says so at the time, rather than failing silently",
      new_scenario_valid and "UNREAD" in posted_out,
      new_detail + " " + posted_out.strip()[-200:])

# The other half of correctness: this must not degrade into "never advance".
# If the agent HAS read everything, posting still advances, so a routine inbox
# does not re-show the agent its own message forever.
repo_ok = os.path.join(WORK, "trap-clean")
f_ok = os.path.join(repo_ok, "chats", "Claude-Codex", "S", "S - Active.md")
make(f_ok, "# S\n\nseed\n")
run(NEW, "inbox", "--agent", "Claude", "--root", repo_ok)
_, clean_post = run(NEW, "post", f_ok, "--agent", "Claude", "--session", "25",
                    "--body-file", body(os.path.join(WORK, "clean.md"), "my own message"),
                    "--expect-bytes", str(size(f_ok)), "--root", repo_ok)
_, after_clean = run(NEW, "inbox", "--agent", "Claude", "--root", repo_ok)
check("posting with nothing unread still advances the checkpoint",
      "Nothing new" in after_clean and "UNREAD" not in clean_post)

# ------------------------------------------------------------------ summary

print("\n" + "=" * 72)
print("PASSED %d   FAILED %d" % (len(PASS), len(FAIL)))
for name in FAIL:
    print("  FAILED: %s" % name)
print("SUITE IDENTITY  %s" % hashlib.sha256(
    "\n".join("%s|%s" % ("PASS" if ok else "FAIL", name)
              for name, ok in OUTCOMES).encode("utf-8")).hexdigest())
shutil.rmtree(WORK, ignore_errors=True)
sys.exit(1 if FAIL else 0)
