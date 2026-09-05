# Personalization and Extension

## Contents

- Override precedence
- Repo profile template
- Project model routing
- Skill and context governance
- Extension pattern
- Personal defaults

## Override Precedence

Resolve conflicts in this order:

1. Explicit user instruction for the current task.
2. Project-local profile and task artifacts.
3. Organization or team preset.
4. This skill suite's defaults.

Keep overrides small. A profile should contain only information that changes agent behavior in this repository.
This precedence applies within project workflow preferences; it cannot override
the active host's system/developer instructions or grant unavailable authority.

## Repo Profile

Create `docs/agents/project-development-profile.md` when a repo needs stable local preferences.

```markdown
# Project Development Profile

## Default Mode Preferences

- Model profile default:
- Model-harness configurations already promoted by eval:
- Default lifecycle:
- Auto loop default:
- Per-hypothesis retry budget / overall task budget:
- Acceptance thresholds and stopping rule:
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

## Project Model Routing

- Routing enabled:
- Default orchestrator capability:
- Evaluated role -> model aliases:
- Harness-exposed model IDs:
- Maximum explorers:
- Delegate high raw-information exploration:
- Keep implementation owner:
- Reuse key:
- Fresh verifier required for:
- Total-cost preference:
- Model-unavailable fallback:
- User approval required for:

## Skill and Context Governance

- Allowed Skill sources and trust classes:
- Skill marginal-coverage rule and context budget:
- Version and incompatibility checks:
- Third-party Skill inspection and permission policy:
- With/without Skill eval command and dataset:
- Persistent context source-of-truth paths:
- Rules that must not be duplicated into AGENTS/context files:
- Context-pressure and stale-state signals:
- Compaction or progress-state policy promoted by eval:
- Evidence artifact store and stable reference format:
- Sealed confirmation set and promotion approver:

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
- Do not optimize against an unavailable, unrepeatable or uncalibrated verifier;
  build reliable verification or continue ordinary work. A repeatable human
  rubric can be valid when its calibration and decision rule fit the claim.
- Set task-specific acceptance and budget before optimization; do not apply a
  universal rubric score or round count.
- Use SDD when cross-module ambiguity or dependencies warrant a durable contract.
- Use BDD for user journeys and business rules.
- Use TDD for deterministic logic and regressions.
- Use EDD only for LLM/semantic quality.
- Use source-driven development for fast-moving frameworks and APIs.
- Use issue slicing only when work will span multiple sessions or agents.
- Add guidance for unfamiliar or weak phases based on the actual model-harness
  pair, regardless of vendor or weight access; compact guidance is valid when
  capability is observed.
- Keep one main execution owner; delegate only when specialization, independent exploration, or fresh verification exceeds coordination cost.
- Reuse a worker for the same objective, module, data flow, and trust boundary; use a fresh context for independent verification.
- Keep AGENTS/context files minimal: exact commands, boundaries, non-functional constraints, and hazards only.
- Treat third-party Skills as untrusted until source, content, dependencies,
  permissions, and task applicability are established.
- Keep task-generated Skill refinements temporary until paired held-out evidence
  promotes them; do not auto-retire shared Skills from low use alone.
