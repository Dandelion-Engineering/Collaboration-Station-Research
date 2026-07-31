# Technical Report Playbook

**Use when creating, revising, or reviewing the Technical Report — the rigorous, field-facing account of the project.**

**Required inputs:**
- The approved `Claim Sheet.md` (its Slot 14, *minimum public artifact*, defines this report's required contents).
- All Phase 2 execution outputs: results, figures, analysis scripts, exclusion logs.
- Both agents' `references.md` (reconciled into the bibliography at Phase 2).

**Output:**
- A complete Technical Report, **written in LaTeX**, that a scientist or engineer in the relevant field would take seriously: claim, methods, materials, evaluation design, results, limitations, and conclusion — with every exclusion named and every baseline reported, and nothing running off the page.

**Applies these shared standards:** Scientific work (no silent exclusions, validation gates honored), Software engineering (figures at 300 DPI, labeled, self-interpretable), Open source and licensing (dependencies' licenses documented), and the references-file discipline (bibliography built from running `references.md`, not fabricated at the end).

---

## Purpose

The Technical Report is the first of the three outward-facing artifacts — the one written for peers in the field. It is not a peer-reviewed paper, but it meets the bar of a serious technical document: a stranger with domain expertise can read it and judge whether the work holds. It is the rigorous record; the Accessible Piece is its plain-language sibling, and the two are *separate pieces of writing for different readers* (do not let one become a reskin of the other).

## Construction sequence

1. **Let Slot 14 set the contents.** The Claim Sheet's *minimum public artifact* slot spells out what this report must contain for this specific project — usually claim, methods, materials, evaluation design, results, limitations, conclusion. Start from that list.
2. **Report all of it, including what didn't work.** Every baseline that was run is reported (including the strongest non-signal control). Every excluded file, failed sample, or discarded run is named with its reason, somewhere a reader can find it. Silent exclusions are a reproducibility failure. A clean negative result is written up as a result, not minimized.
3. **Honor validation gates.** If a sanity check or published-baseline reproduction failed and was diagnosed before proceeding, the report says so. Don't paper over a gate that didn't pass.
4. **Figures.** 300 DPI or higher, labeled axes, titles, consistent color/styling across the project. A figure must be interpretable without opening the code that made it.
5. **Bibliography.** Reconcile both agents' `references.md` files into the report's bibliography. Each citation has a verified link or DOI. No citations fabricated to fill the page.
6. **Page-overflow check before declaring done.** The recurring failure is content running off the right margin — wide tables and long unbreakable tokens (URLs, file paths, `\texttt{}` code). Scan the LaTeX build log for overfull `\hbox` warnings and visually scan the compiled PDF for lines or tables disappearing past the edge. Fix by breaking/wrapping long tokens and sizing wide tables to the text width, until nothing exceeds the margin.

## Quality checklist

- [ ] Contains everything Slot 14 requires for this project.
- [ ] Every baseline that was run is reported; the strongest control is among them.
- [ ] Every exclusion (file, sample, run) is named with its reason.
- [ ] Failed validation gates are disclosed and their diagnosis shown.
- [ ] Result is stated at its true strength — neither overstated nor buried (including clean negatives).
- [ ] Limitations section is honest and specific (what this result does *not* license).
- [ ] All figures: 300 DPI+, labeled, self-interpretable.
- [ ] Bibliography reconciled from both `references.md` files; every entry has a verified link/DOI.
- [ ] LaTeX build log has no unresolved overfull `\hbox`; compiled PDF has nothing past the right margin.
- [ ] Dependency licenses noted where relevant.

## Common failure modes

- **Silent exclusions.** The single most-cited failure in the Standards. If a file was dropped, the report names it and why.
- **Reporting only the baselines that lost.** Cherry-picking comparisons. Report the strongest control, not a strawman.
- **Overflow shipped.** Wide tables/URLs running off the page in the PDF. Always run the overfull-`\hbox` scan.
- **Marketing tone.** Stretching the result past the evidence. The report characterizes what the data shows; persuasion is not its job.
- **Fabricated citations.** Filling the bibliography from memory at the end. Build it from `references.md` as the work happens.
- **Accessible-Piece bleed.** Writing the report as a dressed-up general-audience piece (or vice versa). Different readers, different documents.

## Compact reference — section skeleton (adapt to Slot 14)

> 1. **Abstract / Claim** — the transferable claim and the headline result, stated at true strength.
> 2. **Introduction** — the question, prior rung, why it matters.
> 3. **Methods** — what was studied/built/compared; the baselines.
> 4. **Materials & Evaluation Design** — datasets, splits, metrics, statistical comparisons.
> 5. **Results** — all baselines, all conditions, with figures and tables; exclusions named.
> 6. **Limitations** — what the result does not license; threats to validity.
> 7. **Conclusion** — what can now be said, and what the next rung would be.
> 8. **References** — reconciled bibliography with verified links/DOIs.
