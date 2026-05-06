# src/pba/release

## Purpose

PBSA v2.7 release candidate audit bundle implementation.

## S - Formal specification

This layer packages replay-verified evidence into outside-auditable release surfaces: evidence index, claim-boundary table, failure-surface index, command surface, readiness checks, and release candidate reports.

## H - Hooks

Consumes PBSA v2.0-v2.6 configs, reports, replay audit, evidence package, README/RCC surfaces, docs, and mini READMEs.

## A - Artifacts

- evidence_index.py
- claim_boundary_table.py
- failure_surface_index.py
- command_surface.py
- release_readiness.py
- release_bundle.py

## T - Theory

Replay is not enough. A mature PBSA system must be packaged for outside audit.

## I - Invariants

- Release-candidate packaging is not biological validation.
- Public audit readiness is not medical safety.
- Failure surfaces must remain visible.
- Downgrade locks must remain preserved.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli release-candidate-report
