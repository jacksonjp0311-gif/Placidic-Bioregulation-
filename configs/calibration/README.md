# configs/calibration

## Purpose

Calibration and threshold tuning declarations for PBSA v2.4.

## S - Formal specification

Calibration tests threshold candidates across routed, external, and stress evidence while preserving safe-fail behavior, crash-rate visibility, overfitting guards, and non-claim locks.

## H - Hooks

Used by src/pba/calibration_thresholds.

## A - Artifacts

- calibration_policy_v2_4.json
- threshold_grid_v2_4.json

## T - Theory

Threshold tuning must not hide failures or weaken safe-fail behavior.

## I - Invariants

- Calibration is not biological validation.
- Threshold tuning is not medical safety.
- No automatic kernel replacement.
- No kernel mutation.
- Safe-fail behavior must remain preserved.

## E - Example

python -m pba.cli calibration-report
