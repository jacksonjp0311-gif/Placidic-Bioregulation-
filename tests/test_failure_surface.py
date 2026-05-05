import unittest

from pba.validation.failure_surface import build_failure_surface, classify_failure


class TestFailureSurface(unittest.TestCase):
    def test_underperformance_failure(self):
        reason = classify_failure({
            "route_advantage": -0.1,
            "route_family": "baseline",
            "best_control_policy": "baseline_only",
        })
        self.assertEqual(reason, "route_underperformed_best_control")

    def test_no_failure_when_advantage_non_negative(self):
        reason = classify_failure({
            "route_advantage": 0.1,
            "route_family": "baseline",
            "best_control_policy": "baseline_only",
        })
        self.assertIsNone(reason)

    def test_failure_surface_generation(self):
        surface = build_failure_surface([
            {
                "domain_id": "d1",
                "selected_route": "r1",
                "route_family": "candidate",
                "best_control_policy": "baseline_only",
                "route_advantage": -0.2,
            }
        ])
        self.assertEqual(len(surface), 1)
        self.assertEqual(surface[0]["failure_reason"], "route_underperformed_best_control")


if __name__ == "__main__":
    unittest.main()
