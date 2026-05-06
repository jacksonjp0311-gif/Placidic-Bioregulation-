from __future__ import annotations

import json
from pathlib import Path

from pba.evidence.routed_suite_report import build_routed_suite_report
from pba.evidence.routed_validation_report import build_routed_validation_report
from pba.evidence.external_validation_report import build_external_validation_report
from pba.evidence.stress_validation_report import build_stress_validation_report
from pba.evidence.calibration_report import build_calibration_report
from pba.evidence.evidence_package_report import build_evidence_package_report
from pba.evidence_hardening.hash_manifest import build_hash_manifest
from pba.evidence_hardening.ledger_continuity import verify_ledger_continuity
from pba.evidence_hardening.rcc_anchor_verifier import verify_rcc_anchors
from pba.replay.decision_replay import compare_decision_map, semantic_drift_items
from pba.replay.hash_drift import compare_hash_manifests
from pba.replay.replay_lock_verifier import replay_locks_reproduced, failure_surfaces_replayed


REPORT_PATHS = {
    "routed_suite_report": "reports/routing/latest_routed_suite_report.json",
    "routed_validation_report": "reports/validation/latest_routed_validation_report.json",
    "external_validation_report": "reports/external_validation/latest_external_validation_report.json",
    "stress_validation_report": "reports/stress_validation/latest_stress_validation_report.json",
    "calibration_report": "reports/calibration/latest_calibration_report.json",
    "evidence_package_report": "reports/evidence_packages/latest_evidence_package_report.json",
}


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_policy(root: Path) -> dict:
    return _read_json(root / "configs" / "replay" / "replay_policy_v2_6.json")


def _load_original_reports(root: Path) -> dict:
    reports = {}
    for name, rel in REPORT_PATHS.items():
        path = root / rel
        if path.exists():
            reports[name] = _read_json(path)
    return reports


def _run_replay_sequence(root: Path) -> dict:
    replay_paths = {}

    routed = build_routed_suite_report(root)
    replay_paths["routed_suite_report"] = routed.get("latest_routed_suite_report_json") or routed.get("routed_suite_report_json")

    routed_validation = build_routed_validation_report(root)
    replay_paths["routed_validation_report"] = routed_validation.get("latest_routed_validation_report_json") or routed_validation.get("routed_validation_report_json")

    external = build_external_validation_report(root)
    replay_paths["external_validation_report"] = external.get("latest_external_validation_report_json") or external.get("external_validation_report_json")

    stress = build_stress_validation_report(root)
    replay_paths["stress_validation_report"] = stress.get("latest_stress_validation_report_json") or stress.get("stress_validation_report_json")

    calibration = build_calibration_report(root)
    replay_paths["calibration_report"] = calibration.get("latest_calibration_report_json") or calibration.get("calibration_report_json")

    evidence = build_evidence_package_report(root)
    replay_paths["evidence_package_report"] = evidence.get("latest_evidence_package_report_json") or evidence.get("evidence_package_report_json")

    return replay_paths


def _load_replayed_reports(root: Path) -> dict:
    return _load_original_reports(root)


def run_replay(root: str | Path) -> dict:
    root = Path(root)
    policy = _load_policy(root)

    original_reports = _load_original_reports(root)
    original_hash_manifest = build_hash_manifest(root)

    replay_paths = _run_replay_sequence(root)

    replayed_reports = _load_replayed_reports(root)
    replay_hash_manifest = build_hash_manifest(root)

    decision_fields = policy.get("decision_fields", {})
    decision_replay = compare_decision_map(original_reports, replayed_reports, decision_fields)
    semantic_drift = semantic_drift_items(decision_replay)

    hash_drift = compare_hash_manifests(original_hash_manifest, replay_hash_manifest)

    ledger_replay = verify_ledger_continuity(root)
    rcc_replay = verify_rcc_anchors(root)
    lock_replay = replay_locks_reproduced(replayed_reports)
    failure_replay = failure_surfaces_replayed(replayed_reports)

    drift_ok = len(semantic_drift) == 0 and hash_drift["hash_drift_valid"]
    audit_ok = (
        drift_ok
        and ledger_replay["ledger_continuity_valid"]
        and rcc_replay["rcc_anchor_verification_valid"]
        and lock_replay["downgrade_locks_replayed"]
        and failure_replay["failure_surfaces_replayed"]
    )

    if audit_ok and not hash_drift["expected_timestamp_drift"]:
        decision = "replay_valid"
    elif audit_ok and hash_drift["expected_timestamp_drift"]:
        decision = "replay_valid_with_timestamp_drift"
    elif len(semantic_drift) > 0:
        decision = "replay_semantic_drift"
    elif not lock_replay["downgrade_locks_replayed"]:
        decision = "replay_rejected"
    else:
        decision = "replay_valid_with_caution"

    return {
        "version": "PBSA-v2.6",
        "package_version": "1.6.0",
        "source_evidence_package": "reports/evidence_packages/latest_evidence_package_report.json",
        "replay_policy": "replay_policy_v2_6",
        "replayed_reports": replay_paths,
        "decision_replay": {
            key: value["status"] for key, value in decision_replay.items()
        },
        "decision_replay_detail": decision_replay,
        "hash_drift": hash_drift["hash_drift"],
        "semantic_drift": semantic_drift + hash_drift["semantic_drift"],
        "expected_timestamp_drift": hash_drift["expected_timestamp_drift"],
        "ledger_replay_valid": ledger_replay["ledger_continuity_valid"],
        "rcc_replay_valid": rcc_replay["rcc_anchor_verification_valid"],
        "downgrade_locks_replayed": lock_replay["downgrade_locks_replayed"],
        "failure_surfaces_replayed": failure_replay["failure_surfaces_replayed"],
        "lock_replay_detail": lock_replay,
        "failure_surface_replay_detail": failure_replay,
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": lock_replay["downgrade_locks_replayed"],
        "rcc_contract_preserved": rcc_replay["rcc_anchor_verification_valid"],
        "non_claim_boundary": "computational reproducibility replay only; not biological validation, medical safety, or mechanism proof",
    }
