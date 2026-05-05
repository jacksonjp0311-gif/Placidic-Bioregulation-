# src/pba/external

## Purpose

PBSA v2.2 external-domain validation implementation.

## S - Formal specification

The external layer loads unseen toy-domain families, runs the routed policy against them, compares internal vs external behavior, detects route drift, and emits external validation reports.

## H - Hooks

Consumes configs/external_domains, configs/external_validation_suite_v2_2.json, PBSA v2.1 routed validation reports, and PBSA v2.0 routing.

## A - Artifacts

- external_domain_loader.py
- external_validation_runner.py
- route_drift.py
- external_failure_surface.py

## T - Theory

Internal routed validation is not enough. External toy-domain families test generalization pressure.

## I - Invariants

- External validation is not biological validation.
- External advantage is not medical evidence.
- Route drift must remain visible.
- External failure must remain visible.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli external-validation-report
