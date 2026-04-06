---
name: mdnote
description: Write a personal note capturing ideas, thoughts, prompts, or exploratory directions. Triggers when the user wants to record a thought, hypothesis, or open question without immediately acting on it.
---

按以下步骤执行：

1. 接收用户的想法、思路或 prompt，不做评价，不主动扩展，忠实记录用户的原始表达。
2. 找到项目文档目录：优先使用 `docs/src/notes/`，若不存在则创建该目录。
3. 创建笔记文档，文件名使用 kebab-case 加日期前缀，如 `2026-04-mujoco-control-rate-idea.md`，内容包含：
   - **想法**：用户的原始描述，保持原意，不改写
   - **背景**（可选）：若用户提供了上下文，简要记录
   - **待探索的问题**（可选）：从想法中自然延伸出的开放性问题，若用户没有提及则留空
   - **相关文档**（可选）：关联的 plan、learn 或 adr 文件
4. 更新 `docs/src/SUMMARY.md`：优先填充 `- [个人笔记]()` 下已有的空链接占位符，而不是在末尾追加新条目。
5. 写完后停止，不得主动建议实施或展开讨论，除非用户明确要求。

**写作原则：**
- 这是用户的思考空间，不是任务文档，不要套用结构化模板强行填充
- 忠实于用户原始表达，避免过度整理导致原意丢失
- 中文写作

$ARGUMENTS