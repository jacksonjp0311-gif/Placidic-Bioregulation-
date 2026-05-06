# PBSA v2.4 Implementation Map

## Purpose

Map PBSA v2.4 calibration and threshold tuning architecture to repository implementation.

## Implemented objects

| Architecture object | Repository implementation |
|---|---|
| Calibration policy | configs/calibration/calibration_policy_v2_4.json |
| Threshold grid | configs/calibration/threshold_grid_v2_4.json |
| Threshold candidates | src/pba/calibration_thresholds/threshold_candidate.py |
| Calibration metrics | src/pba/calibration_thresholds/calibration_metrics.py |
| Overfitting guard | src/pba/calibration_thresholds/overfitting_guard.py |
| Safe-fail preservation | src/pba/calibration_thresholds/safe_fail_preservation.py |
| Calibration runner | src/pba/calibration_thresholds/calibration_runner.py |
| Calibration report | src/pba/evidence/calibration_report.py |
| CLI command | python -m pba.cli calibration-report |
| Reports | reports/calibration/ |

## Current lock

Automatic kernel replacement remains disabled.
