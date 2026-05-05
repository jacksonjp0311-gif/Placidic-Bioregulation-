# src/pba/baselines

## Purpose

Comparator models for shared-condition benchmark fairness.

## S - Formal specification

Each baseline exposes a run method using the same domain and perturbation sequence as PBA.

## H - Hooks

Used by benchmark runner and metrics comparison.

## A - Artifacts

- base.py
- proportional.py
- pi_control.py
- threshold.py
- return_to_setpoint.py

## T - Theory

PBSA cannot claim benchmark advantage without simpler baseline comparison.

## I - Invariants

- Baselines must run under shared conditions.
- Baselines must emit trajectories and metrics.
- Baseline-superior results must trigger downgrade.

## E - Example

Proportional feedback is currently the strongest baseline in the latest suite summary.