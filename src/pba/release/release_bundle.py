from __future__ import annotations

from pathlib import Path

from pba.release.claim_boundary_table import build_claim_boundary_table
from pba.release.command_surface import build_command_surface
from pba.release.evidence_index import build_evidence_index
from pba.release.failure_surface_index import build_failure_surface_index
from pba.release.release_readiness import verify_release_readiness


def build_release_bundle(root: str | Path) -> dict:
    root = Path(root)
    return {
        "version": "PBSA-v2.7",
        "package_version": "1.7.0",
        "release_policy": "release_candidate_policy_v2_7",
        "source_replay_report": "reports/replay/latest_replay_audit_report.json",
        "source_evidence_package": "reports/evidence_packages/latest_evidence_package_report.json",
        "evidence_index": build_evidence_index(root),
        "claim_boundary_table": build_claim_boundary_table(),
        "failure_surface_index": build_failure_surface_index(root),
        "command_surface": build_command_surface(),
        "release_readiness": verify_release_readiness(root),
        "automatic_kernel_replacement_allowed": False,
        "kernel_mutation_allowed": False,
        "non_claim_boundary": "release-candidate audit readiness only; not biological validation, medical safety, or mechanism proof",
    }
