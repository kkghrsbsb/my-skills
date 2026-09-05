---
name: agent-plan
description: Turn a repository development request into a bounded feature or fix task with an approach, workspace choice, and verifiable acceptance criteria. Also triage uncertain bugs into diagnosis before implementation.
---

# Agent Plan

Read [the shared protocol](../../dev-flow/protocol.md). Work from the user's request, applicable project instructions, current repository evidence, and any existing cockpit. Respect whether the user requested planning only or end-to-end implementation.

## Choose the Next Useful Activity

Separate the activity (`plan`, `explore`, `diagnose`, or `implement`) from the change type (`feature`, `fix`, or a project-specific type). State the workspace and session choice with a short reason. For a small, well-understood change, a few sentences can be the whole plan.

If unfamiliarity prevents a sound implementation decision, define a focused read-only exploration question. Avoid commissioning an entire repository audit for a local change. For bugs, gather reproduction conditions and evidence for competing explanations before choosing a fix. State the supported root cause, or what observation is still needed; do not present an untested guess as a diagnosis.

Check for existing behavior, utilities, tests, and relevant project decisions before introducing new machinery. Prefer an existing project mechanism when it serves the requirement. Explain a meaningful alternative only when its tradeoff could change the user's decision.

## Make the Task Executable

For a substantial handoff, use [the task template](../../dev-flow/templates/task.md). Include:

- The user-visible outcome, scope, and explicit non-goals.
- The proposed approach and evidence supporting it.
- Observable acceptance criteria, with focused checks for the behavior and its likely failure cases.
- Needed context, task dependencies, file ownership, and the starting revision or unknown baseline.
- The workspace and session choices, authorized actions, and expected report.

Split tasks by independently assessable outcomes. Resolve shared interfaces before parallel implementation; separate file lists alone do not remove behavioral dependencies. Keep tightly coupled work together or sequence it.

Name the assumption most likely to invalidate the plan and the cheapest way to check it. Ask only when missing information changes the outcome, scope, or authorization. Carry forward decisions the user has already made.

## Handoff

For a planning-only request, return the plan and stop before code changes. For an authorized implementation request, continue directly or use `agent-branch` when the chosen separate-session workflow is authorized. Do not require approval merely because a plan was produced.

When persistence is in scope, the main session records the agreed task and next step in the cockpit. Keep rejected ideas out of the active queue; record a consequential rejection only when it will help future decisions.
