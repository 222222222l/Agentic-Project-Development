# Agent System Engineering

## Use When

Use this mode when building or changing an LLM agent, coding agent, tool-using workflow, memory system, evaluator, handoff graph, durable run, or multi-agent application.

## Architecture Rule

Start with the simplest executable design that can satisfy the acceptance and eval gates:

1. Deterministic code without an agent when rules are known.
2. One model call with structured input/output.
3. One agent with a small tool set.
4. A deterministic workflow around one or more agents.
5. A stateful graph or multi-agent system only when parallelism, specialization, durability, or independent verification has measured value.

Do not use multiple agents merely to simulate an organization. Each added agent must own a distinct capability or independent check that exceeds its coordination cost.

## Project Runtime Routing

Use `project-model-routing.md` when routing project work through the current Codex or another agent harness. Keep orchestration and integration with one main owner. Select subagents by semantic capability role first and map to concrete model IDs only when the active runtime exposes them.

The routing skill is policy, not a scheduler. It may request an exposed subagent model, reuse a worker handle, and require fresh verification, but it cannot switch the current main model or create persistence and telemetry the harness does not provide.

## Required Contracts

For every node or agent, define:

```markdown
Responsibility:
Allowed inputs and tools:
Structured output:
Verifier:
Side effects and approvals:
Retry budget:
Escalation / abstention:
```

Keep state transitions explicit. Persist only information needed for recovery, audit, or future decisions.

## Reliability Workflow

1. Define capabilities, unacceptable failures, and fatal gates.
2. Build a representative multi-run task suite before optimizing prompts or topology.
3. Instrument tool calls, state transitions, approvals, token/cost signals,
   artifacts, and verifier outputs. For coding agents eligible for patch
   minimization, preserve normalized task-owned edit sequence, file,
   before/after artifact references, feedback request, and final-survival
   linkage; use `trajectory-guided-patch-minimization.md` rather than creating a
   second trace system.
4. Separate exact metrics, threshold gates, and human preference using `agent-evaluation`.
5. Diagnose failed trajectories as:
   - **Local**: one node, tool call, schema, or action is wrong; retry or repair that unit.
   - **Upstream**: a valid downstream step received bad context; repair from the source transition.
   - **Structural**: decomposition, topology, contract, or verifier is wrong; re-plan the graph.
6. Prefer localized retry, partial re-execution, or re-decomposition over full blind replay.
7. Preserve a compact repair memory: failure evidence, attributed cause, correction, and boundary where it applies.
8. Re-run the task suite across more than one seed or attempt before release.
9. Reassess model and worker routing when a failure becomes upstream or structural, rather than assuming the original specialization remains correct.

## Framework Selection

Choose a framework only after identifying the missing runtime property:

| Need | Candidate | Why |
| --- | --- | --- |
| Lightweight Python agents, tools, handoffs, guardrails, sessions, tracing, sandbox work | OpenAI Agents SDK | Small core with explicit agent primitives and long-horizon sandbox support |
| Python/.NET production workflows, graph orchestration, checkpointing, OTel, governance, HITL | Microsoft Agent Framework | Broad production and enterprise runtime surface |
| Low-level stateful graphs, durable execution, interrupts, memory, trajectory inspection | LangGraph | Fine control over long-running state transitions |
| Typed Python outputs, dependency injection, provider portability, evals, OTel, durable runs | Pydantic AI | Strong schema and validation boundaries |
| Autonomous software-engineering runtime experiments | SWE-agent or OpenHands | Useful reference harnesses and benchmarks, not default app libraries |
| Spec-first coding-agent methodology | GitHub Spec Kit | Executable spec/plan/task/converge artifacts, not an agent runtime |
| Skill-driven coding discipline | Superpowers | Composable methodology and behavior evals; its universal TDD rule is optional here |

Do not install or migrate frameworks solely because they are popular. Preserve the repository's existing runtime when it already supplies the needed state, tracing, validation, and recovery.

## Model-Harness Evaluation

Evaluate the full configuration, not the base model name. Record model/version, prompt or skill set, tool schemas, context policy, permissions, retry limits, state backend, and verifier. A model may move between capability profiles when the harness changes.

Minimum release evidence:

- Exact task outcomes and fatal gate pass rate.
- Verification coverage and unsupported self-claims.
- Recovery efficiency after injected or natural failures.
- Abstention quality when evidence or permissions are missing.
- Cost, latency, turns, and repeated-run variance.
- Trace packets for human review of subjective quality.

## Human Control

Require explicit approval for consequential external actions. Keep authorization separate from model confidence. Make retries idempotent where possible, attach rollback or compensation to side effects, and never let a recovered trajectory conceal an earlier external mutation.
