---
name: mdlearn
description: Write a learning guide explaining how code or architecture works. Triggers on requests to understand, learn, or get an explanation of how something is designed.
---

按以下步骤执行：

1. 阅读指定的代码文件、模块或架构相关文件。
2. 找到项目文档目录：优先使用 `docs/src/learn/`，若不存在则选择项目中合适的文档位置。
3. 创建学习指南文档，文件名必须使用当天日期前缀 `YYYY-MM-DD-` 加 kebab-case 主题，如 `2026-04-24-dataflow-arch-learn.md`，内容围绕"理解"而非"记录变更"，包含：
   - **是什么**：概念或模块的定义和职责
   - **为什么这样设计**：设计动机、权衡和背景
   - **怎么工作的**：核心流程、关键路径、数据流向
   - **关键代码解读**：重要片段的逐步说明
   - **常见误区或注意点**：容易搞错的地方
   - **延伸阅读**（若存在明显相关模块或外部概念时补充）
4. 更新 `docs/src/SUMMARY.md`：保留 `- [学习笔记]()` 分类标题不变，在其下面添加二级子项链接，例如 `  - [数据流架构学习笔记](./learn/2026-04-24-dataflow-arch-learn.md)`。不要把 `- [学习笔记]()` 本身替换成文档链接，也不要在末尾追加孤立条目。
5. 写完后停止，除非用户明确要求继续。

**写作原则：**
- 面向"第一次接触这段代码的人"，不预设读者已有背景知识
- 优先解释"为什么"，而不只是"是什么"
- 用类比或示意说明复杂概念，避免纯罗列代码
- 中文写作

$ARGUMENTS
