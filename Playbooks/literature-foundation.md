# Literature Foundation Playbook

**Use when creating, revising, or reviewing a Literature Foundation — the Phase 0 grounding each agent produces before the Claim Sheet is drafted.**

**Required inputs:**
- `Project Details/Project Details.md` — *The Idea* (the field the project sits in).
- The web search tool (mandatory — every cited source must come from a real search, with a verifiable link or DOI).
- The agent's own running `references.md` (Literature Foundation references migrate into it at Phase 1 start).

**Output:**
- Each agent's own `agents/<AgentName>/Literature Foundation.md` — a six-section survey of the field that grounds the Claim Sheet's method choices, baselines, metrics, and success/failure shapes in what the field has already established, rather than inventing them in the same session the contract is written.

**Applies these shared standards:** the references-file discipline (verified links/DOIs, no citing from memory, written when the source is fresh) and Scientific work (an honest reading of the field, including what has failed). This playbook also absorbs **source-ledger / references behavior** — there is no separate `references` playbook; per-source ledger entries follow the references-file standard in Project Details.

---

## Purpose

Phase 0 is the literature review that precedes everything. Its goal is that the team arrives at Phase 1 already grounded, so the Claim Sheet's choices are informed by the field, not improvised. **Each agent writes their own document independently** — two agents reading the same field from different angles produce different, complementary readings, and the divergence is information worth keeping. The Literature Foundation is also the primary source for **Study Guide Pass 1**, and its open-questions section feeds **Slot 3** (the transferable claim).

## Construction sequence

1. **Search, don't recall.** Conduct your own web search. Every source cited must include a verifiable link or DOI obtained from that search. If a source cannot be verified with a working link or DOI, it is not included. No citing from training knowledge alone.
2. **Write the six sections:**
   1. **Domain and methods landscape** — what approaches exist for this type of problem, and their trade-offs.
   2. **Benchmark results** — what performance ranges are typical for this class of task and these kinds of datasets/inputs (this is where the Claim Sheet's success bars get calibrated to reality).
   3. **Dataset and resource landscape** — open datasets, tools, pre-trained assets; their licenses; what they've been used for.
   4. **Failure modes** — what has been tried and has *not* worked, and why. (Often the most useful section for Claim Sheet sharpening — it keeps the project from re-walking a known dead end.)
   5. **Open questions** — gaps the literature leaves that this project might address. Feeds Slot 3 directly.
   6. **References** — entries in the same format as `references.md`, with verified links/DOIs.
3. **Maintain ledger-quality reference entries** (the source-ledger role). Each entry has: a short summary of what the source covers and why it matters; a note on how it informed the project (what decision it shaped, what method it justified, what question it answered or opened); a direct link; and a citation in a format transferable into the Technical Report's bibliography without rewriting.
4. **Migrate references into your running `references.md`** at Phase 1 start.
5. **Compare notes in chat.** After both agents' documents are complete, compare readings, surface discrepancies, and align on which sources are load-bearing before Phase 1 begins. **Phase 0 closes when both documents are written and the comparison chat is done.** The director is not involved in Phase 0; no `director_requests.md` entry is made at Phase 0 close.

## Quality checklist

- [ ] All six sections present and substantive.
- [ ] Every source has a verified working link or DOI from an actual search — none from memory.
- [ ] Benchmark section gives real performance ranges that can calibrate the Claim Sheet's success bars.
- [ ] Failure-modes section names concrete known dead ends and why they failed.
- [ ] Open-questions section is specific enough to feed Slot 3.
- [ ] Reference entries are ledger-quality (summary · how it informed the work · link · transferable citation).
- [ ] Written independently of the other agent (divergence preserved, not merged prematurely).
- [ ] Comparison chat completed before declaring Phase 0 closed.

## Common failure modes

- **Citing from training knowledge.** The cardinal Phase 0 failure. Every source is searched and link/DOI-verified.
- **Skipping failure modes.** The section most likely to save the project from a known dead end is the easiest to skip. Don't.
- **Thin benchmark section.** Without realistic performance ranges, the Claim Sheet's success bars get set by intuition. Ground them here.
- **Premature merging.** Collapsing both agents' readings into one before the comparison chat loses the divergence that's worth keeping.
- **Ledger debt.** Leaving reference entries thin "to finish later." Write them while the source is fresh; later they get fabricated to fill the page.

## Compact reference — a reference-ledger entry

> **Smith et al. 2023, "Cross-subject EEG decoding limits."** [doi:10.xxxx/xxxxx]
> Covers leave-one-subject-out decoding ceilings on small montages; reports AUC 0.55–0.62 across n≈10 studies.
> *How it informed the work:* sets a realistic benchmark band for Slot 7 and justifies including a behavioral-only control as the strongest baseline (Slot 5).
