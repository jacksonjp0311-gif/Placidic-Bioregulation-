import json
import unittest
from pathlib import Path

from pba.calibration_thresholds.threshold_candidate import build_candidates, ThresholdCandidate


class TestThresholdGrid(unittest.TestCase):
    def test_repo_threshold_grid_builds_candidates(self):
        grid = json.loads(Path("configs/calibration/threshold_grid_v2_4.json").read_text(encoding="utf-8"))
        candidates = build_candidates(grid)
        self.assertEqual(len(candidates), 27)
        self.assertIsInstance(candidates[0], ThresholdCandidate)

    def test_missing_grid_values_raise(self):
        with self.assertRaises(ValueError):
            build_candidates({"values": {"route_confidence": [0.7]}})

    def test_candidate_to_dict(self):
        candidate = ThresholdCandidate("theta", 0.7, 1.0, 0.85, 0.65, 0.0, 0.8)
        data = candidate.to_dict()
        self.assertEqual(data["candidate_id"], "theta")
        self.assertEqual(data["safe_fail"], 1.0)


if __name__ == "__main__":
    unittest.main()
