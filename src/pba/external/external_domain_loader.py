from __future__ import annotations

import json
from pathlib import Path


REQUIRED_EXTERNAL_DOMAIN_FIELDS = {
    "domain_id",
    "family",
    "primary_regime",
    "secondary_regimes",
    "external",
}


def load_external_domain(path: str | Path) -> dict:
    path = Path(path)
    obj = json.loads(path.read_text(encoding="utf-8"))
    missing = REQUIRED_EXTERNAL_DOMAIN_FIELDS - set(obj)
    if missing:
        raise ValueError(f"External domain config missing fields: {sorted(missing)}")
    if not obj.get("external"):
        raise ValueError(f"External domain config must set external=true: {path}")
    return obj


def load_external_suite(root: str | Path, suite_path: str | Path | None = None) -> list[dict]:
    root = Path(root)
    if suite_path is None:
        suite_path = root / "configs" / "external_validation_suite_v2_2.json"
    else:
        suite_path = Path(suite_path)

    suite = json.loads(suite_path.read_text(encoding="utf-8"))
    domains = []
    for rel in suite.get("external_domain_configs", []):
        domains.append(load_external_domain(root / rel))
    return domains
