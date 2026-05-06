import unittest
from pathlib import Path

from pba.evidence_hardening.ledger_continuity import read_ledger_events, verify_ledger_continuity


class TestLedgerContinuity(unittest.TestCase):
    def test_read_ledger_events(self):
        events = read_ledger_events(Path.cwd())
        self.assertGreater(len(events), 0)

    def test_verify_ledger_continuity(self):
        result = verify_ledger_continuity(Path.cwd())
        self.assertTrue(result["present"])
        self.assertTrue(result["ledger_continuity_valid"])


if __name__ == "__main__":
    unittest.main()
