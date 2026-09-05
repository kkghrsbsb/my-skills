---
name: agent-branch
description: Prepare and coordinate a bounded branch-session handoff, choosing direct work, a context-inheriting fork, or a fresh task independently from Git workspace isolation. Use when the user wants development work split across conversations.
---

# Agent Branch

Read [the shared protocol](../../dev-flow/protocol.md). A branch session is a conversation carrying one task; it is not automatically a Git branch or a background subagent.

## Prepare the Dispatch

Use the current task packet, or draft a concise one from [the task template](../../dev-flow/templates/task.md). Resolve the objective, acceptance criteria, dependencies, allowed paths, authorized actions, baseline, and return destination before dispatching an implementer. Keep unknowns explicit for an explorer.

Announce the activity, change type when applicable, workspace mode, and session choice. Apply the user's choices first:

- `fork` for substantial inherited context; include the latest scope and decisions explicitly because history transfer may be incomplete.
- `create` for a self-contained task whose boundaries are clear.
- `direct` for a short discussion or small task that fits the main session.

Independently select `read-only explore`, `small implement`, or `pr implement`. Inspect current changes and active ownership before writing. A read-only branch can share the checkout. Small writers need disjoint ownership or serial execution; PR-bound work needs a dedicated branch/worktree and a known base. Discover the existing branch convention rather than inventing a repository-wide policy.

## Dispatch With Available Capabilities

Check the host's actual task and workspace capabilities and follow its API constraints. If separate user-visible conversations are authorized, create or fork the task and send its packet. Have the branch first restate its assigned scope, read/write boundary, and return destination so inherited project-wide requests do not turn it into a second coordinator. Do not treat a task request queued for setup as an already running implementation; obtain the real task/workspace identifiers before using them.

When the API is unavailable, provide the packet in the current conversation for manual handoff. Explain the limitation and leave the task queued, or continue directly when consistent with the request. Do not install an orchestration dependency or promise automatic return without support.

Record observed task ID or link, branch, worktree path, base revision, ownership, and return destination in the cockpit when persistence is in scope. Never fabricate a task link. Branch sessions do not update the shared cockpit, even when a copied state file exists in their worktree.

## Receive the Result

When coordination includes following the task through completion, use the host's bounded task-status or wait capability. Keep the user informed of meaningful progress. Record attention requests, failures, and missing results rather than treating dispatch as completion.

Ask the branch to return findings or changes, exact checks and outcomes, the tested revision and dirty-state context, unresolved items, and a recommended next action. A chat report is sufficient; use [the report template](../../dev-flow/templates/report.md) for larger work.

Send returned work to the main session's `agent-gate` assessment. The branch does not merge, open a PR, or expand its task because it believes the work is ready; those actions require applicable user authorization and coordination with the main session.
