# src/pba/core

## Purpose

Core PBA runtime primitives.

## S — Formal specification

Defines domain loading, parameter manifests, state records, perturbations, cusp guard, signal preservation, allostasis, and kernel execution.

## H — Hooks

Used by baselines, calibration, benchmark runner, and tests.

## A — Artifacts

- domain.py
- parameters.py
- state.py
- perturbations.py
- cusp_guard.py
- signal.py
- allostasis.py
- kernel.py

## T — Theory

Core runtime implements Delta Phi deviation, Omega damping, cusp states, signal preservation, and anticipatory correction as computational abstractions.

## I — Invariants

- Delta Phi is computational deviation.
- Omega must remain bounded.
- Cusp state must be explicit.
- Signal preservation must not erase structure.
- No biological mechanism claim.

## E — Example

run_pba(domain, params, perturbations)