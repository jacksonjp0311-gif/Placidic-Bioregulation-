# configs

## Purpose

Declared benchmark surface for PBSA.

## S - Formal specification

Configs define domains, parameters, baselines, calibration grid, suite membership, and metric manifest.

## H - Hooks

Used by:
- src/pba/core/domain.py
- src/pba/core/parameters.py
- src/pba/benchmarks/runner.py
- src/pba/benchmarks/suite_runner.py
- tests

## A - Artifacts

- suite_v1_0.json
- pba_params.json
- baseline_params.json
- calibration_grid.json
- metric_manifest.json
- domains/*.json

## T - Theory

Config-first execution prevents hidden calibration and post-hoc benchmark claims.

## I - Invariants

- Parameters must be declared before run.
- Baselines must share task conditions.
- Domains must preserve non-claim locks.
- Fit and evaluation seeds must remain visible.

## E - Example

Run suite from repo root:
python -m pba.cli run-suite --config .\configs\suite_v1_0.json

## PBSA v1.1 evolution configs

- evolution_policy.json declares diagnostic-first rules.
- suite_holdout_v1_0.json is a holdout/repeat-suite placeholder until new domains are added.
- Kernel mutation is disabled by default.

## PBSA v1.2 policy drift cleanup

- evolution_policy.json now declares PBSA-EvolutionPolicy-v1.2.
- suite_holdout_v1_0.json now references PBSA v1.2 diagnostic schema.
- Kernel mutation remains disabled by default.

## PBSA v1.3 holdout configs

Added:
- configs/domains/holdout_direct_recovery.json
- configs/domains/holdout_delayed_pulse.json
- configs/domains/holdout_noisy_recovery.json
- configs/domains/holdout_mixed_oscillation.json
- configs/suite_holdout_v1_3.json

These are computational toy holdout domains only. They are not biological systems.
