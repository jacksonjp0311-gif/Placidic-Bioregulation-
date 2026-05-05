from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.routing.routed_runner import run_routed_suite


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_routed_suite_report(root: str | Path) -> dict:
    root = Path(root)
    routed = run_routed_suite(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-ROUTED-SUITE-" + now

    report = {
        "routed_suite_report_id": report_id,
        "version": "PBSA-v2.0",
        "route_policy": routed["route_policy"],
        "routes": {d["domain_id"]: d["selected_route"] for d in routed["route_decisions"]},
        "route_counts": routed["route_counts"],
        "route_decisions": routed["route_decisions"],
        "route_evidence_count": len(routed["route_evidence"]),
        "source_reports": {
            "original_suite": routed["original_suite_source"],
            "holdout_summary": routed["holdout_summary_source"],
            "champion_challenger_report": routed["champion_challenger_report_source"],
        },
        "champion_challenger_decision": routed["champion_challenger_decision"],
        "decision": "route_by_regime",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "manual_review_required": routed["manual_review_required"],
        "next_required_step": "PBSA v2.1 routed-suite validation",
        "non_claim_boundary": routed["non_claim_boundary"],
    }

    out_dir = root / "reports" / "routing" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "routed_suite_report.json"
    md_path = out_dir / "routed_suite_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "routing" / "latest_routed_suite_report.json"
    latest_md = root / "reports" / "routing" / "latest_routed_suite_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_0_routed_suite_report_generated",
        "routed_suite_report_id": report_id,
        "decision": "route_by_regime",
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "routed_suite_report_json": str(json_path),
        "routed_suite_report_md": str(md_path),
        "latest_routed_suite_report_json": str(latest_json),
        "latest_routed_suite_report_md": str(latest_md),
        "decision": "route_by_regime",
        "manual_review_required": report["manual_review_required"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.0 Routed Suite Report",
        "",
        "## Status",
        "",
        f"- Report ID: {report['routed_suite_report_id']}",
        f"- Version: {report['version']}",
        f"- Route policy: {report['route_policy']}",
        f"- Decision: {report['decision']}",
        f"- Manual review required: {report['manual_review_required']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        f"- Route evidence count: {report['route_evidence_count']}",
        "",
        "## Routes",
        "",
    ]

    for domain, route in report.get("routes", {}).items():
        lines.append(f"- {domain}: {route}")

    lines.extend([
        "",
        "## Route Counts",
        "",
    ])

    for route, count in report.get("route_counts", {}).items():
        lines.append(f"- {route}: {count}")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational route selection only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
