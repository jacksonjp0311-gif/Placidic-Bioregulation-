import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.external_validation_report import build_external_validation_report
from pba.external.external_validation_runner import run_external_validation


class TestExternalValidationReport(unittest.TestCase):
    def _setup_tmp_root(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)

        (root / "configs" / "external_domains").mkdir(parents=True)
        (root / "configs" / "validation").mkdir(parents=True)
        (root / "reports" / "validation").mkdir(parents=True)
        (root / "reports" / "routing").mkdir(parents=True)
        (root / "ledgers").mkdir(parents=True)

        domain = {
            "domain_id": "external_test",
            "family": "external_test_family",
            "primary_regime": "direct_recovery",
            "secondary_regimes": ["baseline_advantage"],
            "external": True,
        }
        (root / "configs" / "external_domains" / "external_test.json").write_text(json.dumps(domain), encoding="utf-8")

        suite = {
            "external_domain_configs": ["configs/external_domains/external_test.json"]
        }
        (root / "configs" / "external_validation_suite_v2_2.json").write_text(json.dumps(suite), encoding="utf-8")

        validation = {
            "version": "PBSA-v2.1",
            "routed_advantage": 0.56,
            "route_preservation_score": 1.0,
            "route_failure_count": 0,
            "route_failure_surface": [],
        }
        (root / "reports" / "validation" / "latest_routed_validation_report.json").write_text(json.dumps(validation), encoding="utf-8")

        routed = {
            "route_decisions": [
                {
                    "domain_id": "temperature_like",
                    "selected_route": "baseline_proportional_route",
                    "route_family": "baseline",
                }
            ]
        }
        (root / "reports" / "routing" / "latest_routed_suite_report.json").write_text(json.dumps(routed), encoding="utf-8")
        return root

    def test_run_external_validation(self):
        root = self._setup_tmp_root()
        result = run_external_validation(root)
        self.assertEqual(result["version"], "PBSA-v2.2")
        self.assertIn("advantage_drift", result)
        self.assertIn("external_failure_surface", result)
        self.assertFalse(result["automatic_kernel_replacement_allowed"])

    def test_build_external_validation_report(self):
        root = self._setup_tmp_root()
        result = build_external_validation_report(root)
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "external_validate_routing",
            "external_validate_with_caution",
            "external_preserve_routing_for_review",
            "external_reject_routing",
        })
        self.assertTrue(Path(result["external_validation_report_json"]).exists())

    def test_external_report_preserves_no_replacement(self):
        root = self._setup_tmp_root()
        result = build_external_validation_report(root)
        report = json.loads(Path(result["external_validation_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v2.2")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
