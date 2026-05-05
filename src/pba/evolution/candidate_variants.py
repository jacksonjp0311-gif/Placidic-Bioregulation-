from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CandidateVariant:
    candidate_id: str
    target_regimes: tuple[str, ...]
    route_type: str
    status: str = "executable_in_comparison_harness_only"


def load_builtin_candidate_variants() -> dict[str, CandidateVariant]:
    return {
        "direct_route_candidate_v0": CandidateVariant(
            candidate_id="direct_route_candidate_v0",
            target_regimes=("direct_recovery",),
            route_type="direct_correction",
        ),
        "pulse_route_candidate_v0": CandidateVariant(
            candidate_id="pulse_route_candidate_v0",
            target_regimes=("pulse_recovery",),
            route_type="pulse_aware_correction",
        ),
        "oscillatory_preservation_candidate_v0": CandidateVariant(
            candidate_id="oscillatory_preservation_candidate_v0",
            target_regimes=("oscillatory",),
            route_type="oscillatory_preservation",
        ),
        "noisy_recovery_guard_candidate_v0": CandidateVariant(
            candidate_id="noisy_recovery_guard_candidate_v0",
            target_regimes=("noisy",),
            route_type="noisy_guard",
        ),
    }


def candidate_effect(candidate: CandidateVariant, primary_regime: str, secondary_regimes: list[str]) -> dict:
    """Return a conservative deterministic comparison effect.

    This is not a live kernel replacement. It is a comparison-harness candidate
    effect model used to decide whether a real challenger deserves deeper review.
    """
    matched = primary_regime in candidate.target_regimes
    baseline_advantage = "baseline_advantage" in secondary_regimes
    pba_advantage = "pba_advantage" in secondary_regimes
    cusp_risk = "cusp_risk" in secondary_regimes

    if not matched:
        return {
            "matched": False,
            "score_multiplier": 1.08,
            "classification_shift": 0,
            "note": "Candidate not matched to primary regime; conservative penalty applied.",
        }

    if candidate.route_type == "direct_correction":
        multiplier = 0.86 if baseline_advantage else 0.94
        shift = 1 if baseline_advantage else 0
        note = "Direct route benefits direct recovery and baseline-advantage regimes."
    elif candidate.route_type == "pulse_aware_correction":
        multiplier = 0.90 if baseline_advantage else 0.96
        shift = 1 if baseline_advantage else 0
        note = "Pulse route improves pulse-like domains only inside comparison harness."
    elif candidate.route_type == "oscillatory_preservation":
        multiplier = 0.92 if pba_advantage else 0.98
        shift = 1 if pba_advantage else 0
        note = "Oscillatory route preserves PBA-favorable oscillatory behavior."
    elif candidate.route_type == "noisy_guard":
        multiplier = 0.91
        shift = 1
        note = "Noisy guard improves noisy recovery cautiously."
    else:
        multiplier = 1.0
        shift = 0
        note = "Unknown route; no effect."

    if cusp_risk:
        multiplier = min(1.0, multiplier + 0.03)
        note += " Cusp-risk overlay dampened the claimed effect."

    return {
        "matched": True,
        "score_multiplier": round(multiplier, 6),
        "classification_shift": shift,
        "note": note,
    }


def apply_candidate_to_domain(candidate: CandidateVariant, domain_result: dict) -> dict:
    primary = domain_result.get("primary_regime", "unknown")
    secondary = domain_result.get("secondary_regimes", [])
    effect = candidate_effect(candidate, primary, secondary)

    champion_score = float(domain_result.get("champion_score", domain_result.get("pba_score", 1.0)) or 1.0)
    candidate_score = champion_score * effect["score_multiplier"]

    champion_class = domain_result.get("champion_classification", domain_result.get("classification", "PBA-D"))
    candidate_class = shift_classification(champion_class, effect["classification_shift"])

    return {
        "candidate_id": candidate.candidate_id,
        "domain_id": domain_result.get("domain_id", "unknown"),
        "primary_regime": primary,
        "secondary_regimes": secondary,
        "matched": effect["matched"],
        "champion_score": champion_score,
        "candidate_score": round(candidate_score, 6),
        "champion_classification": champion_class,
        "candidate_classification": candidate_class,
        "effect_note": effect["note"],
        "candidate_execution_scope": "comparison_harness_only",
        "kernel_mutation_allowed": False,
    }


def shift_classification(classification: str, shift: int) -> str:
    order = ["PBA-E", "PBA-D", "PBA-C", "PBA-B", "PBA-A"]
    if classification not in order:
        classification = "PBA-D"
    idx = order.index(classification)
    idx = min(len(order) - 1, max(0, idx + shift))
    return order[idx]
