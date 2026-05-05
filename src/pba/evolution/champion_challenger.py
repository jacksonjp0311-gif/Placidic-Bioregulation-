from __future__ import annotations


def _count(summary: dict, label: str) -> int:
    return int(summary.get("classification_counts", {}).get(label, 0) or 0)


def compare_champion_challenger(
    champion_summary: dict,
    candidate_summary: dict | None = None,
    policy: dict | None = None,
) -> dict:
    """Compare champion/candidate summaries.

    In diagnostic-first mode with no candidate, always preserve champion.
    """
    policy = policy or {}
    if candidate_summary is None:
        return {
            "decision": "preserve_champion",
            "decision_reason": "Diagnostic evidence generated; no candidate kernel supplied.",
            "candidate_accepted": False,
            "non_claim_locks_preserved": True,
        }

    if _count(candidate_summary, "PBA-E") > 0:
        return {
            "decision": "reject",
            "decision_reason": "Candidate produced PBA-E classification.",
            "candidate_accepted": False,
            "non_claim_locks_preserved": False,
        }

    lower_is_better = policy.get("score_policy", {}).get("lower_is_better", True)
    c_pba = float(champion_summary.get("mean_pba_score", 0.0) or 0.0)
    n_pba = float(candidate_summary.get("mean_pba_score", 0.0) or 0.0)

    if lower_is_better:
        improved = n_pba < c_pba
    else:
        improved = n_pba > c_pba

    if improved and _count(candidate_summary, "PBA-A") >= _count(champion_summary, "PBA-A"):
        return {
            "decision": "accept",
            "decision_reason": "Candidate improves suite score without reducing PBA-A count.",
            "candidate_accepted": True,
            "non_claim_locks_preserved": True,
        }

    return {
        "decision": "preserve_champion",
        "decision_reason": "Candidate does not meet conservative acceptance rule.",
        "candidate_accepted": False,
        "non_claim_locks_preserved": True,
    }
