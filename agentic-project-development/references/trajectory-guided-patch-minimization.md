# Trajectory-Guided Patch Minimization

## Contents

- Purpose and boundary
- Eligibility gate
- Acceptance-preserving objective
- Required evidence
- Minimization workflow
- Search profiles and grouping
- Verification and maintainability gates
- Stop conditions
- Decision record

## Purpose and Boundary

Use this mode after a code-producing task has a reproducible passing baseline and
the agent's exploratory edits may have left speculative, superseded, temporary,
or otherwise unnecessary changes in the final patch.

Correctness precedes minimization. Treat this as a conditional post-success
overlay, not a replacement for specification, design, implementation, testing,
architecture review, or debugging. Search only within the existing task-owned
patch; do not synthesize a different solution while claiming to minimize it.

This mode targets removable functional redundancy introduced by the current
task. It does not automatically solve pre-existing dead code, duplicated domain
models, weak abstractions, dependency bloat, or general documentation
compression. Route those problems through architecture/domain design, review,
or a purpose-built static analysis workflow.

## Eligibility Gate

Run automatic minimization only when all conditions hold:

- the current patch already passes a reproducible acceptance baseline;
- a frozen acceptance verifier can distinguish acceptable from unacceptable
  candidates within a bounded cost;
- task-owned changes can be separated from user-authored or unrelated changes;
- each candidate can be applied and rolled back in an isolated, clean state;
- the edit trajectory or Git history is sufficient to reconstruct candidate
  groups and the final surviving edits;
- required artifacts and non-functional constraints are explicit enough to
  prevent silent deletion.

If any condition fails, set `minimization: skipped`, record the reason, and use a
normal diff review. Never weaken the verifier to make minimization eligible.

## Acceptance-Preserving Objective

Seek the smallest maintainable subset of task-owned changes that preserves the
approved outcome. Use this decision order:

1. Preserve every functional, safety, authorization, compatibility, migration,
   performance, reliability, and rollback hard gate.
2. Preserve required tests, documentation, examples, telemetry, schemas,
   configuration, and other named delivery artifacts.
3. Preserve or improve clarity, stable seams, domain vocabulary, locality, and
   future change cost.
4. Only then reduce changed lines, hunks, files, components, branches, wrappers,
   or dependencies introduced by the task.

Do not optimize raw line count. A shorter patch that hides intent, merges
distinct responsibilities, removes useful regression coverage, or creates a
clever but fragile implementation is not an improvement.

## Required Evidence

Freeze before the first deletion attempt:

```yaml
passing_baseline_ref: commit-or-artifact-hash
task_owned_change_ref: patch-or-manifest
protected_change_ref: user-and-unrelated-change-manifest
acceptance_verifier_ref: commands-evals-rubrics-and-versions
environment_ref: dependency-and-runtime-snapshot
profile: bounded | one-minimal
validation_budget: project-specific-limit
```

For coding-agent runtimes, preserve enough normalized edit evidence to rebuild
the reduced trajectory without creating a second telemetry source:

```yaml
edit_id: edit-017
edit_sequence_id: attempt-04
component: optional-domain-or-package
file: src/example.py
before_ref: artifact-or-content-hash
after_ref: artifact-or-content-hash
feedback_request_ref: verifier-run-04
survives_final_patch: true
```

Discard search, navigation, and other non-modifying actions for minimization.
Replay edits and reversions in temporal order, and retain only edits that still
contribute to the passing patch.

## Minimization Workflow

1. **Checkpoint**: preserve the passing patch, protected changes, verifier
   bundle, environment, and rollback path.
2. **Reconstruct**: derive the reduced trajectory of final surviving task-owned
   edits and map each edit to the acceptance evidence it may affect.
3. **Group**: construct coarse-to-fine candidates using edit sequence, optional
   component, file, and atomic edit or hunk boundaries.
4. **Traverse**: inspect candidates in reverse trajectory order so later
   superseding or temporary work is considered before earlier foundations.
5. **Counterfactually remove**: apply one candidate removal in an isolated copy
   of the passing state.
6. **Verify**: run the frozen acceptance verifier. Accept the removal only when
   all hard gates pass, required artifacts remain, the task-owned change surface
   strictly shrinks, and maintainability does not regress.
