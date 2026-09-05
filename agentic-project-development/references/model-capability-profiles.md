# Model Capability Profiles

Profiles control instruction density, not model selection, authority, or required
quality. Treat the model, tools and harness as a pair. Open weights, provider,
brand, and context-window size do not determine the profile.

## Selection

1. Honor the user's explicit profile.
2. Otherwise use the repository's evaluated default, when applicable.
3. Otherwise assess observed task-relevant capability and available tools.
4. If evidence is missing, use guided steps for the uncertain phase; do not
   demand an eight-stage ceremony for a trivial edit.

Use `project-model-routing.md` only when deciding execution ownership or models.
Concrete aliases belong to the active host or a versioned project profile. The
workflow selector accepts `--model-name` as descriptive metadata; it deliberately
does not classify capabilities from name substrings.

## Capability Probe

Evidence for compact execution includes the ability to:

- ground actions in files, runtime state and tool outputs;
- preserve user constraints, remaining work and verifiers across long context;
- load relevant references conditionally without loading the entire bundle;
- use tool schemas and structured results reliably;
- diagnose failures and change an unsuccessful approach;
- distinguish observed acceptance from its own confidence;
- recover state within the host's permissions and tool capabilities.

Infer from available traces or a small relevant task; do not run a synthetic
benchmark before every assignment. Escalate guidance only where a probe fails.

## Frontier-Compact

For a capable model-harness pair, regardless of vendor or weight access:

- keep one outcome, evidence boundary and verifier;
- let the agent discover routine context and implement independently;
- load only the current mode's material;
- expand plans at ambiguity, dependency or hard-to-reverse decisions;
- retain concise state at slice boundaries when recovery needs it;
- use executable results instead of repetitive prose checkpoints.

## Portable-Guided

For an unfamiliar or uneven model-harness pair:

- give explicit paths, expected artifacts and acceptance examples;
- make the next dependency and next verifier unambiguous;
- read the current file before editing and validate structured outputs;
- checkpoint completed results, current revision and remaining work;
- repair the demonstrated weak phase before expanding the whole workflow.

For substantial work, ALIGN -> EVIDENCE -> IMPLEMENT -> VERIFY -> CONVERGE is
a useful scaffold. Steps may share an artifact; do not summarize every reference
or repeat its rules as a mandatory output.

## Reassessment

Allow a tested open-weight deployment to use compact guidance, and add structure
to a frontier proprietary deployment when it fails on this task. Change one
intended factor when claiming a profile improves performance. Compare repeated
representative tasks and cost using `agent-evaluation-standard.md`; one clean
run supports a local decision, not universal transfer.
