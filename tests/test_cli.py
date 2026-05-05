import os
import subprocess
import sys
import unittest


class TestCLI(unittest.TestCase):
    def test_cli_help_imports(self):
        env = dict(os.environ)
        env["PYTHONPATH"] = "src"
        result = subprocess.run(
            [sys.executable, "-m", "pba.cli", "--help"],
            capture_output=True,
            text=True,
            env=env,
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("PBSA", result.stdout)


if __name__ == "__main__":
    unittest.main()