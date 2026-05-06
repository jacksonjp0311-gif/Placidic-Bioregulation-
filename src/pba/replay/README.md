# src/pba/replay

## Purpose

PBSA v2.6 reproducibility replay implementation.

## S - Formal specification

This layer regenerates the PBSA report chain and compares replayed decisions, hash drift, ledger continuity, RCC anchors, downgrade locks, and failure-surface replay status.

## H - Hooks

Consumes PBSA v2.0-v2.5 configs, reports, ledgers, README/RCC surfaces, and evidence package outputs.

## A - Artifacts

- replay_runner.py
- decision_replay.py
- hash_drift.py
- replay_lock_verifier.py
- replay_audit.py

## T - Theory

An evidence package is not release-candidate ready until replay can reproduce decisions or emit explicit drift.

## I - Invariants

- Reproducibility replay is not biological validation.
- Replay success is not medical safety.
- Decision drift must remain visible.
- Hash drift must remain visible.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli replay-audit-report
