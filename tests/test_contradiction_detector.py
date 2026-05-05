import unittest

from pba.stress.contradiction_detector import detect_contradiction


class TestContradictionDetector(unittest.TestCase):
    def test_detects_baseline_pba_low_confidence_conflict(self):
        result = detect_contradiction("direct_recovery", ["baseline_advantage", "pba_advantage", "low_confidence"])
        self.assertTrue(result["contradiction"])
        self.assertTrue(result["safe_fail_required"])

    def test_detects_unknown_primary_with_pba_advantage(self):
        result = detect_contradiction("unknown", ["pba_advantage"])
        self.assertTrue(result["contradiction"])

    def test_no_contradiction_for_simple_baseline_advantage(self):
        result = detect_contradiction("direct_recovery", ["baseline_advantage"])
        self.assertFalse(result["contradiction"])


if __name__ == "__main__":
    unittest.main()
