# configs

## Purpose

Declared benchmark surface for PBSA.

## S — Formal specification

Configs define domains, parameters, baselines, calibration grid, suite membership, and metric manifest.

## H — Hooks

Used by:
- src/pba/core/domain.py
- src/pba/core/parameters.py
- src/pba/benchmarks/runner.py
- src/pba/benchmarks/suite_runner.py
- tests

## A — Artifacts

- suite_v1_0.json
- pba_params.json
- baseline_params.json
- calibration_grid.json
- metric_manifest.json
- domains/*.json

## T — Theory

Config-first execution prevents hidden calibration and post-hoc benchmark claims.

## I — Invariants

- Parameters must be declared before run.
- Baselines must share task conditions.
- Domains must preserve non-claim locks.
- Fit and evaluation seeds must remain visible.

## E — Example

Run suite from repo root:
python -m pba.cli run-suite --config .\configs\suite_v1_0.json