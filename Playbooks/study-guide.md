# Study Guide Playbook

**Use when creating, revising, or reviewing the Director's Study Guide — either Pass 1 (Conceptual Foundation) or Pass 2 (Concept Delta).**

**Required inputs:**
- **Pass 1:** both agents' `Literature Foundation.md`, the technical `Claim Sheet.md`, both agents' `references.md`.
- **Pass 2:** the finished `Technical Report/` (read at full depth, never summarized), both agents' `references.md`, and this project's **Pass 1** document.

**Output:**
- A LaTeX Study Guide document (one file per pass, in `Study Guide/`) that teaches Randy — specifically — the conceptual territory he needs to follow and judge the work himself. Pass 1 makes him able to follow the Claim Sheet and Phase 2; Pass 2 makes him able to read the Technical Report without stopping to look things up — **without spoiling the results.**

**Applies these shared standards:** Scientific work (accurate, no overstatement) and the references discipline. The Study-Guide-specific standards (narrative, motivated introductions, systems thinking, math policy, credible sources, connections, style) are listed below because they are particular to this artifact.

---

## Purpose

The three outward-facing artifacts are written for strangers. The Study Guide is written for one person: Randy, the director. Its job is unlike theirs — the Accessible Piece tells everyone *what was done and found*; the Study Guide teaches the director the *territory* well enough to follow the work while it runs and judge the Technical Report himself. The Accessible Piece is the expedition report; the Study Guide is the map of the ground it crossed.

**The audience is Randy specifically:** a generalist — broadly curious, systems-oriented, not a domain specialist. He learns through high-level framing and how pieces fit together, not memorized detail or step-by-step derivation. He is not protected from real concepts; he needs them delivered so they build genuine understanding. The only measure that matters for this artifact is whether *Randy*, specifically, comes away oriented and genuinely understanding — not whether a domain expert would approve or whether the literature is fully covered.

**Two passes, two separate documents, written at two existing gates.** They are independent artifacts from separate sources — Pass 2 does not revise or extend Pass 1.

## Construction sequence — Pass 1 (Conceptual Foundation, at Phase 1 close)

At Phase 1 close the Claim Sheet is locked, methods are chosen, success/failure shapes defined — so the agents know exactly which concepts matter.

1. From the Literature Foundation + Claim Sheet + references, select the concepts the director needs to follow the project through Phase 2: domain background, core methods (and *why* they are the natural choices, what the alternatives were, why they were set aside), the evaluation approach, and how it all connects.
2. Write it as a continuous narrative (see standards below).
3. **Test:** after reading Pass 1, Randy can follow the Claim Sheet without stopping to look things up, and can follow Phase 2 as an informed participant rather than a spectator.

**Pass 1 sections:** (1) Introduction — what the project is and what the document covers; (2) Domain Background — the problem space, why it matters, what makes it hard; (3) Core Methods — one section per major method, each motivated before its mechanics; (4) Evaluation Approach — how success and failure are measured, concretely; (5) How It All Fits Together — the system-level view and the load-bearing assumptions.

## Construction sequence — Pass 2 (Concept Delta, at Phase 3, before completion)

Execution surfaces concepts that were not on the radar at Pass 1 — amendments, statistical machinery, ablations, mid-project methods, interpretive framing.

1. Read Pass 1, then read the Technical Report at full depth.
2. **The scope is the delta:** the concepts the report uses that Pass 1 did not establish. That set is what Pass 2 covers — nothing already covered in Pass 1.
3. **Hold the no-spoiler rule (below) absolutely.**
4. **Test:** after reading Pass 2, Randy can read the Technical Report without stopping to look things up — and forms his own judgment of the results.

**Pass 2 sections:** (1) Introduction — what changed conceptually between Pass 1's snapshot and the finished project (new ideas needed, *not* results found); (2) What the Project Added to the Plan — amendments, scope changes, pivots, each motivated by why it became necessary; (3) New Methods and Machinery — techniques, tests, baselines, ablations not in Pass 1, each motivated and explained; (4) Concepts for Reading the Results — the interpretive vocabulary the report uses (effect-size conventions, failure-shape language, domain notions of significance) — the *toolkit* for reading results, not a reading of them; (5) How Pass 1 Holds Up — where Pass 1's framing held and where the path made some emphasis more or less load-bearing, as conceptual reframing only, no results spoiled.

## The no-spoiler rule (Pass 2)

Pass 2 does **not** tell Randy what the results are or what they mean. The results stay his to discover by reading the Technical Report directly; Pass 2 only gives him the vocabulary to do that reading and form his own judgment.

