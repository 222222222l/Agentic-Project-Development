#!/usr/bin/env python3
"""Regression tests for project workflow and execution routing."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


SELECTOR = Path(__file__).with_name("select_workflow.py")


def route(*args: str) -> dict:
    result = subprocess.run(
        [sys.executable, str(SELECTOR), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


class WorkflowRoutingTests(unittest.TestCase):
    def test_small_task_stays_with_main_agent(self) -> None:
        result = route("--work-type", "feature", "--scope", "single-file", "--risk", "low")
        execution = result["execution_route"]
        self.assertFalse(execution["delegate"])
        self.assertFalse(execution["fresh_verifier"])
        self.assertEqual(execution["capability_role"], "code-executor")
        self.assertTrue(result["lightweight_path"])
        self.assertFalse(result["decision_trace_required"])
        self.assertEqual(result["required_references"], [])

    def test_names_do_not_override_observed_capability(self) -> None:
        for name in ("gpt-5.6-sol", "fable5", "qwen", "unknown-future-model"):
            with self.subTest(name=name):
                result = route("--model-name", name, "--harness-maturity", "strong")
                self.assertEqual(result["model_profile"], "portable-guided")
                capable = route(
                    "--model-name", name, "--capability-tier", "frontier",
                    "--harness-maturity", "strong",
                )
                self.assertEqual(capable["model_profile"], "frontier-compact")

    def test_explicit_profile_wins_and_weak_harness_falls_back(self) -> None:
        explicit = route("--model-profile", "frontier-compact")
        self.assertEqual(explicit["model_profile"], "frontier-compact")
        self.assertIn("references/model-capability-profiles.md", explicit["required_references"])
        weak = route("--capability-tier", "frontier", "--harness-maturity", "basic")
        self.assertEqual(weak["model_profile"], "portable-guided")

    def test_small_refactor_does_not_require_architecture_work(self) -> None:
        result = route("--work-type", "refactor", "--risk", "low")
        self.assertTrue(result["lightweight_path"])
        self.assertEqual(result["required_references"], [])
        self.assertFalse(result["decision_trace_required"])

    def test_delivery_request_is_not_a_lightweight_edit(self) -> None:
        result = route("--risk", "low", "--delivery", "prd")
        self.assertFalse(result["lightweight_path"])
        self.assertIn("references/issue-delivery.md", result["required_references"])

    def test_loop_does_not_assume_a_verifier(self) -> None:
        for quantifiable, decision in (
            (None, "design-verifier-before-loop"),
            ("yes", "allow-bounded-loop"),
            ("no", "refuse-loop-fallback-ordinary-task"),
        ):
            args = ["--loop-request", "yes"]
            if quantifiable:
                args.extend(["--quantifiable", quantifiable])
            result = route(*args)
            self.assertEqual(result["loop_decision"], decision)

    def test_long_work_preserves_state_without_claiming_loop_permission(self) -> None:
        result = route("--horizon", "long")
        self.assertEqual(result["state_tracking"], "dependencies-and-verifier-revisions")
        self.assertIn("references/loop-auto-mode.md", result["required_references"])
        self.assertEqual(result["loop_decision"], "not-requested")

    def test_each_bottleneck_routes_targeted_guidance(self) -> None:
        for bottleneck in ("retrieval", "context", "tools", "verification", "retry", "coordination"):
            result = route("--bottleneck", bottleneck, "--risk", "low")
            self.assertIn("references/efficient-execution.md", result["required_references"])
            self.assertFalse(result["lightweight_path"])

    def test_semantic_work_does_not_take_lightweight_path(self) -> None:
        result = route("--risk", "low", "--determinism", "semantic")
        self.assertFalse(result["lightweight_path"])
        self.assertIn("eval-driven-development", result["recommended_modes"])

    def test_forbidden_delegation_wins_over_exploration_request(self) -> None:
        result = route(
            "--delegation-policy", "forbidden", "--delegation-shape", "exploration",
            "--raw-information-volume", "high", "--independent-axes", "2",
        )
        self.assertFalse(result["execution_route"]["delegate"])
        self.assertTrue(result["execution_route"]["routing_conflicts"])

    def test_forbidden_delegation_exposes_required_review_conflict(self) -> None:
        result = route("--delegation-policy", "forbidden", "--verification-independence", "required")
        execution = result["execution_route"]
        self.assertFalse(execution["delegate"])
        self.assertEqual(execution["verification_route"], "unsatisfied-routing-constraint")

    def test_suggestion_is_not_authorization(self) -> None:
        result = route("--raw-information-volume", "high")
        execution = result["execution_route"]
        self.assertTrue(execution["route_is_recommendation"])
        self.assertEqual(execution["authorization_status"], "check-active-host-and-user-policy")

    def test_high_volume_independent_exploration_uses_two_workers(self) -> None:
        result = route(
            "--work-type", "feature",
            "--scope", "cross-module",
            "--raw-information-volume", "high",
            "--independent-axes", "2",
        )
        execution = result["execution_route"]
        self.assertTrue(execution["delegate"])
        self.assertEqual(execution["subagent_role"], "source-researcher")
        self.assertEqual(execution["subagent_count"], 2)

    def test_related_research_reuses_worker(self) -> None:
        result = route(
            "--work-type", "research",
            "--scope", "project",
            "--raw-information-volume", "high",
            "--worker-reuse", "reuse-related",
        )
        self.assertTrue(result["execution_route"]["reuse_worker"])

    def test_high_risk_review_uses_fresh_verifier(self) -> None:
        result = route(
            "--work-type", "review",
            "--scope", "project",
            "--risk", "high",
            "--verification-independence", "required",
        )
        execution = result["execution_route"]
        self.assertTrue(execution["delegate"])
        self.assertTrue(execution["fresh_verifier"])
        self.assertEqual(execution["subagent_role"], "independent-verifier")

    def test_main_only_conflict_is_visible(self) -> None:
        result = route(
            "--work-type", "review",
            "--scope", "project",
            "--risk", "high",
            "--delegation-shape", "main-only",
            "--verification-independence", "required",
        )
        execution = result["execution_route"]
        self.assertEqual(execution["verification_route"], "unsatisfied-routing-constraint")
        self.assertEqual(len(execution["routing_conflicts"]), 1)

    def test_unavailable_model_request_has_bounded_fallback(self) -> None:
        result = route(
            "--work-type", "architecture",
            "--scope", "project",
            "--delegation-shape", "specialist",
            "--requested-model", "unavailable-model-x",
        )
        execution = result["execution_route"]
        self.assertEqual(execution["model_request"], "request-if-exposed-by-active-harness")
        self.assertIn("nearest exposed model", execution["fallback_if_model_unavailable"])

    def test_skill_change_routes_governance_and_paired_evaluation(self) -> None:
        result = route("--work-type", "skill", "--scope", "single-module")
        self.assertEqual(result["primary_mode"], "skill-context-harness-governance")
        self.assertIn(
            "references/skill-context-harness-governance.md",
            result["required_references"],
        )
        self.assertIn(
            "references/agent-evaluation-standard.md",
            result["required_references"],
        )
        self.assertTrue(result["process_discipline_gate"])


if __name__ == "__main__":
    unittest.main()
