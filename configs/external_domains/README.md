# configs/external_domains

## Purpose

External toy-domain family declarations for PBSA v2.2.

## S - Formal specification

External domains are declared toy-domain families not used to shape the v2.0 route selector or v2.1 validation metrics.

## H - Hooks

Used by src/pba/external.

## A - Artifacts

- delayed_recovery_external.json
- slow_drift_external.json
- sharp_shock_external.json
- mixed_regime_external.json
- ambiguous_low_confidence_external.json

## T - Theory

Internal validation is not enough. A routed policy must survive external unseen toy-domain families.

## I - Invariants

- External validation is not biological validation.
- External validation is not medical validation.
- External success is not universal proof.
- Automatic kernel replacement remains disabled.

## E - Example

python -m pba.cli external-validation-report
