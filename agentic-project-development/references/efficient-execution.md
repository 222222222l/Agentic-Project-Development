# Efficient Agent Execution

Use when a trajectory shows unnecessary retrieval, context growth, idle turns,
tool overhead, repeated failure, or excessive verification. Do not add a new
optimization phase to a task that is already progressing efficiently.

## Locate the Cost

Inspect one representative trace before changing the workflow. Classify the
dominant cost as retrieval, context, tool interaction, failed work, verification,
coordination, or external waiting. Change the corresponding mechanism first.
Record quality with total tokens, cache usage, wall time, and retries when
available; do not invent exact savings from shorter prose or fewer tool calls.

## Retrieve for the Next Decision

Start at the error, named symbol, entry point, or acceptance test. Return a small
evidence packet: file and location, relevance, caller/contract, verifier, and
unresolved dependency. Search callers, configuration, generated sources, or
history when the initial evidence cannot explain behavior.

Batch independent searches and file reads. Inspect every result, including
errors and truncation. Read bounded spans; preserve a path to complete output.
Stop broad discovery once the change boundary and verification seam are known.
Reopen exploration if implementation contradicts that evidence. A guessed file
list or irrelevant retrieval can cost more than ordinary repository inspection.

## Use the Existing Tool Surface

Use structured file/edit tools for localized changes when available. Use code
execution for repeated parsing, filtering, aggregation, or independent reads
when it reduces model round trips. Do not force all work through one tool.

Keep per-operation status and useful output. Never batch dependent mutations,
approval decisions, or side effects that require observing the previous result.
Poll a running job through its existing handle rather than launching duplicates.
An error, timeout, or truncated response is a diagnostic signal, not evidence of
an empty repository or completed action.

CLI, MCP, CodeAct, cached and uncached tokens have different costs in different
harnesses. Compare the actual pair under equal task and verification budgets
before changing its default tool architecture.

## Verify in Layers

Choose the cheapest check that can reject the current hypothesis: parse/schema,
typecheck, focused reproduction, affected tests, integration scenario, then
project-required full checks. A documentation or cosmetic edit may need only
inspection or a build; new tests should detect a meaningful failure.

After a narrow repair, run affected checks and retained regression obligations.
Keep passing results tied to code, inputs and environment revisions; invalidate
them when these change. Do not rerun a costly unchanged full suite merely to
produce another success message. Do not skip release-required checks.

For stochastic Skill/harness experiments, selective *development* verification
needs behavior-matched tasks plus regression sentinels and fresh confirmation;
see `skill-context-harness-governance.md`. It cannot replace held-out evaluation.

## Recover with Information

Locate the earliest transition unsupported by evidence. Separate local errors,
bad upstream inputs, structural mistakes, and external tool/environment faults.
If several causes fit, use a small discriminating probe before another full run.
Agent-written probes diagnose; the independent acceptance contract still decides.

Keep the passing candidate, cause tested, evidence, failed alternative and
applicability boundary. When the same failure recurs without new information,
change the hypothesis or intervention. Spend on another model, search branch or
worker only when it addresses the diagnosed limitation and the host permits it.

## Keep State Sufficient

For long work, maintain a compact current-state record and links to full logs.
Preserve unresolved hypotheses, exact identifiers, user corrections, decisions,
remaining dependencies and passed checks at the appropriate revision. Re-read
live state before resuming a mutation or trusting an old verification result.

Do not confuse a rolling summary with a complete audit trail. Open-ended coding
can make an earlier observation relevant later. Retain recoverable originals and
recent tool-call/result pairs; use host-native compaction when available.
Replacing all history with a fixed schema is an optional runtime experiment,
not a change a skill can impose on a host conversation.

## Evidence Boundary

These procedures adapt the tool architecture, retrieval, verification and state
studies summarized in `research-evidence-2026-09.md`. Full CodeAct migration,
trained retrieval, branch-search optimization, and history-free execution need
separate local experiments. Success and cost must be assessed together,
including failed runs and the overhead of optimizing the system itself.
