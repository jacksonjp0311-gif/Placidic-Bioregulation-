from __future__ import annotations

from pathlib import Path


REQUIRED_ROOT_ANCHORS = [
    "Current benchmark results",
    "Do not treat benchmark success as biological validation",
    "PART I - Human README",
    "PART II - AI / Agent README",
    "Required local verification",
    "PBSA v2.5",
]

REQUIRED_RCC_FIELDS = [
    "## Purpose",
    "## S - Formal specification",
    "## H - Hooks",
    "## A - Artifacts",
    "## T - Theory",
    "## I - Invariants",
    "## E - Example",
]


def verify_root_readme_anchors(root: str | Path) -> dict:
    root = Path(root)
    text = (root / "README.md").read_text(encoding="utf-8", errors="replace")
    missing = [anchor for anchor in REQUIRED_ROOT_ANCHORS if anchor not in text]
    return {
        "root_readme": True,
        "required_anchors": REQUIRED_ROOT_ANCHORS,
        "missing_anchors": missing,
        "root_readme_anchors_valid": len(missing) == 0,
    }


def verify_mini_readmes(root: str | Path) -> dict:
    root = Path(root)
    readmes = [
        root / "configs" / "README.md",
        root / "configs" / "evidence" / "README.md",
        root / "src" / "pba" / "evidence_hardening" / "README.md",
        root / "src" / "pba" / "evidence" / "README.md",
        root / "reports" / "README.md",
    ]

    missing_files = []
    missing_fields = {}

    for path in readmes:
        if not path.exists():
            missing_files.append(str(path.relative_to(root)))
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        misses = [field for field in REQUIRED_RCC_FIELDS if field not in text]
        if misses:
            missing_fields[str(path.relative_to(root))] = misses

    return {
        "mini_readmes": True,
        "missing_files": missing_files,
        "missing_fields": missing_fields,
        "mini_readmes_valid": not missing_files and not missing_fields,
    }


def verify_rcc_anchors(root: str | Path) -> dict:
    root_result = verify_root_readme_anchors(root)
    mini_result = verify_mini_readmes(root)
    return {
        **root_result,
        **mini_result,
        "rcc_anchor_verification_valid": root_result["root_readme_anchors_valid"] and mini_result["mini_readmes_valid"],
    }
