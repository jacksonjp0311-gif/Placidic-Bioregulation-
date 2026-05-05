import unittest
from pathlib import Path


def has_any(text, *needles):
    return any(needle in text for needle in needles)


class TestRCCReadmes(unittest.TestCase):
    def test_required_readmes_exist(self):
        required = [
            "README.md",
            "configs/README.md",
            "configs/domains/README.md",
            "docs/README.md",
            "docs/theory/README.md",
            "docs/architecture/README.md",
            "docs/benchmark_protocol/README.md",
            "src/README.md",
            "src/pba/README.md",
            "src/pba/core/README.md",
            "src/pba/baselines/README.md",
            "src/pba/calibration/README.md",
            "src/pba/evaluation/README.md",
            "src/pba/evidence/README.md",
            "src/pba/benchmarks/README.md",
            "src/pba/cli/README.md",
            "tests/README.md",
            "runs/README.md",
            "reports/README.md",
            "ledgers/README.md",
            "evidence_packages/README.md",
            "scripts/README.md",
        ]
        for rel in required:
            self.assertTrue(Path(rel).exists(), f"Missing RCC README: {rel}")

    def test_root_readme_has_human_and_ai_sections(self):
        text = Path("README.md").read_text(encoding="utf-8")
        reports_text = Path("reports/README.md").read_text(encoding="utf-8")

        self.assertTrue(
            has_any(text, "PART I — Human README", "PART I â€” Human README", "PART I - Human README"),
            "Root README must contain the human-facing section heading."
        )
        self.assertTrue(
            has_any(text, "PART II — AI / Agent README", "PART II â€” AI / Agent README", "PART II - AI / Agent README"),
            "Root README must contain the AI-facing section heading."
        )
        self.assertIn("Current benchmark results", text)
        self.assertIn("Where to find benchmark findings", reports_text)
        self.assertIn("AI operating contract", text)
        self.assertIn("RCC documentation contract", text)
        self.assertIn("PBSA evidence contract", text)
        self.assertIn("Not medical guidance", text)
        self.assertIn("Do not treat benchmark success as biological validation", text)

    def test_mini_readmes_have_rcc_fields(self):
        mini = [
            "src/pba/core/README.md",
            "src/pba/evidence/README.md",
            "configs/README.md",
            "reports/README.md",
            "runs/README.md",
        ]
        for rel in mini:
            text = Path(rel).read_text(encoding="utf-8")
            self.assertTrue(
                has_any(text, "S — Formal specification", "S â€” Formal specification", "S - Formal specification"),
                f"{rel} missing S field"
            )
            self.assertTrue(
                has_any(text, "H — Hooks", "H â€” Hooks", "H - Hooks"),
                f"{rel} missing H field"
            )
            self.assertTrue(
                has_any(text, "A — Artifacts", "A â€” Artifacts", "A - Artifacts"),
                f"{rel} missing A field"
            )
            self.assertTrue(
                has_any(text, "I — Invariants", "I â€” Invariants", "I - Invariants"),
                f"{rel} missing I field"
            )
            self.assertTrue(
                has_any(text, "E — Example", "E â€” Example", "E - Example"),
                f"{rel} missing E field"
            )


if __name__ == "__main__":
    unittest.main()