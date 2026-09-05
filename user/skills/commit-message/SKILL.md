---
name: commit-message
description: Generate a Chinese Conventional Commits message from the current diff. Only run git commit when the user explicitly asks to commit.
---

Use this skill when the user wants a commit message, asks to prepare a commit, or explicitly asks to commit current changes.

Default to a conservative workflow:

- Inspect staged changes first with `git diff --cached`.
- If nothing is staged, inspect unstaged changes with `git diff HEAD`.
- Generate a Chinese Conventional Commits message from the inspected diff.
- Do not stage files or run `git commit` unless the user explicitly asks to commit.
- Do not claim tests, checks, or reviews were run unless they actually were.

When generating the message, use this format:

```text
<type>(<scope>): <summary>

 - <body bullet when useful>
```

Allowed `type` values:

- `feat`
- `fix`
- `refactor`
- `docs`
- `chore`
- `test`

Message rules:

- The subject must be Chinese, concise, and specific.
- Avoid vague summaries such as "更新", "修复问题", or "杂项改动".
- Add a short Chinese body for non-trivial changes, covering what changed, why, and any important risk or follow-up.
- Keep body bullets short; each line starts with ` - `.
- Omit the body for trivial changes.
- If the diff includes `Subproject commit`, mention submodule changes separately in the body.

If the user explicitly asks to commit:

- If staged changes exist, commit only staged changes.
- If no staged changes exist, ask before staging unstaged files unless the user's wording clearly authorizes staging all current inspected changes.
- Use the generated subject and body as the complete commit message without opening an interactive editor.
- Report the final commit message and commit hash when successful.
- If committing fails, report the reason and do not imply success.

$ARGUMENTS
