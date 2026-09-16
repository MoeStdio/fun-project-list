# Project Ideas Playground

My personal run through [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) and other project-idea
lists — one folder per project, each self-contained with its own README, stack, and notes on what I learned.

Live versions (when they exist) are linked from each project's README. This repo doubles as a build log for
[my LinkedIn posts](#) and [moestdio.com](https://moestdio.com).

## How this is organized

- `projects/<slug>/` — one folder per project. Copy `projects/_template/` to start a new one.
- Each project README has YAML frontmatter (`difficulty`, `category`, `status`, `stack`, ...) that feeds the table below.
- Run `python scripts/build_index.py` after adding/finishing a project to regenerate the table.

## Projects

<!-- PROJECT_TABLE_START -->
| Project | Difficulty | Category | Status |
|---|---|---|---|
| [Tic-Tac-Toe](projects/tic-tac-toe) | beginner | game | ⏳ planned |
<!-- PROJECT_TABLE_END -->

## Adding a new project

```bash
cp -r projects/_template projects/my-new-project
# edit projects/my-new-project/README.md frontmatter + content
python scripts/build_index.py
git add .
git commit -m "start: my-new-project"
```
