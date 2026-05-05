from __future__ import annotations

from typing import Any


DIRECT = "direct_recovery"
PULSE = "pulse_recovery"
OSCILLATORY = "oscillatory"
NOISY = "noisy"
UNKNOWN = "unknown"

CUSP = "cusp_risk"
BASELINE_ADVANTAGE = "baseline_advantage"
PBA_ADVANTAGE = "pba_advantage"
HIGH_OSCILLATION = "high_oscillation"
UNRECOVERED = "unrecovered"
LOW_CONFIDENCE = "low_confidence"


def _float(value: Any, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def _unique(values: list[str]) -> list[str]:
    out = []
    for value in values:
        if value not in out:
            out.append(value)
    return out


def detect_regime(
    domain_id: str,
    metrics: dict | None = None,
    comparison: dict | None = None,
    records: list[dict] | None = None,
) -> dict:
    """Detect primary regime plus secondary diagnostic overlays.

    PBSA v1.2 keeps backward compatibility by returning detected_regime as the
    primary regime. This is a computational diagnostic, not a biological diagnosis.
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

    scores = {
        DIRECT: 0.0,
        PULSE: 0.0,
        OSCILLATORY: 0.0,
        NOISY: 0.0,
        CUSP: 0.0,
    }

    evidence_notes = []

    # Domain-shape scoring has priority for primary regime.
    if "temp" in domain_key or "direct" in domain_key:
        scores[DIRECT] += 1.0
        evidence_notes.append("Domain identity supports direct_recovery primary regime.")

    if "pulse" in domain_key:
        scores[PULSE] += 1.0
        evidence_notes.append("Domain identity supports pulse_recovery primary regime.")

    if "osc" in domain_key:
        scores[OSCILLATORY] += 1.0
        evidence_notes.append("Domain identity supports oscillatory primary regime.")

    # Feature-based scoring.
    if sign_changes >= 4:
        scores[OSCILLATORY] += 0.6
        evidence_notes.append("Repeated sign changes support oscillatory regime.")

    if oscillation_amplitude >= 0.75:
        scores[OSCILLATORY] += 0.35
        evidence_notes.append("High oscillation amplitude supports oscillatory overlay.")

    if recovery_time is None and cumulative_deviation > 0:
        scores[NOISY] += 0.5
        evidence_notes.append("Unrecovered response supports noisy/unrecovered overlay.")

    if baseline_result == "baseline_advantage" and best_baseline == "proportional_feedback":
        scores[DIRECT] += 0.25
        evidence_notes.append("Proportional baseline advantage supports direct-correction interpretation.")

    if cusp_warnings >= 3:
        scores[CUSP] += _clamp01(cusp_warnings / 10.0)
        evidence_notes.append("Cusp warnings support cusp_risk overlay.")

    if max_deviation >= 0.85:
        scores[CUSP] += 0.35
        evidence_notes.append("High max deviation supports cusp_risk overlay.")

    scores = {k: round(_clamp01(v), 6) for k, v in scores.items()}

    primary_candidates = {
        DIRECT: scores[DIRECT],
        PULSE: scores[PULSE],
        OSCILLATORY: scores[OSCILLATORY],
        NOISY: scores[NOISY],
    }

    primary_regime = max(primary_candidates, key=primary_candidates.get)
    if primary_candidates[primary_regime] <= 0.0:
        primary_regime = UNKNOWN
        evidence_notes.append("No strong primary regime evidence found.")

    secondary = []
    risk_overlays = []

    if scores[CUSP] > 0:
        secondary.append(CUSP)
        risk_overlays.append(CUSP)

    if baseline_result == "baseline_advantage":
        secondary.append(BASELINE_ADVANTAGE)
        evidence_notes.append("Baseline advantage preserved as secondary diagnostic overlay.")

    if baseline_result == "pba_advantage":
        secondary.append(PBA_ADVANTAGE)
        evidence_notes.append("PBA advantage preserved as secondary diagnostic overlay.")

    if oscillation_amplitude >= 0.75 and primary_regime != OSCILLATORY:
        secondary.append(HIGH_OSCILLATION)

    if recovery_time is None and cumulative_deviation > 0:
        secondary.append(UNRECOVERED)
        risk_overlays.append(UNRECOVERED)

    confidence = "high"
    if primary_regime == UNKNOWN:
        confidence = "low"
        secondary.append(LOW_CONFIDENCE)
    elif scores.get(primary_regime, 0.0) < 0.75:
        confidence = "medium"

    secondary = _unique(secondary)
    risk_overlays = _unique(risk_overlays)

    recommendation = "preserve champion kernel; improve diagnostics only"
    if primary_regime == DIRECT and baseline_result == "baseline_advantage":
        recommendation = "preserve baseline win; consider direct-correction candidate only after holdout evidence"
    elif primary_regime == PULSE and baseline_result == "baseline_advantage":
        recommendation = "preserve baseline win; inspect pulse recovery correction behavior before kernel changes"
    elif primary_regime == OSCILLATORY and baseline_result == "pba_advantage":
        recommendation = "preserve current PBA behavior as champion-supported local win"
    elif CUSP in risk_overlays:
        recommendation = "preserve champion; treat cusp_risk as caution overlay, not primary regime collapse"

    return {
        "domain_id": domain_id,
        "detected_regime": primary_regime,
        "primary_regime": primary_regime,
        "secondary_regimes": secondary,
        "risk_overlays": risk_overlays,
        "regime_scores": scores,
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
        "interpretation": (
            f"Primary regime is {primary_regime}; secondary overlays are {secondary}. "
            "This is computational diagnosis only."
        ),
        "evidence_notes": evidence_notes,
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
