# Issue Delivery and Work Decomposition

## Use When

Use this mode when converting a conversation, spec, PRD, design, bug report, or roadmap into implementable work.

## PRD Rules

Create a PRD when product intent and technical direction need a durable handoff. The PRD should focus on problem, solution, users, implementation decisions, testing decisions, out-of-scope items, and unresolved risks.

Use `to-prd` when existing conversation context is already sufficient. Use SDD first when it is not.

## Vertical Slice Rules

Break work into tracer bullets, not horizontal layers.

A good slice:

- Delivers a narrow complete behavior.
- Crosses the necessary stack end to end.
- Is demoable or verifiable alone.
- Has acceptance criteria and a verification command.
- Has clear dependencies.

A weak slice:

- Only creates database tables.
- Only builds UI without behavior.
- Only writes utility functions.
- Requires many later tasks before anything can be checked.

## Issue Template

```markdown
## What to build

## Acceptance criteria

- [ ] ...

## Verification

## Blocked by

## Notes
```

## Integration

- Use SDD or BDD to populate acceptance criteria.
- Use architecture/domain mode before slicing if boundaries are unclear.
- Use EDD to add eval tasks for LLM features.
- Use review mode before marking issue-ready when risk is high.

## AFK-Agent Readiness

An issue is ready for an agent when:

- The behavior is clear.
- The source of truth is linked or included.
- Required files or modules are discoverable.
- Verification is executable or explicitly manual.
- External dependencies and credentials are known.
