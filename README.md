# Agentic Project Development

An extensible Codex skill suite for evidence-grounded project development. It routes work across SDD, BDD, TDD, EDD, source-grounded implementation, architecture/domain design, project-level model and subagent routing, delivery, debugging, review, acceptance-preserving patch minimization, and quantified auto loops without treating any one method as universal.

The suite is a workflow layer, not an agent runtime. It can compose with existing project tools and frameworks while keeping acceptance, verification, and human approval explicit.

## Core Behavior

- Choose the lightest development mode that reduces a real risk.
- Ground every material phase in repository, runtime, or current source evidence.
- Express substantial phases as input -> action -> artifact -> verifier -> stop condition.
- Run loop/auto requests only when the verification target is reliably quantifiable.
- Attribute failures as local, upstream, or structural before retrying.
- Route models by task capability and total execution plus coordination cost; keep one main owner by default.
- Reuse workers for related context and require fresh context when verification must be independent.
- Converge spec, plan, tasks, implementation, and verification before declaring completion.
- Keep context and persistent agent instructions minimal and task-relevant.

## Model Profiles

Instruction density adapts to the complete model-harness configuration, not the model name alone.

### `frontier-compact`

For strong long-horizon coding agents in mature harnesses. The model loads only routed references, gathers ordinary repository context autonomously, keeps compact phase contracts, and relies on executable or external verification.

`gpt-5.6-sol` is a candidate when the current Codex harness supplies reliable tools, state, permissions, traces, and verification. `fable5` remains an explicit user-selectable alias, but the suite does not infer undocumented capabilities from the name.

### `portable-guided`

For open-weight, smaller, unfamiliar, or weakly tooled deployments. It uses explicit ALIGN -> EVIDENCE -> CONTRACT -> SLICE -> IMPLEMENT -> VERIFY -> REVIEW -> CONVERGE phases, re-reads files before edits, checkpoints cross-session work, and restricts multi-agent use to typed handoffs with validators.

Kimi and DeepSeek deployments default here until their actual model-harness pair passes project-representative multi-run evals. Users can explicitly promote a tested deployment.

Examples:

```text
Use $agentic-project-development with the frontier-compact profile for this feature.
Use $agentic-project-development with portable-guided and keep a task state file.
Treat this Kimi deployment as frontier-compact; its harness passed our repo eval.
```

## Project Model Routing

The suite can implement project-level routing policy in Codex: classify each work unit, choose a semantic capability role, decide whether delegation is worth its coordination cost, reuse a related worker, and request a fresh verifier. A project can map evaluated roles to model IDs in `docs/agents/project-development-profile.md`.

The boundary is explicit. A skill cannot force-switch the current main model, expose a model the active host does not provide, guarantee subagent persistence across sessions, or compute exact cost without telemetry. Runtime capability wins; unavailable model requests fall back to the nearest exposed role and must be reported.

Default route:

```text
ROUTE -> EXECUTE -> REASSESS -> VERIFY
```

Start with the main agent. Delegate only high-volume exploration, independent investigation axes, meaningful specialist capability, or high-risk independent verification. Optimize total cost as execution + context loading + handoff + retry + verification.

## Workflow

```text
PROFILE -> GATE -> ROUTE -> ALIGN -> GROUND -> SPECIFY -> SLICE
        -> EXECUTE -> REASSESS -> VERIFY -> RECOVER -> MINIMIZE -> CONVERGE -> EXPLAIN
```

The normal mode router defines acceptance and testing. Patch minimization is a conditional post-success gate for eligible task-owned edits, and auto-loop mode only adds bounded repetition after a reliable quantification gate.

## Auto Loop Rule

For loop, auto, keep-going, or run-until-done requests:

1. Name the verifier, exact metrics, hard gates, rubric grader, threshold, budget, and max rounds.
2. Refuse the loop when checks are subjective, unavailable, non-repeatable, or controlled only by the same agent's preference.
3. Run `PLAN -> DO -> VERIFY -> DECIDE` after the gate passes.
4. Stop only when all hard gates and exact thresholds pass and every required rubric score is at least 8.
5. Diagnose the weakest failure before localized repair, partial re-execution, or structural re-planning.

