---
name: agentic-project-development
description: Extensible multi-mode project development skill suite for agentic software work. Use when planning, specifying, implementing, testing, evaluating, refactoring, reviewing, or decomposing a project or feature; when choosing between Spec-Driven Development, Behavior/Acceptance-Driven Development, Test-Driven Development, Eval-Driven Development, source-documented implementation, architecture deepening, issue slicing, or code review; when converting vague project goals into explainable workflows, PRDs, vertical slices, acceptance scenarios, tests, evals, and quality gates.
---

# Agentic Project Development

## Core Rule

Choose the lightest development mode that makes the project safer and more explainable. Do not force TDD, SDD, BDD, or EDD on every task. Classify the work, state the chosen mode and why, then load only the reference files needed for that mode.

Treat this skill as an orchestration layer over project-development practices. It rewrites and integrates the installed Matt Pocock engineering skills plus the researched SDD, source-driven, BDD, and EDD skills into one extensible decision system.

## Workflow

1. Identify the project type, user outcome, risk level, determinism, affected surfaces, existing tests, delivery target, and whether the output is human-facing, machine-facing, or LLM/agent-facing.
2. If the request is vague, first use the alignment gate in `references/workflow-map.md`. Prefer existing project context, files, docs, and tests over asking broad questions.
3. Select a primary mode from the mode router below. Add secondary overlays only when they reduce real risk.
4. Read the relevant reference file before producing a plan, modifying code, or creating artifacts.
5. Produce explicit artifacts: assumptions, success criteria, behavior scenarios, test seams, eval criteria, implementation slices, review gates, or source citations as appropriate.
6. Keep a short decision trace: chosen mode, rejected modes, required artifacts, verification command, and unresolved risks.
7. When the project needs repeatable local conventions, create or update `docs/agents/project-development-profile.md` using `references/personalization.md`.

## Development Mode Router

When several modes apply, use this order: clarify outcome -> specify -> slice -> implement -> verify -> review. Avoid loading every reference.

### Spec-Driven Development

Use SDD when the project or feature is new, ambiguous, cross-module, stakeholder-facing, or likely to take more than one focused session. Read `references/spec-driven-development.md`.

Prefer SDD before `to-prd` when the conversation lacks a stable source of truth. Prefer `to-prd` directly only when enough discussion already exists.

### Source-Driven Development

Use source-driven development when framework, library, API, platform, or protocol correctness depends on current official documentation. Read `references/source-driven-development.md`.

This is an overlay, not a full lifecycle. Combine it with SDD, BDD, TDD, or implementation whenever stale API memory could cause wrong code.

Use `openai-docs` as the official documentation path when the project uses OpenAI products, APIs, models, or Codex surfaces.

### Behavior and Acceptance Driven Development

Use BDD or acceptance-driven development when user-visible behavior, workflows, rules, permissions, forms, payments, onboarding, reporting, or API contracts matter more than internal structure. Read `references/acceptance-bdd.md`.

BDD scenarios can feed SDD success criteria, TDD seams, Playwright/Cucumber tests, or issue acceptance criteria.

For product/UI work, compose with installed `product-design:*` skills for brief gates, visual exploration, image-to-code implementation, or UX audits. Use browser skills for screenshot-backed verification when the implementation is web-facing.

### Test-Driven Development

Use TDD when the behavior is deterministic, the public seam is known, and the main risk is regression or incorrect logic. Read `references/test-driven-development.md`.

Use TDD as one implementation engine, not as the default for every project. Do not write implementation-coupled or tautological tests.

### Eval-Driven Development

Use EDD when the project contains LLM calls, retrieval, agents, prompt chains, classifiers, extractors, scoring, summarization, generation, or other probabilistic outputs. Read `references/eval-driven-development.md`.

Prefer deterministic assertions where possible. Use model-graded or human-review rubrics only where semantic quality cannot be reduced to exact checks.

### Architecture and Domain Design

Use architecture/domain mode when the request changes module boundaries, introduces a new domain concept, deepens or splits modules, touches many files, or asks whether a codebase is becoming hard to change. Read `references/architecture-and-domain.md`.

Keep project vocabulary in `CONTEXT.md` or the repo's configured domain doc. Record durable rejected decisions as ADRs when useful.

For React component architecture, compose with `vercel-composition-patterns`. For non-trivial code changes, apply `karpathy-guidelines` as a lightweight discipline overlay.

### Issue Delivery and Work Decomposition

Use delivery mode when turning a spec, PRD, plan, or conversation into implementation issues, task slices, or AFK-agent work. Read `references/issue-delivery.md`.

Prefer vertical tracer bullets over horizontal layer tasks.

### Review, Debugging, and Quality Gates

Use review mode when auditing a diff, verifying implementation against a spec, diagnosing failures, preparing for release, or deciding whether work is shippable. Read `references/review-and-quality.md`.

Review should compare both standards and specification, then identify missing tests, missing evals, and residual risks.

## Required Decision Families

Always consider these families when enough context exists:

- Goal clarity: user, outcome, non-goals, constraints, success criteria.
- Work shape: feature, bug, refactor, migration, prototype, research, eval, review, release.
- Determinism: exact behavior, probabilistic output, human judgment, external API variability.
- Verification surface: unit seam, integration seam, user journey, eval dataset, source citation, manual QA.
- Project knowledge: domain language, ADRs, docs, issue tracker, existing tests, current architecture.
- Risk: data loss, security, money movement, compliance, performance, reliability, user trust, cost.
- Delivery shape: one local change, vertical slice, PRD, issue set, release gate, long-running roadmap.
- Personalization: repo conventions, preferred tools, issue tracker, test frameworks, eval platform, documentation layout.

## References

Read these files as needed:

- `references/workflow-map.md`: end-to-end lifecycle, mode selection, decision trace, and how installed skills compose.
- `references/spec-driven-development.md`: SDD workflow for assumptions, specifications, planning, tasks, and approval gates.
- `references/source-driven-development.md`: official-doc verification overlay for framework/API/platform-sensitive work.
- `references/acceptance-bdd.md`: BDD/Gherkin and acceptance-first workflow for user-facing behavior.
- `references/test-driven-development.md`: TDD seam selection, red-green loop, anti-patterns, and when not to use TDD.
- `references/eval-driven-development.md`: EDD for LLM/agent/RAG/prompt systems, promptfoo/Pixie-style evals, datasets, rubrics, and CI gates.
- `references/architecture-and-domain.md`: domain modeling, deep modules, architecture review, ADRs, and explainable design vocabulary.
- `references/issue-delivery.md`: PRD creation, issue tracker configuration, vertical slices, and AFK-agent-ready tickets.
- `references/review-and-quality.md`: code review, debugging, release gates, acceptance coverage, and quality risk reporting.
- `references/personalization.md`: repo-level customization profile, mode defaults, tool choices, and extension slots.
- `references/source-map.md`: rewritten-source mapping from installed and researched skills into this suite.

## Scripts

Use `scripts/select_workflow.py` for a deterministic first-pass recommendation when the request has many possible modes.

```powershell
python scripts/select_workflow.py --work-type feature --determinism deterministic --user-facing yes --scope cross-module
```

Use `scripts/validate_skill_graph.py` after editing this skill to verify that all references listed in `SKILL.md` exist.

```powershell
python scripts/validate_skill_graph.py --skill-dir .
```
