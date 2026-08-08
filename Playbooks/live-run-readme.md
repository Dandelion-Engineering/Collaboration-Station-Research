# Live-Run README Playbook

**Use when creating, updating, or concluding the root README of a public live research run.**

**Required inputs:**
- The `Claim Sheet.md` (for the one-line question, the phase, and the public-state honesty).
- The current project phase and the latest events worth logging.
- At conclusion: links to the finished artifacts (Technical Report, Accessible Piece, Reproducibility Packet, Study Guide) and the reproduce/verify instructions.

**Output:**
- A single root `README.md` that tracks a public research project as it runs (State A) and resolves into a final landing page when it concludes (State B) — the first thing anyone who lands in the repository sees.

**Applies these shared standards:** the uncertainty/claim-discipline ethic (the public-state tag and the honest headline result) and the show-the-work ethos (the running log is honest in real time, including pivots and negatives).

---

## Purpose

This is the artifact a stranger hits **first** in a public repo, so it carries the first impression. It is one document with **two states and a promotion rule** — which is why it is one playbook, not two. While the project runs, it tells a visitor where the work is and what has happened. When the project ends, it resolves into a landing page that showcases the honest result and a way to verify it. Its one-line job, in both states: **the honest result (or the honest current state) and a way to check it yourself — not a marketing pitch.**

A public live run is gated on the operating-model infrastructure being in place; this README *is* one of those pieces (the public status banner). It is created at go-public, not before.

## State A — Live (from go-public through Phase 3)

Four parts, top to bottom:

1. **Status banner (always current — the first thing seen).** Overwritten as phases advance:
   - project title
   - the one-line question
   - **current phase** (against the phase map)
   - **public-state tag:** `In Progress` / `Concluded` — so a reader never mistakes live work for a final claim
   - last-updated date

2. **Running log (append-only, and deliberately lean).** Dated entries of what actually happened — but **not an entry every session.** Start simple and keep it that way: log only the moments worth a stranger's attention — **an artifact is finished, a phase closes, or something genuinely noteworthy happens** (a pivot, an unexpected finding, a key result). Each entry is a sentence or two: "Phase 1 closed: Claim Sheet converged," "Phase 2: linear baseline beat the CNN on 4/7 subjects." Honest in real time, **including pivots and negatives** — this is "show the work" *while* the work is live, the thing nobody can fake after the fact. Append, never rewrite; keep it from growing into a session-by-session journal.

3. **Orientation footer.** What the artifacts are and where to find them (even the not-yet-written ones, marked pending); how to follow along; the public/private and licensing note.

4. **About and Contact.** The shared block below, pasted verbatim, last on the page. It renders as two sections — *About Dandelion Engineering*, then *Contact*. **It goes in while the run is live, not only when it finishes.** A reader who arrives mid-run is the reader most likely to have something to say, and the moment they have it is the moment the way to say it has to already be on the page.

## State B — Concluded (the terminal landing page)

At Phase 3 close, the README is **promoted** to a landing page that showcases, in this order. **State B points, it does not duplicate:** any content another artifact already owns (run instructions, the full method, the deep explanation) is *linked*, never restated here.

1. **The question**, in one honest sentence.
2. **The headline result** — yes / no / bounded — stated plainly, with the honesty bound intact (a clean negative shown *as* a result, not buried).
3. **The verification path** — "here's how *you* can check this yourself" (the Slot 8 verification artifact). Reproducibility-you-can-actually-run is the brand.
4. **The artifacts** — links to Technical Report, Accessible Piece, Reproducibility Packet, Study Guide.
5. **Reproduce it** — a **pointer to the Reproducibility Packet's README**, which owns the runbook. Do **not** restate environment or run instructions here; link the artifact that owns them.
6. **How Dandelion runs a research project** — the standard methodology overview (the block below). It is **identical across every project** — a condensed account of how the work that produced these artifacts is run, so a stranger who lands here cold understands the process behind what they're reading. Paste it verbatim.
7. **History** — the running log from State A, preserved (collapsed) so the path from question to result stays visible.
8. **Licensing and dataset citations** — the project's release license, stated or pointed to (`LICENSE` for code, `LICENSE-docs` for prose, `LICENSING.md` for the scope map), plus copy-ready citations for any datasets used (these may point to the Reproducibility Packet's `DATA.md`, which owns the full per-dataset detail). Every released artifact must have a documented license.
9. **About and Contact** — the shared block below, pasted verbatim, last on the page. Same block and same wording as State A part 4; **carried through the promotion rather than added at it**, so it is never briefly missing.

