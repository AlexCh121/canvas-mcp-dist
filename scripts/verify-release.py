#!/usr/bin/env python3
"""Verify versioned release assets without changing the current installer pointer."""

import json
import os
import re
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
release = json.loads((ROOT / "release.json").read_text())
version = release["version"]
if re.fullmatch(r"\d+\.\d+\.\d+", version) is None:
    raise ValueError("invalid release version")
expected = runpy.run_path(str(ROOT / "scripts/update-latest.py"))["build_manifest"](
    release["archive"]
)
if expected["version"] != version or expected["checksumFile"] != release["checksumFile"]:
    raise ValueError("release metadata does not match package")
if release["notesFile"] != f"releases/{version}/RELEASE-NOTES.md":
    raise ValueError("invalid release notes path")
if not isinstance(release["prerelease"], bool):
    raise ValueError("prerelease must be a boolean")
documentation_only = release.get("documentationOnly", False)
if not isinstance(documentation_only, bool):
    raise ValueError("documentationOnly must be a boolean")
if not release["prerelease"]:
    latest = json.loads((ROOT / "latest.json").read_text())
    if latest != expected:
        raise ValueError("regular release must match latest.json")
for name in ["README.en.md", "INSTALL.zh-CN.md", "RELEASE-NOTES.md", "SHA256SUMS"]:
    if not (ROOT / "releases" / version / name).is_file():
        raise ValueError(f"missing versioned asset: {name}")
if (ROOT / "releases" / version / "SHA256SUMS").read_bytes() != (
    ROOT / release["checksumFile"]
).read_bytes():
    raise ValueError("release checksum copies differ")
if os.environ.get("GITHUB_OUTPUT"):
    with open(os.environ["GITHUB_OUTPUT"], "a") as output:
        for key in ["version", "archive", "checksumFile", "notesFile"]:
            output.write(f"{key}={release[key]}\n")
        output.write(f"prerelease={json.dumps(release['prerelease'])}\n")
        output.write(f"documentationOnly={json.dumps(documentation_only)}\n")
print(f"Release assets verified: {version}; prerelease={release['prerelease']}")
