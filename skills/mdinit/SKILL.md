---
name: mdinit
description: Initialize mdBook documentation structure in docs/ after the user has run `mdbook init`. Updates book.toml, creates README.md, resets SUMMARY.md, and cleans up stub files.
---

## 前提条件

此 skill 假设用户已在 `docs/` 目录中手动执行过 `mdbook init`，即 `docs/` 下已存在：
- `book.toml`
- `src/`
- `book/`

不要自行执行 `mdbook init`，不要读取整个项目源码，不要试图"理解项目"。

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

只读取项目根目录的 `./README.md`（若存在）作为参考，提取项目名称和简介，生成 `docs/src/README.md`。若根目录 README.md 不存在，则生成只含项目名和占位描述的最简版本。不要阅读其他项目文件。

生成内容用中文，格式如下：
```markdown
# <项目名>

<项目简介>

## 快速开始

<!-- TODO -->

## 项目结构

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

### 7. 删除 stub 文件

删除 `docs/src/SUMMARY.md` 原本引用的 stub 文件，通常是 `docs/src/chapter_1.md`。若文件不存在则跳过。

### 8. 提醒用户更新 .gitignore

输出以下提示，不要自动修改 .gitignore：
```
⚠️  请手动在项目根目录的 .gitignore 中添加以下内容以忽略 mdBook 构建产物：
docs/book/
```

---

## 完成后输出摘要

列出本次执行的所有操作：已修改的文件、已删除的文件、以及需要用户手动处理的事项。

$ARGUMENTS