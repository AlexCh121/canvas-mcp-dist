# 无限画布 MCP

[English](README.md)

本仓库提供无限画布本机 Bridge 与 stdio MCP 的安装包，供获授权的画布用户使用。默认安装版本、压缩包和校验文件以 [latest.json](latest.json) 为准。

## 版本选择

| 用途 | 版本与下载 | 状态 |
|---|---|---|
| 默认安装 | [0.1.6](https://github.com/AlexCh121/canvas-mcp-dist/releases/tag/v0.1.6) · [安装说明](releases/0.1.6/INSTALL.zh-CN.md)，由 [latest.json](latest.json) 指定 | 正式发布，当前默认版本 |
| 历史版本 | [0.1.5](https://github.com/AlexCh121/canvas-mcp-dist/releases/tag/v0.1.5) | 保留供查阅和兼容核对 |

下方通用安装指令默认安装 0.1.6；客户偶发断连仍在追踪。使用你已获授权并登录的画布 URL，仓库不提供具体画布入口。

## 使用条件

- Node.js 22 或更新版本，以及已安装的 Codex CLI。
- 能访问获授权的画布，并已在浏览器中登录。
- 浏览器、Bridge 和 Codex 必须运行在**同一台电脑**上。远程执行器、SSH 会话和容器中的 `127.0.0.1` 无法连接到客户电脑上的浏览器。

## 一句话给 Agent（Quickstart）

请先登录画布，复制登录后当前画布的 URL，把下方「请在此处替换画布工作区URL」替换为该 URL，再将整段发给**与画布浏览器运行在同一台电脑上的本地 Codex 或其他 Agent**：

> 请阅读 https://github.com/AlexCh121/canvas-mcp-dist/blob/main/README.zh-CN.md 和 https://github.com/AlexCh121/canvas-mcp-dist/blob/main/latest.json。我已在本机打开无限画布并登录；画布 URL 为：「请在此处替换画布工作区URL」。从仓库 `main` 的 `latest.json` 获取当前版本、`archive`、`checksumFile`、`sha256`、`cli` 和 `codexRegistration`，确认 Node.js 达到 `nodeMajorMinimum`。下载清单指定的压缩包与校验文件，核对两处 SHA256 一致后安装；若清单或文件不一致，请停止。用清单中的注册名及 CLI 注册 Codex MCP。从我提供的画布 URL 提取准确 Origin（协议、域名和端口，不含路径），以 `QORIGIN_CANVAS_ORIGINS` 环境变量传给该 CLI 的 `serve` 进程，启动并保持 Bridge 运行；不要使用通配符或忽略域名校验。然后引导我在画布的「画布助手 → Codex」输入一次性配对码，并显式选择浏览器连接；如果你不在这台电脑上或无法保持 Bridge 运行，请说明原因，不要声称已经连接成功。

## 下载与安装

从本仓库下载 [latest.json](latest.json)，并按其中的 `archive` 和 `checksumFile` 下载同仓库文件，放在同一目录。以下命令在已登录画布的同一台电脑上执行，变量由清单读取，因此新版本无需修改命令：

```bash
CANVAS_URL='请在此处替换画布工作区URL'
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

最后一条命令启动只监听本机的 Bridge，并打印一次性配对码。**保持这个终端运行。**升级已有安装时，先核对并移除同名旧注册，避免重复入口。

## 连接画布

1. 在已登录的画布中打开「画布助手 → Codex」，输入 Bridge 打印的配对码。配对码有效期为 10 分钟，且只能使用一次。
2. 在 Codex 中调用 `canvas_list_connections` 查看连接，再用 `canvas_select_connection` 显式选择要操作的浏览器标签页。
3. 写入前先调用 `canvas_prepare_operation`，并把返回的 `operationId` 原样传给写入工具。如果写入超时，先用 `canvas_get_operation_status` 查询结果，不要换一个操作 ID 盲目重试。

Bridge 保持运行时，如需重新生成配对码，可在另一个终端使用清单中的 `cli` 执行 `pair`。

本包尚未发布到 npm。使用多张不同域名的获授权画布时，可在启动 Bridge 时将多个准确 Origin 以逗号分隔传给 `QORIGIN_CANVAS_ORIGINS`；切换到未配置的域名需重启 Bridge 并重新连接。显式设置为空值会拒绝启动。升级时如有 `qorigin-canvas` 或 `qorigin-canvas-dev` 旧注册，请先移除，避免重复入口。

## 创作流程与限制

分页调用 `canvas_get_state`；修改长文本前用 `canvas_get_node_text` 读到 `nextOffset` 为 `null`。用 `canvas_list_media_versions` 选择准确版本，通过 `canvas_get_image_preview` 或 `canvas_get_media_info` 查看素材；媒体 URL 有效期为 5 分钟。先用 `canvas_get_generation_options` 查询能力并配置图片或视频节点，再用 `canvas_quote_generation` 报价。写入前准备操作 ID，向 `canvas_generate_image` 或 `canvas_generate_video` 原样传递报价指纹、提示词、参考版本和报价金额，并在画布中确认费用。结果不明时查询原操作 ID；素材是否完成还须调用 `canvas_get_generation_status`。旧结果可作为新节点的参考；已完成节点可再次生成并保留旧版，`canvas_select_media_version` 可选回已保存版本。素材审核工具用于供应商合规检查，不评价创作质量。

独立节点可并行生成；本机批量上传最多 20 项，须先授权素材目录。免费业务动作在画布自动执行，收费仍逐项确认，客户端工具审批由客户端控制。刷新后重新打开「画布助手 → Codex」恢复连接，主动断开会撤销配对。HEIC 可保存但目前无法预览和读取宽高，视觉读取优先用 PNG/JPEG。视频截帧和无人值守不在本版范围；签名媒体 URL 到期前仍可用。具体验收范围与限制见版本发布说明。
