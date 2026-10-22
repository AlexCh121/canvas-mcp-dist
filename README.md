# huihui Infinite Canvas MCP 0.1.4

[简体中文](README.zh-CN.md)

This repository distributes the local Bridge and stdio MCP package for authorized Infinite Canvas users. The current package version is 0.1.4.

Requires Node.js 22 or newer, a local Codex CLI, and access to the authorized Canvas on the same computer as the Bridge.

## One-sentence quickstart for an agent

First sign in to Infinite Canvas and copy the URL of the canvas you opened. Replace `PASTE_YOUR_CANVAS_URL_HERE` below with that URL, then send the entire message to a **local Codex or other agent running on the same computer as your browser**:

> Read https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.md. I have opened Infinite Canvas and signed in on this computer. My canvas URL is: `PASTE_YOUR_CANVAS_URL_HERE`. Check that Node.js 22+ is available, download `qorigin-canvas-mcp-0.1.4.tgz` and `SHA256SUMS-0.1.4` from this repository, and verify the checksum. Install the tarball, register `huihui-canvas` with `codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp`, start and keep `qorigin-canvas-mcp serve` running, then guide me to enter the one-use pairing code in Canvas Assistant → Codex and explicitly select the browser connection. If you are not running on this computer or cannot keep the Bridge running, explain the limitation instead of claiming it is connected.

## Install

Download [qorigin-canvas-mcp-0.1.4.tgz](qorigin-canvas-mcp-0.1.4.tgz) and [SHA256SUMS-0.1.4](SHA256SUMS-0.1.4) from this repository. Run these commands on the same computer as your signed-in canvas:

```bash
shasum -a 256 -c SHA256SUMS-0.1.4
npm install -g ./qorigin-canvas-mcp-0.1.4.tgz
codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

Keep the Bridge terminal open. In the logged-in Canvas, open **Canvas Assistant → Codex** and enter the one-use pairing code printed by the Bridge. In Codex, call `canvas_list_connections` and explicitly select the shown connection with `canvas_select_connection` before using tools. Remove any old `qorigin-canvas` or `qorigin-canvas-dev` registration when upgrading to avoid duplicate entries.

For another authorized Canvas, set `QORIGIN_CANVAS_ORIGINS` to its exact Origin; an explicitly empty value is rejected. The browser tab, Bridge, and Codex must run on the same computer. This package is not published to npm.

## Creative workflow and limitations

Page through `canvas_get_state` and read long text with `canvas_get_node_text` until `nextOffset` is null. Select an exact stored version with `canvas_list_media_versions`; view it with `canvas_get_image_preview` or `canvas_get_media_info`. Media URLs expire after five minutes. Use `canvas_get_generation_options`, configure an image or video node, quote with `canvas_quote_generation`, then pass the returned quote fingerprint, prompt, references and quoted amount unchanged to `canvas_generate_image` or `canvas_generate_video` after preparing an operation ID. Confirm the charge in Canvas. Query an uncertain operation with its original ID; media completion requires a separate `canvas_get_generation_status` check. Existing results can serve as references for a new node; a completed node can be generated again while keeping its older versions, and `canvas_select_media_version` can select an older stored version. Material review tools report supplier compliance, not creative quality.

This version does not provide video frame extraction or runtime disable/revoke controls for an existing pairing. A signed media URL remains usable for its five-minute lifetime after permission changes. Validate the complete creative workflow against the matching Canvas deployment.
