import unittest

from pba.calibration_thresholds.calibration_metrics import (
    admissible_candidate,
    calibration_decision,
    calibration_score,
)


class TestCalibrationMetrics(unittest.TestCase):
    def test_calibration_score(self):
        score = calibration_score(
            routed_advantage=0.5,
            preservation_score=1.0,
            safe_fail_score=1.0,
            failure_count=0,
            overfitting_penalty=0.2,
            crash_rate=0.0,
        )
        self.assertGreater(score, 0)

    def test_admissible_candidate_requires_guards(self):
        self.assertTrue(admissible_candidate(True, True, True, True))
        self.assertFalse(admissible_candidate(False, True, True, True))
        self.assertFalse(admissible_candidate(True, True, True, True, automatic_kernel_replacement_allowed=True))

    def test_calibration_decisions(self):
        self.assertEqual(calibration_decision(True, 2.5, True), "calibrate_thresholds")
        self.assertEqual(calibration_decision(True, 1.5, True), "calibrate_with_caution")
        self.assertEqual(calibration_decision(True, 0.5, True), "preserve_thresholds_for_review")
        self.assertEqual(calibration_decision(False, 3.0, True), "reject_calibration")


if __name__ == "__main__":
    unittest.main()
