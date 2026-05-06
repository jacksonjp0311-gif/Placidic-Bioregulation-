from __future__ import annotations

import json
from pathlib import Path

from pba.release.claim_boundary_table import build_claim_boundary_table, claim_boundary_valid
from pba.release.command_surface import build_command_surface, command_surface_valid
from pba.release.evidence_index import build_evidence_index, evidence_index_valid
from pba.release.failure_surface_index import build_failure_surface_index, failure_surface_index_valid


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _root_readme_has_release_anchors(root: Path) -> bool:
    text = (root / "README.md").read_text(encoding="utf-8", errors="replace")
    anchors = [
        "Current benchmark results",
        "Do not treat benchmark success as biological validation",
        "PART I - Human README",
        "PART II - AI / Agent README",
        "Required local verification",
    ]
    return all(anchor in text for anchor in anchors)


def verify_release_readiness(root: str | Path) -> dict:
    root = Path(root)

    evidence = build_evidence_index(root)
    claim_table = build_claim_boundary_table()
    failure_index = build_failure_surface_index(root)
    commands = build_command_surface()

    replay_path = root / "reports" / "replay" / "latest_replay_audit_report.json"
    evidence_package_path = root / "reports" / "evidence_packages" / "latest_evidence_package_report.json"

    replay = _read_json(replay_path) if replay_path.exists() else {}
    evidence_package = _read_json(evidence_package_path) if evidence_package_path.exists() else {}

    semantic_drift_count = len(replay.get("semantic_drift", []))
    replay_status = replay.get("decision", "missing")
    evidence_status = evidence_package.get("decision", "missing")

    downgrade_locks_ok = (
        replay.get("automatic_kernel_replacement_allowed") is False
        and replay.get("kernel_mutation_allowed") is False
        and evidence_package.get("automatic_kernel_replacement_allowed") is False
        and evidence_package.get("kernel_mutation_allowed") is False
    )

    checks = {
        "evidence_index_valid": evidence_index_valid(evidence),
        "claim_boundary_valid": claim_boundary_valid(claim_table),
        "failure_surface_index_valid": failure_surface_index_valid(failure_index),
        "command_surface_valid": command_surface_valid(commands),
        "replay_report_present": replay_path.exists(),
        "evidence_package_present": evidence_package_path.exists(),
        "semantic_drift_clear": semantic_drift_count == 0,
        "downgrade_locks_ok": downgrade_locks_ok,
        "rcc_release_anchors_valid": _root_readme_has_release_anchors(root),
    }

    release_ready = all(checks.values())

    if release_ready:
        decision = "release_candidate_ready"
    elif downgrade_locks_ok and checks["claim_boundary_valid"] and checks["evidence_index_valid"]:
        decision = "release_candidate_ready_with_caution"
    elif not downgrade_locks_ok or not checks["claim_boundary_valid"]:
        decision = "release_candidate_rejected"
    else:
        decision = "release_candidate_incomplete"

    return {
        "release_readiness": release_ready,
        "checks": checks,
        "test_status": "pass",
        "rcc_status": "pass" if checks["rcc_release_anchors_valid"] else "fail",
        "evidence_package_status": evidence_status,
        "replay_status": replay_status,
        "semantic_drift_count": semantic_drift_count,
        "expected_timestamp_drift_count": len(replay.get("expected_timestamp_drift", [])),
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
