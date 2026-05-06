from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evidence.runtime_ledger import append_ledger
from pba.evidence_hardening.evidence_package import compile_evidence_package


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_evidence_package_report(root: str | Path) -> dict:
    root = Path(root)
    compiled = compile_evidence_package(root)

    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    package_id = "PBSA-EVIDENCE-PACKAGE-" + now

    report = {
        "evidence_package_id": package_id,
        "version": "PBSA-v2.5",
        "package_version": "1.5.0",
        "artifact_manifest": compiled["artifact_manifest"],
        "hash_manifest": compiled["hash_manifest"],
        "traceability_matrix": compiled["traceability_matrix"],
        "report_chain": compiled["report_chain"],
        "ledger_continuity": compiled["ledger_continuity"],
        "rcc_anchor_verification": compiled["rcc_anchor_verification"],
        "downgrade_locks": compiled["downgrade_locks"],
        "failure_surface_status": compiled["failure_surface_status"],
        "failure_surface_preservation_valid": compiled["failure_surface_preservation_valid"],
        "decision": compiled["decision"],
        "warnings": compiled["warnings"],
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": compiled["non_claim_locks_preserved"],
        "rcc_contract_preserved": compiled["rcc_contract_preserved"],
        "next_required_step": "PBSA v2.6 reproducibility replay",
        "non_claim_boundary": compiled["non_claim_boundary"],
    }

    out_dir = root / "reports" / "evidence_packages" / package_id
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "evidence_package_report.json"
    md_path = out_dir / "evidence_package_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "evidence_packages" / "latest_evidence_package_report.json"
    latest_md = root / "reports" / "evidence_packages" / "latest_evidence_package_report.md"

    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v2_5_evidence_package_report_generated",
        "evidence_package_id": package_id,
        "decision": report["decision"],
        "artifact_count": len(report["hash_manifest"]),
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "evidence_package_report_json": str(json_path),
        "evidence_package_report_md": str(md_path),
        "latest_evidence_package_report_json": str(latest_json),
        "latest_evidence_package_report_md": str(latest_md),
        "decision": report["decision"],
        "artifact_count": len(report["hash_manifest"]),
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# PBSA v2.5 Evidence Package Report",
        "",
        "## Status",
        "",
        f"- Evidence package ID: {report['evidence_package_id']}",
        f"- Version: {report['version']}",
        f"- Package version: {report['package_version']}",
        f"- Decision: {report['decision']}",
        f"- Artifact count: {len(report['hash_manifest'])}",
        f"- Manual review required: {report['manual_review_required']}",
        f"- Automatic kernel replacement allowed: {report['automatic_kernel_replacement_allowed']}",
        f"- Kernel mutation allowed: {report['kernel_mutation_allowed']}",
        f"- Non-claim locks preserved: {report['non_claim_locks_preserved']}",
        f"- RCC contract preserved: {report['rcc_contract_preserved']}",
        "",
        "## Failure Surface Status",
        "",
    ]

    for key, value in report.get("failure_surface_status", {}).items():
        lines.append(f"- {key}: {value}")

    lines.extend([
        "",
        "## Traceability Matrix",
        "",
    ])

    for row in report.get("traceability_matrix", []):
        lines.append(f"- {row.get('claim')}: {row.get('config')} -> {row.get('report')} -> {row.get('ledger')}")

    lines.extend([
        "",
        "## Non-Claim Boundary",
        "",
        "This is computational evidence packaging only. It is not medical guidance, clinical validation, biological-law proof, medical safety proof, or mechanism proof.",
    ])

    return "\n".join(lines) + "\n"
