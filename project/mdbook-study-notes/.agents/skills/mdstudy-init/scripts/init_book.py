#!/usr/bin/env python3
"""Initialize an image-first mdBook study notebook."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REQUIRED_COMMANDS = ("cargo", "mdbook", "mdbook-katex", "mdbook-mermaid")


def fail(message: str) -> "NoReturn":
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(2)


def command_version(command: str) -> str:
    result = subprocess.run(
        [command, "--version"], check=False, capture_output=True, text=True
    )
    output = (result.stdout or result.stderr).strip()
    return output.splitlines()[0] if output else "未知版本"


def append_katex_config(book_toml: Path) -> None:
    text = book_toml.read_text(encoding="utf-8")
    if "[preprocessor.katex]" not in text:
        text = text.rstrip() + '\n\n[preprocessor.katex]\nafter = ["links"]\n'
        book_toml.write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True, help="book title")
    parser.add_argument("--root", default=".", help="book root (default: current directory)")
    parser.add_argument(
        "--with-pages-workflow",
        action="store_true",
        help="copy the bundled GitHub Pages workflow",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if (root / "book.toml").exists():
        fail(f"{root} 已经包含 book.toml，为避免覆盖已停止")

    missing = [command for command in REQUIRED_COMMANDS if not shutil.which(command)]
    if missing:
        fail("缺少必需命令：" + ", ".join(missing))

    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["mdbook", "init", str(root), f"--title={args.title}", "--ignore=git"],
        check=True,
    )
    subprocess.run(["mdbook-mermaid", "install", str(root)], check=True)
    append_katex_config(root / "book.toml")

    src = root / "src"
    readme = src / "README.md"
    readme.write_text(f"# {args.title}\n", encoding="utf-8")
    (src / "SUMMARY.md").write_text(
        "# Summary\n\n[README](./README.md)\n", encoding="utf-8"
    )
    chapter_stub = src / "chapter_1.md"
    if chapter_stub.exists():
        chapter_stub.unlink()

    if args.with_pages_workflow:
        workflow_source = Path(__file__).parent.parent / "assets" / "mdbook.yml"
        workflow_target = root / ".github" / "workflows" / "mdbook.yml"
        workflow_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(workflow_source, workflow_target)

    subprocess.run(["mdbook", "build", str(root)], check=True)

    print(f"mdBook 学习笔记已初始化：{root}")
    for command in REQUIRED_COMMANDS:
        print(f"{command}: {command_version(command)}")
    if args.with_pages_workflow:
        print("已创建：.github/workflows/mdbook.yml")


if __name__ == "__main__":
    main()
