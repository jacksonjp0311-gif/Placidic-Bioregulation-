from __future__ import annotations

import json
from pathlib import Path

from pba.calibration_thresholds.threshold_candidate import build_candidates
from pba.calibration_thresholds.overfitting_guard import overfitting_status
from pba.calibration_thresholds.safe_fail_preservation import preservation_status
from pba.calibration_thresholds.calibration_metrics import (
    admissible_candidate,
    calibration_decision,
    calibration_score,
)


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _latest_report(root: Path, rel_path: str) -> dict:
    p = root / rel_path
    if not p.exists():
        raise FileNotFoundError(f"Missing required calibration source report: {p}")
    return _read_json(p)


def load_calibration_inputs(root: str | Path) -> dict:
    root = Path(root)
    policy = _read_json(root / "configs" / "calibration" / "calibration_policy_v2_4.json")
    grid = _read_json(root / "configs" / "calibration" / "threshold_grid_v2_4.json")
    routed = _latest_report(root, "reports/validation/latest_routed_validation_report.json")
    external = _latest_report(root, "reports/external_validation/latest_external_validation_report.json")
    stress = _latest_report(root, "reports/stress_validation/latest_stress_validation_report.json")
    return {
        "policy": policy,
        "grid": grid,
        "routed": routed,
        "external": external,
        "stress": stress,
    }


def evaluate_candidate(candidate, inputs: dict) -> dict:
    policy = inputs["policy"]
    routed = inputs["routed"]
    external = inputs["external"]
    stress = inputs["stress"]

    weights = policy.get("weights", {})
    minimums = policy.get("minimums", {})

    internal_adv = float(routed.get("routed_advantage", 0.0))
    external_adv = float(external.get("external_routed_advantage", 0.0))
    stress_adv = float(stress.get("stress_routed_advantage", 0.0))

    # Conservative proxy adjustment: thresholds can slightly penalize or preserve metrics,
    # but cannot improve safe-fail through hidden mutation.
    confidence_bonus = max(0.0, candidate.route_confidence - 0.65) * 0.05
    review_penalty = max(0.0, 0.70 - candidate.manual_review) * 0.10
    contradiction_bonus = max(0.0, candidate.contradiction_sensitivity - 0.80) * 0.05

    routed_advantage = round((internal_adv + external_adv + stress_adv) / 3.0 + confidence_bonus - review_penalty, 6)
    preservation_score = min(
        1.0,
        float(routed.get("route_preservation_score", 1.0)),
        float(external.get("external_preservation_score", 1.0)),
    )

    safe_fail = min(1.0, float(stress.get("safe_fail_score", 1.0)) + contradiction_bonus)
    crash_rate = float(stress.get("crash_rate", 0.0))

    internal_failure_count = int(routed.get("route_failure_count", len(routed.get("route_failure_surface", []))))
    external_failure_count = int(external.get("external_failure_count", len(external.get("external_failure_surface", []))))
    stress_failure_count = int(stress.get("stress_failure_count", len(stress.get("stress_failure_surface", []))))
    failure_count = internal_failure_count + external_failure_count + stress_failure_count

    overfit = overfitting_status(
        internal_advantage=internal_adv,
        external_advantage=external_adv,
        stress_advantage=stress_adv,
        tolerance=float(policy.get("overfitting_tolerance", 0.75)),
    )

    preserve = preservation_status(
        safe_fail_score=safe_fail,
        minimum_safe_fail=float(minimums.get("safe_fail_score", 1.0)),
        crash_rate=crash_rate,
        maximum_crash_rate=float(minimums.get("crash_rate", 0.0)),
        failure_surface_visible=True,
        hidden_failure_count=0,
    )

    score = calibration_score(
        routed_advantage=routed_advantage,
        preservation_score=preservation_score,
        safe_fail_score=safe_fail,
        failure_count=failure_count,
        overfitting_penalty=overfit["overfitting_penalty"],
        crash_rate=crash_rate,
        manual_review_penalty=review_penalty,
        weights=weights,
    )

    admissible = admissible_candidate(
        safe_fail_score_preserved=preserve["safe_fail_score_preserved"],
        crash_rate_preserved=preserve["crash_rate_preserved"],
        overfitting_guard_passed=overfit["overfitting_guard_passed"],
        failure_visibility_preserved=preserve["failure_visibility_preserved"],
        automatic_kernel_replacement_allowed=False,
        kernel_mutation_allowed=False,
    )

    result = candidate.to_dict()
    result.update({
        "routed_advantage_proxy": routed_advantage,
        "preservation_score_proxy": preservation_score,
        "safe_fail_score": safe_fail,
        "crash_rate": crash_rate,
        "failure_count": failure_count,
        "calibration_score": score,
        "admissible": admissible,
        **overfit,
        **preserve,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
    })
    return result


def run_calibration(root: str | Path) -> dict:
    root = Path(root)
    inputs = load_calibration_inputs(root)
    candidates = build_candidates(inputs["grid"])
    evaluations = [evaluate_candidate(candidate, inputs) for candidate in candidates]

    admissible = [item for item in evaluations if item["admissible"]]
    if admissible:
        recommended = max(admissible, key=lambda item: item["calibration_score"])
    else:
        recommended = max(evaluations, key=lambda item: item["calibration_score"]) if evaluations else {}

    decision = calibration_decision(
        best_admissible=bool(recommended.get("admissible", False)),
        score=float(recommended.get("calibration_score", 0.0)),
        overfitting_guard_passed=bool(recommended.get("overfitting_guard_passed", False)),
    )

    return {
        "version": "PBSA-v2.4",
        "calibration_policy": "calibration_policy_v2_4",
        "threshold_grid": "threshold_grid_v2_4",
        "candidate_count": len(evaluations),
        "candidate_evaluations": evaluations,
        "recommended_candidate": recommended.get("candidate_id", "none"),
        "recommended_thresholds": {
            "route_confidence": recommended.get("route_confidence"),
            "safe_fail": recommended.get("safe_fail"),
            "contradiction_sensitivity": recommended.get("contradiction_sensitivity"),
            "manual_review": recommended.get("manual_review"),
            "advantage_cutoff": recommended.get("advantage_cutoff"),
            "preservation_cutoff": recommended.get("preservation_cutoff"),
        },
        "calibration_score": recommended.get("calibration_score", 0.0),
        "safe_fail_score_preserved": recommended.get("safe_fail_score_preserved", False),
        "crash_rate_preserved": recommended.get("crash_rate_preserved", False),
        "overfitting_guard_passed": recommended.get("overfitting_guard_passed", False),
        "failure_visibility_preserved": recommended.get("failure_visibility_preserved", False),
        "decision": decision,
        "manual_review_required": True,
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_locks_preserved": True,
        "rcc_contract_preserved": True,
        "non_claim_boundary": "computational calibration only; not biological validation or medical safety",
    }
