from __future__ import annotations

import json
from pathlib import Path


FAILURE_SURFACE_REPORTS = {
    "routed": ("reports/validation/latest_routed_validation_report.json", "route_failure_surface"),
    "external": ("reports/external_validation/latest_external_validation_report.json", "external_failure_surface"),
    "stress": ("reports/stress_validation/latest_stress_validation_report.json", "stress_failure_surface"),
    "calibration": ("reports/calibration/latest_calibration_report.json", "candidate_evaluations"),
}


def verify_failure_surfaces(root: str | Path) -> dict:
    root = Path(root)
    statuses = {}

    for name, (rel, field) in FAILURE_SURFACE_REPORTS.items():
        path = root / rel
        if not path.exists():
            statuses[name] = "missing"
            continue
        report = json.loads(path.read_text(encoding="utf-8"))
        if field not in report:
            statuses[name] = "missing"
        elif isinstance(report.get(field), list):
            statuses[name] = "present"
        else:
            statuses[name] = "present"

    valid = all(status == "present" for status in statuses.values())

    return {
        "failure_surface_status": statuses,
        "failure_surface_preservation_valid": valid,
    }
