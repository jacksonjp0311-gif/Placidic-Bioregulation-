import unittest

from pba.evolution.candidate_variants import (
    load_builtin_candidate_variants,
    apply_candidate_to_domain,
)


class TestCandidateVariants(unittest.TestCase):
    def test_builtin_candidates_exist(self):
        variants = load_builtin_candidate_variants()
        self.assertIn("direct_route_candidate_v0", variants)
        self.assertIn("pulse_route_candidate_v0", variants)
        self.assertIn("oscillatory_preservation_candidate_v0", variants)
        self.assertIn("noisy_recovery_guard_candidate_v0", variants)

    def test_direct_candidate_improves_matching_direct_domain(self):
        variant = load_builtin_candidate_variants()["direct_route_candidate_v0"]
        result = apply_candidate_to_domain(variant, {
            "domain_id": "temperature_like",
            "primary_regime": "direct_recovery",
            "secondary_regimes": ["baseline_advantage"],
            "champion_score": 10.0,
            "champion_classification": "PBA-D",
        })
        self.assertLess(result["candidate_score"], result["champion_score"])
        self.assertFalse(result["kernel_mutation_allowed"])

    def test_unmatched_candidate_penalized(self):
        variant = load_builtin_candidate_variants()["direct_route_candidate_v0"]
        result = apply_candidate_to_domain(variant, {
            "domain_id": "oscillatory_signal",
            "primary_regime": "oscillatory",
            "secondary_regimes": ["pba_advantage"],
            "champion_score": 10.0,
            "champion_classification": "PBA-C",
        })
        self.assertGreater(result["candidate_score"], result["champion_score"])
        self.assertEqual(result["candidate_execution_scope"], "comparison_harness_only")


if __name__ == "__main__":
    unittest.main()
