# src/pba

## Purpose

Executable PBSA/PBA package.

## S — Formal specification

Implements core runtime, baselines, calibration, evaluation, evidence, benchmarks, and CLI.

## H — Hooks

- configs feed runtime
- tests validate package
- runs/reports/ledgers receive outputs
- scripts call CLI

## A — Artifacts

- core
- baselines
- calibration
- evaluation
- evidence
- benchmarks
- cli

## T — Theory

PBA becomes software-real only when these modules produce auditable outputs.

## I — Invariants

- Preserve non-claim locks.
- Preserve baseline comparison.
- Preserve fit/evaluation separation.
- Preserve evidence outputs.

## E — Example

python -m pba.cli run-suite --config .\configs\suite_v1_0.json