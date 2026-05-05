# src/pba/evolution

## Purpose

PBSA v1.2 diagnostic evolution scaffolding.

## S - Formal specification

This folder contains policy and champion/challenger scaffolding for future kernel evolution. PBSA v1.2 is diagnostic-first and must not silently replace the current PBA kernel.

## H - Hooks

- Reads suite summaries from reports/suite_summaries.
- Uses multi-label regime detection from src/pba/evaluation.
- Uses evolution reports from src/pba/evidence.
- Uses configs/evolution_policy.json.

## A - Artifacts

- evolution_policy.py
- kernel_candidate.py
- champion_challenger.py

## T - Theory

Placidity is regime-conditioned. Baseline wins are diagnostic evidence, not embarrassment. PBSA v1.2 preserves primary regime plus secondary overlays.

## I - Invariants

- Current kernel remains champion.
- No kernel replacement without tests, suite evidence, baseline comparison, evolution report, and non-claim locks.
- Multi-label diagnosis must not mutate the PBA kernel.
- No medical, clinical, mechanism, or biological-law claim.

## E - Example

python -m pba.cli diagnose-evolution

## PBSA v1.3 candidate readiness

Added:
- candidate_spec.py
- candidate_readiness.py

Candidate specs are plans, not executable controllers. Candidate execution remains disabled in v1.3.

## PBSA v1.4 champion/challenger governance

Added:
- candidate_variants.py
- champion_challenger_runner.py
- promotion_governance.py

Candidate execution is not promotion. Candidate routes run only inside comparison reports.
