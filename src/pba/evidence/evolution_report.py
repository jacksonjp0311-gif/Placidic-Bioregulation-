from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evaluation.regime_detector import detect_regime
from pba.evaluation.baseline_advantage import map_baseline_advantage_from_runs
from pba.evolution.kernel_candidate import propose_candidate
from pba.evolution.champion_challenger import compare_champion_challenger
from pba.evolution.evolution_policy import load_evolution_policy
from pba.evidence.runtime_ledger import append_ledger


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def _latest_suite_summary(root: Path) -> Path:
    summary_root = root / "reports" / "suite_summaries"
    candidates = sorted(summary_root.glob("*/suite_summary.json"), key=lambda p: str(p), reverse=True)
    if not candidates:
        raise FileNotFoundError("No suite_summary.json found under reports/suite_summaries.")
    return candidates[0]


def _run_record_from_artifacts(run_dir: Path, fallback: dict) -> dict:
    record = dict(fallback)
    for name, key in [
        ("pba_metrics.json", "pba_metrics"),
        ("metric_comparison.json", "comparison"),
        ("classification.json", "classification_record"),
        ("domain_config.json", "domain_config"),
    ]:
        path = run_dir / name
        if path.exists():
            record[key] = _read_json(path)

    if "domain_config" in record:
        record["domain_id"] = record["domain_config"].get("domain_id", record.get("domain_id", "unknown"))

    if "comparison" in record:
        record.update(record["comparison"])

    if "classification_record" in record:
        record["classification"] = record["classification_record"].get("classification", record.get("classification"))

    return record


def build_evolution_report(
    root: str | Path,
    suite_summary_path: str | Path | None = None,
    policy_path: str | Path | None = None,
    candidate_summary_path: str | Path | None = None,
) -> dict:
    root = Path(root)
    suite_summary_path = Path(suite_summary_path) if suite_summary_path else _latest_suite_summary(root)
    policy_path = Path(policy_path) if policy_path else root / "configs" / "evolution_policy.json"

    suite_summary = _read_json(suite_summary_path)
    policy = load_evolution_policy(policy_path)

    enriched_runs = []
    for run in suite_summary.get("runs", []):
        run_dir_text = run.get("run_dir") or run.get("path")
        if run_dir_text:
            run_dir = Path(run_dir_text)
            if not run_dir.is_absolute():
                run_dir = root / run_dir
            if run_dir.exists():
                enriched_runs.append(_run_record_from_artifacts(run_dir, run))
                continue
        enriched_runs.append(run)

    baseline_map = map_baseline_advantage_from_runs(enriched_runs)

    regime_map = {}
    for run in enriched_runs:
        domain = str(run.get("domain_id", "unknown"))
        metrics = run.get("pba_metrics", run.get("metrics", {}))
        comparison = run.get("comparison", run)
        regime_map[domain] = detect_regime(domain, metrics=metrics, comparison=comparison)

    candidate = propose_candidate(suite_summary, regime_map, baseline_map)

    candidate_summary = None
    if candidate_summary_path:
        candidate_summary = _read_json(Path(candidate_summary_path))

    decision = compare_champion_challenger(suite_summary, candidate_summary, policy)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-EVO-" + now

    report = {
        "evolution_report_id": report_id,
        "version": "PBSA-v1.1",
        "mode": policy.get("mode", "diagnostic_first"),
        "source_suite_summary": str(suite_summary_path),
        "champion_kernel": "current",
        "candidate_kernel": candidate.get("candidate_kernel"),
        "kernel_mutation_allowed": bool(policy.get("kernel_mutation_allowed", False)),
        "motivation": candidate.get("motivation"),
        "suite_evidence": suite_summary,
        "regime_map": regime_map,
        "baseline_advantage_map": baseline_map,
        "candidate_change": candidate,
        "decision": decision.get("decision"),
        "decision_reason": decision.get("decision_reason"),
        "non_claim_locks_preserved": bool(decision.get("non_claim_locks_preserved", True)),
        "memory_promotion": {
            "promote": True,
            "reason": "Promote diagnostic regime lessons, baseline-superiority lessons, and RCC constraints only.",
        },
    }

    out_dir = root / "reports" / "evolution" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "evolution_report.json"
    md_path = out_dir / "evolution_report.md"
    _write_json(json_path, report)
    md_path.write_text(render_evolution_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "evolution" / "latest_evolution_report.json"
    latest_md = root / "reports" / "evolution" / "latest_evolution_report.md"
    _write_json(latest_json, report)
    latest_md.write_text(render_evolution_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v1_1_evolution_report_generated",
        "report_id": report_id,
        "decision": report["decision"],
        "suite_summary": str(suite_summary_path),
    })

    return {
        "status": "complete",
        "evolution_report_json": str(json_path),
        "evolution_report_md": str(md_path),
        "latest_evolution_report_json": str(latest_json),
        "latest_evolution_report_md": str(latest_md),
        "decision": report["decision"],
        "overall_classification": suite_summary.get("overall_classification"),
    }


def render_evolution_markdown(report: dict) -> str:
    lines = [
        "# PBSA v1.1 Evolution Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['evolution_report_id']}",
        f"- Version: {report['version']}",
        f"- Mode: {report['mode']}",
        f"- Decision: {report['decision']}",
        f"- Reason: {report['decision_reason']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Suite Evidence",
        "",
        f"- Overall classification: {report.get('suite_evidence', {}).get('overall_classification')}",
        f"- Source suite summary: {report.get('source_suite_summary')}",
        "",
        "## Baseline Advantage Map",
        "",
    ]

    for domain, item in report.get("baseline_advantage_map", {}).items():
        lines.append(f"- {domain}: {item.get('winner')} ({item.get('baseline_result')})")

    lines.extend(["", "## Regime Map", ""])

    for domain, item in report.get("regime_map", {}).items():
        lines.append(f"- {domain}: {item.get('detected_regime')} ({item.get('confidence')}) - {item.get('recommendation')}")

    lines.extend([
        "",
        "## Candidate Change",
        "",
        report.get("candidate_change", {}).get("summary", ""),
        "",
        "## Non-Claim Boundary",
        "",
        "This report is computational diagnostic evidence only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
