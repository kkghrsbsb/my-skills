#!/usr/bin/env python3
"""
Install skills from this repo's skills/ folder into Codex's skills folder.
Supports Windows, macOS, and Linux.
"""

import os
import shutil
import sys
from pathlib import Path


def main():
    repo_skills = Path(__file__).parent / "skills"
    codex_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    target_skills = codex_home / "skills"

    if not repo_skills.exists():
        print(f"Error: skills/ folder not found at {repo_skills}", file=sys.stderr)
        sys.exit(1)

    target_skills.mkdir(parents=True, exist_ok=True)

    updated = []
    added = []

    for src in repo_skills.rglob("*"):
        if src.is_dir():
            continue
        rel = src.relative_to(repo_skills)
        dst = target_skills / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        existed = dst.exists()
        shutil.copy2(src, dst)
        (updated if existed else added).append(str(rel))

    for f in added:
        print(f"  added:   {f}")
    for f in updated:
        print(f"  updated: {f}")

    total = len(added) + len(updated)
    print(f"\nDone. {total} file(s) synced to {target_skills}")


if __name__ == "__main__":
    main()
