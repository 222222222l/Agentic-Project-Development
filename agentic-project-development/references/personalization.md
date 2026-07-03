# Personalization and Extension

## Repo Profile

Create `docs/agents/project-development-profile.md` when a repo needs stable local preferences.

```markdown
# Project Development Profile

## Default Mode Preferences

- Default lifecycle:
- Prefer SDD when:
- Prefer BDD when:
- Prefer TDD when:
- Prefer EDD when:

## Tooling

- Package manager:
- Test commands:
- E2E command:
- Eval command:
- Lint/typecheck/build:

## Documentation

- Domain docs:
- ADR path:
- Spec path:
- Issue tracker:

## Quality Gates

- Required before PR:
- Required before release:
- Manual checks:

## Local Conventions

- Naming:
- Branching:
- Commit style:
- Security/data constraints:

## Custom Modes

- Mode name:
- Trigger:
- Reference file:
- Verification gate:
```

## Extension Pattern

To add a new mode:

1. Add a short router section to `SKILL.md`.
2. Add one reference file in `references/`.
3. Add the file to the References list.
4. Update `source-map.md` if it adapts an external skill.
5. Run `scripts/validate_skill_graph.py`.

Do not add large details to `SKILL.md`. Keep the entry point navigational.

## Personal Defaults

Good defaults for solo project development:

- Use SDD for any feature touching more than one module.
- Use BDD for user journeys and business rules.
- Use TDD for deterministic logic and regressions.
- Use EDD only for LLM/semantic quality.
- Use source-driven development for fast-moving frameworks and APIs.
- Use issue slicing only when work will span multiple sessions or agents.
