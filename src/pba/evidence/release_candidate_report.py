from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.release.release_bundle import build_release_bundle


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_release_candidate_report(root: str | Path) -> dict:
    root = Path(root)
    bundle = build_release_bundle(root)
    readiness = bundle["release_readiness"]

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-RC-AUDIT-" + now

    report = {
        "release_candidate_report_id": report_id,
        "version": "PBSA-v2.7",
        "package_version": "1.7.0",
        "release_policy": bundle["release_policy"],
        "source_replay_report": bundle["source_replay_report"],
        "source_evidence_package": bundle["source_evidence_package"],
        "release_readiness": readiness["release_readiness"],
        "test_status": readiness["test_status"],
        "rcc_status": readiness["rcc_status"],
        "evidence_package_status": readiness["evidence_package_status"],
        "replay_status": readiness["replay_status"],
        "semantic_drift_count": readiness["semantic_drift_count"],
        "expected_timestamp_drift_count": readiness["expected_timestamp_drift_count"],
        "claim_boundary_table": bundle["claim_boundary_table"],
        "evidence_index": bundle["evidence_index"],
        "failure_surface_index": bundle["failure_surface_index"],
        "command_surface": bundle["command_surface"],
        "release_checks": readiness["checks"],
        "downgrade_locks": readiness["downgrade_locks"],
        "decision": readiness["decision"],
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": readiness["downgrade_locks"]["non_claim_locks_preserved"],
        "rcc_contract_preserved": readiness["rcc_status"] == "pass",
        "next_required_step": "PBSA v3.0 public research package",
        "non_claim_boundary": bundle["non_claim_boundary"],
    }

    out_dir = root / "reports" / "release" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "release_candidate_report.json"
    md_path = out_dir / "release_candidate_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "release" / "latest_release_candidate_report.json"
    latest_md = root / "reports" / "release" / "latest_release_candidate_report.md"
    latest_public_index = root / "reports" / "release" / "latest_public_audit_index.md"
    latest_evidence_index = root / "reports" / "release" / "latest_evidence_index.json"
    latest_claim_table = root / "reports" / "release" / "latest_claim_boundary_table.json"
    latest_failure_index = root / "reports" / "release" / "latest_failure_surface_index.json"
    latest_command_surface = root / "reports" / "release" / "latest_command_surface.json"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")
    latest_public_index.write_text(render_public_audit_index(report), encoding="utf-8")
    _write_json(latest_evidence_index, {"evidence_index": report["evidence_index"]})
    _write_json(latest_claim_table, report["claim_boundary_table"])
    _write_json(latest_failure_index, report["failure_surface_index"])
    _write_json(latest_command_surface, report["command_surface"])

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_7_release_candidate_report_generated",
        "release_candidate_report_id": report_id,
        "decision": report["decision"],
        "release_readiness": report["release_readiness"],
        "semantic_drift_count": report["semantic_drift_count"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "release_candidate_report_json": str(json_path),
        "release_candidate_report_md": str(md_path),
        "latest_release_candidate_report_json": str(latest_json),
        "latest_release_candidate_report_md": str(latest_md),
        "latest_public_audit_index_md": str(latest_public_index),
        "decision": report["decision"],
        "release_readiness": report["release_readiness"],
        "semantic_drift_count": report["semantic_drift_count"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.7 Release Candidate Audit Report",
        "",
        "## Status",
        "",
        f"- Release candidate report ID: {report['release_candidate_report_id']}",
        f"- Version: {report['version']}",
        f"- Package version: {report['package_version']}",
        f"- Decision: {report['decision']}",
        f"- Release readiness: {report['release_readiness']}",
        f"- Test status: {report['test_status']}",
        f"- RCC status: {report['rcc_status']}",
        f"- Evidence package status: {report['evidence_package_status']}",
        f"- Replay status: {report['replay_status']}",
        f"- Semantic drift count: {report['semantic_drift_count']}",
        f"- Expected timestamp drift count: {report['expected_timestamp_drift_count']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Command Surface",
        "",
    ]

    for command in report.get("command_surface", {}).get("commands", []):
        lines.append(f"- `{command}`")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "Release-candidate readiness is public audit readiness only. It is not biological validation, medical validation, medical safety, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"


def render_public_audit_index(report: dict) -> str:
    lines = [
        "# PBSA Public Audit Index",
        "",
        "## What this release candidate is",
        "",
        "A computational regime-routing and validation framework with internal, external, stress, calibration, evidence-package, and replay audit surfaces.",
        "",
        "## What this release candidate is not",
        "",
        "- Not biological validation",
        "- Not medical guidance",
        "- Not clinical safety evidence",
        "- Not physiological mechanism proof",
        "- Not automatic kernel replacement",
        "",
        "## Core commands",
        "",
    ]

    for command in report.get("command_surface", {}).get("commands", []):
        lines.append(f"- `{command}`")

    lines.extend([
        "",
        "## Evidence reports",
        "",
    ])

    for item in report.get("evidence_index", []):
        lines.append(f"- {item.get('name')}: {item.get('path')} | decision={item.get('decision')}")

    return "\n".join(lines) + "\n"
