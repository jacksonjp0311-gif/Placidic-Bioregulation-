from __future__ import annotations

from dataclasses import dataclass, asdict
from itertools import product


@dataclass(frozen=True)
class ThresholdCandidate:
    candidate_id: str
    route_confidence: float
    safe_fail: float
    contradiction_sensitivity: float
    manual_review: float
    advantage_cutoff: float
    preservation_cutoff: float

    def to_dict(self) -> dict:
        return asdict(self)


def build_candidates(grid: dict) -> list[ThresholdCandidate]:
    values = grid.get("values", {})
    keys = [
        "route_confidence",
        "safe_fail",
        "contradiction_sensitivity",
        "manual_review",
        "advantage_cutoff",
        "preservation_cutoff",
    ]

    pools = [values.get(k, []) for k in keys]
    if any(not pool for pool in pools):
        raise ValueError("Threshold grid missing candidate values.")

    candidates: list[ThresholdCandidate] = []
    for idx, combo in enumerate(product(*pools), start=1):
        candidate = ThresholdCandidate(
            candidate_id=f"theta_candidate_{idx:02d}",
            route_confidence=float(combo[0]),
            safe_fail=float(combo[1]),
            contradiction_sensitivity=float(combo[2]),
            manual_review=float(combo[3]),
            advantage_cutoff=float(combo[4]),
            preservation_cutoff=float(combo[5]),
        )
        candidates.append(candidate)

    limit = int(grid.get("candidate_limit", len(candidates)))
    return candidates[:limit]
