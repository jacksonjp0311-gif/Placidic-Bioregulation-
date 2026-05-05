import unittest

from pba.routing.route_eligibility import route_is_eligible, non_claim_locks_valid


class TestRouteEligibility(unittest.TestCase):
    def test_non_claim_locks_valid(self):
        self.assertTrue(non_claim_locks_valid(["not_medical", "not_biological_law", "not_mechanism_proof"]))

    def test_rejects_automatic_kernel_replacement(self):
        result = route_is_eligible({"automatic_kernel_replacement_allowed": True})
        self.assertFalse(result["eligible"])
        self.assertIn("automatic_kernel_replacement_forbidden", result["reasons"])

    def test_rejects_kernel_mutation(self):
        result = route_is_eligible({"kernel_mutation_allowed": True})
        self.assertFalse(result["eligible"])
        self.assertIn("kernel_mutation_forbidden", result["reasons"])


if __name__ == "__main__":
    unittest.main()
