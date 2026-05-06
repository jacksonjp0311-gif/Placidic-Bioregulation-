import unittest
from pathlib import Path

from pba.evidence_hardening.rcc_anchor_verifier import (
    verify_mini_readmes,
    verify_rcc_anchors,
    verify_root_readme_anchors,
)


class TestRCCAnchorVerifier(unittest.TestCase):
    def test_root_readme_anchors(self):
        result = verify_root_readme_anchors(Path.cwd())
        self.assertTrue(result["root_readme_anchors_valid"])

    def test_mini_readmes(self):
        result = verify_mini_readmes(Path.cwd())
        self.assertTrue(result["mini_readmes_valid"])

    def test_rcc_anchors(self):
        result = verify_rcc_anchors(Path.cwd())
        self.assertTrue(result["rcc_anchor_verification_valid"])


if __name__ == "__main__":
    unittest.main()
