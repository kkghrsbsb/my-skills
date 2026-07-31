#!/usr/bin/env python3
"""Initialize the repository's standard mdBook documentation structure."""

from __future__ import annotations

import argparse
import re
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


def is_book_root(path: Path) -> bool:
    return (path / "book.toml").is_file() and (path / "src").is_dir()


def find_book_root(repo_root: Path, requested: str | None) -> Path:
    docs = repo_root / "docs"
    if requested:
        candidate = Path(requested)
        if not candidate.is_absolute():
            candidate = repo_root / candidate
            if len(Path(requested).parts) == 1:
                candidate = docs / requested
        candidate = candidate.resolve()
        if not is_book_root(candidate):
            fail(f"{candidate} 不是 mdBook 根目录（需要 book.toml 和 src/）")
        return candidate

    candidates: list[Path] = []
    if is_book_root(docs):
        candidates.append(docs)
    if docs.is_dir():
        candidates.extend(
            path.parent
            for path in sorted(docs.glob("*/book.toml"))
            if is_book_root(path.parent)
        )
    if not candidates:
        fail(
            "未找到 mdBook。请先在 docs/ 或 docs/<名称>/ 中运行 mdbook init"
        )
    if len(candidates) > 1:
        choices = "\n".join(f"  - {path}" for path in candidates)
        fail(f"找到多个 mdBook，请用 --book-root 指定：\n{choices}")
    return candidates[0].resolve()


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
        "--book-root", help="mdBook root, or a direct child name under docs/"
    )
    parser.add_argument("--project-name", help="README title (default: repository name)")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    book_root = find_book_root(repo_root, args.book_root)
    readme = book_root / "src" / "README.md"
    if readme.exists():
        fail(f"{readme} 已存在；为避免覆盖，本次未修改任何文件")

    project_name = args.project_name or repo_root.name
    repository_url = github_url(repo_root)
    update_book_toml(book_root / "book.toml", repository_url)
    readme.write_text(f"# {project_name}\n", encoding="utf-8")
    (book_root / "src" / "SUMMARY.md").write_text(SUMMARY, encoding="utf-8")

    changed = [
        book_root / "book.toml",
        readme,
        book_root / "src" / "SUMMARY.md",
    ]
    deleted: list[Path] = []
    default_stub = book_root / "src" / "chapter_1.md"
    if default_stub.exists():
        default_stub.unlink()
        deleted.append(default_stub)

    print(f"mdBook 初始化完成：{book_root}")
    for path in changed:
        print(f"修改：{path}")
    for path in deleted:
        print(f"删除：{path}")
    if not repository_url:
        print("提示：未找到 origin，git-repository-url 已留空")


if __name__ == "__main__":
    main()
