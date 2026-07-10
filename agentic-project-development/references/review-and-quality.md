# Review, Debugging, and Quality Gates

## Use When

Use this mode for code review, implementation verification, debugging, regression analysis, release readiness, or deciding whether an issue is complete.

## Review Axes

1. **Spec fidelity**: Does the implementation satisfy the spec, PRD, issue, scenarios, or eval criteria?
2. **Engineering standards**: Does it fit project style, architecture, test strategy, security posture, performance needs, and maintainability?
3. **Verification quality**: Are tests/evals/source checks meaningful and sufficient?
4. **Residual risk**: What can still fail and how would we notice?
5. **Process discipline**: Did planning remain faithful, verification cover claims, recovery target causes, abstention protect missing evidence, and each transition preserve a valid state?

## Debugging Loop

1. Reproduce the failure.
2. Minimize the case.
3. Form a hypothesis.
4. Instrument or inspect the exact boundary.
5. Fix the root cause.
6. Add regression coverage at the right seam.

## Quality Gates

Pick gates based on project type:

- Deterministic code: unit/integration tests, typecheck, lint, build.
- User journey: Playwright/manual smoke/acceptance scenarios.
- LLM output: eval suite, failure examples, score deltas.
- Framework/API work: official source citation and version check.
- Architecture refactor: seam stability and old behavior preserved.
- Release: changelog, migration notes, monitoring, rollback path.
- Agent system: model-harness metadata, repeated runs, trace inspection, failure attribution, approval boundaries, and fatal gates.

## Process Discipline Gate

For substantial or autonomous work, check:

- **Planning fidelity**: the implemented slice still maps to the approved outcome.
- **Verification coverage**: every completion claim has observed evidence.
- **Recovery efficiency**: retries target local or upstream causes instead of replaying blindly.
- **Abstention quality**: the agent stops when permission, evidence, or a reliable verifier is absent.
- **Atomic transition integrity**: failed steps do not leave hidden partial state or corrupt the next phase.

## PR and Handoff Gate

- Keep scope and explanation proportional; complexity and verbosity can reduce reviewer trust.
- State why the change is needed, what changed, what was verified, residual risk, and intentional non-changes.
- Include security, performance, reliability, cost, and rollback constraints when relevant; these are commonly omitted from agent context.
- Separate spec-fidelity review from code-quality review so a polished implementation cannot hide the wrong behavior.

## Output Format

Lead with findings when reviewing. Include:

- Blocking issues.
- Non-blocking risks.
- Missing verification.
- Suggested next action.
- What passed.

## Integration

- Use `code-review` for diff review.
- Use `diagnosing-bugs` for hard failures.
- Use `karpathy-guidelines` to check whether changes stayed simple, surgical, and explicitly verified.
- Use a currently available UX/accessibility audit capability when product flow or visual quality is in scope.
- Use `browser:control-in-app-browser` or `chrome:control-chrome` for screenshot-backed web QA and interaction checks.
- Use BDD/TDD/EDD references to identify missing coverage type.
- Use source-driven development to catch stale API patterns.
- Use `agent-evaluation` for multi-run agent evidence and `agent-system-engineering.md` for trajectory-level failures.
