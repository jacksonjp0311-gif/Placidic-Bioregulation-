import unittest

from pba.replay.replay_lock_verifier import replay_locks_reproduced, failure_surfaces_replayed


class TestReplayLockVerifier(unittest.TestCase):
    def test_locks_replayed(self):
        result = replay_locks_reproduced({
            "report": {
                "automatic_kernel_replacement_allowed": False,
                "kernel_mutation_allowed": False,
                "non_claim_locks_preserved": True,
            }
        })
        self.assertTrue(result["downgrade_locks_replayed"])

    def test_lock_violation(self):
        result = replay_locks_reproduced({
            "report": {
                "automatic_kernel_replacement_allowed": True,
                "kernel_mutation_allowed": False,
            }
        })
        self.assertFalse(result["downgrade_locks_replayed"])

    def test_failure_surfaces_replayed(self):
        result = failure_surfaces_replayed({
            "routed_validation_report": {"route_failure_surface": []},
            "external_validation_report": {"external_failure_surface": []},
            "stress_validation_report": {"stress_failure_surface": []},
            "calibration_report": {"candidate_evaluations": []},
            "evidence_package_report": {"failure_surface_status": {}},
        })
        self.assertTrue(result["failure_surfaces_replayed"])


if __name__ == "__main__":
    unittest.main()
