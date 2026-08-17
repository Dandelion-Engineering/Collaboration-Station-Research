# Review Cycle Playbook

**Use whenever an artifact is handed for review, and when responding after an artifact you own has been reviewed — the bounded loop that brings a candidate to a single state both agents explicitly approve, or to an honest terminal state that says what was not agreed.**

**Required inputs:**
- The candidate artifact, at a state that is not moving while it is read.
- A **Review Card** for it, in `Review Cards/`. The card is created before the first round, not after. `Review Cards/README.md` is how to write one.
- The chat that belongs to the review, where every round and every verdict is recorded.

**Output:**
- One candidate state that **both** agents have **explicitly** approved — or one of the two withholding terminal states, which are outcomes rather than failures.

**Applies these shared standards:** the append-never-overwrite discipline of the chat logs; and the **Standards** section of `Project Details/Project Details.md` — the reviewer reads the artifact against those, and they are the bar a finding is argued from. Where a project has relaxed one of them, the relaxation is named in the Claim Sheet, and a card that ignores a named relaxation is reviewing against a standard this project does not hold.

---

## Purpose

Two agents produce work the other has to be able to trust without redoing it. This playbook is how that trust is earned on a specific artifact, and it is built around one non-negotiable idea:

> **Approval is always explicit, and always about one exact candidate state.** An edit is not approval. A handoff is not approval. Downstream use is not approval. Silence and a timeout are never approval. The loop closes only when both agents have named **the same** state in the chat and approved it.

The second idea is that a review has to **end**. An unbounded loop is not more rigorous than a bounded one; it is a way for a disagreement to consume a project without ever being decided. So this cycle is capped, and when the cap is reached in disagreement, the contested thing is **withheld** rather than argued into the artifact. **Withholding is a real outcome and it is fail-closed by design** — the honest state is the one where the disputed capability does not ship and the record says why.

## The Review Card comes first

**Before the first round, the owner completes co-design and creates a stable card.** A review of a candidate nobody has pinned down is a conversation, not a review — the reviewer cannot say what they read, and no later approval can name a state.

The card names, at minimum:

- **the owner, the reviewer, the subject chat, the candidate's purpose,** and the **exact artifacts and sections** in scope;
- **full identity for every path** — the Git blob identity where the file is tracked, plus the raw SHA-256, the physical byte count, and the LF and CR counts, together with the baseline or superseded state it replaces;
- **the durable acceptance properties** the candidate must satisfy, and the **runnable evidence** used for this state;
- **what counts as blocking**, the **explicit exclusions**, the **downstream gates** this review does not open, and any **scientific or external resource not authorised** for it;
- **the owner's own adversarial evidence** — boundary cases, refusal cases, mutation or counterexample probes where proportionate, and confirmation that each passing check is owed to the guard it is supposed to be testing rather than passing for an unrelated reason.

**That last item is the one most worth the owner's time.** A green result nobody tried to break is weak evidence, and the reviewer's scarcest resource is attention that could have gone to the parts a probe cannot reach.

**Nothing may be written to the candidate while a round is open.** If the owner changes a byte, the state under review no longer exists and the round restarts against the new identity.

## The rounds

**Round 1 is the only exhaustive pass, and it produces one numbered ledger.**

The reviewer reads the full scope of the card against the acceptance properties and the artifact's own purpose, and returns **every reasonably discoverable finding, numbered**. ⚠️ **The reviewer does not stop at the first blocker.** Stopping early converts one review into an unbounded series of them, which is exactly what the cap exists to prevent — and it spends the owner's next round fixing one thing rather than all of them.

**Later rounds are verification, not re-audit.** A round after the first checks only:

1. the numbered findings from the ledger, and whether each is actually addressed;
2. the regions the owner **declared** changed;
3. the regions the owner claims are unchanged, **checked mechanically** rather than read again — an identity comparison is cheaper and stronger than a second reading;
4. **regressions introduced by the response itself.**

⚠️ **An unchanged statement that a repair made false is a regression**, and it belongs in the round. It is not a licence to reopen the full scope. **The distinction is the whole economy of this method:** the response gets checked, the parts nobody touched do not get re-read.

## What a reviewer may change, and what returns as a finding

**A reviewer may directly apply only unambiguously mechanical corrections that cannot change any consumer's behaviour** — a typo, a broken link, a misnumbered list, a wrong path in a comment.

**Everything else returns as a finding or a proposed patch for the owner:** anything scientific, architectural, interpretive, or about permissions or governance. A reviewer who wants to make such a change asks for **explicit ownership transfer** first; the new owner then authenticates and approves the edited state, and the former owner genuinely re-reads it as reviewer.

**Why the line sits there.** A reviewer editing substance is no longer a check — the artifact ends up with one mind on it and a second signature, which is the appearance of review without the thing itself.

## Closing, and the cap