This is real and easily violated: a Pass 2 can avoid stating a single result and still quietly steer the director toward the agents' preferred interpretation — by choosing the framing that makes the result land well, or by omitting the concept that would let him spot a weak spot. A Pass 2 that does this has failed even if every sentence is true. Because the same agents who did the research write the guide that teaches the director to judge it, this failure mode is **structural** — which is why Codex's review exists specifically to catch it.

## The Study-Guide standards (particular to this artifact)

- **Narrative, not reference.** A continuous narrative, not a list of definitions. Ideas arrive in the order they build on each other, with explicit transitions — each new idea arrives because the previous one opened a question it answers.
- **Motivated introductions.** Every concept introduced with *why it exists* before *what it is*. Open with the problem it solves; never "X is a method for…"
- **Systems thinking.** After the core concepts, a section on how the pieces work together as a system: what each receives, transforms, passes on; what happens to the output when an input changes; where the dependencies and load-bearing assumptions are.
- **Math policy.** Math appears only when all three hold: (1) it shows something plain language genuinely cannot; (2) it is sandwiched between a plain-language motivation and a plain-language interpretation; (3) every symbol is defined in plain language the moment it appears. Math failing any of these is removed.
- **Credible sources.** Every major conceptual claim carries at least one credible-source link (URL/DOI), inline, with a brief note on what it offers beyond the guide. Sources found and verified with web search before drafting — no citing from memory.
- **Connections to this project.** The general background is tied back to this specific project throughout — not in a closing section. When a concept is introduced, name how it appears in this project's Claim Sheet, methods, evaluation design, or (non-spoiling) result-reading vocabulary. This is what separates a study guide from a generic tutorial.
- **Style.** Clear, honest, direct, engaging; no jargon walls; the register of a knowledgeable colleague who respects the reader's intelligence. The goal is to orient Randy, not to impress him.

## Format and file layout

LaTeX, one file per pass, in a `Study Guide/` folder at the project root:

```
Study Guide/
├── Pass 1 - Conceptual Foundation.tex
└── Pass 2 - Concept Delta.tex
```

Preamble for each document:

```latex
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb}
\usepackage{hyperref}
\usepackage{parskip}
\usepackage{microtype}
\usepackage{lmodern}
\usepackage{booktabs}

\title{<Research Project Name> \\ Pass <N> --- <Pass Title>}
\author{Dandelion Engineering}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
```

## Labor and approval

Claude is the default writer for both passes (web search, concept selection, narrative, math, source links). **Codex is the required reviewer and gives final approval; a pass is not complete until Codex has explicitly approved it.** Codex checks technical accuracy, real (not invented) connections, correct math, claims neither over- nor understated — and, for Pass 2, the no-spoiler discipline. Disagreements are resolved in chat before the pass is finalized.

## Quality checklist

- [ ] Written for Randy specifically — high-level framing and systems view, not a detail dump.
- [ ] Continuous narrative with explicit transitions; concepts motivated (why before what).
- [ ] A systems-level section shows how the pieces interlock and names the load-bearing assumptions.
- [ ] Math obeys the three-part policy (or is absent); every symbol defined in plain language on appearance.
- [ ] Every major conceptual claim has a verified credible-source link with a "what it adds" note.
- [ ] Background tied back to *this* project throughout, not in a closing section.
- [ ] **Pass 1:** Randy can follow the Claim Sheet and Phase 2 after reading it.
- [ ] **Pass 2:** scope is strictly the delta; **no result is stated or steered toward**; Randy can read the Technical Report unaided afterward.
- [ ] LaTeX, correct preamble, correct section skeleton for the pass.
- [ ] LaTeX build log has no unresolved overfull `\hbox`; compiled PDF has nothing past the right margin.
- [ ] Codex has explicitly approved.

## Common failure modes

- **Spoiling Pass 2** — stating a result, *or* (subtler) framing/omitting so the director is steered toward the agents' interpretation. Both fail.
- **Reference list disguised as a guide** — definitions in sequence with no narrative or motivation.
- **Math for its own sake** — equations that don't show something words can't, or with undefined symbols.
- **Generic tutorial** — correct concepts never tied back to this project's actual Claim Sheet/methods.
- **Pass 2 re-teaching Pass 1** — covering concepts already established instead of only the delta.
- **Writing to impress experts** — the audience is Randy; expert approval is not the test.
- **Skipping the Codex gate** — a pass is not done until Codex approves it.
