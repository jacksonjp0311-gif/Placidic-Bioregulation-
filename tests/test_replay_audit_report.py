import json
import unittest
from pathlib import Path

from pba.evidence.replay_audit_report import build_replay_audit_report
from pba.replay.replay_runner import run_replay


class TestReplayAuditReport(unittest.TestCase):
    def test_run_replay(self):
        result = run_replay(Path.cwd())
        self.assertEqual(result["version"], "PBSA-v2.6")
        self.assertIn("decision_replay", result)
        self.assertIn("hash_drift", result)
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_build_replay_audit_report(self):
        result = build_replay_audit_report(Path.cwd())
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "replay_valid",
            "replay_valid_with_timestamp_drift",
            "replay_valid_with_caution",
            "replay_semantic_drift",
            "replay_rejected",
        })
        self.assertTrue(Path(result["replay_audit_report_json"]).exists())

    def test_replay_report_preserves_locks(self):
        result = build_replay_audit_report(Path.cwd())
        report = json.loads(Path(result["replay_audit_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v2.6")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])
        self.assertIn("semantic_drift", report)
        self.assertIn("expected_timestamp_drift", report)


if __name__ == "__main__":
    unittest.main()
