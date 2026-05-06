from __future__ import annotations


def safe_fail_preserved(candidate_safe_fail: float, minimum_safe_fail: float) -> bool:
    return float(candidate_safe_fail) >= float(minimum_safe_fail)


def crash_rate_preserved(candidate_crash_rate: float, maximum_crash_rate: float = 0.0) -> bool:
    return float(candidate_crash_rate) <= float(maximum_crash_rate)


def failure_visibility_preserved(failure_surface_visible: bool, hidden_failure_count: int = 0) -> bool:
    return bool(failure_surface_visible) and int(hidden_failure_count) == 0


def preservation_status(
    safe_fail_score: float,
    minimum_safe_fail: float,
    crash_rate: float,
    maximum_crash_rate: float,
    failure_surface_visible: bool,
    hidden_failure_count: int = 0,
) -> dict:
    return {
        "safe_fail_score": float(safe_fail_score),
        "minimum_safe_fail": float(minimum_safe_fail),
        "safe_fail_score_preserved": safe_fail_preserved(safe_fail_score, minimum_safe_fail),
        "crash_rate": float(crash_rate),
        "maximum_crash_rate": float(maximum_crash_rate),
        "crash_rate_preserved": crash_rate_preserved(crash_rate, maximum_crash_rate),
        "failure_visibility_preserved": failure_visibility_preserved(failure_surface_visible, hidden_failure_count),
    }
