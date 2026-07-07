#!/usr/bin/env python3
"""Recommend project-development modes from coarse project traits."""

from __future__ import annotations

import argparse
import json


def yes(value: str) -> bool:
    return value.lower() in {"yes", "y", "true", "1"}


def recommend(args: argparse.Namespace) -> dict:
    modes: list[str] = []
    overlays: list[str] = []
    reasons: list[str] = []
    loop_decision = "not-requested"

    if yes(args.loop_request):
        if args.quantifiable == "no":
            loop_decision = "refuse-loop-fallback-ordinary-task"
            reasons.append("loop requested but reliable quantified verification is not available")
        elif args.quantifiable == "partial":
            loop_decision = "clarify-or-design-verifier-before-loop"
            overlays.append("auto-loop-gate")
            reasons.append("loop requested but verification needs a stronger quantified target")
        else:
            loop_decision = "allow-bounded-loop"
            overlays.append("auto-loop-mode")
            reasons.append("loop requested and reliable quantified verification is available")

    if args.scope in {"cross-module", "project", "unknown"} or args.work_type in {"new-project", "feature", "architecture"}:
        modes.append("spec-driven-development")
        reasons.append("scope or novelty warrants a written source of truth")

    if yes(args.user_facing):
        overlays.append("behavior-acceptance-driven-development")
        reasons.append("user-visible behavior should be expressed as acceptance scenarios")

    if args.determinism == "deterministic" and args.work_type in {"bug", "feature", "refactor", "library"}:
        overlays.append("test-driven-development")
        reasons.append("deterministic behavior can be verified at public seams")

    if args.determinism in {"llm", "probabilistic", "semantic"}:
        modes.append("eval-driven-development")
        reasons.append("semantic or probabilistic outputs need datasets and evaluators")

    if yes(args.framework_sensitive):
        overlays.append("source-driven-development")
        reasons.append("framework or API correctness depends on current official docs")

    if args.work_type in {"architecture", "refactor"} or args.scope == "cross-module":
        overlays.append("architecture-domain-design")
        reasons.append("module boundaries and domain language may change")

    if yes(args.multi_agent) or args.delivery in {"issues", "prd"}:
        overlays.append("issue-delivery")
        reasons.append("work should be sliced for handoff or multiple sessions")

    if not modes:
        modes.append("direct-implementation-with-quality-gate")
        reasons.append("small or clear task does not require a heavier lifecycle")

    ordered = []
    for item in modes + overlays:
        if item not in ordered:
            ordered.append(item)

    return {
        "primary_mode": modes[0],
        "recommended_modes": ordered,
        "loop_decision": loop_decision,
        "reasons": reasons,
        "decision_trace_required": yes(args.loop_request) or len(ordered) > 1 or args.scope != "single-file",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-type", default="feature", choices=[
        "new-project", "feature", "bug", "refactor", "architecture", "library", "review", "research"
    ])
    parser.add_argument("--determinism", default="deterministic", choices=[
        "deterministic", "llm", "probabilistic", "semantic", "unknown"
    ])
    parser.add_argument("--user-facing", default="no")
    parser.add_argument("--scope", default="single-file", choices=[
        "single-file", "single-module", "cross-module", "project", "unknown"
    ])
    parser.add_argument("--framework-sensitive", default="no")
    parser.add_argument("--multi-agent", default="no")
    parser.add_argument("--delivery", default="none", choices=["none", "prd", "issues"])
    parser.add_argument("--loop-request", default="no")
    parser.add_argument("--quantifiable", default="yes", choices=["yes", "partial", "no"])
    print(json.dumps(recommend(parser.parse_args()), indent=2))


if __name__ == "__main__":
    main()
