import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.routed_suite_report import build_routed_suite_report


class TestRoutedSuiteReport(unittest.TestCase):
    def test_build_routed_suite_report(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "suite_summaries" / "suite_v1_0_test").mkdir(parents=True)
            (root / "reports" / "holdout").mkdir(parents=True)
            (root / "reports" / "champion_challenger").mkdir(parents=True)
            (root / "ledgers").mkdir(parents=True)

            original = {
                "suite_name": "suite_v1_0",
                "overall_classification": "PBA-C",
                "runs": [
                    {
                        "domain_id": "temperature_like",
                        "classification": "PBA-C",
                        "baseline_result": "baseline_advantage",
                    },
                    {
                        "domain_id": "oscillatory_signal",
                        "classification": "PBA-A",
                        "baseline_result": "pba_advantage",
                    },
                ],
            }
            (root / "reports" / "suite_summaries" / "suite_v1_0_test" / "suite_summary.json").write_text(json.dumps(original), encoding="utf-8")

            holdout = {
                "version": "PBSA-v1.3",
                "overall_classification": "PBA-D",
                "regime_map": {
                    "holdout_noisy_recovery": {
                        "domain_id": "holdout_noisy_recovery",
                        "primary_regime": "noisy",
                        "secondary_regimes": ["baseline_advantage"],
                    }
                },
            }
            (root / "reports" / "holdout" / "latest_holdout_summary.json").write_text(json.dumps(holdout), encoding="utf-8")

            cc = {
                "version": "PBSA-v1.4",
                "decision": "route_by_regime",
                "promotion_status": "no_automatic_promotion",
            }
            (root / "reports" / "champion_challenger" / "latest_champion_challenger_report.json").write_text(json.dumps(cc), encoding="utf-8")

            result = build_routed_suite_report(root)
            self.assertEqual(result["status"], "complete")
            self.assertEqual(result["decision"], "route_by_regime")
            self.assertFalse(result["automatic_kernel_replacement_allowed"])
            self.assertTrue(Path(result["routed_suite_report_json"]).exists())

    def test_report_has_expected_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "suite_summaries" / "suite_v1_0_test").mkdir(parents=True)
            (root / "reports" / "holdout").mkdir(parents=True)
            (root / "reports" / "champion_challenger").mkdir(parents=True)
            (root / "ledgers").mkdir(parents=True)

            (root / "reports" / "suite_summaries" / "suite_v1_0_test" / "suite_summary.json").write_text(json.dumps({"runs": []}), encoding="utf-8")
            (root / "reports" / "holdout" / "latest_holdout_summary.json").write_text(json.dumps({"regime_map": {}}), encoding="utf-8")
            (root / "reports" / "champion_challenger" / "latest_champion_challenger_report.json").write_text(json.dumps({"decision": "route_by_regime"}), encoding="utf-8")

            result = build_routed_suite_report(root)
            report = json.loads(Path(result["routed_suite_report_json"]).read_text(encoding="utf-8"))
            self.assertEqual(report["version"], "PBSA-v2.0")
            self.assertEqual(report["route_policy"], "regime_route_policy_v2_0")
            self.assertFalse(report["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
