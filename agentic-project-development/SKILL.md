---
name: agentic-project-development
description: Route agentic project work through the lightest reliable combination of Spec-Driven, Behavior/Acceptance-Driven, Test-Driven, Eval-Driven, source-grounded, architecture/domain, agent-system, delivery, review, debugging, uncertainty, and quantified auto-loop practices. Use when planning, specifying, implementing, testing, evaluating, refactoring, reviewing, or decomposing projects and features; when building LLM or multi-agent systems; when adapting execution detail to frontier or open-weight models; or when users request loop, auto, autonomous, keep-going, or run-until-done development.
---

# Agentic Project Development

## Operating Contract

1. Choose the lightest mode that reduces a real risk. Do not force TDD, SDD, BDD, EDD, or multi-agent orchestration onto every task.
2. Select an execution profile before loading detailed references. Honor an explicit user profile; otherwise use `references/model-capability-profiles.md` to choose `frontier-compact` or `portable-guided` from the model-harness capability pair.
3. Ground every material phase in repository or source evidence. Do not let a plausible plan drift away from files, runtime state, tool feedback, or observable acceptance criteria.
4. For loop/auto requests, read `references/loop-auto-mode.md` first. Run a loop only when the verification target is reliably quantifiable; otherwise refuse the loop and continue as an ordinary task.
5. For vague, high-risk, hard-to-reverse, architecture-sensitive, or UX-sensitive work, read `references/uncertainty-and-decision-trace.md` before detailed planning.
6. Stop or abstain when required evidence, permission, or verification is unavailable. Never hide a fatal gate behind an average score or confident prose.

On Windows, prefer repository-native commands and explicit UTF-8 handling. Change shells only when encoding, quoting, or tool compatibility creates demonstrated friction.

## Workflow

1. **Profile**: choose the model execution profile and record whether it came from the user, a known alias, or capability self-assessment.
2. **Classify**: identify outcome, work shape, risk, determinism, scope, affected surfaces, delivery target, and verification surface.
3. **Gate**: apply loop quantification and uncertainty gates when triggered.
4. **Route**: choose one primary mode and only the overlays that reduce material risk.
5. **Ground**: name the evidence for each phase: files, versions, docs, runtime state, scenarios, datasets, or prior artifacts.
6. **Contract**: define each substantial phase as input -> action -> artifact -> verifier -> stop/escalation condition.
7. **Execute**: deliver the smallest vertical slice that can be independently verified.
8. **Recover**: classify failures as local, upstream, or structural before retrying; prefer localized repair over replaying the full workflow.
9. **Converge**: check spec -> plan -> task -> implementation -> verification traceability and record remaining work without relaxing gates.
10. **Explain**: report the chosen/rejected modes, evidence, verification, intentional non-changes, and residual risk.

## Mode Router

| Trigger | Primary reference | Common overlays |
| --- | --- | --- |
| New, vague, cross-module, or stakeholder-facing work | `references/spec-driven-development.md` | BDD, architecture, uncertainty |
| User-visible workflow, business rule, permission, or API contract | `references/acceptance-bdd.md` | SDD, TDD, browser verification |
| Deterministic behavior or regression at a known seam | `references/test-driven-development.md` | BDD, source-grounded work |
| LLM, RAG, prompt, routing, semantic, or agent output | `references/eval-driven-development.md` | Agent evaluation, source grounding |
| Current framework, API, protocol, or platform behavior matters | `references/source-driven-development.md` | Any implementation or review mode |
| Agent runtime, tool graph, memory, handoff, durable workflow, or multi-agent system | `references/agent-system-engineering.md` | EDD, source grounding, architecture |
| Domain concepts, module boundaries, data ownership, or deep refactor | `references/architecture-and-domain.md` | SDD, TDD, decision trace |
| PRD, issue set, multi-session or multi-worker handoff | `references/issue-delivery.md` | SDD, BDD, EDD |
| Review, debugging, release readiness, or completion decision | `references/review-and-quality.md` | Relevant coverage mode |
| Loop, auto, keep-going, or run-until-done | `references/loop-auto-mode.md` | Normal router after quantification |

Use `references/workflow-map.md` when several rows apply or when artifact ordering is unclear.

## Decision Trace

Keep this compact:

```markdown
Model profile / source:
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
- `references/loop-auto-mode.md`: quantification gate, bounded loop, state, recovery, and stopping rules.
- `references/uncertainty-and-decision-trace.md`: blind-spot discovery, high-risk decisions, and post-change explanation.
- `references/spec-driven-development.md`: assumptions, specification, planning, tasks, and approval gates.
- `references/source-driven-development.md`: official-source verification for version-sensitive work.
- `references/acceptance-bdd.md`: behavior examples, scenarios, and acceptance-first verification.
- `references/test-driven-development.md`: seam selection, red-green-refactor, and test anti-patterns.
- `references/eval-driven-development.md`: datasets, evaluators, multi-run evidence, and release gates.
- `references/agent-system-engineering.md`: framework selection, agent contracts, state, tracing, recovery, and human control.
- `references/architecture-and-domain.md`: domain modeling, deep modules, ADRs, and stable seams.
- `references/issue-delivery.md`: PRDs, vertical slices, and agent-ready handoffs.
- `references/review-and-quality.md`: spec/standards review, process discipline, debugging, PR, and release gates.
- `references/personalization.md`: layered repo overrides, tooling, risk gates, and model profile defaults.
- `references/source-map.md`: mapping from installed skills, current frameworks, and research into this suite.

## Scripts

Run `scripts/select_workflow.py` for a deterministic first pass when routing is ambiguous. Run `scripts/validate_skill_graph.py` after every skill edit.

```powershell
python scripts/select_workflow.py --work-type feature --scope cross-module --model-name gpt-5.6-sol --harness-maturity strong
python scripts/validate_skill_graph.py --skill-dir .
```
