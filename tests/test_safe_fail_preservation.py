import unittest

from pba.calibration_thresholds.safe_fail_preservation import (
    crash_rate_preserved,
    failure_visibility_preserved,
    preservation_status,
    safe_fail_preserved,
)


class TestSafeFailPreservation(unittest.TestCase):
    def test_safe_fail_preserved(self):
        self.assertTrue(safe_fail_preserved(1.0, 1.0))
        self.assertFalse(safe_fail_preserved(0.9, 1.0))

    def test_crash_rate_preserved(self):
        self.assertTrue(crash_rate_preserved(0.0, 0.0))
        self.assertFalse(crash_rate_preserved(0.1, 0.0))

    def test_failure_visibility_preserved(self):
        self.assertTrue(failure_visibility_preserved(True, 0))
        self.assertFalse(failure_visibility_preserved(False, 0))
        self.assertFalse(failure_visibility_preserved(True, 1))

    def test_preservation_status(self):
        status = preservation_status(1.0, 1.0, 0.0, 0.0, True, 0)
        self.assertTrue(status["safe_fail_score_preserved"])
        self.assertTrue(status["crash_rate_preserved"])
        self.assertTrue(status["failure_visibility_preserved"])


if __name__ == "__main__":
    unittest.main()
