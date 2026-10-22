# huihui Infinite Canvas MCP 0.1.5-dev.1 test guide

For authorized DEV canvas testing only. Built from Canvas source branch `codex/mcp-015-dev-package` at `cb4de1c8`; it needs the matching DEV Canvas Web and Canvas Service. This package is not referenced by the stable `latest.json`. The bundled README remains unchanged; use this guide for the DEV version, port, and install path.

## Install on the browser computer

Requires Node.js 22+ and the Codex CLI. Run in an empty directory:

```bash
DEV_MCP_BASE=https://raw.githubusercontent.com/AlexCh121/canvas-mcp-dist/dev-mcp-0.1.5-dev.1/dev/0.1.5-dev.1
curl -fL -O "$DEV_MCP_BASE/qorigin-canvas-mcp-0.1.5-dev.1.tgz"
curl -fL -O "$DEV_MCP_BASE/SHA256SUMS-0.1.5-dev.1"
shasum -a 256 -c SHA256SUMS-0.1.5-dev.1
npm install --prefix "$HOME/.huihui-canvas-dev" ./qorigin-canvas-mcp-0.1.5-dev.1.tgz
codex mcp add huihui-canvas-dev \
  --env QORIGIN_CANVAS_MCP_PORT=38622 \
  --env QORIGIN_CANVAS_MCP_HOME="$HOME/.huihui-canvas-dev-mcp" \
  -- "$HOME/.huihui-canvas-dev/node_modules/.bin/qorigin-canvas-mcp" mcp
```

This uses a separate package directory and Codex registration, leaving the stable global installation alone. Check and remove an existing `huihui-canvas-dev` registration before registering a replacement.

Open your signed-in **DEV** canvas and start the Bridge with its actual URL. Replace the placeholder below; the command derives the exact Origin. Do not use a production canvas URL.

```bash
CANVAS_DEV_URL='PASTE_YOUR_ACTUAL_DEV_CANVAS_URL_HERE'
CANVAS_DEV_ORIGIN="$(node -e 'process.stdout.write(new URL(process.argv[1]).origin)' "$CANVAS_DEV_URL")"
QORIGIN_CANVAS_ORIGINS="$CANVAS_DEV_ORIGIN" \
QORIGIN_CANVAS_MCP_PORT=38622 \
QORIGIN_CANVAS_MCP_HOME="$HOME/.huihui-canvas-dev-mcp" \
"$HOME/.huihui-canvas-dev/node_modules/.bin/qorigin-canvas-mcp" serve
```

Keep the terminal running. In Canvas Assistant → Codex, set the local port to `38622` and enter the one-use pairing code. Call `canvas_list_connections` and explicitly select the canvas with `canvas_select_connection`. Before local uploads, authorize a directory and restart the Bridge with `--upload-root /absolute/path/to/materials`.

Suggested checks: read state and long text; refresh and verify recovery; upload several authorized files and inspect per-item receipts and media versions; generate on two independent nodes while one is still running; check the quoted charge before confirming, then inspect both persisted results and older versions. Reuse the original `operationId` when reconciling an uncertain write. Verify that a revoked permission prevents new writes.

Paid generation still requires confirmation in Canvas. `committed` confirms submission only, not completed and persisted media. This DEV package is awaiting live workflow acceptance.
