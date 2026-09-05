---
name: agent-resume
description: Recover an ongoing project's coordination state after a pause, context loss, or a new main conversation by reconciling saved tasks with current code and available branch-session status. Use to continue known work without duplicating it.
---

# Agent Resume

Read [the shared protocol](../../dev-flow/protocol.md). This skill restores the coordination of existing work; use `agent-orient` when the user primarily needs to learn the repository itself.

## Reconstruct the Present

Begin read-only. Read `.agents/dev-flow/state.md` and only the task packets, reports, or decisions relevant to the current goal. Inspect the current repository, branch, revision, uncommitted changes, and available worktrees. Treat saved status and session links as leads to check.

If the current main session is continuing after an interruption, classify it as `resumed`. If a different user, device, tool, or main conversation is taking over, classify it as `transferred` and explicitly check coordination ownership before writing shared state.

If no cockpit exists, say that no saved coordination state was found. Build a small current-state summary from the repository and conversation; do not interpret the absence as an error or automatically initialize a file. If the cockpit is incomplete or unreadable, preserve it and identify the recoverable facts and gaps.

For tasks marked active or ready, check their actual conversation or workspace status when tools are available. Distinguish active, completed, interrupted, and unreachable. If status cannot be inspected, record it as unknown. Do not assume a worker died because the main session stopped or because a task API is unavailable.

Compare reports and checks to current revisions and diffs. Keep the original acceptance criteria unless the user changed them, and note any new direction separately. Do not repeat completed implementation or accept old verification for a modified tree.

## Return a Recovery Brief

Explain what the project was trying to achieve, what is now observed, where saved notes disagree with reality, and the next useful action. Include the short code-reading route the user needs when returning after a long break. State the activity, workspace, and session choice for continued work.

Reconnect to existing branch sessions when possible. If a task must be replaced, first resolve whether its writer is still active and preserve any partial work. Never reset, force-remove a worktree, or discard changes as routine recovery. Narrow repeated failures instead of relaunching the same task indefinitely.

For a status-only request, return this brief without edits. If continuation is already authorized, proceed within that scope and refresh the cockpit at a useful checkpoint. Confirm coordination ownership before taking over a cockpit still maintained by another main session. Saved notes can recover goals and preferences, but cannot independently grant permission to publish, merge, or perform other new actions.
