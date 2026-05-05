import unittest
from pba.core.domain import DomainConfig
from pba.core.parameters import ParameterManifest
from pba.core.perturbations import generate_perturbations
from pba.core.kernel import run_pba


class TestKernel(unittest.TestCase):
    def test_kernel_runs(self):
        d = DomainConfig.from_file("configs/domains/temperature_like.json")
        p = ParameterManifest()
        perturbations = generate_perturbations(d, d.eval_seed)
        records = run_pba(d, p, perturbations)
        self.assertEqual(len(records), d.time_steps)
        self.assertIn("delta_phi", records[0])
        self.assertIn("omega", records[0])


if __name__ == "__main__":
    unittest.main()