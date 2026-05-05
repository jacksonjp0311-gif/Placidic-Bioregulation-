from __future__ import annotations

import itertools
from pba.core.parameters import ParameterManifest
from pba.core.kernel import run_pba
from pba.calibration.objective import objective


def expand_grid(grid: dict) -> list[dict]:
    keys = list(grid.keys())
    values = [grid[k] for k in keys]
    return [dict(zip(keys, combo)) for combo in itertools.product(*values)]


def calibrate(domain, base_params: ParameterManifest, perturbations: list[float], grid: dict) -> dict:
    trials = []
    best = None
    base = base_params.to_dict()

    for idx, candidate in enumerate(expand_grid(grid)):
        params_dict = dict(base)
        params_dict.update(candidate)
        params = ParameterManifest.from_dict(params_dict)
        records = run_pba(domain, params, perturbations)
        loss = objective(records, domain.viable_interval)

        trial = {
            "trial": idx,
            "params": params.to_dict(),
            "loss": loss
        }
        trials.append(trial)

        if best is None or loss < best["loss"]:
            best = trial

    return {
        "calibration_id": "PBSA-CAL-local",
        "method": "grid_search",
        "objective": "J_pba_local_v1",
        "fit_seed": domain.fit_seed,
        "eval_seed": domain.eval_seed,
        "selected_params": best["params"],
        "fit_loss": best["loss"],
        "trial_count": len(trials),
        "trials": trials,
        "downgrade_notes": []
    }