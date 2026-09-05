# mdBook 项目文档管理

最后一次 Git 更改日期：2026-08-05。

这是一套可直接复制到项目根目录的 mdBook 工程文档工作流。文档用于快速建立开发认知和追溯事实，不用于生成长篇报告。

## 使用方式

在 `my-skills` 仓库根目录执行：

```bash
cp -R project/mdbook-docs/.agents \
  project/mdbook-docs/AGENTS.md \
  project/mdbook-docs/CLAUDE.md \
  <目标项目>/
```

工作流包含 `.agents/skills/`、`AGENTS.md` 和 `CLAUDE.md`。复制前检查目标项目是否已有同名文件，避免覆盖现有约定。

## 初始化 mdBook

```bash
cargo install mdbook

# 在项目根目录调用，必须明确给出初始化位置
/mdinit docs/

# 从项目根目录预览
mdbook serve docs
```

在 fork 或协作项目中，推荐使用个人隔离目录，避免占用项目正式 `docs/`：

```bash
/mdinit docs/<自定义名称>/

# 从项目根目录预览
mdbook serve docs/<自定义名称>
```

`mdinit` 会执行 `mdbook init` 并建立文档分类。若用户未告知初始化位置，`mdinit` 会暂停并请用户明确指定，不会默认使用 `docs/`。其他文档 skills 会先定位已初始化的 mdBook 根目录；同时存在多个候选时会先询问用户。

忽略策略按项目关系选择：

- 个人仓库或需要保留文档源码：忽略 `<mdbook-root>/book/`
- fork 或协作仓库中的个人文档：可在项目根 `.gitignore` 忽略 `docs/<自定义名称>/`

## 文档设计原则

- 前 30 至 50 行应能说明当前状态。
- 结论前置，明确区分计划、现状、已实现和已验证事实。
- 涉及实现的结论尽量附文件路径、关键符号和验证结果。
- 详细背景和原理按需展开，不重复已有文档。
- Mermaid 仅用于确实需要可视化的复杂关系。
- 完整原始 Prompt 折叠放在文末，不占用正文首屏。

所有文档 skill 共享 [中文工程文档写作规范](./.agents/skills/_shared/chinese-engineering-writing.md)。各 `SKILL.md` 只保留自身职责和模板差异。

## 文档工作流

| 命令 | 用途 | 输出位置 |
| --- | --- | --- |
| `/mdinit <docs 路径>` | 在指定位置初始化 mdBook 并建立文档分类和导航 | `<mdbook-root>/` |
| `/mdplan <功能描述>` | 在改代码前记录推荐方案、实施清单和验收条件 | `<mdbook-root>/src/plan/` |
| `/mdexplain` | 根据实际 diff 记录最终行为、改动证据和验证结果 | `<mdbook-root>/src/explain/` |
| `/mdreview <文件或模块>` | 按严重程度记录有证据的代码问题和验证方式 | `<mdbook-root>/src/review/` |
| `/mdlearn <文件或概念>` | 建立模块的输入、处理、输出和核心调用模型 | `<mdbook-root>/src/learn/` |
| `/mdadr <决策描述>` | 记录技术决策、备选方案、代价和重新评估条件 | `<mdbook-root>/src/adr/` |
| `/mdnote <想法描述>` | 轻量保存想法、必要上下文和待验证问题 | `<mdbook-root>/src/notes/` |

`mdplan` 和 `mdreview` 生成文档后会停止并等待确认，不会自动修改代码。`mdnote` 不会主动把想法扩展为实施方案。

## 典型工作流

```text
# 新功能开发
/mdplan 添加 xxx 功能，实现要求 xxx
→ 确认方案后开始实现
/mdexplain
→ 实现完记录改动
/mycommit

# 代码审查
/mdreview src/auth/

# 学习理解
/mdlearn src/dataflow/node.rs 如何构建？

# 记录技术选型
/mdadr 选择 xxx 而非 xxx 作为架构

# 记录想法
/mdnote 我在想 xxx 是不是可以 xxx，先记下来之后验证。

# 新项目接入
# 正式项目文档
/mdinit docs/

# fork 或协作仓库的隔离文档
/mdinit docs/<自定义名称>/
```

## 文件命名规范

所有 skill 生成的文档统一使用 `YYYY-MM-DD-<主题>-<类型>.md`，例如 `2026-04-24-user-auth-plan.md` 和 `2026-04-24-001-use-dora-rs-adr.md`。
