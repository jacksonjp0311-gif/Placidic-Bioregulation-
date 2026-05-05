import unittest

from pba.evaluation.regime_detector import detect_regime


class TestRegimeDetector(unittest.TestCase):
    def test_temperature_primary_direct_with_cusp_overlay(self):
        result = detect_regime(
            "temperature_like",
            metrics={"oscillation_amplitude": 1.32, "cusp_warnings": 11, "max_deviation": 1.0},
            comparison={"baseline_result": "baseline_advantage", "best_baseline": "proportional_feedback"},
        )
        self.assertEqual(result["primary_regime"], "direct_recovery")
        self.assertEqual(result["detected_regime"], "direct_recovery")
        self.assertIn("cusp_risk", result["secondary_regimes"])
        self.assertIn("cusp_risk", result["risk_overlays"])
        self.assertIn("baseline_advantage", result["secondary_regimes"])
        self.assertEqual(result["non_claim_boundary"], "computational diagnosis only")

    def test_pulse_primary_pulse_with_cusp_overlay(self):
        result = detect_regime(
            "pulse_recovery",
            metrics={"oscillation_amplitude": 1.09, "cusp_warnings": 7, "max_deviation": 0.85},
            comparison={"baseline_result": "baseline_advantage", "best_baseline": "proportional_feedback"},
        )
        self.assertEqual(result["primary_regime"], "pulse_recovery")
        self.assertEqual(result["detected_regime"], "pulse_recovery")
        self.assertIn("cusp_risk", result["secondary_regimes"])
        self.assertIn("baseline_advantage", result["secondary_regimes"])

    def test_oscillatory_primary_oscillatory_with_cusp_overlay(self):
        result = detect_regime(
            "oscillatory_signal",
            metrics={"oscillation_amplitude": 0.98, "cusp_warnings": 8, "max_deviation": 0.78},
            comparison={"baseline_result": "pba_advantage", "best_baseline": "proportional_feedback"},
        )
        self.assertEqual(result["primary_regime"], "oscillatory")
        self.assertEqual(result["detected_regime"], "oscillatory")
        self.assertIn("cusp_risk", result["secondary_regimes"])
        self.assertIn("pba_advantage", result["secondary_regimes"])

    def test_unknown_preserves_low_confidence_overlay(self):
        result = detect_regime(
            "unknown_domain",
            metrics={},
            comparison={},
        )
        self.assertEqual(result["primary_regime"], "unknown")
        self.assertIn("low_confidence", result["secondary_regimes"])


if __name__ == "__main__":
    unittest.main()
