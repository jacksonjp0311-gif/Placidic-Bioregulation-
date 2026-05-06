from __future__ import annotations

import json
from pathlib import Path


EVIDENCE_REPORTS = {
    "routed_suite": "reports/routing/latest_routed_suite_report.json",
    "routed_validation": "reports/validation/latest_routed_validation_report.json",
    "external_validation": "reports/external_validation/latest_external_validation_report.json",
    "stress_validation": "reports/stress_validation/latest_stress_validation_report.json",
    "calibration": "reports/calibration/latest_calibration_report.json",
    "evidence_package": "reports/evidence_packages/latest_evidence_package_report.json",
    "replay_audit": "reports/replay/latest_replay_audit_report.json",
}


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_evidence_index(root: str | Path) -> list[dict]:
    root = Path(root)
    rows = []

    for name, rel in EVIDENCE_REPORTS.items():
        path = root / rel
        if not path.exists():
            rows.append({
                "name": name,
                "path": rel,
                "exists": False,
                "version": None,
                "decision": None,
                "role": "missing_evidence",
            })
            continue

        report = _read_json(path)
        rows.append({
            "name": name,
            "path": rel,
            "exists": True,
            "version": report.get("version"),
            "decision": report.get("decision"),
            "role": "computational_evidence_report",
            "automatic_kernel_replacement_allowed": report.get("automatic_kernel_replacement_allowed", False),
            "kernel_mutation_allowed": report.get("kernel_mutation_allowed", False),
        })

    return rows


def evidence_index_valid(rows: list[dict]) -> bool:
    if not rows:
        return False
    for row in rows:
        if not row.get("exists"):
            return False
        if row.get("automatic_kernel_replacement_allowed") is not False:
            return False
        if row.get("kernel_mutation_allowed") is not False:
            return False
    return True
