from __future__ import annotations

from pba.evaluation.metrics import compute_metrics


def objective(records: list[dict], viable_interval: tuple[float, float]) -> float:
    metrics = compute_metrics(records, viable_interval)
    return (
        metrics["cumulative_deviation"]
        + metrics["overshoot"]
        + metrics["undershoot"]
        + 0.25 * metrics["oscillation_amplitude"]
        + 0.10 * metrics["cusp_warnings"]
        - 0.10 * metrics["signal_preservation"]
    )