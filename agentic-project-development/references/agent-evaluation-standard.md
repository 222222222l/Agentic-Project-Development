# Agent Evaluation Standard

## Contents

- Evaluation object and evidence packet
- Dataset and grader requirements
- Metric definitions
- Skill and context policy experiments
- Default release gates
- Experiment and online validation rules
- Adaptive development and task-clustered comparisons
- Flywheel health scorecard
- Decision record

## Evaluation Object

Evaluate the complete tested system, not the model name. Freeze and report:

- agent/workflow version and topology;
- model provider, exact model version, parameters, and reasoning profile;
- prompts, skills, tool schemas, policies, and configuration hashes;
- context construction, retrieval sources, memory, and compaction policy;
- permissions, sandbox, approvals, retries, timeouts, and stop conditions;
- task dataset and split version;
- environment and dependency versions;
- graders, rubric versions, judge models, and calibration evidence;
- allowed turns, tokens, attempts, wall time, and cost;
- seeds when available and the number of independent trials.

Call this the `system_harness_id`. Any material change creates a new ID.

## Evidence Packet

Every evaluation run must produce:

```yaml
evaluation_run_id: eval_01...
system_harness_id: sha256:...
baseline_system_harness_id: sha256:...
dataset_id: support-regression@17
grader_bundle_id: support-graders@9
environment_id: support-sandbox@5
trials_per_case: 3
budgets: {max_turns: 12, max_tokens: 30000, max_cost_usd: 0.50}
started_at: 2026-07-12T08:00:00Z
metrics: {}
hard_gates: {}
slice_results: {}
trace_manifest_ref: artifact://eval/eval_01/traces.jsonl
failures_ref: artifact://eval/eval_01/failures.parquet
decision: pass | fail | inconclusive
decision_reason: ""
approver: ""
```

Store per-case and per-trial results. Aggregate-only reports are insufficient.

## Dataset Standard

Size the suite and thresholds to the claim, risk, task diversity and detectable
effect *before* candidate selection. Numeric defaults below are examples for an
operational agent release, not prerequisites for ordinary coding or Skill edits,
and not values established by the research. Repeated runs reduce trial noise;
they do not replace independent tasks or justify a significance claim alone.

Maintain separate, versioned suites:

| Suite | Purpose | Target pass rate | May train on it? |
| --- | --- | ---: | --- |
| Smoke | basic runnable contract | 100% | no |
| Regression | behavior already supported | at least 99% and no fatal failure | no |
| Capability | behavior being improved | intentionally below saturation | no |
| Safety/adversarial | forbidden or high-risk behavior | 100% hard-gate pass | no |
| Production shadow | sampled current distribution | monitored, not fixed | no by default |
| Human preference | subjective comparison | report preference and ties | only if separately approved |

Dataset requirements:

- start with 20-50 high-value cases for a new agent;
- represent common, edge, high-risk, long-horizon, recovery, and abstention tasks;
- include positive and negative routing cases for every optional tool or action;
- stratify by business impact, user/scenario group, task length, and failure class;
- assign splits by stable entity or scenario key, not random rows, to prevent near-duplicate leakage;
- store task instructions, initial environment, expected outcomes, forbidden outcomes, graders, and source lineage;
- quarantine suspected contamination and report its effect;
- never rewrite a released case silently; publish a new dataset version;
- inspect saturation and retire or graduate cases with a recorded reason.

Before release, verify that two competent reviewers could independently apply
the success criteria. If not, repair the task or mark the result inconclusive.

## Grader Standard

Prefer graders in this order:

1. external outcome or environment state;
2. deterministic code, schema, policy, security, or business-rule checks;
3. reference comparison or bounded statistical checks;
4. model grader with a single-dimension rubric;
5. human expert review.

Use multiple graders when success is multidimensional. Grade outcomes by
default; grade exact paths only when the path itself is a requirement such as
authorization, required evidence, or forbidden tool use.

For model graders:

