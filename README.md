# Agentic Project Development

A portable Codex skill for software and agent-development work. It routes work
through the lightest reliable combination of specification, behavior and
acceptance, testing, evaluation, source grounding, architecture, delivery,
debugging, review, uncertainty handling, patch minimization, and quantified
improvement loops.

The suite is a workflow layer, not an agent runtime. It works with the host's
existing tools and frameworks while keeping acceptance, verification, human
approval, and recovery explicit. No new runtime or framework is required.

## What This Skill Does

Use `$agentic-project-development` when planning, specifying, implementing,
testing, evaluating, refactoring, reviewing, minimizing agent-generated patches,
or decomposing a project or feature. It is also intended for LLM and
multi-agent systems, Skills and harness policies, persistent context, structured
traces, reusable feedback data, and evidence-backed improvement loops.

The suite helps an agent:

- classify task shape, risk, determinism, scope, and required capability;
- recognize loop, auto, autonomous, and run-until-done requests;
- choose among SDD, BDD, TDD, EDD, source-driven work, architecture, delivery,
  agent-system engineering, review, or debugging modes;
- load only the routed reference material needed for the current task;
- produce explicit assumptions, specifications, acceptance scenarios, test
  seams, eval criteria, issue slices, ADRs, decision traces, and review gates;
- keep project-specific choices explainable, auditable, and recoverable.

## Core Behavior

- Choose the lightest development mode that reduces a real risk.
- Ground every material phase in repository, runtime, or current source evidence.
- Express substantial phases as `input -> action -> artifact -> verifier -> stop`.
- Run loop or auto requests only when the verification target is quantifiable.
- Attribute failures as local, upstream, or structural before retrying.
- Route models by task capability and total execution plus coordination cost;
  keep one main owner by default.
- Reuse workers for related context and require fresh context when verification
  must be independent.
- Converge specification, plan, tasks, implementation, and verification before
  declaring completion.
- Keep persistent context minimal and task-relevant.
- Treat Skill, context-policy, and harness changes as evaluated candidates with
  provenance, permissions, paired utility, and rollback rather than trusted prose.

## How Work Is Routed

For a clear local edit:

```text
inspect -> change -> relevant check -> result
```

For substantial work, keep one outcome, change boundary, and verifier. Load the
relevant method only when ambiguity, behavior, dependencies, or risk requires it:
SDD, BDD, TDD, EDD, source grounding, architecture, review, delivery, or
agent-system engineering. Multiple applicable methods can share one plan and
evidence record.

- Retrieve for the next decision; batch independent reads and preserve results.
- Use existing structured tools or code execution where they reduce round trips.
- Verify affected behavior first, then required integration and release checks.
- Diagnose failed transitions before replaying work; preserve working candidates.
- Track dependencies and completed regression obligations for long tasks.
- Distill reusable subtask procedures instead of loading whole task transcripts.
- Compare skills and harnesses through attributable behavior and held-out outcomes.
- Include failed attempts, cached tokens, and coordination in efficiency accounting.

## Profiles and Delegation

`frontier-compact` and `portable-guided` control instruction density. Select
them from the actual model-harness capability or an explicit user or project
preference. Either profile can fit an open-weight or proprietary model; names
alone do not select a profile.

### `frontier-compact`

For strong long-horizon coding agents in mature harnesses. Load only routed
references, gather ordinary repository context autonomously, keep compact phase
contracts, and rely on executable or external verification.

### `portable-guided`

For smaller, unfamiliar, or weakly tooled deployments. Use explicit
`ALIGN -> EVIDENCE -> CONTRACT -> SLICE -> IMPLEMENT -> VERIFY -> REVIEW ->
CONVERGE` phases, reread files before edits, checkpoint cross-session work, and
restrict multi-agent use to typed handoffs with validators.

Examples:

```text
Use $agentic-project-development with the frontier-compact profile for this feature.
Use $agentic-project-development with portable-guided and keep a task state file.
Treat this deployment as frontier-compact only after a project-representative eval.
```

Keep one execution owner. Delegate bounded independent work only when the active
host and user policy allow it and the expected benefit exceeds coordination and
integration cost. Shared evidence should use artifact references where possible;
fresh verification may use a separate worker when warranted.

The skill cannot switch the current main model, invent worker persistence, expose
unavailable tools, guarantee subagent persistence across sessions, or compute
exact cost without telemetry. Runtime capability wins; unavailable model
requests fall back to the nearest exposed role and must be reported.

## Project Model Routing

The suite can implement project-level routing policy: classify each work unit,
choose a semantic capability role, decide whether delegation is worth its
coordination cost, reuse a related worker, and request a fresh verifier. A
project can map evaluated roles to model IDs in
`docs/agents/project-development-profile.md`.

Default route:

```text
ROUTE -> EXECUTE -> REASSESS -> VERIFY
```

