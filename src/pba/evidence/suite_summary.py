from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean


CLASS_ORDER = ["PBA-A", "PBA-B", "PBA-C", "PBA-D", "PBA-E"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def classify_suite(class_counts: dict[str, int], total: int) -> dict:
    pba_a = class_counts.get("PBA-A", 0)
    pba_b = class_counts.get("PBA-B", 0)
    pba_c = class_counts.get("PBA-C", 0)
    pba_d = class_counts.get("PBA-D", 0)
    pba_e = class_counts.get("PBA-E", 0)

    if total == 0:
        return {
            "overall_classification": "PBA-D",
            "overall_summary": "No valid run directories were available for suite classification.",
            "downgrade_path": "Insufficient evidence."
        }

    if pba_e > 0:
        return {
            "overall_classification": "PBA-E",
            "overall_summary": "At least one run violated a rejection condition.",
            "downgrade_path": "Rejected at suite level because one or more runs were PBA-E."
        }

    if pba_a == total:
        return {
            "overall_classification": "PBA-A",
            "overall_summary": "PBA achieved strong local benchmark advantage across every declared suite domain.",
            "downgrade_path": "No suite-level downgrade."
        }

    if (pba_a + pba_b) == total and pba_a > 0:
        return {
            "overall_classification": "PBA-B",
            "overall_summary": "PBA showed useful suite-level advantage, with at least one run downgraded by identifiability or partial-evidence caution.",
            "downgrade_path": "Downgraded because not every domain reached PBA-A."
        }

    if pba_a > 0 and pba_c > 0:
        return {
            "overall_classification": "PBA-C",
            "overall_summary": "Mixed suite evidence: PBA wins in at least one domain, but simpler baselines perform equally well or better in at least one domain.",
            "downgrade_path": "Downgraded because suite evidence is mixed and baseline-superior domains exist."
        }

    if pba_c == total:
        return {
            "overall_classification": "PBA-C",
            "overall_summary": "Simpler baselines perform equally well or better across the declared suite.",
            "downgrade_path": "Downgraded because PBA does not outperform simpler baselines in this suite."
        }

    if pba_d > 0:
        return {
            "overall_classification": "PBA-D",
            "overall_summary": "Insufficient or incomplete evidence exists in one or more suite runs.",
            "downgrade_path": "Downgraded because at least one run is insufficiently evidenced."
        }

    return {
        "overall_classification": "PBA-D",
        "overall_summary": "Suite evidence does not support a stronger classification.",
        "downgrade_path": "Default conservative downgrade."
    }


def compile_suite_summary(root: str | Path, run_dirs: list[str | Path], suite_name: str = "suite_v1_0") -> dict:
    root = Path(root)
    summary_dir = root / "reports" / "suite_summaries"
    summary_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S_%fZ")
    out_dir = summary_dir / f"{suite_name}_{timestamp}"
    out_dir.mkdir(parents=True, exist_ok=True)

    rows = []
    class_counter = Counter()
    baseline_counter = Counter()
    pba_scores = []
    best_baseline_scores = []

    for run_dir_raw in run_dirs:
        run_dir = Path(run_dir_raw)

        classification_path = run_dir / "classification.json"
        comparison_path = run_dir / "metric_comparison.json"
        domain_path = run_dir / "domain_config.json"
        ident_path = run_dir / "identifiability_report.json"

        if not classification_path.exists() or not comparison_path.exists():
            row = {
                "run_dir": str(run_dir),
                "domain_id": None,
                "classification": "PBA-D",
                "baseline_result": "missing_evidence",
                "pba_score": None,
                "best_baseline": None,
                "best_baseline_score": None,
                "identifiability_status": "missing",
                "non_claim_locks_preserved": False,
                "downgrade_path": "Missing classification or metric comparison file."
            }
            rows.append(row)
            class_counter["PBA-D"] += 1
            continue

        c = load_json(classification_path)
        m = load_json(comparison_path)
        d = load_json(domain_path) if domain_path.exists() else {}
        ident = load_json(ident_path) if ident_path.exists() else {}

        label = c.get("classification", "PBA-D")
        class_counter[label] += 1

        best_baseline = m.get("best_baseline")
        if best_baseline:
            baseline_counter[best_baseline] += 1

        pba_score = m.get("pba_score")
        best_baseline_score = m.get("best_baseline_score")
        if isinstance(pba_score, (int, float)):
            pba_scores.append(float(pba_score))
        if isinstance(best_baseline_score, (int, float)):
            best_baseline_scores.append(float(best_baseline_score))

        rows.append({
            "run_dir": str(run_dir),
            "domain_id": d.get("domain_id"),
            "classification": label,
            "PBAScore": c.get("PBAScore"),
            "baseline_result": c.get("baseline_result"),
            "pba_score": pba_score,
            "best_baseline": best_baseline,
            "best_baseline_score": best_baseline_score,
            "primary_metric": m.get("primary_metric"),
            "identifiability_status": c.get("identifiability_status", ident.get("status")),
            "non_claim_locks_preserved": c.get("non_claim_locks_preserved"),
            "downgrade_path": c.get("downgrade_path")
        })

    total = len(rows)
    class_counts = {k: class_counter.get(k, 0) for k in CLASS_ORDER}
    suite_class = classify_suite(class_counts, total)

    pba_advantage_count = sum(1 for row in rows if row.get("baseline_result") == "pba_advantage")
    baseline_advantage_count = sum(1 for row in rows if row.get("baseline_result") == "baseline_advantage")
    tie_count = sum(1 for row in rows if row.get("baseline_result") == "tie")

    summary = {
        "suite_summary_id": f"PBSA-SUITE-{timestamp}",
        "suite_name": suite_name,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "run_count": total,
        "classification_counts": class_counts,
        "pba_advantage_count": pba_advantage_count,
        "baseline_advantage_count": baseline_advantage_count,
        "tie_count": tie_count,
        "mean_pba_score": mean(pba_scores) if pba_scores else None,
        "mean_best_baseline_score": mean(best_baseline_scores) if best_baseline_scores else None,
        "best_baseline_frequency": dict(baseline_counter),
        "overall_classification": suite_class["overall_classification"],
        "overall_summary": suite_class["overall_summary"],
        "suite_downgrade_path": suite_class["downgrade_path"],
        "non_claim_boundary": {
            "supports": "local toy-suite implementation evidence only",
            "does_not_support": [
                "medical guidance",
                "biological law",
                "mechanism proof",
                "clinical validation",
                "universal biological theory"
            ]
        },
        "runs": rows
    }

    json_path = out_dir / "suite_summary.json"
    md_path = out_dir / "suite_summary.md"

    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    md_path.write_text(render_suite_markdown(summary), encoding="utf-8")

    summary["suite_summary_json"] = str(json_path)
    summary["suite_summary_md"] = str(md_path)

    return summary


def render_suite_markdown(summary: dict) -> str:
    lines = []
    lines.append("# PBSA Suite Summary")
    lines.append("")
    lines.append(f"Suite ID: {summary['suite_summary_id']}")
    lines.append(f"Suite name: {summary['suite_name']}")
    lines.append(f"Created UTC: {summary['created_utc']}")
    lines.append("")
    lines.append("## Overall Classification")
    lines.append("")
    lines.append(f"- Overall classification: {summary['overall_classification']}")
    lines.append(f"- Summary: {summary['overall_summary']}")
    lines.append(f"- Downgrade path: {summary['suite_downgrade_path']}")
    lines.append("")
    lines.append("## Counts")
    lines.append("")
    lines.append(f"- Run count: {summary['run_count']}")
    for key, value in summary["classification_counts"].items():
        lines.append(f"- {key}: {value}")
    lines.append(f"- PBA advantage count: {summary['pba_advantage_count']}")
    lines.append(f"- Baseline advantage count: {summary['baseline_advantage_count']}")
    lines.append(f"- Tie count: {summary['tie_count']}")
    lines.append("")
    lines.append("## Scores")
    lines.append("")
    lines.append(f"- Mean PBA score: {summary['mean_pba_score']}")
    lines.append(f"- Mean best baseline score: {summary['mean_best_baseline_score']}")
    lines.append(f"- Best baseline frequency: {summary['best_baseline_frequency']}")
    lines.append("")
    lines.append("## Run Table")
    lines.append("")
    lines.append("| Domain | Classification | PBA score | Best baseline | Best baseline score | Result | Identifiability |")
    lines.append("|---|---:|---:|---|---:|---|---|")
    for row in summary["runs"]:
        lines.append(
            f"| {row.get('domain_id')} | {row.get('classification')} | {row.get('pba_score')} | "
            f"{row.get('best_baseline')} | {row.get('best_baseline_score')} | "
            f"{row.get('baseline_result')} | {row.get('identifiability_status')} |"
        )
    lines.append("")
    lines.append("## Non-Claim Boundary")
    lines.append("")
    lines.append("This suite summary supports local toy-suite implementation evidence only.")
    lines.append("It does not support medical guidance, biological-law claims, mechanism proof, clinical validation, or universal biological theory.")
    lines.append("")
    return "\n".join(lines)