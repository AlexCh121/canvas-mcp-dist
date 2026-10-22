# huihui 无限画布 MCP 0.1.5

画布入口：[https://lc.tatakeji.cn/](https://lc.tatakeji.cn/)。本版新工具需配套网页与 Canvas Service 部署后使用。

先在电脑浏览器登录无限画布，打开准备操作的画布。将下面的 URL 替换成**实际画布链接**，再把整段发给同一台电脑上的本机 Agent：

> 请先阅读随包 README 和 https://github.com/AlexCh121/canvas-mcp-dist 的安装说明。我已登录的画布是 `<粘贴你的实际画布URL>`。请核对 Node.js 22+，下载本版本提供的 `qorigin-canvas-mcp-0.1.5.tgz` 和 `SHA256SUMS-0.1.5`，校验后安装，以 `huihui-canvas` 注册 Codex MCP 并持续运行本机 Bridge。引导我在「画布助手 → Codex」输入一次性配对码，再列出并明确选择这张画布的连接。如需上传，先问我授权哪个本机素材目录。若你不在这台电脑运行，或不能保持 Bridge 在线，请明确说明。

## 安装与配对

需 Node.js 22+、本机 Codex CLI，以及可登录的画布。从 [v0.1.5 发布页](https://github.com/AlexCh121/canvas-mcp-dist/releases/tag/v0.1.5) 下载压缩包与校验文件。然后执行：

```bash
shasum -a 256 -c SHA256SUMS-0.1.5
npm install -g ./qorigin-canvas-mcp-0.1.5.tgz
codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

保持终端运行，在画布的「画布助手 → Codex」输入终端中的配对码。让 Codex 调用 `canvas_list_connections`，再用页面显示的连接 ID 调用 `canvas_select_connection`。需要新配对码时运行 `qorigin-canvas-mcp pair`。升级前用 `codex mcp list` 检查并移除旧的 `qorigin-canvas`、`qorigin-canvas-dev` 或 `qorigin_canvas_dev` 注册，避免重复工具；已有 `huihui-canvas` 时替换该注册。先停止旧 Bridge 再启动新版，保留原私有状态目录以便恢复。

上传前用明确授权的目录启动 Bridge；多个目录可重复传参：

```bash
qorigin-canvas-mcp serve --upload-root /绝对路径/素材目录
```

只读取授权目录中的普通文件，拒绝 URL、越界路径和跳出目录的符号链接。每批最多 20 项，先调用 `canvas_get_upload_options` 获取当前部署限额。初始传输预算为单文件 64 MiB、整批 512 MiB、最多 4 路传输，网页待传 Blob 合计不超过 128 MiB；业务或部署配置可进一步缩小。MiB 为 `1024 * 1024` 字节。Bridge 私有快照可读取 24 小时，运行中定期清理过期文件，重启时也清理。按真实文件头识别常见二进制图片、视频及 MP3/WAV，无法识别的格式逐项拒绝；上传成功不等于浏览器和生成模型均支持该格式。

## 使用规则

- 配对后，免费业务动作在画布中自动执行，包括文本、节点、连线、参数、版本选择、素材上传与免费审核；Codex 等客户端自身的工具审批仍由客户端控制。
- 扣费生成仍逐项报价和确认。报价、提示词、参考版本、参数和金额必须一致；变化后重新报价。真实零费用也使用服务端金额约束。
- A 节点生成中可提交独立的 B 节点；同一目标或被占用输入仍受冲突保护。新结果保留为版本，可回选旧版本。
- 批量上传返回接受回执，继续用原 `operationId` 查询节点和版本是否已导入。未知时不要换 ID 整批重传。
- 原生批量生成最多 20 个独立目标，由页面持久队列逐项报价、确认和提交。暂停只停止未提交项，继续不会重新生成已提交或未知的任务。报价或输入变化时暂停检查；网页需在线才能继续推进。
- `committed` 只表示提交已核对；任务完成、结果已保存要分别确认。未知结果保留 `outcome_unknown`，不能视为失败或可重复扣费。
- 修改长文本前读完分页；媒体读取和参考素材都绑定节点及具体版本。素材审核是供应商合规审核，不能当作创作质量评分。

刷新后重新打开「画布助手 → Codex」以恢复连接；面板未挂载时不支持后台重连。刷新或 Bridge 重启后，在授权仍有效、账号和权限相同的情况下自动恢复。主动断开即撤销配对。授权为 24 小时，在线可续期，最长七天后需重新配对。登录失效、租约丢失或权限撤销时停止新写入。

## 配置与限制

使用其他获授权部署时，可显式配置 `QORIGIN_CANVAS_ORIGINS` 为其准确 Origin；空值拒绝启动。`QORIGIN_CANVAS_MCP_PORT` 修改本机端口，`QORIGIN_CANVAS_MCP_HOME` 修改私有目录。可通过 `QORIGIN_CANVAS_UPLOAD_MAX_FILE_BYTES`、`QORIGIN_CANVAS_UPLOAD_MAX_BATCH_BYTES`、`QORIGIN_CANVAS_UPLOAD_SNAPSHOT_BYTES` 缩小传输或快照预算。

本包需要配套网页与 Canvas Service 的上传和批次接口。已在 DEV 验证独立图视频重叠生成、六图队列刷新恢复、重做与版本切换、确认期间真实改价拒绝、租约接管、配对撤销、上传幂等及 64 MiB 文件边界。本版为预发布，生产部署验收另行完成。**HEIC 可上传保存，但目前无法预览及读取宽高；需要视觉读取或模型引用时请使用 PNG/JPEG。** HEIF 和模型兼容性分别验证；六视频无干预恢复、真实成员撤权及整批上传容量尚未验收；本包通过压缩包分发，未发布到 npm。远程执行、无人值守、视频截帧、配音字幕、剪辑导出不在本版范围。临时媒体 URL 在到期前仍可使用。上传结果未知时不自动删除对象；已上传但未导入的对象需业务侧核查处理。
