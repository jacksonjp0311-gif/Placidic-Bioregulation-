import unittest
from pathlib import Path

from pba.release.release_bundle import build_release_bundle
from pba.release.release_readiness import verify_release_readiness


class TestReleaseReadiness(unittest.TestCase):
    def test_release_readiness_result(self):
        result = verify_release_readiness(Path.cwd())
        self.assertIn(result["decision"], {
            "release_candidate_ready",
            "release_candidate_ready_with_caution",
            "release_candidate_incomplete",
            "release_candidate_rejected",
        })
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_release_bundle(self):
        bundle = build_release_bundle(Path.cwd())
        self.assertEqual(bundle["version"], "PBSA-v2.7")
        self.assertIn("evidence_index", bundle)
        self.assertIn("claim_boundary_table", bundle)
        self.assertFalse(bundle["automatic_kernel_replacement_allowed"])

    def test_release_readiness_has_checks(self):
        result = verify_release_readiness(Path.cwd())
        self.assertIn("checks", result)
        self.assertIn("claim_boundary_valid", result["checks"])
        self.assertIn("command_surface_valid", result["checks"])


if __name__ == "__main__":
    unittest.main()
