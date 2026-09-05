# Agent Development Flow

This project uses a main conversation to coordinate development and bounded branch sessions when useful. Apply this workflow when the user requests project orientation, planning, session coordination, handoff assessment, or recovery. Ordinary bounded work can stay in the current conversation.

Read [.agents/dev-flow/protocol.md](.agents/dev-flow/protocol.md) when entering the workflow. Read only the skill needed for the current activity:

| Need | Skill |
| --- | --- |
| Learn an unfamiliar repository | [agent-orient](.agents/skills/agent-orient/SKILL.md) |
| Plan a bounded change or investigate a bug | [agent-plan](.agents/skills/agent-plan/SKILL.md) |
| Prepare and coordinate a branch session | [agent-branch](.agents/skills/agent-branch/SKILL.md) |
| Assess returned work and integration evidence | [agent-gate](.agents/skills/agent-gate/SKILL.md) |
| Recover existing tasks after a pause | [agent-resume](.agents/skills/agent-resume/SKILL.md) |

Briefly announce task activity, workspace mode, and session choice when starting meaningful work or changing direction. Treat these as reminders, not additional permission gates. Follow the user's choices and existing authorization within scope.

The runtime cockpit is `.agents/dev-flow/state.md`; only the main coordinator updates it. Branch sessions report back. Current code and observed task status take precedence over stored notes. Keep read-only requests read-only, including the cockpit.

The protocol and skill files are reusable instructions. `state.example.md` is fictional sample content; actual project state belongs in `state.md`. Preserve existing project-specific instructions when adopting this template.
