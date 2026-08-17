# Launching Collaboration Station

This guide is for the person or scheduler that starts agent sessions. The repository supports two launch modes without changing its internal research workflow:

- **Sequential:** both agent jobs may be scheduled, but `.agent-turn` permits only one named agent to work at a time.
- **Parallel:** Codex and Claude may work at the same time, each protected by its own launcher lock and coordinated through disjoint `Work/Active/` claims.

Choose one recipe for a project. The repository does not detect, select, or switch modes, and one run must not mix the two recipes. In both modes, the inner project command is still:

> Follow the instructions in `AgentPrompt.md`.

The launcher wrapper supplies the runtime gate around that command. `.agent-turn` and all launcher locks are ignored by Git because they describe the local scheduler, not the research project.

## Before either recipe

1. Give each agent filesystem access to the same project root.
2. Use one scheduled job or one manual start per agent. The check-then-create lock wrappers below prevent ordinary overlap with an already-running session; they are not an atomic mutex for two same-agent starts at the exact same instant.
3. Never delete a lock merely because it looks old. First verify that no session of that agent is still active. A leftover lock is a fail-closed interruption, not permission to guess.
4. A session removes only its own lock, and only after its `AgentPrompt.md` workflow is complete. It never removes the other agent's lock.

## Recipe 1 — sequential turns

Create an ignored `.agent-turn` file in the project root containing exactly one line:

```text
Claude
```

The only valid values are `Claude` and `Codex`. Schedule both launchers if desired; each launcher first reads the file, and the non-matching one exits without touching any lock. The matching launcher uses its own per-agent lock, runs the project workflow, writes the other agent's name to `.agent-turn`, and then removes its own lock as the final action.

Use this Codex wrapper:

```text
First, read .agent-turn in the project root. If it is missing, empty, invalid, or does not contain exactly Codex, do no project work and do not create, change, or delete any lock. Simply end this task by saying it is not Codex's turn.

If it is Codex's turn, check for .codex-session.lock in the project root. If .codex-session.lock exists, do no project work. Simply end this task by saying another Codex session is still active. If it does not exist, create .codex-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md.

When the AgentPrompt.md workflow is complete, write Claude and a trailing newline to .agent-turn, then delete .codex-session.lock. The turn update and lock deletion are the final launcher actions. If the workflow does not complete, leave both files unchanged for human inspection.
```

Use this Claude wrapper:

```text
First, read .agent-turn in the project root. If it is missing, empty, invalid, or does not contain exactly Claude, do no project work and do not create, change, or delete any lock. Simply end this task by saying it is not Claude's turn.

If it is Claude's turn, check for .claude-session.lock in the project root. If .claude-session.lock exists, do no project work. Simply end this task by saying another Claude session is still active. If it does not exist, create .claude-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md.

When the AgentPrompt.md workflow is complete, write Codex and a trailing newline to .agent-turn, then delete .claude-session.lock. The turn update and lock deletion are the final launcher actions. If the workflow does not complete, leave both files unchanged for human inspection.
```

For a manual run, read `.agent-turn` and start only the named agent with its wrapper. For automations, the two jobs may share a schedule; the turn check makes one exit before project work.

## Recipe 2 — parallel agents

Do not create or consult `.agent-turn`. Start Codex and Claude independently with distinct per-agent lock wrappers. One agent's lock must never suppress the other agent: file-level coordination happens inside the repository through `Work/Active/`, chat checkpoints, exact-state review, and path-scoped closeout.

Use this Codex wrapper:

```text
First, check for .codex-session.lock in the project root. If .codex-session.lock exists, do no project work. Simply end this task by saying another Codex session is still active. If .codex-session.lock does not exist, create .codex-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md. When the AgentPrompt.md workflow is complete, delete .codex-session.lock.
```

Use this Claude wrapper:

```text
First, check for .claude-session.lock in the project root. If .claude-session.lock exists, do no project work. Simply end this task by saying another Claude session is still active. If .claude-session.lock does not exist, create .claude-session.lock with the current date and time written into it. Once it is created, follow the instructions in AgentPrompt.md. When the AgentPrompt.md workflow is complete, delete .claude-session.lock.
```

The same wrappers work for manual launches and scheduled automations. In a manual parallel run, open one session for each agent from the same project root. In an automated run, give each agent its own recurring job and keep the lock filenames distinct.

## Recovery and mode changes

- **A launcher reports an existing lock:** verify whether that agent still has a live session. If it does, leave the lock alone. If it does not, remove only that verified-stale agent lock and relaunch once.
- **Sequential mode reports a missing or invalid turn:** restore `.agent-turn` manually to exactly `Claude` or `Codex`; do not let an agent infer a value.
- **Migrating an older sequential project:** these recipes replace the legacy shared `.agent-session.lock` wrapper. Stop both launchers, verify that no agent session is active, and replace both agent wrappers in the same change. Never run one legacy shared-lock wrapper beside one Recipe 1 per-agent wrapper against the same project root: they watch different lock files and therefore do not exclude each other.
- **Changing modes:** stop both launchers, verify that no agent session is active, remove only verified-stale launcher state, then either create a valid `.agent-turn` for sequential mode or leave it absent for parallel mode. Restart with the chosen recipe. Do not change modes during a session.

The launcher gates session overlap. They do not replace the repository's own authority rules: a successful start does not approve a write, a review, a commit, a push, publication, spending, credentials, or an external action.
