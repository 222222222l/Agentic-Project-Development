# Skill, Context, and Harness Governance

## Contents

- Purpose and evidence threshold
- Candidate and trust contracts
- Skill selection and composition
- Bounded context policy
- Behavior coverage
- Paired promotion gate
- Library maintenance
- Skill supply-chain gate
- Controlled evolution gate
- Decision record

## Purpose

Use this reference when adding, changing, consolidating, retrieving, or removing
agent Skills; changing persistent context files such as `AGENTS.md`; or changing
harness prompts, context selection, compaction, memory, or Skill composition.

Optimize for verified task success first, then reduce unnecessary instructions,
context, execution, and maintenance burden. Treat the model, harness, Skill set,
context policy, permissions, tools, budgets, and verifier as one evaluated
system. Do not infer utility from a plausible document, one successful run, or
the model's claim that it used a Skill.

## Evidence Threshold

Separate four evidence states:

| State | Meaning | Allowed use |
| --- | --- | --- |
| Proposed | rationale only; no task evidence | isolated experiment |
| Internally valid | syntax, links, smoke checks, and declared validator pass | opt-in candidate |
| Downstream proven | paired representative tasks show useful marginal effect | default for the tested scope |
| Transfer proven | held-out scope and claimed model-harness variants pass | shared or portable default |

Return `inconclusive` when the task set, trials, grader, or effect size cannot
support the claim. A narrow positive result does not justify a universal rule.
Keep research-derived numeric settings as experiment parameters unless the
project's own evaluation promotes them.

## Candidate Contract

Record only fields that change routing, execution, validation, or safety:

```yaml
candidate_id: skill-or-context-policy@version
kind: skill | context-file | context-policy | harness-policy
scope: tasks and environments where it is intended to help
applicability: observable conditions for loading or activation
incompatible_versions: []
source: repository, immutable revision, and content hash
inputs: []
expected_artifacts: []
validator: command or evaluator
known_failure_modes: []
permissions: [filesystem, shell, network, secrets, external-side-effects]
fast_path: minimal procedure
fallback: baseline behavior when inapplicable or failing
stop_conditions: []
evidence_state: proposed | internally-valid | downstream-proven | transfer-proven
```

Do not add fields that no decision or validator consumes. Prefer abstract
invariants and observable behavior over one framework version's full template.

## Skill Selection and Composition

1. Filter candidates deterministically by task, environment, version,
   permissions, and declared incompatibilities before semantic selection.
2. Start with the smallest applicable set. Treat one to three loaded Skills as
   an empirical working prior, not a universal hard cap.
3. Order selected content by execution dependency: governing contract, primary
   procedure, optional overlay, then verifier or fallback.
4. Record discovery, read, activation, and use separately. Loaded text is not
   evidence that the procedure affected the result.
5. Prefer the baseline when the model-harness already performs the task better,
   the Skill is version-mismatched, or the Skill forces a heavier pipeline than
   the task needs.
6. Keep task-generated refinements temporary. Promote them only through the
   normal paired and held-out evaluation path.

Do not load every available Skill for recall. Do not create nested routing
levels without project evidence that the additional selection step improves
outcomes after its context and coordination cost.

## Bounded Context Policy

Keep persistent context files limited to information that changes execution and
is not already authoritative elsewhere:

- exact repository commands and source-of-truth paths;
- architecture, ownership, safety, approval, and non-functional boundaries;
- environment-specific hazards and required verification;
- short routing pointers to canonical detail.

Reject generated repository overviews, duplicated documentation, stale file
inventories, generic coding advice, and facts cheaply recoverable from the
current repository. Link to the canonical source instead of copying it.

For long-horizon tool work, preserve four semantic layers:

```text
immutable task and acceptance contract
  + recent high-fidelity tool/state pairs
  + compact progress state for evicted history
  + stable references to complete evidence artifacts
```

Keep a tool call and its response together. A progress state must retain the
remaining objective, completed work, unresolved failures, key identifiers,
current authority, next action, and next verifier. Store full logs, test output,
code snippets, and external responses outside the prompt with stable references
when possible.

Use bounded context only after context pressure, stale-state failures, repeated
retrieval, or a project eval justifies it. Tune window and summary policy for the
tested model-harness pair; do not hard-code research benchmark window sizes as
suite-wide constants.

## Behavior Coverage

Extract only material Skill or context rules into observable constraints:

