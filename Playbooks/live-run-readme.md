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

Three parts, top to bottom:

1. **Status banner (always current — the first thing seen).** Overwritten as phases advance:
   - project title
   - the one-line question
   - **current phase** (against the phase map)
   - **public-state tag:** `In Progress` / `Concluded` — so a reader never mistakes live work for a final claim
   - last-updated date

2. **Running log (append-only, and deliberately lean).** Dated entries of what actually happened — but **not an entry every session.** Start simple and keep it that way: log only the moments worth a stranger's attention — **an artifact is finished, a phase closes, or something genuinely noteworthy happens** (a pivot, an unexpected finding, a key result). Each entry is a sentence or two: "Phase 1 closed: Claim Sheet converged," "Phase 2: linear baseline beat the CNN on 4/7 subjects." Honest in real time, **including pivots and negatives** — this is "show the work" *while* the work is live, the thing nobody can fake after the fact. Append, never rewrite; keep it from growing into a session-by-session journal.

3. **Orientation footer.** What the artifacts are and where to find them (even the not-yet-written ones, marked pending); how to follow along; the public/private and licensing note.

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
- At **Phase 3 close**, promote to **State B**, preserving the running log as the collapsed History section and adding the "How Dandelion runs a research project" block as section 6.
- One document, one playbook, two templates plus this promotion rule.

## Quality checklist

- [ ] **State A:** status banner present and current (title · question · phase · public-state tag · last-updated).
- [ ] **State A:** public-state tag accurately reflects reality — `In Progress` while the project is live (any phase, including review), `Concluded` only once it has ended (never label live work `Concluded`). The current-phase line already tells the reader which phase the live work is in.
- [ ] **State A:** running log is append-only, lean, and honest — entries only at finished artifacts, phase closes, or genuinely noteworthy events (not every session), including pivots and negatives.
- [ ] **State A:** orientation footer lists artifacts (pending ones marked) and the licensing/public-state note.
- [ ] **State B:** question → result → verification → artifacts → reproduce → how-Dandelion-runs-a-project overview → history → licensing, in order.
- [ ] **State B:** headline result keeps the honesty bound; a negative is shown as a result.
- [ ] **State B:** "Reproduce it" is a pointer to the packet's README; no section restates content another artifact owns.
- [ ] **State B:** the methodology overview block is present (pasted verbatim) and the running log is preserved as History (not deleted on promotion).
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
