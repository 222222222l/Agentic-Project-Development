---
name: agentic-project-development
description: Route agentic project work through the lightest reliable combination of Spec-Driven, Behavior/Acceptance-Driven, Test-Driven, Eval-Driven, source-grounded, architecture/domain, agent-system, project-level model and subagent routing, data-flywheel, delivery, review, debugging, uncertainty, trajectory-guided patch minimization, and quantified auto-loop practices. Use when planning, specifying, implementing, testing, evaluating, refactoring, reviewing, minimizing agent-generated patches, or decomposing projects and features; when building LLM or multi-agent systems; when instrumenting structured traces, reusable feedback data, continuous evaluation, or evidence-backed improvement loops; when adapting execution detail or task roles to frontier or open-weight models; or when users request loop, auto, autonomous, keep-going, or run-until-done development.
---

# Agentic Project Development

## Operating Contract

1. Choose the lightest mode that reduces a real risk. Do not force TDD, SDD, BDD, EDD, or multi-agent orchestration onto every task.
2. Select an execution profile before loading detailed references. Honor an explicit user profile; otherwise use `references/model-capability-profiles.md` to choose `frontier-compact` or `portable-guided` from the model-harness capability pair.
3. Before delegating or selecting a specialist model, read `references/project-model-routing.md`. Route by task structure and required capability, minimize execution plus coordination cost, and keep the main agent as owner by default.
4. Ground every material phase in repository or source evidence. Do not let a plausible plan drift away from files, runtime state, tool feedback, or observable acceptance criteria.
5. For loop/auto requests, read `references/loop-auto-mode.md` first. Run a loop only when the verification target is reliably quantifiable; otherwise refuse the loop and continue as an ordinary task.
6. For vague, high-risk, hard-to-reverse, architecture-sensitive, or UX-sensitive work, read `references/uncertainty-and-decision-trace.md` before detailed planning.
7. Stop or abstain when required evidence, permission, runtime capability, or verification is unavailable. Never hide a fatal gate behind an average score or confident prose.
8. After a code-producing task first passes its acceptance verifier, read `references/trajectory-guided-patch-minimization.md` when the patch contains multi-step agent exploration, suspected residual edits, or an explicit simplification request. Minimize only task-owned changes and preserve the passing baseline as rollback.

On Windows, prefer repository-native commands and explicit UTF-8 handling. Change shells only when encoding, quoting, or tool compatibility creates demonstrated friction.

## Workflow

1. **Profile**: choose the instruction-density profile and record whether it came from the user, repo, known alias, or capability self-assessment.
2. **Classify**: map outcome, task structure, required capability, risk, determinism, scope, affected surfaces, delivery target, and verification surface before choosing a model.
3. **Gate**: apply loop quantification, uncertainty, delegation, and independent-verification gates when triggered.
4. **Route**: choose the development modes, execution owner, capability role, worker reuse, and safe fallback. Concrete model IDs are optional runtime aliases.
5. **Ground**: name the evidence for each phase: files, versions, docs, runtime state, scenarios, datasets, or prior artifacts.
6. **Contract**: define each substantial phase as input -> action -> artifact -> verifier -> stop/escalation condition.
7. **Execute**: deliver the smallest vertical slice that can be independently verified. Keep implementation and integration with the main agent unless ownership is deliberately delegated.
8. **Reassess**: re-route when new evidence changes task structure, repeated failure changes the needed capability, or coordination cost exceeds expected value.
9. **Recover**: classify failures as local, upstream, or structural before retrying; prefer localized repair over replaying the full workflow.
10. **Minimize**: after a passing baseline exists, conditionally remove behaviorally unnecessary task-owned edits while preserving the full acceptance contract and maintainability gates.
11. **Converge**: check spec -> plan -> task -> implementation -> verification traceability and record remaining work without relaxing gates.
12. **Explain**: report the chosen/rejected modes and execution routes, evidence, verification, fallbacks, intentional non-changes, and residual risk.

## Mode Router

