PBSA MODULE CONTRACTS

domain.py:
Loads and validates domain configs.

parameters.py:
Loads and validates PBA parameter manifests.

kernel.py:
Runs the PBA update loop with delta_phi, omega, signal preservation, cusp guarding, allostatic anticipation, and perturbations.

baselines:
Runs proportional, PI, threshold, and return-to-setpoint baselines under shared conditions.

calibration:
Performs grid search on fit split and emits trial records.

evaluation:
Computes metrics, compares PBA to baselines, checks identifiability, and assigns PBA-A/B/C/D/E classification.

evidence:
Writes ledgers, evidence_package.json, file_manifest.json, and benchmark_summary.md.

benchmarks:
Runs single-domain and suite benchmarks.

cli:
Exposes local command surface.