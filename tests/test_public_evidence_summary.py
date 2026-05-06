import unittest
from pathlib import Path

from pba.public_package.evidence_summary import build_evidence_summary, evidence_summary_valid
from pba.public_package.public_abstract import build_publication_abstract, public_abstract_valid
from pba.public_package.public_limitations import build_public_limitations, public_limitations_valid
from pba.public_package.public_command_surface import build_public_command_surface, public_command_surface_valid


class TestPublicEvidenceSummary(unittest.TestCase):
    def test_publication_abstract_valid(self):
        text = build_publication_abstract()
        self.assertTrue(public_abstract_valid(text))
        self.assertIn("not medical guidance", text.lower())

    def test_evidence_summary_valid(self):
        rows = build_evidence_summary(Path.cwd())
        self.assertTrue(evidence_summary_valid(rows))
        self.assertTrue(any(row["name"] == "release_candidate" for row in rows))

    def test_public_limitations_valid(self):
        limitations = build_public_limitations()
        self.assertTrue(public_limitations_valid(limitations))

    def test_public_command_surface_valid(self):
        surface = build_public_command_surface()
        self.assertTrue(public_command_surface_valid(surface))
        self.assertIn("python -m pba.cli public-package-report", surface["commands"])


if __name__ == "__main__":
    unittest.main()