**Ordinary review has at most three owner-reviewer round-trips**, and closes as exactly one of:

| Verdict | What it means |
|---|---|
| `Approved` | Both agents named the same state and approved it. Nothing outstanding. |
| `Approved with Follow-ups` | Approved, with non-blocking residue recorded in the card so it closes visibly rather than being rediscovered later. |
| `Revisions Required` | Not approved. The ledger says what has to change. |
| `Split/Redesign Required` | The candidate is the wrong shape; it does not converge by revision. |

**Non-blocking residue belongs in `Approved with Follow-ups`.** It is recorded, it is not applied under the approval, and applying it later produces a new state that takes an ordinary review — an approval names bytes the reviewer actually read, and it never reaches bytes written afterwards.

### A blocker found late

**A pre-existing, purpose-invalidating blocker discovered after Round 1 is labelled `LATE-BLOCKER`, together with why Round 1 missed it.** The label is not a reprimand; it is the only way the method learns where its exhaustive pass is weak.

**A second late blocker, or any new blocker after Round 2, enters convergence** rather than spending another ordinary round.

## Convergence, when the cap is reached in disagreement

**Classify the residual in the same turn the cap is reached** — not in a further round of argument about what kind of disagreement it is.

**If it is a dispute about a fact:** run **one precommitted decisive probe**. Both agents state, before it runs, what each possible result means for their position, so the outcome maps onto both stated positions rather than being reinterpreted afterwards. The probe spends **no unauthorised resource**. ⚠️ **An inconclusive probe does not get a second probe — it becomes a judgment dispute** and follows the next paragraph.

**If it is a dispute of judgment:** one **exact-state narrowing split** is permitted, carrying both positions, followed by **one focused round-trip**. **No recursive split.**

**If that still does not converge, the contested thing is withheld:**

- **`Approved — Contested Element Withheld`** — the candidate ships without the contested capability, permission, or prose.
- **`Withheld — Contested Candidate Not Adopted`** — used when the contested element cannot be separated coherently, so the candidate does not ship at all.

**Any later reinstatement of a withheld element is a new candidate with a new card**, and it starts at Round 1. It does not resume the review that withheld it.

## An out-of-card repair is a proposed scope expansion

**Never a silent widen.** When the owner finds something wrong outside the card while responding to a round, the owner:

1. **authenticates the added state** and names its baseline, exactly as the card does for everything else;
2. **explains why the card stays bounded** — what the addition does *not* pull in;
3. **offers revert or deferral** as real options rather than presenting the widened candidate as the only one available.

**The reviewer rules on scope before content**, and the ruling is recorded. **Acceptance does not reset the round limit and does not transfer any earlier approval** onto the new bytes. **Rejection restores the baseline** and the repair moves to a card of its own.

## Quality checklist

- [ ] A stable Review Card existed **before** Round 1, with full identity for every path in scope.
- [ ] The card states the acceptance properties, the blocking definition, the exclusions, and the downstream gates it does not open.
- [ ] The owner's adversarial evidence is in the card, and each green is attributed to the guard it tests.
- [ ] Round 1 returned **one numbered ledger** of all reasonably discoverable findings, rather than stopping at the first blocker.
- [ ] Later rounds checked findings, declared changed regions, mechanically-verified unchanged regions, and regressions — and did **not** re-audit untouched scope.
- [ ] Every reviewer edit was unambiguously mechanical, or ownership was explicitly transferred first.
- [ ] The closing state carries **two** explicit approvals naming the **same** identity.
- [ ] No approval was inferred from an edit, a handoff, downstream use, silence, or a timeout.
- [ ] A late blocker was labelled `LATE-BLOCKER` with why it was missed.
- [ ] A capped disagreement was classified and resolved through the ladder, and any withholding is named in the terminal verdict.

## Common failure modes

- **Inferred approval.** Treating an edit, a handoff, downstream use, silence, or a timeout as sign-off. The loop stays open until both approvals name the same identity.
- **Reviewing a moving target.** Bytes changing under an open round. The state under review must be still; if it moved, the round restarts against the new identity.
- **Stopping at the first blocker in Round 1.** It converts a bounded review into an unbounded series and wastes the owner's next round.
- **Re-auditing untouched scope in Round 2.** The unchanged regions are checked mechanically. Reading them again is how a three-round cap becomes a three-round full review.
- **The reviewer rewriting substance.** One mind on the artifact and two signatures on it is the appearance of review, not review.
- **Silent widening.** Fixing something outside the card while responding, and folding it into the same approval. It is a scope expansion and the reviewer rules on it first.
- **Arguing past the cap.** The ladder exists so a disagreement ends in a decision. **Withholding the contested element is a correct outcome** — an unbounded argument is not more rigorous, it is just unbounded.
- **A card written after the fact.** Then it documents what happened instead of bounding what was reviewed, and no approval in it can name a state.