Optimize total cost as execution + context loading + handoff + retry +
verification. Project profiles are policies, not new runtime permissions.

## Workflow

```text
PROFILE -> GATE -> ROUTE -> ALIGN -> GROUND -> SPECIFY -> SLICE
        -> EXECUTE -> REASSESS -> VERIFY -> RECOVER -> MINIMIZE -> CONVERGE -> EXPLAIN
```

The normal router defines acceptance and testing. Patch minimization is a
conditional post-success gate for eligible task-owned edits. Auto-loop mode
adds bounded repetition only after a reliable quantification gate.

## Long Tasks and Improvement Loops

User-requested persistence uses observable acceptance and a declared budget or
stop rule. Binary checks are sufficient; neither a universal score nor a fixed
round count applies. Diagnose stalled attempts, execute ready work, and retain
completed checks as regression obligations when dependencies change.

On resume, reconcile the saved objective, user corrections, artifacts, and
passed checks with actual workspace state. A proposed action is not a completed
action. Keep recoverable evidence when compacting progress.

For Skill or harness experiments, use cheap behavior-matched development probes,
regression sentinels, fresh development confirmation, and then a sealed final
set. Author-written tests are diagnostic and cannot replace independent
acceptance.

## Auto Loop Mode

When a user asks for loop, auto, autonomous iteration, keep-going, or
run-until-done behavior, the skill first applies an auto-loop gate:

1. Name the verifier, exact metrics, hard gates, rubric grader, threshold, budget,
   and maximum rounds.
2. Refuse loop execution when checks are subjective, unavailable,
   non-repeatable, or controlled only by the same agent's preference.
3. Run `PLAN -> DO -> VERIFY -> DECIDE` after the gate passes.
4. Stop when all hard gates and exact thresholds pass, or when the declared
   budget, maximum rounds, or blocker is reached.
5. Diagnose the weakest failure before localized repair, partial re-execution,
   or structural replanning.

The acceptance and testing standards still come from the normal router: SDD,
BDD, TDD, EDD, source-driven development, architecture, debugging, or review.

## Agent-System Engineering

The agent-system reference starts with the simplest viable design: deterministic
code, one structured model call, one tool-using agent, a deterministic workflow,
then a stateful graph or multi-agent topology only when measured value justifies
coordination cost.

It includes selection gates for OpenAI Agents SDK, Microsoft Agent Framework,
LangGraph, Pydantic AI, SWE-agent, OpenHands, GitHub Spec Kit, and Superpowers.
The first group is treated as runtime candidates; the latter methodologies are
treated as development-process references. No framework is installed or
required by this repository.

## Integrated Local Skills

This suite consolidates the useful development workflow responsibilities of
local skills into one project-development router:

- `clarify-project-requirements`
- `karpathy-guidelines`
- `grill-with-docs`
- `grilling`
- `domain-modeling`
- `codebase-design`
- `setup-matt-pocock-skills`
- `to-prd`
- `to-issues`
- `tdd`
- `improve-codebase-architecture`
- `code-review`
- `diagnosing-bugs`
- `vercel-composition-patterns`
- `openai-docs`
- `product-design:get-context`
- `product-design:audit`
- `product-design:ideate`
- `product-design:image-to-code`
- `browser:control-in-app-browser`
- `chrome:control-chrome`

The suite records skills that were reviewed but intentionally remain outside
the core router because they are domain, artifact, discovery, or meta-skill
specialists. See `agentic-project-development/references/source-map.md`.

## Repository Layout

```text
agentic-project-development/
  SKILL.md
  agents/openai.yaml
  references/
    workflow-map.md
    model-capability-profiles.md
    project-model-routing.md
    loop-auto-mode.md
    uncertainty-and-decision-trace.md
    spec-driven-development.md
    source-driven-development.md
    acceptance-bdd.md
    test-driven-development.md
    eval-driven-development.md
    agent-system-engineering.md
    skill-context-harness-governance.md
    data-flywheel-development.md
    agent-evaluation-standard.md
    efficient-execution.md
    architecture-and-domain.md
    issue-delivery.md
    review-and-quality.md
    trajectory-guided-patch-minimization.md
    personalization.md
    source-map.md
    research-evidence-2026-09.md
  scripts/
    select_workflow.py
    test_select_workflow.py
    validate_skill_graph.py
```

`SKILL.md` stays navigational. Detailed methods are loaded only when routed,
and deterministic checks live in `scripts/`.

## Install

Install the `agentic-project-development/` directory under:

```text
$CODEX_HOME/skills/agentic-project-development
```

When `CODEX_HOME` is unset, Codex normally uses:

```text
~/.codex/skills/agentic-project-development
```

The package can be installed from GitHub with:

```bash
scripts/install-skill-from-github.py --repo 222222222l/Agentic-Project-Development --path agentic-project-development
```

