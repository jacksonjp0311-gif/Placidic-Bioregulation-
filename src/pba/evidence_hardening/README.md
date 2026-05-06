# src/pba/evidence_hardening

## Purpose

PBSA v2.5 evidence package hardening implementation.

## S - Formal specification

This layer verifies hash manifests, report chains, ledger continuity, README/RCC anchors, downgrade locks, failure surfaces, and evidence package traceability.

## H - Hooks

Consumes PBSA v2.0-v2.4 configs, reports, ledgers, README/RCC surfaces, docs, and mini READMEs.

## A - Artifacts

- hash_manifest.py
- report_chain.py
- ledger_continuity.py
- rcc_anchor_verifier.py
- downgrade_lock_verifier.py
- failure_surface_verifier.py
- evidence_package.py

## T - Theory

Auditability requires every claim to trace from config through report, ledger, hash, and README/RCC anchor.

## I - Invariants

- Evidence packaging is not biological validation.
- Auditability is not mechanism proof.
- Failure surfaces must remain visible.
- Downgrade locks must remain preserved.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli evidence-package-report
