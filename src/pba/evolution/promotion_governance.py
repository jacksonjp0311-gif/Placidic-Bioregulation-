from __future__ import annotations


DECISIONS = {
    "preserve_champion",
    "reject_candidate",
    "preserve_candidate_for_later",
    "route_to_baseline",
    "route_by_regime",
    "promote_candidate_pending_review",
}


def classification_rank(value: str) -> int:
    order = {"PBA-E": 0, "PBA-D": 1, "PBA-C": 2, "PBA-B": 3, "PBA-A": 4}
    return order.get(value, 0)


def decide_promotion(report: dict) -> dict:
    """Governed decision. Never automatically replaces the kernel."""
    original = report.get("original_suite_result", {})
    holdout = report.get("holdout_suite_result", {})

    champion_original = original.get("champion_classification", "PBA-D")
    challenger_original = original.get("best_challenger_classification", "PBA-D")
    champion_holdout = holdout.get("champion_classification", "PBA-D")
    challenger_holdout = holdout.get("best_challenger_classification", "PBA-D")

    original_delta = classification_rank(challenger_original) - classification_rank(champion_original)
    holdout_delta = classification_rank(challenger_holdout) - classification_rank(champion_holdout)

    baseline_visible = bool(report.get("baseline_visibility_preserved", True))
    non_claim = bool(report.get("non_claim_locks_preserved", True))
    rcc = bool(report.get("rcc_contract_preserved", True))

    if not (baseline_visible and non_claim and rcc):
        decision = "reject_candidate"
        reason = "Governance surface failed: baseline, non-claim, or RCC visibility not preserved."
    elif original_delta < 0 or holdout_delta < 0:
        decision = "reject_candidate"
        reason = "Candidate worsened original or holdout classification."
    elif original_delta > 0 and holdout_delta > 0:
        decision = "promote_candidate_pending_review"
        reason = "Candidate improved original and holdout classifications; manual review still required."
    elif holdout_delta > 0 and original_delta >= 0:
        decision = "route_by_regime"
        reason = "Candidate improved holdout or preserved original; routing is safer than global replacement."
    elif original_delta == 0 and holdout_delta == 0:
        decision = "preserve_candidate_for_later"
        reason = "Candidate is non-worse but not strong enough for pending-review promotion."
    else:
        decision = "preserve_champion"
        reason = "Champion remains best governed default."

    return {
        "decision": decision,
        "decision_reason": reason,
        "original_delta": original_delta,
        "holdout_delta": holdout_delta,
        "promotion_status": "no_automatic_promotion",
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "candidate_execution_is_promotion": False,
    }
