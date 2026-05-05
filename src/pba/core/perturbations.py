from __future__ import annotations

import random
from .domain import DomainConfig


def generate_perturbations(domain: DomainConfig, seed: int) -> list[float]:
    rng = random.Random(seed)
    noise = domain.noise_model
    low = float(noise.get("low", -0.02))
    high = float(noise.get("high", 0.02))

    values: list[float] = []
    for t in range(domain.time_steps):
        p = rng.uniform(low, high)

        if domain.perturbation_family == "pulse_plus_noise":
            if t == domain.time_steps // 4:
                p += 0.35
            if t == domain.time_steps // 2:
                p -= 0.20
        elif domain.perturbation_family == "oscillatory_signal":
            p += 0.10 if (t // 5) % 2 == 0 else -0.10
        elif domain.perturbation_family == "noisy_perturbation":
            p += rng.uniform(-0.08, 0.08)

        values.append(p)

    return values