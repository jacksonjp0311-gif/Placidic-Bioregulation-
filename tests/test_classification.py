import unittest
from pba.evaluation.classification import classify


class TestClassification(unittest.TestCase):
    def test_medical_overclaim_rejected(self):
        comparison = {"baseline_result": "pba_advantage"}
        ident = {"status": "stable"}
        c = classify(comparison, ident, True, ["medical_claim"])
        self.assertEqual(c["classification"], "PBA-E")

    def test_advantage_stable_promotes_local_a(self):
        comparison = {"baseline_result": "pba_advantage"}
        ident = {"status": "stable"}
        c = classify(comparison, ident, True, [])
        self.assertEqual(c["classification"], "PBA-A")


if __name__ == "__main__":
    unittest.main()