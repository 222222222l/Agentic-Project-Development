# Architecture and Domain Design

## Use When

Use this mode when a change introduces or reshapes domain concepts, module boundaries, interfaces, adapters, data ownership, or cross-cutting workflows.

Use it for architecture reviews, refactors, module deepening, hard-to-test code, duplicated shallow abstractions, or a codebase that feels difficult for agents and humans to navigate.

## Vocabulary

- Domain term: a word the project uses to compress meaning.
- Module: a unit with an interface and hidden implementation.
- Seam: the public boundary where behavior can be tested.
- Adapter: a boundary to an external dependency or different representation.
- Locality: how much relevant behavior can be understood in one place.
- Leverage: how much behavior is controlled by a small interface.
- ADR: durable decision record explaining why a path was chosen or rejected.

## Process

1. Read project domain docs such as `CONTEXT.md`, `CONTEXT-MAP.md`, and ADRs if present.
2. Identify concepts that lack names or have conflicting names.
3. Identify shallow modules, leaky seams, duplicated adapters, and tests forced into internals.
4. Propose at most a few architecture candidates, each with problem, solution, benefits, risks, and verification.
5. Use SDD or BDD before implementing if behavior or scope remains unclear.
6. Update domain docs when new terms become load-bearing.
7. Offer an ADR when a decision should prevent future re-litigation.

## Integration

- `karpathy-guidelines`: keep architecture edits scoped, assumption-led, and verifiable.
- `domain-modeling`: sharpen vocabulary and maintain `CONTEXT.md`.
- `codebase-design`: design deep modules and testable seams.
- `improve-codebase-architecture`: scan and present architecture deepening candidates.
- `vercel-composition-patterns`: apply React composition patterns when component API shape is part of the architecture.
- `tdd`: verify behavior through the chosen seam.
- `code-review`: confirm the final diff follows the design.

## Explainability Gate

Before implementing architecture changes, state:

- Which complexity is being concentrated or hidden.
- Which public seam will remain stable.
- Which tests should survive a refactor.
- Which domain term names the new concept.
