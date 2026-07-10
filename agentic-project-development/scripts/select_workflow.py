#!/usr/bin/env python3
"""Recommend project-development modes and model instruction density."""

from __future__ import annotations

import argparse
import json


FRONTIER_ALIASES = ("gpt-5.6-sol", "fable5", "fable-5")
PORTABLE_ALIASES = ("kimi", "deepseek", "qwen", "llama", "mistral", "gemma")


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
    broad_scope = args.scope in {"cross-module", "project", "unknown"}

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
        args.risk == "high" or broad_scope or yes(args.loop_request) or yes(args.multi_agent)
    )
    if len(ordered_modes) > 1:
        ordered_refs.insert(0, "references/workflow-map.md")

    return {
        "model_profile": profile,
        "model_profile_source": profile_source,
        "primary_mode": modes[0],
        "recommended_modes": ordered_modes,
        "required_references": list(dict.fromkeys(ordered_refs)),
        "loop_decision": loop_decision,
        "repository_grounding_required": args.work_type != "research",
        "process_discipline_gate": process_gate,
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
    print(json.dumps(recommend(parser.parse_args()), indent=2))


if __name__ == "__main__":
    main()
