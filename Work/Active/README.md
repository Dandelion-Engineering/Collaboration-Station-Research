# Active Work Records

`Work/Active/` is the project's visible coordination state. Before changing a shared project file, open or adopt one record here that names one lead and the exact paths or disjoint regions that lead may write.

**This `README.md` is scaffolding, not an active claim.** When checking the live work set, inspect the other Markdown files in this folder.

## The claim rule

- **One lead owns the declared write scope.** A reviewer or collaborator may read it but does not edit it unless the record first transfers the lead.
- **Read-only inspection needs no claim.** Claims coordinate writes; they do not reserve subjects, ideas, or files merely being read.
- **Chat transcripts are the sole append-only exception.** Participants post through `Tools/chat.py`; no lead owns a conversation.
- **Two live claims may not overlap.** The agents compare every proposed path or declared region with the active records and resolve an overlap in chat before either agent writes.
- **A claim grants no wider authority.** It does not permit a gated scientific run, external resource, publication, credential use, spend, or director-only action.

Name a record for the work, not for the agent. Keep its next ready unit small enough that a future session can tell what to do without reconstructing the plan.

When the objective is complete, update the record with the outcome and move it to `Work/Done/`. When the work is abandoned, record why and move it to `Work/Dropped/`. Do not delete the record; Git and the terminal folder preserve the decision trail.

## Compact record template

Copy the block below into `Work/Active/<short-work-name>.md` and replace every placeholder.

```markdown
# <work name>

**Lead:** <agent>
**Reviewer / collaborator:** <agent or none>
**Opened:** <YYYY-MM-DD HH:MM TZ>
**State:** <claimed | building | review | waiting>

**Next ready unit:** <one concrete bounded action, or the exact condition being awaited and where its answer will appear>

## Purpose

<What this work makes possible, and what is worse without it.>

## Exact write scope

- `<path>` — <entire file, or an exact disjoint region named by stable headings or boundaries>

## Acceptance

1. <Durable property this work must satisfy.>

## Explicit non-goals

- <Nearby work, authority, resource, or path this claim does not reach.>

## Current state and evidence

<What is true now, what was measured, and any handoff or review identity.>
```

Do not leave a placeholder in a live record. If the write boundary cannot be stated precisely enough to compare with another claim, it is not ready to open.
