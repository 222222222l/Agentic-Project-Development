# Spec-Driven Development

## Use When

Use SDD for new projects, new features, vague requests, architectural decisions, cross-module changes, stakeholder-facing work, or tasks likely to exceed one focused session.

Skip a full spec for tiny, reversible, self-contained changes. Still write acceptance criteria when behavior matters.

## Core Artifacts

- Assumptions: what is being inferred and needs correction.
- Objective: user, problem, value, and success signal.
- Scope: in-scope, out-of-scope, constraints, non-goals.
- Acceptance: concrete observable outcomes.
- Technical plan: affected modules, data, APIs, risks, sequence.
- Verification: tests, evals, manual checks, source citations, release gates.

## Gated Workflow

1. **Specify**: state assumptions, ask only direction-changing questions, then write the spec.
2. **Approve**: get explicit user confirmation when ambiguity affects scope, cost, data, or irreversible decisions.
3. **Plan**: convert the spec into implementation slices and verification points.
4. **Implement**: execute one slice at a time.
5. **Update**: keep the spec current when decisions change.

## Spec Template

```markdown
# Spec: <name>

## Objective

## Users and Jobs

## Success Criteria

## Scope

## Out of Scope

## Assumptions

## Technical Approach

## Verification Strategy

## Risks and Open Questions
```

## Integration With Existing Skills

- Use `grill-with-docs` before SDD when the domain language or constraints are not yet shared.
- Use `to-prd` after SDD when the spec is stable enough to publish as a product/engineering artifact.
- Use `to-issues` after SDD or PRD approval to create vertical slices.
- Use `architecture-and-domain.md` when SDD exposes new domain concepts or module boundaries.

## Explainability Gate

Before coding, be able to answer:

- What would make this work wrong even if the code compiles?
- Which assumptions would change the solution?
- Which artifact is the source of truth?
- Which verification gate proves completion?
