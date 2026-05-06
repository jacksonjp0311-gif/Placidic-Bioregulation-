# src/pba/calibration_thresholds

## Purpose

PBSA v2.4 calibration and threshold tuning implementation.

## S - Formal specification

This layer builds threshold candidates, scores calibration candidates, checks safe-fail preservation, checks crash-rate preservation, applies overfitting guards, and emits calibration reports.

## H - Hooks

Consumes PBSA v2.1 routed validation, PBSA v2.2 external validation, and PBSA v2.3 stress validation reports.

## A - Artifacts

- threshold_candidate.py
- calibration_metrics.py
- overfitting_guard.py
- safe_fail_preservation.py
- calibration_runner.py

## T - Theory

Threshold tuning is only admissible after internal, external, and stress evidence exists.

## I - Invariants

- Calibration is not biological validation.
- Threshold tuning is not medical safety.
- Failure visibility must remain preserved.
- Safe-fail behavior must remain preserved.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli calibration-report
