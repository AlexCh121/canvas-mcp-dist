# QOrigin Canvas MCP DEV preview

[简体中文](README.zh-CN.md)

This repository distributes the local Canvas Bridge and stdio MCP package for authorized DEV testing. It does not contain the Canvas application source code.

Version: `@qorigin/canvas-mcp@0.1.1`  
Source: `tano-canvas` branch `codex/customer-mcp` at `763761cf`; the package and MCP server version were set to `0.1.1` for this archive.  
Status: DEV technical preview. Not a production customer release.

Requires Node.js 22 or newer, a local Codex CLI, and access to the DEV Canvas on the same computer as the Bridge.

## One-sentence quickstart for an agent

Paste this into a **local Codex agent running on the same computer as your DEV Canvas browser**:

> Read https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.md, check that Node.js 22+ is available, download and verify the `0.1.1` tarball against `SHA256SUMS`, install it, register `qorigin-canvas-dev` with `codex mcp add qorigin-canvas-dev -- qorigin-canvas-mcp mcp`, start and keep `qorigin-canvas-mcp serve` running, then guide me to enter the one-use pairing code in Canvas and explicitly select the browser connection; if you are not running on this computer or cannot keep the Bridge running, stop and tell me instead of claiming it is connected.

## Install

Download `qorigin-canvas-mcp-0.1.1.tgz` and `SHA256SUMS` from this repository, then run:

```bash
shasum -a 256 -c SHA256SUMS
npm install -g ./qorigin-canvas-mcp-0.1.1.tgz
codex mcp add qorigin-canvas-dev -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

Keep the Bridge terminal open. In the logged-in DEV Canvas, open **Canvas Assistant → Codex** and enter the one-use pairing code printed by the Bridge. In Codex, call `canvas_list_connections` and explicitly select the shown connection with `canvas_select_connection` before using tools.

The browser tab, Bridge, and Codex must run on the same computer. This package is not published to npm.
