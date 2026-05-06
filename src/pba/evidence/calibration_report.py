from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.calibration_thresholds.calibration_runner import run_calibration
from pba.evidence.runtime_ledger import append_ledger


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_calibration_report(root: str | Path) -> dict:
    root = Path(root)
    calibration = run_calibration(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-CALIBRATION-" + now

    report = {
        "calibration_report_id": report_id,
        "version": "PBSA-v2.4",
        "calibration_policy": calibration["calibration_policy"],
        "threshold_grid": calibration["threshold_grid"],
        "candidate_count": calibration["candidate_count"],
        "recommended_candidate": calibration["recommended_candidate"],
        "recommended_thresholds": calibration["recommended_thresholds"],
        "calibration_score": calibration["calibration_score"],
        "safe_fail_score_preserved": calibration["safe_fail_score_preserved"],
        "crash_rate_preserved": calibration["crash_rate_preserved"],
        "overfitting_guard_passed": calibration["overfitting_guard_passed"],
        "failure_visibility_preserved": calibration["failure_visibility_preserved"],
        "candidate_evaluations": calibration["candidate_evaluations"],
        "decision": calibration["decision"],
        "manual_review_required": calibration["manual_review_required"],
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "next_required_step": "PBSA v2.5 evidence package hardening",
        "non_claim_boundary": calibration["non_claim_boundary"],
    }

    out_dir = root / "reports" / "calibration" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "calibration_report.json"
    md_path = out_dir / "calibration_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "calibration" / "latest_calibration_report.json"
    latest_md = root / "reports" / "calibration" / "latest_calibration_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_4_calibration_report_generated",
        "calibration_report_id": report_id,
        "decision": report["decision"],
        "recommended_candidate": report["recommended_candidate"],
        "calibration_score": report["calibration_score"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "calibration_report_json": str(json_path),
        "calibration_report_md": str(md_path),
        "latest_calibration_report_json": str(latest_json),
        "latest_calibration_report_md": str(latest_md),
        "decision": report["decision"],
        "recommended_candidate": report["recommended_candidate"],
        "calibration_score": report["calibration_score"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    thresholds = report.get("recommended_thresholds", {})
    lines = [
        "# PBSA v2.4 Calibration Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['calibration_report_id']}",
        f"- Version: {report['version']}",
        f"- Calibration policy: {report['calibration_policy']}",
        f"- Threshold grid: {report['threshold_grid']}",
        f"- Candidate count: {report['candidate_count']}",
        f"- Recommended candidate: {report['recommended_candidate']}",
        f"- Calibration score: {report['calibration_score']}",
        f"- Decision: {report['decision']}",
        f"- Safe-fail score preserved: {report['safe_fail_score_preserved']}",
        f"- Crash rate preserved: {report['crash_rate_preserved']}",
        f"- Overfitting guard passed: {report['overfitting_guard_passed']}",
        f"- Failure visibility preserved: {report['failure_visibility_preserved']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Recommended Thresholds",
        "",
    ]

    for key, value in thresholds.items():
        lines.append(f"- {key}: {value}")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational calibration only. It is not medical guidance, clinical validation, biological-law proof, medical safety proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
