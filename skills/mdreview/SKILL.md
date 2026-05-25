---
name: mdreview
description: Write a code review document for specified files or recent changes. Triggers on requests to review, audit, or inspect code.
---

先不要改代码。

**定位 mdBook 根目录：**
- 先查找当前项目的 mdBook 根目录，可能是 `docs/`，也可能是 `docs/<自定义名称>/`
- 有且只有一个候选时使用该目录；若多个候选同时存在，询问用户选择
- 后续所有文档路径都基于 `<mdbook-root>/src/`，不要默认写死为 `docs/src/`

**确定审查范围：**
- 若有参数，以参数指定的文件或模块为准
- 若无参数，运行 `git diff HEAD --name-only` 获取最近变更的文件列表，以这些文件为审查范围
- 若 diff 为空且无参数，提示用户说明要审查的文件或模块，停止执行

按以下步骤执行：

1. 阅读审查范围内的代码文件、关联模块和现有行为。
2. 识别以下类型的问题：
   - 逻辑错误
   - 脆弱的假设
   - 缺失的校验
   - 结构不合理
   - 命名不清晰
   - 死代码
   - 性能问题
   - 可维护性风险
3. 找到项目文档目录：使用 `<mdbook-root>/src/review/`，若不存在则创建该目录。
4. 创建 review 文档，文件名必须使用当天日期前缀 `YYYY-MM-DD-` 加 kebab-case 主题，如 `2026-04-24-auth-module-review.md`，内容包含：
   - 审查范围
   - 发现的问题（按严重程度排序）
   - 具体修改建议
5. 更新 `<mdbook-root>/src/SUMMARY.md`：保留 `- [审查报告]()` 分类标题不变，在其下面添加二级子项链接，例如 `  - [认证模块审查](./review/2026-04-24-auth-module-review.md)`。不要把 `- [审查报告]()` 本身替换成文档链接，也不要在末尾追加孤立条目。
6. 写完后停止，等待用户确认，不得主动开始改代码。

$ARGUMENTS
