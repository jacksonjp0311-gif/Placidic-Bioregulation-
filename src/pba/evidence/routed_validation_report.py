from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.validation.routed_validation_runner import run_routed_validation


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_routed_validation_report(root: str | Path) -> dict:
    root = Path(root)
    validation = run_routed_validation(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-ROUTED-VALIDATION-" + now

    report = {
        "routed_validation_report_id": report_id,
        "version": "PBSA-v2.1",
        "route_policy": validation["route_policy"],
        "control_policies": validation["control_policies"],
        "suite_scope": validation["suite_scope"],
        "source_routed_suite_report": validation["source_routed_suite_report"],
        "routed_suite_score": validation["routed_suite_score"],
        "control_suite_scores": validation["control_suite_scores"],
        "best_control_policy": validation["best_control_policy"],
        "best_control_score": validation["best_control_score"],
        "routed_advantage": validation["routed_advantage"],
        "route_preservation_score": validation["route_preservation_score"],
        "route_failure_surface": validation["route_failure_surface"],
        "route_failure_count": validation["route_failure_count"],
        "decision": validation["decision"],
        "manual_review_required": validation["manual_review_required"],
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "next_required_step": "PBSA v2.2 external-domain validation",
        "non_claim_boundary": validation["non_claim_boundary"],
    }

    out_dir = root / "reports" / "validation" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "routed_validation_report.json"
    md_path = out_dir / "routed_validation_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "validation" / "latest_routed_validation_report.json"
    latest_md = root / "reports" / "validation" / "latest_routed_validation_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_1_routed_validation_report_generated",
        "routed_validation_report_id": report_id,
        "decision": report["decision"],
        "routed_advantage": report["routed_advantage"],
        "route_preservation_score": report["route_preservation_score"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "routed_validation_report_json": str(json_path),
        "routed_validation_report_md": str(md_path),
        "latest_routed_validation_report_json": str(latest_json),
        "latest_routed_validation_report_md": str(latest_md),
        "decision": report["decision"],
        "routed_advantage": report["routed_advantage"],
        "route_preservation_score": report["route_preservation_score"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.1 Routed Validation Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['routed_validation_report_id']}",
        f"- Version: {report['version']}",
        f"- Route policy: {report['route_policy']}",
        f"- Decision: {report['decision']}",
        f"- Routed advantage: {report['routed_advantage']}",
        f"- Route preservation score: {report['route_preservation_score']}",
        f"- Best control policy: {report['best_control_policy']}",
        f"- Route failure count: {report['route_failure_count']}",
        f"- Manual review required: {report['manual_review_required']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Control Suite Scores",
        "",
    ]

    for policy, score in report.get("control_suite_scores", {}).items():
        lines.append(f"- {policy}: {score}")

    lines.extend([
        "",
        "## Failure Surface",
        "",
    ])

    if report.get("route_failure_surface"):
        for failure in report["route_failure_surface"]:
            lines.append(f"- {failure.get('domain_id')}: {failure.get('failure_reason')}")
    else:
        lines.append("- No routed validation failures emitted under current proxy metrics.")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational routed-suite validation only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
