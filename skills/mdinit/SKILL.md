---
name: mdinit
description: Initialize mdBook documentation structure in docs/ after the user has run `mdbook init`. Updates book.toml, creates README.md, resets SUMMARY.md, and cleans up stub files.
---

## 前提条件

此 skill 假设用户已在 `docs/` 目录中手动执行过 `mdbook init`，即 `docs/` 下已存在：
- `book.toml`
- `src/`
- `book/`

不要自行执行 `mdbook init`。可以轻量粗读项目元信息和顶层结构，但不要做深度源码分析或全项目扫描。

---

## 执行步骤

### 1. 确认 mdbook init 已执行

检查 `docs/book.toml` 是否存在。若不存在，停止并提示用户先在 `docs/` 目录中执行 `mdbook init`。

### 2. 检查是否已初始化过

检查 `docs/src/README.md` 是否已存在：
- 若已存在，停止执行，提示用户此项目文档结构已初始化，若需要重新初始化请明确确认，不得自动覆盖。
- 若不存在，继续执行。

### 3. 获取 GitHub 仓库 URL

按以下顺序尝试获取：
1. 运行 `git remote get-url origin`
2. 若结果是 SSH 格式（`git@github.com:user/repo.git`），转换为 HTTPS 格式（`https://github.com/user/repo`）
3. 去掉末尾的 `.git`
4. 若没有配置远程仓库，提示用户后续手动填写，`git-repository-url` 留空继续执行

### 4. 更新 book.toml

在 `docs/book.toml` 末尾追加：
```toml
[output.html]
git-repository-url = "<上一步获取的 URL>"
```

### 5. 生成 docs/src/README.md

结合用户调用此 skill 时提供的背景说明、项目根目录 `README.md`（若存在）、常见项目清单文件（如 `package.json`、`Cargo.toml`、`pyproject.toml`、`go.mod`）和顶层目录结构，生成 `docs/src/README.md`。

`docs/src/README.md` 是 mdBook 文档集首页，用来说明这套文档当下服务的工作目标和项目背景，不是 agent 理解项目时必须先看的规则入口。不要把 AGENTS.md、CLAUDE.md、长期维护规则或文档导航重复搬进这里。

生成内容用中文，格式如下：
```markdown
# <项目名>

<项目背景或一句话简介>

## 当前目标

<用户本次建立文档的原因和目标；若用户未说明则写 TODO>

## 项目概览

<!-- TODO -->
```

### 6. 重置 docs/src/SUMMARY.md

将 `docs/src/SUMMARY.md` 内容替换为：
```markdown
# Summary

- [README](./README.md)

- [个人笔记]()

- [方案]()

- [解释说明]()

- [审查报告]()

- [学习笔记]()

- [决策记录]()

- [归档]()
```

后续所有文档工作流都应在对应分类标题下面添加二级子项，不要直接把分类标题改成文档链接。例如：
```markdown
- [方案]()
  - [用户认证方案](./plan/2026-04-24-user-auth-plan.md)
```

### 7. 删除 stub 文件

删除 `docs/src/SUMMARY.md` 原本引用的 stub 文件，通常是 `docs/src/chapter_1.md`。若文件不存在则跳过。

---

## 完成后输出摘要

列出本次执行的所有操作：已修改的文件和已删除的文件。

$ARGUMENTS
