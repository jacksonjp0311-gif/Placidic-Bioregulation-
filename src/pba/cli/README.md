# src/pba/cli

## Purpose

Command-line interface.

## S - Formal specification

Exposes run-benchmark, run-suite, and compile-evidence commands.

## H - Hooks

Used by scripts and human operators.

## A - Artifacts

- main.py
- __main__.py

## T - Theory

CLI reproducibility is required for benchmark credibility.

## I - Invariants

- Commands must be reproducible from repo root.
- CLI must print machine-readable JSON.
- CLI must not push to GitHub.

## E - Example

python -m pba.cli run-suite --config .\configs\suite_v1_0.json

## PBSA v1.3 CLI commands

Added:
- python -m pba.cli summarize-holdout
- python -m pba.cli candidate-readiness

## PBSA v1.4 CLI command

Added:
- python -m pba.cli champion-challenger-report

## PBSA v2.0 CLI command

Added:
- python -m pba.cli routed-suite-report

## PBSA v2.1 CLI command

Added:
- python -m pba.cli routed-validation-report
