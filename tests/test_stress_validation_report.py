import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.stress_validation_report import build_stress_validation_report
from pba.stress.stress_failure_surface import build_stress_failure_surface
from pba.stress.stress_route_drift import crash_rate, safe_fail_score
from pba.stress.stress_validation_runner import run_stress_validation


class TestStressValidationReport(unittest.TestCase):
    def _setup_tmp_root(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)

        (root / "configs" / "stress_domains").mkdir(parents=True)
        (root / "configs" / "validation").mkdir(parents=True)
        (root / "reports" / "external_validation").mkdir(parents=True)
        (root / "ledgers").mkdir(parents=True)

        stress = {
            "domain_id": "stress_bad",
            "family": "contradictory_regime_stress",
            "stress_type": "contradictory_regime",
            "primary_regime": "unknown",
            "secondary_regimes": ["baseline_advantage", "pba_advantage", "low_confidence"],
            "unsafe": True,
            "stress": True,
        }
        (root / "configs" / "stress_domains" / "stress_bad.json").write_text(json.dumps(stress), encoding="utf-8")

        suite = {"stress_domain_configs": ["configs/stress_domains/stress_bad.json"]}
        (root / "configs" / "stress_validation_suite_v2_3.json").write_text(json.dumps(suite), encoding="utf-8")

        external = {
            "version": "PBSA-v2.2",
            "external_routed_advantage": 0.2,
            "external_failure_surface": [],
        }
        (root / "reports" / "external_validation" / "latest_external_validation_report.json").write_text(json.dumps(external), encoding="utf-8")
        return root

    def test_safe_fail_and_crash_metrics(self):
        decisions = [
            {"unsafe": True, "route_family": "reject", "manual_review_required": True, "crash": False},
            {"unsafe": True, "route_family": "reject", "manual_review_required": True, "crash": False},
        ]
        self.assertEqual(safe_fail_score(decisions), 1.0)
        self.assertEqual(crash_rate(decisions), 0.0)

    def test_stress_failure_surface(self):
        failures = build_stress_failure_surface(
            [{"domain_id": "d", "family": "f", "stress_type": "malformed_input", "route_family": "reject", "failure_reason": "malformed_input_rejected"}],
            [{"domain_id": "d", "route_advantage": 0.0}],
        )
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["failure_reason"], "stress_malformed_input_rejected")

    def test_run_stress_validation(self):
        root = self._setup_tmp_root()
        result = run_stress_validation(root)
        self.assertEqual(result["version"], "PBSA-v2.3")
        self.assertIn("safe_fail_score", result)
        self.assertEqual(result["crash_rate"], 0.0)
        self.assertFalse(result["automatic_kernel_replacement_allowed"])

    def test_build_stress_validation_report(self):
        root = self._setup_tmp_root()
        result = build_stress_validation_report(root)
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "stress_validate_routing",
            "stress_validate_with_caution",
            "stress_preserve_routing_for_review",
            "stress_reject_routing",
        })
        self.assertTrue(Path(result["stress_validation_report_json"]).exists())


if __name__ == "__main__":
    unittest.main()
