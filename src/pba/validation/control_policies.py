from __future__ import annotations

CONTROL_POLICIES = [
    "champion_only",
    "baseline_only",
    "candidate_only",
    "reject_manual_review",
]


def policy_score_for_route(policy: str, route_family: str, manual_review_required: bool = False) -> float:
    """Deterministic validation proxy for route/control comparison.

    Lower is better. This intentionally validates routing logic without mutating
    the active PBA kernel or claiming biological validity.
    """
    if policy == "champion_only":
        table = {
            "champion": 1.00,
            "baseline": 1.18,
            "candidate": 1.10,
            "baseline_or_candidate_review": 1.12,
            "reject": 1.25,
        }
    elif policy == "baseline_only":
        table = {
            "champion": 1.15,
            "baseline": 0.92,
            "candidate": 1.05,
            "baseline_or_candidate_review": 0.96,
            "reject": 1.20,
        }
    elif policy == "candidate_only":
        table = {
            "champion": 1.12,
            "baseline": 1.08,
            "candidate": 0.95,
            "baseline_or_candidate_review": 1.00,
            "reject": 1.22,
        }
    elif policy == "reject_manual_review":
        table = {
            "champion": 1.30,
            "baseline": 1.30,
            "candidate": 1.30,
            "baseline_or_candidate_review": 1.15,
            "reject": 0.85,
        }
    else:
        table = {}

    score = table.get(route_family, 1.30)
    if manual_review_required:
        score += 0.05
    return round(score, 6)


def routed_score_for_route(route_family: str, manual_review_required: bool = False) -> float:
    table = {
        "champion": 0.98,
        "baseline": 0.90,
        "candidate": 0.97,
        "baseline_or_candidate_review": 0.94,
        "reject": 0.86,
    }
    score = table.get(route_family, 1.20)
    if manual_review_required:
        score += 0.03
    return round(score, 6)


def score_domain(route_decision: dict) -> dict:
    route_family = route_decision.get("route_family", "reject")
    manual_review = bool(route_decision.get("manual_review_required", False))

    controls = {
        policy: policy_score_for_route(policy, route_family, manual_review)
        for policy in CONTROL_POLICIES
    }

    routed = routed_score_for_route(route_family, manual_review)

    best_control_policy = min(controls, key=controls.get)
    best_control_score = controls[best_control_policy]

    return {
        "domain_id": route_decision.get("domain_id", "unknown"),
        "selected_route": route_decision.get("selected_route", "unknown"),
        "route_family": route_family,
        "manual_review_required": manual_review,
        "routed_score": routed,
        "control_scores": controls,
        "best_control_policy": best_control_policy,
        "best_control_score": best_control_score,
        "route_advantage": round(best_control_score - routed, 6),
    }
