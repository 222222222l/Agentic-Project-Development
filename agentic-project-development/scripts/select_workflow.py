#!/usr/bin/env python3
"""Recommend development modes, instruction density, and project execution routing."""

from __future__ import annotations

import argparse
import json


FRONTIER_ALIASES = ("gpt-5.6-sol", "fable5", "fable-5")
PORTABLE_ALIASES = ("kimi", "deepseek", "qwen", "llama", "mistral", "gemma")
ROLE_MAP = {
    "orchestration": "orchestrator-editor",
    "reasoning": "reasoning-investigator",
    "code": "code-executor",
    "visual": "visual-evaluator",
    "research": "source-researcher",
    "verification": "independent-verifier",
}


def yes(value: str) -> bool:
    return value.lower() in {"yes", "y", "true", "1"}


def choose_model_profile(args: argparse.Namespace) -> tuple[str, str, list[str]]:
    reasons: list[str] = []
    if args.model_profile != "auto":
        return args.model_profile, "explicit-user-or-repo-override", [
            f"explicit model profile selected: {args.model_profile}"
        ]

    model_name = args.model_name.lower().strip()
    frontier_hint = any(alias in model_name for alias in FRONTIER_ALIASES)
    portable_hint = any(alias in model_name for alias in PORTABLE_ALIASES)

    if args.capability_tier == "frontier" or frontier_hint:
        if args.harness_maturity == "strong":
            reasons.append("frontier capability plus a strong harness supports compact routing")
            return "frontier-compact", "capability-or-model-hint", reasons
        reasons.append("frontier model hint lacks a strong verified harness")
        return "portable-guided", "safe-fallback", reasons

    if args.capability_tier == "portable" or portable_hint:
        reasons.append("portable or open-weight model hint benefits from explicit phase contracts")
        return "portable-guided", "capability-or-model-hint", reasons

    reasons.append("unknown model-harness capability defaults to portable guidance")
    return "portable-guided", "safe-fallback", reasons


def choose_capability_role(args: argparse.Namespace) -> tuple[str, str]:
    if args.task_role != "auto":
        return ROLE_MAP[args.task_role], "explicit-user-or-project-route"
    if args.work_type in {"review", "release"}:
        return "independent-verifier", "work-shape"
    if args.work_type == "research":
        return "source-researcher", "work-shape"
    if args.work_type in {"architecture", "migration"}:
        return "reasoning-investigator", "work-shape"
    if args.work_type == "new-project":
        return "orchestrator-editor", "work-shape"
    return "code-executor", "work-shape"


def choose_execution_route(
    args: argparse.Namespace, capability_role: str, broad_scope: bool
) -> dict:
    reasons: list[str] = []
    conflicts: list[str] = []
    delegate = False
    subagent_role = "none"
    subagent_count = 0

    auto_fresh_verifier = (
        args.risk == "high"
        and (broad_scope or args.work_type in {"review", "release", "migration"})
    )
    fresh_verifier = args.verification_independence == "required" or (
        args.verification_independence == "auto" and auto_fresh_verifier
    )
    if args.delegation_shape == "independent-review":
        fresh_verifier = True

    if args.delegation_shape == "main-only":
        reasons.append("explicit main-only route disables execution delegation")
        if fresh_verifier:
            conflicts.append("independent verification is required but delegation is main-only")
    elif args.delegation_shape == "exploration":
        delegate = True
        subagent_role = "source-researcher"
        subagent_count = max(1, min(2, args.independent_axes or 1))
        reasons.append("explicit exploration route uses bounded read-only workers")
    elif args.delegation_shape == "specialist":
        delegate = True
        subagent_role = capability_role
        subagent_count = 1
        reasons.append("explicit specialist route delegates the selected capability role")
    elif args.delegation_shape == "parallel-independent":
        delegate = True
        subagent_role = capability_role
        subagent_count = max(1, min(2, args.independent_axes or 2))
        reasons.append("explicit independent axes permit bounded parallel delegation")
    elif args.delegation_shape == "independent-review":
        delegate = True
        subagent_role = "independent-verifier"
        subagent_count = 1
        reasons.append("explicit independent review uses a fresh verifier")
    elif args.coordination_cost != "high" and args.raw_information_volume == "high":
        delegate = True
        subagent_role = "source-researcher"
        subagent_count = max(1, min(2, args.independent_axes or 1))
        reasons.append("high raw-information volume justifies bounded exploration")
    elif args.coordination_cost != "high" and args.independent_axes >= 2:
        delegate = True
        subagent_role = capability_role
        subagent_count = min(2, args.independent_axes)
        reasons.append("multiple independent axes exceed expected coordination cost")
    elif (
        args.coordination_cost != "high"
        and yes(args.multi_agent)
        and args.scope != "single-file"
    ):
        delegate = True
        subagent_role = capability_role
        subagent_count = 1
        reasons.append("explicit multi-agent request permits one bounded specialist")
    elif fresh_verifier:
        delegate = True
        subagent_role = "independent-verifier"
        subagent_count = 1
        reasons.append("fresh verification is the only justified delegation")
    else:
        reasons.append("one main owner is cheaper and sufficient for this task shape")

    verifier_is_delegate = fresh_verifier and subagent_role == "independent-verifier"
    if fresh_verifier:
        reasons.append("risk or explicit policy requires fresh-context verification")

    reuse_worker = (
        delegate
        and subagent_role != "independent-verifier"
        and args.worker_reuse == "reuse-related"
    )
    if reuse_worker:
        reasons.append("related objective and context permit worker continuation")
    elif args.worker_reuse == "reuse-related" and subagent_role == "independent-verifier":
        conflicts.append("independent verification cannot reuse the implementation worker")
    elif args.worker_reuse == "fresh":
        reasons.append("changed or isolated context requires a fresh worker")

    requested_model = args.requested_model.strip() or None
    model_request = "none"
    if requested_model:
        model_request = "request-if-exposed-by-active-harness"
        reasons.append("concrete model request is conditional on runtime availability")

    verification_route = "fresh-independent-verifier" if fresh_verifier else "main-agent-plus-executable-verifiers"
    if conflicts:
        verification_route = "unsatisfied-routing-constraint"

    return {
        "execution_owner": "main-agent-orchestrator",
        "capability_role": capability_role,
        "delegate": delegate,
        "subagent_role": subagent_role,
        "subagent_count": subagent_count,
        "reuse_worker": reuse_worker,
        "worker_reuse_policy": (
            "reuse-related-handle" if reuse_worker else "fresh-or-main-owner"
        ),
        "fresh_verifier": fresh_verifier,
        "verifier_is_execution_delegate": verifier_is_delegate,
        "verification_route": verification_route,
        "requested_model": requested_model,
        "model_request": model_request,
        "fallback_if_model_unavailable": (
            "preserve the capability role, use the nearest exposed model, "
            "or keep the main agent; disclose the fallback"
        ),
        "coordination_cost_assumption": args.coordination_cost,
        "routing_conflicts": conflicts,
        "routing_reasons": reasons,
    }


