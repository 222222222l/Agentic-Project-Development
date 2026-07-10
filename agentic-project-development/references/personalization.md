# Personalization and Extension

## Contents

- Override precedence
- Repo profile template
- Extension pattern
- Personal defaults

## Override Precedence

Resolve conflicts in this order:

1. Explicit user instruction for the current task.
2. Project-local profile and task artifacts.
3. Organization or team preset.
4. This skill suite's defaults.

Keep overrides small. A profile should contain only information that changes agent behavior in this repository.

## Repo Profile

Create `docs/agents/project-development-profile.md` when a repo needs stable local preferences.

```markdown
# Project Development Profile

## Default Mode Preferences

- Model profile default:
- Model-harness configurations already promoted by eval:
- Default lifecycle:
- Auto loop default:
- Max auto loop rounds:
- Minimum loop passing score:
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
- Loop verifiers:
- Loop state path:
- Fatal gates:
- Security/performance/reliability/cost checks:

## Agent Systems

- Preferred framework or no-framework rule:
- Trace/observability backend:
- State/checkpoint backend:
- Human approval boundaries:
- Eval dataset and repeated-run count:

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

- Use auto loop mode only when the user asks for loop/auto/run-until-done behavior and the target can be reliably quantified.
- Refuse loop execution when the verifier is subjective, unavailable, or not repeatable; continue as an ordinary task.
- Default to 3 loop rounds and require every loop criterion to score at least 8.
- Use SDD for any feature touching more than one module.
- Use BDD for user journeys and business rules.
- Use TDD for deterministic logic and regressions.
- Use EDD only for LLM/semantic quality.
- Use source-driven development for fast-moving frameworks and APIs.
- Use issue slicing only when work will span multiple sessions or agents.
- Default unknown or open-weight model-harness pairs to `portable-guided`; promote only from project-representative eval evidence.
- Keep AGENTS/context files minimal: exact commands, boundaries, non-functional constraints, and hazards only.
