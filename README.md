# Agentic Project Development

An extensible Codex skill suite for project development work across multiple modes:
Spec-Driven Development (SDD), Behavior/Acceptance-Driven Development (BDD),
Test-Driven Development (TDD), Eval-Driven Development (EDD), source-driven
implementation, architecture/domain design, issue delivery, debugging, and review.

The suite is designed as an orchestration layer. It does not force every project
through TDD. Instead, it chooses the lightest workflow that makes the work safer,
more explainable, and easier to verify.

## Install

Install the skill folder from this repository:

```bash
scripts/install-skill-from-github.py --repo 222222222l/Agentic-Project-Development --path agentic-project-development
```

You can also install manually by copying `agentic-project-development/` into:

```text
$CODEX_HOME/skills/agentic-project-development
```

If `CODEX_HOME` is not set, Codex normally uses:

```text
~/.codex/skills/agentic-project-development
```

Restart Codex after installing so the skill metadata is reloaded.

## What This Skill Does

Use `$agentic-project-development` when planning, specifying, implementing,
testing, evaluating, refactoring, reviewing, or decomposing a project or feature.

The skill helps an agent:

- classify the shape and risk of a project task;
- choose between SDD, BDD, TDD, EDD, source-driven work, architecture mode,
  issue delivery, or review mode;
- load only the reference files needed for the chosen mode;
- produce explicit artifacts such as assumptions, specs, acceptance scenarios,
  test seams, eval criteria, issue slices, ADRs, or review gates;
- keep a short decision trace that explains why the mode was selected;
- preserve room for project-specific personalization.

## Repository Layout

```text
agentic-project-development/
  SKILL.md
  agents/
    openai.yaml
  references/
    workflow-map.md
    spec-driven-development.md
    source-driven-development.md
    acceptance-bdd.md
    test-driven-development.md
    eval-driven-development.md
    architecture-and-domain.md
    issue-delivery.md
    review-and-quality.md
    personalization.md
    source-map.md
  scripts/
    select_workflow.py
    validate_skill_graph.py
```

`SKILL.md` is intentionally concise. Detailed workflows live in `references/`
and are loaded only when needed. Deterministic helpers live in `scripts/`.

## Integrated Local Skills

This suite rewrites and integrates the local development-related skills into a
single project-development router:

- `clarify-project-requirements`
- `karpathy-guidelines`
- `grill-with-docs`
- `grilling`
- `domain-modeling`
- `codebase-design`
- `setup-matt-pocock-skills`
- `to-prd`
- `to-issues`
- `tdd`
- `improve-codebase-architecture`
- `code-review`
- `diagnosing-bugs`
- `vercel-composition-patterns`
- `openai-docs`
- `product-design:get-context`
- `product-design:audit`
- `product-design:ideate`
- `product-design:image-to-code`
- `browser:control-in-app-browser`
- `chrome:control-chrome`

It also records which installed local skills were reviewed but intentionally
kept outside the core router because they are domain, artifact, discovery, or
meta-skill specialists. See `agentic-project-development/references/source-map.md`.

## Researched Skills Rewritten Into This Suite

The suite incorporates the useful ideas from researched agent skill frameworks,
without copying them verbatim:

- `addyosmani/agent-skills` Spec-Driven Development
- `addyosmani/agent-skills` Source-Driven Development
- `fradser/dotclaude` Behavior-Driven Development
- `robotlearning123/behavior-driven-testing`
- `promptfoo/promptfoo` promptfoo evals
- `github/awesome-copilot` Eval-Driven Development

See `agentic-project-development/references/source-map.md` for the mapping.

## Example Prompts

```text
Use $agentic-project-development to choose the right development workflow for this feature.
```

```text
Use $agentic-project-development to turn this vague app idea into a spec, acceptance scenarios, and implementation slices.
```

```text
Use $agentic-project-development for this LLM extraction pipeline and define the eval gates before implementation.
```

```text
Use $agentic-project-development to review whether this PR satisfies the spec and has enough verification.
```

## Validation

Validate the skill graph after edits:

```bash
python agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
```

Try the deterministic workflow selector:

```bash
python agentic-project-development/scripts/select_workflow.py --work-type feature --determinism deterministic --user-facing yes --scope cross-module
```

## Extension Points

Customize a project by adding or updating:

```text
docs/agents/project-development-profile.md
```

The personalization reference supports local defaults for:

- preferred development modes;
- test and eval frameworks;
- issue tracker conventions;
- documentation layout;
- risk gates;
- source-documentation preferences;
- project-specific vocabulary and ADR practices.

## Design Principles

- Use the lightest workflow that reduces real risk.
- Prefer explicit success criteria over ritual process.
- Treat TDD as one implementation mode, not a universal default.
- Use BDD when user-visible behavior is the contract.
- Use EDD when semantic or probabilistic output quality matters.
- Use source-driven development when current docs can invalidate memory.
- Keep project-specific decisions explainable and auditable.
