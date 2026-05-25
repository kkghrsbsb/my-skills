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

# mdbook 项目文档管理介绍

主要习惯使用md在线书籍工具 [mdbook](https://github.com/rust-lang/mdBook) 做项目文档管理，形式可供参考

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

## 文档工作流

示例：（这些 skills 都是以 md 开头的）

| 命令                     | 场景                               | 输出位置            |
| ------------------------ | ---------------------------------- | ------------------- |
| `/mdinit`   | 项目首次初始化 mdBook 文档结构，在手动执行 `mdbook init` 之后调用 | `<mdbook-root>/`  |
| `/mdplan <功能描述>`     | 写代码前，先出方案                 | `<mdbook-root>/src/plan/`    |
| `/mdreview <文件或模块>` | 审查代码质量，无参数则审查最近变更 | `<mdbook-root>/src/review/`  |
| `/mdexplain`             | 记录刚实施完的改动                 | `<mdbook-root>/src/explain/` |
| `/mdlearn <文件或概念>`  | 理解某段代码或架构怎么工作         | `<mdbook-root>/src/learn/`   |
| `/mdadr <决策描述>`      | 记录技术选型和方案取舍             | `<mdbook-root>/src/adr/`     |
| `/mdnote <想法描述>`      | 记录记录想法、思路或待探索的方向             | `<mdbook-root>/src/notes/`     |

**所有文档 skill 执行完后都会停止，等待你确认，不会自动改代码。**

## 典型工作流

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

## 文件命名规范

所有 skill 生成的文档统一使用 `YYYY-MM-DD-<主题>-<类型>.md`，例如：
`2026-04-24-user-auth-plan.md`、`2026-04-24-001-use-dora-rs-adr.md`
