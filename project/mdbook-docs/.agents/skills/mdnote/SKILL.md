---
name: mdnote
description: Capture a concise personal note from a user idea or visible conversation context without turning it into an implementation plan. Use when the user wants to preserve a thought, hypothesis, prompt, or open question.
---

按以下步骤执行：

1. 读取并遵守 `../_shared/chinese-engineering-writing.md`。
2. 定位 mdBook 根目录。候选可以是 `docs/` 或 `docs/<自定义名称>/`，且必须同时包含 `book.toml` 和 `src/`。只有一个候选时使用该目录；有多个候选时询问用户。后续路径都基于 `<mdbook-root>/src/`。
3. 确定记录范围。可以使用当前用户消息，以及当前可见对话中理解该想法所必需的用户补充、Agent 提问和用户确认。不要记录隐藏推理。Agent 提议与用户观点必须明确区分。
4. 默认直接记录，不主动评价或扩展。只有用户明确要求通过对话梳理时，才在写入前提出必要的简短问题。
5. 在 `<mdbook-root>/src/notes/` 创建笔记。文件名使用当天日期前缀和 kebab-case 主题，例如 `2026-04-24-mujoco-control-rate-idea.md`。

按需使用以下章节，不要为了结构完整而补充内容：

1. **想法**：忠实保留用户原意；若包含 Agent 提议，明确标注来源。
2. **已知背景**：只记录理解想法所必需的已知事实和对话上下文。
3. **待验证问题**：只记录用户提出或对话中已经形成的问题，不主动扩展新问题。
4. **相关文档**：链接直接相关的 plan、learn 或 ADR。
5. **原始请求**：按共享规范折叠放在文末。

用户只提供一句想法时，正文也可以只有一句。不要主动形成实施计划。

6. 更新 `<mdbook-root>/src/SUMMARY.md`。保留 `- [个人笔记]()` 分类标题，在其下添加二级子项，例如 `  - [MuJoCo 控制频率想法](./notes/2026-04-24-mujoco-control-rate-idea.md)`。不要替换分类标题，也不要追加孤立条目。
7. 写完后停止。除非用户明确要求，不得建议实施或继续展开讨论。

$ARGUMENTS
