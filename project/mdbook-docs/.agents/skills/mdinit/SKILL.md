---
name: mdinit
description: Initialize a new mdBook engineering documentation structure in a user-specified docs/ directory or a named direct subdirectory. Use when the user asks to create or initialize project documentation with mdBook.
---

## 前提条件

必须由用户明确告知 mdBook 初始化位置。只接受：

- `docs/`
- `docs/<自定义名称>/`，适合 fork、协作仓库或个人隔离文档

若用户没有告知初始化位置，立即暂停：不执行脚本，不自动探测，不默认使用 `docs/`。提醒用户明确回复 `docs/` 或 `docs/<自定义名称>/` 后再继续。

可以轻量粗读项目元信息和顶层结构，但不要做深度源码分析或全项目扫描。

执行前读取并遵守 `../_shared/chinese-engineering-writing.md`。共享规范属于已安装 skill，不要把它复制到项目的 mdBook 目录。若共享文件不存在，停止并提示用户重新运行本仓库的安装脚本。

不要在初始化阶段运行 `mdbook-mermaid install`。后续文档确实需要 Mermaid 时，再按共享规范检查环境并按需启用。

---

## 执行步骤

### 1. 确定调用参数

在仓库根目录调用 `scripts/init_mdbook.py`。`--book-root` 必须传递用户明确给出的目录：

```bash
python3 <mdinit-skill-root>/scripts/init_mdbook.py \
  --book-root docs/ \
  [--project-name '<项目名>']
```

用户给出自定义目录时，将命令中的 `docs/` 替换为完整路径，例如 `docs/alice/`。不得传入 `.` 在仓库根目录初始化。

脚本会检查目标路径和 `mdbook` 命令，执行 `mdbook init`，完成重复初始化保护、origin URL 规范化、`book.toml` 更新、README 与 SUMMARY 写入、默认 `src/chapter_1.md` 删除，并执行首次构建。任何前置检查失败时，不得绕过脚本手工修改。

若缺少 `mdbook` 命令，报告缺失项并提醒用户安装。不得未经允许执行 `cargo install mdbook`。

若用户在 fork 或协作项目中未明确指定目录，暂停并建议使用 `docs/<自定义名称>/`，避免占用项目正式 `docs/`。

README 只包含项目标题，不套用共享规范的文档模板。不要添加项目简介、
文档导航、维护规则或占位内容。

后续文档工作流应在 SUMMARY 的对应分类标题下添加二级子项，不要把分类
标题改成文档链接。

---

## 完成后输出摘要

转述脚本输出的 mdBook 根目录、工具版本、构建结果、修改文件、删除文件和提示。不要声称执行了
脚本未报告的操作。

$ARGUMENTS
