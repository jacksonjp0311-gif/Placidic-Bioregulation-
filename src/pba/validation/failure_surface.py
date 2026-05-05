from __future__ import annotations


def classify_failure(domain_score: dict) -> str | None:
    advantage = float(domain_score.get("route_advantage", 0.0))
    manual_review = bool(domain_score.get("manual_review_required", False))
    route_family = domain_score.get("route_family", "unknown")
    best_control = domain_score.get("best_control_policy", "unknown")

    if advantage < 0:
        return "route_underperformed_best_control"
    if manual_review and route_family not in {"reject", "baseline_or_candidate_review", "candidate"}:
        return "manual_review_overused"
    if route_family == "candidate" and best_control == "baseline_only":
        return "candidate_route_weak"
    if route_family == "baseline" and best_control == "champion_only":
        return "baseline_route_missed"
    if route_family == "champion" and best_control == "baseline_only":
        return "champion_route_missed"
    if route_family == "reject" and best_control != "reject_manual_review":
        return "low_confidence_route"
    return None


def build_failure_surface(domain_scores: list[dict]) -> list[dict]:
    failures = []
    for item in domain_scores:
        reason = classify_failure(item)
        if reason:
            failures.append({
                "domain_id": item.get("domain_id", "unknown"),
                "route": item.get("selected_route", "unknown"),
                "route_family": item.get("route_family", "unknown"),
                "best_control_policy": item.get("best_control_policy", "unknown"),
                "delta_score": item.get("route_advantage", 0.0),
                "failure_reason": reason,
            })
    return failures
