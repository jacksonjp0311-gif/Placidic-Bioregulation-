from __future__ import annotations


RELEASE_COMMANDS = [
    "python -m unittest discover -s tests",
    "python -m unittest tests.test_rcc_readmes -v",
    "python -m pba.cli routed-suite-report",
    "python -m pba.cli routed-validation-report",
    "python -m pba.cli external-validation-report",
    "python -m pba.cli stress-validation-report",
    "python -m pba.cli calibration-report",
    "python -m pba.cli evidence-package-report",
    "python -m pba.cli replay-audit-report",
    "python -m pba.cli release-candidate-report",
]


def build_command_surface() -> dict:
    return {
        "commands": RELEASE_COMMANDS,
        "clone_hint": "git clone https://github.com/jacksonjp0311-gif/Placidic-Bioregulation-.git",
        "working_directory_hint": "Set-Location \"C:\\Users\\jacks\\OneDrive\\Desktop\\Placidic Bioregulation\"",
        "non_claim_boundary": "Commands are computational audit commands, not biological or medical validation commands.",
    }


def command_surface_valid(surface: dict) -> bool:
    commands = surface.get("commands", [])
    required = {
        "python -m unittest discover -s tests",
        "python -m pba.cli replay-audit-report",
        "python -m pba.cli release-candidate-report",
    }
    return required.issubset(set(commands))
