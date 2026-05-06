from __future__ import annotations


def build_publication_abstract() -> str:
    return (
        "Placidic Bioregulation Software Architecture (PBSA) is a computational "
        "regime-routing and validation framework for evaluating evidence-feedback "
        "control policies across internal routed validation, external-domain "
        "validation, stress/adversarial validation, threshold calibration, evidence "
        "package hardening, reproducibility replay, and release-candidate audit "
        "surfaces. PBSA is a software research artifact only: it is not medical "
        "guidance, not biological validation, not clinical safety evidence, not "
        "treatment advice, and not proof of a physiological mechanism."
    )


def public_abstract_valid(text: str) -> bool:
    lowered = text.lower()
    required = [
        "computational",
        "software research artifact",
        "not medical guidance",
        "not medical",
        "not biological validation",
    ]
    return all(fragment in lowered for fragment in required)