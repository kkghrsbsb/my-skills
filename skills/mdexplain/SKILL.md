---
name: mdexplain
description: Summarize code changes into a documented explanation. Triggers on requests to explain or document what was implemented.
---

按以下步骤执行：

1. 阅读相关变更文件或指定代码。
2. 找到项目文档目录：优先使用 `docs/src/explain/`，若不存在则选择项目中合适的文档位置。
3. 创建说明文档，文件名必须使用当天日期前缀 `YYYY-MM-DD-` 加 kebab-case 主题，如 `2026-04-24-user-auth-explain.md`，内容包含：
   - 改动了什么
   - 为什么改动
   - 影响了哪些部分
   - 潜在风险或兼容性注意事项
   - 若已有对应的 plan 文档，注明与原方案的差异（不重复背景内容，直接引用 plan 文件）
   - 原理性内容不在此展开，指向对应的 `learn/` 文档
4. 更新 `docs/src/SUMMARY.md`：保留 `- [解释说明]()` 分类标题不变，在其下面添加二级子项链接，例如 `  - [用户认证改动说明](./explain/2026-04-24-user-auth-explain.md)`。不要把 `- [解释说明]()` 本身替换成文档链接，也不要在末尾追加孤立条目。
5. 写完后停止，除非用户明确要求继续。

若用户在实施后调用此 skill，则先完成实施，再执行上述步骤总结改动。

$ARGUMENTS
