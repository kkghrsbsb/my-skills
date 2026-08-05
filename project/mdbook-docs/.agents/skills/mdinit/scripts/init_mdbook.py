#!/usr/bin/env python3
"""Initialize the repository's standard mdBook documentation structure."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


SUMMARY = """# Summary

- [README](./README.md)

- [个人笔记]()

- [方案]()

- [解释说明]()

- [审查报告]()

- [学习笔记]()

- [决策记录]()

- [归档]()
"""


def fail(message: str) -> "NoReturn":
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(2)


def command_version(command: str) -> str:
    result = subprocess.run(
        [command, "--version"], check=False, capture_output=True, text=True
    )
    output = (result.stdout or result.stderr).strip()
    return output.splitlines()[0] if output else "未知版本"


def resolve_book_root(repo_root: Path, requested: str | None) -> Path:
    if not requested or not requested.strip():
        fail(
            "未指定 mdBook 初始化位置。"
            "请用 --book-root 明确指定 docs/ 或 docs/<自定义名称>/"
        )

    docs_root = (repo_root / "docs").resolve()
    requested_path = Path(requested)
    candidate = (
        requested_path.resolve()
        if requested_path.is_absolute()
        else (repo_root / requested_path).resolve()
    )
    if candidate != docs_root and candidate.parent != docs_root:
        fail(
            f"{candidate} 不是允许的初始化位置；"
            "只能指定 docs/ 或 docs/<自定义名称>/"
        )
    return candidate


def ensure_uninitialized(book_root: Path) -> None:
    conflicts = [
        path
        for path in (book_root / "book.toml", book_root / "src")
        if path.exists()
    ]
    if conflicts:
        details = ", ".join(str(path) for path in conflicts)
        fail(f"目标位置已包含 mdBook 初始化文件：{details}")


def run_mdbook(*arguments: str) -> None:
    try:
        subprocess.run(["mdbook", *arguments], check=True)
    except subprocess.CalledProcessError as error:
        fail(f"mdbook 命令执行失败（退出码 {error.returncode}）")


def github_url(repo_root: Path) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo_root), "remote", "get-url", "origin"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        return ""
    url = result.stdout.strip()
    match = re.fullmatch(r"git@github\.com:([^/]+)/(.+?)(?:\.git)?", url)
    if match:
        return f"https://github.com/{match.group(1)}/{match.group(2)}"
    return url.removesuffix(".git")


def update_book_toml(path: Path, repository_url: str) -> None:
    text = path.read_text(encoding="utf-8")
    setting = f'git-repository-url = "{repository_url}"'
    section = re.search(r"(?m)^\[output\.html\]\s*$", text)
    if not section:
        path.write_text(text.rstrip() + f"\n\n[output.html]\n{setting}\n", encoding="utf-8")
        return

    section_end = re.search(r"(?m)^\[", text[section.end() :])
    end = section.end() + section_end.start() if section_end else len(text)
    body = text[section.end() : end]
    pattern = re.compile(r'(?m)^git-repository-url\s*=\s*.*$')
    if pattern.search(body):
        body = pattern.sub(setting, body, count=1)
    else:
        body = body.rstrip() + f"\n{setting}\n\n"
    path.write_text(text[: section.end()] + body + text[end:], encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root", default=".", help="repository root (default: current directory)"
    )
    parser.add_argument(
        "--book-root", help="required mdBook root: docs/ or docs/<custom-name>/"
    )
    parser.add_argument("--project-name", help="README title (default: repository name)")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.is_dir():
        fail(f"仓库根目录不存在：{repo_root}")
    book_root = resolve_book_root(repo_root, args.book_root)
    ensure_uninitialized(book_root)
    if not shutil.which("mdbook"):
        fail("缺少必需命令：mdbook。请先安装 mdBook 后重试")

    project_name = args.project_name or repo_root.name
    book_root.mkdir(parents=True, exist_ok=True)
    run_mdbook(
        "init",
        str(book_root),
        f"--title={project_name}",
        "--ignore=git",
    )

    readme = book_root / "src" / "README.md"
    repository_url = github_url(repo_root)
    update_book_toml(book_root / "book.toml", repository_url)
    readme.write_text(f"# {project_name}\n", encoding="utf-8")
    (book_root / "src" / "SUMMARY.md").write_text(SUMMARY, encoding="utf-8")

    changed = [
        book_root / "book.toml",
        readme,
        book_root / "src" / "SUMMARY.md",
    ]
    gitignore = book_root / ".gitignore"
    if gitignore.exists():
        changed.append(gitignore)
    deleted: list[Path] = []
    default_stub = book_root / "src" / "chapter_1.md"
    if default_stub.exists():
        default_stub.unlink()
        deleted.append(default_stub)

    run_mdbook("build", str(book_root))

    print(f"mdBook 初始化完成：{book_root}")
    print(f"mdbook: {command_version('mdbook')}")
    print("构建：成功")
    print(f"构建输出：{book_root / 'book'}")
    for path in changed:
        print(f"修改：{path}")
    for path in deleted:
        print(f"删除：{path}")
    if not repository_url:
        print("提示：未找到 origin，git-repository-url 已留空")


if __name__ == "__main__":
    main()
