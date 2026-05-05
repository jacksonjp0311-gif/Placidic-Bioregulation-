import unittest

from pba.evaluation.baseline_advantage import map_baseline_advantage_from_runs


class TestBaselineAdvantage(unittest.TestCase):
    def test_maps_pba_and_baseline_wins(self):
        runs = [
            {
                "domain_id": "oscillatory_signal",
                "baseline_result": "pba_advantage",
                "best_baseline": "proportional_feedback",
                "classification": "PBA-A",
            },
            {
                "domain_id": "temperature_like",
                "baseline_result": "baseline_advantage",
                "best_baseline": "proportional_feedback",
                "classification": "PBA-C",
            },
        ]
        result = map_baseline_advantage_from_runs(runs)
        self.assertEqual(result["oscillatory_signal"]["winner"], "PBA")
        self.assertEqual(result["temperature_like"]["winner"], "proportional_feedback")


if __name__ == "__main__":
    unittest.main()
