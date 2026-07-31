# Reproducibility Packet Playbook

**Use when creating, revising, or reviewing the Reproducibility Packet — the artifact that lets an outsider reproduce the result on their own machine.**

**Required inputs:**
- All analysis/build scripts and configurations from Phase 2.
- The `Claim Sheet.md` Slot 8 (*Director's verification path*) — the verification artifact lives inside this packet.
- The project's data-access situation (open dataset links, or a documented access path).

**Output:**
- A self-contained packet — code, configs, data references, organized files, a `requirements.txt`, its own `.gitignore`, a top-level README, and a dataset-access document (`DATA.md`) — such that someone who copies **the `Reproducibility Packet/` folder alone**, with no other project file reachable, can obtain the data and reproduce the result without contacting anyone on the team.

**Applies these shared standards:** Reproducibility and portability (no hard-coded paths, project-relative outputs, runs end-to-end on a fresh environment), Software engineering (one purpose per script, `argparse`, shared logic in `utils/`, pinned dependencies), and Open source and licensing (every dependency's license documented; commercial-use-permitting by default unless an explicit project exception is approved and named).

---

## Purpose

The Reproducibility Packet is what turns a private result into a checkable public claim. Its standard is strict and binary: an outside person copies the `Reproducibility Packet/` folder to a clean machine and reproduces the result, alone, with no team contact and no other project files reachable. It also houses the **Slot 8 verification artifact**, so anyone who downloads the packet can verify the work the same hands-on way the director does.

## Construction sequence

*This packet is assembled in Phase 3, but it is not built from scratch then. Its raw materials — portable scripts, pinned dependencies, and exclusion records — are kept packet-ready throughout Phase 2 (per the Reproducibility and portability standard). Final assembly is curation and validation, not reconstruction.*

0. **Create the `Reproducibility Packet/` folder early in Phase 2 and write to it directly.** As scripts used in the headline pipeline are finalized, they live in this folder (e.g. `Reproducibility Packet/scripts/`), not in the project root with the packet README pointing back to them. Exploratory Phase-2 work that doesn't survive can stay outside it — only what the final pipeline actually runs needs to be here — but nothing the README tells a reader to run may live anywhere else. **The test of self-containment is literal: copy only this folder to a machine with none of the rest of the repo, and follow the README.** If that fails because a command reaches outside the folder, the packet is not done.
1. **Write the README as a sequential, copy-paste runbook.** An ordered list of steps from a fresh copy of the packet folder to reproduced result. Each step:
   - names the script being run,
   - says in one line what that script does,
   - gives the exact command to copy and paste,
   - lists the output files it produces (if any).
2. **Write the dataset-access document, `DATA.md`.** The packet is only reproducible if a stranger can actually obtain the data it runs on. For **every** dataset the project uses, `DATA.md` gives:
   - **What it is** — one line on the dataset and what role it plays in the project.
   - **How to get it** — the exact download link or access path. If the data is not a direct download (registration, a data-use agreement, an application, a request to authors), spell out those steps so the reader can follow them unaided.
   - **License and commercial-use status** — the dataset's license, and whether it permits commercial use, or the explicit approved exception under which the project uses it and the downstream limits that creates.
   - **Citation** — a full, copy-ready citation for the dataset.
   Keep it machine-agnostic — links and instructions only, no local paths. The README's data-directory convenience variable points the reader to `DATA.md` for how to obtain and place the data. (This covers *dataset* licenses; software-dependency licenses are documented in the README per step 7.)
3. **Define machine-specific values once as convenience variables** at the top of the README (data directory, output directory, etc.), reused in every command — so no command has to be hand-edited.
4. **Place the verification artifact last.** If the Slot 8 artifact is run via a script, its instructions come after the end-to-end pipeline has produced the outputs it depends on. The README may *introduce* it near the top as the reader's eventual way to check the result, but the runnable steps come last.
5. **Keep the README outsider-clean.** Do **not** mention this compute environment's local paths. Do **not** reference the Collaboration Station, the agents, or a history of what was done when. Someone who never saw the Station should follow it easily.
6. **Include `requirements.txt` with pinned versions** and the packet's **own `.gitignore`** (separate from the whole-project `.gitignore`).
7. **Document every dependency's license** in the README so an auditor can identify each one without re-reading every dependency's repo. Resolve any unclear license before shipping; the named per-project release license comes from the Claim Sheet. If a project uses a non-commercial or otherwise restrictive dependency under an approved exception, name that exception and the downstream limits explicitly. (Dataset licenses live in `DATA.md`, step 2.)
8. **Preserve quality-control records.** Every excluded file/sample/run named in the Technical Report is preserved here too — exclusions are reproducible, not hidden.
9. **For physical artifacts**, include build documentation and a parts list to the same standard.
10. **Validate end-to-end on a fresh environment before declaring done.** Given the correct data path and a clean install from `requirements.txt`, every script must execute correctly. Actually run it; don't assume it.

## Quality checklist

- [ ] README is a step-by-step runbook: script name · one-line purpose · exact command · output files, per step.
- [ ] `DATA.md` present: every dataset has a one-line description, a download link / access path, its license + commercial-use status, and a copy-ready citation.
- [ ] Convenience variables defined once at top; no command needs hand-editing; the data-directory variable points to `DATA.md` for how to obtain the data.
- [ ] Verification artifact (Slot 8) instructions placed after the pipeline steps it depends on.
- [ ] No local/compute-environment paths anywhere in the README.
- [ ] No Collaboration Station / agent / session history in the README.
- [ ] `requirements.txt` present with pinned versions; packet has its own `.gitignore`.
- [ ] Every dependency's license documented; all permit commercial use or have an explicit approved exception with downstream limits named.
- [ ] Excluded files/samples/runs preserved and findable.
- [ ] **Verified:** a fresh-environment, correct-data-path run reproduces the result end-to-end.
- [ ] Verified on a copy of the packet folder alone, with no other project file reachable.

## Common failure modes

- **Leaking the local machine.** Hard-coded paths, `C:\Users\...`, or the Station's folder names in the README. The packet must be machine-agnostic.
- **Narrating the project's history.** The README is a runbook, not a journal. No "Session 14 we tried X."
- **Unpinned dependencies.** "It worked on my machine" six months from now. Pin versions.
- **Verification artifact misplaced.** Putting Slot 8 run-steps before the pipeline that generates their inputs.
- **Declaring done without running it.** The end-to-end fresh-env validation is the gate. Skipping it is the most common way a packet ships broken.
- **License hand-waving.** Importing a great tool whose license is unclear, or burying a restrictive license instead of naming the exception. Unclear = unusable until resolved.
- **Assuming the reader already has the data.** Naming a dataset but not saying where to get it, under what license, or how to cite it. `DATA.md` closes that gap — a packet whose data can't be obtained isn't reproducible, however clean the code is.
- **Treating the whole Collaboration Station instance as the deliverable.** Referencing project-root scripts by relative path from the packet's own README instead of writing them into the packet. Portable is not the same claim as self-contained — the packet folder must hold everything its README runs, not just point at it.

## Compact reference — runbook step shape

> **Step 3 — Train the model.**
> Runs `train.py` on the preprocessed features; writes the trained model and a metrics summary.
> ```
> python train.py --data "$DATA_DIR/features" --out "$OUT_DIR/model"
> ```
> Produces: `$OUT_DIR/model/model.pt`, `$OUT_DIR/model/metrics.json`
