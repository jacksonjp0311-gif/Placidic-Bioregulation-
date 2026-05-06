# configs/release

## Purpose

Release-candidate audit bundle declarations for PBSA v2.7.

## S - Formal specification

Release-candidate packaging turns replay-verified evidence into public audit surfaces: clone/run commands, evidence index, claim-boundary table, failure-surface index, release checklist, downgrade locks, and limitations.

## H - Hooks

Used by src/pba/release.

## A - Artifacts

- release_candidate_policy_v2_7.json
- release_audit_manifest_v2_7.json

## T - Theory

Replay is not enough. A mature PBSA system must be packaged for outside audit.

## I - Invariants

- Release-candidate packaging is not biological validation.
- Public audit readiness is not medical safety.
- Release readiness must not hide limitations.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.

## E - Example

python -m pba.cli release-candidate-report
