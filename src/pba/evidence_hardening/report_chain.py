from __future__ import annotations

import json
from pathlib import Path


REPORT_CHAIN = {
    "routed_suite": "reports/routing/latest_routed_suite_report.json",
    "routed_validation": "reports/validation/latest_routed_validation_report.json",
    "external_validation": "reports/external_validation/latest_external_validation_report.json",
    "stress_validation": "reports/stress_validation/latest_stress_validation_report.json",
    "calibration": "reports/calibration/latest_calibration_report.json",
}


def _read_json(root: Path, rel: str) -> dict:
    return json.loads((root / rel).read_text(encoding="utf-8"))


def verify_report_chain(root: str | Path) -> dict:
    root = Path(root)
    reports = {}
    missing = []

    for name, rel in REPORT_CHAIN.items():
        path = root / rel
        if not path.exists():
            missing.append(name)
            continue
        reports[name] = _read_json(root, rel)

    locks_ok = True
    for name, report in reports.items():
        if report.get("automatic_kernel_replacement_allowed") is not False:
            locks_ok = False
        if report.get("kernel_mutation_allowed", False) is not False:
            locks_ok = False

    expected_versions = {
        "routed_validation": "PBSA-v2.1",
        "external_validation": "PBSA-v2.2",
        "stress_validation": "PBSA-v2.3",
        "calibration": "PBSA-v2.4",
    }

    versions_ok = True
    for name, version in expected_versions.items():
        if name in reports and reports[name].get("version") != version:
            versions_ok = False

    return {
        "present": len(missing) == 0,
        "missing": missing,
        "locks_ok": locks_ok,
        "versions_ok": versions_ok,
        "report_chain_valid": len(missing) == 0 and locks_ok and versions_ok,
        "reports": {name: REPORT_CHAIN[name] for name in reports},
    }
