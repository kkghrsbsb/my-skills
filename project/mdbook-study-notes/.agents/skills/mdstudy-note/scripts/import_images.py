#!/usr/bin/env python3
"""Copy note images beside a chapter and append links in input order."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from datetime import date
from pathlib import Path


SUPPORTED_EXTENSIONS = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".webp"}
IMAGE_LINK = re.compile(r"!\[[^]]*]\(([^)]+)\)")


def fail(message: str) -> "NoReturn":
    print(f"错误：{message}", file=sys.stderr)
    raise SystemExit(2)


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            value.update(chunk)
    return value.hexdigest()


def contained_path(base: Path, relative: str) -> Path:
    candidate = (base / relative).resolve()
    if candidate != base and base not in candidate.parents:
        fail(f"路径超出 src 目录：{relative}")
    return candidate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("images", nargs="+", help="images in display order")
    parser.add_argument("--root", default=".", help="mdBook root")
    parser.add_argument("--chapter", required=True, help="chapter path relative to src/")
    parser.add_argument("--title", help="required when creating a chapter")
    parser.add_argument("--date", default=date.today().isoformat().replace("-", ""))
    args = parser.parse_args()

    root = Path(args.root).resolve()
    src = (root / "src").resolve()
    if not (root / "book.toml").is_file() or not src.is_dir():
        fail(f"{root} 不是 mdBook 根目录")

    chapter = contained_path(src, args.chapter)
    if chapter.suffix.lower() != ".md":
        fail("章节文件必须使用 .md 扩展名")
    if not chapter.exists() and not args.title:
        fail("创建章节时必须传入 --title")

    sources = [Path(item).resolve() for item in args.images]
    for source in sources:
        if not source.is_file():
            fail(f"图片不存在：{source}")
        if source.suffix.lower() not in SUPPORTED_EXTENSIONS:
            fail(f"不支持的图片格式：{source.suffix}")

    chapter.parent.mkdir(parents=True, exist_ok=True)
    images_dir = chapter.parent / "images"
    images_dir.mkdir(exist_ok=True)

    existing_hashes = {
        digest(path): path
        for path in images_dir.iterdir()
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS
    }
    existing_names = {path.name for path in images_dir.iterdir() if path.is_file()}
    chapter_text = chapter.read_text(encoding="utf-8") if chapter.exists() else f"# {args.title}\n"
    display_index = len(IMAGE_LINK.findall(chapter_text)) + 1
    next_file_index = 1
    additions: list[str] = []

    for source in sources:
        source_hash = digest(source)
        if source_hash in existing_hashes:
            print(f"跳过重复图片：{source} -> {existing_hashes[source_hash].name}")
            continue
        while True:
            name = f"{args.date}-{next_file_index:02d}{source.suffix.lower()}"
            next_file_index += 1
            if name not in existing_names:
                break
        target = images_dir / name
        shutil.copy2(source, target)
        existing_names.add(name)
        existing_hashes[source_hash] = target
        additions.append(f"![手写笔记 {display_index}](./images/{name})")
        display_index += 1
        print(f"导入：{source} -> {target}")

    if additions:
        chapter.write_text(
            chapter_text.rstrip() + "\n\n" + "\n\n".join(additions) + "\n",
            encoding="utf-8",
        )
        print(f"更新章节：{chapter}")
    else:
        print("没有需要导入的新图片")


if __name__ == "__main__":
    main()
