# Live-Run README Playbook

**Use when creating, updating, or concluding the root README of a public live research run.**

**Required inputs:**
- The `Claim Sheet.md` (for the one-line question, the phase, and the public-state honesty).
- **Whether this run was selected by the agents or requested by the director** — from `Project Details/Project Details.md`. It decides whether the run-provenance block goes on the page, and it is looked up rather than assumed.
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

Top to bottom. **The run-provenance part is conditional**, so this is the order, not a fixed count:

- **Status banner (always current — the first thing seen).** Overwritten as phases advance:
   - project title
   - the one-line question
   - **current phase** (against the phase map)
   - **public-state tag:** `In Progress` / `Concluded` — so a reader never mistakes live work for a final claim
   - last-updated date

- **How this project was run.** The shared block below, pasted verbatim, **when this run was selected and launched by the agents rather than requested by the director** — see *When the run-provenance block is required*. It goes directly under the banner, above everything else, because a reader who learns how the work was produced after reading the result has already taken the result at face value.

- **Running log (append-only, and deliberately lean).** Dated entries of what actually happened — but **not an entry every session.** Start simple and keep it that way: log only the moments worth a stranger's attention — **an artifact is finished, a phase closes, or something genuinely noteworthy happens** (a pivot, an unexpected finding, a key result). Each entry is a sentence or two: "Phase 1 closed: Claim Sheet converged," "Phase 2: linear baseline beat the CNN on 4/7 subjects." Honest in real time, **including pivots and negatives** — this is "show the work" *while* the work is live, the thing nobody can fake after the fact. Append, never rewrite; keep it from growing into a session-by-session journal.

- **Orientation footer.** What the artifacts are and where to find them (even the not-yet-written ones, marked pending); how to follow along; the public/private and licensing note.

- **About and Contact.** The shared block below, pasted verbatim, last on the page. It renders as two sections — *About Dandelion Engineering*, then *Contact*. **It goes in while the run is live, not only when it finishes.** A reader who arrives mid-run is the reader most likely to have something to say, and the moment they have it is the moment the way to say it has to already be on the page.

## State B — Concluded (the terminal landing page)

At Phase 3 close, the README is **promoted** to a landing page that showcases, in this order. **State B points, it does not duplicate:** any content another artifact already owns (run instructions, the full method, the deep explanation) is *linked*, never restated here.

- **Status banner (always current — the first thing seen).** Carry the State A banner through the promotion and overwrite its terminal values: project title, the one-line question, the completed phase, the public-state tag `Concluded`, and the conclusion date as last-updated. The question already lives here; do not create a second standalone copy below it.
- **How this project was run** — the shared run-provenance block below, pasted verbatim, **when this run was selected and launched by the agents rather than requested by the director** — see *When the run-provenance block is required*. Same block and same wording as State A's *How this project was run*; **carried through the promotion rather than added at it.** It sits directly under the banner and above the result on purpose: a disclosure a reader reaches after the headline is a disclosure that arrived too late to do anything.
- **The headline result** — yes / no / bounded — stated plainly, with the honesty bound intact (a clean negative shown *as* a result, not buried).
- **The verification path** — "here's how *you* can check this yourself" (the Slot 8 verification artifact). Reproducibility-you-can-actually-run is the brand.
- **The artifacts** — links to Technical Report, Accessible Piece, Reproducibility Packet, Study Guide.
- **Reproduce it** — a **pointer to the Reproducibility Packet's README**, which owns the runbook. Do **not** restate environment or run instructions here; link the artifact that owns them.
- **How Dandelion runs a research project** — the standard methodology overview (the block below). It is **identical across every project** — a condensed account of how the work that produced these artifacts is run, so a stranger who lands here cold understands the process behind what they're reading. Paste it verbatim.
- **History** — the running log from State A, preserved (collapsed) so the path from question to result stays visible.
- **Licensing and dataset citations** — the project's release license, stated or pointed to (`LICENSE` for code, `LICENSE-docs` for prose, `LICENSING.md` for the scope map), plus copy-ready citations for any datasets used (these may point to the Reproducibility Packet's `DATA.md`, which owns the full per-dataset detail). Every released artifact must have a documented license.
- **About and Contact** — the shared block below, pasted verbatim, last on the page. Same block and same wording as State A's *About and Contact*; **carried through the promotion rather than added at it**, so it is never briefly missing.

