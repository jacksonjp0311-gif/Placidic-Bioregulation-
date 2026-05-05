from __future__ import annotations

from pba.routing.route_registry import get_route


def select_route(
    domain_id: str,
    primary_regime: str,
    secondary_regimes: list[str] | None = None,
    evidence: dict | None = None,
) -> dict:
    secondary_regimes = secondary_regimes or []
    evidence = evidence or {}

    if "low_confidence" in secondary_regimes or primary_regime in {"unknown", "", None}:
        route_id = "reject_route_selection"
        reason = "Low confidence or unknown primary regime."

    elif primary_regime == "direct_recovery" and "baseline_advantage" in secondary_regimes:
        route_id = "baseline_proportional_route"
        reason = "Baseline advantage in direct recovery regime."

    elif primary_regime == "pulse_recovery" and "baseline_advantage" in secondary_regimes:
        route_id = "baseline_or_pulse_candidate_review"
        reason = "Pulse recovery with baseline advantage requires route review."

    elif primary_regime == "oscillatory" and "pba_advantage" in secondary_regimes:
        route_id = "champion_pba_route"
        reason = "PBA advantage in oscillatory regime supports champion route."

    elif primary_regime == "noisy":
        route_id = "candidate_noisy_guard_route_pending_review"
        reason = "Noisy regime supports candidate guard route under review."

    else:
        route_id = "preserve_champion_route"
        reason = "Fallback preserves champion route."

    route = get_route(route_id)

    return {
        "domain_id": domain_id,
        "primary_regime": primary_regime,
        "secondary_regimes": secondary_regimes,
        "selected_route": route.route_id,
        "route_family": route.route_family,
        "selection_reason": reason,
        "manual_review_required": route.manual_review_required,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_boundary": "computational route selection only",
    }


def route_decision_for_domain(regime_record: dict) -> dict:
    return select_route(
        domain_id=regime_record.get("domain_id", "unknown"),
        primary_regime=regime_record.get("primary_regime", regime_record.get("detected_regime", "unknown")),
        secondary_regimes=regime_record.get("secondary_regimes", []),
        evidence=regime_record,
    )
