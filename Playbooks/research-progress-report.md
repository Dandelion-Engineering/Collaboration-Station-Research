# Research Progress Report Playbook

**Use when writing a research progress report — the recurring, phase-shaped update each agent writes for the director.**

**Required inputs:**
- The current project state: what's been done since the last report, what was found, what's working/not working, what's next.
- The verification artifact's current state (if there's something new to show).
- The agent's own session count (the cadence is per-agent).

**Output:**
- A progress report in `Progress Reports/` inside the agent's personal workspace, written for the director at the bar of the Accessible Piece, that keeps the director current on where the work is.

**Applies these shared standards:** the Accessible-Piece readability bar (clear, honest, jargon-free, credible-source links for unfamiliar concepts) and the uncertainty/claim-discipline ethic (report what's not working, not just what is).

---

## Purpose

The progress report is one of the three mechanisms that keep the director close enough to the work to know the result is real without becoming its bottleneck (the others are the verification path and the Study Guide). It conveys the **current state** of the work, on a recurring cadence, in language a generalist can follow. It is **smaller and more frequent** than the big deliverables — a real update, not a mini Technical Report and not a thin "we did stuff."

It is distinct from the per-session human report: those live in `Session Summaries/` and are written every session for the record; progress reports live in `Progress Reports/`, are written on the cadence below, and are written *for the director* at the Accessible-Piece bar.

## When to write one

- **Every eighth session each agent runs** — at the agent's own sessions 8, 16, 24, … (the count is per-agent, not cumulative across agents). Do the session's normal work first, then write the report before closing out.
- **At a phase transition** — whoever's session closes Phase 0 / 1 / 2 / 3.
- **At an approved Claim Sheet amendment** — whoever's session writes the approving turn.

These triggers **stack** and do **not** reset the per-agent counter (session 8, then a phase-close two sessions later, then session 16). Phase transitions and amendments are extra reporting events, not replacements for the regular cadence.

## File naming

In `Progress Reports/` inside the agent's personal workspace:
- Regular cadence: `Progress Report Session <N>.md` (e.g. `Progress Report Session 8.md`).
- Phase transition: `Progress Report <Trigger Event>.md` (e.g. `Progress Report Phase 2 Close.md`).
- Amendment: `Progress Report Amendment <Short Description>.md`.

## Construction sequence

1. **Write at the Accessible-Piece bar.** Clear, honest, free of jargon walls, engaging. Any concept the reader isn't expected to know gets a simple explanation and at least one credible-source link. The test: the director reads it end to end without stopping to look something up. Technical accuracy alone is not enough if it isn't followable.
2. **Default content shape** (not fixed — depth follows the work):
   - educational content the director needs to follow the project (explained simply, with credible sources),
   - where the project stands right now,
   - what's been done since the last report,
   - what was found that wasn't expected,
   - what's working,
   - what isn't working (this is also where open `director_requests.md` blockers surface),
   - what the next stretch of work will be.
3. **Verification artifact.** When there's something new to show on it, include its current state. When there isn't, don't manufacture an update.
4. **Write with the Accessible Piece in mind, but not as an installment of it.** The eventual Accessible Piece will reuse this language and these teaching moments — write so it could be — but this report is its own document for the moment it's written in, not constrained to fit a final piece that doesn't exist yet.
5. **Right-size it.** A session-8 report over dense Phase 2 work looks different from a Phase 0-close transition report. The cadence is what matters; the depth follows the work.

## Quality checklist

- [ ] Triggered correctly (per-agent session 8/16/24…, or a phase transition, or an approved amendment).
- [ ] Filed in `Progress Reports/` with the correct trigger-based name.
- [ ] Written at the Accessible-Piece bar — director can read it end to end without looking things up.
- [ ] Covers: where things stand, what's new, what was unexpected, what's working, what isn't, what's next.
- [ ] "What isn't working" honestly surfaces open blockers, including director-only ones.
- [ ] Unfamiliar concepts explained with credible-source links.
- [ ] Verification-artifact update included only if there's genuinely something new.
- [ ] Written as a standalone document, not padded to look like a Technical Report.

## Common failure modes

- **Too thin** — "we did stuff, it's going well." A real update names what was found and what isn't working.
- **Too bloated** — a mini Technical Report. It's a director update at the Accessible bar, not a peer document.
- **Jargon wall** — technically accurate but unfollowable. Explain or link every leaned-on term.
- **Hiding the blockers** — omitting what isn't working. The "what isn't working" content is where the director learns what's stuck.
- **Manufacturing a verification update** — reporting on the Slot 8 artifact when nothing changed. Only when there's something new.
- **Confusing it with the session report** — writing the `Session Summaries/` log instead. Different folder, different audience, different cadence.
