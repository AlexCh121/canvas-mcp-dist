# huihui 无限画布 MCP 0.1.5-dev.1 测试说明

仅供已获授权的 DEV 画布测试。本包来自画布源码分支 `codex/mcp-015-dev-package` 提交 `cb4de1c8`；需要配套的 DEV Canvas Web 和 Canvas Service。它不在稳定版 `latest.json` 中，GitHub `main` 的安装说明仍指向 0.1.4。包内 README 保留原文，测试时以本说明的版本、端口和安装路径为准。

## 一句话给本机 Agent

先登录 DEV 画布并复制当前画布 URL，将下面的占位符替换为该 URL，再把整句话发给与画布浏览器在同一台电脑上的本机 Agent：

> 请阅读 https://github.com/AlexCh121/canvas-mcp-dist/blob/dev-mcp-0.1.5-dev.1/dev/0.1.5-dev.1/INSTALL-DEV.zh-CN.md；我已登录的 DEV 画布 URL 是「请在此处替换为实际 DEV 画布 URL」；请只从该 DEV 测试分支下载并校验 `0.1.5-dev.1` 包，按文档隔离安装并注册 `huihui-canvas-dev`，从画布 URL 提取 Origin，以独立端口 `38622` 启动并保持本机 Bridge 运行，然后引导我在画布里输入一次性配对码、设置同一端口并显式选择浏览器连接；上传素材前先询问我授权的本机目录，若你不在这台电脑上或无法保持 Bridge 运行，请说明原因，不要声称连接成功。

## 本机安装

需 Node.js 22+、Codex CLI，以及与画布浏览器同一台电脑的终端。在一个空目录执行：

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

安装在独立目录，MCP 注册名为 `huihui-canvas-dev`，不会替换现有全局安装或稳定版注册。若该 DEV 注册已存在，先在 Codex 中核对旧配置，再移除同名旧注册并重新执行注册命令。

打开已登录的 **DEV** 画布，用实际画布 URL 启动 Bridge。下面的 URL 占位符必须替换；Origin 会从 URL 自动提取，不要指向生产画布：

```bash
CANVAS_DEV_URL='请在此处替换为实际 DEV 画布 URL'
CANVAS_DEV_ORIGIN="$(node -e 'process.stdout.write(new URL(process.argv[1]).origin)' "$CANVAS_DEV_URL")"
QORIGIN_CANVAS_ORIGINS="$CANVAS_DEV_ORIGIN" \
QORIGIN_CANVAS_MCP_PORT=38622 \
QORIGIN_CANVAS_MCP_HOME="$HOME/.huihui-canvas-dev-mcp" \
"$HOME/.huihui-canvas-dev/node_modules/.bin/qorigin-canvas-mcp" serve
```

保持终端运行。在画布「画布助手 → Codex」中将本机端口设为 `38622`，输入 Bridge 打印的一次性配对码。让 Codex 调用 `canvas_list_connections`，再用 `canvas_select_connection` 明确选择这张画布。上传本机素材前，先征得素材目录授权，重启 Bridge 时追加 `--upload-root /绝对路径/素材目录`。

## 建议验证

1. 读取画布状态和长文本，刷新页面后确认连接恢复。
2. 在授权目录选择多张图片上传，检查每项回执、节点和素材版本；重试未决操作时沿用原 `operationId`。
3. 在两个互不依赖的节点分别发起生成，确认可重叠运行；扣费前核对报价，完成后分别检查保存结果和旧版本。
4. 验证免费动作无需画布扣费确认、断线后结果对账、撤销权限后拒绝新写入。

付费生成仍需在画布内确认。`committed` 只代表提交已核对，不能代替生成完成与结果持久化。此次发布只是 DEV 测试包，完整创作流程仍需真实验收。
