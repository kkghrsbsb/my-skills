# my-skills

个人 skills 仓库，管理和备份个人 Claude Code / Codex skills。

## 安装

```bash
# 安装到 Claude Code
python3 install_claude.py

# 安装到 Codex
python3 install_codex.py
```

默认安装位置：

- Claude Code: `~/.claude/skills/`
- Codex: `~/.codex/skills/`

可通过环境变量覆盖安装根目录：

- Claude Code: `CLAUDE_HOME`
- Codex: `CODEX_HOME`

## mdBook 项目文档管理

文档类 skills 使用 [mdBook](https://github.com/rust-lang/mdBook) 记录开发过程。文档用于快速建立开发认知和追溯事实，不用于生成长篇报告。

```
# 传统模式：安装 mdBook 在项目 docs/ 中
cargo install mdbook
cd docs
mdbook init

# 项目根目录启用在线预览
mdbook serve docs
```

在 fork 或协作项目中，推荐使用个人隔离目录，避免占用项目正式 `docs/`：

```
mkdir -p docs/<自定义名称>
cd docs/<自定义名称>
mdbook init

# 项目根目录启用在线预览
mdbook serve docs/<自定义名称>
```

所有文档类 skill 会先定位 mdBook 根目录。根目录可以是 `docs/`，也可以是 `docs/<自定义名称>/`；若同时存在多个候选，会先询问用户选择。

忽略策略按项目关系选择：

- 个人仓库或希望保留文档源码：忽略 `<mdbook-root>/book/`
- fork 或协作仓库中的个人文档：可在项目根 `.gitignore` 忽略 `docs/<自定义名称>/`

### 文档设计原则

- 前 30 至 50 行应能说明当前状态。
- 结论前置，计划、现状、已实现和已验证事实明确区分。
- 涉及实现的结论尽量附文件路径、关键符号和验证结果。
- 详细背景和原理按需展开，不重复已有文档。
- Mermaid 仅用于确实需要可视化的复杂关系，使用前检查环境，缺失时降级为普通 Markdown。
- 完整原始 Prompt 折叠放在文末，不占用正文首屏。

所有文档 skill 共享 [中文工程文档写作规范](./skills/_shared/chinese-engineering-writing.md)。各 `SKILL.md` 只保留自身职责和模板差异。

### 文档工作流

| 命令 | 用途 | 输出位置 |
| --- | --- | --- |
| `/mdinit` | 在手动执行 `mdbook init` 后建立文档分类和导航 | `<mdbook-root>/` |
| `/mdplan <功能描述>` | 在改代码前记录推荐方案、实施清单和验收条件 | `<mdbook-root>/src/plan/` |
| `/mdexplain` | 根据实际 diff 记录最终行为、改动证据和验证结果 | `<mdbook-root>/src/explain/` |
| `/mdreview <文件或模块>` | 按严重程度记录有证据的代码问题和验证方式 | `<mdbook-root>/src/review/` |
| `/mdlearn <文件或概念>` | 建立模块的输入、处理、输出和核心调用模型 | `<mdbook-root>/src/learn/` |
| `/mdadr <决策描述>` | 记录技术决策、备选方案、代价和重新评估条件 | `<mdbook-root>/src/adr/` |
| `/mdnote <想法描述>` | 轻量保存想法、必要上下文和待验证问题 | `<mdbook-root>/src/notes/` |

`mdplan` 和 `mdreview` 生成文档后会停止，等待确认，不会自动修改代码。`mdnote` 不会主动把想法扩展为实施方案。

### 典型工作流

```
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

# 记录想法、思路或待探索的方向
/mdnote 我在想 xxx 是不是可以 xxx ，先记下来之后验证。

# 新项目接入
# 先在 docs/ 或 docs/<自定义名称>/ 目录执行 mdbook init，然后：
/mdinit
```

### 文件命名规范

所有 skill 生成的文档统一使用 `YYYY-MM-DD-<主题>-<类型>.md`，例如：
`2026-04-24-user-auth-plan.md`、`2026-04-24-001-use-dora-rs-adr.md`
