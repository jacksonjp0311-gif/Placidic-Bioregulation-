# src/pba/calibration

## Purpose

Parameter search and objective evaluation.

## S - Formal specification

Runs grid search over declared calibration grid and records all trials.

## H - Hooks

Uses core kernel and evaluation metrics.

## A - Artifacts

- objective.py
- grid_search.py

## T - Theory

Calibration is not truth. Calibration is a declared search over fit conditions.

## I - Invariants

- Search grid must be declared.
- Fit seed must be separate from evaluation seed.
- Trial losses must be preserved.
- Selected parameters must be recorded.

## E - Example

Calibration output appears in each run folder as calibration_record.json.