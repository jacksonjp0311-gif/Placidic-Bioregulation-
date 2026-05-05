from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Route:
    route_id: str
    route_family: str
    manual_review_required: bool
    automatic_kernel_replacement_allowed: bool = False
    kernel_mutation_allowed: bool = False


def builtin_routes() -> dict[str, Route]:
    return {
        "baseline_proportional_route": Route(
            route_id="baseline_proportional_route",
            route_family="baseline",
            manual_review_required=False,
        ),
        "baseline_or_pulse_candidate_review": Route(
            route_id="baseline_or_pulse_candidate_review",
            route_family="baseline_or_candidate_review",
            manual_review_required=True,
        ),
        "champion_pba_route": Route(
            route_id="champion_pba_route",
            route_family="champion",
            manual_review_required=False,
        ),
        "candidate_noisy_guard_route_pending_review": Route(
            route_id="candidate_noisy_guard_route_pending_review",
            route_family="candidate",
            manual_review_required=True,
        ),
        "reject_route_selection": Route(
            route_id="reject_route_selection",
            route_family="reject",
            manual_review_required=True,
        ),
        "preserve_champion_route": Route(
            route_id="preserve_champion_route",
            route_family="champion",
            manual_review_required=False,
        ),
    }


def get_route(route_id: str) -> Route:
    routes = builtin_routes()
    if route_id not in routes:
        return routes["reject_route_selection"]
    return routes[route_id]
