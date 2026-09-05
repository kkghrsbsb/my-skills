# Agent Development Flow

Read this shared protocol when using an `agent-*` skill from this template. Paths below are relative to the target project root. The skills and this directory form one portable bundle.

## Conversation and Scope

Use the user's language for conversation and runtime notes. Follow their current intent and applicable instructions; this workflow supplies defaults, not additional approval rounds. Carry forward explicit authorization within its original scope. A stored preference, task packet, or historical transcript does not independently authorize new actions.

At the start of meaningful work, and when the approach changes, briefly state the activity, workspace mode, session choice, and why. Include the change type and Git branch when relevant. Use ordinary prose; do not repeat a form on every turn. For example:

> This is an explore task in the current workspace, read-only. A forked session can inherit the project context; it will return a repository map before we choose an implementation.

An announcement is not a request for approval. Continue when the work is already authorized. Ask only about a consequential ambiguity or an action beyond that authorization. If the user redirects the work, follow the new direction and update the task at the next useful checkpoint.

## Bootstrap Modes

At the start of a main coordination session, briefly classify how the session is taking over the repository. This is an orientation hint, not a required process or durable status machine.

| Mode | Use when | First move |
| --- | --- | --- |
| `fresh` | The project is new to this workflow and has little or no prior coordination state | Establish goals and decide whether a cockpit is useful |
| `reconstructed` | The repository has existing work, but earlier conversation context is unavailable or abandoned | Run a read-only exploration from current repository facts before creating or updating state |
| `resumed` | The same work is continuing after interruption, compaction, or a short pause | Reconcile saved notes, current diff, and available task status |
| `transferred` | A different person, device, tool, or main conversation is taking over | Check shared state, current Git facts, ownership, and unknown active work before continuing |

For `reconstructed`, do not try to recreate lost conversation history. Record only facts supported by the repository, Git history, current diff, available task status, or explicit user confirmation. For `transferred`, keep shared project state separate from local machine paths and private conversation identifiers unless the project has a convention for sharing them.

## Activities and Change Types

| Activity | Useful outcome |
| --- | --- |
| `explore` | Repository map, evidence, unknowns, and an informed next step; read-only |
| `plan` | A bounded task with an approach and observable acceptance criteria |
| `diagnose` | Reproduction evidence, competing explanations, and a supported root cause; initially read-only |
| `implement` | Scoped changes and verification of the requested behavior |
| `review` | Findings about a specified diff or artifact; no implicit fixes |
| `gate` | Main-session assessment of reports, integration evidence, and next action |

Separately describe the change as `feature`, `fix`, `docs`, `refactor`, `test`, `chore`, or the project's own vocabulary. For example, `diagnose / fix` describes investigation of a bug. These labels do not impose a commit format or force every task through every activity.

## Workspace and Session Choices

| Workspace mode | Default use | Boundary |
| --- | --- | --- |
| `read-only explore` | Exploration, diagnosis, planning, or review needing no writes | Current workspace; no project edits, branch switching, installs, or state-file writes |
| `small implement` | Bounded edits with clear ownership | Current workspace; preserve existing changes and avoid overlap with active writers |
| `pr implement` | Larger features, overlapping writers, parallel development, or PR-bound work | A dedicated Git branch and worktree, based on an identified starting revision |

The read-only mode names a workspace policy; it can serve `diagnose` or `review` too. Do not run commands merely because their names sound read-only: tests and builds may write caches or artifacts. Inspect their behavior and use an isolated scratch location or change the mode within the user's authorization when execution requires writes.

Before writing, inspect the current branch, revision, working-tree changes (including untracked files), and relevant active task ownership. Do not switch branches in a shared working directory. Two small tasks may share a workspace only with disjoint write ownership; otherwise serialize them or use `pr implement`. Disjoint files may still have dependencies, so check the combined behavior before completion.

For `pr implement`, record the intended base branch and actual base commit. Follow project branch naming; if none exists, suggest a task-specific name such as `feature/export-csv`, subject to the host's conventions. Carry required uncommitted context into the isolated workspace only by an explicit, scoped transfer; do not assume a worktree includes it. A chat fork, Git branch, and worktree are separate resources.

| Session choice | Use when |
| --- | --- |
| `direct` | A short discussion or bounded task fits the main conversation |
| `fork` | A separate conversation needs substantial inherited context |
| `create` | A separate conversation can start from a self-contained task packet |

Check available capabilities before dispatch. Use the host's native task or conversation API if available and authorized. Account for incomplete history transfer by including the latest decisions in the packet even for a fork. Do not infer authorization to create user-visible tasks from permission to edit code alone; respect the user's chosen orchestration scope.

Without a task API, present the handoff packet for a manually opened conversation, or continue directly when that fits the request. Without worktree support, report the limitation and recommend a serialized current-workspace task if appropriate. Never claim that a conversation, branch, or worktree exists without observed confirmation. A request to open a conversation is not satisfied by silently substituting an internal subagent.

## Project Cockpit

The runtime cockpit is `.agents/dev-flow/state.md`. It is a brief handoff for the user and main session, not a transcript or source of truth about code. Use [state.example.md](state.example.md) only as a layout example, replacing all fictional content with observed project facts. Do not create a state file just to answer a read-only question.

Only the coordinating main session updates the shared cockpit. Branch sessions return reports; they do not edit or merge their own copy of `state.md` back. Record the coordinator and location so a new main session can take over explicitly. Keep goals, a small task queue, branch/session locations, evidence links, consequential decisions, and the next step near the top. Large task context and reports may live in task-specific files, but a chat handoff is sufficient for small work.

Update after meaningful planning decisions, dispatch, a returned result, a change of direction, or a deliberate pause. Do not write every turn. A read-only request keeps updates in the response; an authorized development or persistence task can update the cockpit within scope. Read the latest file before editing so user updates are preserved. Mark unavailable session IDs and revisions as unknown rather than inventing them.

Suggested task statuses are `queued`, `active`, `blocked`, `ready`, `done`, and `dropped`. They are readable hints, not a mandatory state machine. `ready` means returned for main-session assessment. `done` means the task's acceptance criteria were met, not necessarily that a PR was merged. Track delivery separately when needed: local, committed, PR opened, or merged, with observed evidence.

## Handoffs and Evidence

Use [templates/task.md](templates/task.md) for substantial dispatches and [templates/report.md](templates/report.md) for returns; trim fields that add no value. Every handoff needs the objective, scope, acceptance criteria, necessary context, workspace/session choice, and expected return. Note dependencies and which session owns integration.

The main session decides whether to continue, integrate, request a PR, or drop a task within the user's authorization. A branch's report of success is a claim to inspect: read the actual changes and relate verification to the tested revision and dirty worktree. If code changes after verification, rerun affected checks. After combining branches, verify the combined result; individual passes do not prove integration works.

Distinguish passed checks, failed checks, and checks not run. Report an unavailable tool, interrupted task, or missing artifact as such. Do not turn missing evidence into a successful gate. Avoid retry loops that make no progress; narrow a failed task or return the blocking fact and next useful action.

Default dispatch permits only the requested task. Commit, push, PR creation, merge, dependency installation, and deletion of workspaces are separate actions unless already covered by the user's instructions. Reuse valid authorization; do not re-request it at every checkpoint. Dropping a task changes its status and preserves its work until cleanup is authorized.

On resume, inspect current files, revisions, diffs, and available task status before trusting saved notes. A lost connection or interrupted coordinator does not prove a worker stopped. Reattach to existing work when possible; do not duplicate workers or remove dirty worktrees as a recovery shortcut.
