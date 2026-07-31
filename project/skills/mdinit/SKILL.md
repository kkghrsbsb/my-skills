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

### 1. 确定调用参数

在仓库根目录调用 `scripts/init_mdbook.py`。只传递用户已经明确给出的可选参数：

```bash
python3 <mdinit-skill-root>/scripts/init_mdbook.py \
  [--book-root docs/<名称>] \
  [--project-name '<项目名>']
```

脚本会确定唯一 mdBook 根目录，并在有多个候选时要求显式传入
`--book-root`。脚本还会完成重复初始化保护、origin URL 规范化、
`book.toml` 幂等更新、README 与 SUMMARY 写入，以及默认
`src/chapter_1.md` 的删除。任何前置检查失败时，不得绕过脚本手工修改。

若用户在 fork 或协作项目中未明确指定目录，优先建议使用
`docs/<自定义名称>/`，避免占用项目正式 `docs/`。

README 只包含项目标题，不套用共享规范的文档模板。不要添加项目简介、
文档导航、维护规则或占位内容。

后续文档工作流应在 SUMMARY 的对应分类标题下添加二级子项，不要把分类
标题改成文档链接。

---

## 完成后输出摘要

转述脚本输出的 mdBook 根目录、修改文件、删除文件和提示。不要声称执行了
脚本未报告的操作。

$ARGUMENTS
