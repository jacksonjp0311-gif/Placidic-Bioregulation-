import json
import unittest
from pathlib import Path

from pba.evidence.release_candidate_report import build_release_candidate_report


class TestReleaseCandidateReport(unittest.TestCase):
    def test_build_release_candidate_report(self):
        result = build_release_candidate_report(Path.cwd())
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "release_candidate_ready",
            "release_candidate_ready_with_caution",
            "release_candidate_incomplete",
            "release_candidate_blocked",
            "release_candidate_rejected",
        })
        self.assertTrue(Path(result["release_candidate_report_json"]).exists())

    def test_release_candidate_report_preserves_locks(self):
        result = build_release_candidate_report(Path.cwd())
        report = json.loads(Path(result["release_candidate_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v2.7")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])
        self.assertIn("claim_boundary_table", report)
        self.assertIn("evidence_index", report)

    def test_public_audit_index_created(self):
        result = build_release_candidate_report(Path.cwd())
        self.assertTrue(Path(result["latest_public_audit_index_md"]).exists())


if __name__ == "__main__":
    unittest.main()
