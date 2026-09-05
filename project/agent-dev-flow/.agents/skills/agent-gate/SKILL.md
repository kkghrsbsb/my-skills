---
name: agent-gate
description: Assess returned branch-session work against its task, actual diff, and verification evidence, then decide the next development or delivery action. Use for main-session handoff review and integration checks.
---

# Agent Gate

Read [the shared protocol](../../dev-flow/protocol.md). This is the coordinator's assessment of completed or interrupted work, not an automatic merge or release command.

## Establish What Was Returned

Read the task and report, then inspect the available result. Identify the task's baseline, returned revision or current dirty worktree, and actual changed files. Missing artifacts mean the result is not yet assessable; a confident report cannot substitute for them.

For exploration or diagnosis, check that findings cite real code or observations and distinguish unknowns. Decide whether the evidence supports implementation or calls for a narrower investigation. Do not force a code-test gate onto a reading task.

For implementation, review the actual diff against scope, acceptance criteria, project conventions, and affected callers. Present actionable findings by severity with file locations. Distinguish pre-existing problems from regressions and unrelated user changes.

## Check the Evidence

Relate each material acceptance criterion to a check or explain what is unverified. Keep reported checks separate from checks independently run by the main session. A command that was planned, interrupted, or skipped did not pass.

A green test on another revision does not cover later edits. Check the tested commit and uncommitted changes, then rerun affected verification when the result changed. Respect the chosen workspace policy: tests that write cannot run under a strictly read-only review without suitable isolation or authorized mode change. Missing dependencies do not authorize installation by themselves.

When authorized to integrate, inspect the destination's current changes first, integrate only task-owned changes, and verify the combined result. Review overlapping interfaces even when files are disjoint. Resolve conflicts within task scope and existing authorization; ask only when resolution requires a consequential new decision. Never report integration as verified using only the individual branches' tests.

## Decide and Record

Give a concise assessment: accepted for the task's purpose, needs changes, or blocked by specified missing evidence. Separate this assessment from delivery status. A useful report includes what changed, what was checked, unresolved findings, and the recommended next action.

The main session may continue, request a scoped revision, integrate, prepare or open a PR, or drop the task according to the user's authorization. A PR request can be carried through when already authorized; otherwise keep the proposal local. Do not repeat approval questions for actions already covered.

Only mark the task `done` when its own acceptance criteria are met; record whether delivery is local, committed, PR opened, or merged separately, with evidence. An unmerged PR may satisfy a task to prepare a PR, but not a task to merge it. Mark returned work `ready` while assessment is pending, and keep missing verification explicit. Update the main cockpit at this checkpoint when persistence is in scope.
