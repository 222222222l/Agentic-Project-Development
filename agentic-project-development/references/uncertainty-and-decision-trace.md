# Uncertainty and Decision Trace

## Purpose

Use this overlay to reduce guessing before work, surface high-risk decisions during work, and preserve human understanding after work. It does not replace SDD, BDD, TDD, EDD, architecture, delivery, or review modes; it makes their decision points explicit.

## Use When

Use this overlay when the task is vague, cross-module, user-facing, architecture-sensitive, design-sensitive, hard to reverse, or likely to contain unknown requirements, hidden coupling, or expensive rework.

## Before Work: Expose Unknowns

Start by asking what problem the system primarily solves. Then scan for blind spots that can change the plan:

- Current architecture, ownership boundaries, integration seams, and coupling.
- Existing data, historical behavior, migrations, and compatibility constraints.
- Long-term expansion paths, likely variants, and non-goals.
- Risk points: security, money, data loss, performance, reliability, compliance, UX trust, and operational cost.
- Reference examples, prior art, screenshots, design systems, API docs, or comparable workflows.

Ask at most one high-leverage question at a time. Prefer questions whose answers can change architecture, data model, API contracts, UX flow, test strategy, or delivery slices. If a question would only polish wording, record an assumption and continue.

For style, visual design, interaction design, or unclear product feel, prefer a small prototype or concrete reference over long verbal description when explanation cost is high.

## During Work: Track Decision Points

Do not follow only a generic task checklist. Identify the high-risk decision route and watch the points where rework cost is highest:

- Data model and persistence boundaries.
- API, event, or integration contract shape.
- UX interaction and user-perceived behavior.
- Test strategy, eval strategy, and acceptance coverage.
- Reuse, dependency, framework, and abstraction choices.
- Migration, rollout, monitoring, and rollback choices.

When the implementation deviates from the original route, record the deviation, reason, boundary condition, tradeoff, and follow-up. Keep this short, but make it inspectable.

Use this decision note shape:

```markdown
Decision:
Why now:
Alternatives considered:
Evidence:
Boundary / edge case:
Tradeoff:
Follow-up:
```

## Layer Unknown Tasks

Treat substantial tasks as something to illuminate layer by layer rather than solve in one pass:

1. Clarify the outcome, inputs, constraints, and done criteria.
2. Split unknown work into chain/tooling/data/UI/domain-technique layers.
3. For unknown output quality, make a prototype or minimal tracer bullet first.
4. For unfamiliar domain technique, ask for or produce a short teaching note, reference, or checklist before implementing.
5. Promote the learned constraints into acceptance criteria, tests, evals, or review gates.

## After Work: Preserve Understanding

After implementation or review, do more than report that commands passed. Produce a human-readable change explanation when the change is non-trivial:

- Why the change was needed.
- What changed at the behavior, interface, data, and architecture levels.
- What risks remain and how they are monitored or bounded.
- What verification was run and what it proves.
- What was intentionally not changed.

If the agent cannot explain the change coherently, do not treat the work as ready to merge. Ask a clarifying question, inspect the diff again, or create a smaller explanation artifact first.

For high-risk changes, ask one reverse-check question that tests understanding, such as: "What would break if this assumption is wrong?" or "Which edge case is least covered?"
