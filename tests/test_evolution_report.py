import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.evolution_report import build_evolution_report


class TestEvolutionReport(unittest.TestCase):
    def test_builds_evolution_report_from_minimal_suite_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            summary_dir = root / "reports" / "suite_summaries" / "suite_test"
            summary_dir.mkdir(parents=True)
            (root / "configs").mkdir()
            (root / "ledgers").mkdir()
            (root / "reports" / "evolution").mkdir(parents=True)

            suite = {
                "overall_classification": "PBA-C",
                "overall_summary": "Mixed evidence.",
                "classification_counts": {"PBA-A": 1, "PBA-B": 0, "PBA-C": 2, "PBA-D": 0, "PBA-E": 0},
                "mean_pba_score": 14.2,
                "runs": [
                    {
                        "domain_id": "temperature_like",
                        "classification": "PBA-C",
                        "baseline_result": "baseline_advantage",
                        "best_baseline": "proportional_feedback",
                        "pba_score": 14.0,
                        "best_baseline_score": 12.0,
                    },
                    {
                        "domain_id": "oscillatory_signal",
                        "classification": "PBA-A",
                        "baseline_result": "pba_advantage",
                        "best_baseline": "proportional_feedback",
                        "pba_score": 15.0,
                        "best_baseline_score": 19.0,
                    },
                ],
            }
            summary_path = summary_dir / "suite_summary.json"
            summary_path.write_text(json.dumps(suite), encoding="utf-8")

            policy_path = root / "configs" / "evolution_policy.json"
            policy_path.write_text(json.dumps({"mode": "diagnostic_first", "kernel_mutation_allowed": False}), encoding="utf-8")

            result = build_evolution_report(root, suite_summary_path=summary_path, policy_path=policy_path)
            self.assertEqual(result["status"], "complete")
            self.assertEqual(result["decision"], "preserve_champion")
            self.assertTrue(Path(result["evolution_report_json"]).exists())


if __name__ == "__main__":
    unittest.main()
