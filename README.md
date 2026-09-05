# Agentic Project Development

A portable skill for completing software and agent-development work with relevant
evidence, task-sized planning, targeted verification and recoverable progress.
It works with the host's existing tools; no new runtime or framework is required.

**2026-09 research update:** [中文调研、证据与采纳记录](agentic-project-development/references/research-evidence-2026-09.md)
covers 2026-07-05 through 2026-09-05. It separates reported paper results,
engineering adaptations, negative evidence and mechanisms requiring local trials.

## How Work Is Routed

For a clear local edit:

```text
inspect -> change -> relevant check -> result
```

For substantial work, keep one outcome, change boundary and verifier. Load the
relevant method only when ambiguity, behavior, dependencies or risk requires it:
SDD, BDD, TDD, EDD, source grounding, architecture, review, delivery or agent-system
engineering. Multiple applicable methods can share one plan and evidence record.

- Retrieve for the next decision; batch independent reads and preserve results.
- Use existing structured tools or code execution where they reduce round trips.
- Verify affected behavior first, then required integration/release checks.
- Diagnose failed transitions before replaying work; preserve working candidates.
- Track dependencies and completed regression obligations for long tasks.
- Distill reusable subtask procedures instead of loading whole task transcripts.
- Compare skills and harnesses through attributable behavior and held-out outcomes.
- Include failed attempts, cached tokens and coordination in efficiency accounting.

## Profiles and Delegation

`frontier-compact` and `portable-guided` control instruction density. Select them
from the actual model-harness capability or an explicit user/project preference.
Either profile can fit an open-weight or proprietary model. Names alone do not
select a profile; add guidance only to weak or unfamiliar phases.

Keep one execution owner. Delegate bounded independent work only when the active
host and user policy allow it and the expected benefit exceeds coordination and
integration cost. Shared evidence should use artifact references when that avoids
repeated messages. Fresh verification may use a separate worker when warranted.

The skill cannot switch the current model, invent worker persistence, expose
unavailable tools, or grant permission. A router recommendation is not authority.

## Long Tasks and Improvement Loops

User-requested persistence uses observable acceptance and a declared budget or
stop rule. Binary checks are sufficient; neither a universal 8/10 rubric nor a
fixed three-round limit applies. Diagnose stalled attempts, execute ready work,
and retain completed checks as regression obligations when dependencies change.

On resume, reconcile the saved objective, user corrections, artifacts and passed
checks with actual workspace state. A proposed action is not a completed action.
Keep recoverable evidence when compacting progress.

For Skill/harness experiments, use cheap behavior-matched development probes,
regression sentinels, fresh development confirmation, then a sealed final set.
Author-written tests are diagnostic and cannot replace independent acceptance.

## Research and Evidence Limits

The new review includes controlled tool-interface experiments, SkillHEX,
HarnessLens, skill-transfer studies, Harness-IF and recent context-file ablations.
LoopsBench supplies long-task diagnostics. The existing AgentTether recovery and
TRIM patch-minimization methods remain scoped to their evidence.

History-free state, trained retrievers, automatic skill-selection algorithms,
recursive agent systems and full harness evolution remain optional experiments.
The skill does not turn a paper's benchmark gain into a promise about a prompt.

This revision is research-grounded and locally validated, not a replicated
cross-harness productivity result. Static and routing checks establish package
integrity and routing behavior; behavioral smoke checks establish only exercised
cases. Quantified transfer requires paired representative tasks on each claimed
model-harness configuration. See the linked research record for study limitations
and [source lineage](agentic-project-development/references/source-map.md).

## Install

Copy the `agentic-project-development/` directory to the host's skill directory.
For a standard Codex installation this is:

```text
~/.codex/skills/agentic-project-development
```

Use the configured skills location when it differs. Keep backups outside skill
discovery roots. The package contains `SKILL.md`, UI metadata, direct references
and dependency-free Python routing/validation scripts.

## Use and Validate

```text
Use $agentic-project-development to implement this change and verify it.
Use $agentic-project-development to diagnose repeated tool/retrieval overhead.
Use $agentic-project-development with portable-guided for this unfamiliar toolchain.
```

From the repository root:

```bash
python3 agentic-project-development/scripts/test_select_workflow.py
python3 agentic-project-development/scripts/validate_skill_graph.py --skill-dir agentic-project-development
python3 agentic-project-development/scripts/select_workflow.py --work-type feature --scope cross-module --capability-tier frontier --harness-maturity strong
python3 agentic-project-development/scripts/select_workflow.py --work-type skill --scope single-module --bottleneck verification
python3 agentic-project-development/scripts/select_workflow.py --horizon long --loop-request yes --quantifiable yes --delegation-policy forbidden
```

Use the environment's Python executable if `python3` is unavailable.
`--model-name` records metadata; use explicit capability/profile flags for routing.
`--quantifiable` defaults to `partial`, so a requested loop first establishes its
verifier. `--bottleneck` routes a diagnosed cost to focused guidance;
`--horizon long` adds dependency and resume-state tracking.

## Project Conventions

Keep stable project commands, evaluated profiles, acceptance gates and model-role
mappings in an existing project instruction file or
`docs/agents/project-development-profile.md` when persistence helps. Do not create
one for every task or duplicate canonical documentation. Existing user
authorization remains valid for its scope.
