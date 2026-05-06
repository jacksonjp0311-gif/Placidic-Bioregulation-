import unittest

from pba.replay.decision_replay import compare_decision, compare_decision_map, semantic_drift_items


class TestDecisionReplay(unittest.TestCase):
    def test_matching_decision(self):
        result = compare_decision({"decision": "a"}, {"decision": "a"})
        self.assertEqual(result["status"], "match")
        self.assertTrue(result["matches"])

    def test_semantic_drift_decision(self):
        result = compare_decision({"decision": "a"}, {"decision": "b"})
        self.assertEqual(result["status"], "semantic_drift")
        self.assertFalse(result["matches"])

    def test_decision_map_drift_items(self):
        result = compare_decision_map(
            {"x": {"decision": "a"}},
            {"x": {"decision": "b"}},
            {"x": "decision"},
        )
        drift = semantic_drift_items(result)
        self.assertEqual(len(drift), 1)
        self.assertEqual(drift[0]["report"], "x")


if __name__ == "__main__":
    unittest.main()
