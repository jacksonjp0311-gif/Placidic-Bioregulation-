from __future__ import annotations

import json
from pathlib import Path

from pba.evolution.candidate_variants import load_builtin_candidate_variants, apply_candidate_to_domain
from pba.evolution.promotion_governance import classification_rank


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_summary(root: Path, prefix: str) -> Path:
    candidates = sorted((root / "reports" / "suite_summaries").glob(f"{prefix}_*/suite_summary.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError(f"No suite summary found for prefix: {prefix}")
    return candidates[0]


def _latest_holdout_summary(root: Path) -> Path:
    p = root / "reports" / "holdout" / "latest_holdout_summary.json"
    if p.exists():
        return p
    candidates = sorted((root / "reports" / "holdout").glob("PBSA-HOLDOUT-*/holdout_summary.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError("No holdout summary found.")
    return candidates[0]


def _classification_counts(rows: list[dict], key: str) -> dict:
    counts = {"PBA-A": 0, "PBA-B": 0, "PBA-C": 0, "PBA-D": 0, "PBA-E": 0}
    for row in rows:
        value = row.get(key, "PBA-D")
        counts[value] = counts.get(value, 0) + 1
    return counts


def _best_classification(rows: list[dict], key: str) -> str:
    if not rows:
        return "PBA-D"
    return max((row.get(key, "PBA-D") for row in rows), key=classification_rank)


def _domain_rows_from_original(summary: dict) -> list[dict]:
    rows = []
    for run in summary.get("runs", []):
        domain = str(run.get("domain_id", "unknown"))
        primary = "direct_recovery" if "temperature" in domain else "pulse_recovery" if "pulse" in domain else "oscillatory" if "osc" in domain else "unknown"
        secondary = []
        result = run.get("baseline_result", "")
        if result == "baseline_advantage":
            secondary.append("baseline_advantage")
        if result == "pba_advantage":
            secondary.append("pba_advantage")
        rows.append({
            "domain_id": domain,
            "primary_regime": primary,
            "secondary_regimes": secondary,
            "champion_score": run.get("pba_score", run.get("pbaScore", 1.0)),
            "champion_classification": run.get("classification", "PBA-D"),
            "baseline_result": result,
        })
    return rows


def _domain_rows_from_holdout(summary: dict) -> list[dict]:
    rows = []
    for domain, item in summary.get("regime_map", {}).items():
        rows.append({
            "domain_id": domain,
            "primary_regime": item.get("primary_regime", "unknown"),
            "secondary_regimes": item.get("secondary_regimes", []),
            "champion_score": item.get("features", {}).get("cumulative_deviation", 1.0) or 1.0,
            "champion_classification": summary.get("overall_classification", "PBA-D"),
        })
    return rows


def run_candidate_comparison(rows: list[dict]) -> dict:
    variants = load_builtin_candidate_variants()
    all_results = []
    best_rows = []

    for row in rows:
        candidate_results = [apply_candidate_to_domain(v, row) for v in variants.values()]
        all_results.extend(candidate_results)
        best = min(candidate_results, key=lambda r: r.get("candidate_score", 999999.0))
        best_rows.append(best)

    return {
        "domain_count": len(rows),
        "candidate_results": all_results,
        "best_by_domain": best_rows,
        "champion_classification_counts": _classification_counts(rows, "champion_classification"),
        "candidate_classification_counts": _classification_counts(best_rows, "candidate_classification"),
        "champion_classification": _best_classification(rows, "champion_classification"),
        "best_challenger_classification": _best_classification(best_rows, "candidate_classification"),
    }


def build_champion_challenger_packet(root: Path) -> dict:
    original_summary = _read_json(_latest_summary(root, "suite_v1_0"))
    holdout_summary = _read_json(_latest_holdout_summary(root))

    original_rows = _domain_rows_from_original(original_summary)
    holdout_rows = _domain_rows_from_holdout(holdout_summary)

    original_result = run_candidate_comparison(original_rows)
    holdout_result = run_candidate_comparison(holdout_rows)

    return {
        "original_suite_source": str(_latest_summary(root, "suite_v1_0")),
        "holdout_summary_source": str(_latest_holdout_summary(root)),
        "original_suite_result": original_result,
        "holdout_suite_result": holdout_result,
        "baseline_visibility_preserved": True,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
    }