| Trigger | Primary reference | Common overlays |
| --- | --- | --- |
| New, vague, cross-module, or stakeholder-facing work | `references/spec-driven-development.md` | BDD, architecture, uncertainty |
| User-visible workflow, business rule, permission, or API contract | `references/acceptance-bdd.md` | SDD, TDD, browser verification |
| Deterministic behavior or regression at a known seam | `references/test-driven-development.md` | BDD, source-grounded work |
| LLM, RAG, prompt, routing, semantic, or agent output | `references/eval-driven-development.md` | Agent evaluation, source grounding |
| Current framework, API, protocol, or platform behavior matters | `references/source-driven-development.md` | Any implementation or review mode |
| Agent runtime, tool graph, memory, handoff, durable workflow, or multi-agent system | `references/agent-system-engineering.md` | EDD, source grounding, architecture |
| Project model routing, specialist subagent, worker reuse, or independent verifier | `references/project-model-routing.md` | Agent-system engineering, review |
| Production traces, feedback data, reusable failures, continuous improvement, or data flywheel | `references/data-flywheel-development.md` | Agent evaluation standard, EDD, agent-system engineering |
| Domain concepts, module boundaries, data ownership, or deep refactor | `references/architecture-and-domain.md` | SDD, TDD, decision trace |
| PRD, issue set, multi-session or multi-worker handoff | `references/issue-delivery.md` | SDD, BDD, EDD |
| Review, debugging, release readiness, or completion decision | `references/review-and-quality.md` | Relevant coverage mode |
| Passing agent-generated patch with multi-step edit history, suspected residual edits, or explicit simplification request | `references/trajectory-guided-patch-minimization.md` | Review, TDD/BDD/EDD, architecture |
| Loop, auto, keep-going, or run-until-done | `references/loop-auto-mode.md` | Normal router after quantification |

Use `references/workflow-map.md` when several rows apply or when artifact ordering is unclear.

## Decision Trace

Keep this compact:

```markdown
Model profile / source:
Execution route / source:
Chosen mode / overlays:
Rejected modes:
Evidence loaded:
Artifacts and verifier:
Failure class or open risk:
Next decision:
```

For repeatable repo conventions, create or update `docs/agents/project-development-profile.md` using `references/personalization.md`.

## References

- `references/workflow-map.md`: lifecycle, phase contracts, traceability, convergence, and mode composition.
- `references/model-capability-profiles.md`: self-selection and explicit override for frontier-compact and portable-guided execution.
- `references/project-model-routing.md`: project-level capability roles, delegation gate, worker reuse, total-cost routing, reassessment, and runtime fallbacks.
- `references/loop-auto-mode.md`: quantification gate, bounded loop, state, recovery, and stopping rules.
- `references/uncertainty-and-decision-trace.md`: blind-spot discovery, high-risk decisions, and post-change explanation.
- `references/spec-driven-development.md`: assumptions, specification, planning, tasks, and approval gates.
- `references/source-driven-development.md`: official-source verification for version-sensitive work.
- `references/acceptance-bdd.md`: behavior examples, scenarios, and acceptance-first verification.
- `references/test-driven-development.md`: seam selection, red-green-refactor, and test anti-patterns.
- `references/eval-driven-development.md`: datasets, evaluators, multi-run evidence, and release gates.
- `references/agent-system-engineering.md`: framework selection, agent contracts, state, tracing, recovery, and human control.
- `references/data-flywheel-development.md`: structured run data, trace and feedback contracts, curation, reuse, and the observe-to-release loop.
- `references/agent-evaluation-standard.md`: metric definitions, dataset rules, default thresholds, experiment comparison, and release gates.
- `references/architecture-and-domain.md`: domain modeling, deep modules, ADRs, and stable seams.
- `references/issue-delivery.md`: PRDs, vertical slices, and agent-ready handoffs.
- `references/review-and-quality.md`: spec/standards review, process discipline, debugging, PR, and release gates.
- `references/trajectory-guided-patch-minimization.md`: post-success, acceptance-preserving removal of behaviorally unnecessary task-owned edits.
- `references/personalization.md`: layered repo overrides, tooling, risk gates, and model profile defaults.
- `references/source-map.md`: mapping from installed skills, current frameworks, and research into this suite.

## Scripts

Run `scripts/select_workflow.py` for a deterministic first pass when routing is ambiguous. Run `scripts/test_select_workflow.py` and `scripts/validate_skill_graph.py` after every routing or skill edit.

```powershell
python scripts/select_workflow.py --work-type feature --scope cross-module --task-role code --raw-information-volume high --independent-axes 2 --model-name gpt-5.6-sol --harness-maturity strong
python scripts/test_select_workflow.py
python scripts/validate_skill_graph.py --skill-dir .
```
