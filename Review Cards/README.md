# Review Cards

**One card per candidate under review.** The card is what makes a review a review rather than a conversation: it pins the exact bytes, states what the candidate has to satisfy, and says what the review is *not* about. `Playbooks/review-cycle.md` is the procedure; this folder is where its cards live.

**Copy `TEMPLATE.md` and fill it in before the first round.** A card written afterwards documents what happened instead of bounding what was reviewed, and no approval recorded in it can name a state.

---

## What a card is for

**A reviewer's scarcest resource is attention.** A card spends it well by answering, up front, the four questions a reviewer would otherwise have to reconstruct:

1. **Exactly which bytes am I reading?** Not "the technical report" — a path, and an identity that proves the file has not moved since.
2. **What does this have to be true of?** The acceptance properties, so a finding can be argued against a stated standard rather than against taste.
3. **What is out of scope?** So the reviewer neither wastes a round on it nor assumes it was checked.
4. **What did the owner already try to break?** So the reviewer starts where the owner's own probes stopped.

## Naming

`<short-candidate-name>.md`, named for the candidate rather than for the agent who owns it. Ownership is temporary and attaches to the work; a card named after an agent misleads the moment the work changes hands.

A second review of the same artifact after a withholding terminal verdict is a **new candidate with a new card** — suffix it (`-2`, `-3`) rather than reopening the old one. The old card stays exactly as written; it is the record of what was withheld and why.

## Identity, and why it is measured rather than stated

**Every path in scope carries the Git blob identity where the file is tracked, plus the raw SHA-256, the physical byte count, and the LF and CR counts.**

- **The SHA-256 is the thing an approval attaches to.** Both agents recompute it from the file on disk; a reported hash is a claim about a run nobody watched.
- **The byte count catches what a hash comparison alone does not tell you** — namely, how far off you are when it mismatches.
- **The LF and CR counts catch the failure that hashes quietly report as "different file"**: a line-ending change from an editor or a fetch, which alters every byte while changing nothing anyone meant to change. **Measure them before editing, and preserve them.**

**Record the baseline or superseded state as well**, so the card says what this candidate replaces, not only what it is.

## Adversarial evidence is the owner's half of the work

**A passing check nobody tried to break is weak evidence.** The card asks the owner to record boundary cases, refusal cases, and — where proportionate — mutation or counterexample probes: does removing the guard actually reproduce the failure the guard is supposed to prevent?

**Confirm that each green is owed to the intended guard.** A test that would pass with the guard deleted is measuring something else, and finding that out is much cheaper for the owner than for the reviewer.

## Where the verdicts go

**In the review's chat, not in the card**, while the review is open. Writing a verdict into the card produces a new card state, and the reviewer approved the old one — so the record of the approval falsifies the thing it approved.

**When the review closes, the card records the terminal verdict and the identity it names**, together with any `Approved with Follow-ups` residue. That residue is the point of writing it down: it closes visibly, so the next agent neither rediscovers it at full cost nor assumes somebody judged it acceptable.

## Cards are kept

**Nothing is deleted from this folder.** A withheld candidate, a `Split/Redesign Required`, and a review that found nothing are all part of the project's record — and the withholding ones are the most useful, because they are the only durable statement of what the two agents did not agree on.
