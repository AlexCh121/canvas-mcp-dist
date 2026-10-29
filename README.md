# Infinite Canvas MCP

[简体中文](README.zh-CN.md)

This repository distributes the local Bridge and stdio MCP package for authorized Infinite Canvas users. The default installation version, archive, and checksum file are listed in [latest.json](latest.json).

Requires Node.js 22 or newer, a local Codex CLI, and access to the authorized Canvas on the same computer as the Bridge.

## Choose a version

| Purpose | Version and downloads | Status |
|---|---|---|
| Default installation | [0.1.9](https://github.com/AlexCh121/canvas-mcp-dist/releases/tag/v0.1.9) · [installation guide](releases/0.1.9/README.en.md), selected by [latest.json](latest.json) | Stable release, current default |
| Previous version | [0.1.8](https://github.com/AlexCh121/canvas-mcp-dist/releases/tag/v0.1.8) | Retained for reference and compatibility checks |

The generic commands below install 0.1.9 by default. Intermittent disconnects remain under investigation. Supply the URL of your authorized, signed-in canvas; this repository does not list a Canvas deployment entry.

## One-sentence quickstart for an agent

First sign in to Canvas and copy the URL of the canvas you opened. Replace `PASTE_YOUR_CANVAS_URL_HERE` below with that URL, then send the entire message to a **local Codex or other agent running on the same computer as your browser**:

> Read https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.md and https://github.com/AlexCh121/canvas-mcp-dist/blob/main/latest.json. I have opened Infinite Canvas and signed in on this computer. My canvas URL is: `PASTE_YOUR_CANVAS_URL_HERE`. Read `latest.json` from the repository's `main` branch for the current version, `archive`, `checksumFile`, `sha256`, `cli`, and `codexRegistration`; check that Node.js meets `nodeMajorMinimum`. Download the named archive and checksum file from the same repository, verify both SHA256 values, and install the archive. Stop if the manifest or files disagree. Register the MCP with Codex using the manifest's registration name and CLI. Extract the exact Origin (scheme, host, and port, without the path) from my canvas URL and pass it as `QORIGIN_CANVAS_ORIGINS` to that CLI's `serve` process; keep the Bridge running. Do not use a wildcard or bypass the Origin check. Then guide me to enter the one-use pairing code in Canvas Assistant → Codex and explicitly select the browser connection. If you are not running on this computer or cannot keep the Bridge running, explain the limitation instead of claiming it is connected.

## Install

Download [latest.json](latest.json), then download the `archive` and `checksumFile` it names from this repository into the same directory. Run the following on the same computer as your signed-in canvas. The commands read the manifest, so they do not need a version edit for each release:

```bash
CANVAS_URL='PASTE_YOUR_CANVAS_URL_HERE'
CANVAS_ORIGIN="$(node -p 'new URL(process.argv[1]).origin' "$CANVAS_URL")"
CANVAS_ARCHIVE="$(node -p "require('./latest.json').archive")"
CANVAS_SUMS="$(node -p "require('./latest.json').checksumFile")"
CANVAS_CLI="$(node -p "require('./latest.json').cli")"
CANVAS_REG="$(node -p "require('./latest.json').codexRegistration")"
node -e "const m=require('./latest.json'); if (Number(process.versions.node.split('.')[0]) < m.nodeMajorMinimum) process.exit(1)"
shasum -a 256 -c "$CANVAS_SUMS"
node -e "const m=require('./latest.json'); const h=require('node:crypto').createHash('sha256').update(require('node:fs').readFileSync(m.archive)).digest('hex'); if (h !== m.sha256) process.exit(1)"
npm install -g "./$CANVAS_ARCHIVE"
codex mcp add "$CANVAS_REG" -- "$CANVAS_CLI" mcp
QORIGIN_CANVAS_ORIGINS="$CANVAS_ORIGIN" "$CANVAS_CLI" serve
```

Keep the Bridge terminal open. Enter its one-use pairing code in **Canvas Assistant → Codex**. In Codex, call `canvas_list_connections`, then explicitly select the shown connection with `canvas_select_connection`. Check for and remove an existing registration under the same name before upgrading to avoid duplicates.

For multiple authorized Canvas domains, pass their exact Origins as a comma-separated `QORIGIN_CANVAS_ORIGINS` value when starting the Bridge. Switching to an unconfigured domain requires restarting the Bridge and reconnecting. An explicitly empty value is rejected. The browser tab, Bridge, and Codex must run on the same computer. This package is not published to npm.

## Creative workflow and limitations

Page through `canvas_get_state` and read long text with `canvas_get_node_text` until `nextOffset` is null. Select an exact stored version with `canvas_list_media_versions`; view it with `canvas_get_image_preview` or `canvas_get_media_info`. Media URLs expire after five minutes. Use `canvas_get_generation_options`, configure an image or video node, quote with `canvas_quote_generation`, then pass the returned quote fingerprint, prompt, references and quoted amount unchanged to `canvas_generate_image` or `canvas_generate_video` after preparing an operation ID. Confirm the charge in Canvas. Query an uncertain operation with its original ID; media completion requires a separate `canvas_get_generation_status` check. Existing results can serve as references for a new node; a completed node can be generated again while keeping its older versions, and `canvas_select_media_version` can select an older stored version. Material review tools report supplier compliance, not creative quality.

Independent nodes can generate concurrently; local uploads accept up to 20 files per batch after explicit folder authorization. Free Canvas business actions run automatically, while paid items still require confirmation and client tool approvals remain under the client's control. The page reconnects automatically after refresh while pairing and permissions remain valid. Explicit disconnect revokes pairing. HEIC can be stored but currently fails preview and dimensions; use PNG/JPEG for visual reading. Video frame extraction and unattended execution are outside this version. Signed media URLs remain usable until expiry. See the versioned release notes for validation limits.

## Node names in 0.1.7

Read `displayName` and use `canvas_rename_node` for the visible name; `title` stays internal. Matching Web and Canvas Service support is required. Package publication does not deploy services. See the [0.1.7 release notes](releases/0.1.7/RELEASE-NOTES.md) for validation and limits.

## Connection fixes in 0.1.8

The package distinguishes transport, browser response and authorization, supports offline diagnosis using the original connection ID, and retains bounded redacted Bridge evidence across restarts. Canvas Web will be updated separately; preserving ambiguous rejected resume bindings requires that Web update. The original disconnect trigger remains under investigation. See the [0.1.8 release notes](releases/0.1.8/RELEASE-NOTES.md).

## 0.1.9 pairing reuse and upload prompts

The default package is now 0.1.9. Explicit cross-canvas pairing reuse requires matching Canvas Web; per-upload names and prompts require matching Canvas Service. Those services are deployed separately as part of the same evening release. See the [0.1.9 release notes](releases/0.1.9/RELEASE-NOTES.md).
