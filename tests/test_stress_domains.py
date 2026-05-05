import unittest
from pathlib import Path

from pba.stress.stress_domain_loader import load_stress_suite
from pba.stress.malformed_input_guard import inspect_stress_domain


class TestStressDomains(unittest.TestCase):
    def test_load_repo_stress_suite(self):
        domains = load_stress_suite(Path.cwd())
        self.assertGreaterEqual(len(domains), 6)
        self.assertTrue(any(d.get("stress_type") == "malformed_input" for d in domains))

    def test_valid_stress_domain_guard(self):
        result = inspect_stress_domain({
            "domain_id": "d",
            "family": "f",
            "stress_type": "noise_injection",
            "primary_regime": "noisy",
            "secondary_regimes": [],
            "stress": True,
        })
        self.assertEqual(result["status"], "valid")

    def test_malformed_stress_domain_guard_rejects(self):
        result = inspect_stress_domain({
            "domain_id": "d",
            "family": "f",
            "stress_type": "malformed_input",
            "secondary_regimes": [],
            "stress": True,
        })
        self.assertEqual(result["status"], "reject")
        self.assertIn("primary_regime", result["missing_fields"])


if __name__ == "__main__":
    unittest.main()
