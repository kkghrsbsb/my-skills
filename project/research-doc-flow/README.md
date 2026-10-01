# research-doc-flow

让主会话维护研究问题、证据边界和研究者自己的理解。适合刚进入科研、资料整理、技术调研、论文/报告准备，以及隔很久回到一个主题时恢复认识。

它不要求 mdBook、特定笔记软件、Zotero、联网检索、脚本或指定模型。普通 Markdown 是共享接口；已有的文档目录、引用管理器和写作工具可以继续作为项目自己的实现选择。可用工具的连接经验放在 `.agents/research-flow/tools/`。

## 接入项目

将 `.agents/skills/research-*` 和 `.agents/research-flow/` 一起加入目标项目，保持相对位置。共享协议和模板是技能的一部分，不能只复制一个 `SKILL.md`。已有同名 skill、`AGENTS.md` 或 `CLAUDE.md` 时，先比较并只合并适用入口；不要递归覆盖 `.agents`、项目指令或项目 README。

首次需要保存研究认识时，可参考 [understanding.example.md](.agents/research-flow/understanding.example.md) 创建 `.agents/research-flow/understanding.md`。它保存当前问题、关键证据与派生链、决策理由、你的实际复述与不理解之处。它不是事实来源或问答流水；真实来源、数据、实验产物和你的最新表述优先于旧摘要。

是否追踪 `understanding.md`、来源卡片和研究产物由目标项目决定；本模板不修改 `.gitignore`，也不把个人会话链接或本机私有路径写进共享文件。

## 五个入口

| Skill | 适合什么时候用 | 结果 |
| --- | --- | --- |
| [research-orient](.agents/skills/research-orient/SKILL.md) | 新主题、资料库不熟悉 | 当前认识摸底、研究问题与资料地图 |
| [research-capture](.agents/skills/research-capture/SKILL.md) | 阅读网页、论文、项目文档、数据说明 | 可定位的来源卡和证据摘录 |
| [research-synthesize](.agents/skills/research-synthesize/SKILL.md) | 要比较资料、形成判断、起草文档 | 证据边界清楚的提纲、结论或文稿 |
| [research-resume](.agents/skills/research-resume/SKILL.md) | 中断、换会话、接手资料整理 | 证据核对、主动复述与理解缺口 |
| [research-tool-connect](.agents/skills/research-tool-connect/SKILL.md) | 接入、重连或记录 Zotero 等研究工具 | 当前环境的验证结果与可复现连接说明 |

不必按顺序使用。一个明确的问题可以从 `research-capture` 开始；需要快速解释已有材料时可直接综合；只有在资料和问题都不清楚时才先做定向。

## 工具连接经验

[tools/](.agents/research-flow/tools/README.md) 保存每个研究工具的使用途径、最小只读验证和已知限制。模板里的 [Zotero 记录](.agents/research-flow/tools/zotero.md) 基于一次真实本机检查：API 可访问，文献条目可列出并按标题搜索。它不代表复制模板后的目标环境仍能连接，也不证明附件或全文可读。`research-tool-connect` 在目标研究仓库重新检查后，更新该仓库相应的工具记录。

日后把某个研究项目的工具经验带回 `my-skills` 时，逐个文件审阅并合并可复用方法；不要用整个文件夹覆盖已有记录，也不要带回凭证、私有路径或项目文献清单。

## 工作模型

主会话整合研究问题、证据、派生链和你的理解。新主题开始前可先问一两个开放问题，了解你已经能解释什么、哪里没把握。研究中你问「为什么」或说「看不懂这个结论」时，就在当下沿证据与数据链澄清。Agent 看过材料不代表你已理解；只有你的实际复述和自述把握能说明你的理解情况。

| 活动 | 关注点 |
| --- | --- |
| `orient` | 明确问题、读者、时限、已有材料和缺口 |
| `collect` | 发现、筛选或取得候选来源 |
| `capture` | 记录来源内容、定位、上下文与可信度限制 |
| `analyze` | 比较来源、检验冲突、形成暂定推断 |
| `synthesize` | 按受众组织答案、笔记、报告或文档 |
| `review` | 检查可追溯性、范围、引用与未证实断言 |

`source claim`、`analysis` 和 `decision` 必须分开：来源实际说了什么；我们据此怎样推断；用户最终决定采用什么。任何一层都不能替另一层背书。没有来源或定位的外部事实应标为待核实，而不是补成看似可靠的引文。

## 保存与会话

主会话在问题变化、关键证据或实验结论出现、你复述出新的认识或提出具体困惑时更新 `understanding.md`；不记录完整问答。证据是否核实和你是否能解释它要分别写清。较大的来源阅读可用[来源卡](.agents/research-flow/templates/source.md)，跨来源写作可用[综合模板](.agents/research-flow/templates/synthesis.md)。行动项及其状态由 Linear 管理，这里只保留影响研究理解的依赖，必要时附相关 issue 链接。

你手动开新空白会话或从主会话 fork，自选当前工作区或新 worktree；你或主会话再说明研究问题。方向可随证据拆分或合并，无须在认识文件中维护固定会话树。其他会话带回来源定位、冲突、推断和未验证之处，主会话核对后整合认识。聊天分支不自动等于 Git 分支或独立工作区。

联网检索、下载资料、安装工具、写入笔记库、创建引用库、发布文稿和删除素材都取决于当前请求与可用权限。本模板不会假定其中任何能力已经存在，也不会把阅读来源的许可扩展为大段复制或公开再发布。

## 一次使用示例

1. 新主题开始，你说明自己目前怎样理解研究对象、哪里没有把握。主会话据此选一个能回答的研究问题。
2. 阅读中你说「我看不懂这个结论」。Agent 当下沿原始资料或数据链解释，再请你尝试用自己的话说一遍；没有复述就记录为尚未确认。
3. 需要更多材料时，你手动开会话阅读来源；回报证据与冲突后，主会话整合研究认识。
4. 久后继续，`research-resume` 核对材料和旧认识，并用适合你当前深度的短题帮助恢复理解。

## 验证

见 [行为场景](references/scenarios.md)。它们是模板的使用验收，不是已运行的测试。第一次试用建议选一个小而真实的主题，观察「初始摸底、随时澄清、本人复述、久后恢复」是否有效。
