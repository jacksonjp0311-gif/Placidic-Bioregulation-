from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.external.external_validation_runner import run_external_validation


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_external_validation_report(root: str | Path) -> dict:
    root = Path(root)
    validation = run_external_validation(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-EXTERNAL-VALIDATION-" + now

    report = {
        "external_validation_report_id": report_id,
        "version": "PBSA-v2.2",
        "route_policy": validation["route_policy"],
        "external_suite": validation["external_suite"],
        "external_domain_families": validation["external_domain_families"],
        "source_internal_validation_report": validation["source_internal_validation_report"],
        "internal_routed_advantage": validation["internal_routed_advantage"],
        "external_routed_advantage": validation["external_routed_advantage"],
        "advantage_drift": validation["advantage_drift"],
        "internal_preservation_score": validation["internal_preservation_score"],
        "external_preservation_score": validation["external_preservation_score"],
        "preservation_drift": validation["preservation_drift"],
        "internal_failure_count": validation["internal_failure_count"],
        "external_failure_count": validation["external_failure_count"],
        "failure_surface_drift": validation["failure_surface_drift"],
        "route_frequency_drift": validation["route_frequency_drift"],
        "external_route_decisions": validation["external_route_decisions"],
        "external_control_suite_scores": validation["external_control_suite_scores"],
        "external_best_control_policy": validation["external_best_control_policy"],
        "external_failure_surface": validation["external_failure_surface"],
        "decision": validation["decision"],
        "manual_review_required": validation["manual_review_required"],
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "next_required_step": "PBSA v2.3 stress/adversarial validation",
        "non_claim_boundary": validation["non_claim_boundary"],
    }

    out_dir = root / "reports" / "external_validation" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "external_validation_report.json"
    md_path = out_dir / "external_validation_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "external_validation" / "latest_external_validation_report.json"
    latest_md = root / "reports" / "external_validation" / "latest_external_validation_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_2_external_validation_report_generated",
        "external_validation_report_id": report_id,
        "decision": report["decision"],
        "internal_routed_advantage": report["internal_routed_advantage"],
        "external_routed_advantage": report["external_routed_advantage"],
        "advantage_drift": report["advantage_drift"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "external_validation_report_json": str(json_path),
        "external_validation_report_md": str(md_path),
        "latest_external_validation_report_json": str(latest_json),
        "latest_external_validation_report_md": str(latest_md),
        "decision": report["decision"],
        "external_routed_advantage": report["external_routed_advantage"],
        "advantage_drift": report["advantage_drift"],
        "external_preservation_score": report["external_preservation_score"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.2 External Validation Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['external_validation_report_id']}",
        f"- Version: {report['version']}",
        f"- Route policy: {report['route_policy']}",
        f"- External suite: {report['external_suite']}",
        f"- Decision: {report['decision']}",
        f"- Internal routed advantage: {report['internal_routed_advantage']}",
        f"- External routed advantage: {report['external_routed_advantage']}",
        f"- Advantage drift: {report['advantage_drift']}",
        f"- Internal preservation score: {report['internal_preservation_score']}",
        f"- External preservation score: {report['external_preservation_score']}",
        f"- Preservation drift: {report['preservation_drift']}",
        f"- External failure count: {report['external_failure_count']}",
        f"- Manual review required: {report['manual_review_required']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## External Domain Families",
        "",
    ]

    for family in report.get("external_domain_families", []):
        lines.append(f"- {family}")

    lines.extend([
        "",
        "## Route Frequency Drift",
        "",
    ])

    for route, drift in report.get("route_frequency_drift", {}).items():
        lines.append(f"- {route}: {drift}")

    lines.extend([
        "",
        "## External Failure Surface",
        "",
    ])

    if report.get("external_failure_surface"):
        for failure in report["external_failure_surface"]:
            lines.append(f"- {failure.get('domain_id')}: {failure.get('failure_reason')}")
    else:
        lines.append("- No external routed validation failures emitted under current proxy metrics.")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational external-domain validation only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