**A note on cross-references.** **Sections are referred to by name here, never by number.** The run-provenance section is conditional, so any ordinal counted past it is wrong on one of the two branches — *"section 7"* is section 6 on every run the director asked for, and nothing errors when it is. Refer to a section by its heading, and to its placement by the sections it sits between. **The overviews above are deliberately unnumbered** — they give reading order, and a number on a conditional sequence would read as an identifier that two branches disagree about.

**Anything new goes on the end** unless it has a reason to sit earlier; if it does, name its neighbours rather than renumbering anything.

## When the run-provenance block is required

**Two kinds of run land in this framework, and they differ in exactly one respect that a public reader would care about: who chose the question.**

- **Agent-selected.** The agents running Dandelion Station found the question, judged it worth answering, and launched this project. **The run-provenance block is required.**
- **Director-requested.** The director brought this question himself and asked for it to be researched. **The block is omitted**, because its third statement — a director who sets direction and reads summaries but does not follow the work in detail — is not true of a project built from his own idea, and a disclosure that is partly false is worse than none.

**`Project Details/Project Details.md` states which kind of run this is.** It is written at launch, before the first session, and it is the file you read at the start of every session — so the answer is already in front of you and does not have to be inferred from anything.

**If it does not say, stop and ask. Do not guess, in either direction.** Pasting the block into a director-requested run publishes a false statement about how the question was chosen. Omitting it from an agent-selected run withholds a true one that a reader needs in order to weigh what they are reading. Neither error is the safe one, which is why the answer is an input rather than a default.

**Omitting the block never hides that AI agents did the work.** The About block below and the methodology block both say so plainly, and both are present in every run of either kind. What this block adds is narrower and more specific: that nobody *chose* the question either, and that no human checked the work line by line.

## The run-provenance block (both states, agent-selected runs — paste verbatim)

**This block is identical in State A and State B**, and it is carried through the promotion unchanged for the same reason the About block is: a disclosure that appears only on finished work reaches exactly the readers who have stopped forming an impression.

**The wording is the director's and is not an agent's to edit.** If a run needs it to say something different, that is a question for him, not a local adaptation.

> ## How this project was run
>
> - **This is an automated exploratory research run.** It investigates one question and reports what it found. It is not a confirmatory study, and it is not meant to settle anything.
> - **The work was selected and carried out by AI agents.** Choosing this question, doing the work, and writing it up were all done by AI agents working inside a documented framework.
> - **A human director sets direction and reads summaries. He does not review the work in detail.** Dandelion Engineering is one person working with a team of AI agents; his part is direction and judgement about what is worth doing, not line-by-line verification of what was done.
> - **Negative findings are published as produced.** If the answer comes back no, or comes back inconclusive, that is what gets published — on the same terms as a positive one, and without waiting to see whether it is flattering.
> - **This is not reviewed work.** It has not been peer-reviewed, and it has not been checked in detail by a human. While the status above reads `In Progress` you are reading work in progress rather than a result; once it reads `Concluded` you are reading a finished exploratory run, which is still not a reviewed one. **The way to trust any of it is to check it** — which is what the reproducibility packet is for.

**Do not soften it, and do not move it down the page.** Every line of it is a limitation stated before a reader has invested anything, which is the only point at which a limitation is useful to them.

## The About + Contact block (both states — paste verbatim)

**This block is identical in State A and State B, and identical across every project.** It survives the promotion untouched — as does the run-provenance block above, and for the same reason: something that appears only on finished work reaches exactly the readers who have stopped needing it.

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

## The "How Dandelion runs a research project" block (State B — paste verbatim)

This is the condensed Project Details overview. It is the **same for every project** — drop it into State B unchanged, between *Reproduce it* and *History*, and only touch it if the framework itself changes. It exists so a stranger landing on a finished repo understands the process behind the artifacts without reading the whole framework.

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
- The status banner is **overwritten** at each phase transition and **carried through the promotion**. At Phase 3 close, its phase line records completion, its public-state tag becomes `Concluded`, and its last-updated value becomes the conclusion date.
- The running log is **append-only** and **lean** throughout State A (entries only at finished artifacts, phase closes, or genuinely noteworthy events — not every session).
- The **run-provenance block**, on an agent-selected run, is present from creation and **carried through the promotion unchanged**, directly under the status banner. Whether the run is agent-selected or director-requested is settled at launch and never re-decided here.
- The **About + Contact block** is present from creation and **carried through the promotion unchanged**. It is never added at promotion and never removed during it — a promotion that has to *add* contact information is a promotion that ran without it.
- At **Phase 3 close**, promote to **State B**, finalizing rather than dropping the status banner, preserving the running log as the collapsed History section, and adding the *How Dandelion runs a research project* block between *Reproduce it* and *History*.
- One document, one playbook, two templates, three shared paste-verbatim blocks (one of them conditional), plus this promotion rule.

