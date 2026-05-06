# configs/evidence

## Purpose

Evidence package hardening declarations for PBSA v2.5.

## S - Formal specification

Evidence package hardening verifies configs, reports, ledgers, hashes, README/RCC anchors, downgrade locks, and failure surfaces.

## H - Hooks

Used by src/pba/evidence_hardening.

## A - Artifacts

- evidence_package_policy_v2_5.json
- evidence_artifact_manifest_v2_5.json

## T - Theory

Auditability requires config-to-runtime-to-report-to-ledger-to-README traceability.

## I - Invariants

- Evidence packaging is not biological validation.
- Auditability is not mechanism proof.
- No automatic kernel replacement.
- No kernel mutation.
- Failure surfaces remain visible.

## E - Example

python -m pba.cli evidence-package-report
