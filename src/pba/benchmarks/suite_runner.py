from __future__ import annotations

import json
from pathlib import Path
from pba.benchmarks.runner import run_benchmark


def run_suite(root: str | Path, suite_config: str | Path) -> list[str]:
    root = Path(root)
    suite_config = Path(suite_config)
    cfg = json.loads(suite_config.read_text(encoding="utf-8"))

    params = root / cfg.get("parameter_manifest", "configs/pba_params.json")
    baselines = root / cfg.get("baseline_params", "configs/baseline_params.json")
    grid = root / cfg.get("calibration_grid", "configs/calibration_grid.json")
    metrics = root / cfg.get("metric_manifest", "configs/metric_manifest.json")

    run_dirs = []
    for domain_rel in cfg["domains"]:
        run_dir = run_benchmark(root, root / domain_rel, params, baselines, grid, metrics)
        run_dirs.append(str(run_dir))

    return run_dirs