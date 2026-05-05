from __future__ import annotations


def propose_candidate(suite_summary: dict, regime_map: dict, baseline_advantage_map: dict) -> dict:
    """Create a diagnostic candidate proposal without mutating the kernel."""
    baseline_wins = [
        domain for domain, item in baseline_advantage_map.items()
        if item.get("baseline_result") == "baseline_advantage"
    ]
    pba_wins = [
        domain for domain, item in baseline_advantage_map.items()
        if item.get("baseline_result") == "pba_advantage"
    ]

    recommendations = []
    for domain in baseline_wins:
        regime = regime_map.get(domain, {}).get("detected_regime", "unknown")
        recommendations.append({
            "domain_id": domain,
            "regime": regime,
            "action": "preserve baseline win; consider bounded direct-correction route in future candidate",
        })

    for domain in pba_wins:
        regime = regime_map.get(domain, {}).get("detected_regime", "unknown")
        recommendations.append({
            "domain_id": domain,
            "regime": regime,
            "action": "preserve current PBA behavior as champion-supported local win",
        })

    return {
        "candidate_kernel": None,
        "mode": "diagnostic_first",
        "kernel_mutation_allowed": False,
        "summary": "No kernel replacement in PBSA v1.1 diagnostic phase.",
        "motivation": suite_summary.get("overall_summary", "Suite evidence requires diagnostic interpretation."),
        "recommendations": recommendations,
        "files_changed": [],
        "expected_improvement": [],
    }
