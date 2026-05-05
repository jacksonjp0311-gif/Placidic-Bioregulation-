from __future__ import annotations

import json
from pathlib import Path

from pba.external.external_domain_loader import load_external_suite
from pba.external.external_failure_surface import build_external_failure_surface
from pba.external.route_drift import (
    advantage_drift,
    failure_surface_drift,
    preservation_drift,
    route_frequency_drift,
)
from pba.routing.route_selector import select_route
from pba.validation.control_policies import score_domain
from pba.validation.route_metrics import (
    best_control_policy,
    control_suite_scores,
    route_advantage,
    route_preservation_score,
    suite_score,
)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_internal_validation_report(root: Path) -> Path:
    p = root / "reports" / "validation" / "latest_routed_validation_report.json"
    if p.exists():
        return p
    candidates = sorted(
        (root / "reports" / "validation").glob("PBSA-ROUTED-VALIDATION-*/routed_validation_report.json"),
        key=lambda x: str(x),
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("No routed validation report found. Run routed-validation-report first.")
    return candidates[0]


def _latest_internal_routed_report(root: Path) -> Path | None:
    p = root / "reports" / "routing" / "latest_routed_suite_report.json"
    if p.exists():
        return p
    return None


def run_external_validation(root: str | Path) -> dict:
    root = Path(root)
    domains = load_external_suite(root)
    internal_validation_path = _latest_internal_validation_report(root)
    internal_validation = _read_json(internal_validation_path)

    internal_routed_path = _latest_internal_routed_report(root)
    internal_route_decisions = []
    if internal_routed_path is not None:
        internal_routed = _read_json(internal_routed_path)
        internal_route_decisions = internal_routed.get("route_decisions", [])

    route_decisions = []
    domain_scores = []

    for domain in domains:
        decision = select_route(
            domain_id=domain["domain_id"],
            primary_regime=domain["primary_regime"],
            secondary_regimes=domain.get("secondary_regimes", []),
            evidence=domain,
        )
        decision["family"] = domain["family"]
        decision["source"] = "external_validation_suite_v2_2"
        route_decisions.append(decision)

        score = score_domain(decision)
        score["family"] = domain["family"]
        domain_scores.append(score)

    external_total = suite_score(domain_scores, "routed_score")
    control_totals = control_suite_scores(domain_scores)
    best_control = best_control_policy(control_totals)
    best_control_total = control_totals.get(best_control, 0.0)
    external_advantage = route_advantage(external_total, best_control_total)
    external_preservation = route_preservation_score(domain_scores)

    internal_advantage = float(internal_validation.get("routed_advantage", 0.0))
    internal_preservation = float(internal_validation.get("route_preservation_score", 0.0))
    internal_failure_count = int(internal_validation.get("route_failure_count", len(internal_validation.get("route_failure_surface", []))))

    adv_drift = advantage_drift(external_advantage, internal_advantage)
    pres_drift = preservation_drift(external_preservation, internal_preservation)
    external_failures = build_external_failure_surface(domain_scores, advantage_drift_value=adv_drift)
    fail_drift = failure_surface_drift(len(external_failures), internal_failure_count)
    freq_drift = route_frequency_drift(route_decisions, internal_route_decisions)

    decision = external_decision(
        external_advantage=external_advantage,
        external_preservation=external_preservation,
        advantage_drift_value=adv_drift,
        failure_count=len(external_failures),
    )

    return {
        "version": "PBSA-v2.2",
        "route_policy": "regime_route_policy_v2_0",
        "external_suite": "external_validation_suite_v2_2",
        "external_domain_families": [d["family"] for d in domains],
        "source_internal_validation_report": str(internal_validation_path),
        "internal_routed_advantage": internal_advantage,
        "external_routed_advantage": external_advantage,
        "advantage_drift": adv_drift,
        "internal_preservation_score": internal_preservation,
        "external_preservation_score": external_preservation,
        "preservation_drift": pres_drift,
        "internal_failure_count": internal_failure_count,
        "external_failure_count": len(external_failures),
        "failure_surface_drift": fail_drift,
        "route_frequency_drift": freq_drift,
        "external_route_decisions": route_decisions,
        "external_domain_scores": domain_scores,
        "external_control_suite_scores": control_totals,
        "external_best_control_policy": best_control,
        "external_failure_surface": external_failures,
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "non_claim_boundary": "computational external-domain validation only; not biological validation",
    }


def external_decision(
    external_advantage: float,
    external_preservation: float,
    advantage_drift_value: float,
    failure_count: int,
) -> str:
    if external_advantage > 0 and external_preservation >= 1.0 and advantage_drift_value >= 0 and failure_count == 0:
        return "external_validate_routing"
    if external_advantage >= 0 and external_preservation >= 0.80:
        return "external_validate_with_caution"
    if external_advantage >= -0.25 and external_preservation >= 0.50:
        return "external_preserve_routing_for_review"
    return "external_reject_routing"
