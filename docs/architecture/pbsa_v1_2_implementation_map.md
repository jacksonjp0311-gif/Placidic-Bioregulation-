# PBSA v1.2 Implementation Map

## Purpose

Map PBSA v1.2 architecture to repository implementation.

## Implemented changes

- PBSA_VERSION updated to PBSA-v1.2
- package version updated to 0.3.0
- regime_detector.py now emits multi-label output
- evolution_report.py now writes PBSA-v1.2 reports
- evolution reports include domain_regimes
- tests updated for multi-label detection
- README and mini README surfaces updated under RCC

## Architecture-to-code map

| Architecture object | Repository implementation |
|---|---|
| Multi-label regime detector | src/pba/evaluation/regime_detector.py |
| Primary regime | primary_regime field |
| Backward-compatible regime | detected_regime field |
| Secondary overlays | secondary_regimes field |
| Risk overlays | risk_overlays field |
| Regime scores | regime_scores field |
| Evidence notes | evidence_notes field |
| Evolution report v1.2 | src/pba/evidence/evolution_report.py |
| Latest generated report | reports/evolution/latest_evolution_report.json |
| RCC README contract | tests/test_rcc_readmes.py |

## Current expected regime interpretation

| Domain | Primary regime | Secondary overlays |
|---|---|---|
| temperature_like | direct_recovery | cusp_risk, baseline_advantage |
| pulse_recovery | pulse_recovery | cusp_risk, baseline_advantage |
| oscillatory_signal | oscillatory | cusp_risk, pba_advantage |

## Current decision

preserve_champion

## Kernel mutation

Disabled. PBSA v1.2 improves diagnostics only.
