# Auto Loop Mode

## Use When

Use this reference when the user asks for loop, auto, autonomous iteration, keep-going, self-running, repeated improvement, run-until-done, or similar behavior.

Auto loop mode is a control wrapper around the normal development modes. It does not replace SDD, BDD, TDD, EDD, source-driven work, architecture review, debugging, or code review. Those modes still define the acceptance and testing standards.

## Non-Negotiable Gate

Run a loop only when the verification target can be reliably quantified.

Reliable quantification means:

- The target has observable metrics or binary gates.
- The verification method is independent enough that the same agent is not merely grading its own preference.
- The check can be repeated on the same inputs with comparable results.
- The command, dataset, source, artifact, screenshot, or rubric used to verify is named before the loop starts.
- The stopping rule is explicit before implementation begins.

If this gate fails, do not run auto loop mode. Tell the user that the request is not suitable for a loop, explain which quantification property is missing, and continue as an ordinary task through the normal router.

## Quantification Design

Before the first loop iteration, produce a compact verification scheme:

```markdown
## Auto Loop Gate

Loop request:
Quantified target:
Verifier:
Metrics or gates:
Passing threshold:
Max rounds:
State file:
Fallback if not quantifiable:
```

Good quantified targets include:

- Tests, typecheck, lint, build, benchmark, migration dry-run, or smoke command passes.
- API or UI scenario passes with explicit inputs and expected outputs.
- Eval dataset score reaches a stated threshold with failure examples preserved.
- Documentation/source audit covers named official pages or files.
- Review checklist scores every required criterion at or above the threshold.
- Bug reproduction fails before the fix and passes after the fix.

Weak targets that should not start a loop by themselves:

- "Make it better", "polish it", "optimize it", "improve quality", or "keep going" without a measurable verifier.
- Purely subjective taste unless converted into a rubric with examples and a stable reviewer.
- Work blocked by credentials, unavailable systems, missing data, or manual decisions the agent cannot observe.
- Architecture exploration where the only success signal is preference rather than a constrained tradeoff.

## Four-Step Cycle

Each round repeats the same protocol.

### PLAN

State the next smallest action and which metric or failing criterion it targets.

### DO

Make the change or improve the current result. Keep changes scoped to the target criterion.

### VERIFY

Run the named verifier or inspect the named artifact. Score each criterion from 1 to 10 and list remaining deficits honestly.

Use this scale:

- 10: fully passes with strong evidence.
- 8-9: passes with minor non-blocking risk.
- 6-7: partially passes; one or more material gaps remain.
- 4-5: weak evidence or fragile behavior.
- 1-3: fails or cannot be verified.

### DECIDE

Stop only when every required criterion is at least 8 and all hard gates pass. Otherwise, select the weakest criterion, plan the next round, and continue until the max rounds, budget, or blocker is reached.

## State File

For multi-round or cross-session loops, create or update a state file such as:

```text
docs/agents/loop-state.md
```

Use a task-specific path when several loops may run in one repo:

```text
docs/agents/loops/<slug>.md
```

State file template:

```markdown
# Loop State: <goal>

## Quantified Target

- Verifier:
- Passing threshold:
- Max rounds:

## Current Scores

| Criterion | Score | Evidence | Deficit |
| --- | ---: | --- | --- |

## Round Log

| Round | Plan | Verification | Decision |
| ---: | --- | --- | --- |

## Blockers

- 

## Next Action

- 
```

Do not create state files for a single short loop unless persistence would reduce risk.

## Verification Routing

After the auto-loop gate passes, use the normal mode router to choose verification:

- Deterministic code: use TDD or regression tests at public seams.
- User-visible workflows: use BDD acceptance scenarios and browser or API checks.
- LLM, RAG, agents, classifiers, or semantic output: use EDD with datasets and evaluators.
- Framework/API-sensitive work: use source-driven development against official docs.
- Architecture or refactor work: quantify seam stability, behavior preservation, dependency reduction, public API constraints, and review criteria.
- Debugging: require a reproduction, root-cause hypothesis, fix, and regression check.

## Autonomy Levels

Default to the lowest autonomy level that satisfies the request:

- L0 ordinary task: no repeated loop; use the normal router.
- L1 bounded local loop: same thread, explicit max rounds, named verifier.
- L2 stateful loop: state file, ledger, resumable evidence, optional worktree.
- L3 autonomous orchestration: background work, subagents, hooks, or automations. Use only when the user explicitly asks for that operating model and the verifier is strong.

## Safety and Stop Rules

- Set a default max of 3 rounds unless the user gives another cap.
- Stop early when all hard gates pass and every required score is at least 8.
- Stop when the same blocker repeats twice or the verifier cannot run.
- Never loosen the threshold mid-loop to declare success.
- Do not count self-assessed prose as sufficient evidence when executable or external verification is available.
- For destructive, expensive, credentialed, or externally visible actions, ask for approval before the action even if the loop gate passed.

## Method Sources Integrated

This suite absorbs loop-engineering methods as patterns, not as a mandatory external runtime:

- Loop readiness audit and cost/budget gate from practical loop-engineering toolkits.
- File-backed state, task claiming, review feedback, and recoverable loops from PlanWeave-style systems.
- Plan/execute/summary memory discipline from LoongFlow-style research.
- Maker/checker separation and deterministic verdict gates from review-loop harnesses.
- Skill-eval caution from SWE-Skills-Bench: skills and loops must earn their token overhead with measurable improvement.
- Runtime diagnosis emphasis from SWE-Doctor and RAMP: judge the running loop by observable failures, recovery, tool use, and verification evidence.
