from __future__ import annotations

from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ParameterManifest:
    eta: float = 0.10
    tau_1: float = 0.30
    tau_2: float = 0.80
    kappa: float = 0.05
    alpha: float = 0.80
    theta_M: float = 0.70
    beta: float = 0.10
    gamma: float = 0.05

    @classmethod
    def from_file(cls, path: str | Path) -> "ParameterManifest":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ParameterManifest":
        params = data.get("parameters", data)
        allowed = cls.__annotations__.keys()
        obj = cls(**{k: float(v) for k, v in params.items() if k in allowed})
        obj.validate()
        return obj

    def validate(self) -> None:
        if self.eta <= 0:
            raise ValueError("eta must be positive")
        if not (0.0 <= self.kappa <= 1.0):
            raise ValueError("kappa must be in [0, 1]")
        if self.tau_1 >= self.tau_2:
            raise ValueError("tau_1 must be less than tau_2")
        if self.alpha < 0:
            raise ValueError("alpha must be nonnegative")

    def to_dict(self) -> dict[str, float]:
        return asdict(self)