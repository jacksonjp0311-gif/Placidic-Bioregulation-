from __future__ import annotations

REQUIRED_STRESS_FIELDS = {
    "domain_id",
    "family",
    "stress_type",
    "primary_regime",
    "secondary_regimes",
    "stress",
}


def inspect_stress_domain(domain: dict) -> dict:
    missing = sorted(REQUIRED_STRESS_FIELDS - set(domain))
    invalid = []

    if "secondary_regimes" in domain and not isinstance(domain["secondary_regimes"], list):
        invalid.append("secondary_regimes_must_be_list")
    if "stress" in domain and domain.get("stress") is not True:
        invalid.append("stress_must_be_true")

    if missing:
        status = "reject"
    elif invalid:
        status = "reject"
    else:
        status = "valid"

    return {
        "status": status,
        "missing_fields": missing,
        "invalid_fields": invalid,
        "safe_fail_required": status == "reject",
    }


def safe_fail_decision(domain: dict, reason: str) -> dict:
    return {
        "domain_id": domain.get("domain_id", "unknown_malformed_domain"),
        "family": domain.get("family", "malformed"),
        "stress_type": domain.get("stress_type", "malformed_input"),
        "primary_regime": domain.get("primary_regime", "unknown"),
        "secondary_regimes": domain.get("secondary_regimes", [] if isinstance(domain.get("secondary_regimes", []), list) else ["invalid_secondary_regimes"]),
        "selected_route": "reject_route_selection",
        "route_family": "reject",
        "manual_review_required": True,
        "safe_fail": True,
        "crash": False,
        "failure_reason": reason,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_boundary": "computational safe-fail route only",
    }
