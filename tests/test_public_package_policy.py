import json
import unittest
from pathlib import Path


class TestPublicPackagePolicy(unittest.TestCase):
    def test_public_package_policy_exists(self):
        path = Path("configs/public_package/public_package_policy_v3_0.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-PublicPackagePolicy-v3.0")
        self.assertEqual(data["release_tag"], "v3.0.0-public-research-package")
        self.assertFalse(data["automatic_kernel_replacement_allowed"])

    def test_public_release_manifest_exists(self):
        path = Path("configs/public_package/public_release_manifest_v3_0.json")
        self.assertTrue(path.exists())
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual(data["version"], "PBSA-PublicReleaseManifest-v3.0")
        self.assertIn("public_outputs", data)

    def test_policy_has_non_claim_locks(self):
        data = json.loads(Path("configs/public_package/public_package_policy_v3_0.json").read_text(encoding="utf-8"))
        self.assertIn("not_medical", data["non_claim_locks"])
        self.assertFalse(data["public_release_is_biological_validation"])


if __name__ == "__main__":
    unittest.main()
