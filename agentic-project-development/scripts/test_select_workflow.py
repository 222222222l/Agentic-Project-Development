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


if __name__ == "__main__":
    unittest.main()
