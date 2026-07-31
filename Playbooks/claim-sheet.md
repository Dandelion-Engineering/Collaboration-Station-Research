# Claim Sheet Playbook

**Use when creating, revising, or reviewing a Dandelion Research Claim Sheet.**

**Required inputs:**
- `Project Details/Project Details.md` — especially *The Idea* (the seed the sheet starts from) and the Standards.
- Both agents' `agents/<AgentName>/Literature Foundation.md` (Phase 0 output).
- Both agents' `agents/<AgentName>/references.md`.
- Any existing entries in `director_requests.md`.

**Output:**
- A rigorous *and* readable `Claim Sheet.md` at the project root that defines the project contract — the question, the transferable claim, the success/failure/inconclusive shapes, the baselines, the constraints, the verification path, and the claim boundaries — and that a fresh reader can follow without having already read the other project documents.

**Applies these shared standards (defined in Project Details, not restated here):** Scientific work (claims characterize what the evidence shows, no advocacy), Efficiency (smallest-sufficient framing), Open source and licensing (named per project), and the uncertainty/claim-discipline ethic ("a clean failure is still a public artifact").

---

## Purpose

The Claim Sheet is the contract for the project. Every agent reads it at the start of every session; every result is measured against it. It is filled in collaboratively by the agents during Phase 1. The director reviews and (where needed) amends it, but that review is **non-blocking**: agents may keep working — and a short project may even run to conclusion — while director review is still pending. See the amendment protocol below for exactly how director review and approval flow.

Two readers use it, and the tension between them is the whole design problem of this artifact. The agents executing the work need it **precise** — exact baselines, exact metrics, exact success bars. The director (and any future reader who lands on it) needs it **legible** — able to be understood as a story without reconstructing context from the other documents. The Claim Sheet is rigor-first; readability is what makes the rigor *inspectable*. It is not the place lay-accessibility lives — that is the Accessible Claim Sheet and the Accessible Piece. The job here is: stay as exact as the contract requires, and add an on-ramp so the exactness can be followed.

## Construction sequence

Write the on-ramp first, then the slots. The on-ramp is not decoration added at the end; it is what lets everything below it be read.

**1. Orientation header (write this first; it is a hard requirement).** Before Slot 1, a fresh reader must be *handed* the story rather than forced to reconstruct it. The header has four parts, in plain language:
   - **What this document is** — one or two sentences: this is the contract for the project; here is how to read it.
   - **The question, in ordinary language** — what we are actually trying to find out, and why it matters / who it would help.
   - **A few sentences of narrative context** — the prior rung (what previous Dandelion Engineering research projects or the literature established), the current rung (what this project tests), and what success and failure would each mean.
   - **A "contract at a glance" box** — target · inputs · baselines · success bar · failure bar, in five compact lines, so the spine of the contract is visible before the slot machinery starts.

**2. A one-line gloss of the slot framework.** State that the sheet is organized as fifteen numbered slots, each a structurally important commitment, and that they can be read in order as a throughline. (Or point to where the framework is defined.) A reader should never hit "Slot 1" cold.

**3. Fill the fifteen slots**, drawing method choices, baselines, metrics, and success/failure shapes from the Literature Foundation rather than inventing them:

