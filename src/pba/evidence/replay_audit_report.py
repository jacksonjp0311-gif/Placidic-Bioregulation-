from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.replay.replay_runner import run_replay


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_replay_audit_report(root: str | Path) -> dict:
    root = Path(root)
    replay = run_replay(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-REPLAY-AUDIT-" + now

    report = {
        "replay_audit_report_id": report_id,
        "version": "PBSA-v2.6",
        "package_version": "1.6.0",
        "source_evidence_package": replay["source_evidence_package"],
        "replay_policy": replay["replay_policy"],
        "replayed_reports": replay["replayed_reports"],
        "decision_replay": replay["decision_replay"],
        "decision_replay_detail": replay["decision_replay_detail"],
        "hash_drift": replay["hash_drift"],
        "semantic_drift": replay["semantic_drift"],
        "expected_timestamp_drift": replay["expected_timestamp_drift"],
        "ledger_replay_valid": replay["ledger_replay_valid"],
        "rcc_replay_valid": replay["rcc_replay_valid"],
        "downgrade_locks_replayed": replay["downgrade_locks_replayed"],
        "failure_surfaces_replayed": replay["failure_surfaces_replayed"],
        "lock_replay_detail": replay["lock_replay_detail"],
        "failure_surface_replay_detail": replay["failure_surface_replay_detail"],
        "decision": replay["decision"],
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": replay["non_claim_locks_preserved"],
        "rcc_contract_preserved": replay["rcc_contract_preserved"],
        "next_required_step": "PBSA v2.7 release candidate audit bundle",
        "non_claim_boundary": replay["non_claim_boundary"],
    }

    out_dir = root / "reports" / "replay" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "replay_audit_report.json"
    md_path = out_dir / "replay_audit_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "replay" / "latest_replay_audit_report.json"
    latest_md = root / "reports" / "replay" / "latest_replay_audit_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_6_replay_audit_report_generated",
        "replay_audit_report_id": report_id,
        "decision": report["decision"],
        "semantic_drift_count": len(report["semantic_drift"]),
        "expected_timestamp_drift_count": len(report["expected_timestamp_drift"]),
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "replay_audit_report_json": str(json_path),
        "replay_audit_report_md": str(md_path),
        "latest_replay_audit_report_json": str(latest_json),
        "latest_replay_audit_report_md": str(latest_md),
        "decision": report["decision"],
        "semantic_drift_count": len(report["semantic_drift"]),
        "expected_timestamp_drift_count": len(report["expected_timestamp_drift"]),
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.6 Replay Audit Report",
        "",
        "## Status",
        "",
        f"- Replay audit report ID: {report['replay_audit_report_id']}",
        f"- Version: {report['version']}",
        f"- Package version: {report['package_version']}",
        f"- Decision: {report['decision']}",
        f"- Semantic drift count: {len(report['semantic_drift'])}",
        f"- Expected timestamp drift count: {len(report['expected_timestamp_drift'])}",
        f"- Ledger replay valid: {report['ledger_replay_valid']}",
        f"- RCC replay valid: {report['rcc_replay_valid']}",
        f"- Downgrade locks replayed: {report['downgrade_locks_replayed']}",
        f"- Failure surfaces replayed: {report['failure_surfaces_replayed']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        "",
        "## Decision Replay",
        "",
    ]

    for key, value in report.get("decision_replay", {}).items():
        lines.append(f"- {key}: {value}")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational reproducibility replay only. It is not medical guidance, clinical validation, biological-law proof, medical safety proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
