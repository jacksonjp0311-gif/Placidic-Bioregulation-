import unittest
from pathlib import Path

from pba.evidence_hardening.report_chain import verify_report_chain


class TestReportChain(unittest.TestCase):
    def test_report_chain_verifies(self):
        result = verify_report_chain(Path.cwd())
        self.assertTrue(result["present"])
        self.assertTrue(result["locks_ok"])
        self.assertTrue(result["report_chain_valid"])


if __name__ == "__main__":
    unittest.main()
