# Skill, Context, and Harness Governance

## Contents

- Purpose and evidence threshold
- Candidate and trust contracts
- Skill selection and composition
- Bounded context policy
- Behavior coverage
- Subtask reuse and attributable verification
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

User-authorized editing or installation is not a claim of default performance
superiority. Complete the requested revision and report its evidence state;
do not block ordinary maintenance behind a production promotion experiment.
Never label static validation or a behavioral smoke pass as downstream proof.

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
2. Start with the smallest applicable set. Add a Skill only for an uncovered
   capability or constraint; count its marginal coverage and context cost, not
   just semantic similarity. One to three Skills is a historical benchmark
   prior, not a target count or cap.
3. Order selected content by execution dependency: governing contract, primary
   procedure, optional overlay, then verifier or fallback.
4. Record discovery, read, activation, and use separately. Loaded text is not
   evidence that the procedure affected the result.
5. Prefer the baseline when the model-harness already performs the task better,
   the Skill is version-mismatched, or the Skill forces a heavier pipeline than
   the task needs.
6. Keep task-generated refinements temporary. Promote them only through the
   normal paired and held-out evaluation path.

## Subtask Reuse

Distill reusable experience at a coherent subtask boundary: applicability,
inputs, procedure, observable verifier, failure modes, and source evidence.
Exclude source-task answers, transient identifiers and one-off workarounds.
Prefer concise procedural text for flexible transfer; keep tested deterministic
scripts for exact, repeated operations. A complete transcript is an evidence
artifact, not a reusable procedure. Validate retrieval against negative cases
and new tasks; similarity, reuse counts or a utility score do not prove benefit.

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

Use host-native compaction and compact progress state when long work needs it.
Changing the host's history policy requires runtime support and project evidence.
Validate state patches before persistence; preserve prior keys unless deletion
is intentional. Separate proposed actions from observed outcomes and reconcile
external state on resume. Never replace an audit trail with a summary. A fixed
schema may omit facts whose relevance becomes apparent later; retain full
artifact references and a retrieval fallback. See `efficient-execution.md`.

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

For a material new instruction, include a rule-withheld control. When the
baseline already behaves that way, successful compliance does not demonstrate
the rule's marginal value. Include against-prior cases and mid-task user
corrections; record the instruction surface and actual host hierarchy.

## Attributable Development Verification

For an expensive candidate search, use this staged development procedure:

1. Name the failure hypothesis, intended behavioral change and editable component.
2. Check syntax, loading and activation before spending on agent rollouts.
3. Select development cases that exercise the behavior plus plausible regression
   cases. Match baseline/candidate budgets and conditions on every selected case.
4. Inspect behavior evidence as well as outcomes. Use a cheap discriminating
   probe when multiple explanations fit; an author-written probe is diagnostic.
5. Confirm promising edits on previously unused development cases, broadening
   coverage when the changed component has broad effects.
6. Evaluate the selected final candidate once on the untouched holdout before
   a general improvement claim. Reserve that budget before candidate search.

Adaptive development selection is allowed and must be logged. Do not report its
selected subset as an unbiased population score. Predetermine confirmation and
stopping rules; repeated inspection of the holdout turns it into development
data. Retain a baseline and alternative hypotheses; do not automatically install
a search tree or continue editing when there is no attributable improvement.

## Paired Promotion Gate

Use `agent-evaluation-standard.md`. Freeze the baseline, candidate, tasks,
environment, budgets, graders, and trial count. Change one intended factor:

```text
current baseline or no-Skill
  versus
candidate Skill, context file, context policy, or harness policy
```

At minimum report:

- task success, paired wins/losses/ties, task-clustered confidence, and every fatal failure;
- discovery, read, activation, behavior coverage, and fallback use;
- task and version slices, including cases where the candidate should abstain;
- tokens (cached and uncached), tool calls, retries, latency, cost per success,
  failed-run cost, optimizer/evaluation overhead, and trace completeness;
- context precision, redundant retrieval, and explored-but-unused evidence when
  an evidence map makes those diagnostics reliable;
- all new regressions and whether the candidate displaced a stronger baseline.

Choose repeated trials using the evaluation standard and the project's stated
effect size and uncertainty needs. Test held-out tasks whenever the claim exceeds one task. Test
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
- Keep authorization outside the Skill text. Honor authorization already given
  for the same scope; obtain missing approval at a consequential action boundary.
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
7. Obtain missing authorization before increasing authority, changing shared
   policy, or making a destructive library decision. An explicit request to
   update this Skill already authorizes the scoped revision; do not ask again.

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
