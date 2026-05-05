from __future__ import annotations


def build_candidate_specs(holdout_summary: dict) -> list[dict]:
    """Build non-executable candidate specifications from evidence.

    v1.3 may specify candidates but must not execute or promote them.
    """
    regime_map = holdout_summary.get("regime_map", {})
    specs = []

    baseline_domains = [
        d for d, r in regime_map.items()
        if "baseline_advantage" in r.get("secondary_regimes", [])
    ]

    pba_domains = [
        d for d, r in regime_map.items()
        if "pba_advantage" in r.get("secondary_regimes", [])
    ]

    direct_like = [
        d for d, r in regime_map.items()
        if r.get("primary_regime") == "direct_recovery"
    ]

    pulse_like = [
        d for d, r in regime_map.items()
        if r.get("primary_regime") == "pulse_recovery"
    ]

    oscillatory_like = [
        d for d, r in regime_map.items()
        if r.get("primary_regime") == "oscillatory"
    ]

    noisy_like = [
        d for d, r in regime_map.items()
        if r.get("primary_regime") == "noisy"
    ]

    if direct_like or baseline_domains:
        specs.append({
            "candidate_id": "direct_route_candidate_v0",
            "status": "specified_not_executable",
            "target_regimes": ["direct_recovery"],
            "motivation": "Baseline advantage in direct-like or proportional-like domains suggests a bounded direct-correction route may be worth testing later.",
            "expected_benefit": "Lower cumulative deviation in direct recovery domains.",
            "risk": "May reduce PBA advantage in oscillatory domains if applied globally.",
            "forbidden_claims": ["medical_claim", "biological_law_claim", "mechanism_proof_claim"],
            "required_tests": ["original_suite", "holdout_suite", "baseline_comparison", "non_claim_locks"],
            "source_domains": sorted(set(direct_like + baseline_domains)),
        })

    if pulse_like:
        specs.append({
            "candidate_id": "pulse_route_candidate_v0",
            "status": "specified_not_executable",
            "target_regimes": ["pulse_recovery"],
            "motivation": "Pulse recovery domains require evidence before changing correction dynamics.",
            "expected_benefit": "Improve recovery time or cumulative deviation in pulse-like domains.",
            "risk": "Over-correction or instability under noisy pulses.",
            "forbidden_claims": ["medical_claim", "biological_law_claim", "mechanism_proof_claim"],
            "required_tests": ["original_suite", "holdout_suite", "baseline_comparison", "non_claim_locks"],
            "source_domains": sorted(set(pulse_like)),
        })

    if oscillatory_like or pba_domains:
        specs.append({
            "candidate_id": "oscillatory_preservation_candidate_v0",
            "status": "specified_not_executable",
            "target_regimes": ["oscillatory"],
            "motivation": "PBA advantage in oscillatory regimes should be preserved rather than overwritten by direct correction.",
            "expected_benefit": "Protect current champion behavior where PBA has local advantage.",
            "risk": "May not improve direct or pulse recovery domains.",
            "forbidden_claims": ["medical_claim", "biological_law_claim", "mechanism_proof_claim"],
            "required_tests": ["original_suite", "holdout_suite", "baseline_comparison", "non_claim_locks"],
            "source_domains": sorted(set(oscillatory_like + pba_domains)),
        })

    if noisy_like:
        specs.append({
            "candidate_id": "noisy_recovery_guard_candidate_v0",
            "status": "specified_not_executable",
            "target_regimes": ["noisy"],
            "motivation": "Noisy recovery domains require guard behavior before candidate execution.",
            "expected_benefit": "Avoid unstable reaction to stochastic perturbation.",
            "risk": "May over-dampen useful correction.",
            "forbidden_claims": ["medical_claim", "biological_law_claim", "mechanism_proof_claim"],
            "required_tests": ["original_suite", "holdout_suite", "baseline_comparison", "non_claim_locks"],
            "source_domains": sorted(set(noisy_like)),
        })

    return specs