7. **Restore on rejection**: return exactly to the last accepted state before
   evaluating the next candidate.
8. **Refine**: move from coarse groups to finer groups only after the current
   level completes according to the selected profile.
9. **Re-verify**: run the complete final verifier, inspect the final diff, and
   compare it with the preserved baseline before completion.

Never evaluate deletion candidates directly in a dirty user worktree. Use a
temporary worktree, sandbox, reversible patch application, or equivalent
isolated mechanism.

## Search Profiles and Grouping

### Bounded profile

Use one reverse pass at each granularity. Prefer this TRIM-NG-inspired profile
for ordinary development, expensive verifiers, or larger patches. Stop when the
validation budget is reached and report the remaining untested candidates.

### One-minimal profile

Repeat each granularity until no remaining candidate can be removed by itself.
Use this TRIM-G-inspired profile for small patches, high review cost, or
high-assurance work when the verifier and budget justify repeated execution.
This provides one-minimality relative to the candidate units and verifier, not a
globally shortest or universally correct implementation.

### Candidate groups

- **Edit sequence**: changes made between two consecutive feedback requests.
- **Component**: an optional suite adaptation for a clear domain, package, or
  subsystem boundary; skip it when ownership or grouping is ambiguous.
- **File**: surviving task-owned edits pooled by file.
- **Atomic edit or hunk**: the smallest reliably replayable change unit.

Do not split below the smallest unit that can be replayed and rolled back
reliably. Dependencies between remaining units may prevent a globally minimal
result; never compensate by generating unrequested replacement code.

## Verification and Maintainability Gates

Build the frozen acceptance verifier from the task contract, not only from tests
the same agent happened to run. Include the applicable combination of:

- pre-existing regression tests and task-specific tests;
- build, typecheck, lint, schema, and packaging checks;
- BDD scenarios, browser journeys, or external state checks;
- LLM or agent eval suites with repeated trials and independent grading;
- API, storage, migration, compatibility, security, and authorization checks;
- performance, resource, observability, and rollback thresholds;
- explicit presence and quality checks for required tests, documentation,
  examples, configuration, and operational artifacts.

After functional minimization, review maintainability separately:

- every retained edit traces to the accepted outcome or a named guard;
- public seams and domain vocabulary remain coherent;
- the result does not introduce duplication, dead branches, speculative flags,
  shallow wrappers, or task-created orphans;
- tests remain readable and fail for the intended reason;
- simplicity comes from removing unnecessary behavior, not compressing syntax;
- future maintainers can explain why each non-obvious retained change exists.

Use a fresh verifier or human reviewer for subjective maintainability when risk
justifies it. The implementing agent's preference is not an acceptance oracle.

## Stop Conditions

Stop minimization and preserve the last passing state when:

- the baseline cannot be reproduced;
- ownership overlaps protected user or unrelated changes;
- the verifier is flaky, incomplete, non-repeatable, or mutates irreversible
  external state;
- a candidate affects behavior not represented in the acceptance contract;
- deletion requires new code, scope expansion, or architectural redesign;
- a smaller diff reduces clarity, test quality, stable seams, or required
  operational evidence;
- the validation budget or time limit is reached;
- rollback cannot be proven exact.

Do not treat a skipped or budget-limited minimization as failure when the
implementation otherwise passes. Report the reason and residual redundancy risk.

## Decision Record

```markdown
## Patch Minimization Decision

Passing baseline / protected changes:
Eligibility verdict and evidence:
Frozen acceptance verifier:
Profile / validation budget:
Candidate hierarchy:
Accepted removals / verification evidence:
Rejected or untested candidates:
Before -> after lines, hunks, files, and components:
Maintainability review:
Final full verification:
Intentional retained changes:
Residual risk:
```

This method adapts the trajectory-guided counterfactual search introduced by
[TRIM (arXiv:2607.18161v1)](https://arxiv.org/abs/2607.18161v1). The suite deliberately
strengthens the paper's test-preservation constraint into a full acceptance and
maintainability contract, protects non-agent changes and required artifacts, and
adds an optional component grouping. Treat those additions as engineering
adaptations rather than paper-validated claims.
