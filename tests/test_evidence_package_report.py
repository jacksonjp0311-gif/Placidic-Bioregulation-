import json
import tempfile
import unittest
from pathlib import Path

from pba.evidence.evidence_package_report import build_evidence_package_report
from pba.evidence_hardening.evidence_package import compile_evidence_package


class TestEvidencePackageReport(unittest.TestCase):
    def test_compile_repo_evidence_package(self):
        result = compile_evidence_package(Path.cwd())
        self.assertEqual(result["version"], "PBSA-v2.5")
        self.assertIn("hash_manifest", result)
        self.assertIn("traceability_matrix", result)
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_build_repo_evidence_package_report(self):
        result = build_evidence_package_report(Path.cwd())
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "evidence_package_valid",
            "evidence_package_valid_with_caution",
            "evidence_package_incomplete",
            "evidence_package_rejected",
        })
        self.assertTrue(Path(result["evidence_package_report_json"]).exists())

    def test_report_preserves_locks(self):
        result = build_evidence_package_report(Path.cwd())
        report = json.loads(Path(result["evidence_package_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v2.5")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
