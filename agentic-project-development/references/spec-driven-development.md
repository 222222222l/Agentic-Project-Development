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

1. **Ground**: inspect repository evidence, historical behavior, current sources, and project constraints before drafting.
2. **Specify**: state assumptions, ask only direction-changing questions, then write the spec.
3. **Approve**: get explicit user confirmation when ambiguity affects scope, cost, data, or irreversible decisions.
4. **Plan**: convert the spec into implementation slices and phase contracts.
5. **Analyze**: verify consistency and coverage across spec, plan, acceptance criteria, and tasks before implementation.
6. **Implement**: execute and verify one vertical slice at a time.
7. **Converge**: map implemented evidence back to acceptance criteria and append genuine remaining work.
8. **Update**: keep the source-of-truth artifact current when decisions change.

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
- Use `agent-system-engineering.md` when the design introduces tools, handoffs, state, memory, evaluators, or multi-agent topology.

## Context Discipline

Keep repository guidance minimal and task-relevant. Prefer exact build/test commands, architecture boundaries, non-functional constraints, and known hazards. Do not copy a full handbook into agent context; unnecessary requirements can reduce success and increase cost.

For durable project principles, reuse the repo profile or existing constitution instead of repeating them in every feature spec.

## Explainability Gate

Before coding, be able to answer:

- What would make this work wrong even if the code compiles?
- Which assumptions would change the solution?
- Which artifact is the source of truth?
- Which verification gate proves completion?
- Which repository evidence grounds each architecture or API claim?
- Can every implementation task be traced to an acceptance criterion?
