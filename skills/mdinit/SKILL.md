---
name: mdinit
description: Initialize mdBook documentation structure after the user has run `mdbook init`. Supports either docs/ or an isolated namespaced directory under docs/ as the book root.
---

## 前提条件

此 skill 假设用户已在目标 mdBook 根目录中手动执行过 `mdbook init`。目标根目录可以是：
- `docs/`
- `docs/<自定义名称>/`，适合 fork、协作仓库或个人隔离文档

目标根目录下应已存在：
- `book.toml`
- `src/`
- `book/`

不要自行执行 `mdbook init`。可以轻量粗读项目元信息和顶层结构，但不要做深度源码分析或全项目扫描。

执行前读取并遵守 `../_shared/chinese-engineering-writing.md`。共享规范属于已安装 skill，不要把它复制到项目的 mdBook 目录。若共享文件不存在，停止并提示用户重新运行本仓库的安装脚本。

不要在初始化阶段运行 `mdbook-mermaid install`。后续文档确实需要 Mermaid 时，再按共享规范检查环境并按需启用。

---

## 执行步骤

### 1. 定位 mdBook 根目录

按以下顺序确定 mdBook 根目录，后续所有路径都相对此根目录展开：
1. 若用户明确指定目录或名称，如 `docs/kkghrsbsb/` 或 `kkghrsbsb`，使用 `docs/<名称>/`。
2. 若存在 `docs/book.toml` 和 `docs/src/`，将 `docs/` 作为候选。
3. 扫描 `docs/*/book.toml` 且同级存在 `src/` 的目录，将其作为候选。
4. 若只有一个候选，使用该候选。
5. 若存在多个候选，停止并询问用户选择哪个 mdBook 根目录。
6. 若没有候选，停止并提示用户先执行：
   - 传统模式：`cd docs && mdbook init`
   - 个人隔离模式：`mkdir -p docs/<名称> && cd docs/<名称> && mdbook init`

如果用户在 fork 或协作项目中未明确指定目录，优先建议使用 `docs/<自定义名称>/`，避免占用项目正式 `docs/`。

### 2. 检查是否已初始化过

检查 `<mdbook-root>/src/README.md` 是否已存在：
- 若已存在，停止执行，提示用户此项目文档结构已初始化，若需要重新初始化请明确确认，不得自动覆盖。
- 若不存在，继续执行。

### 3. 获取 GitHub 仓库 URL

按以下顺序尝试获取：
1. 运行 `git remote get-url origin`
2. 若结果是 SSH 格式（`git@github.com:user/repo.git`），转换为 HTTPS 格式（`https://github.com/user/repo`）
3. 去掉末尾的 `.git`
4. 若没有配置远程仓库，提示用户后续手动填写，`git-repository-url` 留空继续执行

### 4. 更新 book.toml

在 `<mdbook-root>/book.toml` 末尾追加：
```toml
[output.html]
git-repository-url = "<上一步获取的 URL>"
```

若 `[output.html]` 或 `git-repository-url` 已存在，不要重复追加；应在保留其他配置的前提下补充或更新 `git-repository-url`。

### 5. 生成 <mdbook-root>/src/README.md

创建 `<mdbook-root>/src/README.md`，只写项目标题。项目名优先使用用户明确提供的名称，否则使用项目根目录名称。

文件内容必须严格保持为：
```markdown
# <项目名>
```

README 是结构首页，不套用共享规范的文档模板。不要添加原始 Prompt、项目简介、当前目标、项目概览、文档导航、维护规则或占位内容。

### 6. 重置 <mdbook-root>/src/SUMMARY.md

将 `<mdbook-root>/src/SUMMARY.md` 内容替换为：
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

删除 `<mdbook-root>/src/SUMMARY.md` 原本引用的 stub 文件，通常是 `<mdbook-root>/src/chapter_1.md`。若文件不存在则跳过。

---

## 完成后输出摘要

列出本次执行的所有操作：已修改的文件和已删除的文件。

$ARGUMENTS
