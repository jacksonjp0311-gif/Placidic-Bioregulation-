import unittest

from pba.evolution.promotion_governance import decide_promotion, DECISIONS


class TestPromotionGovernance(unittest.TestCase):
    def test_decision_taxonomy_contains_expected_decisions(self):
        self.assertIn("preserve_champion", DECISIONS)
        self.assertIn("route_by_regime", DECISIONS)
        self.assertIn("promote_candidate_pending_review", DECISIONS)

    def test_no_automatic_replacement_even_when_improved(self):
        result = decide_promotion({
            "original_suite_result": {"champion_classification": "PBA-C", "best_challenger_classification": "PBA-B"},
            "holdout_suite_result": {"champion_classification": "PBA-D", "best_challenger_classification": "PBA-C"},
            "baseline_visibility_preserved": True,
            "non_claim_locks_preserved": True,
            "rcc_contract_preserved": True,
        })
        self.assertEqual(result["decision"], "promote_candidate_pending_review")
        self.assertFalse(result["automatic_kernel_replacement_allowed"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_rejects_when_governance_surface_fails(self):
        result = decide_promotion({
            "baseline_visibility_preserved": False,
            "non_claim_locks_preserved": True,
            "rcc_contract_preserved": True,
        })
        self.assertEqual(result["decision"], "reject_candidate")


if __name__ == "__main__":
    unittest.main()
