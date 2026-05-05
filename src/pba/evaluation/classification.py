from __future__ import annotations

FORBIDDEN_CLAIMS = {
    "medical_claim",
    "biological_law_claim",
    "mechanism_proof_claim",
    "clinical_validation_claim",
    "coherence_as_truth_claim"
}


def classify(comparison: dict, identifiability: dict, non_claim_locks_preserved: bool, failure_flags: list[str] | None = None) -> dict:
    failure_flags = failure_flags or []

    if any(flag in FORBIDDEN_CLAIMS for flag in failure_flags) or not non_claim_locks_preserved:
        label = "PBA-E"
        path = "Rejected because non-claim lock was violated."
    elif comparison["baseline_result"] == "pba_advantage" and identifiability["status"] == "stable":
        label = "PBA-A"
        path = "Strong local implementation benchmark result under declared toy conditions."
    elif comparison["baseline_result"] == "pba_advantage":
        label = "PBA-B"
        path = "Useful local result, downgraded by identifiability caution."
    elif comparison["baseline_result"] == "tie":
        label = "PBA-C"
        path = "Simpler baseline performs equally well."
    else:
        label = "PBA-C"
        path = "Simpler baseline performs better."

    return {
        "classification": label,
        "PBAScore": 1.0 if label == "PBA-A" else 0.5 if label == "PBA-B" else 0.25 if label == "PBA-C" else 0.0,
        "baseline_result": comparison["baseline_result"],
        "identifiability_status": identifiability["status"],
        "downgrade_path": path,
        "falsification_note": "",
        "non_claim_locks_preserved": non_claim_locks_preserved
    }