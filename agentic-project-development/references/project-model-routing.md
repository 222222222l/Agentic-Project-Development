# Project Model Routing

## Contents

- Purpose and boundary
- Routing lifecycle
- Capability roles
- Delegation gate
- Model selection and total cost
- Worker reuse
- Reassessment and verification
- Project profile contract

## Purpose and Boundary

Use this reference to route one project's work between the main agent, specialist subagents, and an independent verifier. Map the task before choosing a model. A model name is an optional runtime alias, not the routing ontology.

A skill can define project policy, inspect a project profile, recommend roles, and request a subagent model when the active harness exposes that control. A skill cannot by itself switch the current main model, create unavailable model IDs, guarantee worker persistence across sessions, or measure exact cost without telemetry. Runtime capability and user authorization always override the static route.

## Routing Lifecycle

Use `ROUTE -> EXECUTE -> REASSESS -> VERIFY`:

1. **ROUTE**: map task structure, capability, dependencies, risk, context, verifier, and expected coordination cost.
2. **EXECUTE**: keep one main owner; delegate only a bounded, non-overlapping responsibility with a typed result.
3. **REASSESS**: re-route when evidence changes the plan, failure attribution changes, or coordination cost exceeds expected value.
4. **VERIFY**: use executable evidence first; add a fresh independent verifier when risk justifies its cost.

Do not pre-assign models to an entire project. Route each coherent work unit after its shape is known.

## Capability Roles

| Role | Use for | Default owner |
| --- | --- | --- |
| `orchestrator-editor` | Decomposition, decisions, integration, user communication, final state | Main agent |
| `reasoning-investigator` | Ambiguous architecture, causal analysis, competing hypotheses | Main agent or one bounded specialist |
| `code-executor` | Repository inspection, implementation, tests, tool-heavy iteration | Main agent |
| `visual-evaluator` | Screenshot, layout, interaction, perceptual or design judgment | Visual-capable worker when needed |
| `source-researcher` | Large current-source search and evidence organization | Read-only explorer |
| `independent-verifier` | High-risk final review, adversarial checks, spec/standards comparison | Fresh context or worker |

Roles describe required capability. Map them to concrete model IDs only from the active harness or the project's evaluated alias table.

## Delegation Gate

Start with one agent. Delegate only when at least one condition is true and the expected value exceeds coordination cost:

- exploration will produce much more raw information than the final conclusion;
- there are two or more independent investigation axes with no overlapping search;
- a visual, retrieval, or other specialist capability is materially stronger than the main route;
- independent verification is required by risk, policy, or the acceptance contract;
- the user explicitly requests a model or subagent split that the harness can support.

Do not delegate a small, clearly located, tightly coupled, or immediate blocking task. Keep planning, implementation integration, and overlapping file edits with the main agent unless the project explicitly assigns disjoint ownership.

For exploration, prefer one worker; use two only for distinct axes. More workers require a project override plus an integration verifier. Every delegation contract names:

```markdown
Role and objective:
Owned scope / forbidden overlap:
Inputs and evidence:
Required output and file-line evidence:
Verifier:
Return or escalation condition:
```

Wait for the worker, consume its distilled result, and do not repeat its search. Spot-check only material uncertainty.

## Model Selection and Total Cost

Resolve a route in this order:

1. Explicit user model or role choice.
2. Project profile and project-representative eval evidence.
3. Models, roles, tools, permissions, and reuse controls exposed by the current harness.
4. Task-role fit and verification needs.
5. Current main model or safest available fallback.

Optimize expected total cost, not token price:

```text
total cost = execution + context loading + handoff + retry + verification
```

Use observed telemetry when available. Otherwise compare `low`, `medium`, or `high` coordination cost and record the assumption. A cheap worker that needs repeated prompting, duplicated context, and stronger re-verification may cost more than one capable owner.

When the user requests an unavailable model, preserve the requested role and select the nearest exposed capability. Report the fallback; never silently claim the requested model ran.

## Worker Reuse

Reuse an existing worker handle when the next task has the same objective, module, data flow, evidence base, and trust boundary. Send a focused continuation instead of reloading background context.

Use a fresh worker when:

- verification must be independent of the implementation context;
- the objective, module, data flow, or permission boundary changed;
- prior context is contaminated by a disproven assumption;
- the existing worker is unavailable or the harness cannot continue it safely.

Reuse is opportunistic. Do not promise persistence beyond the current run or thread unless the harness exposes durable thread identity and continuation.

## Reassessment and Verification

Re-run routing when:

- new evidence invalidates decomposition or acceptance assumptions;
- a verifier fails twice for materially the same reason;
- failure changes from local to upstream or structural;
- a supposedly independent axis becomes coupled;
- actual coordination, retry, or context-loading cost exceeds the route estimate.

For low-risk work, executable tests plus main-agent review are sufficient. For high-risk, security-sensitive, cross-module, release, or hard-to-reverse work, prefer a fresh `independent-verifier` after implementation. Independence means fresh task framing and no ownership of the implementation; it does not require a different model family.

If no independent worker is available, run the named executable verifiers and perform a separate review pass. Disclose that the review was not agent-independent.

## Project Profile Contract

Put stable project routing policy in `docs/agents/project-development-profile.md`:

```markdown
## Project Model Routing

- Routing enabled: yes
- Default orchestrator capability:
- Evaluated role -> model aliases:
- Harness-exposed model IDs:
- Maximum explorers: 2
- Delegate high raw-information exploration: yes
- Keep implementation owner: main-agent
- Reuse key: objective + module + data-flow + trust-boundary
- Fresh verifier required for:
- Total-cost preference:
- Model-unavailable fallback:
- User approval required for:
```

The profile may narrow delegation and model use. It cannot grant unavailable tools, models, permissions, or authority.
