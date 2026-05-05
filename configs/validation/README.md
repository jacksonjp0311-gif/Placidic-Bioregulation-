# configs/validation

## Purpose

Validation policy declarations for PBSA v2.1.

## S - Formal specification

Routed validation compares routed PBSA against champion-only, baseline-only, candidate-only, and reject/manual-review controls.

## H - Hooks

Used by src/pba/validation.

## A - Artifacts

- routed_validation_policy_v2_1.json

## T - Theory

Route selection must be validated against non-routed controls.

## I - Invariants

- No automatic kernel replacement.
- No biological validation claim.
- Non-claim locks remain preserved.

## E - Example

python -m pba.cli routed-validation-report
