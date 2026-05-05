import json
import tempfile
import unittest
from pathlib import Path

from pba.evolution.candidate_spec import build_candidate_specs
from pba.evolution.candidate_readiness import build_candidate_readiness_report


class TestCandidateReadiness(unittest.TestCase):
    def test_candidate_specs_are_non_executable(self):
        holdout = {
            "regime_map": {
                "holdout_direct_recovery": {
                    "primary_regime": "direct_recovery",
                    "secondary_regimes": ["baseline_advantage", "cusp_risk"],
                },
                "holdout_mixed_oscillation": {
                    "primary_regime": "oscillatory",
                    "secondary_regimes": ["pba_advantage"],
                },
            }
        }
        specs = build_candidate_specs(holdout)
        self.assertGreaterEqual(len(specs), 2)
        for spec in specs:
            self.assertEqual(spec["status"], "specified_not_executable")
            self.assertIn("medical_claim", spec["forbidden_claims"])

    def test_candidate_readiness_report_preserves_champion(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "reports" / "holdout").mkdir(parents=True)
            (root / "ledgers").mkdir()

            holdout = {
                "holdout_summary_id": "PBSA-HOLDOUT-test",
                "version": "PBSA-v1.3",
                "regime_map": {
                    "holdout_direct_recovery": {
                        "primary_regime": "direct_recovery",
                        "secondary_regimes": ["baseline_advantage"],
                        "risk_overlays": [],
                    }
                }
            }
            holdout_path = root / "reports" / "holdout" / "latest_holdout_summary.json"
            holdout_path.write_text(json.dumps(holdout), encoding="utf-8")

            result = build_candidate_readiness_report(root, holdout_path)
            self.assertEqual(result["status"], "complete")
            self.assertEqual(result["decision"], "preserve_champion")
            self.assertFalse(result["candidate_execution_allowed"])
            self.assertTrue(Path(result["candidate_readiness_report_json"]).exists())

    def test_candidate_readiness_schema_has_next_required_step(self):
        holdout = {
            "regime_map": {
                "holdout_noisy_recovery": {
                    "primary_regime": "noisy",
                    "secondary_regimes": ["baseline_advantage"],
                }
            }
        }
        specs = build_candidate_specs(holdout)
        self.assertTrue(any(spec["candidate_id"] == "noisy_recovery_guard_candidate_v0" for spec in specs))


if __name__ == "__main__":
    unittest.main()
