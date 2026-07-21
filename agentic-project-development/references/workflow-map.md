# Workflow Map

## Contents

- Lifecycle
- Grounded phase contract
- Mode selection
- Project execution routing
- Current skill composition
- Patch minimization
- Artifact traceability
- Decision templates

## Purpose

Use this file when several development modes apply, when artifact ordering is unclear, or when work spans more than one independently verifiable slice.

## Lifecycle

1. **Profile**: choose `frontier-compact` or `portable-guided` from the model-harness pair.
2. **Loop gate**: for loop/auto requests, prove reliable quantified verification before repetition.
3. **Route execution**: map task structure and choose main owner, capability role, worker reuse, independent verification, and fallback.
4. **Expose unknowns**: scan architecture, history, data, constraints, risks, and references.
5. **Align**: define outcome, users, non-goals, approvals, and done criteria.
6. **Ground**: attach each material claim to repo files, runtime state, current sources, examples, or prior artifacts.
7. **Specify**: create a durable source of truth when ambiguity or scope warrants it.
8. **Model behavior**: express user-visible rules as scenarios or acceptance criteria.
9. **Plan slices**: create vertical increments with explicit phase contracts.
10. **Implement**: use TDD, direct implementation, source grounding, or prototypes according to risk.
11. **Reassess**: re-route after direction-changing evidence, repeated verifier failure, or excessive coordination cost.
12. **Evaluate**: run exact checks, gates, evals, browser/manual QA, and review.
13. **Recover**: attribute failures as local, upstream, or structural before targeted repair.
14. **Minimize**: when eligible, reduce the passing patch to the smallest task-owned change that preserves the full acceptance contract and maintainability gates.
15. **Converge**: check spec -> plan -> task -> implementation -> verification coverage and append only genuine remaining work.
16. **Explain and record**: report why, what changed, evidence, routes, fallbacks, risks, intentional non-changes, and reusable learning.

## Grounded Phase Contract

Use this for each substantial phase. `portable-guided` requires every field; `frontier-compact` may keep it terse.

```markdown
Phase / outcome:
Inputs and repository evidence:
Action boundary:
Expected artifact:
Verifier and threshold:
Stop, abstain, or escalate when:
```

Validate intermediate artifacts before they become downstream context. A clean final test does not prove that the spec, plan, tasks, and implementation stayed aligned.

## Mode Selection Matrix

| Situation | Primary mode | Overlay |
| --- | --- | --- |
| New feature with fuzzy requirements | SDD | BDD if user-facing |
| Existing discussion ready to package | Delivery | Architecture if cross-module |
| Deterministic logic or bug fix | TDD | Source grounding if framework-specific |
| UI workflow, permissions, checkout, onboarding | BDD | TDD or browser journey |
| LLM, agent, RAG, prompt, extractor, classifier | EDD | Agent-system engineering |
| Tool graph, handoff, memory, durable or multi-agent runtime | Agent-system engineering | EDD, architecture |
| Project model route, specialist worker, or independent verifier | Project model routing | Agent-system engineering, review |
| Production traces, feedback curation, reusable failures, or continuous improvement | Data-flywheel development | Agent evaluation standard, EDD, agent-system engineering |
| New framework/API integration | Source-grounded | TDD, BDD, or EDD |
| Codebase feels hard to change | Architecture/domain | Review after tracer bullet |
| PR/diff quality check | Review | BDD/TDD/EDD gap analysis |
| Passing agent patch contains exploratory residue or needs simplification | Trajectory-guided patch minimization | Review, acceptance, architecture |
| Vague or high-risk task | Uncertainty and decision trace | SDD, BDD, architecture |
| Loop/auto/run-until-done | Auto-loop gate | Normal router after quantification |

## Current Skill Composition

- `clarify-project-requirements`, `grilling`, and `grill-with-docs`: outcome alignment and high-leverage questioning.
- `domain-modeling`, `codebase-design`, and `improve-codebase-architecture`: vocabulary, deep modules, stable seams, and architecture candidates.
- `to-prd` and `to-issues`: durable intent and vertical delivery slices.
- `tdd`, `diagnosing-bugs`, and `code-review`: deterministic implementation, root-cause diagnosis, and standards/spec review.
- `agent-evaluation`: exact metrics, fatal/threshold gates, multi-run evidence, and human preference traces for agents.
- `openai-docs`: official OpenAI model/API/Codex source route.
- `vercel-composition-patterns`: React component API and composition overlay.
- `browser:control-in-app-browser` and `chrome:control-chrome`: browser-backed acceptance and logged-in flow verification.

Compose optional skills only when they are currently available. Do not encode a missing integration as a required step.

## Project Execution Routing

Read `project-model-routing.md` before spawning a specialist or selecting a concrete model alias. Start with one owner, route by capability rather than model prestige, count context/handoff/retry/verification overhead, reuse a related worker, and reserve a fresh worker for independent verification or changed boundaries.

## Patch Minimization

Read `trajectory-guided-patch-minimization.md` only after a code-producing task has a reproducible passing baseline and the ownership and verifier gates are satisfied. Treat it as a conditional post-success overlay, not a replacement for specification, design, testing, or review. Record an explicit skip reason when the verifier, edit lineage, rollback, or acceptance coverage is insufficient.

## Artifact Traceability Gate

Before declaring non-trivial work complete, answer:

- Which acceptance criterion maps to which implementation evidence?
- Which test, eval, source check, or manual observation verifies it?
- Which planned item was changed or dropped, and why?
- Which failure was repaired, and was it local, upstream, or structural?
- Which non-functional constraints cover security, performance, reliability, cost, and rollback?
- Was eligible agent-authored change minimized, or was minimization skipped for a recorded ownership, verifier, risk, or cost reason?

Record uncovered criteria as remaining work. Do not silently redefine done.

## Decision Trace Template

```markdown
## Development Decision

Model profile / selection source:
Execution owner / capability role / selection source:
Worker reuse / fresh verifier / fallback:
Primary mode / overlays:
Rejected modes:
Evidence loaded:
Artifacts and verification gate:
Failure attribution or open risks:
Next decision:
```

Keep the trace short. Its job is reproducibility and explanation, not ceremony.

## Auto Loop Decision Template

```markdown
## Auto Loop Decision

Quantification verdict:
Exact metrics / hard gates / rubric:
Verifier and threshold:
Max rounds and state:
Normal modes used:
Fallback if refused:
```

If quantification is not reliable, set `Quantification verdict: refused` and continue as an ordinary task.
