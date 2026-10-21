# QOrigin Canvas MCP（DEV 预览版）

[English](README.md)

本仓库提供雷盈画布本机 Bridge 与 stdio MCP 的安装包，供获授权的 DEV 测试使用。这里仅发布安装包，不包含画布应用源码。

- 版本：`@qorigin/canvas-mcp@0.1.1`
- 来源：`tano-canvas` 的 `codex/customer-mcp` 分支，提交 `763761cf`；打包时将包版本和 MCP 服务版本设为 `0.1.1`
- 状态：DEV 技术预览，尚非生产客户版本

## 使用条件

- Node.js 22 或更新版本，以及已安装的 Codex CLI。
- 能访问 DEV 画布，并已在浏览器中登录。
- 浏览器、Bridge 和 Codex 必须运行在**同一台电脑**上。远程执行器、SSH 会话和容器中的 `127.0.0.1` 无法连接到客户电脑上的浏览器。

## 下载与安装

从本仓库下载 [qorigin-canvas-mcp-0.1.1.tgz](qorigin-canvas-mcp-0.1.1.tgz) 和 [SHA256SUMS](SHA256SUMS)，放在同一目录。在该目录执行：

```bash
shasum -a 256 -c SHA256SUMS
npm install -g ./qorigin-canvas-mcp-0.1.1.tgz
codex mcp add qorigin-canvas-dev -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

最后一条命令会启动只监听本机 `127.0.0.1:38621` 的 Bridge，并打印一次性配对码。**保持这个终端运行。**

## 连接画布

1. 在已登录的 DEV 画布中打开「画布助手 → Codex」，输入 Bridge 打印的配对码。配对码有效期为 10 分钟，且只能使用一次。
2. 在 Codex 中调用 `canvas_list_connections` 查看连接，再用 `canvas_select_connection` 显式选择要操作的浏览器标签页。
3. 写入前先调用 `canvas_prepare_operation`，并把返回的 `operationId` 原样传给写入工具。如果写入超时，先用 `canvas_get_operation_status` 查询结果，不要换一个操作 ID 盲目重试。

Bridge 保持运行时，如需重新生成配对码，可在另一个终端执行 `qorigin-canvas-mcp pair`。

本包尚未发布到 npm。默认仅允许 DEV 画布 Origin `https://ica.qianyuan-aitech.cn` 和本地开发 Origin `http://localhost:3000`；连接其他画布地址时需设置 `QORIGIN_CANVAS_ORIGINS` 为准确的 Origin。
