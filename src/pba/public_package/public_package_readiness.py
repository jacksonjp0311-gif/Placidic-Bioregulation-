from __future__ import annotations

import json
from pathlib import Path

from pba.public_package.public_abstract import build_publication_abstract, public_abstract_valid
from pba.public_package.evidence_summary import build_evidence_summary, evidence_summary_valid
from pba.public_package.public_limitations import build_public_limitations, public_limitations_valid
from pba.public_package.public_command_surface import build_public_command_surface, public_command_surface_valid
from pba.public_package.public_claim_boundaries import build_public_claim_boundary_table, public_claim_boundaries_valid


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _root_readme_has_public_anchors(root: Path) -> bool:
    text = (root / "README.md").read_text(encoding="utf-8", errors="replace")
    anchors = [
        "Current benchmark results",
        "Do not treat benchmark success as biological validation",
        "PART I - Human README",
        "PART II - AI / Agent README",
        "Required local verification",
    ]
    return all(anchor in text for anchor in anchors)


def verify_public_package_readiness(root: str | Path) -> dict:
    root = Path(root)

    abstract = build_publication_abstract()
    evidence_summary = build_evidence_summary(root)
    limitations = build_public_limitations()
    command_surface = build_public_command_surface()
    claim_table = build_public_claim_boundary_table()

    release_candidate_path = root / "reports" / "release" / "latest_release_candidate_report.json"
    release_candidate = _read_json(release_candidate_path) if release_candidate_path.exists() else {}

    release_ready = bool(release_candidate.get("release_readiness", False))
    semantic_drift_count = int(release_candidate.get("semantic_drift_count", 0))
    downgrade_locks_ok = (
        release_candidate.get("automatic_kernel_replacement_allowed") is False
        and release_candidate.get("kernel_mutation_allowed") is False
    )

    checks = {
        "publication_abstract_valid": public_abstract_valid(abstract),
        "evidence_summary_valid": evidence_summary_valid(evidence_summary),
        "public_limitations_valid": public_limitations_valid(limitations),
        "public_command_surface_valid": public_command_surface_valid(command_surface),
        "public_claim_boundaries_valid": public_claim_boundaries_valid(claim_table),
        "release_candidate_report_present": release_candidate_path.exists(),
        "release_candidate_ready": release_ready,
        "semantic_drift_clear": semantic_drift_count == 0,
        "downgrade_locks_ok": downgrade_locks_ok,
        "rcc_public_anchors_valid": _root_readme_has_public_anchors(root),
    }

    public_ready = all(checks.values())

    if public_ready:
        decision = "public_package_ready"
    elif downgrade_locks_ok and checks["public_claim_boundaries_valid"] and checks["evidence_summary_valid"]:
        decision = "public_package_ready_with_caution"
    elif not downgrade_locks_ok or not checks["public_claim_boundaries_valid"]:
        decision = "public_package_rejected"
    else:
        decision = "public_package_incomplete"

    return {
        "public_package_readiness": public_ready,
        "checks": checks,
        "release_candidate_status": release_candidate.get("decision", "missing"),
        "release_readiness": release_ready,
        "semantic_drift_count": semantic_drift_count,
        "expected_timestamp_drift_count": int(release_candidate.get("expected_timestamp_drift_count", 0)),
        "downgrade_locks": {
            "automatic_kernel_replacement_allowed": False,
            "kernel_mutation_allowed": False,
            "non_claim_locks_preserved": downgrade_locks_ok,
        },
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }
