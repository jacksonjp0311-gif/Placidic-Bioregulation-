from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evaluation.regime_detector import detect_regime
from pba.evidence.runtime_ledger import append_ledger


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def _latest_holdout_suite_summary(root: Path) -> Path:
    candidates = sorted(
        (root / "reports" / "suite_summaries").glob("suite_holdout_v1_3_*/suite_summary.json"),
        key=lambda p: str(p),
        reverse=True,
    )
    if not candidates:
        raise FileNotFoundError("No PBSA v1.3 holdout suite summary found. Run the holdout suite first.")
    return candidates[0]


def _load_run_record(run_dir: Path, fallback: dict) -> dict:
    record = dict(fallback)
    for name, key in [
        ("domain_config.json", "domain_config"),
        ("pba_metrics.json", "pba_metrics"),
        ("metric_comparison.json", "comparison"),
        ("classification.json", "classification_record"),
    ]:
        p = run_dir / name
        if p.exists():
            record[key] = _read_json(p)

    if "domain_config" in record:
        record["domain_id"] = record["domain_config"].get("domain_id", record.get("domain_id", "unknown"))
        record["non_claim_locks"] = record["domain_config"].get("non_claim_locks", [])

    if "comparison" in record:
        record.update(record["comparison"])

    if "classification_record" in record:
        record["classification"] = record["classification_record"].get("classification", record.get("classification"))

    return record


def build_regime_coverage(regime_map: dict) -> dict:
    primary = []
    secondary = []
    risks = []

    for item in regime_map.values():
        p = item.get("primary_regime")
        if p and p not in primary:
            primary.append(p)

        for value in item.get("secondary_regimes", []):
            if value not in secondary:
                secondary.append(value)

        for value in item.get("risk_overlays", []):
            if value not in risks:
                risks.append(value)

    return {
        "primary_regimes": sorted(primary),
        "secondary_overlays": sorted(secondary),
        "risk_overlays": sorted(risks),
        "coverage_count": {
            "primary_regimes": len(primary),
            "secondary_overlays": len(secondary),
            "risk_overlays": len(risks),
        },
    }


def compile_holdout_summary(
    root: str | Path,
    suite_summary_path: str | Path | None = None,
) -> dict:
    root = Path(root)
    suite_summary_path = Path(suite_summary_path) if suite_summary_path else _latest_holdout_suite_summary(root)
    suite_summary = _read_json(suite_summary_path)

    enriched_runs = []
    for run in suite_summary.get("runs", []):
        run_dir_text = run.get("run_dir") or run.get("path")
        if run_dir_text:
            run_dir = Path(run_dir_text)
            if not run_dir.is_absolute():
                run_dir = root / run_dir
            if run_dir.exists():
                enriched_runs.append(_load_run_record(run_dir, run))
                continue
        enriched_runs.append(run)

    regime_map = {}
    all_non_claim_locks_preserved = True

    for run in enriched_runs:
        domain = str(run.get("domain_id", "unknown"))
        regime_map[domain] = detect_regime(
            domain,
            metrics=run.get("pba_metrics", run.get("metrics", {})),
            comparison=run.get("comparison", run),
        )
        locks = set(run.get("non_claim_locks", []))
        if not {"not_medical", "not_biological_law", "not_mechanism_proof"}.issubset(locks):
            all_non_claim_locks_preserved = False

    coverage = build_regime_coverage(regime_map)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    summary_id = "PBSA-HOLDOUT-" + now

    holdout_summary = {
        "holdout_summary_id": summary_id,
        "version": "PBSA-v1.3",
        "suite_name": suite_summary.get("suite_name", "suite_holdout_v1_3"),
        "source_suite_summary": str(suite_summary_path),
        "run_count": len(enriched_runs),
        "overall_classification": suite_summary.get("overall_classification"),
        "classification_counts": suite_summary.get("classification_counts", {}),
        "regime_map": regime_map,
        "regime_coverage": coverage,
        "candidate_readiness": {
            "ready": True,
            "allowed_actions": ["specify_candidate"],
            "forbidden_actions": ["replace_kernel", "promote_candidate", "execute_candidate_kernel"],
        },
        "decision": "preserve_champion",
        "kernel_mutation_allowed": False,
        "candidate_execution_allowed": False,
        "non_claim_locks_preserved": all_non_claim_locks_preserved,
        "non_claim_boundary": "computational holdout evidence only; not biological validation",
    }

    out_dir = root / "reports" / "holdout" / summary_id
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "holdout_summary.json"
    md_path = out_dir / "holdout_summary.md"

    _write_json(json_path, holdout_summary)
    md_path.write_text(render_holdout_markdown(holdout_summary), encoding="utf-8")

    latest_json = root / "reports" / "holdout" / "latest_holdout_summary.json"
    latest_md = root / "reports" / "holdout" / "latest_holdout_summary.md"
    _write_json(latest_json, holdout_summary)
    latest_md.write_text(render_holdout_markdown(holdout_summary), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v1_3_holdout_summary_generated",
        "holdout_summary_id": summary_id,
        "decision": "preserve_champion",
        "suite_summary": str(suite_summary_path),
    })

    return {
        "status": "complete",
        "holdout_summary_json": str(json_path),
        "holdout_summary_md": str(md_path),
        "latest_holdout_summary_json": str(latest_json),
        "latest_holdout_summary_md": str(latest_md),
        "decision": "preserve_champion",
        "overall_classification": holdout_summary["overall_classification"],
        "run_count": holdout_summary["run_count"],
    }


def render_holdout_markdown(summary: dict) -> str:
    lines = [
        "# PBSA v1.3 Holdout Summary",
        "",
        "## Status",
        "",
        f"- Summary ID: {summary['holdout_summary_id']}",
        f"- Version: {summary['version']}",
        f"- Suite: {summary['suite_name']}",
        f"- Run count: {summary['run_count']}",
        f"- Overall classification: {summary.get('overall_classification')}",
        f"- Decision: {summary.get('decision')}",
        f"- Kernel mutation allowed: {summary.get('kernel_mutation_allowed')}",
        f"- Candidate execution allowed: {summary.get('candidate_execution_allowed')}",
        "",
        "## Regime Coverage",
        "",
        f"- Primary regimes: {summary.get('regime_coverage', {}).get('primary_regimes', [])}",
        f"- Secondary overlays: {summary.get('regime_coverage', {}).get('secondary_overlays', [])}",
        f"- Risk overlays: {summary.get('regime_coverage', {}).get('risk_overlays', [])}",
        "",
        "## Domain Regimes",
        "",
    ]

    for domain, item in summary.get("regime_map", {}).items():
        lines.append(
            f"- {domain}: primary={item.get('primary_regime')}; "
            f"secondary={item.get('secondary_regimes', [])}; "
            f"risks={item.get('risk_overlays', [])}"
        )

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational holdout evidence only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
