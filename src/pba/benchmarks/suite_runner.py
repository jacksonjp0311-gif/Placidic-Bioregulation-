from __future__ import annotations

import json
from pathlib import Path
from pba.benchmarks.runner import run_benchmark
from pba.evidence.suite_summary import compile_suite_summary


def run_suite(root: str | Path, suite_config: str | Path, compile_summary: bool = True) -> dict:
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

    result = {
        "runs": run_dirs,
        "suite_summary_json": None,
        "suite_summary_md": None,
        "overall_classification": None
    }

    if compile_summary:
        suite_name = cfg.get("suite_name", suite_config.stem)
        summary = compile_suite_summary(root, run_dirs, suite_name=suite_name)
        result["suite_summary_json"] = summary.get("suite_summary_json")
        result["suite_summary_md"] = summary.get("suite_summary_md")
        result["overall_classification"] = summary.get("overall_classification")

    return result