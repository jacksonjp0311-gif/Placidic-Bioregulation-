import unittest
from pathlib import Path

from pba.evidence_hardening.downgrade_lock_verifier import verify_downgrade_locks
from pba.evidence_hardening.failure_surface_verifier import verify_failure_surfaces


class TestDowngradeLockVerifier(unittest.TestCase):
    def test_downgrade_locks(self):
        result = verify_downgrade_locks(Path.cwd())
        self.assertTrue(result["downgrade_locks_valid"])
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_failure_surfaces(self):
        result = verify_failure_surfaces(Path.cwd())
        self.assertTrue(result["failure_surface_preservation_valid"])
        self.assertEqual(result["failure_surface_status"]["calibration"], "present")


if __name__ == "__main__":
    unittest.main()
