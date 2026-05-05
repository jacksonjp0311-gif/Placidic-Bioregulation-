from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DomainConfig:
    domain_id: str
    regulated_variable: str
    target: float
    viable_interval: tuple[float, float]
    time_steps: int
    initial_state: float
    perturbation_family: str
    noise_model: dict[str, Any]
    observation_cadence: int
    fit_seed: int
    eval_seed: int
    non_claim_locks: list[str]

    @classmethod
    def from_file(cls, path: str | Path) -> "DomainConfig":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "DomainConfig":
        split = data.get("fit_eval_split", {})
        obj = cls(
            domain_id=str(data["domain_id"]),
            regulated_variable=str(data.get("regulated_variable", "x_t")),
            target=float(data["target"]),
            viable_interval=(float(data["viable_interval"][0]), float(data["viable_interval"][1])),
            time_steps=int(data["time_steps"]),
            initial_state=float(data["initial_state"]),
            perturbation_family=str(data.get("perturbation_family", "pulse_plus_noise")),
            noise_model=dict(data.get("noise_model", {})),
            observation_cadence=int(data.get("observation_cadence", 1)),
            fit_seed=int(split.get("fit_seed", 101)),
            eval_seed=int(split.get("eval_seed", 202)),
            non_claim_locks=list(data.get("non_claim_locks", [])),
        )
        obj.validate()
        return obj

    def validate(self) -> None:
        if not self.domain_id:
            raise ValueError("domain_id is required")
        if self.time_steps < 2:
            raise ValueError("time_steps must be >= 2")
        low, high = self.viable_interval
        if low >= high:
            raise ValueError("viable_interval must have low < high")
        required = {"not_medical", "not_biological_law", "not_mechanism_proof"}
        missing = sorted(required.difference(set(self.non_claim_locks)))
        if missing:
            raise ValueError(f"missing non-claim locks: {missing}")