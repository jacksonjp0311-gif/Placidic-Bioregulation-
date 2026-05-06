import unittest

from pba.release.claim_boundary_table import build_claim_boundary_table, claim_boundary_valid


class TestClaimBoundaryTable(unittest.TestCase):
    def test_claim_boundary_table_valid(self):
        table = build_claim_boundary_table()
        self.assertTrue(claim_boundary_valid(table))

    def test_forbidden_claims_include_medical_and_biological(self):
        table = build_claim_boundary_table()
        forbidden = " ".join(table["forbidden_claims"]).lower()
        self.assertIn("medical guidance", forbidden)
        self.assertIn("biological validation", forbidden)

    def test_no_automatic_replacement(self):
        table = build_claim_boundary_table()
        self.assertFalse(table["automatic_kernel_replacement_allowed"])
        self.assertFalse(table["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
