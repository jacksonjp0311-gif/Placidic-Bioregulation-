import json
import unittest
from pathlib import Path

from pba.evidence.public_package_report import build_public_package_report


class TestPublicPackageReport(unittest.TestCase):
    def test_build_public_package_report(self):
        result = build_public_package_report(Path.cwd())
        self.assertEqual(result["status"], "complete")
        self.assertIn(result["decision"], {
            "public_package_ready",
            "public_package_ready_with_caution",
            "public_package_incomplete",
            "public_package_blocked",
            "public_package_rejected",
        })
        self.assertTrue(Path(result["public_package_report_json"]).exists())

    def test_public_package_report_preserves_locks(self):
        result = build_public_package_report(Path.cwd())
        report = json.loads(Path(result["public_package_report_json"]).read_text(encoding="utf-8"))
        self.assertEqual(report["version"], "PBSA-v3.0")
        self.assertEqual(report["package_version"], "3.0.0")
        self.assertFalse(report["automatic_kernel_replacement_allowed"])
        self.assertFalse(report["kernel_mutation_allowed"])
        self.assertIn("publication_abstract", report)
        self.assertIn("public_limitations", report)

    def test_public_outputs_created(self):
        result = build_public_package_report(Path.cwd())
        self.assertTrue(Path(result["latest_publication_abstract_md"]).exists())
        self.assertEqual(result["release_tag"], "v3.0.0-public-research-package")


if __name__ == "__main__":
    unittest.main()
