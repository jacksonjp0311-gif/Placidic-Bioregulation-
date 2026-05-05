# src/pba/evidence

## Purpose

Evidence package, suite summary, file manifest, runtime ledger, and report generation.

## S - Formal specification

Turns runtime outputs into machine-readable evidence and conservative summaries.

## H - Hooks

Used by benchmark runner, suite runner, CLI, reports, ledgers, and root README.

## A - Artifacts

- runtime_ledger.py
- evidence_package.py
- report_generator.py
- file_manifest.py
- suite_summary.py

## T - Theory

Evidence must be machine-readable before narrative interpretation.

## I - Invariants

- Evidence package must preserve files and claim boundary.
- Suite summary must aggregate without inflating claims.
- Reports must preserve non-claim boundary.
- Ledgers must record continuity.

## E - Example

reports/suite_summaries contains generated suite_summary.json and suite_summary.md.

## PBSA v1.1 evolution reporting

- evolution_report.py generates diagnostic evolution reports from suite summaries.
- Reports preserve baseline wins, detected regimes, candidate recommendations, and non-claim locks.
- Evolution reports do not replace the champion kernel.

## PBSA v1.2 evolution report schema

evolution_report.py now writes PBSA-v1.2 reports with:

- diagnostic_upgrade = multi_label_regime_detection
- domain_regimes
- primary_regime
- secondary_regimes
- risk_overlays
- evidence_notes

The decision remains preserve_champion unless a future candidate passes the full acceptance policy.

## PBSA v1.3 holdout summary

holdout_summary.py generates:
- holdout_summary.json
- holdout_summary.md
- regime coverage matrix
- candidate readiness preconditions

Holdout evidence is computational only and does not validate biological claims.
