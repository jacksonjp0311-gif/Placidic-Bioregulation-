# PBSA v2.5 Implementation Map

## Purpose

Map PBSA v2.5 evidence package hardening architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Evidence package policy | configs/evidence/evidence_package_policy_v2_5.json |
| Evidence artifact manifest | configs/evidence/evidence_artifact_manifest_v2_5.json |
| Hash manifest | src/pba/evidence_hardening/hash_manifest.py |
| Report-chain verifier | src/pba/evidence_hardening/report_chain.py |
| Ledger-continuity verifier | src/pba/evidence_hardening/ledger_continuity.py |
| RCC anchor verifier | src/pba/evidence_hardening/rcc_anchor_verifier.py |
| Downgrade-lock verifier | src/pba/evidence_hardening/downgrade_lock_verifier.py |
| Failure-surface verifier | src/pba/evidence_hardening/failure_surface_verifier.py |
| Evidence package compiler | src/pba/evidence_hardening/evidence_package.py |
| Evidence package report | src/pba/evidence/evidence_package_report.py |
| CLI command | python -m pba.cli evidence-package-report |
| Reports | reports/evidence_packages/ |

## Current lock

Automatic kernel replacement remains disabled.
