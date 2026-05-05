from __future__ import annotations

from .base import Baseline
from pba.core.domain import DomainConfig


class ReturnToSetpointBaseline(Baseline):
    name = "return_to_setpoint"

    def run(self, domain: DomainConfig, perturbations: list[float], config: dict) -> list[dict]:
        rate = float(config.get("rate", 0.05))
        x = domain.initial_state
        records = []

        for t, p in enumerate(perturbations):
            error = x - domain.target
            correction = -rate * error
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