- keep one rubric dimension per score where practical;
- include `pass`, `fail`, and `unknown/insufficient_evidence` outcomes;
- hide candidate identity and randomize ordering for pairwise comparisons;
- require a rationale linked to trace evidence;
- calibrate against a held-out human-reviewed set before release;
- re-calibrate after judge-model or rubric changes and at a fixed cadence;
- treat grader disagreement as evidence, not noise to discard.

Default calibration gate:

- at least 50 double-reviewed items when feasible, 20 for a cold start;
- Cohen's kappa at least `0.70` for categorical labels, or Spearman correlation
  at least `0.80` for ordinal scores;
- no more than `5%` false-pass rate on fatal or high-risk cases;
- otherwise use the grader for triage only, not release decisions.

## Core Metrics

Report counts and confidence intervals with rates. Always provide slice-level
results for high-risk and materially different groups.

### Outcome quality

```text
task_success_rate = successful_trials / eligible_trials
task_macro_success = mean(per_task_successful_trials / per_task_trials)
empirical_first_attempt_success = successful_first_trials / tasks
pass^k = tasks_where_all_k_trials_pass / tasks
fatal_failure_rate = fatal_trials / eligible_trials
abstention_precision = correct_abstentions / all_abstentions
abstention_recall = correct_abstentions / cases_requiring_abstention
```

Use `pass@k` only where several attempts are an allowed product behavior. Use
`pass^k` when repeated reliability matters.

Declare whether pass@1 estimates the expected single-attempt success from all
independent trials or uses just the first recorded attempt. Report task-macro
and trial-micro aggregation explicitly when repetitions differ. Empty
denominators are undefined, never zero or a passing score.

### Trajectory quality

```text
tool_selection_precision = valid_required_or_useful_calls / all_tool_calls
tool_call_success_rate = successful_tool_calls / attempted_tool_calls
handoff_success_rate = accepted_valid_handoffs / attempted_handoffs
recovery_rate = recovered_eligible_failures / eligible_recoverable_failures
unsupported_claim_rate = unsupported_material_claims / material_claims
verification_coverage = verified_material_claims / material_claims_requiring_verification
skill_applicability_precision = applicable_loaded_skills / loaded_skills
skill_behavior_coverage = evidenced_applicable_constraints / applicable_constraints
context_use_rate = retrieved_units_used_in_final_decision / retrieved_units
retrieval_redundancy = redundant_retrieved_units / retrieved_units
```

Also report turns, tool calls, retries, tokens, latency, and state transitions per
successful task and for the complete attempted population. Report idle/no-action
turns, duplicate retrieval and redundant full-suite runs when traces support
those labels. Report Skill discovery, read, activation, and fallback use as
separate events. Use context-use metrics only when a reviewed evidence map makes
their denominators reliable. Do not reward shorter paths that omit required
verification.

### Observability and reproducibility

```text
trace_completeness = required_present_events / required_expected_events
lineage_completeness = samples_with_full_lineage / curated_samples
replay_success_rate = reproducible_replays / attempted_replays
schema_validity_rate = valid_structured_outputs / structured_outputs
```

### Economics

```text
cost_per_success =
  (all_attempt_model_cost + all_attempt_tool_cost + human_review_cost
   + attributed_error_loss)
  / successful_tasks

value_per_success = verified_business_value / successful_tasks
agent_roi = (verified_business_value - total_operating_cost) / total_operating_cost
```

Report P50 and P95 cost and latency. Means alone hide long tails.

Use a consistent denominator: successful trials for trial-level total cost,
successful tasks for total task budgets that include allowed retries. Report
input, output, cached-input tokens and cache-adjusted billed cost separately.
Charge optimizer, retrieval-worker, evaluation, retry and integration overhead
to the method that used them. Report successful-run-only costs as conditional
diagnostics, not cost per success; omitting failed runs can reverse a ranking.
With no successes, cost per success is undefined/infinite, not zero.

### Data-flywheel health

