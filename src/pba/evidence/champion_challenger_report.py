from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from pba.evolution.champion_challenger_runner import build_champion_challenger_packet
from pba.evolution.promotion_governance import decide_promotion
from pba.evidence.runtime_ledger import append_ledger


def _write_json(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def build_champion_challenger_report(root: str | Path) -> dict:
    root = Path(root)
    packet = build_champion_challenger_packet(root)

    shell = {
        "original_suite_result": {
            "champion_classification": packet["original_suite_result"]["champion_classification"],
            "best_challenger_classification": packet["original_suite_result"]["best_challenger_classification"],
        },
        "holdout_suite_result": {
            "champion_classification": packet["holdout_suite_result"]["champion_classification"],
            "best_challenger_classification": packet["holdout_suite_result"]["best_challenger_classification"],
        },
        "baseline_visibility_preserved": packet["baseline_visibility_preserved"],
        "non_claim_locks_preserved": packet["non_claim_locks_preserved"],
        "rcc_contract_preserved": packet["rcc_contract_preserved"],
    }

    decision = decide_promotion(shell)
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    report_id = "PBSA-CC-" + now

    report = {
        "champion_challenger_report_id": report_id,
        "version": "PBSA-v1.4",
        "champion": "current_pba_kernel",
        "candidate_execution_allowed": True,
        "candidate_execution_scope": "comparison_harness_only",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "original_suite_result": shell["original_suite_result"],
        "holdout_suite_result": shell["holdout_suite_result"],
        "baseline_visibility_preserved": True,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "comparison_packet": packet,
        "decision": decision["decision"],
        "decision_reason": decision["decision_reason"],
        "promotion_status": decision["promotion_status"],
        "next_required_step": "PBSA v2.0 regime-routed PBSA or manual review",
        "non_claim_boundary": "computational champion/challenger comparison only; not biological validation",
    }

    out_dir = root / "reports" / "champion_challenger" / report_id
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "champion_challenger_report.json"
    md_path = out_dir / "champion_challenger_report.md"

    _write_json(json_path, report)
    md_path.write_text(render_markdown(report), encoding="utf-8")

    latest_json = root / "reports" / "champion_challenger" / "latest_champion_challenger_report.json"
    latest_md = root / "reports" / "champion_challenger" / "latest_champion_challenger_report.md"
    _write_json(latest_json, report)
    latest_md.write_text(render_markdown(report), encoding="utf-8")

    append_ledger(root / "ledgers" / "pba_decision_ledger.jsonl", {
        "event": "pbsa_v1_4_champion_challenger_report_generated",
        "champion_challenger_report_id": report_id,
        "decision": report["decision"],
        "automatic_kernel_replacement_allowed": False,
    })

    return {
        "status": "complete",
        "champion_challenger_report_json": str(json_path),
        "champion_challenger_report_md": str(md_path),
        "latest_champion_challenger_report_json": str(latest_json),
        "latest_champion_challenger_report_md": str(latest_md),
        "decision": report["decision"],
        "promotion_status": report["promotion_status"],
        "automatic_kernel_replacement_allowed": False,
    }


def render_markdown(report: dict) -> str:
    return f"""# PBSA v1.4 Champion/Challenger Report

## Status

- Report ID: {report["champion_challenger_report_id"]}
- Version: {report["version"]}
- Champion: {report["champion"]}
- Candidate execution allowed: {report["candidate_execution_allowed"]}
- Candidate execution scope: {report["candidate_execution_scope"]}
- Automatic kernel replacement allowed: {report["automatic_kernel_replacement_allowed"]}
- Kernel mutation allowed: {report["kernel_mutation_allowed"]}
- Decision: {report["decision"]}
- Decision reason: {report["decision_reason"]}
- Promotion status: {report["promotion_status"]}

## Original Suite

- Champion classification: {report["original_suite_result"]["champion_classification"]}
- Best challenger classification: {report["original_suite_result"]["best_challenger_classification"]}

## Holdout Suite

- Champion classification: {report["holdout_suite_result"]["champion_classification"]}
- Best challenger classification: {report["holdout_suite_result"]["best_challenger_classification"]}

## Governance

- Baseline visibility preserved: {report["baseline_visibility_preserved"]}
- Non-claim locks preserved: {report["non_claim_locks_preserved"]}
- RCC contract preserved: {report["rcc_contract_preserved"]}
- Next required step: {report["next_required_step"]}

## Non-Claim Boundary

This is computational champion/challenger comparison only. It is not medical guidance, clinical validation, biological-law proof, or mechanism proof.
"""
