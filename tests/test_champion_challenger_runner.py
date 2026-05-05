import json
import tempfile
import unittest
from pathlib import Path

from pba.evolution.champion_challenger_runner import run_candidate_comparison
from pba.evidence.champion_challenger_report import build_champion_challenger_report


class TestChampionChallengerRunner(unittest.TestCase):
    def test_candidate_comparison_packet(self):
        rows = [
            {
                "domain_id": "temperature_like",
                "primary_regime": "direct_recovery",
                "secondary_regimes": ["baseline_advantage"],
                "champion_score": 10.0,
                "champion_classification": "PBA-D",
            }
        ]
        packet = run_candidate_comparison(rows)
        self.assertEqual(packet["domain_count"], 1)
        self.assertIn("best_by_domain", packet)
        self.assertIn("candidate_classification_counts", packet)

    def test_report_generation_preserves_no_auto_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "suite_summaries" / "suite_v1_0_test").mkdir(parents=True)
            (root / "reports" / "holdout").mkdir(parents=True)
            (root / "ledgers").mkdir(parents=True)

            original = {
                "suite_name": "suite_v1_0",
                "overall_classification": "PBA-C",
                "runs": [
                    {
                        "domain_id": "temperature_like",
                        "classification": "PBA-C",
                        "baseline_result": "baseline_advantage",
                        "pba_score": 10.0,
                    }
                ],
            }
            (root / "reports" / "suite_summaries" / "suite_v1_0_test" / "suite_summary.json").write_text(json.dumps(original), encoding="utf-8")

            holdout = {
                "version": "PBSA-v1.3",
                "overall_classification": "PBA-D",
                "regime_map": {
                    "holdout_noisy_recovery": {
                        "primary_regime": "noisy",
                        "secondary_regimes": ["baseline_advantage"],
                        "features": {"cumulative_deviation": 10.0},
                    }
                },
            }
            (root / "reports" / "holdout" / "latest_holdout_summary.json").write_text(json.dumps(holdout), encoding="utf-8")

            result = build_champion_challenger_report(root)
            self.assertEqual(result["status"], "complete")
            self.assertFalse(result["automatic_kernel_replacement_allowed"])
            self.assertTrue(Path(result["champion_challenger_report_json"]).exists())


if __name__ == "__main__":
    unittest.main()
