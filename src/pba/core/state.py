from __future__ import annotations

from dataclasses import dataclass, asdict


@dataclass
class RuntimeState:
    t: int
    x_t: float
    target: float
    delta_phi: float
    omega: float
    correction: float
    signal: float
    allostatic_term: float
    perturbation: float
    cusp_state: str

    def to_dict(self) -> dict:
        return asdict(self)