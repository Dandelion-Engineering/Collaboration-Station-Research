# Review Card — <candidate name>

**Owner:** <agent>
**Reviewer:** <agent>
**Subject chat:** `chats/<channel>/<subject>/<subject> - Active.md`
**Opened:** <YYYY-MM-DD HH:MM TZ>
**Round:** <1, 2 or 3>
**State:** <awaiting Round 1 | in Round N | closed — see terminal verdict>

## Purpose of this candidate

<One paragraph. What this candidate is for, and what would be worse without it. Not a summary of the diff.>

## Exact artifacts in scope

| Path | Git blob | Raw SHA-256 | Bytes | LF / CR |
|---|---|---|---:|---:|
| `<path>` | `<blob or — if untracked>` | `<64 hex>` | <n> | <n> / <n> |

**Baseline or superseded state:**

| Path | Raw SHA-256 | Bytes | LF / CR |
|---|---|---:|---:|
| `<path>` | `<64 hex>` | <n> | <n> / <n> |

⚠️ **Nothing is written to these paths while a round is open.** If a byte changes, the state under review no longer exists and the round restarts against the new identity.

## Sections in scope

<If the candidate is part of a file, name the sections. If it is whole files, say so explicitly — "entire file" is an answer and an absent answer is not.>

## Durable acceptance properties

<What this candidate must be true of, stated so a finding can be argued against it. Properties that outlive this state, not a checklist of what was done.>

1.
2.
3.

## What counts as blocking

<The severity line for this candidate. Without it, "blocker" means whatever each agent assumed it meant.>

## Explicit exclusions

<What this review does not cover. A reviewer who spends a round here has wasted it; a reader who assumes it was checked has been misled.>

-

## Downstream gates this review does not open

<Approval of these bytes is not approval to publish, push, spend, send, launch, or run anything. Name the gates that still stand.>

-

## Resources not authorised for this review

<Scientific, external, network, compute or paid resources that may not be spent on it. "None" is an answer.>

## Owner-side adversarial evidence

**Runnable evidence for this exact state:**

| What was run | Result | What it proves |
|---|---|---|
| | | |

**Boundary cases:**

**Refusal cases:**

**Mutation or counterexample probes** — *does removing the guard reproduce the failure it exists to prevent?*

**Confirmation that each green is owed to the intended guard:**

<Name any check that would still pass with its guard removed. If there are none, say that you looked.>

## Round ledger

**Round 1 — the exhaustive pass. One numbered ledger, every reasonably discoverable finding, no stopping at the first blocker.**

| # | Finding | Severity | Status |
|---:|---|---|---|
| 1 | | | |

**Round 2 — verification only.** Findings addressed, declared changed regions, unchanged regions checked mechanically, and regressions introduced by the response.

**Round 3 — as Round 2. This is the cap.**

⚠️ **A pre-existing purpose-invalidating blocker found after Round 1 is labelled `LATE-BLOCKER` with why Round 1 missed it.**

## Scope expansions requested

| Date | Added state and its baseline | Why the card stays bounded | Reviewer's ruling |
|---|---|---|---|
| | | | |

## Terminal verdict

**Verdict:** <Approved | Approved with Follow-ups | Revisions Required | Split/Redesign Required | Approved — Contested Element Withheld | Withheld — Contested Candidate Not Adopted>

**Identity approved:** <path + SHA-256 + bytes, for every path — or "none" for a withholding verdict>

**Both approvals name the same state:** <where each one is, in the subject chat>

**Follow-ups, unapplied:** <the non-blocking residue, so it closes visibly. Applying any of it later is a new state and takes an ordinary review.>

**Withheld element, if any, and why:** <what did not ship, and what the disagreement was. Reinstating it is a new candidate and a new card, starting at Round 1.>
