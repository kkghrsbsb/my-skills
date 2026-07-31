# mdBook 学习笔记

这是一套面向个人领域钻研、课程和研究记录的 mdBook 项目模板。它以处理后的手写笔记图片为主，默认只负责归类、存储、排序和展示，不自动转写或扩写内容。

## 模板结构

```text
mdbook-study-notes/
├── .agents/
│   └── skills/
│       ├── mdstudy-init/
│       ├── mdstudy-note/
│       ├── mdstudy-ask/
│       ├── mdstudy-organize/
│       └── mdstudy-publish/
├── AGENTS.md
├── CLAUDE.md
└── README.md
```

## 复制到目标项目

在 `my-skills` 仓库根目录执行：

```bash
cp -R project/mdbook-study-notes/.agents \
  project/mdbook-study-notes/AGENTS.md \
  project/mdbook-study-notes/CLAUDE.md \
  <目标项目>/
```

复制前检查目标项目是否已有同名规则文件。本 README 只用于介绍模板，不会复制并覆盖目标项目的 README。

## Skills

| Skill | 用途 |
| --- | --- |
| `mdstudy-init` | 推测书名、检查工具、初始化 mdBook，并可选配置 Pages workflow |
| `mdstudy-note` | 分析图片主题，按附件顺序创建或修改图片笔记 |
| `mdstudy-ask` | 只读分析手写笔记并回答内容问题 |
| `mdstudy-organize` | 整理目录与 SUMMARY，检查孤立章节、图片和断链 |
| `mdstudy-publish` | 构建、提交并推送笔记，不等待异步 Pages 部署 |

## 工具环境

初始化 skill 会检查：

- `cargo`
- `mdbook`
- `mdbook-katex`
- `mdbook-mermaid`

参考版本为 `mdbook 0.5.4`、`mdbook-katex 0.10.0` 和 `mdbook-mermaid 0.17.0`。版本不同时先尝试构建，只在构建错误有明确版本证据时调整。

## 笔记布局

每篇笔记默认将 Markdown 与图片放在同一目录：

```text
src/
└── robotics/
    └── kinematics/
        ├── README.md
        └── images/
            ├── 20260731-01.webp
            └── 20260731-02.webp
```

Markdown 只在用户没有要求文字时保留标题和图片：

```markdown
# 机器人运动学

![手写笔记 1](./images/20260731-01.webp)

![手写笔记 2](./images/20260731-02.webp)
```

## GitHub Pages

`mdstudy-init` 只在用户明确要求时从 skill 资源中创建 `.github/workflows/mdbook.yml`。workflow 使用固定参考版本构建 mdBook，并通过 GitHub Actions 部署 `book/` 到 Pages。

创建远程仓库、push 和开启 Pages 是独立的外部操作，必须由用户要求或确认。默认建议 private 仓库，但 private Pages 是否可用取决于 GitHub 套餐和组织策略。`mdstudy-publish` 在 push 成功后立即返回，不调用 API 轮询 Actions 或 Pages 状态。
