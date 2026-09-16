#!/usr/bin/env python3
"""
Regenerates the project table in the root README.md by reading the YAML
frontmatter of every projects/*/README.md file.

Usage:
    python scripts/build_index.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECTS_DIR = ROOT / "projects"
README = ROOT / "README.md"

START_MARK = "<!-- PROJECT_TABLE_START -->"
END_MARK = "<!-- PROJECT_TABLE_END -->"

STATUS_EMOJI = {"planned": "⏳", "in-progress": "🚧", "done": "✅"}


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        # strip inline comments like `status: "planned"      # ...`
        value = value.split("#")[0].strip().strip('"').strip("'")
        fm[key] = value
    return fm


def main():
    rows = []
    for project_dir in sorted(PROJECTS_DIR.iterdir()):
        if not project_dir.is_dir() or project_dir.name.startswith("_"):
            continue
        readme = project_dir / "README.md"
        if not readme.exists():
            continue
        fm = parse_frontmatter(readme.read_text(encoding="utf-8"))
        title = fm.get("title", project_dir.name)
        difficulty = fm.get("difficulty", "-")
        category = fm.get("category", "-")
        status = fm.get("status", "planned")
        emoji = STATUS_EMOJI.get(status, "⏳")
        link = f"projects/{project_dir.name}"
        rows.append((title, difficulty, category, f"{emoji} {status}", link))

    table_lines = [
        "| Project | Difficulty | Category | Status |",
        "|---|---|---|---|",
    ]
    for title, difficulty, category, status, link in rows:
        table_lines.append(f"| [{title}]({link}) | {difficulty} | {category} | {status} |")
    table = "\n".join(table_lines)

    content = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START_MARK) + r".*?" + re.escape(END_MARK), re.DOTALL)
    new_block = f"{START_MARK}\n{table}\n{END_MARK}"
    if pattern.search(content):
        content = pattern.sub(new_block, content)
    else:
        content += f"\n\n{new_block}\n"

    README.write_text(content, encoding="utf-8")
    print(f"Indexed {len(rows)} project(s).")


if __name__ == "__main__":
    main()
