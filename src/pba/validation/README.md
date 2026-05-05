# src/pba/validation

## Purpose

PBSA v2.1 routed-suite validation implementation.

## S - Formal specification

The validation layer compares routed policy behavior against non-routed controls and emits route advantage, preservation, and failure metrics.

## H - Hooks

Consumes PBSA v2.0 routed suite reports and produces routed validation reports.

## A - Artifacts

- control_policies.py
- routed_validation_runner.py
- route_metrics.py
- failure_surface.py

## T - Theory

A route selector is not validated until compared against non-routed controls.

## I - Invariants

- Routed validation is not biological validation.
- Routed advantage is not medical evidence.
- Validation is not automatic kernel replacement.
- Failure surfaces remain visible.

## E - Example

python -m pba.cli routed-validation-report
