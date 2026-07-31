# Collaboration Station — Research

A plain-language framework for running exploratory scientific research projects with AI agents.

Collaboration Station is not software. There is nothing to install, no dependencies, no API to call. It is a folder structure and a set of instructions written in ordinary English. You point one or more AI agents at it, give them an idea to investigate, and they work the project across many sessions — reading where the last session left off, contributing something real, and writing down clearly what they did before they stop.

The whole framework is readable in an afternoon. That is deliberate. If you cannot read it, you cannot trust what it produces.

## What it is good for

Exploratory research — the stage before you commit real time, money, or a graduate student to an idea.

A lot of promising ideas are worth a week of investigation and not worth a year. The problem is that finding out which is which has historically cost about as much as just doing the work. This framework is aimed squarely at that gap: it lets you run an idea far enough to learn whether it deserves your main research effort, and it makes the answer "no" cheap enough that you can afford to ask often.

Projects can run for days, weeks, or months with minimal supervision. The director checks in, approves the direction, and reads the reports; the agents do the cumulative work in between.

## What it is not

Being clear about this matters more than the pitch:

- **Not a replacement for a scientist.** The framework produces work a domain expert still has to judge. It is built to make that judgment fast and possible, not to remove it.
- **Not a guarantee of correct results.** It is a structure for doing honest work and showing your reasoning. Honest work is still sometimes wrong.
- **Not autonomous science.** A human director sets the question, approves the plan, and owns the result. The framework is explicit about where the director is required.
- **Not benchmarked.** This is a working method, shared because it has been useful, not a validated methodology with published performance claims.

## How it works

The loop is simple and it is the whole idea:

1. **The director writes down an idea** — informally, in a few paragraphs, in `Project Details/Project Details.md`.
2. **The agents sharpen it into an executable brief** — a Claim Sheet of fifteen numbered slots covering the problem, the claim, the methods and baselines, the evaluation design, and, before any results exist, the predeclared shapes of success, failure, and an inconclusive outcome. A plain-language Accessible Claim Sheet is produced alongside it so the director can hold the contract without reading the technical version.
3. **The director reviews that brief.** Their review is the first use of the amendment protocol, and it is non-blocking — work does not stall waiting on it. Every later change to the contract runs through the same protocol: appended and dated, never overwritten, so the question cannot quietly drift toward whatever the data happened to support.
4. **The agents execute across sessions**, reviewing each other's work and reporting to the director on a fixed cadence.
5. **The project ends with a defined set of deliverables** (below) rather than trailing off.

Continuity between sessions is handled by files, not by model memory. Each agent maintains a summary of exactly what a future session needs to resume, and writes a human-readable report at the end of every session. That is why a project can survive weeks of interruptions.

## Repository layout

```
AgentPrompt.md              The instructions an agent reads first. Start here.
Project Details/            Identity, standards, working method, and the project idea.
Playbooks/                  How each deliverable is built — one file per artifact.
agents/<name>/              One workspace per agent.
  README.md                   Guide to that agent's workspace.
  Summary of Only Necessary Context.md
                              Rewritten each session; how the next session resumes.
  Session Summaries/          A human-readable report from every session.
  Progress Reports/           Director-facing updates on a recurring cadence.
chats/                      File-based messaging between participants.
  Claude-Codex/               One folder per participant combination; inside each,
  Claude-Codex-Human/         one folder per conversation subject.
  Claude-Human/
  Codex-Human/
LICENSE, LICENSE-docs, LICENSING.md, CITATION.cff
                            Licensing and citation metadata.
```

The `chats/` folders are the part people tend to find surprising. Agents talk to each other and to the director in Markdown files, appending timestamped messages. It costs nothing, it keeps conversations out of the main context window, and it leaves a complete record of how a decision was actually reached.

## What a finished project leaves behind

- **A Technical Report** — the full account of what was done and found.
- **An Accessible Piece** — the same result written for a non-specialist.
- **A Reproducibility Packet** — a self-contained folder of scripts and data pointers. The test it has to pass is that you can copy that folder alone to a clean machine and reproduce the work with no other project file reachable.
- **A Study Guide** — written for the director, so the person who commissioned the work can actually follow and judge it.
- **The full reasoning trail** — every chat and every session report, kept as written.

A project released publicly also carries a **Live-Run README** at its repository root: while the work is running it shows a status banner and a lean running log, so a visitor can tell live exploration from a finished claim; when the project concludes it resolves into a landing page that leads with the result and a way to check it.

The reasoning trail is the point. You do not get a result handed to you from a black box; you get the result plus the argument, and you can go back and see where a decision was made and why.

## Getting started

1. Copy this repository to a new folder — one folder per project.
2. Open `Project Details/Project Details.md` and make it yours. The identity, values, and founder sections describe Dandelion Engineering; replace them with your own, or cut them. Write your idea into **The Idea** section at the bottom.
3. Update `CITATION.cff` and `LICENSING.md` — both name Dandelion Engineering's director as the citable author. Replace that with your own name before you publish anything.
4. Rename the folders in `agents/` and `chats/` if you are using different agents. Two agents from different model families is the configuration this was built around — it makes cross-review meaningful rather than an echo — but the structure does not depend on the specific names. If you rename them, also update the default writer/reviewer convention in `Project Details/Project Details.md`, which currently assigns Claude as the default writer and Codex as the required reviewer.
5. Start a session by giving your agent this instruction: **"Follow the instructions in AgentPrompt.md."** That is the entire launch command.

The framework assumes an agent with filesystem access to the project folder. Nothing else is required.

## A note on honesty

The standards in `Project Details/Project Details.md` exist because the failure mode of AI-assisted research is not incompetence — it is plausible-sounding work that nobody checked. Several of the rules are there specifically to make that harder: predeclaring what failure looks like, requiring one agent to review another's work, keeping a written amendment trail, and holding every deliverable at a bar where a stranger can audit it.

A clean negative result is a successful project. If the framework is working, it should tell you your idea was wrong quickly and cheaply, and leave you a record showing why.

## License

Path-scoped. Code and software-like materials are MIT (`LICENSE`); prose and narrative artifacts are CC BY 4.0 (`LICENSE-docs`). `LICENSING.md` is the authoritative map of which applies where. Datasets are not redistributed and remain under their source licenses.

---

Built and used by Dandelion Engineering. Take it, fork it, personalize it, or use it as a starting point for something that fits your work better.

---

## About Dandelion Engineering

Dandelion Engineering is a research and technology company with a single purpose: to do real research, and to turn what we learn from it into affordable technology that materially improves the lives of everyday people. It is not venture-scale and not built to maximize profit — it is a small, deliberate, long-running collaboration between one human director and a team of AI agents, pointed at problems that matter for ordinary people.


- **The essay:** [*What to do when Everything Changes*](https://dandelionengineering.substack.com/p/what-to-do-when-everything-changes)

---

## Contact

Dandelion Engineering is run by Randy Crespo. If this work or the way it was made resonates with you — whether you're a researcher, an engineer, someone working on adjacent problems, or just curious — I'd genuinely like to hear from you. Thoughtful questions, critique, and ideas for collaboration are all welcome.

- **LinkedIn:** [linkedin.com/in/randy-crespo](https://www.linkedin.com/in/randy-crespo)
- **Email:** [randy@dandelionengineering.com](mailto:randy@dandelionengineering.com)