```text
feedback_link_rate = feedback_joined_to_trace / feedback_received
usable_sample_yield = curated_reusable_samples / captured_runs
failure_to_eval_rate = confirmed_novel_failures_added_to_evals / confirmed_novel_failures
reuse_rate = samples_used_in_two_or_more_decisions / curated_samples
cycle_time = median(deployment_time - signal_observed_time)
promotion_hit_rate = promoted_candidates_improving_online_target / promoted_candidates
```

## Default Hard Gates

These are illustrative operational defaults, not universal research thresholds.
Choose the applicable project gates in advance. Do not loosen a gate during an
active experiment merely to pass the candidate. Static validation and bounded
smoke checks may finish an authorized edit without establishing efficacy.

### All profiles

- `fatal_failure_count = 0` in every release-blocking suite;
- privacy, secret exposure, unauthorized side effect, and irreversible wrong
  action counts are all `0`;
- eval/train contamination has `0` known unapproved cases;
- schema validity is `100%` for required machine-consumed outputs;
- configuration, dataset, grader, and trace manifests are present for `100%` of trials;
- every candidate regression is listed; no average may hide it;
- rollback target and stop conditions are tested before production promotion.

### Standard operational profile

- regression suite pass rate at least `99%`;
- no high-impact slice declines by more than `2` percentage points;
- trace completeness at least `99.5%` in production and `100%` in eval runs;
- tool-call success at least `99%` excluding declared external outages;
- unsupported material claim rate no greater than baseline and below `1%` for grounded tasks;
- candidate task success improves by at least `3` percentage points absolute or
  `10%` relative on the target slice, unless the change is a pure cost/risk improvement;
- cost per success and P95 latency do not worsen by more than `10%` unless the
  approved objective explicitly buys quality or safety with that budget;
- grader calibration meets the standard above;
- at least three independent trials per case for semantic or agentic behavior.

### High-stakes profile

- use at least five independent trials per critical case;
- require `100%` pass on safety, authorization, and irreversible-action suites;
- enforce the active authorization policy at production promotion and consequential
  actions; reuse approval already granted for the same scope;
- use a lower-confidence-bound decision: the candidate's 95% confidence lower
  bound must meet the minimum target, not only the point estimate;
- require `pass^5` on critical deterministic-outcome cases to meet the project target;
- require shadow or canary evidence before any increase in action authority;
- any unexplained trace gap, grader drift, or disputed fatal label blocks release.

For small datasets where confidence intervals are too wide, return
`inconclusive`. Add evidence or obtain explicit human risk acceptance; do not
convert weak evidence into a pass.

## Baseline-Candidate Comparison

Use paired tasks and equal budgets. Randomize execution order when shared
infrastructure or time effects may matter. Report:

- baseline and candidate counts, rates, confidence intervals, and absolute delta;
- paired wins, losses, and ties;
- per-slice deltas and all new fatal or regression failures;
- cost, latency, turns, tools, retries, and human-review deltas;
- which single variable was intended to change;
- any environment, provider, or dataset drift during the run.

For binary outcomes, use a paired method such as McNemar's test when sample size
supports it and each task contributes one independent outcome. For repeated
trials, preserve baseline/candidate pairs and cluster resampling by task or
scenario; do not treat correlated repetitions as independent tasks. Report
intervals and the number of unique tasks, not only a p-value. For online rates,
report confidence intervals and predeclared
minimum effect. For subjective results, use blinded pairwise human preference
with ties and inter-reviewer agreement.

Do not claim improvement when:

- the candidate changed several uncontrolled variables;
- the reported final test set was chosen after seeing candidate outputs;
- retries or budgets differ without being part of the claim;
- a model grader is uncalibrated or saw variant identity;
- a score increase comes from evaluation leakage or reward hacking;
- the business outcome is unchanged and no approved proxy relationship exists.

## Adaptive Development and Final Confirmation

Behavior-based task selection can reduce *development* evaluation cost. Log
selection rationale, the affected behavior, regression sentinels, budgets and
all tried candidates. Confirm promising changes on unused development cases;
reserve an inaccessible holdout for the final nominated candidate. That holdout
must not guide task grouping, prompt authoring or selection.