## Agent-System Engineering

The agent-system reference starts with the simplest viable design: deterministic code, one structured model call, one tool-using agent, a deterministic workflow, then a stateful graph or multi-agent topology only when measured value justifies coordination cost.

It includes selection gates for:

- OpenAI Agents SDK;
- Microsoft Agent Framework;
- LangGraph;
- Pydantic AI;
- SWE-agent and OpenHands as software-engineering reference harnesses;
- GitHub Spec Kit and Superpowers as development methodologies rather than runtimes.

No framework is installed or required by this repository.

## Repository Layout

```text
agentic-project-development/
  SKILL.md
  agents/openai.yaml
  references/
    workflow-map.md
    model-capability-profiles.md
    project-model-routing.md
    loop-auto-mode.md
    uncertainty-and-decision-trace.md
    spec-driven-development.md
    source-driven-development.md
    acceptance-bdd.md
    test-driven-development.md
    eval-driven-development.md
    agent-system-engineering.md
    data-flywheel-development.md
    agent-evaluation-standard.md
    architecture-and-domain.md
    issue-delivery.md
    review-and-quality.md
    trajectory-guided-patch-minimization.md
    personalization.md
    source-map.md
  scripts/
    select_workflow.py
    test_select_workflow.py
    validate_skill_graph.py
```

`SKILL.md` stays navigational. Detailed methods are loaded only when routed, and deterministic checks live in `scripts/`.

## Install

Place `agentic-project-development/` under:

```text
$CODEX_HOME/skills/agentic-project-development
```

When `CODEX_HOME` is unset, the usual location is:

```text
~/.codex/skills/agentic-project-development
```

Restart Codex after installation so skill metadata is reloaded.

## Personalization

For stable repository conventions, create:

```text
docs/agents/project-development-profile.md
```

Override precedence is: explicit task instruction -> project profile/artifacts -> organization preset -> suite defaults. Profiles can set model execution detail, test/eval commands, state paths, framework preferences, approval boundaries, fatal gates, and non-functional constraints.

Project profiles can also set evaluated role-to-model aliases, maximum explorers, worker reuse keys, fresh-verifier triggers, total-cost preference, and unavailable-model fallback. These are policies, not new runtime permissions.

## Validation

Use the bundled Python runtime when `python` is unavailable on `PATH`.

```bash
python agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
python agentic-project-development/scripts/test_select_workflow.py
```

Try frontier and portable routing:

```bash
python agentic-project-development/scripts/select_workflow.py --work-type feature --scope cross-module --model-name gpt-5.6-sol --harness-maturity strong
python agentic-project-development/scripts/select_workflow.py --work-type agent-system --determinism llm --model-name Kimi-K2.7-Code --harness-maturity partial --risk high
python agentic-project-development/scripts/select_workflow.py --work-type review --scope project --risk high --task-role verification --verification-independence required
```

## Research Basis

Research and model evidence in this revision was checked on 2026-07-10.

The trajectory-guided patch-minimization evidence and adaptation boundary were checked against TRIM (arXiv:2607.18161v1) on 2026-07-21.

The project-routing boundary was checked against the active Codex subagent interface on 2026-07-16. Concrete model availability remains host-specific.

The current constraints absorb evidence from GitHub Spec Kit, Superpowers, Evaluating AGENTS.md, Agent READMEs, Spec Kit Agents, RigorBench, Harness-Bench, Meta-Agent, AgentTether, RAMP, TRIM, and empirical studies of rejected agent-authored PRs. See `agentic-project-development/references/source-map.md` for links and the exact mapping.

The practical result is intentionally conservative: minimal persistent context, repository-grounded phases, explicit contracts, process-discipline gates, model-harness evaluation, localized recovery, and human-readable evidence before completion.
