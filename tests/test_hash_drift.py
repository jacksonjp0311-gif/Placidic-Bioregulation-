import unittest

from pba.replay.hash_drift import classify_hash_drift, compare_hash_manifests


class TestHashDrift(unittest.TestCase):
    def test_hash_match(self):
        result = classify_hash_drift("README.md", "abc", "abc")
        self.assertEqual(result["status"], "match")
        self.assertFalse(result["drift"])

    def test_expected_timestamp_drift(self):
        result = classify_hash_drift("reports/replay/latest_replay_audit_report.json", "a", "b")
        self.assertEqual(result["status"], "expected_timestamp_drift")

    def test_semantic_hash_drift(self):
        result = classify_hash_drift("src/pba/core.py", "a", "b")
        self.assertEqual(result["status"], "semantic_hash_drift")

    def test_compare_hash_manifests(self):
        result = compare_hash_manifests(
            [{"path": "README.md", "sha256": "a"}],
            [{"path": "README.md", "sha256": "a"}],
        )
        self.assertTrue(result["hash_drift_valid"])


if __name__ == "__main__":
    unittest.main()
