from __future__ import annotations

import json
from pathlib import Path

from pba.validation.control_policies import CONTROL_POLICIES, score_domain
from pba.validation.failure_surface import build_failure_surface
from pba.validation.route_metrics import (
    best_control_policy,
    control_suite_scores,
    route_advantage,
    route_preservation_score,
    suite_score,
    validation_decision,
)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_routed_suite_report(root: Path) -> Path:
    p = root / "reports" / "routing" / "latest_routed_suite_report.json"
    if p.exists():
        return p
    candidates = sorted(
        (root / "reports" / "routing").glob("PBSA-ROUTED-SUITE-*/routed_suite_report.json"),
        key=lambda x: str(x),
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("No routed suite report found. Run routed-suite-report first.")
    return candidates[0]


def run_routed_validation(root: str | Path) -> dict:
    root = Path(root)
    routed_report_path = _latest_routed_suite_report(root)
    routed_report = _read_json(routed_report_path)

    route_decisions = routed_report.get("route_decisions", [])
    domain_scores = [score_domain(item) for item in route_decisions]

    routed_total = suite_score(domain_scores, "routed_score")
    control_totals = control_suite_scores(domain_scores)
    best_control = best_control_policy(control_totals)
    best_control_total = control_totals.get(best_control, 0.0)
    advantage = route_advantage(routed_total, best_control_total)
    preservation = route_preservation_score(domain_scores)
    failures = build_failure_surface(domain_scores)
    decision = validation_decision(advantage, preservation, len(failures))

    return {
        "version": "PBSA-v2.1",
        "route_policy": routed_report.get("route_policy", "regime_route_policy_v2_0"),
        "source_routed_suite_report": str(routed_report_path),
        "control_policies": CONTROL_POLICIES,
        "suite_scope": ["original_suite", "holdout_suite"],
        "domain_scores": domain_scores,
        "routed_suite_score": routed_total,
        "control_suite_scores": control_totals,
        "best_control_policy": best_control,
        "best_control_score": best_control_total,
        "routed_advantage": advantage,
        "route_preservation_score": preservation,
        "route_failure_surface": failures,
        "route_failure_count": len(failures),
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "non_claim_boundary": "computational routed-suite validation only; not biological validation",
    }
