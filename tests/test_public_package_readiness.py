import unittest
from pathlib import Path

from pba.public_package.public_package_bundle import build_public_package_bundle
from pba.public_package.public_package_readiness import verify_public_package_readiness


class TestPublicPackageReadiness(unittest.TestCase):
    def test_public_package_readiness_result(self):
        result = verify_public_package_readiness(Path.cwd())
        self.assertIn(result["decision"], {
            "public_package_ready",
            "public_package_ready_with_caution",
            "public_package_incomplete",
            "public_package_rejected",
        })
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_public_package_bundle(self):
        bundle = build_public_package_bundle(Path.cwd())
        self.assertEqual(bundle["version"], "PBSA-v3.0")
        self.assertEqual(bundle["package_version"], "3.0.0")
        self.assertIn("publication_abstract", bundle)
        self.assertIn("evidence_summary", bundle)
        self.assertFalse(bundle["automatic_kernel_replacement_allowed"])

    def test_release_checklist(self):
        bundle = build_public_package_bundle(Path.cwd())
        checklist = bundle["release_checklist"]
        self.assertIn("claim_locks_visible", checklist)
        self.assertFalse(checklist["automatic_kernel_replacement_allowed"])


if __name__ == "__main__":
    unittest.main()
