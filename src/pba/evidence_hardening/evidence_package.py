from __future__ import annotations

from pathlib import Path

from pba.evidence_hardening.hash_manifest import build_hash_manifest, hash_manifest_valid
from pba.evidence_hardening.report_chain import verify_report_chain
from pba.evidence_hardening.ledger_continuity import verify_ledger_continuity
from pba.evidence_hardening.rcc_anchor_verifier import verify_rcc_anchors
from pba.evidence_hardening.downgrade_lock_verifier import verify_downgrade_locks
from pba.evidence_hardening.failure_surface_verifier import verify_failure_surfaces


def compile_evidence_package(root: str | Path) -> dict:
    root = Path(root)

    hash_manifest = build_hash_manifest(root)
    report_chain = verify_report_chain(root)
    ledger = verify_ledger_continuity(root)
    rcc = verify_rcc_anchors(root)
    locks = verify_downgrade_locks(root)
    failures = verify_failure_surfaces(root)

    valid = (
        hash_manifest_valid(hash_manifest)
        and report_chain["report_chain_valid"]
        and ledger["ledger_continuity_valid"]
        and rcc["rcc_anchor_verification_valid"]
        and locks["downgrade_locks_valid"]
        and failures["failure_surface_preservation_valid"]
    )

    warnings = []
    if not valid:
        warnings.append("one_or_more_evidence_verifiers_failed")

    decision = "evidence_package_valid" if valid else "evidence_package_incomplete"
    if valid and warnings:
        decision = "evidence_package_valid_with_caution"
    if not locks["downgrade_locks_valid"]:
        decision = "evidence_package_rejected"

    traceability_matrix = [
        {
            "claim": "route_by_regime",
            "config": "configs/routing/regime_route_policy_v2_0.json",
            "report": "reports/routing/latest_routed_suite_report.json",
            "ledger": "ledgers/pba_decision_ledger.jsonl",
            "readme_anchor": "Current benchmark results",
        },
        {
            "claim": "routed_validation",
            "config": "configs/validation/routed_validation_policy_v2_1.json",
            "report": "reports/validation/latest_routed_validation_report.json",
            "ledger": "ledgers/pba_decision_ledger.jsonl",
            "readme_anchor": "PBSA v2.1",
        },
        {
            "claim": "external_validation",
            "config": "configs/validation/external_validation_policy_v2_2.json",
            "report": "reports/external_validation/latest_external_validation_report.json",
            "ledger": "ledgers/pba_decision_ledger.jsonl",
            "readme_anchor": "PBSA v2.2",
        },
        {
            "claim": "stress_validation",
            "config": "configs/validation/stress_validation_policy_v2_3.json",
            "report": "reports/stress_validation/latest_stress_validation_report.json",
            "ledger": "ledgers/pba_decision_ledger.jsonl",
            "readme_anchor": "PBSA v2.3",
        },
        {
            "claim": "calibration",
            "config": "configs/calibration/calibration_policy_v2_4.json",
            "report": "reports/calibration/latest_calibration_report.json",
            "ledger": "ledgers/pba_decision_ledger.jsonl",
            "readme_anchor": "PBSA v2.4",
        },
    ]

    return {
        "version": "PBSA-v2.5",
        "package_version": "1.5.0",
        "artifact_manifest": "configs/evidence/evidence_artifact_manifest_v2_5.json",
        "hash_manifest": hash_manifest,
        "traceability_matrix": traceability_matrix,
        "report_chain": report_chain,
        "ledger_continuity": ledger,
        "rcc_anchor_verification": rcc,
        "downgrade_locks": locks,
        "failure_surface_status": failures["failure_surface_status"],
        "failure_surface_preservation_valid": failures["failure_surface_preservation_valid"],
        "decision": decision,
        "warnings": warnings,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": locks["downgrade_locks_valid"],
        "rcc_contract_preserved": rcc["rcc_anchor_verification_valid"],
        "non_claim_boundary": "computational evidence packaging only; not biological validation, medical safety, or mechanism proof",
    }
