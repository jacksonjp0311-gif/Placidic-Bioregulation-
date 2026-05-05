# src/pba/stress

## Purpose

PBSA v2.3 stress/adversarial validation implementation.

## S - Formal specification

The stress layer loads adversarial toy domains, guards malformed inputs, detects contradictory regimes, forces unsafe cases into safe-fail routing, and emits stress validation reports.

## H - Hooks

Consumes configs/stress_domains, configs/stress_validation_suite_v2_3.json, PBSA v2.2 external validation reports, and PBSA v2.0 routing.

## A - Artifacts

- stress_domain_loader.py
- malformed_input_guard.py
- contradiction_detector.py
- stress_validation_runner.py
- stress_route_drift.py
- stress_failure_surface.py

## T - Theory

A routed policy must fail safely under adversarial pressure before threshold tuning or broader expansion.

## I - Invariants

- Stress validation is not biological validation.
- Adversarial robustness is not medical safety.
- Malformed inputs must not crash the report path.
- Unsafe stress domains route to reject/manual review.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli stress-validation-report
