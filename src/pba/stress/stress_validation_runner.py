from __future__ import annotations

import json
from pathlib import Path

from pba.routing.route_selector import select_route
from pba.stress.contradiction_detector import detect_contradiction
from pba.stress.malformed_input_guard import inspect_stress_domain, safe_fail_decision
from pba.stress.stress_domain_loader import load_stress_suite
from pba.stress.stress_failure_surface import build_stress_failure_surface
from pba.stress.stress_route_drift import crash_rate, safe_fail_score, stress_advantage_drift, stress_frequency
from pba.validation.control_policies import score_domain
from pba.validation.route_metrics import best_control_policy, control_suite_scores, route_advantage, suite_score


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_external_validation_report(root: Path) -> Path:
    p = root / "reports" / "external_validation" / "latest_external_validation_report.json"
    if p.exists():
        return p
    candidates = sorted(
        (root / "reports" / "external_validation").glob("PBSA-EXTERNAL-VALIDATION-*/external_validation_report.json"),
        key=lambda x: str(x),
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("No external validation report found. Run external-validation-report first.")
    return candidates[0]


def run_stress_validation(root: str | Path) -> dict:
    root = Path(root)
    domains = load_stress_suite(root)
    external_path = _latest_external_validation_report(root)
    external_report = _read_json(external_path)

    decisions = []
    scores = []

    for domain in domains:
        try:
            guard = inspect_stress_domain(domain)

            if guard["status"] == "reject":
                decision = safe_fail_decision(domain, "malformed_input_rejected")
                decision["safe_fail_required"] = True
                decision["unsafe"] = True
            else:
                contradiction = detect_contradiction(domain.get("primary_regime"), domain.get("secondary_regimes", []))

                if contradiction["contradiction"]:
                    decision = safe_fail_decision(domain, "contradiction_detected")
                    decision["safe_fail_required"] = True
                    decision["unsafe"] = True
                    decision["contradiction_reasons"] = contradiction["reasons"]
                else:
                    decision = select_route(
                        domain_id=domain["domain_id"],
                        primary_regime=domain["primary_regime"],
                        secondary_regimes=domain.get("secondary_regimes", []),
                        evidence=domain,
                    )
                    decision["family"] = domain["family"]
                    decision["stress_type"] = domain["stress_type"]
                    decision["unsafe"] = bool(domain.get("unsafe", False))
                    decision["safe_fail_required"] = bool(domain.get("unsafe", False))
                    decision["safe_fail"] = bool(decision.get("manual_review_required", False) or decision.get("route_family") == "reject")
                    decision["crash"] = False

                    if decision["safe_fail_required"] and not decision["safe_fail"]:
                        # Guarded fallback: unsafe stress pressure cannot keep a confident route.
                        decision["selected_route"] = "reject_route_selection"
                        decision["route_family"] = "reject"
                        decision["manual_review_required"] = True
                        decision["safe_fail"] = True
                        decision["failure_reason"] = "unsafe_route_guarded_to_reject"

            decisions.append(decision)
            scores.append(score_domain(decision))

        except Exception as exc:
            decision = {
                "domain_id": domain.get("domain_id", "unknown_crash_domain"),
                "family": domain.get("family", "unknown"),
                "stress_type": domain.get("stress_type", "unknown"),
                "selected_route": "reject_route_selection",
                "route_family": "reject",
                "manual_review_required": True,
                "safe_fail": True,
                "safe_fail_required": True,
                "unsafe": True,
                "crash": False,
                "failure_reason": f"exception_guarded:{type(exc).__name__}",
                "automatic_kernel_replacement_allowed": False,
                "kernel_mutation_allowed": False,
            }
            decisions.append(decision)
            scores.append(score_domain(decision))

    stress_total = suite_score(scores, "routed_score")
    control_totals = control_suite_scores(scores)
    best_control = best_control_policy(control_totals)
    best_control_total = control_totals.get(best_control, 0.0)
    stress_advantage = route_advantage(stress_total, best_control_total)

    external_advantage = float(external_report.get("external_routed_advantage", 0.0))
    advantage_drift = stress_advantage_drift(stress_advantage, external_advantage)

    failures = build_stress_failure_surface(decisions, scores)
    safe_score = safe_fail_score(decisions)
    crash = crash_rate(decisions)

    decision = stress_decision(
        stress_advantage=stress_advantage,
        safe_fail=safe_score,
        crash=crash,
        failure_count=len(failures),
    )

    return {
        "version": "PBSA-v2.3",
        "route_policy": "regime_route_policy_v2_0",
        "stress_suite": "stress_validation_suite_v2_3",
        "stress_domain_families": [d.get("family", "unknown") for d in domains],
        "source_external_validation_report": str(external_path),
        "external_routed_advantage": external_advantage,
        "stress_routed_advantage": stress_advantage,
        "stress_advantage_drift": advantage_drift,
        "safe_fail_score": safe_score,
        "crash_rate": crash,
        "stress_route_frequency": stress_frequency(decisions),
        "stress_control_suite_scores": control_totals,
        "stress_best_control_policy": best_control,
        "stress_route_decisions": decisions,
        "stress_domain_scores": scores,
        "stress_failure_surface": failures,
        "stress_failure_count": len(failures),
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "non_claim_boundary": "computational stress/adversarial validation only; not biological validation or medical safety",
    }


def stress_decision(stress_advantage: float, safe_fail: float, crash: float, failure_count: int) -> str:
    if crash > 0:
        return "stress_reject_routing"
    if safe_fail >= 1.0 and stress_advantage >= 0 and failure_count == 0:
        return "stress_validate_routing"
    if safe_fail >= 1.0 and stress_advantage >= -0.25:
        return "stress_validate_with_caution"
    if safe_fail >= 0.75:
        return "stress_preserve_routing_for_review"
    return "stress_reject_routing"
