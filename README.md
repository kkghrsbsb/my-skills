# my-skills

个人 skills 仓库，管理和备份个人 `~/.claude/skills/`

# mdbook 项目文档管理介绍

主要习惯使用md在线书籍工具 [mdbook](https://github.com/rust-lang/mdBook) 做项目文档管理，形式可供参考

```
# 安装 mdbook 在项目 docs/ 中
cargo install mdbook
cd docs
mdbook init

# 项目根目录启用在线预览
mdbook serve docs
```

## 文档工作流

示例：（这些 skills 都是以 md 开头的）

| 命令                     | 场景                               | 输出位置            |
| ------------------------ | ---------------------------------- | ------------------- |
| `/mdinit`   | 项目首次初始化 mdBook 文档结构，在手动执行 `mdbook init` 之后调用 | 要求在 `docs/` 中先初始化 `mdbook init`  |
| `/mdplan <功能描述>`     | 写代码前，先出方案                 | `docs/src/plan/`    |
| `/mdreview <文件或模块>` | 审查代码质量，无参数则审查最近变更 | `docs/src/review/`  |
| `/mdexplain`             | 记录刚实施完的改动                 | `docs/src/explain/` |
| `/mdlearn <文件或概念>`  | 理解某段代码或架构怎么工作         | `docs/src/learn/`   |
| `/mdadr <决策描述>`      | 记录技术选型和方案取舍             | `docs/src/adr/`     |

**所有文档 skill 执行完后都会停止，等待你确认，不会自动改代码。**

## 典型工作流

示例

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

# 新项目接入
# 先在 docs/ 目录执行 mdbook init，然后：
/mdinit
```

## 文件命名规范

所有 skill 生成的文档统一使用 `YYYY-MM-<主题>-<类型>.md`，例如：
`2026-04-user-auth-plan.md`、`2026-04-001-use-dora-rs-adr.md`
