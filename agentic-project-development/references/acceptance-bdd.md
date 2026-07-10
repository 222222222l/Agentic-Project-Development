# Behavior and Acceptance Driven Development

## Use When

Use BDD or acceptance-driven development when user-visible behavior is the contract: workflows, permissions, checkout, onboarding, forms, notifications, reports, API contracts, state machines, business rules, and edge-case handling.

## Discovery

Start with concrete examples. Ask for or infer representative scenarios:

- Happy path.
- Boundary path.
- Permission or role difference.
- Invalid input.
- Recovery from failure.
- Existing behavior that must not regress.

## Scenario Format

Use Given/When/Then for behavior, not UI mechanics.

```gherkin
Scenario: Eligible customer applies a discount
  Given the customer has an active account
  And the cart contains an eligible item
  When the customer applies a valid discount code
  Then the order total reflects the discount
  And the discount appears in the order summary
```

## Automation Strategy

- Use executable `.feature` files only when the project already supports or wants Cucumber/Gherkin.
- Otherwise translate scenarios into framework-native tests, Playwright journeys, API contract tests, or issue acceptance criteria.
- Keep scenarios business-readable. Put technical setup inside fixtures or test helpers.

## Integration

- Feed scenarios into SDD success criteria.
- Feed scenarios into `to-issues` acceptance criteria.
- Compose with a currently available frontend or design skill when scenarios involve visual product direction or implementation.
- Use `browser:control-in-app-browser` or `chrome:control-chrome` to verify implemented journeys in a real browser.
- Use TDD for deterministic units behind a scenario.
- Use EDD when a scenario's output is semantic, probabilistic, or LLM-generated.
- Use review mode to check which scenarios are untested.

## Anti-Patterns

- Gherkin that describes clicks and CSS selectors rather than behavior.
- One scenario that tests many independent behaviors.
- Scenarios written after implementation merely to document what happened.
- Acceptance criteria that cannot be observed by a user, API client, or evaluator.
