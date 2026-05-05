from __future__ import annotations

import json
from pathlib import Path


def compile_evidence_package(run_dir: str | Path) -> dict:
    run = Path(run_dir)
    files = {
        "domain_config": "domain_config.json",
        "parameter_manifest": "parameter_manifest.json",
        "baseline_params": "baseline_params.json",
        "metric_manifest": "metric_manifest.json",
        "state_log": "state_log.jsonl",
        "baseline_state_log": "baseline_state_log.jsonl",
        "pba_metrics": "pba_metrics.json",
        "baseline_metrics": "baseline_metrics.json",
        "calibration_record": "calibration_record.json",
        "identifiability_report": "identifiability_report.json",
        "classification": "classification.json",
        "result_ledger": "result_ledger.jsonl"
    }

    package = {
        "evidence_package_id": f"PBSA-EVIDENCE-{run.name}",
        "version": "PBSA-v1.0",
        "pba_version": "PBA-v1.3",
        "run_dir": str(run),
        "files": {k: str(run / v) for k, v in files.items()},
        "file_exists": {k: (run / v).exists() for k, v in files.items()},
        "claim_boundary": {
            "supports": "local implementation and toy benchmark evidence only",
            "does_not_support": [
                "medical guidance",
                "biological law",
                "mechanism proof",
                "clinical validation",
                "universal biological theory"
            ]
        }
    }

    (run / "evidence_package.json").write_text(json.dumps(package, indent=2), encoding="utf-8")
    return package