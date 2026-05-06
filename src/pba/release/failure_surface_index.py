from __future__ import annotations

import json
from pathlib import Path


FAILURE_SURFACE_FIELDS = {
    "routed_validation": ("reports/validation/latest_routed_validation_report.json", "route_failure_surface"),
    "external_validation": ("reports/external_validation/latest_external_validation_report.json", "external_failure_surface"),
    "stress_validation": ("reports/stress_validation/latest_stress_validation_report.json", "stress_failure_surface"),
    "calibration": ("reports/calibration/latest_calibration_report.json", "candidate_evaluations"),
    "evidence_package": ("reports/evidence_packages/latest_evidence_package_report.json", "failure_surface_status"),
    "replay_audit": ("reports/replay/latest_replay_audit_report.json", "semantic_drift"),
}


def build_failure_surface_index(root: str | Path) -> dict:
    root = Path(root)
    index = {}

    for name, (rel, field) in FAILURE_SURFACE_FIELDS.items():
        path = root / rel
        if not path.exists():
            index[name] = {"path": rel, "field": field, "status": "missing_report", "count": None}
            continue

        report = json.loads(path.read_text(encoding="utf-8"))
        if field not in report:
            index[name] = {"path": rel, "field": field, "status": "missing_field", "count": None}
            continue

        value = report.get(field)
        if isinstance(value, list):
            count = len(value)
        elif isinstance(value, dict):
            count = len(value)
        else:
            count = 1 if value else 0

        index[name] = {"path": rel, "field": field, "status": "present", "count": count}

    return index


def failure_surface_index_valid(index: dict) -> bool:
    return bool(index) and all(item.get("status") == "present" for item in index.values())
