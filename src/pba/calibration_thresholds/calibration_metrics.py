from __future__ import annotations


def calibration_score(
    routed_advantage: float,
    preservation_score: float,
    safe_fail_score: float,
    failure_count: int,
    overfitting_penalty: float,
    crash_rate: float,
    manual_review_penalty: float = 0.0,
    weights: dict | None = None,
) -> float:
    weights = weights or {}
    w_a = float(weights.get("advantage", 1.0))
    w_p = float(weights.get("preservation", 1.0))
    w_s = float(weights.get("safe_fail", 1.5))
    w_f = float(weights.get("failure_penalty", 0.25))
    w_o = float(weights.get("overfitting_penalty", 0.5))
    w_r = float(weights.get("crash_penalty", 2.0))
    w_m = float(weights.get("manual_review_penalty", 0.05))

    score = (
        w_a * float(routed_advantage)
        + w_p * float(preservation_score)
        + w_s * float(safe_fail_score)
        - w_f * int(failure_count)
        - w_o * float(overfitting_penalty)
        - w_r * float(crash_rate)
        - w_m * float(manual_review_penalty)
    )
    return round(score, 6)


def admissible_candidate(
    safe_fail_score_preserved: bool,
    crash_rate_preserved: bool,
    overfitting_guard_passed: bool,
    failure_visibility_preserved: bool,
    automatic_kernel_replacement_allowed: bool = False,
    kernel_mutation_allowed: bool = False,
) -> bool:
    return (
        bool(safe_fail_score_preserved)
        and bool(crash_rate_preserved)
        and bool(overfitting_guard_passed)
        and bool(failure_visibility_preserved)
        and not bool(automatic_kernel_replacement_allowed)
        and not bool(kernel_mutation_allowed)
    )


def calibration_decision(best_admissible: bool, score: float, overfitting_guard_passed: bool) -> str:
    if best_admissible and score > 2.0 and overfitting_guard_passed:
        return "calibrate_thresholds"
    if best_admissible and score > 1.0:
        return "calibrate_with_caution"
    if best_admissible:
        return "preserve_thresholds_for_review"
    return "reject_calibration"
