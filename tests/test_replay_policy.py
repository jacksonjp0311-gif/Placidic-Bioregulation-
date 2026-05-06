import json
import unittest
from pathlib import Path


class TestReplayPolicy(unittest.TestCase):
    def test_replay_policy_exists(self):
        path = Path("configs/replay/replay_policy_v2_6.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-ReplayPolicy-v2.6")
        self.assertFalse(data["automatic_kernel_replacement_allowed"])

    def test_replay_artifact_manifest_exists(self):
        path = Path("configs/replay/replay_artifact_manifest_v2_6.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-ReplayArtifactManifest-v2.6")
        self.assertIn("source_reports", data)

    def test_replay_policy_has_sequence(self):
        data = json.loads(Path("configs/replay/replay_policy_v2_6.json").read_text(encoding="utf-8"))
        self.assertIn("routed_validation_report", data["replay_sequence"])
        self.assertIn("evidence_package_report", data["replay_sequence"])


if __name__ == "__main__":
    unittest.main()
