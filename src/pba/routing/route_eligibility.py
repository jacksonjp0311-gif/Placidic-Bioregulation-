from __future__ import annotations

REQUIRED_NON_CLAIM_LOCKS = {"not_medical", "not_biological_law", "not_mechanism_proof"}


def non_claim_locks_valid(locks: list[str] | set[str] | tuple[str, ...] | None) -> bool:
    return REQUIRED_NON_CLAIM_LOCKS.issubset(set(locks or []))


def route_is_eligible(route: dict, evidence: dict | None = None) -> dict:
    evidence = evidence or {}

    automatic_replacement = bool(route.get("automatic_kernel_replacement_allowed", False))
    kernel_mutation = bool(route.get("kernel_mutation_allowed", False))
    biological_validation = bool(route.get("routing_is_biological_validation", False))

    locks = evidence.get("non_claim_locks", ["not_medical", "not_biological_law", "not_mechanism_proof"])
    locks_ok = non_claim_locks_valid(locks)

    eligible = not automatic_replacement and not kernel_mutation and not biological_validation and locks_ok

    reasons = []
    if automatic_replacement:
        reasons.append("automatic_kernel_replacement_forbidden")
    if kernel_mutation:
        reasons.append("kernel_mutation_forbidden")
    if biological_validation:
        reasons.append("routing_is_not_biological_validation")
    if not locks_ok:
        reasons.append("non_claim_locks_missing")

    return {
        "eligible": eligible,
        "reasons": reasons,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": locks_ok,
    }
