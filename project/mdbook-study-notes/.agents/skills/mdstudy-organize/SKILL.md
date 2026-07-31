---
name: mdstudy-organize
description: Reorganize an mdBook study notebook, improve its chapter hierarchy and SUMMARY, and detect orphaned chapters, images, or broken links. Use when the user asks to tidy, organize, classify, restructure, audit, or repair the current notes or table of contents.
---

# 整理学习笔记

1. 阅读 `src/SUMMARY.md`、章节标题、目录和必要的图片内容，先建立当前笔记的主题模型。
2. 只在能降低查找成本时调整层级。目录以领域、课程、书籍或稳定主题为主，避免为少量笔记创建过深层级。
3. 允许按当前内容调整 `SUMMARY.md`，不强制预设分类。保持标题、目录和阅读顺序一致。
4. 需要移动章节时，将整个章节目录与 `images/` 一起移动。修正 SUMMARY 和所有相对链接。
5. 不要改变章节中图片的显示顺序，除非用户明确要求。不要为了整齐而重命名已入库图片。
6. 删除重复、孤立或无法引用的文件前，列出确切路径并获得确认。
7. 调整后运行：

   ```bash
   python3 <skill-root>/scripts/validate_book.py --root . --build
   ```

8. 报告新的章节层级、移动的路径、未解决的孤立文件和构建结果。

$ARGUMENTS
