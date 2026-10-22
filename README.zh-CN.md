# huihui 无限画布 MCP 0.1.4

[English](README.md)

本仓库提供无限画布本机 Bridge 与 stdio MCP 的安装包，供获授权的画布用户使用。当前安装包版本为 0.1.4。

## 使用条件

- Node.js 22 或更新版本，以及已安装的 Codex CLI。
- 能访问获授权的画布，并已在浏览器中登录。
- 浏览器、Bridge 和 Codex 必须运行在**同一台电脑**上。远程执行器、SSH 会话和容器中的 `127.0.0.1` 无法连接到客户电脑上的浏览器。

## 一句话给 Agent（Quickstart）

请先登录无限画布，复制登录后当前画布的 URL，把下方「请在此处替换画布工作区URL」替换为该 URL，再将整段发给**与画布浏览器运行在同一台电脑上的本地 Codex 或其他 Agent**：

> 请阅读 https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.zh-CN.md。我已在本机打开无限画布并登录；画布 URL 为：「请在此处替换画布工作区URL」。确认 Node.js 22 或更新版本，从该仓库下载 `qorigin-canvas-mcp-0.1.4.tgz` 和 `SHA256SUMS-0.1.4` 并校验；安装压缩包，用 `codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp` 注册 MCP，启动并保持 `qorigin-canvas-mcp serve` 运行，然后引导我在画布的「画布助手 → Codex」输入一次性配对码，并显式选择浏览器连接；如果你不在这台电脑上或无法保持 Bridge 运行，请说明原因，不要声称已经连接成功。

## 下载与安装

从本仓库下载 [qorigin-canvas-mcp-0.1.4.tgz](qorigin-canvas-mcp-0.1.4.tgz) 和 [SHA256SUMS-0.1.4](SHA256SUMS-0.1.4)，放在同一目录。在已登录画布的同一台电脑上执行：

```bash
shasum -a 256 -c SHA256SUMS-0.1.4
npm install -g ./qorigin-canvas-mcp-0.1.4.tgz
codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

最后一条命令会启动只监听本机 `127.0.0.1:38621` 的 Bridge，并打印一次性配对码。**保持这个终端运行。**

## 连接画布

1. 在已登录的画布中打开「画布助手 → Codex」，输入 Bridge 打印的配对码。配对码有效期为 10 分钟，且只能使用一次。
2. 在 Codex 中调用 `canvas_list_connections` 查看连接，再用 `canvas_select_connection` 显式选择要操作的浏览器标签页。
3. 写入前先调用 `canvas_prepare_operation`，并把返回的 `operationId` 原样传给写入工具。如果写入超时，先用 `canvas_get_operation_status` 查询结果，不要换一个操作 ID 盲目重试。

Bridge 保持运行时，如需重新生成配对码，可在另一个终端执行 `qorigin-canvas-mcp pair`。

本包尚未发布到 npm。使用其他获授权画布时，可用 `QORIGIN_CANVAS_ORIGINS` 指定其准确 Origin（协议、域名和端口），多个 Origin 用逗号分隔。显式设置为空值会拒绝启动。升级时如有 `qorigin-canvas` 或 `qorigin-canvas-dev` 旧注册，请先移除，避免重复入口。

## 创作流程与限制

分页调用 `canvas_get_state`；修改长文本前用 `canvas_get_node_text` 读到 `nextOffset` 为 `null`。用 `canvas_list_media_versions` 选择准确版本，通过 `canvas_get_image_preview` 或 `canvas_get_media_info` 查看素材；媒体 URL 有效期为 5 分钟。先用 `canvas_get_generation_options` 查询能力并配置图片或视频节点，再用 `canvas_quote_generation` 报价。写入前准备操作 ID，向 `canvas_generate_image` 或 `canvas_generate_video` 原样传递报价指纹、提示词、参考版本和报价金额，并在画布中确认费用。结果不明时查询原操作 ID；素材是否完成还须调用 `canvas_get_generation_status`。旧结果可作为新节点的参考；已完成节点可再次生成并保留旧版，`canvas_select_media_version` 可选回已保存版本。素材审核工具用于供应商合规检查，不评价创作质量。

本版尚不支持视频关键帧提取及运行时停用或撤销既有配对。已签发的媒体 URL 在 5 分钟有效期内无法即时撤销。完整创作流程仍需在对应画布部署中验证。
