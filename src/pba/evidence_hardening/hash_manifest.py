from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha256_file(path: str | Path) -> str:
    path = Path(path)
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_artifact_manifest(root: str | Path) -> dict:
    root = Path(root)
    path = root / "configs" / "evidence" / "evidence_artifact_manifest_v2_5.json"
    return json.loads(path.read_text(encoding="utf-8"))


def build_hash_manifest(root: str | Path) -> list[dict]:
    root = Path(root)
    manifest = load_artifact_manifest(root)
    rows = []

    for item in manifest.get("required_artifacts", []):
        rel = item["path"]
        path = root / rel
        exists = path.exists()
        required = bool(item.get("required", True))
        rows.append({
            "path": rel,
            "role": item.get("role", "unknown"),
            "required": required,
            "exists": exists,
            "sha256": sha256_file(path) if exists else None,
            "status": "present" if exists else ("missing_required" if required else "missing_optional"),
        })

    return rows


def hash_manifest_valid(rows: list[dict]) -> bool:
    return all(row["exists"] or not row["required"] for row in rows)