def recommend(args: argparse.Namespace) -> dict:
    modes: list[str] = []
    overlays: list[str] = []
    references: list[str] = []
    reasons: list[str] = []
    loop_decision = "not-requested"

    profile, profile_source, profile_reasons = choose_model_profile(args)
    reasons.extend(profile_reasons)
    if args.model_profile == "auto":
        references.append("references/model-capability-profiles.md")

    capability_role, capability_role_source = choose_capability_role(args)
    broad_scope = args.scope in {"cross-module", "project", "unknown"}
    execution_route = choose_execution_route(args, capability_role, broad_scope)
    reasons.extend(execution_route["routing_reasons"])
    routing_signal = (
        execution_route["delegate"]
        or execution_route["fresh_verifier"]
        or args.task_role != "auto"
        or args.worker_reuse != "auto"
        or bool(args.requested_model.strip())
    )
    if routing_signal:
        references.append("references/project-model-routing.md")

    if yes(args.loop_request):
        references.append("references/loop-auto-mode.md")
        if args.quantifiable == "no":
            loop_decision = "refuse-loop-fallback-ordinary-task"
            reasons.append("loop requested but reliable quantified verification is unavailable")
        elif args.quantifiable == "partial":
            loop_decision = "design-verifier-before-loop"
            overlays.append("auto-loop-gate")
            reasons.append("loop verification needs a stronger quantified target")
        else:
            loop_decision = "allow-bounded-loop"
            overlays.append("auto-loop-mode")
            reasons.append("loop has a repeatable quantified verifier")

    high_uncertainty = args.risk == "high" or args.scope == "unknown"
    if high_uncertainty:
        overlays.append("uncertainty-decision-trace")
        references.append("references/uncertainty-and-decision-trace.md")
        reasons.append("risk or unknown scope requires blind-spot and decision tracking")

    agent_system = yes(args.agent_system) or args.work_type == "agent-system"

    if args.work_type in {"review", "release"}:
        modes.append("review-and-quality-gates")
        references.append("references/review-and-quality.md")
        reasons.append("review or release work needs spec, standards, verification, and residual-risk gates")

    if agent_system:
        modes.append("agent-system-engineering")
        references.append("references/agent-system-engineering.md")
        reasons.append("tools, state, handoffs, memory, or agent topology need explicit contracts")

    if broad_scope or args.work_type in {"new-project", "architecture", "migration"} or (
        args.work_type == "feature" and args.scope != "single-file"
    ):
        modes.append("spec-driven-development")
        references.append("references/spec-driven-development.md")
        reasons.append("scope or novelty warrants a written source of truth")

    if yes(args.user_facing):
        overlays.append("behavior-acceptance-driven-development")
        references.append("references/acceptance-bdd.md")
        reasons.append("user-visible behavior needs acceptance scenarios")

    if args.determinism == "deterministic" and args.work_type in {
        "bug", "feature", "refactor", "library", "migration"
    }:
        overlays.append("test-driven-development")
        references.append("references/test-driven-development.md")
        reasons.append("deterministic behavior can be verified at a public seam")

    if args.determinism in {"llm", "probabilistic", "semantic"} or agent_system:
        if "eval-driven-development" not in modes:
            modes.append("eval-driven-development")
        references.append("references/eval-driven-development.md")
        reasons.append("probabilistic or agent behavior needs multi-run eval evidence")

    if yes(args.framework_sensitive):
        overlays.append("source-driven-development")
        references.append("references/source-driven-development.md")
        reasons.append("framework or API correctness depends on current official docs")

    if args.work_type in {"architecture", "refactor", "migration"} or args.scope == "cross-module":
        overlays.append("architecture-domain-design")
        references.append("references/architecture-and-domain.md")
        reasons.append("module boundaries or domain language may change")

    if yes(args.multi_agent) or args.delivery in {"issues", "prd"}:
        overlays.append("issue-delivery")
        references.append("references/issue-delivery.md")
        reasons.append("work needs explicit handoff-ready vertical slices")

    if not modes:
        modes.append("direct-implementation-with-quality-gate")
        reasons.append("small clear work does not require a heavier lifecycle")

    ordered_modes = list(dict.fromkeys(modes + overlays))
    ordered_refs = list(dict.fromkeys(references))
    process_gate = (
        args.risk == "high"
        or broad_scope
        or yes(args.loop_request)
        or yes(args.multi_agent)
        or execution_route["delegate"]
        or execution_route["fresh_verifier"]
    )
    if len(ordered_modes) > 1:
        ordered_refs.insert(0, "references/workflow-map.md")

    return {
        "model_profile": profile,
        "model_profile_source": profile_source,
        "capability_role_source": capability_role_source,
        "primary_mode": modes[0],
        "recommended_modes": ordered_modes,
        "required_references": list(dict.fromkeys(ordered_refs)),
        "loop_decision": loop_decision,
        "repository_grounding_required": args.work_type != "research",
        "process_discipline_gate": process_gate,
        "execution_route": execution_route,
        "reasons": reasons,
        "decision_trace_required": process_gate or len(ordered_modes) > 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-type", default="feature", choices=[
        "new-project", "feature", "bug", "refactor", "architecture", "migration",
        "library", "agent-system", "prototype", "review", "release", "research"
    ])
    parser.add_argument("--determinism", default="deterministic", choices=[
        "deterministic", "llm", "probabilistic", "semantic", "unknown"
    ])
    parser.add_argument("--user-facing", default="no")
    parser.add_argument("--scope", default="single-file", choices=[
        "single-file", "single-module", "cross-module", "project", "unknown"
    ])
    parser.add_argument("--risk", default="medium", choices=["low", "medium", "high"])
    parser.add_argument("--framework-sensitive", default="no")
    parser.add_argument("--agent-system", default="no")
    parser.add_argument("--multi-agent", default="no")
    parser.add_argument("--delivery", default="none", choices=["none", "prd", "issues"])
    parser.add_argument("--loop-request", default="no")
    parser.add_argument("--quantifiable", default="yes", choices=["yes", "partial", "no"])
    parser.add_argument("--model-name", default="")
    parser.add_argument("--model-profile", default="auto", choices=[
        "auto", "frontier-compact", "portable-guided"
    ])
    parser.add_argument("--capability-tier", default="auto", choices=[
        "auto", "frontier", "portable"
    ])
    parser.add_argument("--harness-maturity", default="unknown", choices=[
        "unknown", "basic", "partial", "strong"
    ])
    parser.add_argument("--task-role", default="auto", choices=[
        "auto", "orchestration", "reasoning", "code", "visual", "research", "verification"
    ])
    parser.add_argument("--delegation-shape", default="auto", choices=[
        "auto", "main-only", "exploration", "specialist", "parallel-independent",
        "independent-review"
    ])
    parser.add_argument("--raw-information-volume", default="low", choices=[
        "low", "medium", "high"
    ])
    parser.add_argument("--independent-axes", type=int, default=0, choices=range(0, 4))
    parser.add_argument("--worker-reuse", default="auto", choices=[
        "auto", "reuse-related", "fresh", "unavailable"
    ])
    parser.add_argument("--verification-independence", default="auto", choices=[
        "auto", "required", "not-required"
    ])
    parser.add_argument("--coordination-cost", default="medium", choices=[
        "low", "medium", "high"
    ])
    parser.add_argument("--requested-model", default="")
    print(json.dumps(recommend(parser.parse_args()), indent=2))


if __name__ == "__main__":
    main()
