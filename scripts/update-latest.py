#!/usr/bin/env python3
"""Publish or verify the stable pointer to the latest installable MCP archive."""

import argparse
import hashlib
import json
import re
import tarfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "latest.json"


def build_manifest(archive_name: str) -> dict[str, object]:
    if Path(archive_name).name != archive_name or not archive_name.endswith(".tgz"):
        raise ValueError("archive must be a .tgz filename in the repository root")
    archive = ROOT / archive_name
    with tarfile.open(archive, "r:gz") as package:
        metadata = json.load(package.extractfile("package/package.json"))
    version = metadata["version"]
    bins = metadata["bin"]
    if not isinstance(bins, dict) or len(bins) != 1:
        raise ValueError("package must expose exactly one CLI command")
    cli = next(iter(bins))
    node = re.fullmatch(r">=(\d+)", metadata.get("engines", {}).get("node", ""))
    if node is None:
        raise ValueError("package must declare a minimum Node.js major version")

    checksum_file = f"SHA256SUMS-{version}"
    match = re.fullmatch(r"([0-9a-f]{64})  (\S+)\n?", (ROOT / checksum_file).read_text())
    if match is None or match.group(2) != archive_name:
        raise ValueError("version checksum file must contain exactly this archive")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    if digest != match.group(1):
        raise ValueError("archive does not match its version checksum file")
    if f"{digest}  {archive_name}" not in (ROOT / "SHA256SUMS").read_text().splitlines():
        raise ValueError("archive is missing from the aggregate SHA256SUMS")
    return {
        "schemaVersion": 1,
        "version": version,
        "archive": archive_name,
        "checksumFile": checksum_file,
        "sha256": digest,
        "cli": cli,
        "codexRegistration": "huihui-canvas",
        "nodeMajorMinimum": int(node.group(1)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", nargs="?", help="archive to make current")
    parser.add_argument("--check", action="store_true", help="verify latest.json and its assets")
    args = parser.parse_args()
    if not args.check and not args.archive:
        parser.error("provide an archive to publish")
    current = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else None
    archive_name = args.archive or (current or {}).get("archive")
    if not archive_name:
        parser.error("latest.json has no archive to check")
    expected = build_manifest(archive_name)
    if args.check:
        if current != expected:
            raise ValueError("latest.json does not match the archive and checksum file")
        print(f"latest.json verified: {expected['version']}")
    else:
        MANIFEST.write_text(json.dumps(expected, indent=2) + "\n")
        print(f"latest.json updated: {expected['version']}")


if __name__ == "__main__":
    main()
