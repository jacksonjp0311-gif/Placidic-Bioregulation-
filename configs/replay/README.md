# configs/replay

## Purpose

Reproducibility replay declarations for PBSA v2.6.

## S - Formal specification

Replay verifies whether source configs can regenerate the PBSA report chain and reproduce decisions, locks, failure surfaces, ledgers, hashes, and RCC anchors.

## H - Hooks

Used by src/pba/replay.

## A - Artifacts

- replay_policy_v2_6.json
- replay_artifact_manifest_v2_6.json

## T - Theory

Evidence packaging is not enough. A mature PBSA system must replay its evidence package.

## I - Invariants

- Reproducibility replay is not biological validation.
- Replay success is not medical safety.
- Replay drift must remain visible.
- Automatic kernel replacement remains disabled.
- Kernel mutation remains disabled.

## E - Example

python -m pba.cli replay-audit-report
