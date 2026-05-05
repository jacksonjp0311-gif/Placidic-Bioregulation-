import unittest

from pba.validation.route_metrics import (
    best_control_policy,
    control_suite_scores,
    route_advantage,
    route_preservation_score,
    suite_score,
    validation_decision,
)


class TestRouteMetrics(unittest.TestCase):
    def test_suite_and_control_scores(self):
        rows = [
            {"routed_score": 0.9, "control_scores": {"baseline_only": 1.0, "champion_only": 1.2}},
            {"routed_score": 1.0, "control_scores": {"baseline_only": 1.1, "champion_only": 1.1}},
        ]
        self.assertEqual(suite_score(rows), 1.9)
        controls = control_suite_scores(rows)
        self.assertEqual(controls["baseline_only"], 2.1)
        self.assertEqual(best_control_policy(controls), "baseline_only")

    def test_route_advantage(self):
        self.assertEqual(route_advantage(1.9, 2.1), 0.2)

    def test_preservation_and_decision(self):
        rows = [
            {"routed_score": 0.9, "best_control_score": 1.0},
            {"routed_score": 1.0, "best_control_score": 1.0},
        ]
        self.assertEqual(route_preservation_score(rows), 1.0)
        self.assertEqual(validation_decision(0.2, 1.0, 0), "validate_routing")


if __name__ == "__main__":
    unittest.main()
