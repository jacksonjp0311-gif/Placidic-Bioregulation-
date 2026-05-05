import unittest
from pba.core.domain import DomainConfig
from pba.core.perturbations import generate_perturbations
from pba.baselines import ProportionalBaseline, PIBaseline, ThresholdBaseline, ReturnToSetpointBaseline


class TestBaselines(unittest.TestCase):
    def test_all_baselines_run(self):
        d = DomainConfig.from_file("configs/domains/temperature_like.json")
        perturbations = generate_perturbations(d, d.eval_seed)
        baselines = [
            ProportionalBaseline(),
            PIBaseline(),
            ThresholdBaseline(),
            ReturnToSetpointBaseline(),
        ]
        for baseline in baselines:
            records = baseline.run(d, perturbations, {})
            self.assertEqual(len(records), d.time_steps)
            self.assertIn("delta_phi", records[0])


if __name__ == "__main__":
    unittest.main()