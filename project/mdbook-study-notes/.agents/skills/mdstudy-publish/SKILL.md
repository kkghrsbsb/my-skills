---
name: mdstudy-publish
description: Validate, build, commit, and push an mdBook study notebook to its Git remote without waiting for GitHub Actions or Pages. Use when the user asks to upload, sync, push, or publish their notes, or to create a remote repository for them.
---

# 发布学习笔记

1. 检查 `git status`、当前分支、差异和远程仓库。已有远程时不运行 `gh auth status` 或 GitHub API。不得把无关变更混入笔记发布。
2. 运行 `python3 <mdstudy-organize-skill-root>/scripts/validate_book.py --root . --build`。检查大图片、断链、孤立文件、密钥和意外的临时文件。构建或检查失败时不得推送。
3. 没有远程仓库时：
   - 推测简洁的 kebab-case 仓库名；
   - 默认建议 private；
   - 向用户明确展示仓库名、owner 和可见性；
   - 只在这个分支中检查 `gh auth status`；
   - 获得许可后才运行 `gh repo create <name> --private --source=. --remote=origin`。
4. 使用中文 Conventional Commits 提交信息。若已有 staged 变更，只提交 staged 变更；否则只暂存本次笔记范围。
5. 用户要求“发布”、“上传”、“同步”或“push”时，可在提交后推送当前分支。不得强制推送、删除远程分支或改写远程历史。
6. push 成功即完成本 skill。返回 commit hash、推送分支和远程仓库 URL。若仓库包含 Pages workflow，只说明 push 会异步触发 workflow；不轮询 GitHub Actions、不查询 Pages API，不等待部署结果，也不声称 Pages 已部署成功。

$ARGUMENTS
