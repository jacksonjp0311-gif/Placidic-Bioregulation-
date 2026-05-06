import unittest

from pba.public_package.public_claim_boundaries import (
    build_public_claim_boundary_table,
    public_claim_boundaries_valid,
)


class TestPublicClaimBoundaries(unittest.TestCase):
    def test_public_claim_boundaries_valid(self):
        table = build_public_claim_boundary_table()
        self.assertTrue(public_claim_boundaries_valid(table))

    def test_forbidden_claims_present(self):
        table = build_public_claim_boundary_table()
        forbidden = " ".join(table["forbidden_public_claims"]).lower()
        self.assertIn("medical guidance", forbidden)
        self.assertIn("biological validation", forbidden)
        self.assertIn("clinical safety", forbidden)

    def test_no_replacement_locks(self):
        table = build_public_claim_boundary_table()
        self.assertFalse(table["automatic_kernel_replacement_allowed"])
        self.assertFalse(table["kernel_mutation_allowed"])


if __name__ == "__main__":
    unittest.main()