## Quality checklist

- [ ] **State A:** status banner present and current (title · question · phase · public-state tag · last-updated).
- [ ] **State A:** public-state tag accurately reflects reality — `In Progress` while the project is live (any phase, including review), `Concluded` only once it has ended (never label live work `Concluded`). The current-phase line already tells the reader which phase the live work is in.
- [ ] **State A:** running log is append-only, lean, and honest — entries only at finished artifacts, phase closes, or genuinely noteworthy events (not every session), including pivots and negatives.
- [ ] **State A:** orientation footer lists artifacts (pending ones marked) and the licensing/public-state note.
- [ ] **State A:** the About + Contact block is present, pasted verbatim, at the bottom of the page — from creation, not added later.
- [ ] **Both states:** `Project Details/Project Details.md` was read to determine whether this run is agent-selected or director-requested — **read, not inferred** — and the run-provenance block is present verbatim directly under the status banner if agent-selected, absent if director-requested.
- [ ] **Both states:** if that file does not say which kind of run this is, the README was not published and the question went to the director instead.
- [ ] **State B:** status banner → *[how-this-was-run — agent-selected runs only]* → result → verification → artifacts → reproduce → how-Dandelion-runs-a-project overview → history → licensing → about-and-contact, in order. On a director-requested run the bracketed section is absent and everything else keeps this order.
- [ ] **State B:** status banner survived the promotion, contains the one-line question, records the completed phase, carries the public-state tag `Concluded`, and gives the conclusion date as last-updated.
- [ ] **State B:** headline result keeps the honesty bound; a negative is shown as a result.
- [ ] **State B:** "Reproduce it" is a pointer to the packet's README; no section restates content another artifact owns.
- [ ] **State B:** the methodology overview block is present (pasted verbatim) and the running log is preserved as History (not deleted on promotion).
- [ ] **State B:** the About + Contact block survived the promotion unchanged — same wording and same links as State A.
- [ ] **State B, agent-selected runs only:** the run-provenance block survived the promotion unchanged, and is still above the headline result. **On a director-requested run it is absent from both states, and its absence at State B is not a promotion failure** — the check that applies there is the one above: it was absent at State A too.
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
- **Stale or dropped banner.** A phase advanced without updating the banner, or promotion removed it. Update it at every phase transition and retain it in State B with the terminal `Concluded` state.
- **Contact only on finished work.** The About + Contact block gets added at promotion instead of at creation, so the entire live run — the whole period when a reader has a question someone could still act on — is published with no way to reach anyone. This is the failure the block is in State A to prevent.
- **A personalized contact block.** A project-specific address, form, or handle is added "just for this run." It becomes a second place the company's contact information lives, and it is the copy nobody updates. One address, everywhere, pasted verbatim.
- **Merging About with the methodology block.** They share a sentence, so someone collapses them to avoid apparent duplication. They answer different questions — *how was this done* and *who do I talk to* — and merging them loses the second one, which is the one with an action attached.
- **Guessing which kind of run this is.** `Project Details.md` does not say, and rather than ask, someone reasons it out from the project's history and picks. Both wrong answers publish something untrue, so there is no cautious default to fall back on — this is the one input in the playbook that must be looked up.
- **Demoting the run-provenance block.** It gets moved below the result, folded into the orientation footer, or collapsed behind a details tag, because it reads as a disclaimer and disclaimers feel like they belong at the bottom. A reader who meets it after the headline has already formed the impression it exists to prevent.
- **Editing the run-provenance wording for a particular project.** Softening a line, dropping the peer-review sentence on a run that feels solid, or adding a project-specific caveat. The wording is the director's and is the same everywhere; a per-project version is a claim nobody approved.
- **Merging the run-provenance block into About or the methodology block.** All three touch how the work is made, so they look like duplicates. They are not: the methodology block describes the *process in general*, About says *who is behind it*, and this block states *what is and is not true of this specific run* — the only one of the three that is a limitation rather than a description.
