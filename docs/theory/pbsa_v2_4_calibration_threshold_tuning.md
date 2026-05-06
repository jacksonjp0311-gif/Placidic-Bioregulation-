# Codex Delta Phi - PBSA v2.4 Calibration and Threshold Tuning

## Status

Canonical PBSA v2.4 calibration and threshold tuning layer.

## Purpose

PBSA v2.4 tunes route thresholds and confidence gates using internal, external, and stress evidence while preserving safe-fail behavior, failure visibility, non-claim locks, and RCC anchors.

## Core invariant

Threshold tuning must not hide failures or weaken safe-fail behavior.

## Added surfaces

- calibration policy config
- threshold grid config
- threshold candidate schema
- calibration metrics
- safe-fail preservation check
- overfitting guard
- calibration runner
- calibration report

## Lock

Calibration is not biological validation. Threshold tuning is not medical safety. Calibration is not automatic kernel replacement.
