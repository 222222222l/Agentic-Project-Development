#!/usr/bin/env python3
"""Validate skill metadata, direct resources, and UI metadata without PyYAML."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


RESOURCE_RE = re.compile(r"`((?:references/[^`]+?\.md)|(?:scripts/[^`]+?\.py))`")
FRONTMATTER_RE = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
DEFAULT_PROMPT_RE = re.compile(r'default_prompt:\s*"(?P<value>[^"]+)"')
SHORT_DESCRIPTION_RE = re.compile(r'short_description:\s*"(?P<value>[^"]+)"')


def fail(messages: list[str]) -> None:
    for message in messages:
        print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", default=".")
    skill_dir = Path(parser.parse_args().skill_dir).resolve()
    skill_md = skill_dir / "SKILL.md"
    errors: list[str] = []

    if not skill_md.exists():
        fail([f"missing SKILL.md at {skill_md}"])

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = FRONTMATTER_RE.search(text)
    if not frontmatter:
        fail(["missing YAML frontmatter block"])

    fields: dict[str, str] = {}
    for line in frontmatter.group("body").splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    if set(fields) != {"name", "description"}:
        errors.append("frontmatter must contain only name and description")
    if fields.get("name") != "agentic-project-development":
        errors.append("frontmatter name must be agentic-project-development")
    if not fields.get("description") or "TODO" in fields["description"]:
        errors.append("frontmatter description is missing or incomplete")

    listed = set(RESOURCE_RE.findall(text))
    for rel in sorted(listed):
        resource = skill_dir / rel
        if not resource.exists():
            errors.append(f"referenced resource is missing: {rel}")
        elif rel.startswith("references/"):
            lines = resource.read_text(encoding="utf-8").splitlines()
            if len(lines) > 100 and "## Contents" not in lines[:25]:
                errors.append(f"reference over 100 lines needs a Contents section: {rel}")

    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must stay under 500 lines")

    bundled = {
        path.relative_to(skill_dir).as_posix()
        for folder, suffix in (("references", "*.md"), ("scripts", "*.py"))
        for path in (skill_dir / folder).glob(suffix)
    }
    for rel in sorted(bundled - listed):
        errors.append(f"bundled resource is not directly listed in SKILL.md: {rel}")

    for readme in skill_dir.rglob("README.md"):
        errors.append(f"skill folder must not contain README.md: {readme.relative_to(skill_dir)}")

    routing_file = skill_dir / "references" / "project-model-routing.md"
    if routing_file.exists():
        routing_text = routing_file.read_text(encoding="utf-8")
        for fragment in (
            "ROUTE -> EXECUTE -> REASSESS -> VERIFY",
            "total cost = execution + context loading + handoff + retry + verification",
            "Start with one agent",
            "Reuse an existing worker handle",
            "A skill cannot by itself switch the current main model",
        ):
            if fragment not in routing_text:
                errors.append(f"project routing reference is missing contract: {fragment}")

    selector = skill_dir / "scripts" / "select_workflow.py"
    if selector.exists():
        selector_text = selector.read_text(encoding="utf-8")
        for fragment in (
            "--task-role",
            "--delegation-shape",
            "--worker-reuse",
            "--verification-independence",
            '"execution_owner"',
            '"fallback_if_model_unavailable"',
        ):
            if fragment not in selector_text:
                errors.append(f"workflow selector is missing routing field: {fragment}")

    personalization = skill_dir / "references" / "personalization.md"
    if personalization.exists():
        profile_text = personalization.read_text(encoding="utf-8")
        if "## Project Model Routing" not in profile_text:
            errors.append("personalization reference lacks project model routing fields")

    minimization = skill_dir / "references" / "trajectory-guided-patch-minimization.md"
    if minimization.exists():
        minimization_text = minimization.read_text(encoding="utf-8")
        for fragment in (
            "Correctness precedes minimization",
            "task-owned changes",
            "frozen acceptance verifier",
            "user-authored or unrelated changes",
            "Do not optimize raw line count",
        ):
            if fragment not in minimization_text:
                errors.append(f"patch minimization reference is missing contract: {fragment}")
        for fragment in (
            "Passing agent-generated patch with multi-step edit history",
            "**Minimize**",
        ):
            if fragment not in text:
                errors.append(f"SKILL.md is missing patch minimization route: {fragment}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        errors.append("missing agents/openai.yaml")
    else:
        ui_text = openai_yaml.read_text(encoding="utf-8")
        prompt = DEFAULT_PROMPT_RE.search(ui_text)
        if not prompt or "$agentic-project-development" not in prompt.group("value"):
            errors.append("openai.yaml default_prompt must mention $agentic-project-development")
        short = SHORT_DESCRIPTION_RE.search(ui_text)
        if not short or not 25 <= len(short.group("value")) <= 64:
            errors.append("openai.yaml short_description must be 25-64 characters")

    if errors:
        fail(errors)

    print(
        "OK: metadata, UI config, and "
        f"{len(listed)} directly listed bundled resources are valid"
    )


if __name__ == "__main__":
    main()
