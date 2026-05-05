# src

## Purpose

Python source root.

## S — Formal specification

Contains the importable pba package.

## H — Hooks

Used by tests, scripts, CLI, and pyproject package discovery.

## A — Artifacts

- pba package

## T — Theory

Source code is implementation evidence, not empirical validation.

## I — Invariants

- Keep package importable.
- Keep PYTHONPATH-compatible local execution.
- Do not place generated benchmark outputs here.

## E — Example

Set local path:
$env:PYTHONPATH = ".\src"