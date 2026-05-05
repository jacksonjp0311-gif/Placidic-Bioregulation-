# src/pba/evolution

## Purpose

PBSA v1.1 diagnostic evolution scaffolding.

## S - Formal specification

This folder contains policy and champion/challenger scaffolding for future kernel evolution. PBSA v1.1 is diagnostic-first and must not silently replace the current PBA kernel.

## H - Hooks

- Reads suite summaries from reports/suite_summaries.
- Uses regime detection from src/pba/evaluation.
- Uses evolution reports from src/pba/evidence.
- Uses configs/evolution_policy.json.

## A - Artifacts

- evolution_policy.py
- kernel_candidate.py
- champion_challenger.py

## T - Theory

Placidity is regime-conditioned. Baseline wins are diagnostic evidence, not embarrassment.

## I - Invariants

- Current kernel remains champion.
- No kernel replacement without tests, suite evidence, baseline comparison, evolution report, and non-claim locks.
- No medical, clinical, mechanism, or biological-law claim.

## E - Example

python -m pba.cli diagnose-evolution
