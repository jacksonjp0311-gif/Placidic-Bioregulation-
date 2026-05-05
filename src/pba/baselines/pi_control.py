from __future__ import annotations

from .base import Baseline
from pba.core.domain import DomainConfig


class PIBaseline(Baseline):
    name = "pi_control"

    def run(self, domain: DomainConfig, perturbations: list[float], config: dict) -> list[dict]:
        kp = float(config.get("kp", 0.06))
        ki = float(config.get("ki", 0.005))
        x = domain.initial_state
        integral = 0.0
        records = []

        for t, p in enumerate(perturbations):
            error = x - domain.target
            integral += error
            correction = -kp * error - ki * integral
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