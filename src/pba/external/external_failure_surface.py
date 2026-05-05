from __future__ import annotations

from pba.validation.failure_surface import classify_failure


def classify_external_failure(domain_score: dict, advantage_drift_value: float | None = None) -> str | None:
    base = classify_failure(domain_score)
    if base:
        return "external_" + base

    if advantage_drift_value is not None and advantage_drift_value < -0.25:
        return "external_advantage_degraded"

    if bool(domain_score.get("manual_review_required", False)) and domain_score.get("route_family") == "reject":
        return "external_low_confidence_route"

    return None


def build_external_failure_surface(domain_scores: list[dict], advantage_drift_value: float | None = None) -> list[dict]:
    failures = []
    for item in domain_scores:
        reason = classify_external_failure(item, advantage_drift_value=advantage_drift_value)
        if reason:
            failures.append({
                "domain_id": item.get("domain_id", "unknown"),
                "family": item.get("family", "unknown"),
                "route": item.get("selected_route", "unknown"),
                "route_family": item.get("route_family", "unknown"),
                "best_control_policy": item.get("best_control_policy", "unknown"),
                "delta_score": item.get("route_advantage", 0.0),
                "advantage_drift": advantage_drift_value,
                "failure_reason": reason,
            })
    return failures
