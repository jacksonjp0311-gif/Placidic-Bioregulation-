from __future__ import annotations

from statistics import mean


def compute_metrics(records: list[dict], viable_interval: tuple[float, float]) -> dict:
    deltas = [float(r.get("delta_phi", abs(float(r["x_t"]) - float(r["target"])))) for r in records]
    xs = [float(r["x_t"]) for r in records]
    low, high = viable_interval

    cumulative_deviation = sum(deltas)
    overshoot = max(max(xs) - high, 0.0) if xs else 0.0
    undershoot = max(low - min(xs), 0.0) if xs else 0.0
    cusp_warnings = sum(1 for r in records if r.get("cusp_state") in {"caution", "halt-audit"})
    signal_values = [float(r.get("signal", 1.0)) for r in records]
    signal_preservation = mean(signal_values) if signal_values else 1.0

    recovery_time = None
    for r in records:
        if low <= float(r["x_t"]) <= high:
            recovery_time = int(r["t"])
            break

    oscillation_amplitude = (max(xs) - min(xs)) if xs else 0.0

    return {
        "recovery_time": recovery_time,
        "overshoot": overshoot,
        "undershoot": undershoot,
        "oscillation_amplitude": oscillation_amplitude,
        "cumulative_deviation": cumulative_deviation,
        "mean_deviation": mean(deltas) if deltas else 0.0,
        "max_deviation": max(deltas) if deltas else 0.0,
        "cusp_warnings": cusp_warnings,
        "signal_preservation": signal_preservation,
        "robustness": 1.0 / (1.0 + cumulative_deviation),
        "parameter_sensitivity": None
    }


def compare_pba_to_baselines(pba_metrics: dict, baseline_metrics: dict) -> dict:
    pba_score = float(pba_metrics["cumulative_deviation"])
    baseline_scores = {
        name: float(metrics["cumulative_deviation"])
        for name, metrics in baseline_metrics.items()
    }

    best_baseline_name = min(baseline_scores, key=baseline_scores.get)
    best_baseline_score = baseline_scores[best_baseline_name]

    if pba_score < best_baseline_score:
        result = "pba_advantage"
    elif pba_score == best_baseline_score:
        result = "tie"
    else:
        result = "baseline_advantage"

    return {
        "primary_metric": "cumulative_deviation",
        "pba_score": pba_score,
        "best_baseline": best_baseline_name,
        "best_baseline_score": best_baseline_score,
        "baseline_result": result
    }