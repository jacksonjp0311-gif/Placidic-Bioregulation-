from __future__ import annotations


def suite_score(domain_scores: list[dict], key: str = "routed_score") -> float:
    if not domain_scores:
        return 0.0
    return round(sum(float(item.get(key, 0.0)) for item in domain_scores), 6)


def control_suite_scores(domain_scores: list[dict]) -> dict:
    totals: dict[str, float] = {}
    for item in domain_scores:
        for policy, score in item.get("control_scores", {}).items():
            totals[policy] = totals.get(policy, 0.0) + float(score)
    return {k: round(v, 6) for k, v in totals.items()}


def best_control_policy(control_scores: dict) -> str:
    if not control_scores:
        return "none"
    return min(control_scores, key=control_scores.get)


def route_advantage(routed_suite_score: float, best_control_score: float) -> float:
    return round(float(best_control_score) - float(routed_suite_score), 6)


def route_preservation_score(domain_scores: list[dict], epsilon: float = 0.000001) -> float:
    if not domain_scores:
        return 1.0
    preserved = 0
    for item in domain_scores:
        routed = float(item.get("routed_score", 0.0))
        best = float(item.get("best_control_score", 0.0))
        if routed <= best + epsilon:
            preserved += 1
    return round(preserved / len(domain_scores), 6)


def validation_decision(routed_advantage_value: float, preservation_score: float, failure_count: int) -> str:
    if routed_advantage_value > 0 and preservation_score >= 1.0 and failure_count == 0:
        return "validate_routing"
    if routed_advantage_value >= 0 and preservation_score >= 0.80:
        return "validate_with_caution"
    if routed_advantage_value >= -0.10 and preservation_score >= 0.50:
        return "preserve_routing_for_review"
    return "reject_routing"
