from __future__ import annotations

import argparse
import json
from pathlib import Path

from pba.benchmarks.runner import run_benchmark
from pba.benchmarks.suite_runner import run_suite
from pba.evidence.evidence_package import compile_evidence_package


def main() -> int:
    parser = argparse.ArgumentParser(prog="pba", description="PBSA/PBA local benchmark CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    rb = sub.add_parser("run-benchmark")
    rb.add_argument("--domain", required=True)
    rb.add_argument("--params", default="configs/pba_params.json")
    rb.add_argument("--baselines", default="configs/baseline_params.json")
    rb.add_argument("--grid", default="configs/calibration_grid.json")
    rb.add_argument("--metrics", default="configs/metric_manifest.json")

    rs = sub.add_parser("run-suite")
    rs.add_argument("--config", default="configs/suite_v1_0.json")
    rs.add_argument("--no-summary", action="store_true")

    ce = sub.add_parser("compile-evidence")
    ce.add_argument("--run", required=True)

    args = parser.parse_args()
    root = Path.cwd()

    if args.cmd == "run-benchmark":
        run_dir = run_benchmark(root, args.domain, args.params, args.baselines, args.grid, args.metrics)
        print(json.dumps({"status": "complete", "run_dir": str(run_dir)}, indent=2))
        return 0

    if args.cmd == "run-suite":
        result = run_suite(root, args.config, compile_summary=not args.no_summary)
        print(json.dumps({
            "status": "complete",
            "runs": result["runs"],
            "suite_summary_json": result["suite_summary_json"],
            "suite_summary_md": result["suite_summary_md"],
            "overall_classification": result["overall_classification"]
        }, indent=2))
        return 0

    if args.cmd == "compile-evidence":
        package = compile_evidence_package(args.run)
        print(json.dumps(package, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())