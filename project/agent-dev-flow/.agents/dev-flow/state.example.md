# Agent Dev Flow State

这是目标项目里的运行时驾驶舱示例。真实项目中可参考它生成 `.agents/dev-flow/state.md`。下面内容是虚构示例，不代表当前仓库状态。

## 协调信息

- bootstrap mode：`reconstructed`
- 主协调会话：`main conversation / unknown link`
- 共享状态文件：`.agents/dev-flow/state.md`
- 仓库路径：`/path/to/ExampleApp`
- 当前工作区：`/path/to/ExampleApp`
- 当前 Git branch：`main`
- base branch：`main`
- base revision：`not checked`
- dirty-worktree baseline：`not checked`
- delivery：`local only`

## 上下文来源

本示例假设主会话从已有仓库事实重建状态。旧开发会话不可用，不作为当前事实来源。历史意图只有被代码、Git 记录、任务系统或用户确认时才写入。

## 当前目标

为 `ExampleApp` 增加轻量导出能力，同时不影响现有导入流程。

## 仓库认知

- `src/export/`：可能是导出流程入口。
- `src/import/`：相关行为；改共享模型前需要阅读。
- `tests/export/`：现有 CSV 导出测试。
- evidence last checked：示例未检查。

## 约束

- 除非用户在当前对话中要求，否则不 push、不创建 PR。
- 保持现有导入行为。
- 较大实现前优先 `read-only explore`。

## 任务队列

| id | status | activity | type | mode | session | summary |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | done | explore | feature | read-only explore | fork | 主会话已接受探索结论：导出流程清楚，缺少 JSON formatter。 |
| T2 | active | implement | feature | small implement | direct | 添加 JSON formatter 和聚焦测试。 |
| T3 | queued | gate | feature | read-only explore | direct | 主会话审查 T2 diff，并决定后续交付方式。 |

状态可用：`queued`、`active`、`blocked`、`ready`、`done`、`dropped`。`ready` 表示等待主会话 gate，不等于已经合并。

## 分支会话

| session | task | mode | owner | report |
| --- | --- | --- | --- | --- |
| session/export-explore | T1 | read-only explore | branch | 探索报告已回收并被主会话接受。 |

## 决策

- 2026-01-15：T2 使用 `small implement`，因为预期改动限制在导出 formatter 和测试。

## 验证

- 上次实际命令：示例未运行。
- gate 前需要：运行导出测试，并检查 diff 是否符合 T2 范围。
- 未知项：导入快照是否共享 formatter 假设。

## 下一步

完成 T2，然后由主会话运行 `agent-gate`。
