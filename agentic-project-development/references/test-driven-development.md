# Test-Driven Development

## Use When

Use TDD for deterministic behavior where a public seam is known or can be agreed. Good targets include pure logic, domain rules, reducers, API handlers, validators, adapters, state transitions, and regression fixes.

Do not default to TDD when the real risk is unclear requirements, UX acceptance, architecture direction, or LLM quality. Use SDD, BDD, architecture, or EDD first.

## Seam Rule

Name the seam before writing a test. A seam is the public interface where behavior can be observed without coupling to internals.

Prefer high seams that survive refactors. Avoid testing private helpers unless the helper is itself a public module contract.

## Loop

1. Write one failing test for one behavior.
2. Run it and confirm it fails for the expected reason.
3. Implement only enough to pass.
4. Run the relevant suite.
5. Refactor only after behavior is covered and passing.

## Test Quality

Good tests:

- Read like behavior specifications.
- Use independent expected values.
- Fail when behavior is wrong.
- Survive internal refactors.
- Avoid duplicated implementation logic in assertions.

Bad tests:

- Assert private implementation details.
- Mock the unit under test into tautology.
- Use snapshots without meaningful review.
- Cover imagined future behavior before current slice works.

## Integration

- Use BDD scenarios to choose high-value tests.
- Use SDD success criteria to define what must be covered.
- Use source-driven development for framework-specific test patterns.
- Use review mode to identify missing regression tests.
