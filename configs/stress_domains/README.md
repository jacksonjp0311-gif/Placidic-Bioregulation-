# configs/stress_domains

## Purpose

Stress/adversarial toy-domain declarations for PBSA v2.3.

## S - Formal specification

Stress domains pressure route selection with noisy, contradictory, malformed, boundary-case, ambiguous, and overlay-overload inputs.

## H - Hooks

Used by src/pba/stress.

## A - Artifacts

- noise_pressure_stress.json
- contradictory_regime_stress.json
- malformed_input_stress.json
- boundary_case_stress.json
- ambiguous_overlay_stress.json
- overlay_overload_stress.json

## T - Theory

External validation is not enough. A routed policy must fail safely under adversarial pressure.

## I - Invariants

- Stress validation is not biological validation.
- Stress robustness is not medical safety.
- Malformed inputs must not crash the report path.
- Unsafe stress domains must route to reject/manual review.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli stress-validation-report
