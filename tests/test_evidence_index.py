import unittest
from pathlib import Path

from pba.release.command_surface import build_command_surface, command_surface_valid
from pba.release.evidence_index import build_evidence_index, evidence_index_valid
from pba.release.failure_surface_index import build_failure_surface_index, failure_surface_index_valid


class TestEvidenceIndex(unittest.TestCase):
    def test_evidence_index_valid(self):
        rows = build_evidence_index(Path.cwd())
        self.assertTrue(evidence_index_valid(rows))
        self.assertTrue(any(row["name"] == "replay_audit" for row in rows))

    def test_failure_surface_index_valid(self):
        index = build_failure_surface_index(Path.cwd())
        self.assertTrue(failure_surface_index_valid(index))
        self.assertIn("replay_audit", index)

    def test_command_surface_valid(self):
        surface = build_command_surface()
        self.assertTrue(command_surface_valid(surface))
        self.assertIn("python -m pba.cli release-candidate-report", surface["commands"])


if __name__ == "__main__":
    unittest.main()
