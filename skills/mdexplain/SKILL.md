---
name: mdexplain
description: Document implemented code changes as a concise, evidence-based change record. Use when the user asks to explain or record what was implemented.
---

按以下步骤执行：

1. 读取并遵守 `../_shared/chinese-engineering-writing.md`。
2. 定位 mdBook 根目录。候选可以是 `docs/` 或 `docs/<自定义名称>/`，且必须同时包含 `book.toml` 和 `src/`。只有一个候选时使用该目录；有多个候选时询问用户。后续路径都基于 `<mdbook-root>/src/`。
3. 以实际 diff 和当前代码为事实来源。阅读相关变更、关键符号、验证记录和对应 plan；不要把计划内容当作已实现事实。
4. 在 `<mdbook-root>/src/explain/` 创建说明文档。文件名使用当天日期前缀和 kebab-case 主题，例如 `2026-04-24-user-auth-explain.md`。

文档按以下顺序组织：

1. **一句话结果**：说明已经发生的结果，不超过 2 句。
2. **最终行为**：说明用户或系统现在可观察到的行为。
3. **改动清单**：优先使用表格，至少包含文件、关键符号和作用。
4. **关键调用链或数据流**：只说明理解改动所需的路径；符合共享规范的必要性和环境条件时使用 Mermaid 图。
5. **修改前后对比**：明确区分旧行为和新行为。
6. **验证**：列出实际执行的命令和结果。未执行测试时明确写“未执行”，不得表述为已验证。
7. **限制和未完成事项**：分别标记“待验证”或“未实现”。
8. **与原计划的偏差**：引用 plan，只记录差异，不重复背景；没有对应 plan 时省略。
9. **相关文档**：原理性内容链接到对应 learn 文档，不在此展开。
10. **原始请求**：按共享规范折叠放在文末。

5. 更新 `<mdbook-root>/src/SUMMARY.md`。保留 `- [解释说明]()` 分类标题，在其下添加二级子项，例如 `  - [用户认证改动说明](./explain/2026-04-24-user-auth-explain.md)`。不要替换分类标题，也不要追加孤立条目。
6. 写完后停止，除非用户明确要求继续。

若用户在同一请求中要求先实施再记录，完成实施和验证后再生成文档。否则不得把尚未实施的计划写成结果。

$ARGUMENTS
