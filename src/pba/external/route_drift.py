from __future__ import annotations


def advantage_drift(external_advantage: float, internal_advantage: float) -> float:
    return round(float(external_advantage) - float(internal_advantage), 6)


def preservation_drift(external_preservation: float, internal_preservation: float) -> float:
    return round(float(external_preservation) - float(internal_preservation), 6)


def failure_surface_drift(external_failure_count: int, internal_failure_count: int) -> int:
    return int(external_failure_count) - int(internal_failure_count)


def route_frequency(route_decisions: list[dict]) -> dict:
    total = len(route_decisions)
    counts: dict[str, int] = {}
    for item in route_decisions:
        route = item.get("selected_route", "unknown")
        counts[route] = counts.get(route, 0) + 1
    if total == 0:
        return {}
    return {k: round(v / total, 6) for k, v in counts.items()}


def route_frequency_drift(external_decisions: list[dict], internal_decisions: list[dict]) -> dict:
    external = route_frequency(external_decisions)
    internal = route_frequency(internal_decisions)
    keys = sorted(set(external) | set(internal))
    return {k: round(external.get(k, 0.0) - internal.get(k, 0.0), 6) for k in keys}