```text
When <applicability condition>, the agent shall <observable behavior>.
```

For each constraint, record its source span, applicability, required evidence,
and one result:

- `not-applicable`: the condition did not hold;
- `not-covered`: the trajectory did not exercise it;
- `pass`: required evidence is present;
- `fail`: the behavior was exercised but violated.

Report task success separately from behavior coverage. Use `fail` to target a
bounded instruction or implementation repair. Use `not-covered` to improve the
task suite before changing the Skill. Do not strengthen every instruction when
only one constraint failed.

## Paired Promotion Gate

Use `agent-evaluation-standard.md`. Freeze the baseline, candidate, tasks,
environment, budgets, graders, and trial count. Change one intended factor:

```text
current baseline or no-Skill
  versus
candidate Skill, context file, context policy, or harness policy
```

At minimum report:

- task success, paired wins/losses/ties, confidence, and every fatal failure;
- discovery, read, activation, behavior coverage, and fallback use;
- task and version slices, including cases where the candidate should abstain;
- tokens, tool calls, retries, latency, cost per success, and trace completeness;
- context precision, redundant retrieval, and explored-but-unused evidence when
  an evidence map makes those diagnostics reliable;
- all new regressions and whether the candidate displaced a stronger baseline.

Use at least the evaluation standard's repeated-run requirement for semantic or
agentic behavior. Test held-out tasks whenever the claim exceeds one task. Test
changed role, domain, model, or harness only when portability across that axis is
claimed. Never promote from the same trajectory used to author the candidate.

## Library Maintenance

Before creating a new Skill or reference:

1. Check exact name, normalized content hash, trigger and scope overlap,
   resource overlap, and routed capability coverage.
2. Establish the authoritative source and immutable revision.
3. Prefer extending a compact router with one direct progressive reference when
   the capability already belongs to the suite.
4. Classify overlap as duplicate, compatible overlay, alternative, dependency,
   or unresolved semantic conflict.
5. Propose `merge`, `repair`, `retire`, or `keep-separate` with evidence.

Do not automatically delete or retire from low use, apparent similarity, or an
LLM summary. Preserve rollback, source lineage, downstream validators, and user
approval for destructive library changes. Keep backups outside Skill discovery
roots so a backup cannot become another discoverable Skill.

## Skill Supply-Chain Gate

Treat third-party Skill instructions, scripts, resources, and dependencies as
untrusted by default.

- Pin source and version; verify the expected content hash.
- Inspect instructions, scripts, external dependencies, and referenced files.
- Compare requested capabilities with the current task and candidate contract.
- Deny undeclared filesystem, network, shell, secret, or external-side-effect
  access; use the least privilege and sandbox available.
- Keep authorization outside the Skill text. Require contextual approval for
  consequential or externally visible actions even when the Skill requests them.
- Run security/adversarial cases before increasing authority.

Static or model-based screening is supporting evidence, not authorization.
Reject a candidate whose provenance or effective capabilities cannot be
established.

## Controlled Evolution Gate

Automatic Skill or harness evolution is optional and must stay behind a stronger
gate than ordinary editing:

1. Freeze an immutable kernel: task contracts, acceptance verifiers, permission
   boundaries, evaluation splits, budgets, and rollback target.
2. Diagnose a specific failure surface and cause before proposing a candidate.
3. Require activation evidence that the changed path actually ran.
4. Select candidates on a development split using paired repeated trials and a
   predeclared minimum effect.
5. Confirm once on a sealed split that was not used to author or select the
   candidate.
6. Reject harmful, inactive, underpowered, or inconclusive candidates; preserve
   rejected evidence to prevent repeated rediscovery.
7. Require human approval before changing authority, safety policy, a shared
   Skill, or a destructive library decision.

Do not let an evolving agent edit its own verifier or silently broaden its
permissions. Do not equate benchmark gain with long-term maintainability.

## Decision Record

```markdown
## Skill / Context / Harness Decision

Candidate and evidence state:
Claimed scope and applicability:
Source, version, hash, and trust boundary:
Baseline system_harness_id -> candidate system_harness_id:
Paired tasks, trials, graders, and budgets:
Outcome, coverage, context, and cost deltas:
Regressions, incompatibilities, and security findings:
Held-out or transfer evidence:
Decision: promote | retain-opt-in | repair | reject | retire | inconclusive
Rollback and approver:
```
