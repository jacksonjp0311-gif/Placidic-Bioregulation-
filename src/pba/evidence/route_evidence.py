from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.routing.route_eligibility import route_is_eligible


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_route_evidence(root: str | Path, route_decision: dict, evidence_sources: dict | None = None) -> dict:
    root = Path(root)
    evidence_sources = evidence_sources or {
        "original_suite": True,
        "holdout_suite": True,
        "champion_challenger_report": True,
    }

    route = {
        "route_id": route_decision.get("selected_route"),
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }

    eligibility = route_is_eligible(route, {
        "non_claim_locks": ["not_medical", "not_biological_law", "not_mechanism_proof"]
    })

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    route_evidence_id = "PBSA-ROUTE-" + now + "-" + route_decision.get("domain_id", "unknown")

    package = {
        "route_evidence_id": route_evidence_id,
        "version": "PBSA-v2.0",
        "domain_id": route_decision.get("domain_id"),
        "primary_regime": route_decision.get("primary_regime"),
        "secondary_regimes": route_decision.get("secondary_regimes", []),
        "selected_route": route_decision.get("selected_route"),
        "route_family": route_decision.get("route_family"),
        "alternatives_considered": [
            "baseline_proportional_route",
            "champion_pba_route",
            "candidate_noisy_guard_route_pending_review",
            "reject_route_selection",
        ],
        "selection_reason": route_decision.get("selection_reason"),
        "manual_review_required": route_decision.get("manual_review_required", False),
        "evidence_sources": evidence_sources,
        "eligibility": eligibility,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": eligibility["non_claim_locks_preserved"],
        "rcc_contract_preserved": True,
        "non_claim_boundary": "computational route selection only",
    }

    out_dir = root / "reports" / "routing" / "route_evidence"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / (route_evidence_id + ".json")
    _write_json(path, package)
    package["path"] = str(path)
    return package
