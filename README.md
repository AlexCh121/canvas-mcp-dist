# QOrigin Canvas MCP 0.1.3 · production candidate

[简体中文](README.zh-CN.md)

This repository distributes the local Canvas Bridge and stdio MCP package for authorized Canvas users. It does not contain the Canvas application source code.

Version: `@qorigin/canvas-mcp@0.1.3`
Source: integrated `tano-canvas` branch `hotfix.20261021.prompt-limits` at `c2b45887`, with package hardening on `codex/mcp-0.1.3` at `8e91dc1a`; integrated backend branch `hotfix.20261021.1` at `4e89f8d5`.
Status: Production candidate for a controlled rollout. Customer release remains gated on the matching Canvas and backend deployment and end-to-end acceptance tests.

Requires Node.js 22 or newer, a local Codex CLI, and access to the authorized Canvas on the same computer as the Bridge.

## One-sentence quickstart for an agent

Paste this into a **local Codex agent running on the same computer as your Canvas browser**:

> Read https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.md. Check that Node.js 22+ is available, download `qorigin-canvas-mcp-0.1.3.tgz` and `SHA256SUMS-0.1.3` from this repository, and verify the checksum. Set `QORIGIN_CANVAS_ORIGINS` to the exact Origin of my authorized Canvas, install the tarball, register `qorigin-canvas` with `codex mcp add qorigin-canvas -- qorigin-canvas-mcp mcp`, start and keep `qorigin-canvas-mcp serve` running, then guide me to enter the one-use pairing code in Canvas and explicitly select the browser connection. If you are not running on this computer or cannot keep the Bridge running, explain the limitation instead of claiming it is connected.

## Install

Download [qorigin-canvas-mcp-0.1.3.tgz](qorigin-canvas-mcp-0.1.3.tgz) and [SHA256SUMS-0.1.3](SHA256SUMS-0.1.3) from this repository. Replace the example Origin below with your authorized Canvas Origin, then run:

```bash
shasum -a 256 -c SHA256SUMS-0.1.3
npm install -g ./qorigin-canvas-mcp-0.1.3.tgz
codex mcp add qorigin-canvas -- qorigin-canvas-mcp mcp
export QORIGIN_CANVAS_ORIGINS="https://your-canvas.example"
qorigin-canvas-mcp serve
```

Keep the Bridge terminal open. In the logged-in Canvas, open **Canvas Assistant → Codex** and enter the one-use pairing code printed by the Bridge. In Codex, call `canvas_list_connections` and explicitly select the shown connection with `canvas_select_connection` before using tools. Remove an old `qorigin-canvas-dev` registration if upgrading from 0.1.2.

The browser tab, Bridge, and Codex must run on the same computer. This package is not published to npm.

## Creative workflow and release status

Page through `canvas_get_state` and read long text with `canvas_get_node_text` until `nextOffset` is null. Select an exact stored version with `canvas_list_media_versions`; view it with `canvas_get_image_preview` or `canvas_get_media_info`. Media URLs expire after five minutes. Use `canvas_get_generation_options`, configure an image or video node, quote with `canvas_quote_generation`, then pass the returned quote fingerprint, prompt, references and quoted amount unchanged to `canvas_generate_image` or `canvas_generate_video` after preparing an operation ID. Confirm the charge in Canvas. Query an uncertain operation with its original ID; media completion requires a separate `canvas_get_generation_status` check. Existing results can serve as references for a new node; a completed node can be generated again while keeping its older versions, and `canvas_select_media_version` can select an older stored version. Material review tools report supplier compliance, not creative quality.

The 0.1.3 package was built from the integrated Canvas branch and passed local type checks, Bridge recovery tests, and the explicit Origin startup test. Earlier DEV browser tests covered charged reference image generation, exact amount rejection, operation recovery after a lost receipt, image material review, regeneration on one node, and version rollback. The integrated production build still needs live pricing-change, reference-video, permission-revocation, repeated-operation billing, and cloud Agent tests before customer release. Video frame extraction and runtime disable/revoke controls are not yet available. A signed media URL remains usable for its five-minute lifetime after permission changes.
