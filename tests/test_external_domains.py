import unittest
import tempfile
import json
from pathlib import Path

from pba.external.external_domain_loader import load_external_domain, load_external_suite


class TestExternalDomains(unittest.TestCase):
    def test_load_external_domain(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "domain.json"
            path.write_text(json.dumps({
                "domain_id": "d",
                "family": "f",
                "primary_regime": "direct_recovery",
                "secondary_regimes": ["baseline_advantage"],
                "external": True,
            }), encoding="utf-8")
            obj = load_external_domain(path)
            self.assertEqual(obj["domain_id"], "d")

    def test_rejects_non_external_domain(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "domain.json"
            path.write_text(json.dumps({
                "domain_id": "d",
                "family": "f",
                "primary_regime": "direct_recovery",
                "secondary_regimes": [],
                "external": False,
            }), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_external_domain(path)

    def test_load_repo_external_suite(self):
        root = Path.cwd()
        domains = load_external_suite(root)
        self.assertGreaterEqual(len(domains), 5)
        self.assertTrue(all(d["external"] for d in domains))


if __name__ == "__main__":
    unittest.main()
