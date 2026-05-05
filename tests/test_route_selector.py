import unittest

from pba.routing.route_registry import builtin_routes
from pba.routing.route_selector import select_route


class TestRouteSelector(unittest.TestCase):
    def test_builtin_routes_exist(self):
        routes = builtin_routes()
        self.assertIn("baseline_proportional_route", routes)
        self.assertIn("champion_pba_route", routes)
        self.assertIn("candidate_noisy_guard_route_pending_review", routes)

    def test_direct_baseline_routes_to_baseline(self):
        result = select_route(
            "temperature_like",
            "direct_recovery",
            ["baseline_advantage", "cusp_risk"],
        )
        self.assertEqual(result["selected_route"], "baseline_proportional_route")
        self.assertEqual(result["route_family"], "baseline")
        self.assertFalse(result["automatic_kernel_replacement_allowed"])

    def test_oscillatory_pba_routes_to_champion(self):
        result = select_route(
            "oscillatory_signal",
            "oscillatory",
            ["pba_advantage"],
        )
        self.assertEqual(result["selected_route"], "champion_pba_route")
        self.assertEqual(result["route_family"], "champion")

    def test_low_confidence_rejects_route(self):
        result = select_route(
            "unknown_domain",
            "unknown",
            ["low_confidence"],
        )
        self.assertEqual(result["selected_route"], "reject_route_selection")
        self.assertEqual(result["route_family"], "reject")


if __name__ == "__main__":
    unittest.main()
