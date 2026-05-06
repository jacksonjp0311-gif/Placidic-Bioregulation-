import unittest
from pathlib import Path

from pba.evidence_hardening.hash_manifest import build_hash_manifest, hash_manifest_valid, sha256_file


class TestHashManifest(unittest.TestCase):
    def test_sha256_file(self):
        path = Path("README.md")
        digest = sha256_file(path)
        self.assertEqual(len(digest), 64)

    def test_build_hash_manifest(self):
        rows = build_hash_manifest(Path.cwd())
        self.assertGreater(len(rows), 5)
        self.assertTrue(any(row["role"] == "root_readme" for row in rows))

    def test_hash_manifest_valid(self):
        rows = build_hash_manifest(Path.cwd())
        self.assertTrue(hash_manifest_valid(rows))


if __name__ == "__main__":
    unittest.main()
