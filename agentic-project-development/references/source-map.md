# Source Map

This suite is a rewritten orchestration layer, not a verbatim bundle. Keep method sources separate from runtime dependencies and current local availability.

## Local Skills Integrated

| Skill | Integrated role |
| --- | --- |
| `clarify-project-requirements` | Outcome alignment and lowest-cost viable path |
| `karpathy-guidelines` | Assumptions, small scoped changes, and explicit verification |
| `grill-with-docs`, `grilling` | High-leverage questioning and durable decision capture |
| `domain-modeling`, `codebase-design` | Shared vocabulary, deep modules, and stable seams |
| `setup-matt-pocock-skills` | Repo issue and domain-doc setup |
| `to-prd`, `to-issues` | Durable intent and vertical tracer-bullet delivery |
| `tdd` | Deterministic red-green implementation at public seams |
| `improve-codebase-architecture` | Architecture deepening candidates |
| `code-review`, `diagnosing-bugs` | Standards/spec review and root-cause diagnosis |
| `agent-evaluation` | Exact metrics, fatal gates, multi-run task suites, and human trace scoring |

## Current Optional Composition

| Capability | Use |
| --- | --- |
| `openai-docs` | Official OpenAI model/API/Codex source route |
| `vercel-composition-patterns` | React component API and composition design |
| `browser:control-in-app-browser`, `chrome:control-chrome` | Browser-backed acceptance and logged-in journeys |
| `sites:sites-building`, `imagegen` | Frontend delivery or visual assets when the task specifically requires them |

Treat optional composition as availability-dependent. Do not claim a plugin skill is locally installed when it is merely surfaced by the current harness.

## Development Methods Adapted

| Source | Integrated role |
| --- | --- |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Constitution/spec/plan/tasks, cross-artifact analysis, checklist, converge, extensions, and project overrides |
| [Superpowers](https://github.com/obra/superpowers) | Clean baseline, verification-before-completion, spec-then-quality review, skill behavior evals; universal TDD is intentionally not inherited |
| `addyosmani/agent-skills` | Spec-driven and source-driven development gates |
| `fradser/dotclaude`, `robotlearning123/behavior-driven-testing` | Behavior discovery, scenarios, branch coverage, and real-environment checks |
| `promptfoo/promptfoo`, `github/awesome-copilot` | Prompt/agent eval datasets, graders, instrumentation, and CI gates |
| `cobusgreyling/loop-engineering`, `GaosCode/PlanWeave`, `baidu-baige/LoongFlow` | Loop readiness, file-backed state, recoverability, and plan-execute-summary memory |
| `doodledood/manifest-dev`, `indiekitai/codex-orchestrator`, `StGarca/consensus-mcp` | Define-done-first, worktree/ledger patterns, and maker-checker separation |

## Agent Runtime Frameworks Reviewed

| Framework | Position in this suite |
| --- | --- |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | Lightweight agents, sandbox work, tools, handoffs, guardrails, sessions, and tracing |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Python/.NET production graphs, checkpoints, OTel, governance, and HITL |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Low-level stateful graphs, durable execution, interrupts, memory, and traces |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | Typed Python contracts, provider portability, evals, OTel, and durable workflows |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent), [OpenHands](https://github.com/OpenHands/OpenHands) | Software-engineering agent reference harnesses and evaluation targets |

These are candidates, not required dependencies. `references/agent-system-engineering.md` defines the selection gate.

## Research Constraints Added

| Research | Constraint absorbed |
| --- | --- |
| [Evaluating AGENTS.md (2602.11988)](https://hf.co/papers/2602.11988) | Keep context files minimal; unnecessary instructions can reduce success and increase inference cost |
| [Agent READMEs (2511.12884)](https://hf.co/papers/2511.12884) | Include neglected non-functional constraints such as security and performance |
| [Spec Kit Agents (2604.05278)](https://hf.co/papers/2604.05278) | Ground and validate every phase against repository evidence |
| [RigorBench (2606.22678)](https://hf.co/papers/2606.22678) | Measure planning, verification, recovery, abstention, and atomic transition integrity |
| [Harness-Bench (2605.27922)](https://hf.co/papers/2605.27922) | Attribute capability to model plus harness configuration |
| [Meta-Agent (2605.25233)](https://hf.co/papers/2605.25233) | Use explicit contracts, intermediate verification, and local/upstream/structural error attribution |
| [AgentTether (2607.06273)](https://hf.co/papers/2607.06273) | Localize failed transitions and retain behavior-scoped repair memory |
| [RAMP (2605.27492)](https://hf.co/papers/2605.27492) | Evaluate runtime failures, recovery, tool use, serial dependencies, and cost |
| [Why Agentic-PRs Get Rejected (2602.04226)](https://hf.co/papers/2602.04226) | Keep PR scope/explanation proportional and preserve reviewer-trust evidence |

## Data-Flywheel Methods Integrated

Evidence checked on 2026-07-12:

| Source | Constraint absorbed |
| --- | --- |
| [Shared ChatGPT discussion: Data Flywheel and AI Applications](https://chatgpt.com/share/6a533694-1c98-83e8-932f-6a6d05e8410a) | Separate product, learning, and validation loops; prioritize attributable feedback and the lowest-cost effective improvement |
| [OpenAI: trustworthy evaluation playbook](https://openai.com/index/trustworthy-third-party-evaluations-foundations/) | Evaluate the model plus harness, tools, safeguards, environment, and budget; report contamination, reward hacking, broken tasks, and other validity hazards |
| [OpenAI AgentKit](https://openai.com/index/introducing-agentkit/) | Use versioned datasets, end-to-end trace grading, human annotations, and evidence-backed optimization |
| [Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Define tasks, trials, graders, and complete trajectories; use multi-run evidence, stable isolated environments, calibrated graders, and capability/regression suites |
| [Google Cloud agent observability](https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability) | Unify logs, metrics, traces, prompts, tool calls, safety, cost, and quality through OpenTelemetry-compatible telemetry |
| [Microsoft Foundry Agent DevOps loop](https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/) | Convert production traces into datasets, replay incidents, evaluate multi-turn behavior, preserve candidate lineage and rollback, and measure business ROI |
| [AWS production feedback loops](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-feedback.html) | Link every feedback item to its full trace with a stable `trace_id`; centralize schema validation and retain humans for high-risk decisions |
| [AWS AgentCore quality optimization](https://aws.amazon.com/blogs/machine-learning/introducing-agent-quality-optimization-in-agentcore-now-in-preview/) | Use observe -> evaluate -> improve with batch evaluation and controlled A/B testing before promotion |
| [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) | Keep agent, model, tool, MCP, metric, and event telemetry vendor-neutral and portable |

## Model Evidence Boundary

Evidence checked on 2026-07-10:

- The current Codex harness exposes `gpt-5.6-sol` as a frontier agentic coding model; capability still depends on its tools, state, permissions, and verifier.
- [Kimi K2.5](https://hf.co/papers/2602.02276) documents multimodal agentic training and Agent Swarm; current open checkpoints include Kimi K2.7 Code. Use `portable-guided` until the deployment passes project evals.
- [DeepSeek V4](https://hf.co/papers/2606.19348) documents million-token open models; long context does not itself prove reliable tool execution or workflow recovery. Use `portable-guided` until evaluated.
- Public Fable 5 evidence is dominated by agent traces and distillation datasets. Keep it as an explicit alias, not a hard-coded capability claim.

## Design Difference

The suite adds a mode router, progressive references, quantification-first loops, evidence-grounded phase contracts, artifact convergence, process-discipline gates, model-harness profiles, and repo-local customization without requiring one runtime or one development ritual.
