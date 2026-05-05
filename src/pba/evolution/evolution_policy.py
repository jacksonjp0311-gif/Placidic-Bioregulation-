from __future__ import annotations

import json
from pathlib import Path


DEFAULT_POLICY = {
    "version": "PBSA-EvolutionPolicy-v1.1",
    "mode": "diagnostic_first",
    "kernel_mutation_allowed": False,
    "acceptance_rules": {
        "tests_must_pass": True,
        "pba_e_count_must_be_zero": True,
        "baseline_comparison_required": True,
        "non_claim_locks_required": True,
        "holdout_required_before_kernel_replacement": True,
        "do_not_hide_baseline_wins": True,
        "evolution_report_required": True,
        "decision_ledger_required": True,
    },
    "score_policy": {
        "primary_metric": "cumulative_deviation",
        "lower_is_better": True,
        "preserve_or_explain_pba_a_loss": True,
    },
}


def load_evolution_policy(path: str | Path | None = None) -> dict:
    if path is None:
        return dict(DEFAULT_POLICY)
    p = Path(path)
    if not p.exists():
        return dict(DEFAULT_POLICY)
    data = json.loads(p.read_text(encoding="utf-8"))
    merged = dict(DEFAULT_POLICY)
    merged.update(data)
    return merged
