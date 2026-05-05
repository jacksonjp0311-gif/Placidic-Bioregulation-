import unittest
from pathlib import Path
from pba.core.domain import DomainConfig


class TestDomainConfig(unittest.TestCase):
    def test_load_temperature_domain(self):
        d = DomainConfig.from_file(Path("configs/domains/temperature_like.json"))
        self.assertEqual(d.domain_id, "temperature_like")
        self.assertIn("not_medical", d.non_claim_locks)


if __name__ == "__main__":
    unittest.main()