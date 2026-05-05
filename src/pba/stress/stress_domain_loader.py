from __future__ import annotations

import json
from pathlib import Path


def load_stress_domain(path: str | Path) -> dict:
    path = Path(path)
    obj = json.loads(path.read_text(encoding="utf-8"))
    obj["_source_path"] = str(path)
    return obj


def load_stress_suite(root: str | Path, suite_path: str | Path | None = None) -> list[dict]:
    root = Path(root)
    if suite_path is None:
        suite_path = root / "configs" / "stress_validation_suite_v2_3.json"
    else:
        suite_path = Path(suite_path)

    suite = json.loads(suite_path.read_text(encoding="utf-8"))
    domains = []
    for rel in suite.get("stress_domain_configs", []):
        domains.append(load_stress_domain(root / rel))
    return domains
