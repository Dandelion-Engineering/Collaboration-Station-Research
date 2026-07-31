# Director Requests Playbook

**Use when appending to, replying in, or reviewing `director_requests.md` — the project's single record of work that only the director can do.**

**Required inputs:**
- The current `director_requests.md` at the project root.
- The blocked work and (when one exists) a fallback path the agents can take meanwhile.

**Output:**
- A correctly-formed, append-only entry in `director_requests.md` that tells the director exactly what is needed, why, what is blocked on it, and what the agents are doing in the meantime — without turning the file into a task dump.

**Applies these shared standards:** the append-never-overwrite discipline shared with the amendment protocol and the chat logs.

---

## Purpose

Some work can only be done by the director — download a dataset behind a login, sign up for an API, make a call that needs his identity or judgment. The director is not always available (at his job, asleep, not checking in). `director_requests.md` is the single source of truth for "what is the director on the hook for right now," so the project never stalls waiting and the director can resolve things on whatever cadence his life allows.

## The protocol

1. **When an agent hits director-only work, append a new entry** containing:
   - the **date**,
   - **what is needed**,
   - **why** it is needed,
   - **what part of the project is blocked** on it,
   - **a fallback path** the agents can take in the meantime, when one is available, so the project keeps moving.
2. **Append, never delete or rewrite.** Entries are a permanent record.
3. **The director replies in place.** When the director satisfies a request, he appends a brief reply line under it; the original entry stays as a record.
4. **Requests can be retired by the agents** if they genuinely no longer matter — append a note under the original (e.g. "Not needed anymore — found an open dataset that serves the same purpose"). Don't delete the entry.
5. **The agent does not sit idle.** A blocked line of work does not block the session: move to other Phase-2 work, or Phase-3 work that can start early (drafting parts of the Technical Report or Accessible Piece, the packet README, the Slot 8 artifact), or prototype against a substitute so the real input drops in cleanly later.
6. **First entry is structural.** The Phase-1-close *Claim Sheet ready for director review* entry is the project's first entry in this file; every later director-only request follows the same discipline.

## Quality checklist

- [ ] Entry has date · what's needed · why · what's blocked · fallback (when one exists).
- [ ] Appended, not overwriting any prior entry.
- [ ] A real fallback is named where one is possible (the agent keeps moving).
- [ ] Retired requests get a note, not a deletion.
- [ ] The file reads as genuine director-only blockers, not a general to-do list.

## Common failure modes

- **Task-dumping.** Filling it with work the agents could do themselves. Only genuinely director-only items belong here.
- **Rewriting history.** Editing or deleting old entries. Append-only, always.
- **No fallback.** Logging a blocker and stopping, when a substitute path existed. Log it *and* keep moving.
- **Silent abandonment.** Letting a stale request sit as if live. Retire it with a note when it no longer matters.
