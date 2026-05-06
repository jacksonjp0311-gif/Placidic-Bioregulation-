import json
import tempfile
import unittest
from pathlib import Path

from pba.calibration_thresholds.calibration_runner import run_calibration
from pba.evidence.calibration_report import build_calibration_report


class TestCalibrationReport(unittest.TestCase):
    def _setup_tmp_root(self) -> Path:
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = Path(tmp.name)

        (root / "configs" / "calibration").mkdir(parents=True)
        (root / "reports" / "validation").mkdir(parents=True)
        (root / "reports" / "external_validation").mkdir(parents=True)
        (root / "reports" / "stress_validation").mkdir(parents=True)
        (root / "ledgers").mkdir(parents=True)

        policy = {
            "weights": {
                "advantage": 1.0,
                "preservation": 1.0,
                "safe_fail": 1.5,
                "failure_penalty": 0.25,
                "overfitting_penalty": 0.5,
                "crash_penalty": 2.0,
                "manual_review_penalty": 0.05,
            },
            "minimums": {
                "safe_fail_score": 1.0,
                "crash_rate": 0.0,
                "preservation_score": 0.8,
            },
            "overfitting_tolerance": 0.75,
        }
        grid = {
            "values": {
                "route_confidence": [0.70],
                "safe_fail": [1.0],
                "contradiction_sensitivity": [0.85],
                "manual_review": [0.65],
                "advantage_cutoff": [0.0],
                "preservation_cutoff": [0.8],
            },
            "candidate_limit": 1,
        }

        (root / "configs" / "calibration" / "calibration_policy_v2_4.json").write_text(json.dumps(policy), encoding="utf-8")
        (root / "configs" / "calibration" / "threshold_grid_v2_4.json").write_text(json.dumps(grid), encoding="utf-8")

        routed = {
            "routed_advantage": 0.56,
            "route_preservation_score": 1.0,
            "route_failure_count": 0,
            "route_failure_surface": [],
        }
        external = {
            "external_routed_advantage": 0.20,
            "external_preservation_score": 1.0,
            "external_failure_count": 0,
            "external_failure_surface": [],
        }
        stress = {
            "stress_routed_advantage": 0.28,
            "safe_fail_score": 1.0,
            "crash_rate": 0.0,
            "stress_failure_count": 0,
            "stress_failure_surface": [],
        }

        (root / "reports" / "validation" / "latest_routed_validation_report.json").write_text(json.dumps(routed), encoding="utf-8")
        (root / "reports" / "external_validation" / "latest_external_validation_report.json").write_text(json.dumps(external), encoding="utf-8")
        (root / "reports" / "stress_validation" / "latest_stress_validation_report.json").write_text(json.dumps(stress), encoding="utf-8")

        return root

    def test_run_calibration(self):
        root = self._setup_tmp_root()
        result = run_calibration(root)
        self.assertEqual(result["version"], "PBSA-v2.4")
        self.assertEqual(result["candidate_count"], 1)
        self.assertIn("recommended_thresholds", result)
        self.assertFalse(result["automatic_kernel_replacement_allowed"])

    def test_build_calibration_report(self):
        root = self._setup_tmp_root()
        result = build_calibration_report(root)
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "calibrate_thresholds",
            "calibrate_with_caution",
            "preserve_thresholds_for_review",
            "reject_calibration",
        })
        self.assertTrue(Path(result["calibration_report_json"]).exists())

    def test_calibration_report_preserves_no_replacement(self):
        root = self._setup_tmp_root()
        result = build_calibration_report(root)
        report = json.loads(Path(result["calibration_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v2.4")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
