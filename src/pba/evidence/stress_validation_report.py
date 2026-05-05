from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.stress.stress_validation_runner import run_stress_validation


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_stress_validation_report(root: str | Path) -> dict:
    root = Path(root)
    validation = run_stress_validation(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-STRESS-VALIDATION-" + now

    report = {
        "stress_validation_report_id": report_id,
        "version": "PBSA-v2.3",
        "route_policy": validation["route_policy"],
        "stress_suite": validation["stress_suite"],
        "stress_domain_families": validation["stress_domain_families"],
        "source_external_validation_report": validation["source_external_validation_report"],
        "external_routed_advantage": validation["external_routed_advantage"],
        "stress_routed_advantage": validation["stress_routed_advantage"],
        "stress_advantage_drift": validation["stress_advantage_drift"],
        "safe_fail_score": validation["safe_fail_score"],
        "crash_rate": validation["crash_rate"],
        "stress_route_frequency": validation["stress_route_frequency"],
        "stress_control_suite_scores": validation["stress_control_suite_scores"],
        "stress_best_control_policy": validation["stress_best_control_policy"],
        "stress_failure_surface": validation["stress_failure_surface"],
        "stress_failure_count": validation["stress_failure_count"],
        "decision": validation["decision"],
        "manual_review_required": validation["manual_review_required"],
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "next_required_step": "PBSA v2.4 calibration and threshold tuning",
        "non_claim_boundary": validation["non_claim_boundary"],
    }

    out_dir = root / "reports" / "stress_validation" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "stress_validation_report.json"
    md_path = out_dir / "stress_validation_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "stress_validation" / "latest_stress_validation_report.json"
    latest_md = root / "reports" / "stress_validation" / "latest_stress_validation_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_3_stress_validation_report_generated",
        "stress_validation_report_id": report_id,
        "decision": report["decision"],
        "safe_fail_score": report["safe_fail_score"],
        "crash_rate": report["crash_rate"],
        "stress_advantage_drift": report["stress_advantage_drift"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "stress_validation_report_json": str(json_path),
        "stress_validation_report_md": str(md_path),
        "latest_stress_validation_report_json": str(latest_json),
        "latest_stress_validation_report_md": str(latest_md),
        "decision": report["decision"],
        "safe_fail_score": report["safe_fail_score"],
        "crash_rate": report["crash_rate"],
        "stress_advantage_drift": report["stress_advantage_drift"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.3 Stress Validation Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['stress_validation_report_id']}",
        f"- Version: {report['version']}",
        f"- Route policy: {report['route_policy']}",
        f"- Stress suite: {report['stress_suite']}",
        f"- Decision: {report['decision']}",
        f"- External routed advantage: {report['external_routed_advantage']}",
        f"- Stress routed advantage: {report['stress_routed_advantage']}",
        f"- Stress advantage drift: {report['stress_advantage_drift']}",
        f"- Safe-fail score: {report['safe_fail_score']}",
        f"- Crash rate: {report['crash_rate']}",
        f"- Stress failure count: {report['stress_failure_count']}",
        f"- Manual review required: {report['manual_review_required']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Stress Domain Families",
        "",
    ]

    for family in report.get("stress_domain_families", []):
        lines.append(f"- {family}")

    lines.extend([
        "",
        "## Stress Failure Surface",
        "",
    ])

    if report.get("stress_failure_surface"):
        for failure in report["stress_failure_surface"]:
            lines.append(f"- {failure.get('domain_id')}: {failure.get('failure_reason')}")
    else:
        lines.append("- No stress failures emitted under current proxy metrics.")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational stress/adversarial validation only. It is not medical guidance, clinical validation, biological-law proof, medical safety proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
