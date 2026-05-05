import json
import tempfile
import unittest
from pathlib import Path

from pba.validation.control_policies import CONTROL_POLICIES, score_domain
from pba.validation.routed_validation_runner import run_routed_validation
from pba.evidence.routed_validation_report import build_routed_validation_report


class TestRoutedValidation(unittest.TestCase):
    def test_control_policies_exist(self):
        self.assertIn("champion_only", CONTROL_POLICIES)
        self.assertIn("baseline_only", CONTROL_POLICIES)
        self.assertIn("candidate_only", CONTROL_POLICIES)
        self.assertIn("reject_manual_review", CONTROL_POLICIES)

    def test_score_domain_emits_advantage(self):
        score = score_domain({
            "domain_id": "temperature_like",
            "selected_route": "baseline_proportional_route",
            "route_family": "baseline",
            "manual_review_required": False,
        })
        self.assertIn("routed_score", score)
        self.assertIn("control_scores", score)
        self.assertIn("route_advantage", score)

    def test_build_routed_validation_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "routing").mkdir(parents=True)
            (root / "ledgers").mkdir(parents=True)

            routed = {
                "routed_suite_report_id": "test",
                "version": "PBSA-v2.0",
                "route_policy": "regime_route_policy_v2_0",
                "route_decisions": [
                    {
                        "domain_id": "temperature_like",
                        "selected_route": "baseline_proportional_route",
                        "route_family": "baseline",
                        "manual_review_required": False,
                    },
                    {
                        "domain_id": "oscillatory_signal",
                        "selected_route": "champion_pba_route",
                        "route_family": "champion",
                        "manual_review_required": False,
                    },
                ],
                "decision": "route_by_regime",
            }
            (root / "reports" / "routing" / "latest_routed_suite_report.json").write_text(json.dumps(routed), encoding="utf-8")

            result = build_routed_validation_report(root)
            self.assertEqual(result["status"], "complete")
            self.assertIn(result["decision"], {"validate_routing", "validate_with_caution", "preserve_routing_for_review", "reject_routing"})
            self.assertFalse(result["automatic_kernel_replacement_allowed"])
            self.assertTrue(Path(result["routed_validation_report_json"]).exists())

    def test_runner_emits_required_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "routing").mkdir(parents=True)
            routed = {
                "route_policy": "regime_route_policy_v2_0",
                "route_decisions": [
                    {
                        "domain_id": "holdout_noisy_recovery",
                        "selected_route": "candidate_noisy_guard_route_pending_review",
                        "route_family": "candidate",
                        "manual_review_required": True,
                    }
                ],
            }
            (root / "reports" / "routing" / "latest_routed_suite_report.json").write_text(json.dumps(routed), encoding="utf-8")
            result = run_routed_validation(root)
            self.assertEqual(result["version"], "PBSA-v2.1")
            self.assertIn("routed_advantage", result)
            self.assertIn("route_preservation_score", result)
            self.assertFalse(result["automatic_kernel_replacement_allowed"])


if __name__ == "__main__":
    unittest.main()
