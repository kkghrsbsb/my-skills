---
name: mdstudy-note
description: Create, update, move, find, or delete image-first mdBook study notes and their attached handwritten-note images. Use when the user attaches note images and asks to save, add, insert, replace, reorder, move, rename, find, or remove notes or images, whether or not they explicitly name the skill.
---

# 管理图片学习笔记

1. 确认项目根目录包含 `book.toml`、`src/` 和 `src/SUMMARY.md`。
2. 按用户附件的原始顺序查看图片。可分析内容以判断领域、主题、章节名和存放位置，但不得因此自动生成文字笔记。
3. 用户指定章节时使用指定位置。未指定时，检查现有目录和章节：
   - 主题与现有章节一致时追加到该章节；
   - 属于现有领域但主题独立时新建章节；
   - 没有合适领域时新建简洁、可扩展的目录。
4. 每篇笔记默认使用 `<领域>/<主题>/README.md`，图片放在同级 `images/`。目录和文件使用稳定的 kebab-case 英文路径，章节标题可使用中文。
5. 对新建或追加图片，按附件顺序调用：

   ```bash
   python3 <skill-root>/scripts/import_images.py \
     --root . \
     --chapter '<领域>/<主题>/README.md' \
     [--title '<章节标题>'] \
     <图片1> <图片2> ...
   ```

   脚本只复制原图、去重、生成稳定文件名并追加图片引用；不裁切、不压缩、不 OCR。
6. 新建或移动章节后同步更新 `src/SUMMARY.md`。使用内容导向、简洁且层级合理的结构，不强制固定分类。
7. 未经用户要求，章节只写一级标题和按顺序排列的图片。图片 alt 文本使用中性编号，不得把推测内容写入 alt。
8. 用户要求插入或重排时，只调整 Markdown 中图片引用的顺序，不为了顺序重命名历史图片。
9. 删除、替换、覆盖图片或删除整篇章节前，列出确切目标并获得确认。移动时同时移动章节目录与 `images/`，并修正 SUMMARY。
10. 完成后运行 `mdbook build`，列出更改的章节、图片和 SUMMARY 项。

$ARGUMENTS
