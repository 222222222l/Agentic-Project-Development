# Data-Flywheel Agent Development

## Contents

- Purpose and non-negotiable gates
- Flywheel lifecycle
- Run, trace, feedback, and sample contracts
- Data layers and reuse rules
- Improvement routing
- Operating cadence
- Minimal deployment profiles
- KohakuTerrarium adapter

## Purpose

Use this mode when production use should continuously improve an agent through
structured evidence. Treat the flywheel as:

```text
observe -> link outcomes -> curate -> evaluate -> change -> validate -> deploy -> observe
```

The objective is not to collect the most data. It is to make each accepted
production signal reduce future error, cost, or risk while preserving evidence
of what changed and why.

Read `agent-evaluation-standard.md` with this file. Do not run an automated
improvement loop until its quantification and release gates are defined.

## Non-Negotiable Gates

Before collecting production data, define:

- one business outcome and one agent task outcome;
- a versioned event schema and stable correlation identifiers;
- what data may be retained, reused, exported, or deleted;
- the fatal safety, privacy, authorization, and side-effect gates;
- a protected evaluation set that cannot silently enter training or tuning;
- a baseline, candidate comparison method, release threshold, and rollback;
- a human owner for disputed labels and consequential promotion decisions.

Do not call a log archive a flywheel. A valid flywheel must prove all three:

1. Each selected run produces interpretable feedback or an observable outcome.
2. Feedback is converted into a named change through a reproducible process.
3. The candidate change beats the baseline without violating a hard gate.

Never send production data directly into self-training. Automate capture and
triage; keep curation, promotion, and high-risk actions governed.

## Flywheel Lifecycle

### 1. Frame

Write a `FlywheelContract` before implementation:

```yaml
objective: reduce_cost_per_successful_task
unit_of_work: one customer-support resolution
business_metric: resolved_cases_per_paid_hour
task_metric: verified_resolution_rate
fatal_gates: [privacy_breach, unauthorized_action, irreversible_wrong_action]
baseline_id: support-agent-v12
comparison_budget: {trials_per_case: 3, max_turns: 12, max_cost_usd: 0.50}
promotion_owner: support-ops-lead
rollback_target: support-agent-v12
```

If the business outcome arrives later than the agent run, define the join key,
observation window, and censoring rule before launch.

### 2. Instrument

Instrument the smallest complete causal path:

```text
request -> context/retrieval -> model decision -> tool or handoff -> artifact
        -> user or reviewer response -> downstream outcome -> evaluation
```

Use OpenTelemetry-compatible traces when practical. Preserve vendor-neutral
event and dataset exports so the evidence remains reusable if the runtime,
model provider, or observability backend changes.

Record references or hashes for large or sensitive payloads instead of copying
them into every event. Keep secrets out of traces. Redact or tokenize personal
data before it reaches reusable datasets.

### 3. Observe

Capture four signal classes and keep their provenance separate:

| Signal | Examples | Default trust |
| --- | --- | --- |
| Explicit feedback | score, rejection reason, expert correction | medium until calibrated |
| Behavioral feedback | accept, edit, undo, regenerate, escalate | weak-to-medium |
| Operational evidence | tool error, timeout, schema failure, approval denial | high for the event |
| Downstream outcome | task resolved, transaction completed, rollback, loss | highest when attributable |

Do not equate silence, completion, a thumbs-up, or lack of escalation with
correctness. Link weak signals to stronger downstream evidence when possible.

### 4. Triage

Rank samples by expected information value, not volume:

```text
sample_value = business_impact * uncertainty * novelty * reuse_probability
```

Use normalized factors in `[0, 1]`; record the factors and policy version.
Always surface fatal incidents regardless of score. Cluster the remainder by
failure signature, task slice, tool, model/harness version, and outcome.

Attribute each failure before proposing a fix:

- **local**: one call, schema, prompt branch, or tool action failed;
- **upstream**: valid downstream behavior received bad context or data;
- **structural**: topology, authority, state model, task contract, or evaluator is wrong;
- **external**: provider, dependency, user state, or environment failed outside the change boundary;
- **unknown**: evidence is insufficient; collect more rather than guessing.

### 5. Curate

Promote a raw run into a reusable sample only after:

- schema validation and trace-link validation pass;
- permission and retention class are known;
- sensitive fields are redacted or access-controlled;
- duplicate and near-duplicate checks run;
- the outcome, label source, label confidence, and adjudication state are stored;
- dataset split assignment is deterministic and leakage-safe;
- the sample carries its source trace and configuration lineage.

Use machine labeling for routing and candidate labels. Require domain review for
fatal, disputed, high-impact, and gold-evaluation samples. Track inter-reviewer
agreement instead of hiding disagreement in a majority label.

