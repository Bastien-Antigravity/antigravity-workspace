#!/usr/bin/env python3
"""ensure_frontmatter.py – Add minimal YAML front‑matter to any markdown file lacking it.

Usage: python3 scripts/ensure_frontmatter.py
"""
import pathlib, yaml, sys

ROOT = pathlib.Path("/Users/imac/Desktop/Bastien-Antigravity/obsidian-brain")
TAGFILE = ROOT / "00-AI-Orchestration/tags.yaml"

def load_tags():
    with open(TAGFILE, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)["tags"]

# Default front‑matter – can be extended later.
DEFAULT_FRONT = {
    "microservice": "obsidian-brain",
    "type": "note",
    "status": "draft",
    "tags": ["#service/obsidian-brain", "#type/note"]
}

def ensure_frontmatter(md_path: pathlib.Path):
    txt = md_path.read_text(encoding="utf-8")
    if txt.lstrip().startswith("---"):
        return False  # already has front‑matter
    front = yaml.safe_dump(DEFAULT_FRONT, sort_keys=False)
    new_txt = f"---\n{front}---\n\n{txt}"
    md_path.write_text(new_txt, encoding="utf-8")
    return True

if __name__ == "__main__":
    _ = load_tags()  # currently unused – keeps script extensible
    changed = []
    for md in ROOT.rglob("*.md"):
        if ensure_frontmatter(md):
            changed.append(md.relative_to(ROOT))
    for p in changed:
        print(f"✔ Added front‑matter to {p}")
    if not changed:
        print("All markdown files already have front‑matter.")
