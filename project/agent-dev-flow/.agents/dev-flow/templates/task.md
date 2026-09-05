# Branch Task Packet

这是分支会话任务包模板。小任务可以直接在聊天里交接；使用文件时，删除无关字段即可。

## 身份

- task id：
- activity：`explore` / `plan` / `diagnose` / `implement` / `review` / `gate`
- type：`feature` / `fix` / `docs` / `refactor` / `test` / `chore`
- workspace mode：`read-only explore` / `small implement` / `pr implement`
- session strategy：`direct` / `fork` / `create`

## 目标

待填：这次任务完成后应得到什么可观察的结果。
## 范围

- 文件或模块归属：
- 推荐起点：
- 不做的事：

## 验收标准

- 待填

## 上下文

- 主协调会话：
- 回报接收方：
- 工作目录：
- Git branch：
- base branch：
- base revision：`not checked`
- dirty-worktree baseline：`not checked`
- 依赖或阻塞：
- 能力 fallback：如果没有用户可见 task/fork API，提供 `manual handoff` 任务包，并标明尚未实际创建会话。

## 已记录的用户授权

- 待填

## 禁止动作

- 不要把这个任务包当作新的授权。它只记录用户已经给出的当前任务授权。
- 除非用户实际授权，不要 commit、push、创建 PR、安装依赖、删除文件，或执行其他外部/破坏性动作。
- 分支会话只向主协调会话回报；不更新共享 `.agents/dev-flow/state.md`。

## 回报要求

回报发现或改动、实际验证证据、未验证区域、风险和建议下一步。小任务可以直接用聊天回报，不必写报告文件。
