# Agentic Project Development

[中文](README.md)

A portable development-workflow Skill for software and Agent projects. It selects specification, behavior/acceptance, testing, evaluation, source grounding, architecture, delivery, and review methods from task scope, risk, determinism, and verifiability, while retaining completion evidence.

This is a workflow/reference layer using the host's existing tools. It is not an Agent runtime and cannot grant models, permissions, or persistent workers.

## Method

- For a simple edit: inspect, change, and perform the relevant check. Add process only to reduce a material risk.
- Define input, action, artifact, verifier, and stop conditions for substantial phases.
- Select testing/evaluation by behavior; TDD is not mandatory for every task.
- Distinguish local, upstream, and structural failures before retrying; retain passed regression obligations.
- Route work by capability and total execution/coordination cost. Reuse related context and require independent evidence where acceptance needs it.
- Treat Skill, context, and harness changes as attributable, reversible candidates rather than assuming instructions improve outcomes.

## Profiles and scope

| Profile/topic | Purpose |
| --- | --- |
| `frontier-compact` | Strong models in mature hosts; compact phase contracts and routed references |
| `portable-guided` | Unfamiliar or limited hosts; explicit phases, state handoffs, bounded delegation |
| SDD/BDD/TDD/EDD | Specification, behavior acceptance, tests, or probabilistic-output evaluation |
| Agent-system engineering | Start with the simplest verifiable design; add state graphs or multiple agents after measured benefit |
| Long tasks and iteration | Explicit verifier, budget/stop rules, dependencies, resume state |
| Patch minimization | Constrained reduction of eligible task-owned edits after behavior passes |

Profiles depend on actual model/harness capabilities; model names are metadata. Persistent execution remains subject to available verifiers, permissions, and stop conditions. See [SKILL.md](agentic-project-development/SKILL.md).

## Install and use

Install `agentic-project-development/` in the host's supported Skill directory. Preserve prior versions outside discovery roots to avoid duplicate Skills.

```text
Use $agentic-project-development to choose the lightest reliable
workflow for this feature, with acceptance, change boundaries,
and completion evidence.
```

Existing repository checks:

```bash
python agentic-project-development/scripts/test_select_workflow.py
python agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
python agentic-project-development/scripts/select_workflow.py --work-type review --scope project --risk high --task-role verification --verification-independence required
```

Stable project conventions may live in `docs/agents/project-development-profile.md`; do not duplicate a new convention document for every task.

## Sources and evidence

[source-map.md](agentic-project-development/references/source-map.md) records provenance and integration boundaries, including addyosmani/agent-skills, fradser/dotclaude, robotlearning123/behavior-driven-testing, promptfoo, and github/awesome-copilot. Integration does not imply endorsement by those authors.

The [research record](agentic-project-development/references/research-evidence-2026-09.md) separates paper results, engineering adaptations, negative evidence, and untested mechanisms. Structural/routing checks establish only exercised behavior. Cross-model or cross-harness productivity gains require paired representative tasks, independent acceptance, and full cost accounting.

Detailed references for context governance, evaluation, feedback data, model routing, and patch minimization remain in [references/](agentic-project-development/references/). No top-level `LICENSE` is currently supplied.
