# 雷盈画布 MCP 0.1.3（生产候选版）

[English](README.md)

本仓库提供雷盈画布本机 Bridge 与 stdio MCP 的安装包，供获授权的画布用户使用。这里仅发布安装包，不包含画布应用源码。

- 版本：`@qorigin/canvas-mcp@0.1.3`
- 来源：画布集成分支 `hotfix.20261021.prompt-limits` 提交 `c2b45887`，安装包加固分支 `codex/mcp-0.1.3` 提交 `8e91dc1a`；后端集成分支 `hotfix.20261021.1` 提交 `4e89f8d5`
- 状态：生产候选包，供受控验证；客户正式开放仍需对应画布和后端部署及端到端验收

## 使用条件

- Node.js 22 或更新版本，以及已安装的 Codex CLI。
- 能访问获授权的画布，并已在浏览器中登录。
- 浏览器、Bridge 和 Codex 必须运行在**同一台电脑**上。远程执行器、SSH 会话和容器中的 `127.0.0.1` 无法连接到客户电脑上的浏览器。

## 一句话给 Agent（Quickstart）

把下面这句话发给**与画布浏览器运行在同一台电脑上的本地 Codex**：

> 请阅读 https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.zh-CN.md，确认本机有 Node.js 22 或更新版本，从 v0.1.3 Release 下载 `qorigin-canvas-mcp-0.1.3.tgz` 和 `SHA256SUMS-0.1.3` 并校验。将 `QORIGIN_CANVAS_ORIGINS` 设置为我获授权画布的准确 Origin，安装压缩包，用 `codex mcp add qorigin-canvas -- qorigin-canvas-mcp mcp` 注册 MCP，启动并保持 `qorigin-canvas-mcp serve` 运行，然后引导我在画布里手动输入一次性配对码并显式选择浏览器连接；如果你不在这台电脑上或无法保持 Bridge 运行，请说明原因，不要声称已经连接成功。

## 下载与安装

从同一 Release 下载 [qorigin-canvas-mcp-0.1.3.tgz](https://github.com/AlexCh121/canvas-mcp-dist/releases/download/v0.1.3/qorigin-canvas-mcp-0.1.3.tgz) 和 [SHA256SUMS-0.1.3](https://github.com/AlexCh121/canvas-mcp-dist/releases/download/v0.1.3/SHA256SUMS-0.1.3)，放在同一目录。将下面的示例 Origin 换成获授权画布的准确 Origin，然后执行：

```bash
shasum -a 256 -c SHA256SUMS-0.1.3
npm install -g ./qorigin-canvas-mcp-0.1.3.tgz
codex mcp add qorigin-canvas -- qorigin-canvas-mcp mcp
export QORIGIN_CANVAS_ORIGINS="https://your-canvas.example"
qorigin-canvas-mcp serve
```

最后一条命令会启动只监听本机 `127.0.0.1:38621` 的 Bridge，并打印一次性配对码。**保持这个终端运行。**

## 连接画布

1. 在已登录的画布中打开「画布助手 → Codex」，输入 Bridge 打印的配对码。配对码有效期为 10 分钟，且只能使用一次。
2. 在 Codex 中调用 `canvas_list_connections` 查看连接，再用 `canvas_select_connection` 显式选择要操作的浏览器标签页。
3. 写入前先调用 `canvas_prepare_operation`，并把返回的 `operationId` 原样传给写入工具。如果写入超时，先用 `canvas_get_operation_status` 查询结果，不要换一个操作 ID 盲目重试。

Bridge 保持运行时，如需重新生成配对码，可在另一个终端执行 `qorigin-canvas-mcp pair`。

本包尚未发布到 npm。Bridge 未设置 `QORIGIN_CANVAS_ORIGINS` 时会拒绝启动；该变量须填写目标站点的准确 Origin（协议、域名和端口），多个 Origin 用逗号分隔。从 0.1.2 升级时，建议移除旧的 `qorigin-canvas-dev` 注册，避免重复入口。

## 创作流程与发布状态

分页调用 `canvas_get_state`；修改长文本前用 `canvas_get_node_text` 读到 `nextOffset` 为 `null`。用 `canvas_list_media_versions` 选择准确版本，通过 `canvas_get_image_preview` 或 `canvas_get_media_info` 查看素材；媒体 URL 有效期为 5 分钟。先用 `canvas_get_generation_options` 查询能力并配置图片或视频节点，再用 `canvas_quote_generation` 报价。写入前准备操作 ID，向 `canvas_generate_image` 或 `canvas_generate_video` 原样传递报价指纹、提示词、参考版本和报价金额，并在画布中确认费用。结果不明时查询原操作 ID；素材是否完成还须调用 `canvas_get_generation_status`。旧结果可作为新节点的参考；已完成节点可再次生成并保留旧版，`canvas_select_media_version` 可选回已保存版本。素材审核工具用于供应商合规检查，不评价创作质量。

0.1.3 包基于合并后的画布源码构建，本地类型检查、Bridge 恢复测试和显式 Origin 启动测试通过。此前 DEV 浏览器已验证参考图付费生成、金额不符拒绝、回执丢失后的操作恢复、图片合规审核、同节点重做与旧版切回；合并后的生产构建仍需完成真实改价竞态、参考视频生成、权限撤销、重复操作不重复扣费和云端 Agent 回归。视频关键帧提取及运行时停用/撤销既有配对尚未实现。已签发的媒体 URL 在 5 分钟有效期内无法即时撤销。
