import unittest

from pba.calibration_thresholds.overfitting_guard import (
    overfitting_guard_passed,
    overfitting_penalty,
    overfitting_status,
)


class TestOverfittingGuard(unittest.TestCase):
    def test_overfitting_penalty(self):
        self.assertEqual(overfitting_penalty(0.5, 0.2, 0.1), 0.4)

    def test_guard_passed(self):
        self.assertTrue(overfitting_guard_passed(0.2, 0.75))
        self.assertFalse(overfitting_guard_passed(1.0, 0.75))

    def test_status(self):
        status = overfitting_status(0.56, 0.20, 0.28, 0.75)
        self.assertIn("overfitting_penalty", status)
        self.assertTrue(status["overfitting_guard_passed"])


if __name__ == "__main__":
    unittest.main()
