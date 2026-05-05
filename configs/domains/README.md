# configs/domains

## Purpose

Benchmark domain declarations.

## S - Formal specification

Each domain JSON defines target, viable interval, time steps, initial state, perturbation family, noise model, fit/evaluation seeds, and non-claim locks.

## H - Hooks

Loaded by DomainConfig and benchmark runners.

## A - Artifacts

- temperature_like.json
- pulse_recovery.json
- oscillatory_signal.json

## T - Theory

Domains are toy computational evaluation surfaces, not biological systems.

## I - Invariants

- Must include not_medical.
- Must include not_biological_law.
- Must include not_mechanism_proof.
- Must define fit/evaluation split.

## E - Example

python -m pba.cli run-benchmark --domain .\configs\domains\temperature_like.json