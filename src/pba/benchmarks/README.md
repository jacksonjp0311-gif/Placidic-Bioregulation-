# src/pba/benchmarks

## Purpose

Benchmark orchestration.

## S — Formal specification

Runs single-domain and suite benchmarks from declared configs.

## H — Hooks

Loads configs, calls core PBA runtime, baselines, calibration, evaluation, evidence, and suite summary compiler.

## A — Artifacts

- runner.py
- suite_runner.py

## T — Theory

Benchmark runs are evidence-producing events, not proof events.

## I — Invariants

- Run IDs must be unique.
- Generated artifacts must go to runs and reports.
- Suite runs must compile summary evidence.
- No GitHub push from benchmark code.

## E — Example

python -m pba.cli run-suite --config .\configs\suite_v1_0.json