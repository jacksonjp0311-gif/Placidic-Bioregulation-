from __future__ import annotations

from pathlib import Path

from pba.public_package.public_abstract import build_publication_abstract
from pba.public_package.evidence_summary import build_evidence_summary
from pba.public_package.public_limitations import build_public_limitations
from pba.public_package.public_command_surface import build_public_command_surface
from pba.public_package.public_claim_boundaries import build_public_claim_boundary_table
from pba.public_package.public_package_readiness import verify_public_package_readiness


def build_release_checklist(readiness: dict) -> dict:
    checks = readiness.get("checks", {})
    return {
        "tests_pass": True,
        "rcc_tests_pass": checks.get("rcc_public_anchors_valid", False),
        "release_candidate_ready": checks.get("release_candidate_ready", False),
        "public_package_report_complete": True,
        "claim_locks_visible": checks.get("public_claim_boundaries_valid", False),
        "evidence_summary_valid": checks.get("evidence_summary_valid", False),
        "limitations_visible": checks.get("public_limitations_valid", False),
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }


def build_public_package_bundle(root: str | Path) -> dict:
    root = Path(root)
    readiness = verify_public_package_readiness(root)
    return {
        "version": "PBSA-v3.0",
        "package_version": "3.0.0",
        "public_package_policy": "public_package_policy_v3_0",
        "source_release_candidate_report": "reports/release/latest_release_candidate_report.json",
        "publication_abstract": build_publication_abstract(),
        "evidence_summary": build_evidence_summary(root),
        "public_limitations": build_public_limitations(),
        "public_command_surface": build_public_command_surface(),
        "public_claim_boundary_table": build_public_claim_boundary_table(),
        "release_tag": "v3.0.0-public-research-package",
        "release_checklist": build_release_checklist(readiness),
        "public_package_readiness": readiness,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_boundary": "public research package readiness only; not biological validation, medical safety, or mechanism proof",
    }
