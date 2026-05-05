import unittest

from pba.external.route_drift import (
    advantage_drift,
    failure_surface_drift,
    preservation_drift,
    route_frequency,
    route_frequency_drift,
)
from pba.external.external_failure_surface import build_external_failure_surface


class TestRouteDrift(unittest.TestCase):
    def test_advantage_and_preservation_drift(self):
        self.assertEqual(advantage_drift(0.2, 0.5), -0.3)
        self.assertEqual(preservation_drift(1.0, 0.5), 0.5)

    def test_route_frequency_drift(self):
        external = [{"selected_route": "a"}, {"selected_route": "b"}]
        internal = [{"selected_route": "a"}, {"selected_route": "a"}]
        drift = route_frequency_drift(external, internal)
        self.assertEqual(route_frequency(external)["a"], 0.5)
        self.assertLess(drift["a"], 0)

    def test_external_failure_surface(self):
        failures = build_external_failure_surface([
            {
                "domain_id": "d",
                "family": "f",
                "selected_route": "r",
                "route_family": "candidate",
                "best_control_policy": "baseline_only",
                "route_advantage": -0.1,
            }
        ])
        self.assertEqual(len(failures), 1)
        self.assertTrue(failures[0]["failure_reason"].startswith("external_"))


if __name__ == "__main__":
    unittest.main()
