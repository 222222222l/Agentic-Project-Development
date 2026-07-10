# Model Capability Profiles

## Purpose

Adapt instruction density to the model plus execution harness. Treat model capability as a property of the full configuration: model, tools, context policy, permissions, state, tracing, and verifier.

## Selection Order

1. Honor an explicit user choice: `frontier-compact` or `portable-guided`.
2. Honor a repo default from `docs/agents/project-development-profile.md` when the user is silent.
3. Otherwise self-assess the model-harness pair using the capability probe below.
4. When uncertain, choose `portable-guided`. Record the selection source in the decision trace.

Known names are hints, not proof:

- Treat `gpt-5.6-sol` as a `frontier-compact` candidate when the current harness exposes reliable tools, state, and verification.
- Treat `fable5` or `fable-5` as a user-selectable frontier alias only when the runtime exposes that model or agent. Public evidence is currently trace-oriented, so do not infer hidden capabilities from the name alone.
- Default open-weight Kimi, DeepSeek, Qwen, and similar deployments to `portable-guided` until the actual harness passes project-local evals. A user may override this after evidence.

## Capability Probe

Choose `frontier-compact` only when all are true:

- Reliably inspect files, repository state, and tool outputs before acting.
- Preserve outcome, constraints, and verifier across long or compacted contexts.
- Follow conditional references without loading the entire skill bundle.
- Produce schema-stable artifacts and respect explicit stop or abstention gates.
- Attribute failures from evidence and change strategy instead of blindly repeating.
- Run the named verifier and distinguish observed results from self-assessment.
- The harness exposes safe file/tool execution, permissions, state, and useful traces.

Otherwise choose `portable-guided`.

## Frontier-Compact

Use for strong long-horizon coding agents in mature harnesses.

- Load only this file, the router-selected mode references, and task-local evidence.
- Let the model gather ordinary repo context autonomously; ask only direction-changing questions.
- Keep plans outcome-oriented. Expand steps only at high-risk or hard-to-reverse decisions.
- Use compact phase contracts and one decision trace instead of repeating instructions.
- Verify with executable or external evidence; do not add prose checkpoints that have no decision value.
- Use multi-agent work only when tasks are independent, ownership is disjoint, and integration has a named verifier.
- After compaction or handoff, preserve goal, constraints, changed files, evidence, verifier, failures, and next action.

Minimum phase contract:

```markdown
Outcome:
Evidence:
Change boundary:
Verifier:
Stop / escalate when:
```

## Portable-Guided

Use for open-weight, smaller, unfamiliar, weakly tooled, or unevenly instruction-following model-harness pairs.

Run phases explicitly:

1. **ALIGN**: restate outcome, non-goals, constraints, and done criteria.
2. **EVIDENCE**: list exact files, versions, runtime state, sources, and unresolved assumptions.
3. **CONTRACT**: define input, action, artifact, verifier, and stop condition for the next phase.
4. **SLICE**: choose one vertical, independently verifiable increment.
5. **IMPLEMENT**: make only the scoped change; list touched files and deviations.
6. **VERIFY**: run the named command or evaluator and preserve raw failures.
7. **REVIEW**: check spec fidelity first, engineering quality second, residual risk third.
8. **CONVERGE**: map acceptance criteria to evidence and name remaining work.

Additional constraints:

- Read one routed reference at a time and summarize its operative rules before acting.
- Use explicit file paths, commands, expected outputs, and acceptance examples.
- For multi-step or cross-session work, maintain a task state file with completed evidence and next action.
- Re-read current files before edits; do not rely on remembered repository state.
- Require a clean or understood baseline before attributing new failures to the change.
- Classify a failure as local, upstream, or structural before retrying.
- Prefer one worker. Add agents only when the harness supports isolation and every handoff has typed inputs, outputs, and validators.
- Checkpoint after each slice; do not batch unrelated edits behind one final test.

## User Overrides

Accept natural-language directives such as:

```text
Use the frontier-compact profile for this task.
Use the portable-guided profile and keep a state file.
Treat this Kimi deployment as frontier-compact; its harness passed our repo eval.
```

An override changes instruction density, not safety, approval, source, or verification gates.

## Promotion Rule

Promote a model-harness pair from `portable-guided` only after repeated project-representative runs show acceptable task success, verification coverage, recovery, abstention, cost, and trace quality. Use `agent-evaluation` for multi-run evidence; do not promote from one successful demo.
