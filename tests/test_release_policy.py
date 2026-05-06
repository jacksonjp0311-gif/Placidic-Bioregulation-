import json
import unittest
from pathlib import Path


class TestReleasePolicy(unittest.TestCase):
    def test_release_candidate_policy_exists(self):
        path = Path("configs/release/release_candidate_policy_v2_7.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-ReleaseCandidatePolicy-v2.7")
        self.assertFalse(data["automatic_kernel_replacement_allowed"])

    def test_release_audit_manifest_exists(self):
        path = Path("configs/release/release_audit_manifest_v2_7.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-ReleaseAuditManifest-v2.7")
        self.assertIn("release_bundle_outputs", data)

    def test_release_policy_has_required_commands(self):
        data = json.loads(Path("configs/release/release_candidate_policy_v2_7.json").read_text(encoding="utf-8"))
        self.assertIn("python -m pba.cli release-candidate-report", data["required_commands"])


if __name__ == "__main__":
    unittest.main()
