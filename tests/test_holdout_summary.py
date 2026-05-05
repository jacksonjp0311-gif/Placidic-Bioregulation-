import json
import tempfile
import unittest
from pathlib import Path

from pba.core.domain import DomainConfig
from pba.evidence.holdout_summary import build_regime_coverage, compile_holdout_summary


class TestHoldoutSummary(unittest.TestCase):
    def test_holdout_domain_configs_are_valid(self):
        paths = [
            "configs/domains/holdout_direct_recovery.json",
            "configs/domains/holdout_delayed_pulse.json",
            "configs/domains/holdout_noisy_recovery.json",
            "configs/domains/holdout_mixed_oscillation.json",
        ]
        for path in paths:
            domain = DomainConfig.from_file(path)
            self.assertIn("not_medical", domain.non_claim_locks)
            self.assertIn("not_biological_law", domain.non_claim_locks)
            self.assertIn("not_mechanism_proof", domain.non_claim_locks)

    def test_regime_coverage_matrix(self):
        coverage = build_regime_coverage({
            "a": {"primary_regime": "direct_recovery", "secondary_regimes": ["cusp_risk"], "risk_overlays": ["cusp_risk"]},
            "b": {"primary_regime": "noisy", "secondary_regimes": ["baseline_advantage"], "risk_overlays": []},
        })
        self.assertIn("direct_recovery", coverage["primary_regimes"])
        self.assertIn("noisy", coverage["primary_regimes"])
        self.assertIn("cusp_risk", coverage["secondary_overlays"])

    def test_compile_holdout_summary_from_minimal_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run = root / "runs" / "run_holdout"
            run.mkdir(parents=True)
            (root / "reports" / "suite_summaries" / "suite_holdout_v1_3_test").mkdir(parents=True)
            (root / "ledgers").mkdir()
            (root / "reports" / "holdout").mkdir(parents=True)

            (run / "domain_config.json").write_text(json.dumps({
                "domain_id": "holdout_noisy_recovery",
                "non_claim_locks": ["not_medical", "not_biological_law", "not_mechanism_proof"]
            }), encoding="utf-8")
            (run / "pba_metrics.json").write_text(json.dumps({"cumulative_deviation": 1.0, "cusp_warnings": 3}), encoding="utf-8")
            (run / "metric_comparison.json").write_text(json.dumps({"baseline_result": "baseline_advantage", "best_baseline": "proportional_feedback"}), encoding="utf-8")
            (run / "classification.json").write_text(json.dumps({"classification": "PBA-C"}), encoding="utf-8")

            suite = {
                "suite_name": "suite_holdout_v1_3",
                "overall_classification": "PBA-C",
                "classification_counts": {"PBA-A": 0, "PBA-B": 0, "PBA-C": 1, "PBA-D": 0, "PBA-E": 0},
                "runs": [{"run_dir": str(run), "domain_id": "holdout_noisy_recovery"}],
            }
            summary_path = root / "reports" / "suite_summaries" / "suite_holdout_v1_3_test" / "suite_summary.json"
            summary_path.write_text(json.dumps(suite), encoding="utf-8")

            result = compile_holdout_summary(root, summary_path)
            self.assertEqual(result["status"], "complete")
            self.assertEqual(result["decision"], "preserve_champion")
            self.assertTrue(Path(result["holdout_summary_json"]).exists())


if __name__ == "__main__":
    unittest.main()
