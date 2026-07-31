# Accessible Claim Sheet Playbook

**Use when creating, revising, or reviewing the Accessible Claim Sheet — the director-facing companion to the technical Claim Sheet.**

**Required inputs:**
- The approved technical `Claim Sheet.md` (this is the source; the Accessible Claim Sheet carries the same content).
- `Project Details/Project Details.md` — for the values/standards the translation must preserve.
- The `accessible-piece` playbook — the Accessible Claim Sheet is written in the same plain-language register.

**Output:**
- An `Accessible Claim Sheet.md` at the project root that carries the full content of the technical Claim Sheet — the slots, commitments, success/failure shapes, verification path, and monetization paths — translated into plain language, such that the director can read it alone and come away with an accurate, complete mental model of what the project has committed to.

**Applies these shared standards:** the same uncertainty/claim-discipline ethic as the technical sheet (honesty bounds must survive translation), and the plain-language bar of the Accessible Piece.

---

## Purpose

The technical Claim Sheet leans technical by necessity — its most frequent readers are the agents executing the work. That makes it hard for the director to keep a clean grip on what the project is committed to. The Accessible Claim Sheet fixes that: same commitments, different reader. It is the director's reference companion to the contract.

It is **not** a summary and **not** a softening. It carries the *same* content — every slot, the success/failure/inconclusive shapes, the verification path, the monetization paths — with the jargon walls removed and the honesty bounds fully intact. The technical sheet remains the contract for the team; the accessible sheet is how the director holds the contract. Both are required.

## Construction sequence

1. **Produced at Phase 1 close**, immediately after the agents approve the technical Claim Sheet, by the default writer convention (Claude writes, Codex reviews).
2. **Walk the slots in order** and translate each into plain language. Keep the same structure so the director can move between the two documents slot-for-slot if he wants.
3. **Preserve every commitment exactly.** Success bars, failure bars, baselines, and claim boundaries must mean the same thing in both documents. Translating the *language* must never translate away the *bound*. A reader of the accessible sheet should know precisely what would count as failure.
4. **Explain, don't assume.** Any concept the document leans on that the director is not expected to already know gets a simple explanation and at least one credible-source link (URL or DOI), verified, not cited from memory.
5. **Carry the honest framing.** A clean negative is presented as a real result, not buried. The monetization slot stays forward-looking and honest, including `none identified`.
6. **Keep it in sync forever.** Whenever the technical Claim Sheet is amended, update the Accessible Claim Sheet. Drift between them is a defect, not a backlog item.

## Quality checklist

- [ ] Every slot of the technical Claim Sheet is represented.
- [ ] Success/failure/inconclusive shapes carry identical meaning to the technical sheet.
- [ ] No jargon wall: terms the director isn't expected to know are explained with a credible-source link.
- [ ] The test is met: a generalist reads it end to end and comes away with an accurate, complete model of the commitment **without opening the technical sheet alongside it.**
- [ ] The honesty bounds are intact — a reader knows exactly what would count as failure.
- [ ] In sync with the current state of the technical Claim Sheet (no un-propagated amendments).
- [ ] URL or DOI of credible sources work and lead to what is referenced

## Common failure modes

- **Summarizing instead of translating.** Dropping slots or commitments to make it shorter. It must carry *all* the content, just in plain language.
- **Losing the bound in translation.** Making the claim sound better by blurring the success/failure line. The exact bound must survive.
- **Citing from memory.** Explanations need verified links, same as everywhere in the framework.
- **Drift.** The single most common failure: the technical sheet gets amended and this one doesn't. Update both together, every time.

