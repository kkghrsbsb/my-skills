#!/usr/bin/env bash

set -euo pipefail

readonly SESSION_ID_PATTERN='^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
readonly ROLLOUT_FILE_PATTERN='^rollout-[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}-[0-9]{2}-[0-9]{2}-([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})\.jsonl$'
readonly HASH_PATTERN='^[0-9a-fA-F]{64}$'

usage() {
  cat >&2 <<'USAGE'
用法：
  handoff.sh SESSION_ID TARGET
  handoff.sh JSONL_PATH TARGET
  handoff.sh --dry-run SESSION_ID_OR_JSONL_PATH TARGET
USAGE
}

die() {
  printf '错误：%s\n' "$*" >&2
  exit 1
}

require_command() {
  command -v "$1" >/dev/null 2>&1 || die "缺少必需命令：$1"
}

sha256_file() {
  local checksum_output checksum
  checksum_output=$(sha256sum -- "$1") || die "无法计算 SHA256：$1"
  checksum=${checksum_output%% *}
  checksum=${checksum#\\}
  [[ "$checksum" =~ $HASH_PATTERN ]] || die "无法解析 SHA256：$1"
  printf '%s\n' "${checksum,,}"
}

shell_quote() {
  local escaped
  escaped=${1//\'/\'\\\'\'}
  printf "'%s'" "$escaped"
}

dry_run=false
if [[ ${1:-} == "--dry-run" ]]; then
  dry_run=true
  shift
elif [[ ${1:-} == "--help" || ${1:-} == "-h" ]]; then
  usage
  exit 0
fi

if (( $# != 2 )); then
  usage
  exit 2
fi

source_spec=$1
target_host=$2

[[ -n "${HOME:-}" && "$HOME" == /* ]] || die "本地 HOME 不可用"
[[ "$target_host" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*(@[A-Za-z0-9][A-Za-z0-9._-]*)?$ ]] \
  || die "目标 SSH 地址格式不安全或不受支持：$target_host"

for required in find realpath rsync sha256sum ssh; do
  require_command "$required"
done

sessions_root_input="$HOME/.codex/sessions"
[[ -d "$sessions_root_input" ]] || die "Codex sessions 目录不存在：$sessions_root_input"
sessions_root=$(realpath -e -- "$sessions_root_input") \
  || die "无法解析 Codex sessions 目录：$sessions_root_input"

source_file=''
requested_session_id=''

if [[ "$source_spec" =~ $SESSION_ID_PATTERN ]]; then
  requested_session_id=${source_spec,,}
  matches=()
  shopt -s lastpipe
  if ! find "$sessions_root" -type f -iname "*${requested_session_id}.jsonl" -print0 \
    | while IFS= read -r -d '' candidate; do
        matches+=("$candidate")
      done; then
    die "递归查找 session 文件失败：$sessions_root_input"
  fi

  case ${#matches[@]} in
    0)
      die "未找到 Session ID 对应的文件：$source_spec"
      ;;
    1)
      source_file=$(realpath -e -- "${matches[0]}") \
        || die "无法解析匹配的 session 文件：${matches[0]}"
      ;;
    *)
      printf '错误：Session ID 匹配到多个文件，已停止：%s\n' "$source_spec" >&2
      printf '  %s\n' "${matches[@]}" >&2
      exit 1
      ;;
  esac
else
  case "$source_spec" in
    '~')
      expanded_source=$HOME
      ;;
    '~/'*)
      expanded_source="$HOME/${source_spec#\~/}"
      ;;
    *)
      expanded_source=$source_spec
      ;;
  esac

  [[ -f "$expanded_source" ]] || die "JSONL 文件不存在或不是普通文件：$expanded_source"
  source_file=$(realpath -e -- "$expanded_source") \
    || die "无法将 JSONL 路径转换为绝对路径：$expanded_source"
fi

case "$source_file" in
  "$sessions_root"/*)
    relative_path=${source_file#"$sessions_root"/}
    ;;
  *)
    die "session 文件不在 $sessions_root_input 下：$source_file"
    ;;
esac

source_name=${source_file##*/}
if [[ "$source_name" =~ $ROLLOUT_FILE_PATTERN ]]; then
  session_id=${BASH_REMATCH[1],,}
else
  die "文件名不符合 Codex rollout session 基本格式：$source_name"
fi

if [[ -n "$requested_session_id" && "$session_id" != "$requested_session_id" ]]; then
  die "文件名中的 Session ID 与请求不一致：$session_id != $requested_session_id"
fi

source_checksum=$(sha256_file "$source_file")

readonly -a ssh_options=(
  -T
  -o BatchMode=yes
  -o ConnectTimeout=5
  -o StrictHostKeyChecking=yes
  -o UpdateHostKeys=no
)

if ! ssh "${ssh_options[@]}" -- "$target_host" true; then
  die "无法通过无交互 SSH 连接目标：$target_host"
fi

remote_run() {
  local remote_script=$1 remote_command remote_arg
  shift
  remote_command="sh -c $(shell_quote "$remote_script") sh"
  for remote_arg in "$@"; do
    remote_command+=" $(shell_quote "$remote_arg")"
  done
  ssh "${ssh_options[@]}" -- "$target_host" "$remote_command"
}

if ! remote_home=$(remote_run \
  'if [ -z "${HOME:-}" ] || [ "${HOME#/}" = "$HOME" ] || [ ! -d "$HOME" ]; then exit 1; fi; printf "%s" "$HOME"'); then
  die "目标用户 HOME 不可用：$target_host"
fi
[[ -n "$remote_home" && "$remote_home" == /* && "$remote_home" != *$'\n'* && "$remote_home" != *$'\r'* ]] \
  || die "目标用户 HOME 返回了无效路径"

if ! remote_run \
  'for tool in cp date mkdir rsync sha256sum; do command -v "$tool" >/dev/null 2>&1 || { printf "缺少目标命令：%s\n" "$tool" >&2; exit 1; }; done'; then
  die "目标环境缺少迁移所需命令"
fi

remote_target="$remote_home/.codex/sessions/$relative_path"
target_display="$target_host:~/.codex/sessions/$relative_path"

if ! target_info=$(remote_run \
  'target=$1; if [ -L "$target" ]; then printf "SYMLINK\n"; elif [ ! -e "$target" ]; then printf "MISSING\n"; elif [ ! -f "$target" ]; then printf "OTHER\n"; else output=$(sha256sum -- "$target") || exit 1; digest=${output%% *}; digest=${digest#\\}; printf "FILE %s\n" "$digest"; fi' \
  "$remote_target"); then
  die "无法检查目标 session 状态"
fi

target_state=${target_info%% *}
target_checksum=''
case "$target_state" in
  MISSING)
    ;;
  FILE)
    target_checksum=${target_info#FILE }
    target_checksum=${target_checksum,,}
    [[ "$target_checksum" =~ $HASH_PATTERN ]] || die "无法解析目标 SHA256"
    ;;
  SYMLINK)
    die "目标路径是符号链接，无法安全覆盖：$target_display"
    ;;
  OTHER)
    die "目标路径存在但不是普通文件：$target_display"
    ;;
  *)
    die "无法识别目标 session 状态：$target_info"
    ;;
esac

if [[ "$dry_run" == true ]]; then
  if [[ "$target_state" == MISSING ]]; then
    target_status='不存在'
    backup_expected='否'
  elif [[ "$target_checksum" == "$source_checksum" ]]; then
    target_status='已存在，SHA256 与源文件一致'
    backup_expected='否'
  else
    target_status='已存在，SHA256 与源文件不同'
    backup_expected='是'
  fi

  printf '%s\n\n' 'Codex session handoff dry run'
  printf '源文件：\n  %s\n\n' "$source_file"
  printf 'Session ID：\n  %s\n\n' "$session_id"
  printf '目标 SSH：\n  %s\n\n' "$target_host"
  printf '最终目标：\n  %s\n\n' "$target_display"
  printf '目标状态：\n  %s\n\n' "$target_status"
  printf '预计需要备份：\n  %s\n' "$backup_expected"
  exit 0
fi

pre_copy_checksum=$(sha256_file "$source_file")
[[ "$pre_copy_checksum" == "$source_checksum" ]] \
  || die "源 session 在检查期间发生变化，未执行迁移"

backup_path=''
already_current=false

if [[ "$target_state" == FILE && "$target_checksum" == "$source_checksum" ]]; then
  already_current=true
else
  if [[ "$target_state" == FILE ]]; then
    if ! backup_path=$(remote_run \
      'set -eu; umask 077; target=$1; relative=$2; expected=$3; [ -f "$target" ] && [ ! -L "$target" ] || { printf "目标类型已变化\n" >&2; exit 1; }; output=$(sha256sum -- "$target"); current=${output%% *}; current=${current#\\}; [ "$current" = "$expected" ] || { printf "目标内容已变化\n" >&2; exit 1; }; timestamp=$(date +%Y%m%d-%H%M%S); base="$HOME/.codex/handoff-backups/$timestamp"; backup="$base/$relative"; counter=1; while [ -e "$backup" ]; do suffix=$(printf "%02d" "$counter"); base="$HOME/.codex/handoff-backups/${timestamp}-$suffix"; backup="$base/$relative"; counter=$((counter + 1)); done; parent=${backup%/*}; mkdir -p -- "$parent"; cp -p -- "$target" "$backup"; output=$(sha256sum -- "$backup"); copied=${output%% *}; copied=${copied#\\}; [ "$copied" = "$expected" ] || { printf "备份 SHA256 验证失败\n" >&2; exit 1; }; printf "%s\n" "$backup"' \
      "$remote_target" "$relative_path" "$target_checksum"); then
      die "目标旧 session 备份失败，已禁止覆盖"
    fi
    [[ "$backup_path" == "$remote_home/.codex/handoff-backups/"* ]] \
      || die "目标返回了无效的备份路径，已禁止覆盖"
  else
    if ! remote_run \
      'umask 077; target=$1; if [ -e "$target" ] || [ -L "$target" ]; then printf "目标在检查后出现\n" >&2; exit 1; fi; parent=${target%/*}; mkdir -p -- "$parent"' \
      "$remote_target"; then
      die "无法安全创建目标 session 目录"
    fi
  fi

  rsync_ssh='ssh -T -o BatchMode=yes -o ConnectTimeout=5 -o StrictHostKeyChecking=yes -o UpdateHostKeys=no'
  if ! rsync --archive --protect-args --rsh="$rsync_ssh" -- \
    "$source_file" "$target_host:$remote_target"; then
    die "rsync 迁移失败"
  fi
fi

final_source_checksum=$(sha256_file "$source_file")
[[ "$final_source_checksum" == "$source_checksum" ]] \
  || die "源 session 在迁移期间发生变化，无法确认结果"

if ! final_target_info=$(remote_run \
  'target=$1; [ -f "$target" ] && [ ! -L "$target" ] || exit 1; output=$(sha256sum -- "$target"); digest=${output%% *}; digest=${digest#\\}; printf "%s\n" "$digest"' \
  "$remote_target"); then
  die "无法计算迁移后的目标 SHA256"
fi
final_target_checksum=${final_target_info,,}
[[ "$final_target_checksum" =~ $HASH_PATTERN ]] || die "无法解析迁移后的目标 SHA256"
[[ "$final_source_checksum" == "$final_target_checksum" ]] \
  || die "迁移后 SHA256 不一致：源=$final_source_checksum，目标=$final_target_checksum"

if [[ "$already_current" == true ]]; then
  printf '%s\n\n' 'session already up to date'
fi

printf '%s\n\n' 'Codex 会话迁移完成'
printf '源文件：\n  %s\n\n' "$source_file"
printf '目标：\n  %s\n\n' "$target_display"
printf 'Session ID：\n  %s\n\n' "$session_id"
printf 'SHA256：\n  verified\n\n'

if [[ -n "$backup_path" ]]; then
  backup_display="~${backup_path#"$remote_home"}"
  printf '目标旧 session 已备份到：\n  %s\n\n' "$backup_display"
fi

printf '在目标机恢复：\n  codex resume %s\n\n' "$session_id"
printf '或浏览全部会话：\n  codex resume --all\n'
