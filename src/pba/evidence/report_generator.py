from __future__ import annotations

import json
from pathlib import Path


def generate_report(run_dir: str | Path) -> str:
    run = Path(run_dir)
    pba_metrics = json.loads((run / "pba_metrics.json").read_text(encoding="utf-8"))
    baseline_metrics = json.loads((run / "baseline_metrics.json").read_text(encoding="utf-8"))
    classification = json.loads((run / "classification.json").read_text(encoding="utf-8"))

    lines = []
    lines.append("PBSA BENCHMARK SUMMARY")
    lines.append("")
    lines.append(f"Run: {run.name}")
    lines.append("")
    lines.append("Classification")
    lines.append(f"- Label: {classification['classification']}")
    lines.append(f"- Downgrade path: {classification['downgrade_path']}")
    lines.append("")
    lines.append("PBA Metrics")
    for k, v in pba_metrics.items():
        lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("Baseline Metrics")
    for name, metrics in baseline_metrics.items():
        lines.append("")
        lines.append(name)
        for k, v in metrics.items():
            lines.append(f"- {k}: {v}")
    lines.append("")
    lines.append("Non-claim locks")
    lines.append("- Not medical guidance.")
    lines.append("- Not biological-law proof.")
    lines.append("- Not mechanism proof.")
    lines.append("- Not clinical validation.")
    lines.append("- Not universal biological theory.")

    report = "\n".join(lines)
    (run / "benchmark_summary.md").write_text(report, encoding="utf-8")
    return report