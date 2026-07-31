---
name: mdstudy-init
description: Initialize an image-first mdBook project for personal study, research, courses, or domain notes. Use when the user asks to create, start, or configure a learning notebook or says they want to study a subject with mdBook, including implicit requests such as "构建 mdBook 记录机器人学笔记".
---

# 初始化学习笔记

1. 确认当前目录是用户要初始化的项目根目录。若已有 `book.toml`，不得重新初始化。
2. 从用户表述推测具体书名。例如“记录学机器人学的笔记”可使用“机器人学学习笔记”。若用户未提供可推测的领域、课程或书名，停止并询问。
3. 运行 `scripts/init_book.py --title '<书名>' --root .`。脚本会检查 `cargo`、`mdbook`、`mdbook-katex` 和 `mdbook-mermaid`，初始化根目录，配置预处理器并执行首次构建。
4. 命令缺失时，报告缺失项并请求安装许可。不得未经允许执行 `cargo install`。版本不同不是失败条件；先以 `mdbook build` 结果为准，只在构建问题有版本证据时建议调整。参考版本为 `mdbook 0.5.4`、`mdbook-katex 0.10.0`、`mdbook-mermaid 0.17.0`。
5. 用户明确要求 GitHub Pages 时，传入 `--with-pages-workflow`。未要求时只在完成摘要中提醒可以稍后配置，不创建 workflow。
6. 用户明确要求创建远程仓库时，先检查 `git` 配置、`gh auth status` 和当前仓库状态。明确展示仓库名与可见性后获得许可；默认建议 private，但不得默认执行创建、push 或开启 Pages。
7. 列出书名、生成文件、工具版本和构建结果。

不要在初始化时预设领域目录。等首批真实笔记出现后再根据内容建立结构。

$ARGUMENTS
