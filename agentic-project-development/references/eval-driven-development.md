# Eval-Driven Development

## Use When

Use EDD for LLM, agent, RAG, prompt, tool-calling, classification, extraction, summarization, generation, routing, ranking, or semantic QA systems where exact-output unit tests are insufficient.

Use deterministic tests for deterministic code around the LLM. Use evals for semantic quality and distributional behavior.

## Eval Artifacts

- Capability inventory: what the system must do.
- Failure modes: ways the system can be wrong.
- Dataset: realistic inputs covering common, edge, and adversarial-ish cases.
- Evaluators: deterministic checks, schema checks, similarity checks, rubric graders, or human review.
- Baseline run: current score and examples.
- Action plan: prioritized changes backed by eval evidence.
- Run metadata: model/version, harness, prompt/skills, tools, context policy, permissions, budgets, and seeds.

## Tool Choices

Use `promptfoo-evals` style when the project needs a general eval suite for prompts, endpoints, RAG pipelines, or agent outputs and can run through `promptfoo`.

Use Pixie/eval-driven-dev style when working on a Python LLM application that benefits from instrumentation, real app execution, golden datasets, evaluator mapping, and persisted analysis artifacts.

Do not mock the core LLM in evals. Mock or instrument external data sources only when needed to control scenario inputs.

## Workflow

1. Define quality criteria and failure modes.
2. Build or locate the eval harness.
3. Create a small but representative dataset first.
4. Split metrics into exact quantitative measures, fatal/threshold gates, and human preference scores.
5. Add evaluators; prefer deterministic assertions where possible.
6. Run repeated trials and preserve raw outputs and trajectories.
7. Analyze failures before changing prompts, code, topology, or model profile.
8. Compare the complete model-harness configuration, not model names in isolation.
9. Add the eval to CI or a documented release gate when stable.

## Integration

- Use SDD to define quality goals before eval construction.
- Use BDD to express user-facing semantic scenarios.
- Use source-driven development for SDK/tool-calling/eval-platform correctness.
- Use review mode to compare code changes against eval deltas.
- Use `agent-evaluation` for multi-run task suites, fatal gates, trace packets, and weighted reporting.
- Use `agent-system-engineering.md` for tool graphs, memory, handoffs, recovery, observability, and framework decisions.

## Output Contract

Report:

- What capability was evaluated.
- Dataset coverage.
- Evaluators used and why.
- Baseline score or qualitative result.
- Failure examples.
- Next improvement slice.
- Repeated-run variance, fatal failures, and missing evidence.

Never let an average score hide a fatal failure. Keep subjective scores empty until a human or explicitly declared grader actually reviews the trace.
