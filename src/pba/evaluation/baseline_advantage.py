from __future__ import annotations


def map_baseline_advantage_from_runs(runs: list[dict]) -> dict:
    """Map each domain to PBA, baseline, tie, or unknown winner."""
    output = {}
    for run in runs:
        domain_id = str(run.get("domain_id", "unknown"))
        result = run.get("baseline_result", "unknown")
        best_baseline = run.get("best_baseline")
        if result == "pba_advantage":
            winner = "PBA"
        elif result == "baseline_advantage":
            winner = best_baseline or "baseline"
        elif result == "tie":
            winner = "tie"
        else:
            winner = "unknown"

        output[domain_id] = {
            "winner": winner,
            "baseline_result": result,
            "best_baseline": best_baseline,
            "pba_score": run.get("pba_score"),
            "best_baseline_score": run.get("best_baseline_score"),
            "classification": run.get("classification"),
            "interpretation": interpret_advantage(result, best_baseline),
        }
    return output


def interpret_advantage(result: str, best_baseline: str | None = None) -> str:
    if result == "pba_advantage":
        return "PBA has local advantage under declared toy conditions."
    if result == "baseline_advantage":
        base = best_baseline or "a simpler baseline"
        return f"{base} performs better; preserve as diagnostic evidence."
    if result == "tie":
        return "Simpler baseline performs equally well; downgrade interpretation."
    return "Insufficient comparison evidence."
