---
name: mdstudy-ask
description: Read, search, compare, explain, or answer questions about handwritten image notes in an mdBook study project without changing the notebook. Use when the user asks what their notes say, where a concept appears, how an equation or diagram works, or requests synthesis across existing note images.
---

# 回答笔记内容问题

1. 从 `src/SUMMARY.md`、用户指定的章节、关键词或附件中确定最小阅读范围。
2. 按 Markdown 中的引用顺序查看相关图片。分析手写文字、公式、图形和页面之间的连续关系。
3. 明确区分：
   - 图片中可直接读取的内容；
   - 基于上下文的解释或推导；
   - 无法辨认或待确认的部分。
4. 回答时引用章节路径和必要的图片文件名，便于用户回看原笔记。
5. 默认只读。不要修改 Markdown、SUMMARY 或图片，也不要把回答自动写回笔记。用户要求保存分析结果时，改用 `mdstudy-note` 的写入规则。

$ARGUMENTS
