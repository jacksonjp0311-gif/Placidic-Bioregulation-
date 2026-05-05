from __future__ import annotations

from abc import ABC, abstractmethod
from pba.core.domain import DomainConfig


class Baseline(ABC):
    name = "base"

    @abstractmethod
    def run(self, domain: DomainConfig, perturbations: list[float], config: dict) -> list[dict]:
        raise NotImplementedError