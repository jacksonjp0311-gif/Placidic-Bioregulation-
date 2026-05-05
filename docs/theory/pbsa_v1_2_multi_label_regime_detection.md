# Codex Delta Phi - PBSA v1.2 Multi-Label Regime Detection

## Status

Canonical PBSA v1.2 diagnostic architecture layer.

## Purpose

PBSA v1.2 upgrades the diagnostic instrument from single-label regime detection to multi-label regime detection.

## Core invariant

A regime detector must preserve both the domain shape and the risk overlay. Cusp risk may modify interpretation, but it must not erase the primary regime.

## Why this exists

PBSA v1.1 worked, but its first evolution report classified all current domains as cusp_risk. That preserved risk evidence but collapsed the declared domain geometry.

PBSA v1.2 corrects that by emitting:

- primary_regime
- secondary_regimes
- risk_overlays
- regime_scores
- evidence_notes

## Expected current interpretation

- temperature_like: primary direct_recovery, secondary cusp_risk and baseline_advantage
- pulse_recovery: primary pulse_recovery, secondary cusp_risk and baseline_advantage
- oscillatory_signal: primary oscillatory, secondary cusp_risk and pba_advantage

## Non-mutation lock

PBSA v1.2 does not replace the PBA kernel.

Current decision remains preserve_champion.

## RCC synchronization

When diagnostic semantics change, the root README, relevant mini READMEs, docs/theory, docs/architecture, and tests must be updated in the same version step.

## Non-claim boundary

Better diagnosis is not biological proof. Software clarity is not medical validation. Multi-label classification is not mechanism proof.
