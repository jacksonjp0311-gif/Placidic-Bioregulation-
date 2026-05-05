from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from pba.core.domain import DomainConfig
from pba.core.parameters import ParameterManifest
from pba.core.perturbations import generate_perturbations
from pba.core.kernel import run_pba
from pba.baselines import ProportionalBaseline, PIBaseline, ThresholdBaseline, ReturnToSetpointBaseline
from pba.calibration.grid_search import calibrate
from pba.evaluation.metrics import compute_metrics, compare_pba_to_baselines
from pba.evaluation.identifiability import identifiability_report
from pba.evaluation.classification import classify
from pba.evidence.runtime_ledger import append_ledger
from pba.evidence.evidence_package import compile_evidence_package
from pba.evidence.report_generator import generate_report
from pba.evidence.file_manifest import write_file_manifest


def write_json(path: Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, sort_keys=True) + "\n")


def run_benchmark(
    root: str | Path,
    domain_path: str | Path,
    params_path: str | Path,
    baseline_path: str | Path,
    calibration_grid_path: str | Path,
    metric_manifest_path: str | Path
) -> Path:
    root = Path(root)
    domain_path = Path(domain_path)
    params_path = Path(params_path)
    baseline_path = Path(baseline_path)
    calibration_grid_path = Path(calibration_grid_path)
    metric_manifest_path = Path(metric_manifest_path)

    run_id = "run_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = root / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    domain = DomainConfig.from_file(domain_path)
    base_params = ParameterManifest.from_file(params_path)
    baseline_cfg = json.loads(baseline_path.read_text(encoding="utf-8"))
    calibration_grid = json.loads(calibration_grid_path.read_text(encoding="utf-8")).get("grid", {})
    metric_manifest = json.loads(metric_manifest_path.read_text(encoding="utf-8"))

    for src, dst in [
        (domain_path, "domain_config.json"),
        (params_path, "parameter_manifest.json"),
        (baseline_path, "baseline_params.json"),
        (calibration_grid_path, "calibration_grid.json"),
        (metric_manifest_path, "metric_manifest.json")
    ]:
        shutil.copyfile(src, run_dir / dst)

    append_ledger(run_dir / "result_ledger.jsonl", {"event": "run_started", "domain": domain.domain_id})

    fit_perturbations = generate_perturbations(domain, domain.fit_seed)
    cal = calibrate(domain, base_params, fit_perturbations, calibration_grid)
    write_json(run_dir / "calibration_record.json", cal)

    selected = ParameterManifest.from_dict(cal["selected_params"])
    eval_perturbations = generate_perturbations(domain, domain.eval_seed)

    pba_records = run_pba(domain, selected, eval_perturbations)
    write_jsonl(run_dir / "state_log.jsonl", pba_records)

    baselines = [
        ProportionalBaseline(),
        PIBaseline(),
        ThresholdBaseline(),
        ReturnToSetpointBaseline()
    ]

    baseline_logs = []
    baseline_metrics = {}

    for baseline in baselines:
        records = baseline.run(domain, eval_perturbations, baseline_cfg.get(baseline.name, {}))
        baseline_logs.extend(records)
        baseline_metrics[baseline.name] = compute_metrics(records, domain.viable_interval)

    write_jsonl(run_dir / "baseline_state_log.jsonl", baseline_logs)

    pba_metrics = compute_metrics(pba_records, domain.viable_interval)
    write_json(run_dir / "pba_metrics.json", pba_metrics)
    write_json(run_dir / "baseline_metrics.json", baseline_metrics)

    comparison = compare_pba_to_baselines(pba_metrics, baseline_metrics)
    write_json(run_dir / "metric_comparison.json", comparison)

    ident = identifiability_report(cal["trials"], float(cal["fit_loss"]))
    write_json(run_dir / "identifiability_report.json", ident)

    non_claim_locks_preserved = all(
        lock in domain.non_claim_locks
        for lock in ["not_medical", "not_biological_law", "not_mechanism_proof"]
    )

    class_record = classify(comparison, ident, non_claim_locks_preserved)
    write_json(run_dir / "classification.json", class_record)

    package = compile_evidence_package(run_dir)
    generate_report(run_dir)
    write_file_manifest(root, run_dir / "file_manifest.json")

    append_ledger(run_dir / "result_ledger.jsonl", {
        "event": "run_completed",
        "classification": class_record["classification"],
        "evidence_package": package["evidence_package_id"]
    })

    append_ledger(root / "ledgers" / "pba_runtime_ledger.jsonl", {
        "event": "local_run_completed",
        "run_dir": str(run_dir),
        "domain": domain.domain_id,
        "classification": class_record["classification"]
    })

    return run_dir