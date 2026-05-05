from __future__ import annotations

from .base import Baseline
from pba.core.domain import DomainConfig


class ThresholdBaseline(Baseline):
    name = "threshold_control"

    def run(self, domain: DomainConfig, perturbations: list[float], config: dict) -> list[dict]:
        threshold = float(config.get("threshold", 0.20))
        step = float(config.get("step", 0.10))
        x = domain.initial_state
        records = []

        for t, p in enumerate(perturbations):
            error = x - domain.target
            correction = 0.0
            if abs(error) > threshold:
                correction = -step * (1.0 if error > 0 else -1.0)
            records.append({
                "model": self.name,
                "t": t,
                "x_t": x,
                "target": domain.target,
                "delta_phi": abs(error),
                "correction": correction,
                "perturbation": p
            })
            x = x + correction + p

        return records