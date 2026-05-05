from __future__ import annotations

from pathlib import Path
import hashlib
import json


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_file_manifest(root: str | Path) -> list[dict]:
    root = Path(root)
    records = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            if any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
                continue
            records.append({
                "path": str(path.relative_to(root)),
                "size_bytes": path.stat().st_size,
                "sha256": sha256_file(path)
            })
    return records


def write_file_manifest(root: str | Path, output: str | Path) -> None:
    manifest = build_file_manifest(root)
    Path(output).write_text(json.dumps(manifest, indent=2), encoding="utf-8")