import unittest

from pba.stress.malformed_input_guard import inspect_stress_domain, safe_fail_decision


class TestMalformedInputGuard(unittest.TestCase):
    def test_missing_required_field_safe_fails(self):
        result = inspect_stress_domain({"domain_id": "bad"})
        self.assertEqual(result["status"], "reject")
        self.assertTrue(result["safe_fail_required"])

    def test_invalid_secondary_regimes_rejected(self):
        result = inspect_stress_domain({
            "domain_id": "bad",
            "family": "f",
            "stress_type": "malformed_input",
            "primary_regime": "unknown",
            "secondary_regimes": "not-a-list",
            "stress": True,
        })
        self.assertEqual(result["status"], "reject")
        self.assertIn("secondary_regimes_must_be_list", result["invalid_fields"])

    def test_safe_fail_decision_no_replacement(self):
        decision = safe_fail_decision({"domain_id": "bad"}, "malformed_input_rejected")
        self.assertEqual(decision["selected_route"], "reject_route_selection")
        self.assertTrue(decision["manual_review_required"])
        self.assertFalse(decision["automatic_kernel_replacement_allowed"])
        self.assertFalse(decision["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
