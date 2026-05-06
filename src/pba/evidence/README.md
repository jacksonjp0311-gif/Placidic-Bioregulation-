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

## PBSA v1.4 champion/challenger report

Added champion_challenger_report.py.

The report compares candidate routes against the champion across original and holdout evidence while preserving baseline visibility, non-claim locks, and RCC boundaries.

## PBSA v2.0 route evidence

Added:
- route_evidence.py
- routed_suite_report.py

Route evidence explains why a route was selected and preserves non-claim boundaries.

## PBSA v2.1 routed validation report

Added:
- routed_validation_report.py

The report emits routed advantage, route preservation score, best control policy, and route failure surface.

## PBSA v2.2 external validation report

Added:
- external_validation_report.py

The report emits internal advantage, external advantage, advantage drift, preservation drift, route frequency drift, and external failure surface.

## PBSA v2.3 stress validation report

Added:
- stress_validation_report.py

The report emits safe-fail score, crash rate, stress advantage drift, stress failure surface, and no automatic replacement.

## PBSA v2.4 calibration report

Added:
- calibration_report.py

The report emits recommended thresholds, calibration score, safe-fail preservation, crash-rate preservation, overfitting guard status, and no automatic replacement.

## PBSA v2.5 evidence package report

Added:
- evidence_package_report.py

The report emits artifact hashes, report-chain status, ledger-continuity status, RCC anchor verification, downgrade-lock verification, and failure-surface status.

## PBSA v2.6 replay audit report

Added:
- replay_audit_report.py

The report emits decision replay status, semantic drift, expected timestamp drift, ledger replay status, RCC replay status, downgrade-lock replay, and no automatic replacement.

## PBSA v2.7 release candidate report

Added:
- release_candidate_report.py

The report emits release readiness, evidence index, claim-boundary table, failure-surface index, command surface, downgrade locks, and no automatic replacement.

## PBSA v3.0 public package report

Added:
- public_package_report.py

The report emits publication abstract, evidence summary, public limitations, command surface, claim-boundary table, release checklist, release tag metadata, and no automatic replacement.
