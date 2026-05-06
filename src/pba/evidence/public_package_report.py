from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.public_package.public_package_bundle import build_public_package_bundle


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_public_package_report(root: str | Path) -> dict:
    root = Path(root)
    bundle = build_public_package_bundle(root)
    readiness = bundle["public_package_readiness"]

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-PUBLIC-PACKAGE-" + now

    report = {
        "public_package_report_id": report_id,
        "version": "PBSA-v3.0",
        "package_version": "3.0.0",
        "public_package_policy": bundle["public_package_policy"],
        "source_release_candidate_report": bundle["source_release_candidate_report"],
        "public_package_readiness": readiness["public_package_readiness"],
        "publication_abstract": bundle["publication_abstract"],
        "evidence_summary": bundle["evidence_summary"],
        "public_claim_boundary_table": bundle["public_claim_boundary_table"],
        "public_limitations": bundle["public_limitations"],
        "public_command_surface": bundle["public_command_surface"],
        "release_checklist": bundle["release_checklist"],
        "release_tag": bundle["release_tag"],
        "release_candidate_status": readiness["release_candidate_status"],
        "release_readiness": readiness["release_readiness"],
        "semantic_drift_count": readiness["semantic_drift_count"],
        "expected_timestamp_drift_count": readiness["expected_timestamp_drift_count"],
        "public_checks": readiness["checks"],
        "downgrade_locks": readiness["downgrade_locks"],
        "decision": readiness["decision"],
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": readiness["downgrade_locks"]["non_claim_locks_preserved"],
        "rcc_contract_preserved": readiness["checks"].get("rcc_public_anchors_valid", False),
        "next_required_step": "archive release tag and publish README",
        "non_claim_boundary": bundle["non_claim_boundary"],
    }

    out_dir = root / "reports" / "public_package" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "public_package_report.json"
    md_path = out_dir / "public_package_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "public_package" / "latest_public_package_report.json"
    latest_md = root / "reports" / "public_package" / "latest_public_package_report.md"
    latest_abstract = root / "reports" / "public_package" / "latest_publication_abstract.md"
    latest_evidence_summary = root / "reports" / "public_package" / "latest_public_evidence_summary.json"
    latest_limitations = root / "reports" / "public_package" / "latest_public_limitations.json"
    latest_claim_table = root / "reports" / "public_package" / "latest_public_claim_boundary_table.json"
    latest_command_surface = root / "reports" / "public_package" / "latest_public_command_surface.json"
    latest_release_checklist = root / "reports" / "public_package" / "latest_release_checklist.json"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")
    latest_abstract.write_text(report["publication_abstract"] + "\n", encoding="utf-8")
    _write_json(latest_evidence_summary, {"evidence_summary": report["evidence_summary"]})
    _write_json(latest_limitations, {"public_limitations": report["public_limitations"]})
    _write_json(latest_claim_table, report["public_claim_boundary_table"])
    _write_json(latest_command_surface, report["public_command_surface"])
    _write_json(latest_release_checklist, report["release_checklist"])

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v3_0_public_package_report_generated",
        "public_package_report_id": report_id,
        "decision": report["decision"],
        "public_package_readiness": report["public_package_readiness"],
        "release_tag": report["release_tag"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "public_package_report_json": str(json_path),
        "public_package_report_md": str(md_path),
        "latest_public_package_report_json": str(latest_json),
        "latest_public_package_report_md": str(latest_md),
        "latest_publication_abstract_md": str(latest_abstract),
        "decision": report["decision"],
        "public_package_readiness": report["public_package_readiness"],
        "release_tag": report["release_tag"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v3.0 Public Research Package Report",
        "",
        "## Status",
        "",
        f"- Public package report ID: {report['public_package_report_id']}",
        f"- Version: {report['version']}",
        f"- Package version: {report['package_version']}",
        f"- Decision: {report['decision']}",
        f"- Public package readiness: {report['public_package_readiness']}",
        f"- Release tag: {report['release_tag']}",
        f"- Release candidate status: {report['release_candidate_status']}",
        f"- Semantic drift count: {report['semantic_drift_count']}",
        f"- Expected timestamp drift count: {report['expected_timestamp_drift_count']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Publication Abstract",
        "",
        report["publication_abstract"],
        "",
        "## Public Commands",
        "",
    ]

    for command in report.get("public_command_surface", {}).get("commands", []):
        lines.append(f"- `{command}`")

    lines.extend([
        "",
        "## Public Limitations",
        "",
    ])

    for limitation in report.get("public_limitations", []):
        lines.append(f"- {limitation}")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "Public research package readiness is public computational audit readiness only. It is not biological validation, medical validation, medical safety, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
