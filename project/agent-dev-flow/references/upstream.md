# 上游参考与适配

这套模板根据主会话编排的需求重新编写，保留下面的来源名称和固定版本以便回看。未复制上游 skill 目录、脚本、角色文件或运行时实现，也不要求安装上游插件。

## 本次参考版本

| 仓库 | 阅读的提交 |
| --- | --- |
| [tw93/Waza](https://github.com/tw93/Waza/tree/535a3cdfa651695ecf032fe830861f8b51f29596) | `535a3cdfa651695ecf032fe830861f8b51f29596` |
| [null0xxx/kimi-atlas](https://github.com/null0xxx/kimi-atlas/tree/90406503cc7726bb670c3d4e0896209bb03d3d66) | `90406503cc7726bb670c3d4e0896209bb03d3d66` |

## 借鉴落点

| 上游原名与材料 | 借鉴机制 | 在本模板中的落点与调整 |
| --- | --- | --- |
| Waza [think](https://github.com/tw93/Waza/blob/535a3cdfa651695ecf032fe830861f8b51f29596/skills/think/SKILL.md) | 明确结果、先读项目、简化方案、交接时减少重新决策 | `agent-plan` 产出范围与验收；小改动可用几句话，不照搬全量规划步骤与固定确认点 |
| Waza [hunt](https://github.com/tw93/Waza/blob/535a3cdfa651695ecf032fe830861f8b51f29596/skills/hunt/SKILL.md) | 先定位原因、用可复现证据检验假设 | `diagnose` 活动先只读，原因未明时交付下一项探针；不要求所有 bug 进入新会话 |
| Waza [check](https://github.com/tw93/Waza/blob/535a3cdfa651695ecf032fe830861f8b51f29596/skills/check/SKILL.md) | 基于实际 diff 与工作区审查、验证有证据、区分审查和发布 | `agent-gate` 区分任务验收与交付状态；已有授权可继续，不移植完整发布矩阵 |
| Waza [durable-context](https://github.com/tw93/Waza/blob/535a3cdfa651695ecf032fe830861f8b51f29596/rules/durable-context.md) | 当前证据优先、历史记忆不能自行授权、共享规则去除私有上下文 | `state.md` 是恢复线索；共享模板使用虚构示例；会话内仍有效的授权不因切换 skill 丢失 |
| kimi-atlas [atlas](https://github.com/null0xxx/kimi-atlas/blob/90406503cc7726bb670c3d4e0896209bb03d3d66/skills/atlas/SKILL.md) | 明确任务边界、验收与基线，区分实现报告和验证结论 | 任务包与 `agent-gate` 要求可检查的证据；不声称具备上游的确定性质量门禁 |
| kimi-atlas [atlas-weave](https://github.com/null0xxx/kimi-atlas/blob/90406503cc7726bb670c3d4e0896209bb03d3d66/skills/atlas-weave/SKILL.md) | 按任务分工、检查实际文件归属、组合后再验证 | `agent-branch` 检查写入重叠和依赖，`agent-gate` 检查组合结果；不用 DAG 调度器与租约系统 |
| kimi-atlas [atlas-resume](https://github.com/null0xxx/kimi-atlas/blob/90406503cc7726bb670c3d4e0896209bb03d3d66/skills/atlas-resume/SKILL.md) | 从持久记录恢复，避免重跑已完成步骤 | `agent-resume` 先核实代码与活跃任务；保留部分工作，不移植强制移除脏 worktree 的恢复步骤 |

## 工具专属假设

kimi-atlas 在这个版本面向 Claude Code CLI，包含命名 agent、`AskUserQuestion` 等工具调用、SessionStart hooks、Python 环境设置、`.atlas` 账本和脚本质量门禁。本模板用普通文件与可选任务 API 表达同一类交接需求，没有导入这些运行时能力。因此不能把上游的验证、自动恢复或并发保证当成本模板已经实现的能力。

Waza 的 skill 文件含有自己的路由字段、输出标记、斜杠命令和部分按当前轮授权的约定。本模板只用 `name` 与 `description` 作为必需 frontmatter，技能按实际宿主加载；交互跟随用户语言，授权按当前任务范围与有效的会话上下文判断。

工具适配发生在派工时：能 fork 就按需继承上下文，能创建 task 就发送完整任务包，不能创建会话就明确交付可手动转交的任务包。工作区隔离单独决定，不假设聊天分叉自动带来 Git 隔离。

## 来源与许可

本目录的协议与模板为重新组织和撰写的内容。来源标注用于说明设计借鉴，不代表上游为本模板背书，也不替整个 `my-skills` 仓库选择发布许可证。未来直接引入上游文件时，应分别保留对应文件的许可证和来源；kimi-atlas 的打包技能存在各自的许可证，不能只依据仓库根许可证处理。

Waza 和 kimi-atlas 的根目录均提供 MIT License。以下保留两个来源的版权通知与共同的 MIT 许可正文；对应原件为 [Waza LICENSE](https://github.com/tw93/Waza/blob/535a3cdfa651695ecf032fe830861f8b51f29596/LICENSE) 与 [kimi-atlas LICENSE](https://github.com/null0xxx/kimi-atlas/blob/90406503cc7726bb670c3d4e0896209bb03d3d66/LICENSE)。

```text
MIT License

Copyright (c) 2026 Tw93
Copyright (c) 2026 kimi-atlas (null0xxx)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
