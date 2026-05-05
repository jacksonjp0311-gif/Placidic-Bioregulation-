from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evolution.candidate_spec import build_candidate_specs
from pba.evidence.runtime_ledger import append_ledger


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def _latest_holdout_summary(root: Path) -> Path:
    p = root / "reports" / "holdout" / "latest_holdout_summary.json"
    if p.exists():
        return p
    candidates = sorted((root / "reports" / "holdout").glob("PBSA-HOLDOUT-*/holdout_summary.json"), key=lambda x: str(x), reverse=True)
    if not candidates:
        raise FileNotFoundError("No holdout summary found. Run summarize-holdout first.")
    return candidates[0]


def build_candidate_readiness_report(
    root: str | Path,
    holdout_summary_path: str | Path | None = None,
) -> dict:
    root = Path(root)
    holdout_summary_path = Path(holdout_summary_path) if holdout_summary_path else _latest_holdout_summary(root)
    holdout_summary = _read_json(holdout_summary_path)
    specs = build_candidate_specs(holdout_summary)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-CANDIDATE-READY-" + now

    report = {
        "candidate_readiness_report_id": report_id,
        "version": "PBSA-v1.3",
        "source_holdout_summary": str(holdout_summary_path),
        "decision": "preserve_champion",
        "candidate_execution_allowed": False,
        "candidate_promotion_allowed": False,
        "kernel_mutation_allowed": False,
        "candidate_specs": specs,
        "candidate_spec_count": len(specs),
        "next_required_step": "PBSA v1.4 champion/challenger execution",
        "non_claim_boundary": "candidate readiness only; not candidate validation; not biological proof",
    }

    out_dir = root / "reports" / "candidates" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "candidate_readiness_report.json"
    md_path = out_dir / "candidate_readiness_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_candidate_readiness_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "candidates" / "latest_candidate_readiness_report.json"
    latest_md = root / "reports" / "candidates" / "latest_candidate_readiness_report.md"
    _write_json(latest_json, report)
    latest_md.write_text(render_candidate_readiness_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v1_3_candidate_readiness_generated",
        "candidate_readiness_report_id": report_id,
        "decision": "preserve_champion",
        "candidate_execution_allowed": False,
    })

    return {
        "status": "complete",
        "candidate_readiness_report_json": str(json_path),
        "candidate_readiness_report_md": str(md_path),
        "latest_candidate_readiness_report_json": str(latest_json),
        "latest_candidate_readiness_report_md": str(latest_md),
        "decision": "preserve_champion",
        "candidate_execution_allowed": False,
        "candidate_spec_count": len(specs),
    }


def render_candidate_readiness_markdown(report: dict) -> str:
    lines = [
        "# PBSA v1.3 Candidate Readiness Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['candidate_readiness_report_id']}",
        f"- Version: {report['version']}",
        f"- Decision: {report['decision']}",
        f"- Candidate execution allowed: {report['candidate_execution_allowed']}",
        f"- Candidate promotion allowed: {report['candidate_promotion_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        f"- Candidate spec count: {report['candidate_spec_count']}",
        f"- Next required step: {report['next_required_step']}",
        "",
        "## Candidate Specifications",
        "",
    ]

    for spec in report.get("candidate_specs", []):
        lines.extend([
            f"### {spec.get('candidate_id')}",
            "",
            f"- Status: {spec.get('status')}",
            f"- Target regimes: {spec.get('target_regimes')}",
            f"- Motivation: {spec.get('motivation')}",
            f"- Expected benefit: {spec.get('expected_benefit')}",
            f"- Risk: {spec.get('risk')}",
            f"- Source domains: {spec.get('source_domains')}",
            "",
        ])

    lines.extend([
        "## Non-Claim Boundary",
        "",
        "Candidate readiness is not candidate validation. This is not medical guidance, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
