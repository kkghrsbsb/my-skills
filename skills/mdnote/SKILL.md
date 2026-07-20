---
name: mdnote
description: Write a personal note capturing ideas, thoughts, prompts, or exploratory directions. Triggers when the user wants to record a thought, hypothesis, or open question without immediately acting on it.
---

按以下步骤执行：

0. 定位 mdBook 根目录：先查找当前项目的 mdBook 根目录，可能是 `docs/`，也可能是 `docs/<自定义名称>/`；有且只有一个候选时使用该目录，若多个候选同时存在，询问用户选择。后续所有文档路径都基于 `<mdbook-root>/src/`，不要默认写死为 `docs/src/`。
1. 接收用户的想法、思路或 prompt，不做评价，不主动扩展，忠实记录用户的原始表达。
2. 找到项目文档目录：使用 `<mdbook-root>/src/notes/`，若不存在则创建该目录。
3. 创建笔记文档，文件名必须使用当天日期前缀 `YYYY-MM-DD-` 加 kebab-case 主题，如 `2026-04-24-mujoco-control-rate-idea.md`，内容包含：
   - **原始 Prompt 引用块**：紧跟主标题，先写 `> **原始 Prompt**`，再逐字引用触发此 skill 的完整用户消息，保留原始换行，不改写、不总结；不要包含 system、developer 或其他上下文消息
   - **想法**：用户的原始描述，保持原意，不改写
   - **背景**（可选）：若用户提供了上下文，简要记录
   - **待探索的问题**（可选）：从想法中自然延伸出的开放性问题，若用户没有提及则留空
   - **相关文档**（可选）：关联的 plan、learn 或 adr 文件
4. 更新 `<mdbook-root>/src/SUMMARY.md`：保留 `- [个人笔记]()` 分类标题不变，在其下面添加二级子项链接，例如 `  - [MuJoCo 控制频率想法](./notes/2026-04-24-mujoco-control-rate-idea.md)`。不要把 `- [个人笔记]()` 本身替换成文档链接，也不要在末尾追加孤立条目。
5. 写完后停止，不得主动建议实施或展开讨论，除非用户明确要求。

**写作原则：**
- 这是用户的思考空间，不是任务文档，不要套用结构化模板强行填充
- 忠实于用户原始表达，避免过度整理导致原意丢失
- 中文写作

$ARGUMENTS
