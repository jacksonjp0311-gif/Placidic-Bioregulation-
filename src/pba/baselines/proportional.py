from __future__ import annotations

from .base import Baseline
from pba.core.domain import DomainConfig


class ProportionalBaseline(Baseline):
    name = "proportional_feedback"

    def run(self, domain: DomainConfig, perturbations: list[float], config: dict) -> list[dict]:
        gain = float(config.get("gain", 0.08))
        x = domain.initial_state
        records = []

        for t, p in enumerate(perturbations):
            error = x - domain.target
            direction = 1.0 if error > 0 else -1.0 if error < 0 else 0.0
            correction = -gain * direction
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