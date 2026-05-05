from __future__ import annotations


def stress_advantage_drift(stress_advantage: float, external_advantage: float) -> float:
    return round(float(stress_advantage) - float(external_advantage), 6)


def safe_fail_score(decisions: list[dict]) -> float:
    unsafe = [d for d in decisions if bool(d.get("unsafe", False)) or bool(d.get("safe_fail_required", False))]
    if not unsafe:
        return 1.0

    safe = [
        d for d in unsafe
        if d.get("selected_route") == "reject_route_selection"
        or d.get("route_family") == "reject"
        or bool(d.get("manual_review_required", False))
    ]
    return round(len(safe) / len(unsafe), 6)


def crash_rate(decisions: list[dict]) -> float:
    if not decisions:
        return 0.0
    crashes = [d for d in decisions if bool(d.get("crash", False))]
    return round(len(crashes) / len(decisions), 6)


def stress_frequency(decisions: list[dict]) -> dict:
    total = len(decisions)
    if total == 0:
        return {}
    counts: dict[str, int] = {}
    for item in decisions:
        route = item.get("selected_route", "unknown")
        counts[route] = counts.get(route, 0) + 1
    return {k: round(v / total, 6) for k, v in counts.items()}
