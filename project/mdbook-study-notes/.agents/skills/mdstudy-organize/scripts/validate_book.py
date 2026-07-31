#!/usr/bin/env python3
"""Validate SUMMARY chapter references and local image links."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote


SUMMARY_LINK = re.compile(r"\[[^]]+]\(([^)]+\.md(?:#[^)]+)?)\)")
IMAGE_LINK = re.compile(r"!\[[^]]*]\(([^)]+)\)")


def local_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().split("#", 1)[0]
    if not target or "://" in target or target.startswith("data:"):
        return None
    return (source.parent / unquote(target)).resolve()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="mdBook root")
    parser.add_argument("--build", action="store_true", help="also run mdbook build")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    src = (root / "src").resolve()
    summary = src / "SUMMARY.md"
    if not (root / "book.toml").is_file() or not summary.is_file():
        print(f"错误：{root} 不是完整的 mdBook 根目录", file=sys.stderr)
        raise SystemExit(2)

    errors: list[str] = []
    summary_text = summary.read_text(encoding="utf-8")
    chapter_targets: set[Path] = set()
    for raw_target in SUMMARY_LINK.findall(summary_text):
        target = local_target(summary, raw_target)
        if target is None:
            continue
        if target != src and src not in target.parents:
            errors.append(f"SUMMARY 章节路径超出 src：{raw_target}")
            continue
        if target in chapter_targets:
            errors.append(f"SUMMARY 重复引用章节：{target.relative_to(src)}")
        chapter_targets.add(target)
        if not target.is_file():
            errors.append(f"SUMMARY 引用的章节不存在：{target.relative_to(root)}")

    all_chapters = {
        path.resolve()
        for path in src.rglob("*.md")
        if path.name != "SUMMARY.md"
    }
    for chapter in sorted(all_chapters - chapter_targets):
        errors.append(f"章节未加入 SUMMARY：{chapter.relative_to(root)}")

    referenced_images: set[Path] = set()
    for chapter in sorted(all_chapters):
        text = chapter.read_text(encoding="utf-8")
        for raw_target in IMAGE_LINK.findall(text):
            target = local_target(chapter, raw_target)
            if target is None:
                continue
            if target != src and src not in target.parents:
                errors.append(
                    f"图片路径超出 src：{chapter.relative_to(root)} -> {raw_target}"
                )
                continue
            referenced_images.add(target)
            if not target.is_file():
                errors.append(
                    f"图片链接失效：{chapter.relative_to(root)} -> {raw_target}"
                )

    all_images = {
        path.resolve()
        for path in src.rglob("*")
        if path.is_file()
        and path.suffix.lower() in {".avif", ".gif", ".jpeg", ".jpg", ".png", ".webp"}
    }
    for image in sorted(all_images - referenced_images):
        errors.append(f"图片未被任何章节引用：{image.relative_to(root)}")

    if args.build:
        result = subprocess.run(["mdbook", "build", str(root)], check=False)
        if result.returncode:
            errors.append("mdbook build 失败")

    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)
    print("mdBook 结构、SUMMARY 和图片链接检查通过")


if __name__ == "__main__":
    main()
