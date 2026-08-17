# Coordination tools

This template includes two standard-library Python programs for the shared surfaces that are unsafe to manage by convention alone:

- `chat.py` appends to shared transcripts and maintains per-agent inbox checkpoints.
- `closeout.py` stages, commits, and pushes an exact path set under a repository-local lock.

They need Python 3 and Git; there is no package installation, bundled credential, account configuration, or service dependency. `closeout.py` uses the network only through the repository's configured `git push`.

These programs provide mechanics, not authority. A successful command never substitutes for a work claim, same-state review, human approval, or any project-specific gate.

## Safe chat operations

`chat.py` is the supported way to inspect and append active transcripts. It resolves the project root from the nearest ancestor `AgentPrompt.md`, discovers active transcripts under `chats/`, and keeps local read markers in `Tools/.state/`.

### Read before composing

```shell
python -B Tools/chat.py check "chats/<channel>/<subject>/<subject> - Active.md"
```

`check` prints the raw byte count, a short SHA-256, line-ending measurements, and the last 400 bytes. Read the complete transcript as well; the tail is collision evidence, not a substitute for context.

### Append one message

Write only the message body to a separate UTF-8 file, then use the byte count returned by `check`:

```shell
python -B Tools/chat.py post "chats/<channel>/<subject>/<subject> - Active.md" \
  --agent Claude --session 4 \
  --body-file "<message-body.md>" \
  --expect-bytes 5728
```

The tool:

1. refuses if the transcript's byte count changed;
2. shows bytes that arrived while the reply was being composed;
3. appends in one binary write while preserving the existing line endings;
4. uses the real local time for the message header; and
5. verifies that the previous bytes survived and that its exact block occupies the old end of file.

There is deliberately no automatic retry. After a stale-state refusal, read the new content and decide whether the draft still belongs in the conversation.

### Verify an existing transcript

```shell
python -B Tools/chat.py verify "chats/<channel>/<subject>/<subject> - Active.md"
```

This checks UTF-8 decoding, line endings, trailing newline, replacement characters, and message headers without rewriting the file.

### Check the inbox

```shell
python -B Tools/chat.py inbox --agent Claude
```

The first run establishes a baseline for every participant-matching active transcript. Later runs print exactly what was appended after the saved checkpoint. A shortened or rewritten transcript is reported and is not marked read.

`inbox` displays and consumes in one operation. Do not pipe it through a truncating viewer. Whenever content is consumed, a full recovery copy is written to `Tools/.state/last-inbox-<agent>.txt`, and the last line is an `=== END OF INBOX (...) ===` sentinel. If that sentinel is missing from the visible output, open the recovery copy.

### Wait for an identified reply

```shell
python -B Tools/chat.py wait --agent Claude --timeout 180
```

`wait` polls the inbox and returns when content arrives. It is capped at 900 seconds. A timeout returns exit code `3` and means only that nothing arrived in the window; it is never approval, rejection, or a blocker by itself.

### Chat exit codes

| Code | Meaning |
|---:|---|
| `0` | command completed and any append was verified |
| `1` | refused input, stale state, or integrity problem |
| `2` | bytes were appended but post-verification failed; inspect before any retry |
| `3` | bounded wait ended with nothing new |

## Path-scoped Git closeout

`closeout.py` resolves the repository from Git's own top level. It serializes the complete stage/commit/push sequence with `.closeout-session.lock` and uses explicit pathspecs so one agent does not adopt another writer's files.

Preview first:

```shell
python -B Tools/closeout.py --agent Claude --session 4 --dry-run \
  --paths "Work/Active/example.md" "agents/Claude"
```

Then run the same exact set without `--dry-run`:

```shell
python -B Tools/closeout.py --agent Claude --session 4 \
  --paths "Work/Active/example.md" "agents/Claude"
```

For a moved path, pass both the tracked source and destination. A detected rename with only one selected endpoint refuses before commit.

`--all` remains available:

```shell
python -B Tools/closeout.py --agent Claude --session 4 --all
```

Use it only after establishing that the session is the sole writer and reviewing the entire worktree. It intentionally stages everything and can therefore adopt unrelated work visible on disk.

### Closeout safety boundary

The tool:

- stages into a scratch copy of the index during `--dry-run`, leaving the real index untouched;
- removes its live lock from the intended commit even if `.gitignore` is misconfigured;
- refuses a one-sided move;
- never breaks a lock automatically;
- never force-pushes, amends, rebases, merges, resets history, or resolves conflicts; and
- stops on remote divergence, leaving the local and remote commits separate for explicit inspection and coordination.

If the lock holder is gone, the program diagnoses a probably stale lock but does not delete it. Confirm no other Git operation is active before manually deleting the exact `.closeout-session.lock` it names.

A successful closeout still requires explicit verification of local `HEAD`, the remote-tracking state, and the live remote. Git success is not proof that the intended review or publication gate was satisfied.

### Closeout exit codes

| Code | Meaning |
|---:|---|
| `0` | preview completed, or commit/push completed |
| `1` | refused or failed; inspect the printed repository state |
| `4` | closeout lock remained busy until the bounded timeout |

## Tests

Both suites operate only on temporary files and throwaway Git repositories:

```shell
python -B Tools/test_chat.py
python -B Tools/test_closeout.py
```

The chat suite covers stale-state refusal, timestamp validation, line-ending preservation, simultaneous append behavior, checkpoint isolation and recovery, transcript discovery, rewrite detection, bounded wait, and the unread-message checkpoint trap.

The closeout suite first reproduces the raw concurrent-Git failures, then covers serialized exact attribution, path-scoped staging, scratch-index dry runs, lock refusal and release, one-sided and two-sided moves, recovery from a half-committed move, and fail-closed remote divergence.

Run the complete relevant suite after every change to either program or its tests. A passing suite proves only the tested mechanics on that candidate state.
