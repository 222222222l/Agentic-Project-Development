# Workflow Map

## Purpose

Use this file as the suite's top-level operating map. It explains how the component practices fit together without assuming one method fits every project.

## Lifecycle

1. **Loop gate**: when the user asks for auto/loop behavior, prove that the verification target can be reliably quantified before entering a repeated cycle.
2. **Align**: clarify the real outcome, constraints, audience, and non-goals.
3. **Specify**: write a stable spec when ambiguity or scope warrants it.
4. **Model behavior**: express user-visible rules as scenarios or acceptance criteria.
5. **Plan slices**: break work into vertical, independently verifiable increments.
6. **Implement**: choose TDD, source-driven implementation, prototype-first, or direct implementation based on risk.
7. **Evaluate**: run tests, evals, source checks, manual QA, and review gates.
8. **Record learning**: update domain docs, ADRs, issue tracker notes, eval datasets, loop state, and project profile.

## Mode Selection Matrix

| Situation | Primary mode | Overlay |
| --- | --- | --- |
| New feature with fuzzy requirements | SDD | BDD if user-facing |
| Existing discussion ready to package | PRD/issue delivery | Architecture if cross-module |
| Deterministic logic or bug fix | TDD | Source-driven if framework-specific |
| UI workflow, permissions, checkout, onboarding | BDD | TDD or Playwright |
| LLM, agent, RAG, prompt, extractor, classifier | EDD | Source-driven for SDK/API use |
| New framework/API integration | Source-driven | TDD or BDD |
| Codebase feels hard to change | Architecture/domain | Review after prototype |
| PR/diff quality check | Review | BDD/TDD/EDD gap analysis |
| User asks for loop/auto/run-until-done | Auto loop gate | Normal router after reliable quantification |

## Installed Skill Composition

- `karpathy-guidelines`: Apply across non-trivial coding work to keep assumptions visible, changes small, and verification explicit.
- `grill-with-docs`: Use during Align when project language or durable decisions need to be captured.
- `domain-modeling`: Use when new vocabulary appears or existing terms are fuzzy.
- `codebase-design`: Use when module boundaries, seams, adapters, and deep-module design matter.
- `vercel-composition-patterns`: Use as a React/UI architecture overlay when component APIs, reusable libraries, or prop proliferation are central.
- `tdd`: Use during Implement for deterministic behavior at confirmed public seams.
- `to-prd`: Use after enough context exists to synthesize a PRD without another interview.
- `to-issues`: Use after the plan or PRD is stable and ready for vertical slices.
- `improve-codebase-architecture`: Use when surfacing architecture candidates before choosing one to deepen.
- `code-review`: Use at Review for standards-vs-spec checks.
- `diagnosing-bugs`: Use when failures require reproduce, minimize, hypothesize, instrument, fix, and regression-test.
- `product-design:*`: Use for product/UI brief gates, visual exploration, image-to-code implementation, and UX audits.
- `browser:control-in-app-browser` and `chrome:control-chrome`: Use for web verification, screenshots, logged-in flows, and interaction checks.
- `openai-docs`: Use inside source-driven or eval-driven work when OpenAI SDK/API/model behavior matters.
- Auto loop mode: Use `references/loop-auto-mode.md` before other modes when the user asks for repeated autonomous iteration. It may wrap any mode, but only after a reliable quantified verifier is named.

## Decision Trace Template

```markdown
## Development Mode Decision

Chosen mode:
Rejected modes:
Why this mode:
Artifacts to produce:
Verification gate:
Open risks:
Next decision:
```

Keep the trace short. Its job is explainability, not bureaucracy.

## Auto Loop Decision Template

```markdown
## Auto Loop Decision

Loop requested:
Quantification verdict:
Verifier:
Threshold:
Max rounds:
Loop state:
Normal modes used:
Fallback if loop refused:
```

Use this only for loop/auto requests. If quantification is not reliable, set `Quantification verdict: refused` and continue as an ordinary task.
