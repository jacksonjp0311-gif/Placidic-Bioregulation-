from __future__ import annotations


def replay_locks_reproduced(replayed_reports: dict) -> dict:
    violations = []

    for name, report in replayed_reports.items():
        if report.get("automatic_kernel_replacement_allowed") is not False:
            violations.append({"report": name, "reason": "automatic_kernel_replacement_not_false"})
        if report.get("kernel_mutation_allowed", False) is not False:
            violations.append({"report": name, "reason": "kernel_mutation_not_false"})
        if "non_claim_locks_preserved" in report and report.get("non_claim_locks_preserved") is not True:
            violations.append({"report": name, "reason": "non_claim_locks_not_preserved"})

    return {
        "downgrade_locks_replayed": len(violations) == 0,
        "violations": violations,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    }


def failure_surfaces_replayed(replayed_reports: dict) -> dict:
    required = {
        "routed_validation_report": "route_failure_surface",
        "external_validation_report": "external_failure_surface",
        "stress_validation_report": "stress_failure_surface",
        "calibration_report": "candidate_evaluations",
        "evidence_package_report": "failure_surface_status",
    }

    missing = []
    for report_name, field in required.items():
        report = replayed_reports.get(report_name, {})
        if field not in report:
            missing.append({"report": report_name, "missing_field": field})

    return {
        "failure_surfaces_replayed": len(missing) == 0,
        "missing": missing,
    }
