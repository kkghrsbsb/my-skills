---
name: mdadr
description: Write a concise Architecture Decision Record with options, tradeoffs, and reevaluation conditions. Use when the user asks to record or explain a technical decision.
---

按以下步骤执行：

1. 读取并遵守 `../_shared/chinese-engineering-writing.md`。
2. 定位 mdBook 根目录。候选可以是 `docs/` 或 `docs/<自定义名称>/`，且必须同时包含 `book.toml` 和 `src/`。只有一个候选时使用该目录；有多个候选时询问用户。后续路径都基于 `<mdbook-root>/src/`。
3. 扫描 `<mdbook-root>/src/adr/`，检查同主题决策：
   - 若存在，询问用户是修订原决策，还是记录替代旧决策的新 ADR。
   - 若新 ADR 替代旧决策，在新文档中链接旧文件，并在旧文件开头添加 `> ⚠️ 此决策已被 [xxx-adr.md](../adr/xxx-adr.md) 替代`。不要删除旧文件。
4. 阅读决策当时的用户描述、约束和必要代码或配置。不要用当前视角虚构当时不存在的因素。
5. 在 `<mdbook-root>/src/adr/` 创建 ADR。文件名使用当天日期、三位序号和 kebab-case 主题，例如 `2026-04-24-001-use-dora-rs-over-ros2.md`。

文档按以下顺序组织：

1. **决策**：开头直接写最终选择。
2. **状态**：只使用“草稿”“已采纳”或“已替代”。
3. **决定因素**：列出推动选择的关键条件。
4. **背景与约束**：只保留理解决策所需的上下文。
5. **选项对比**：使用表格比较方案、优点、缺点和放弃原因；至少包含两个真实选项。
6. **选择理由**：说明所选方案如何满足决定因素。
7. **后果与代价**：同时记录正面影响、负面影响和需要接受的权衡。
8. **重新评估条件**：说明哪些约束、规模、成本或能力发生变化时应重新决策。
9. **相关文档**：链接被替代 ADR、plan、learn 或外部依据。
10. **原始请求**：按共享规范折叠放在文末。

6. 更新 `<mdbook-root>/src/SUMMARY.md`。保留 `- [决策记录]()` 分类标题，在其下添加二级子项，例如 `  - [采用 Dora RS 决策](./adr/2026-04-24-001-use-dora-rs-over-ros2.md)`。不要替换分类标题，也不要追加孤立条目。
7. 写完后停止，除非用户明确要求继续。

$ARGUMENTS
