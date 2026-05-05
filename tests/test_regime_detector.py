import unittest

from pba.evaluation.regime_detector import detect_regime


class TestRegimeDetector(unittest.TestCase):
    def test_oscillatory_domain_detects_oscillatory(self):
        result = detect_regime(
            "oscillatory_signal",
            metrics={"oscillation_amplitude": 1.2, "cusp_warnings": 0},
            comparison={"baseline_result": "pba_advantage", "best_baseline": "proportional_feedback"},
        )
        self.assertEqual(result["detected_regime"], "oscillatory")
        self.assertEqual(result["non_claim_boundary"], "computational diagnosis only")

    def test_temperature_baseline_advantage_detects_direct(self):
        result = detect_regime(
            "temperature_like",
            metrics={"oscillation_amplitude": 0.1, "cusp_warnings": 0},
            comparison={"baseline_result": "baseline_advantage", "best_baseline": "proportional_feedback"},
        )
        self.assertEqual(result["detected_regime"], "direct_recovery")


if __name__ == "__main__":
    unittest.main()
