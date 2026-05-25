# 个人 CLAUDE.md 模板

这是个人通用文档工作流模板。优先放在 `.claude/CLAUDE.md` 这类个人 Claude Code 配置目录中；只有当项目团队也接受这套规则时，才放到仓库根目录 `CLAUDE.md`。

复制下面的内容到个人或项目级 CLAUDE.md 作为初始

# CLAUDE.md

## Documentation Rules
- The mdBook root may be `docs/` or an isolated personal directory such as `docs/<name>/`.
- Before writing documentation, locate the active mdBook root by checking for `book.toml` and `src/`; if multiple candidates exist, ask which one to use.
- `<mdbook-root>/src/README.md` is only the mdBook homepage for the current documentation context, not an agent instruction file.
- Keep agent operating rules in AGENTS.md or CLAUDE.md, not in `<mdbook-root>/src/README.md`.
- When changing Markdown files under `<mdbook-root>/src/`, update `<mdbook-root>/src/SUMMARY.md` in the same task.
- When updating `<mdbook-root>/src/SUMMARY.md`, keep category headings such as `- [方案]()` unchanged and add documents as nested child links below them.
- Example: add `  - [用户认证方案](./plan/2026-04-24-user-auth-plan.md)` below `- [方案]()` instead of replacing the category link.
- Use file names with an exact date prefix: `YYYY-MM-DD-kebab-case-topic.md`.

## Documentation Paths
# Overrides the default paths used by /mdplan, /mdreview, /mdexplain, /mdlearn, /mdadr skills.
- Plan documents go in `<mdbook-root>/src/plan/`
- Review documents go in `<mdbook-root>/src/review/`
- Change summary documents go in `<mdbook-root>/src/explain/`
- Learning guides go in `<mdbook-root>/src/learn/`
- Architecture decision records go in `<mdbook-root>/src/adr/`
- Archived documents go in `<mdbook-root>/src/archive/`
- Always update `<mdbook-root>/src/SUMMARY.md` after creating any document under `<mdbook-root>/src/`
- Personal notes go in `<mdbook-root>/src/notes/`
