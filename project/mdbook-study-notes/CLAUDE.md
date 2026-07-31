# CLAUDE.md

## Notebook Rules

- Treat this repository as an image-first personal study notebook built with mdBook.
- Use `src/SUMMARY.md` as the authoritative reading order and navigation hierarchy.
- Store each note as `<domain>/<topic>/README.md` with its images in the sibling `<domain>/<topic>/images/` directory.
- Preserve the user's attachment order when placing images in a note.
- Do not transcribe, summarize, explain, or expand handwritten notes unless the user explicitly asks for text.
- Image analysis may determine the destination, title, or answer a question, but inferred content must not be written into the notebook without permission.
- Use neutral image alt text such as `手写笔记 1`; do not put inferred note content in alt text.
- Do not crop, recompress, rotate, enhance, or otherwise alter imported images. Import the user-provided processed files unchanged.
- Do not rename existing images merely to change display order. Reorder their Markdown references instead.
- Update `src/SUMMARY.md` whenever a chapter is created, moved, renamed, or deleted. Choose a concise hierarchy based on the actual subjects; no fixed category structure is required.
- Before deleting, replacing, overwriting, or moving material, list the exact target chapters and images and obtain confirmation.
- After notebook writes, check local links and run `mdbook build`.
- Keep build output under `book/` out of version control.

## GitHub Rules

- Treat commit, push, remote repository creation, visibility changes, and GitHub Pages enablement as separate actions.
- Never create a remote repository, push, or enable Pages unless the user has requested that external action.
- Recommend private visibility by default, but show the repository name, owner, and visibility before creation.
- Never change a private repository to public, force-push, or rewrite remote history without explicit permission.
