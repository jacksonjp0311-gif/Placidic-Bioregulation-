from __future__ import annotations


def classify_stress_failure(decision: dict, score: dict | None = None) -> str | None:
    score = score or {}

    if decision.get("crash"):
        return "stress_runtime_crash"

    if decision.get("failure_reason") == "malformed_input_rejected":
        return "stress_malformed_input_rejected"

    if decision.get("failure_reason") == "contradiction_detected":
        return "stress_contradiction_detected"

    unsafe = bool(decision.get("unsafe", False)) or bool(decision.get("safe_fail_required", False))
    safe_failed = (
        decision.get("selected_route") == "reject_route_selection"
        or decision.get("route_family") == "reject"
        or bool(decision.get("manual_review_required", False))
    )

    if unsafe and not safe_failed:
        return "stress_manual_review_underused"

    if float(score.get("route_advantage", 0.0)) < 0:
        return "stress_route_underperformed_best_control"

    if decision.get("stress_type") == "boundary_case" and decision.get("route_family") not in {"reject", "baseline_or_candidate_review"}:
        return "stress_boundary_route_instability"

    if decision.get("stress_type") == "noise_injection" and decision.get("route_family") == "candidate":
        return "stress_noise_route_instability"

    return None


def build_stress_failure_surface(decisions: list[dict], scores: list[dict]) -> list[dict]:
    score_by_domain = {s.get("domain_id"): s for s in scores}
    failures = []

    for decision in decisions:
        score = score_by_domain.get(decision.get("domain_id"), {})
        reason = classify_stress_failure(decision, score)

        if reason:
            failures.append({
                "domain_id": decision.get("domain_id", "unknown"),
                "family": decision.get("family", "unknown"),
                "stress_type": decision.get("stress_type", "unknown"),
                "route": decision.get("selected_route", "unknown"),
                "route_family": decision.get("route_family", "unknown"),
                "safe_fail": bool(decision.get("manual_review_required", False) or decision.get("route_family") == "reject"),
                "crash": bool(decision.get("crash", False)),
                "delta_score": score.get("route_advantage", 0.0),
                "failure_reason": reason,
            })

    return failures