1. **Domain and substrate.** What system/material the project engages; where the data, signal, or object comes from.
2. **Problem being addressed.** The question, framed concretely enough that an answer is possible.
3. **The transferable claim.** What we could say if the project succeeds — one declarative sentence.
4. **Constraints.** Technical, hardware, budget, time, safety, ethical — the bounds the work lives inside.
5. **Methods or approach.** What is studied, built, or compared, and the baselines/comparison points.
6. **Application and downstream relevance.** Why it matters, who it helps, what future projects it feeds.
7. **Materials and evaluation design.** Datasets, hardware, splits, metrics, statistical comparisons — how we will know whether the claim holds. (This slot is the *team's* confidence path.)
8. **Director's verification path.** The hands-on artifact the agents commit to building so the director — and anyone who downloads the Reproducibility Packet — can verify the result without reading the Technical Report end to end. Describe the artifact (simulation, side-by-side visualization, worked example, interactive demo) and what the director must look at or do to be convinced. (This slot is the *director's* confidence path; the artifact lives inside the Reproducibility Packet.)
9. **Architecture or build plan.** Start with the smallest version that could plausibly work — but pre-commit to a *capacity-escalation ladder*, not a single fixed size. State the starting architecture, the larger versions you will try if the small one falls short, and the ceiling the available hardware allows (name the actual compute budget — the GPU/VRAM, memory, and time you can spend). **"Smallest sufficient" governs the *final shipped* solution, not the *investigation*:** a null result from an undersized model is evidence about *that model*, not about whether the signal exists. So the plan must say, in advance, that you will scale capacity up when **(a)** there is partial signal worth strengthening, **or (b)** there is no signal yet but a larger-capacity model could plausibly capture one the small model cannot — and that you stop climbing only when the result holds across the ladder, the hardware ceiling is genuinely reached, or there is a *scientific* reason (not a budget reflex) that a bigger model would not help. Concluding "a bigger version won't work" is itself a claim: it requires that scientific reason stated explicitly. Absent it, the ladder has not been climbed far enough to make the claim.
10. **Computational and physical environment.** Platform, hardware, software, libraries, paths, dependencies.
11. **What would count as success.** Pre-declared, before any result is observed.
12. **What would count as failure.** Also pre-declared. A clean failure is still a public artifact.
13. **What would count as inconclusive or non-transfer.** The "not this, not yet" shapes — recorded so partial wins are not reported as full ones.
14. **Minimum public artifact required to conclude the project.** What must exist before the project is done (this drives the Technical Report's required contents).
15. **Possible monetization paths.** Forward-looking and honest; `none identified` is a real entry. Both the succeeds-as-scoped case and the succeeds-and-scaled case may be filled, or neither.

   Not every slot is heavy for every project (a software project may have a thin physical-environment entry). The slots are all present so nothing structurally important is left implicit.

**4. Make the slots read as a narrative spine, not a form.** Use explicit transitions so each slot arrives because the previous one opened a question it answers. Define specialized terms on first use. Internal shorthand ("Amendment 1," phase names) must be glossed the first time it appears — never assume the reader has read the other docs.

**5. Make "what would make this claim fail" easy to find.** Slots 12 and 13 already hold this; surface them so a reader can locate the failure conditions without hunting. This is core to the show-the-work ethic.

**6. Write the Accessible Claim Sheet immediately after** (see the `accessible-claim-sheet` playbook). The two are produced in the same Phase-1-close window and kept in sync thereafter.

**Construction-phase revisions stay clean.** While the sheet is being drafted and cross-reviewed in Phase 1 — including a director's non-blocking review of the draft — edit it directly and cleanly. Do not add a Status header, a "changelog," or any dated revision log for this back-and-forth; git history already records it. The finished sheet should read as a single clean contract with no trace of how it was built. The amendment protocol below is for a different thing entirely: a change discovered once the sheet is in force, during or after execution — not the ordinary give-and-take of getting the draft agreed on in the first place.

## Amendment protocol (how the sheet changes after approval)

Real research surfaces what the sheet did not anticipate. When it does, the agent who finds it writes a short **amendment proposal**: what was found, why it changes the path, the new path, and the new success/failure/non-transfer shapes. The other agents approve or reject before execution shifts. If approved, the amendment is **appended and dated, never overwritten** on the original; work proceeds on the amended sheet. If rejected, the agents discuss to consensus.

- **Archive on invalidation.** When an amendment invalidates already-done work, move the affected files to `archive/YYYY-MM-DD-<short-reason>/` and point the amendment entry at that subfolder. Append, never delete.
- **Director review/approval.** The director's Phase-1 review runs through this same protocol: approve-with-no-changes closes silently; director-proposed changes run through the amendment cycle and, if appropriate, the archive cycle. Director review and subsequent approval are **non-blocking**: the project can continue without director approval of the Claim Sheet, and can even be brought to finish without the director's explicit approval. (This is a deliberate decision for a full-time director — if a fast project concludes before the director can review it and a real problem surfaces on later reading, it is flagged with a public disclaimer rather than retroactively gating the run.)
- **Keep the Accessible Claim Sheet in sync.** The information in the Accessible Claim Sheet must match the information in the Claim Sheet.

## Quality checklist

- [ ] A fresh reader can read the orientation header alone and correctly state the question, the prior rung, what is being tested, and what success/failure mean.
- [ ] "Contract at a glance" box present: target · inputs · baselines · success bar · failure bar.
- [ ] All fifteen slots present (thin entries allowed and labeled; nothing silently omitted).
- [ ] Success (11), failure (12), and inconclusive (13) shapes are **pre-declared** and specific, not vibes.
- [ ] Baselines in Slot 5/7 include the *strongest non-signal control*, not just a weak one.
- [ ] Slot 8 names a concrete, buildable verification artifact and what the director does with it.
- [ ] Slot 9 defines a capacity-escalation ladder (start size → larger versions → hardware ceiling, with the compute budget named), not a single fixed size; any "a bigger model wouldn't help" stopping rule is backed by a stated scientific reason, not a budget reflex.
- [ ] Method/baseline/metric choices trace to the Literature Foundation, not to memory.
- [ ] Specialized terms defined on first use; internal shorthand glossed.
- [ ] Slots read as a throughline with transitions, not a disconnected form.
- [ ] Licensing posture and any relaxed standard named explicitly (per the Standards section).
- [ ] Accessible Claim Sheet written/updated in the same session.
- [ ] No Status header or changelog carried over from Phase-1 drafting/cross-review — the sheet reads as a clean, current contract; that history lives in git, not the document.

## Common failure modes

- **Opening cold on "Slot 1."** No orientation, so the reader reconstructs the story instead of being handed it. (This is the exact readability defect that prompted this playbook.) Fix: the orientation header.
- **Readability bought with rigor.** Softening the technical content to make it "readable." Wrong trade. Keep the slots exact; add the on-ramp around them.
- **Lay-accessibility creeping in.** Trying to make the Claim Sheet itself fully lay-readable. That job belongs to the Accessible Claim Sheet — don't sand the contract into mush.
- **Post-hoc success bars.** Declaring or quietly loosening success/failure shapes after seeing results. Slots 11–13 are pre-registration; treat them as locked unless formally amended.
- **Mistaking an undersized model for a settled negative.** Running one small architecture, finding nothing, and concluding the signal is absent — or that scaling up wouldn't help — without climbing the Slot 9 capacity ladder to the hardware ceiling or giving a scientific reason a larger model would fail. "Smallest sufficient" describes the final shipped solution, not a cap on the search.
- **Bolting a new headline on after a result.** When a result disappoints, resist promoting an exploratory side-finding into the claim. Amend honestly; a clean negative is a result.
- **Drift between the technical and accessible sheets.** Amend one, forget the other. Always update both in the same session.
- **Leaving construction scaffolding in the finished sheet.** Adding a Status header or a changelog to record the ordinary back-and-forth of getting the draft agreed on (e.g. a reviewer's requested changes before the sheet is in force). That process history should leave no procedural trace in the final document.
