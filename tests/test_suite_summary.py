import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.suite_summary import compile_suite_summary


class TestSuiteSummary(unittest.TestCase):
    def test_suite_summary_mixed_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports").mkdir()

            runs = []
            payloads = [
                ("domain_a", "PBA-A", "pba_advantage", 1.0, 2.0),
                ("domain_b", "PBA-C", "baseline_advantage", 3.0, 2.0),
            ]

            for idx, (domain, label, result, pba_score, base_score) in enumerate(payloads):
                rd = root / "runs" / f"run_{idx}"
                rd.mkdir(parents=True)
                runs.append(str(rd))

                (rd / "classification.json").write_text(json.dumps({
                    "classification": label,
                    "PBAScore": 1.0 if label == "PBA-A" else 0.25,
                    "baseline_result": result,
                    "identifiability_status": "stable",
                    "downgrade_path": "test",
                    "non_claim_locks_preserved": True
                }), encoding="utf-8")

                (rd / "metric_comparison.json").write_text(json.dumps({
                    "primary_metric": "cumulative_deviation",
                    "pba_score": pba_score,
                    "best_baseline": "proportional_feedback",
                    "best_baseline_score": base_score,
                    "baseline_result": result
                }), encoding="utf-8")

                (rd / "domain_config.json").write_text(json.dumps({
                    "domain_id": domain
                }), encoding="utf-8")

                (rd / "identifiability_report.json").write_text(json.dumps({
                    "status": "stable"
                }), encoding="utf-8")

            summary = compile_suite_summary(root, runs, suite_name="test_suite")
            self.assertEqual(summary["overall_classification"], "PBA-C")
            self.assertEqual(summary["classification_counts"]["PBA-A"], 1)
            self.assertEqual(summary["classification_counts"]["PBA-C"], 1)
            self.assertTrue(Path(summary["suite_summary_json"]).exists())
            self.assertTrue(Path(summary["suite_summary_md"]).exists())


if __name__ == "__main__":
    unittest.main()