### 6. Diagnose and route the change

Choose the lowest-cost reversible intervention that addresses the attributed
cause:

1. repair data, knowledge, or freshness;
2. repair deterministic parsing, routing, validation, or authorization;
3. improve tool description, prompt, context selection, or output schema;
4. change workflow, memory, handoff, retry, or approval policy;
5. change model or model-harness profile;
6. fine-tune or preference-optimize on approved, sufficiently large data;
7. redesign the task or product when the target is not reliably solvable.

Do not use fine-tuning to mask a broken tool, stale knowledge source, unclear
business rule, or invalid evaluator.

### 7. Evaluate

Freeze the baseline and candidate configurations. Run the same task set,
environment, tools, budgets, and graders unless the experiment explicitly tests
one of them. Preserve complete trial traces and report distributional results,
not only averages.

Use `agent-evaluation-standard.md` for the release decision. A fatal failure
cannot be offset by a higher composite score.

### 8. Release

Promote through bounded exposure:

```text
offline gates -> shadow replay -> canary -> controlled A/B -> full release
```

For low-traffic systems, use paired replay plus manual review instead of
pretending an underpowered A/B test is significant. Record the release decision,
evidence, approver, exposure, stop conditions, and rollback target.

### 9. Harvest

After release:

- monitor quality, safety, cost, latency, drift, and business outcomes;
- sample high-value successes as well as failures to prevent negative-only bias;
- turn confirmed novel failures into regression cases;
- turn solved but difficult cases into capability or stress cases;
- recalibrate model graders against humans;
- retire stale tasks and keep a reasoned history rather than deleting evidence.

## Structured Run Contract

Every event uses an immutable envelope. Store large bodies as artifacts and
refer to them by URI plus content hash.

```json
{
  "schema_version": "agent.event.v1",
  "event_id": "evt_01...",
  "event_type": "tool.completed",
  "occurred_at": "2026-07-12T08:15:30.123Z",
  "run_id": "run_01...",
  "trace_id": "tr_01...",
  "span_id": "sp_01...",
  "parent_span_id": "sp_parent...",
  "task_id": "task_support_refund",
  "session_id": "session_01...",
  "actor": {"type": "agent", "id": "refund-worker", "version": "3"},
  "configuration": {
    "system_id": "support-agent-v13",
    "model": "provider/model-version",
    "prompt_hash": "sha256:...",
    "toolset_hash": "sha256:...",
    "policy_hash": "sha256:...",
    "harness_hash": "sha256:..."
  },
  "input_refs": [{"uri": "artifact://...", "sha256": "..."}],
  "output_refs": [{"uri": "artifact://...", "sha256": "..."}],
  "status": "succeeded",
  "error": null,
  "metrics": {"latency_ms": 842, "input_tokens": 310, "output_tokens": 86, "cost_usd": 0.014},
  "data_policy": {"classification": "internal", "reuse": "eval_only", "retention_days": 90},
  "attributes": {"tool_name": "issue_refund", "attempt": 1}
}
```

Required event types:

- `run.started`, `run.completed`, `run.failed`, `run.abstained`;
- `model.started`, `model.completed`, `model.failed`;
- `tool.started`, `tool.completed`, `tool.failed`;
- `handoff.started`, `handoff.completed`, `handoff.failed`;
- `state.changed`, `approval.requested`, `approval.decided`;
- `artifact.created`, `feedback.recorded`, `outcome.recorded`;
- `evaluation.completed`, `deployment.promoted`, `deployment.rolled_back`.

For asynchronous work, propagate `run_id`, `trace_id`, and causal parent links.
Do not infer parentage from timestamp order.

## Feedback Contract

```json
{
  "schema_version": "agent.feedback.v1",
  "feedback_id": "fb_01...",
  "trace_id": "tr_01...",
  "run_id": "run_01...",
  "target": {"type": "span", "id": "sp_01..."},
  "source": {"type": "downstream_system", "id": "ticketing"},
  "signal": "case_reopened_within_72h",
  "value": true,
  "observed_at": "2026-07-15T09:00:00Z",
  "label": "resolution_failed",
  "label_confidence": 0.98,
  "adjudication": "automatic_rule_v4",
  "comment_ref": null,
  "data_policy": {"reuse": "eval_and_analysis", "retention_days": 365}
}
```

Keep raw signal, interpreted label, confidence, and adjudication method separate
so labels can be corrected without rewriting history.

## Reusable Sample Contract

