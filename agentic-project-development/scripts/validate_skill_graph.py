#!/usr/bin/env python3
"""Validate that SKILL.md references point to existing bundled files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REFERENCE_RE = re.compile(r"`(references/[^`]+?\.md)`")
SCRIPT_RE = re.compile(r"`(scripts/[^`]+?\.py)`")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", default=".")
    skill_dir = Path(parser.parse_args().skill_dir).resolve()
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        raise SystemExit(f"Missing SKILL.md at {skill_md}")

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = FRONTMATTER_RE.search(text)
    if not frontmatter:
        raise SystemExit("Missing YAML frontmatter block")
    fields = {}
    for line in frontmatter.group("body").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if fields.get("name") != "agentic-project-development":
        raise SystemExit("Frontmatter name must be agentic-project-development")
    if not fields.get("description") or "TODO" in fields["description"]:
        raise SystemExit("Frontmatter description is missing or incomplete")

    missing: list[str] = []
    for pattern in (REFERENCE_RE, SCRIPT_RE):
        for rel in sorted(set(pattern.findall(text))):
            if not (skill_dir / rel).exists():
                missing.append(rel)

    if missing:
        for rel in missing:
            print(f"MISSING {rel}")
        raise SystemExit(1)

    print("OK: all referenced bundled files exist")


if __name__ == "__main__":
    main()
