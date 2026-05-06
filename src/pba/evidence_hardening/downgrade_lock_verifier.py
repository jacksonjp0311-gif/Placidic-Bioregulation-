from __future__ import annotations

import json
from pathlib import Path


REPORTS = [
    "reports/validation/latest_routed_validation_report.json",
    "reports/external_validation/latest_external_validation_report.json",
    "reports/stress_validation/latest_stress_validation_report.json",
    "reports/calibration/latest_calibration_report.json",
]


def verify_downgrade_locks(root: str | Path) -> dict:
    root = Path(root)
    violations = []

    for rel in REPORTS:
        path = root / rel
        if not path.exists():
            violations.append({"path": rel, "reason": "missing_report"})
            continue
        report = json.loads(path.read_text(encoding="utf-8"))
        if report.get("automatic_kernel_replacement_allowed") is not False:
            violations.append({"path": rel, "reason": "automatic_kernel_replacement_not_false"})
        if report.get("kernel_mutation_allowed", False) is not False:
            violations.append({"path": rel, "reason": "kernel_mutation_not_false"})
        if report.get("non_claim_locks_preserved", True) is not True:
            violations.append({"path": rel, "reason": "non_claim_locks_not_preserved"})

    return {
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": len(violations) == 0,
        "violations": violations,
        "downgrade_locks_valid": len(violations) == 0,
    }
