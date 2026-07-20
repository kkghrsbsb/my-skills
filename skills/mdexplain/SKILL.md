---
name: mdexplain
description: Summarize code changes into a documented explanation. Triggers on requests to explain or document what was implemented.
---

按以下步骤执行：

0. 定位 mdBook 根目录：先查找当前项目的 mdBook 根目录，可能是 `docs/`，也可能是 `docs/<自定义名称>/`；有且只有一个候选时使用该目录，若多个候选同时存在，询问用户选择。后续所有文档路径都基于 `<mdbook-root>/src/`，不要默认写死为 `docs/src/`。
1. 阅读相关变更文件或指定代码。
2. 找到项目文档目录：使用 `<mdbook-root>/src/explain/`，若不存在则创建该目录。
3. 创建说明文档，文件名必须使用当天日期前缀 `YYYY-MM-DD-` 加 kebab-case 主题，如 `2026-04-24-user-auth-explain.md`，内容包含：
   - 原始 Prompt 引用块：紧跟主标题，先写 `> **原始 Prompt**`，再逐字引用触发此 skill 的完整用户消息，保留原始换行，不改写、不总结；不要包含 system、developer 或其他上下文消息
   - 改动了什么
   - 为什么改动
   - 影响了哪些部分
   - 潜在风险或兼容性注意事项
   - 若已有对应的 plan 文档，注明与原方案的差异（不重复背景内容，直接引用 plan 文件）
   - 原理性内容不在此展开，指向对应的 `learn/` 文档
4. 更新 `<mdbook-root>/src/SUMMARY.md`：保留 `- [解释说明]()` 分类标题不变，在其下面添加二级子项链接，例如 `  - [用户认证改动说明](./explain/2026-04-24-user-auth-explain.md)`。不要把 `- [解释说明]()` 本身替换成文档链接，也不要在末尾追加孤立条目。
5. 写完后停止，除非用户明确要求继续。

若用户在实施后调用此 skill，则先完成实施，再执行上述步骤总结改动。

$ARGUMENTS
