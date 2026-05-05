# scripts

## Purpose

Local automation helpers.

## S — Formal specification

Scripts run tests, benchmarks, suite summaries, and repo dumps.

## H — Hooks

Calls Python package through PYTHONPATH and CLI.

## A — Artifacts

- run_local.ps1
- repo_dump_light.ps1
- run_benchmark.py
- run_suite.py

## T — Theory

Scripts are local execution convenience, not source of truth.

## I — Invariants

- No GitHub push unless explicitly requested.
- Avoid fragile embedded code fences.
- Keep scripts copy-pasteable and PowerShell-safe.

## E — Example

powershell -ExecutionPolicy Bypass -File .\scripts\run_local.ps1