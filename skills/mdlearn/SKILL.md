---
name: mdlearn
description: Write a concise learning guide that builds a working model of code or architecture. Use when the user asks to understand, learn, or explain how something is designed.
---

按以下步骤执行：

1. 读取并遵守 `../_shared/chinese-engineering-writing.md`。
2. 定位 mdBook 根目录。候选可以是 `docs/` 或 `docs/<自定义名称>/`，且必须同时包含 `book.toml` 和 `src/`。只有一个候选时使用该目录；有多个候选时询问用户。后续路径都基于 `<mdbook-root>/src/`。
3. 阅读指定代码、模块、配置和必要的关联文件。默认读者熟悉基本编程，但第一次接触当前项目。
4. 在 `<mdbook-root>/src/learn/` 创建学习文档。文件名使用当天日期前缀和 kebab-case 主题，例如 `2026-04-24-dataflow-arch-learn.md`。

文档按以下顺序组织：

1. **30 秒理解**：用最短内容说明模块职责、边界和核心机制。
2. **输入、处理和输出**：明确数据或控制从哪里来、如何变化、到哪里去。
3. **核心调用链或数据流**：先建立整体模型；复杂关系使用 Mermaid 图。
4. **关键文件和符号**：列出理解模块所需的路径、类、函数、结构体或配置项。
5. **为什么这样设计**：只解释与当前设计直接相关的动机和取舍。
6. **容易误解的点**：说明名称、边界或行为上容易产生的错误认识。
7. **进一步查看的位置**：链接相关文件、测试或文档。
8. **原始请求**：按共享规范折叠放在文末。

不要从通用计算机基础开始讲解，不默认写成完整教程，不逐行解释普通样板代码。只解释理解当前模块所必需的背景。用户明确要求深入学习时，才扩展原理和示例。

5. 更新 `<mdbook-root>/src/SUMMARY.md`。保留 `- [学习笔记]()` 分类标题，在其下添加二级子项，例如 `  - [数据流架构学习笔记](./learn/2026-04-24-dataflow-arch-learn.md)`。不要替换分类标题，也不要追加孤立条目。
6. 写完后停止，除非用户明确要求继续。

$ARGUMENTS
