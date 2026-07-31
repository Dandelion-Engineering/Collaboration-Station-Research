# Review Cycle Playbook

**Use whenever an artifact is being reviewed, and when responding after an artifact you created has been reviewed — the loop that brings an artifact still in active review to a single state both agents explicitly approve.**

**Required inputs:**
- The artifact under review, and the chat that belongs to it.
- The reviewing agent's role: read the artifact against the standards and the artifact's own purpose.

**Output:**
- One artifact state that **both** agents have **explicitly** approved, with the feedback, edits, reasons, and approvals recorded in the artifact's chat.

**Applies these shared standards:** the append-never-overwrite discipline of the chat logs; the Standards section of `Project Details.md` (the reviewer reads the artifact against them).

---

## Purpose

Cross-review, by default, keeps the work moving by propagating corrections *forward* — a problem found in concluded work is fixed in the next piece, not by reopening the old one. While an artifact is still in active review, however, its owner and reviewer use this playbook to converge on a single state **both agents explicitly approve**, instead of stalling in comment-and-wait or drifting on an assumption that silence meant assent. This applies to every artifact review, not only to artifacts whose approval is a downstream gate.

Its one non-negotiable idea: **approval is always explicit and always about a specific artifact state.** An edit is not approval. A handoff is not approval. Silence is never approval. The loop is closed only when both agents have said, in the chat, that they approve *the same* state of the artifact.

## The cycle

1. **The owner hands off an explicitly approved state.** After creating or revising the artifact, the owning agent records what was created or changed and why, hands the artifact to the reviewer, and **explicitly approves the state being handed off**. The reviewing agent then reads it against the standards and the artifact's purpose.
2. **The reviewer may edit directly, then hands back with explicit approval.** If the review finds changes, the reviewer may implement them in the artifact itself rather than only describing them. In the artifact's chat the reviewer then states **what changed and why**, hands the artifact back, and **explicitly approves the state being handed off**. (If the review finds nothing to change, the reviewer explicitly approves the state as-is — that closes the loop.)
3. **The owner genuinely re-reviews — this step only happens if the owner comes back to the artifact.** The owning agent must re-open the artifact and review **both the feedback and the edits**, not wave them through. Then:
   - If the owner accepts both, the owner **explicitly approves** the artifact. The loop is closed.
   - If the owner does not accept both — **including accepting the diagnosis but not the reviewer's implementation of it** — or discovers a separate problem upon re-review the owner may edit the artifact and hand it back to the reviewer, stating **what changed** and **explicitly approving the state being handed off**. Back to step 1 on the new state.
4. **Continue until both agents explicitly approve the same state.** Approval is **never inferred** from an edit, a handoff, silence, or implication. Every edited handoff states its approval, every acceptance states it, and the artifact is not done until both approvals name the same state.
5. **Escalate rather than loop.** If the same issue has not converged after roughly two full review round-trips, escalate that **specific disagreement** to Randy rather than looping indefinitely. Escalate the point in dispute, not the whole artifact.
6. **The chat is the record.** The artifact's chat records the feedback, edits, reasons, handoffs, and approvals. Git history preserves file-level provenance; in-file attribution is optional unless separately required.

## Quality checklist

- [ ] Every handoff in the chat states **what changed, why, and an explicit approval** of the state being handed off.
- [ ] The owning agent actually re-opened and re-reviewed the reviewer's edits — it did not treat the reviewer's edit as final by default.
- [ ] The closing state carries **two** explicit approvals naming the **same** artifact state.
- [ ] No approval was inferred from an edit, a handoff, or silence.
- [ ] A disagreement still unresolved after ~2 round-trips was escalated to Randy, scoped to the specific point.

## Common failure modes

- **Inferred approval.** Treating the reviewer's edit, a handoff, or silence as sign-off. The loop stays open until both approvals are stated.
- **The initial handoff carries no owner approval.** Creation is not itself explicit approval. The owner must approve the state being handed to the reviewer; otherwise an as-is reviewer approval still leaves the two-approval requirement open.
- **The owner never comes back.** The owning agent has to re-open the artifact after it is reviewed; if it never does, the re-review in step 3 simply does not happen and the "agreed state" is a fiction. Owning an artifact includes returning to it.
- **Accepting the diagnosis but silently swallowing the implementation.** If the owner agrees there was a problem but not with how the reviewer fixed it, that is a real disagreement — edit and hand back, don't quietly accept edits you'd have made differently.
- **Looping instead of escalating.** Re-editing the same contested point past ~2 round-trips. Hand the specific disagreement to Randy.
- **Reopening concluded work.** This loop is for artifacts in active review, not for reaching back into already-approved work — those corrections still propagate forward per the standard cross-review discipline.
