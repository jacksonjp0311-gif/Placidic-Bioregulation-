from __future__ import annotations

import json
from pathlib import Path


EVIDENCE_LAYERS = [
    ("PBSA v2.1", "routed_validation", "reports/validation/latest_routed_validation_report.json", "internal computational routed validation only"),
    ("PBSA v2.2", "external_validation", "reports/external_validation/latest_external_validation_report.json", "external toy-domain validation only"),
    ("PBSA v2.3", "stress_validation", "reports/stress_validation/latest_stress_validation_report.json", "stress/adversarial toy-domain safe-fail behavior only"),
    ("PBSA v2.4", "calibration", "reports/calibration/latest_calibration_report.json", "threshold recommendation only"),
    ("PBSA v2.5", "evidence_package", "reports/evidence_packages/latest_evidence_package_report.json", "audit traceability only"),
    ("PBSA v2.6", "replay_audit", "reports/replay/latest_replay_audit_report.json", "computational reproducibility only"),
    ("PBSA v2.7", "release_candidate", "reports/release/latest_release_candidate_report.json", "public audit readiness only"),
]


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_evidence_summary(root: str | Path) -> list[dict]:
    root = Path(root)
    rows = []

    for layer, name, rel, boundary in EVIDENCE_LAYERS:
        path = root / rel
        if path.exists():
            report = _read_json(path)
            rows.append({
                "layer": layer,
                "name": name,
                "artifact": rel,
                "exists": True,
                "version": report.get("version"),
                "decision": report.get("decision"),
                "claim_boundary": boundary,
                "automatic_kernel_replacement_allowed": report.get("automatic_kernel_replacement_allowed", False),
                "kernel_mutation_allowed": report.get("kernel_mutation_allowed", False),
            })
        else:
            rows.append({
                "layer": layer,
                "name": name,
                "artifact": rel,
                "exists": False,
                "version": None,
                "decision": None,
                "claim_boundary": boundary,
                "automatic_kernel_replacement_allowed": False,
                "kernel_mutation_allowed": False,
            })

    return rows


def evidence_summary_valid(rows: list[dict]) -> bool:
    if not rows:
        return False
    for row in rows:
        if not row.get("exists"):
            return False
        if row.get("automatic_kernel_replacement_allowed") is not False:
            return False
        if row.get("kernel_mutation_allowed") is not False:
            return False
        if not row.get("claim_boundary"):
            return False
    return True
