---
name: mdplan
description: Write a concise, executable feature plan before touching code. Use when the user asks to plan, design, or think through a new feature or implementation.
---

先不要改代码。

1. 读取并遵守 `../_shared/chinese-engineering-writing.md`。
2. 定位 mdBook 根目录。候选可以是 `docs/` 或 `docs/<自定义名称>/`，且必须同时包含 `book.toml` 和 `src/`。只有一个候选时使用该目录；有多个候选时询问用户。后续路径都基于 `<mdbook-root>/src/`。
3. 扫描 `<mdbook-root>/src/plan/`，检查是否已有同主题文档：
   - 若存在，询问用户是创建新版本，还是修订原文件。
   - 若需要归档，将旧文件移动到 `<mdbook-root>/src/archive/`，并在 `SUMMARY.md` 的 `- [归档]()` 下添加子项。
4. 阅读与需求直接相关的代码、配置和现有文档。区分当前事实、计划内容和待确认信息。
5. 在 `<mdbook-root>/src/plan/` 创建计划文档。文件名使用当天日期前缀和 kebab-case 主题，例如 `2026-04-24-user-auth-plan.md`。

文档按以下顺序组织：

1. **一句话结论**：先写推荐方案，不超过 2 句。
2. **目标**：写清预期行为和可观察结果。
3. **当前约束**：只写会影响方案的现有限制。
4. **推荐方案**：说明关键设计和必要取舍。
5. **关键流程或数据流**：符合共享规范的必要性和环境条件时使用 Mermaid 图。
6. **影响范围**：列出确定的文件、模块和关键符号；无法确定的项目标记为“待确认”，不得虚构。
7. **实施清单**：使用可逐项执行的编号步骤。
8. **验收条件**：每项都必须可观察或可测试。
9. **风险与回退方式**：区分待验证风险和可执行回退操作。
10. **相关文档**：只链接直接相关的文档。
11. **原始请求**：按共享规范折叠放在文末。

不要生成与当前功能无关的技术背景。

6. 更新 `<mdbook-root>/src/SUMMARY.md`。保留 `- [方案]()` 分类标题，在其下添加二级子项，例如 `  - [用户认证方案](./plan/2026-04-24-user-auth-plan.md)`。不要替换分类标题，也不要追加孤立条目。
7. 写完后停止，等待用户确认。不得主动修改代码。

$ARGUMENTS
