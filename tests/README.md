# tests

## Purpose

Implementation and documentation-contract health checks.

## S - Formal specification

Tests verify domain loading, parameters, kernel execution, baselines, metrics, classification, CLI, and suite summary behavior.

## H - Hooks

Tests import src/pba and use configs.

## A - Artifacts

- test_domain_config.py
- test_parameters.py
- test_kernel.py
- test_baselines.py
- test_metrics.py
- test_classification.py
- test_cli.py
- test_suite_summary.py
- test_rcc_readmes.py

## T - Theory

A repository should not make strong claims if its tests fail.

## I - Invariants

- Tests must pass before push.
- Tests must pass before README claims are updated.
- README presence is part of RCC continuity.

## E - Example

python -m unittest discover -s tests