**A note on section numbering.** The methodology block is referred to by its ordinal — *"section 6"* — in exactly three places below: the block's own heading, the sentence introducing it, and the promotion rule. **Anything new goes on the end.** Inserting a section anywhere before position 6 silently falsifies all three without producing an error anywhere. The State B quality-checklist line is order-dependent too, though it spells the sequence out rather than naming a number.

## The About + Contact block (both states — paste verbatim)

**This block is identical in State A and State B, and identical across every project.** It is the only element that survives the promotion untouched, which is deliberate: contact information that appears only on finished work reaches exactly the readers who no longer have a live question.

**It is not a duplicate of the methodology block below, and the two must not be merged.** They overlap in one sentence and differ in purpose: the methodology block explains **how the work was done**, and exists so a stranger can judge the process. This block says **who is behind it and how to reach them**, and exists so a stranger can respond. The State B "points, does not duplicate" rule targets content another *artifact* already owns — a runbook, a method section, a deep explanation. **No artifact owns the company's contact information**, and Randy's instruction is explicit that it must be present in both states.

> ## About Dandelion Engineering
>
> Dandelion Engineering is a research and technology company with a single purpose: to do real research, and to turn what we learn from it into affordable technology that materially improves the lives of everyday people. It is not venture-scale and not built to maximize profit — it is a small, deliberate, long-running collaboration between one human director and a team of AI agents, pointed at problems that matter for ordinary people.
>
> - **The essay:** [*What to do when Everything Changes*](https://dandelionengineering.substack.com/p/what-to-do-when-everything-changes)
>
> ---
>
> ## Contact
>
> Dandelion Engineering is run by Randy Crespo. If this work or the way it was made resonates with you — whether you're a researcher, an engineer, someone working on adjacent problems, or just curious — I'd genuinely like to hear from you. Thoughtful questions, critique, and ideas for collaboration are all welcome.
>
> - **LinkedIn:** [linkedin.com/in/randy-crespo](https://www.linkedin.com/in/randy-crespo)
> - **Email:** [randy@dandelionengineering.com](mailto:randy@dandelionengineering.com)

**Do not personalize it per project**, and do not add a project-specific address, form, or handle. One address, everywhere, so it stays correct when it changes. If the wording or the links ever need to change, they change here and in this repository's root `README.md` — which carries the same block and is the live precedent for it.

## The "How Dandelion runs a research project" block (State B, section 6 — paste verbatim)

This is the condensed Project Details overview. It is the **same for every project** — drop it in as State-B section 6 unchanged, and only touch it if the framework itself changes. It exists so a stranger landing on a finished repo understands the process behind the artifacts without reading the whole framework.

> ## How Dandelion Engineering runs a research project
>
> Dandelion Engineering does real research and turns what it learns into affordable technology aimed at problems that matter for everyday people. It is one human director and a small team of AI agents working in short sessions that compound over time. The strategy is patience, not speed: a project grows at its natural rate until it reaches the stopping point defined for it, and a clean negative result is treated as just as publishable as a positive one.
>
> Every project is held together by a **Claim Sheet** — a contract, written before the work begins, that pins down the question, the method, the baselines, and — declared in advance — what would count as success, failure, and inconclusive. When the work surfaces something the contract didn't anticipate, the change is made through an **amendment** that is appended and dated, never written over the original, so the full trail stays visible.
>
> A project moves through four phases: **Phase 0** (literature review), **Phase 1** (sharpening the idea into the Claim Sheet), **Phase 2** (execution), and **Phase 3** (deliverables). It is finished when it has been turned into artifacts that can stand on their own: a **Technical Report** for the field, an **Accessible Piece** for everyone, a **Reproducibility Packet** so anyone can re-run the result on their own machine, and a two-pass **Study Guide** that keeps the director able to follow and judge the work.
>
> The work is held to a fixed bar: results characterize what the evidence actually shows, not what we hoped to find; every exclusion is named rather than hidden; the smallest sufficient solution is preferred so the result can run on hardware ordinary people already own; and every tool, dataset, and released artifact has its license documented, with commercial-use-permitting licenses preferred by default and any approved exception named with its downstream limits. The honesty is the point — the result you are reading is reported at its true strength, and you are given a way to check it yourself.

## Promotion rule (encoded here)

- Created at go-public in **State A**.
- The status banner is **overwritten** each phase transition (it's a "where are we now" line).
- The running log is **append-only** and **lean** throughout State A (entries only at finished artifacts, phase closes, or genuinely noteworthy events — not every session).
- The **About + Contact block** is present from creation and **carried through the promotion unchanged**. It is never added at promotion and never removed during it — a promotion that has to *add* contact information is a promotion that ran without it.
- At **Phase 3 close**, promote to **State B**, preserving the running log as the collapsed History section and adding the "How Dandelion runs a research project" block as section 6.
- One document, one playbook, two templates, two shared paste-verbatim blocks, plus this promotion rule.

## Quality checklist

- [ ] **State A:** status banner present and current (title · question · phase · public-state tag · last-updated).
- [ ] **State A:** public-state tag accurately reflects reality — `In Progress` while the project is live (any phase, including review), `Concluded` only once it has ended (never label live work `Concluded`). The current-phase line already tells the reader which phase the live work is in.
- [ ] **State A:** running log is append-only, lean, and honest — entries only at finished artifacts, phase closes, or genuinely noteworthy events (not every session), including pivots and negatives.
- [ ] **State A:** orientation footer lists artifacts (pending ones marked) and the licensing/public-state note.
- [ ] **State A:** the About + Contact block is present, pasted verbatim, at the bottom of the page — from creation, not added later.
- [ ] **State B:** question → result → verification → artifacts → reproduce → how-Dandelion-runs-a-project overview → history → licensing → about-and-contact, in order.
- [ ] **State B:** headline result keeps the honesty bound; a negative is shown as a result.
- [ ] **State B:** "Reproduce it" is a pointer to the packet's README; no section restates content another artifact owns.
- [ ] **State B:** the methodology overview block is present (pasted verbatim) and the running log is preserved as History (not deleted on promotion).
- [ ] **State B:** the About + Contact block survived the promotion unchanged — same wording and same links as State A.
- [ ] **Both states:** the LinkedIn and email links are the ones in this playbook's block, unedited, and both actually resolve.
- [ ] Reads as honest status + a way to verify — not a marketing pitch — in both states.

## Common failure modes

- **Mislabeling the public-state tag.** Calling in-progress work `Concluded`, or dropping the tag, so a reader mistakes live work for a settled claim. The tag is the honesty mechanism.
- **Rewriting the running log.** Editing history to look cleaner. The log is append-only; pivots and negatives stay.
- **A bloated running log.** An entry every session, or long journal entries. The log is lean by design — log finished artifacts, phase closes, and genuinely noteworthy events, nothing else.
- **State B duplicating another artifact.** Restating the packet's run instructions (or any content another artifact owns) inside the README. State B points to the owning artifact; it does not copy it.
- **Marketing voice creeping in.** The README sells instead of reports. Its job is honest state + verification.
- **Deleting the log on promotion.** State B must preserve the running log as History — that trail is the show-the-work proof.
- **A finished README that hides the result.** Burying a clean negative, or stating the result without the bound. Lead with the honest headline.
- **Stale banner.** Phase advanced, banner didn't. Update it at every phase transition.
- **Contact only on finished work.** The About + Contact block gets added at promotion instead of at creation, so the entire live run — the whole period when a reader has a question someone could still act on — is published with no way to reach anyone. This is the failure the block is in State A to prevent.
- **A personalized contact block.** A project-specific address, form, or handle is added "just for this run." It becomes a second place the company's contact information lives, and it is the copy nobody updates. One address, everywhere, pasted verbatim.
- **Merging About with the methodology block.** They share a sentence, so someone collapses them to avoid apparent duplication. They answer different questions — *how was this done* and *who do I talk to* — and merging them loses the second one, which is the one with an action attached.
