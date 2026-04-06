# 个人项目级 CLAUDE.md

`docs/src/README.md` 是项目文档的唯一入口，Claude Code 理解项目时从这里开始。它只维护稳定内容：项目定位、快速开始、文档导航。实现细节由各 skill 写入对应目录。

复制下面的内容到项目级 CLAUDE.md 作为初始

# CLAUDE.md

## Documentation Entry
- Default to using `docs/src/README.md` as the first entry point for understanding this project.
- Before making assumptions about project structure, script purpose, workflows, or safety notes, read `docs/src/README.md` first.
- `docs/src/README.md` only maintains: project overview, quick start, and documentation navigation. Do not record implementation details here; those belong in the respective skill output directories.
- When a task changes project structure, script usage, run commands, or risk/safety guidance, update `docs/src/README.md` to keep it in sync with the repository.
- When creating, deleting, renaming, or moving Markdown documents under `docs/src/`, always update `docs/src/SUMMARY.md` in the same task so the mdBook table of contents stays accurate.
- When updating `docs/src/SUMMARY.md`, prefer filling existing empty placeholder links over appending new entries at the end.
- When the user explicitly asks for a change, decision, convention, or detail to be documented, record it in `docs/src/README.md`.
- When making a change that seems important for future understanding of the repository, proactively update `docs/src/README.md` even if the user did not separately remind you.

## Documentation Paths
# Overrides the default paths used by /mdplan, /mdreview, /mdexplain, /mdlearn, /mdadr skills.
- Plan documents go in `docs/src/plan/`
- Review documents go in `docs/src/review/`
- Change summary documents go in `docs/src/explain/`
- Learning guides go in `docs/src/learn/`
- Architecture decision records go in `docs/src/adr/`
- Archived documents go in `docs/src/archive/`
- Always update `docs/src/SUMMARY.md` after creating any document under `docs/src/`

