from __future__ import annotations

from typing import Any


DIRECT = "direct_recovery"
PULSE = "pulse_recovery"
OSCILLATORY = "oscillatory"
NOISY = "noisy"
CUSP = "cusp_risk"
UNKNOWN = "unknown"


def _float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def detect_regime(
    domain_id: str,
    metrics: dict | None = None,
    comparison: dict | None = None,
    records: list[dict] | None = None,
) -> dict:
    """Detect a computational disturbance regime.

    This is a diagnostic heuristic, not a biological diagnosis.
    It intentionally preserves downgrade-friendly uncertainty.
    """
    metrics = metrics or {}
    comparison = comparison or {}
    records = records or []

    domain_key = (domain_id or "").lower()
    baseline_result = comparison.get("baseline_result", "")
    best_baseline = comparison.get("best_baseline", "")

    oscillation_amplitude = _float(metrics.get("oscillation_amplitude"))
    cusp_warnings = _float(metrics.get("cusp_warnings"))
    recovery_time = metrics.get("recovery_time")
    cumulative_deviation = _float(metrics.get("cumulative_deviation"))
    max_deviation = _float(metrics.get("max_deviation"))

    sign_changes = 0
    previous_sign = None
    xs = []
    for record in records:
        x = _float(record.get("x_t"))
        target = _float(record.get("target"))
        xs.append(x)
        diff = x - target
        sign = 1 if diff > 0 else -1 if diff < 0 else 0
        if previous_sign is not None and sign != 0 and previous_sign != 0 and sign != previous_sign:
            sign_changes += 1
        if sign != 0:
            previous_sign = sign

    recovery_slope = 0.0
    if len(xs) >= 2:
        recovery_slope = xs[-1] - xs[0]

    regime = UNKNOWN
    confidence = "low"
    interpretation = "insufficient evidence for confident regime detection"
    recommendation = "preserve downgrade and collect more evidence"

    if cusp_warnings >= 3 or max_deviation >= 1.0:
        regime = CUSP
        confidence = "medium"
        interpretation = "cusp-risk behavior detected from warnings or high deviation"
        recommendation = "prioritize bounded audit behavior and do not promote kernel changes"
    elif "osc" in domain_key or sign_changes >= 4 or oscillation_amplitude >= 0.75:
        regime = OSCILLATORY
        confidence = "high" if "osc" in domain_key else "medium"
        interpretation = "oscillatory or sign-changing disturbance pattern"
        recommendation = "preserve PBA behavior if PBA advantage is present; use anticipation cautiously"
    elif "pulse" in domain_key:
        regime = PULSE
        confidence = "high"
        interpretation = "pulse recovery domain"
        recommendation = "preserve baseline win and test direct correction candidates later"
    elif "temp" in domain_key or "direct" in domain_key:
        regime = DIRECT
        confidence = "high" if baseline_result == "baseline_advantage" else "medium"
        interpretation = "direct recovery domain where simple feedback may be sufficient"
        recommendation = "preserve baseline win and consider proportional-like route later"
    elif baseline_result == "baseline_advantage" and best_baseline == "proportional_feedback":
        regime = DIRECT
        confidence = "medium"
        interpretation = "baseline advantage suggests direct correction regime"
        recommendation = "preserve baseline win and diagnose whether PBA is over-smoothing"
    elif recovery_time is None and cumulative_deviation > 0:
        regime = NOISY
        confidence = "low"
        interpretation = "unrecovered or noisy response pattern"
        recommendation = "do not promote candidate without holdout evidence"

    return {
        "domain_id": domain_id,
        "detected_regime": regime,
        "confidence": confidence,
        "features": {
            "oscillation_amplitude": oscillation_amplitude,
            "recovery_time": recovery_time,
            "recovery_slope": recovery_slope,
            "sign_changes": sign_changes,
            "cusp_warnings": cusp_warnings,
            "cumulative_deviation": cumulative_deviation,
            "max_deviation": max_deviation,
            "baseline_result": baseline_result,
            "best_baseline": best_baseline,
        },
        "interpretation": interpretation,
        "recommendation": recommendation,
        "non_claim_boundary": "computational diagnosis only",
    }


def detect_regimes_from_runs(runs: list[dict]) -> dict:
    return {
        str(run.get("domain_id", "unknown")): detect_regime(
            str(run.get("domain_id", "unknown")),
            metrics=run.get("pba_metrics", run.get("metrics", {})),
            comparison=run,
        )
        for run in runs
    }
