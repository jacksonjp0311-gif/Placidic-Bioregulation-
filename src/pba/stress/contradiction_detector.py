from __future__ import annotations


def detect_contradiction(primary_regime: str | None, secondary_regimes: list[str] | None) -> dict:
    primary = primary_regime or "unknown"
    overlays = set(secondary_regimes or [])

    reasons = []

    if "baseline_advantage" in overlays and "pba_advantage" in overlays and "low_confidence" in overlays:
        reasons.append("baseline_pba_advantage_conflict_under_low_confidence")

    if primary == "unknown" and "pba_advantage" in overlays:
        reasons.append("unknown_primary_with_pba_advantage")

    if "low_confidence" in overlays and "high_oscillation" in overlays and "baseline_advantage" in overlays:
        reasons.append("low_confidence_high_oscillation_baseline_conflict")

    contradiction = bool(reasons)

    return {
        "contradiction": contradiction,
        "reasons": reasons,
        "safe_fail_required": contradiction,
    }
