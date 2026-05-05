from __future__ import annotations

import json
from pathlib import Path

from pba.evidence.route_evidence import build_route_evidence
from pba.routing.route_selector import select_route


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_original_summary(root: Path) -> Path:
    candidates = sorted((root / "reports" / "suite_summaries").glob("suite_v1_0_*/suite_summary.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError("No original suite summary found.")
    return candidates[0]


def _latest_holdout_summary(root: Path) -> Path:
    p = root / "reports" / "holdout" / "latest_holdout_summary.json"
    if p.exists():
        return p
    candidates = sorted((root / "reports" / "holdout").glob("PBSA-HOLDOUT-*/holdout_summary.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError("No holdout summary found.")
    return candidates[0]


def _latest_champion_report(root: Path) -> Path:
    p = root / "reports" / "champion_challenger" / "latest_champion_challenger_report.json"
    if p.exists():
        return p
    candidates = sorted((root / "reports" / "champion_challenger").glob("PBSA-CC-*/champion_challenger_report.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError("No champion/challenger report found.")
    return candidates[0]


def _primary_from_domain(domain: str) -> str:
    d = domain.lower()
    if "temperature" in d or "direct" in d:
        return "direct_recovery"
    if "pulse" in d:
        return "pulse_recovery"
    if "osc" in d:
        return "oscillatory"
    if "noise" in d or "noisy" in d:
        return "noisy"
    return "unknown"


def _original_route_inputs(summary: dict) -> list[dict]:
    rows = []
    for run in summary.get("runs", []):
        domain = str(run.get("domain_id", "unknown"))
        secondary = []
        if run.get("baseline_result") == "baseline_advantage":
            secondary.append("baseline_advantage")
        if run.get("baseline_result") == "pba_advantage":
            secondary.append("pba_advantage")
        rows.append({
            "domain_id": domain,
            "primary_regime": _primary_from_domain(domain),
            "secondary_regimes": secondary,
            "source": "original_suite",
        })
    return rows


def _holdout_route_inputs(summary: dict) -> list[dict]:
    rows = []
    for domain, item in summary.get("regime_map", {}).items():
        rows.append({
            "domain_id": domain,
            "primary_regime": item.get("primary_regime", "unknown"),
            "secondary_regimes": item.get("secondary_regimes", []),
            "source": "holdout_suite",
        })
    return rows


def run_routed_suite(root: str | Path) -> dict:
    root = Path(root)

    original_path = _latest_original_summary(root)
    holdout_path = _latest_holdout_summary(root)
    champion_path = _latest_champion_report(root)

    original = _read_json(original_path)
    holdout = _read_json(holdout_path)
    champion_report = _read_json(champion_path)

    rows = _original_route_inputs(original) + _holdout_route_inputs(holdout)

    route_decisions = []
    route_evidence = []

    for row in rows:
        decision = select_route(
            domain_id=row["domain_id"],
            primary_regime=row["primary_regime"],
            secondary_regimes=row["secondary_regimes"],
            evidence=row,
        )
        decision["source"] = row["source"]
        route_decisions.append(decision)
        route_evidence.append(build_route_evidence(root, decision))

    route_counts = {}
    for d in route_decisions:
        route_counts[d["selected_route"]] = route_counts.get(d["selected_route"], 0) + 1

    manual_review_required = any(d.get("manual_review_required") for d in route_decisions)

    return {
        "version": "PBSA-v2.0",
        "route_policy": "regime_route_policy_v2_0",
        "original_suite_source": str(original_path),
        "holdout_summary_source": str(holdout_path),
        "champion_challenger_report_source": str(champion_path),
        "champion_challenger_decision": champion_report.get("decision"),
        "route_decisions": route_decisions,
        "route_evidence": route_evidence,
        "route_counts": route_counts,
        "decision": "route_by_regime",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "manual_review_required": manual_review_required,
        "non_claim_boundary": "computational routed suite only; not biological validation",
    }
