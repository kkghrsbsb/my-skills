---
name: mdplan
description: Write a feature plan document before touching any code. Triggers on requests to plan, design, or think through a new feature or implementation.
---

先不要改代码。

**检查是否已有同主题文档：**
- 扫描 `docs/src/plan/` 下已有文件，判断是否存在同主题的 plan 文档
- 若存在，询问用户：是创建新版本文档，还是在原文件上修订？等待用户确认后再继续
- 若原文件需要归档，将其移动到 `docs/src/archive/` 并更新 SUMMARY.md 的归档节点

按以下步骤执行：

1. 理解功能需求：澄清预期行为、受影响的模块、输入输出、潜在风险和权衡。
2. 找到项目文档目录：优先使用 `docs/src/plan/`，若不存在则选择项目中合适的文档位置。
3. 创建 plan 文档，文件名使用 kebab-case 加日期前缀，如 `2026-04-user-auth-plan.md`，内容包含：
   - 功能目标
   - 当前问题或动机
   - 方案设计
   - 可能受影响的文件或模块
   - 潜在风险和边界情况
   - 实施步骤
4. 更新 `docs/src/SUMMARY.md`：优先填充 `- [方案]()` 下已有的空链接占位符，而不是在末尾追加新条目。
5. 写完后停止，等待用户确认，不得主动开始改代码。

$ARGUMENTS