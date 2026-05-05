import unittest
from pba.evaluation.metrics import compute_metrics


class TestMetrics(unittest.TestCase):
    def test_metrics_emit(self):
        records = [
            {"t": 0, "x_t": 1.0, "target": 0.0, "delta_phi": 1.0, "signal": 1.0},
            {"t": 1, "x_t": 0.1, "target": 0.0, "delta_phi": 0.1, "signal": 0.9},
        ]
        m = compute_metrics(records, (-0.25, 0.25))
        self.assertIn("cumulative_deviation", m)
        self.assertIn("signal_preservation", m)


if __name__ == "__main__":
    unittest.main()