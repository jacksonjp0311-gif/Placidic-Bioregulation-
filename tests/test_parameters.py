import unittest
from pba.core.parameters import ParameterManifest


class TestParameters(unittest.TestCase):
    def test_defaults_validate(self):
        p = ParameterManifest()
        p.validate()
        self.assertGreater(p.eta, 0)
        self.assertLess(p.tau_1, p.tau_2)


if __name__ == "__main__":
    unittest.main()