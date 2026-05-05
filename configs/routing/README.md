# configs/routing

## Purpose

Routing policy declarations for PBSA v2.0.

## S - Formal specification

Routes are selected by primary regime, secondary overlays, evidence gates, and non-claim locks.

## H - Hooks

Used by src/pba/routing.

## A - Artifacts

- regime_route_policy_v2_0.json

## T - Theory

PBSA v2.0 routes by regime instead of forcing one universal kernel.

## I - Invariants

- No automatic kernel replacement.
- No biological validation claim.
- Non-claim locks remain preserved.

## E - Example

python -m pba.cli routed-suite-report
