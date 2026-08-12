---
name: codex-handoff
description: Migrate exactly one Codex rollout session between two Linux development machines over SSH with path preservation, conflict backup, and SHA256 verification. Use when the user invokes `$codex-handoff`, asks to hand off or copy one Codex session to another machine, or provides a Codex Session ID or rollout JSONL path plus an SSH target. Do not use for bidirectional, bulk, or whole-`~/.codex` synchronization.
---

# 精确迁移单个 Codex 会话

将当前机器始终视为源机器。只迁移用户指定的一个 rollout JSONL 文件。

## 执行

1. 接收两个必需参数：
   - Session UUID，或 `~/.codex/sessions/` 下的完整或相对 JSONL 路径；
   - 目标 SSH 地址，例如 `user@host` 或 SSH config 别名。
2. 参数齐全时直接运行脚本，不重复询问确认：

   ```bash
   bash <skill-root>/scripts/handoff.sh '<SESSION_ID_OR_JSONL_PATH>' '<SSH_TARGET>'
   ```

3. 用户明确要求预演时加入 `--dry-run`：

   ```bash
   bash <skill-root>/scripts/handoff.sh --dry-run '<SESSION_ID_OR_JSONL_PATH>' '<SSH_TARGET>'
   ```

4. 将脚本结果用用户当前使用的语言简洁转述。成功时保留 Session ID、目标路径、SHA256 验证状态和恢复命令。

## 边界

- 允许在复制前执行本地查找、哈希计算、SSH 连通性和目标状态检查。
- 遇到零匹配、多匹配、非法路径、目标非普通文件、SSH 失败或无法验证的冲突时立即停止，并说明具体原因。
- 使用脚本完成迁移和冲突备份；不要临时改写为目录同步命令。
- 不迁移其他 session，不同步 `auth.json`、配置、skills 或整个 `~/.codex`。
- 不修改源 session、SSH 配置、known_hosts、项目 Git 仓库或远端认证信息。
- 不要求 sudo，不扩展为双向同步或批量同步。

$ARGUMENTS
