from __future__ import annotations


PUBLIC_LIMITATIONS = [
    "PBSA is a computational software research artifact only.",
    "PBSA does not provide medical guidance.",
    "PBSA does not constitute biological validation.",
    "PBSA does not prove a physiological mechanism.",
    "PBSA does not provide clinical safety evidence.",
    "PBSA does not prove universal bioregulation.",
    "PBSA benchmark domains are computational toy or proxy domains unless otherwise stated.",
    "PBSA reports may contain timestamp/hash drift for regenerated artifacts.",
    "PBSA keeps manual review and conservative downgrade outcomes valid.",
    "PBSA does not permit automatic kernel replacement.",
]


def build_public_limitations() -> list[str]:
    return list(PUBLIC_LIMITATIONS)


def public_limitations_valid(limitations: list[str]) -> bool:
    lowered = " ".join(limitations).lower()
    required = [
        "does not provide medical guidance",
        "does not constitute biological validation",
        "does not prove a physiological mechanism",
        "does not permit automatic kernel replacement",
    ]
    return all(item in lowered for item in required)