```yaml
schema_version: agent.sample.v1
sample_id: sample_01...
source_trace_ids: [tr_01...]
task_type: support_refund
slice_tags: [frustrated_user, policy_boundary]
input_ref: artifact://sanitized/input/...
environment_ref: env://support-sandbox-v5
expected_outcome:
  state: resolved
  forbidden: [unauthorized_refund]
graders: [state_check_v3, policy_gate_v2, interaction_rubric_v4]
label_provenance: expert_adjudicated
label_confidence: 1.0
split: regression
rights: eval_only
created_from_incident: incident_01...
```

## Data Layers and Reuse Rules

Keep one-way promotion with lineage:

| Layer | Purpose | Mutable? | Training allowed? |
| --- | --- | --- | --- |
| Raw event log | audit and reconstruction | append-only | no |
| Normalized traces | query and replay | derived/versioned | no by default |
| Curated samples | reviewed reusable cases | new versions only | policy-dependent |
| Gold evaluation | stable release decision | tightly controlled | never |
| Regression set | previously supported behavior | append/versioned | never |
| Capability set | unsolved or partial tasks | append/versioned | never |
| Training/preference set | approved optimization data | versioned | yes, when licensed |
| Experiment results | baseline/candidate evidence | append-only | no |

Use content hashes and dataset manifests. Never edit a released dataset version
in place. Maintain sample lineage when a case is transformed, redacted,
re-labeled, split, or retired.

## Agent Behavior Contract

Require every agent or workflow node to:

- accept a schema-bound task packet and emit a schema-bound result;
- declare tools, permissions, budgets, retry limit, and abstention conditions;
- emit start, completion, failure, and approval events with correlation IDs;
- separate observed facts, inferred claims, decisions, and side effects;
- cite artifact or trace references for material claims;
- preserve errors and recoveries instead of reporting only the final success;
- retry locally and idempotently; re-plan on structural failure;
- stop on missing authority, missing evidence, or a fatal gate;
- return compact status to the control plane and keep raw data in artifacts;
- never grade or train on its own output without an independent check.

## Operating Cadence

### Per change

1. Name the target metric and failure cluster.
2. Freeze baseline, candidate, dataset, harness, budget, and graders.
3. Run offline evaluation and inspect representative traces.
4. Record deltas, regressions, costs, and gate decisions.
5. Promote through the smallest safe exposure or reject the candidate.

### Weekly

- review the highest-value new failures and disputed labels;
- convert confirmed failures into regression samples;
- inspect trace completeness, label yield, cost per success, and drift;
- recalibrate at least a sample of model-graded cases with a human;
- choose one bounded improvement slice instead of changing several variables.

### Monthly or per release train

- audit dataset leakage, permissions, retention, and evaluator drift;
- review saturated or stale evals and add capability cases;
- compare flywheel benefits with storage, review, inference, and incident costs;
- verify rollback and reproducibility from manifests and hashes.

## Minimal Deployment Profiles

### Personal developer

- append JSONL or SQLite events locally;
- store artifacts by content hash;
- keep configs, dataset manifests, and eval cases in Git;
- start with 20-50 real or manually tested cases and three trials per case;
- run a weekly failure review and a pre-release regression gate;
- use scripts for exact graders and human review for disputed semantic quality.

### Small or medium business

- emit OpenTelemetry-compatible traces to a central collector;
- store immutable raw events separately from normalized analytics tables;
- use role-based access, redaction, retention, and audit logs;
- maintain named owners for instrumentation, domain labels, evals, and release;
- sample production traces by risk and novelty rather than evaluating all traffic;
- use batch evaluation before release and controlled canary or A/B evidence after;
- publish a version scorecard covering quality, safety, cost, latency, and ROI.

Start with the personal profile. Add platform components only when volume,
compliance, collaboration, or recovery needs justify them.

## KohakuTerrarium Adapter

Keep the `.kohakutr` append-only event log as the canonical raw history. Add a
lifecycle plugin or export adapter for normalized flywheel events because
instrumentation and policy are cross-cutting concerns; do not put data-flywheel
policy into the terrarium wiring engine.

- map session, event, job, tool, sub-agent, channel, and artifact identifiers to
  the run and trace contract without creating a second source of truth;
- keep vertical sub-agent spans and horizontal creature/channel spans distinct;
- propagate correlation IDs through tool jobs, sub-agent dispatch, output wiring,
  and channel messages;
- send only compact status and artifact references to a privileged root;
- keep full trace payloads in session artifacts or an external telemetry sink;
- implement deterministic schema validation, export, curation, and scoring in
  tools or scripts rather than an LLM controller;
- retain the framework rule that the terrarium has no LLM or policy decisions.

Before changing runtime code, first prove that a plugin plus session export
cannot satisfy the instrumentation contract.
