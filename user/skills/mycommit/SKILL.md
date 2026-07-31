---
name: mycommit
description: Generate a Chinese Conventional Commits message from the current diff and commit the changes, unless the user explicitly asks not to execute git commit.
---

默认生成 commit message 并执行 `git commit`。只有用户明确要求“不提交”“只生成 commit message”或表达同等含义时，才不得执行 `git commit`。

执行步骤：
1. 运行 `git diff --cached`，若无内容则运行 `git diff HEAD`，获取当前变更。
2. 若 diff 中出现 `Subproject commit` 行，说明涉及子模块变更，在 body 中单独列出，不要混入主要改动描述。
3. 分析变更内容，判断改动类型和影响范围。
4. 按以下规范生成 commit message：

**格式：**
`<type>(<scope>): <summary>`

**type 可选值：**
`feat` `fix` `refactor` `docs` `chore` `test`

**要求：**
- subject 必须用中文，简洁、具体
- 禁止使用模糊描述，如"更新"、"修复问题"、"杂项改动"
- 非 trivial 改动需附 body，用中文简短说明：改了什么、为什么改、重要注意事项或风险
- body 使用短 bullet，不写长段落；每行以 ` - ` 开头，每条只写一个要点
- body 每条尽量控制在一行内，避免展开实现细节，除非该细节影响使用或风险判断
- trivial 改动可省略 body
- 不要编造测试结果

5. 除非用户明确要求不提交，否则执行提交：
   - 若已有 staged 变更，仅提交 staged 变更，不擅自加入未暂存文件
   - 若没有 staged 变更，将本次分析范围内的变更加入暂存区，再执行 `git commit`
   - 使用生成的 subject 和 body 作为完整提交信息，不打开交互式编辑器
6. 输出最终 commit message；若已提交，同时报告提交哈希。若提交失败，报告原因，不声称提交成功。

$ARGUMENTS
