# QOrigin Canvas MCP 0.1.2 · internal DEV preview

[简体中文](README.zh-CN.md)

This repository distributes the local Canvas Bridge and stdio MCP package for authorized DEV testing. It does not contain the Canvas application source code.

Version: `@qorigin/canvas-mcp@0.1.2`
Source: `tano-canvas` branch `codex/customer-mcp` at `25ae6242` (package files last changed at `0d43eb04`); backend changes at `5cd48559`.
Status: Internal DEV preview. Not approved for customer release.

Requires Node.js 22 or newer, a local Codex CLI, and access to the DEV Canvas on the same computer as the Bridge.

## One-sentence quickstart for an agent

Paste this into a **local Codex agent running on the same computer as your DEV Canvas browser**:

> Read https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.md, check that Node.js 22+ is available, download and verify the `0.1.2` tarball against `SHA256SUMS`, install it, register `qorigin-canvas-dev` with `codex mcp add qorigin-canvas-dev -- qorigin-canvas-mcp mcp`, start and keep `qorigin-canvas-mcp serve` running, then guide me to enter the one-use pairing code in Canvas and explicitly select the browser connection; if you are not running on this computer or cannot keep the Bridge running, stop and tell me instead of claiming it is connected.

## Install

Download `qorigin-canvas-mcp-0.1.2.tgz` and `SHA256SUMS` from this repository, then run:

```bash
shasum -a 256 -c SHA256SUMS
npm install -g ./qorigin-canvas-mcp-0.1.2.tgz
codex mcp add qorigin-canvas-dev -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

Keep the Bridge terminal open. In the logged-in DEV Canvas, open **Canvas Assistant → Codex** and enter the one-use pairing code printed by the Bridge. In Codex, call `canvas_list_connections` and explicitly select the shown connection with `canvas_select_connection` before using tools.

The browser tab, Bridge, and Codex must run on the same computer. This package is not published to npm.

## Creative workflow and release status

Page through `canvas_get_state` and read long text with `canvas_get_node_text` until `nextOffset` is null. Select an exact stored version with `canvas_list_media_versions`; view it with `canvas_get_image_preview` or `canvas_get_media_info`. Media URLs expire after five minutes. Use `canvas_get_generation_options`, configure an image or video node, quote with `canvas_quote_generation`, then pass the returned quote fingerprint, prompt, references and quoted amount unchanged to `canvas_generate_image` or `canvas_generate_video` after preparing an operation ID. Confirm the charge in Canvas. Query an uncertain operation with its original ID; media completion requires a separate `canvas_get_generation_status` check. Existing results can serve as references for a new node; a completed node can be generated again while keeping its older versions, and `canvas_select_media_version` can select an older stored version. Material review tools report supplier compliance, not creative quality.

Local type checks, focused tests and Bridge receipt loss/restart tests passed. DEV browser tests covered charged reference image generation, exact amount rejection, operation recovery after a lost receipt, image material review, regeneration on one node and version rollback. Live pricing changes, reference video generation, permission revocation and cloud Agent regression still need testing. Video frame extraction and runtime disable/revoke controls are not yet available. A signed media URL remains usable for its five-minute lifetime after permission changes. This archive is for internal validation only.
