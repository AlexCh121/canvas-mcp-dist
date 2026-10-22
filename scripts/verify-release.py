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
if release["prerelease"] is not True:
    raise ValueError("this publication workflow requires a prerelease")
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
print(f"Release assets verified: {version}; current latest.json unchanged")
