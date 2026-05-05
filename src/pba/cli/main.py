from __future__ import annotations

import argparse
import json
from pathlib import Path

from pba.benchmarks.runner import run_benchmark
from pba.benchmarks.suite_runner import run_suite
from pba.evidence.evidence_package import compile_evidence_package
from pba.evidence.evolution_report import build_evolution_report
from pba.evidence.holdout_summary import compile_holdout_summary
from pba.evolution.candidate_readiness import build_candidate_readiness_report
from pba.evolution.champion_challenger import compare_champion_challenger
from pba.evolution.evolution_policy import load_evolution_policy


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

    de = sub.add_parser("diagnose-evolution")
    de.add_argument("--suite-summary", default=None)
    de.add_argument("--policy", default="configs/evolution_policy.json")

    hs = sub.add_parser("summarize-holdout")
    hs.add_argument("--suite-summary", default=None)

    cr = sub.add_parser("candidate-readiness")
    cr.add_argument("--holdout-summary", default=None)

    ck = sub.add_parser("compare-kernels")
    ck.add_argument("--champion-summary", default=None)
    ck.add_argument("--candidate-summary", default=None)
    ck.add_argument("--policy", default="configs/evolution_policy.json")

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

    if args.cmd == "diagnose-evolution":
        result = build_evolution_report(root, suite_summary_path=args.suite_summary, policy_path=args.policy)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "summarize-holdout":
        result = compile_holdout_summary(root, suite_summary_path=args.suite_summary)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "candidate-readiness":
        result = build_candidate_readiness_report(root, holdout_summary_path=args.holdout_summary)
        print(json.dumps(result, indent=2))
        return 0

    if args.cmd == "compare-kernels":
        policy = load_evolution_policy(args.policy)

        def load(path_text):
            if not path_text:
                return None
            return json.loads(Path(path_text).read_text(encoding="utf-8"))

        champion = load(args.champion_summary) or {}
        candidate = load(args.candidate_summary)
        result = compare_champion_challenger(champion, candidate, policy)
        print(json.dumps(result, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