Or copy the directory manually. Keep backups outside the skill discovery root
so they are not discovered as duplicate skills. Restart Codex after installing
so skill metadata is reloaded.

## Use and Validate

Example prompts:

```text
Use $agentic-project-development to choose the right development workflow for this feature.
Use $agentic-project-development to turn this vague app idea into a spec, acceptance scenarios, and implementation slices.
Use $agentic-project-development for this LLM extraction pipeline and define the eval gates before implementation.
Use $agentic-project-development to diagnose repeated tool or retrieval overhead.
Use $agentic-project-development with portable-guided for this unfamiliar toolchain.
Use $agentic-project-development to review whether this PR satisfies the spec and has enough verification.
```

From the repository root:

```bash
python agentic-project-development/scripts/test_select_workflow.py
python agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
python agentic-project-development/scripts/select_workflow.py --work-type feature --scope cross-module --model-name gpt-5.6-sol --harness-maturity strong
python agentic-project-development/scripts/select_workflow.py --work-type agent-system --determinism llm --model-name Kimi-K2.7-Code --harness-maturity partial --risk high
python agentic-project-development/scripts/select_workflow.py --work-type review --scope project --risk high --task-role verification --verification-independence required
python agentic-project-development/scripts/select_workflow.py --work-type skill --scope single-module
python agentic-project-development/scripts/select_workflow.py --horizon long --loop-request yes --quantifiable yes --delegation-policy forbidden
```

Use the environment's Python executable when `python` or `python3` is not on
`PATH`. `--model-name` records metadata; explicit capability and profile flags
drive routing. `--quantifiable` defaults to `partial`, so a requested loop
first establishes its verifier. `--bottleneck` routes a diagnosed cost to
focused guidance, and `--horizon long` adds dependency and resume-state
tracking.

## Project Conventions and Extension Points

For stable repository conventions, create or update:

```text
docs/agents/project-development-profile.md
```

Do not create one for every task or duplicate canonical documentation. The
personalization reference supports local defaults for development modes,
test/eval frameworks, issue tracker conventions, documentation layout, risk
gates, source preferences, project vocabulary, ADR practice, model-role
mappings, worker reuse, fresh-verifier triggers, total-cost preference, and
unavailable-model fallback. Existing user authorization remains valid for its
scope.

## Researched Skills Rewritten Into This Suite

The suite incorporates useful ideas from researched agent skill frameworks
without copying them verbatim:

- `addyosmani/agent-skills`: Spec-Driven Development and Source-Driven Development
- `fradser/dotclaude`: Behavior-Driven Development
- `robotlearning123/behavior-driven-testing`
- `promptfoo/promptfoo`: prompt evaluation patterns
- `github/awesome-copilot`: Eval-Driven Development

See `agentic-project-development/references/source-map.md` for the mapping,
scope boundaries, and source lineage.

## Research and Evidence Limits

The 2026-09 research update is documented in
[`research-evidence-2026-09.md`](agentic-project-development/references/research-evidence-2026-09.md).
It covers 2026-07-05 through 2026-09-05 and separates reported paper results,
engineering adaptations, negative evidence, and mechanisms requiring local
trials.

The research record includes controlled tool-interface experiments, SkillHEX,
HarnessLens, skill-transfer studies, Harness-IF, context-file ablations, and
LoopsBench diagnostics. History-free state, trained retrievers, automatic
skill-selection algorithms, recursive agent systems, and full harness evolution
remain optional experiments. A paper's benchmark gain is not a promise about a
prompt, model, or local harness.

This revision is research-grounded and locally validated, not a replicated
cross-harness productivity result. Static and routing checks establish package
integrity and routing behavior; behavioral smoke checks establish only exercised
cases. Quantified transfer requires paired representative tasks on each claimed
model-harness configuration.

Research and model evidence in the base suite was checked on 2026-07-10. The
Skill/context/harness governance increment was checked against its linked arXiv
versions on 2026-07-25. The trajectory-guided patch-minimization boundary was
checked against TRIM (arXiv:2607.18161v1) on 2026-07-21. Concrete model
availability remains host-specific.

## Design Principles

- Use the lightest workflow that reduces real risk.
- Prefer explicit success criteria over ritual process.
- Treat TDD as one implementation mode, not a universal default.
- Use BDD when user-visible behavior is the contract.
- Use EDD when semantic or probabilistic output quality matters.
- Use source-driven development when current documentation can invalidate memory.
- Keep project-specific decisions explainable and auditable.
- Keep context and Skills minimal until paired evidence shows that more helps.
- Preserve human approval, permissions, and rollback boundaries during evolution.

The practical result is intentionally conservative: minimal persistent context,
repository-grounded phases, explicit contracts, process-discipline gates,
model-harness evaluation, localized recovery, and human-readable evidence before
completion.
