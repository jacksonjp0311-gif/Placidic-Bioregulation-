import unittest

from pba.evolution.champion_challenger import compare_champion_challenger


class TestChampionChallenger(unittest.TestCase):
    def test_no_candidate_preserves_champion(self):
        result = compare_champion_challenger({"mean_pba_score": 10.0}, None)
        self.assertEqual(result["decision"], "preserve_champion")
        self.assertFalse(result["candidate_accepted"])

    def test_rejects_pba_e_candidate(self):
        champion = {"mean_pba_score": 10.0, "classification_counts": {"PBA-A": 1, "PBA-E": 0}}
        candidate = {"mean_pba_score": 9.0, "classification_counts": {"PBA-A": 1, "PBA-E": 1}}
        result = compare_champion_challenger(champion, candidate)
        self.assertEqual(result["decision"], "reject")


if __name__ == "__main__":
    unittest.main()