Predeclare the minimum effect, uncertainty method, stopping rule and primary
metric. For cost improvements, require quality non-inferiority against a stated
margin with enough evidence; an insignificant quality difference is not proof
of equality. Small or saturated task sets may remain inconclusive even after
many repeated trials. Control repeated looks/multiple comparisons or label
exploratory results accordingly. Do not select a best run and call it pass@1.

Separate three reports: diagnostic behavior changes, final task performance,
and resource cost. An activated rule can be followed without improving success;
use rule-withheld controls for material instruction additions. See
`skill-context-harness-governance.md` for the staged verification procedure.

## Skill and Context Policy Experiments

Read `skill-context-harness-governance.md` when the intended variable is a
Skill, persistent context file, retrieval/composition policy, compaction policy,
or harness instruction. Compare the current or no-Skill baseline with the
candidate under equal tasks, budgets, tools, permissions, environment, and
graders. Only the intended Skill or context factor may differ between the two
`system_harness_id` manifests.

In addition to the baseline-candidate report:

- record whether each candidate was discovered, read, activated, used, skipped,
  or replaced by fallback behavior;
- report behavior coverage separately from task success;
- include negative applicability, version-mismatch, and baseline-stronger cases;
- report context precision, redundancy, explored-but-unused evidence, and stale
  state failures only when those labels are reliable;
- test held-out tasks whenever utility beyond one task is claimed;
- test changed role, domain, model, or harness only when transfer across that
  axis is claimed;
- never promote a task-generated candidate from the same trajectory that
  authored it.

Treat one to three loaded Skills as an initial experimental prior, not a release
gate. Do not encode a universal context window or summary interval from one
benchmark. If the sample cannot distinguish a real gain from noise, return
`inconclusive` and retain the baseline.

## Online Validation

Promote in stages and predeclare stop rules.

| Stage | Evidence | Default stop condition |
| --- | --- | --- |
| Shadow replay | same inputs, no user-visible action | any fatal failure or material regression |
| Canary | small bounded traffic and authority | safety gate, SLO, or target metric breach |
| A/B test | randomized eligible traffic | harm threshold, invalid randomization, or insufficient data window |
| Full release | monitored production | drift, incident, or rollback threshold |

Link every online outcome to the originating trace and variant. Exclude ineligible
or censored outcomes by a predeclared rule. Keep exposure assignment immutable.

For low traffic, prefer paired replay of representative traces plus expert review
and a longer canary. Do not use statistical language that the sample cannot support.

## Flywheel Scorecard

Keep hard gates separate. A suggested non-gating health score is:

```text
flywheel_health =
  0.20 * trace_completeness
  + 0.15 * feedback_link_rate
  + 0.15 * lineage_completeness
  + 0.15 * failure_to_eval_rate
  + 0.10 * grader_calibration_score
  + 0.10 * replay_success_rate
  + 0.15 * normalized_cycle_time_score
```

Use it to locate weak infrastructure, never to approve a release. Report the
underlying metrics beside the score.

Default maturity bands:

- **L0 ad hoc**: outputs exist, but traces or success criteria are missing;
- **L1 observable**: structured traces and versioned configurations exist;
- **L2 evaluable**: curated datasets, calibrated graders, and baselines exist;
- **L3 releasable**: offline gates, canary/A-B evidence, rollback, and ownership exist;
- **L4 compounding**: production failures reliably become reusable evals and
  measurable improvements with declining cycle time and stable safety.

Do not claim L4 until at least three completed observe-to-release cycles have
preserved lineage and improved an online or verified business outcome.

## Release Decision Record

```markdown
## Agent Release Decision

Claim being tested:
System/harness baseline -> candidate:
Dataset / graders / environment:
Budgets and trials:
Hard gates:
Target metric delta and confidence:
Regressions and slice effects:
Cost / latency / ROI effect:
Trace and lineage evidence:
Validity risks: contamination, reward hacking, broken tasks, grader drift:
Online validation plan or result:
Decision: pass | fail | inconclusive
Approver and rollback target:
```

Preserve this record with the experiment and deployment manifests.
