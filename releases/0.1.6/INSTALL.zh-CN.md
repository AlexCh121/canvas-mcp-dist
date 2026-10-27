# huihui 无限画布 MCP 0.1.6

生产画布：https://lc.tatakeji.cn/ 。登录后打开自己的画布，再进行配对。

本包为 0.1.6 待发布候选；客户偶发断连仍在定位。

先在电脑浏览器登录无限画布，打开准备操作的画布。将下面的 URL 替换成**实际画布链接**，再把整段发给同一台电脑上的本机 Agent：

> 请先阅读随包 README 和 https://github.com/AlexCh121/canvas-mcp-dist 的安装说明。我已登录的画布是 `<粘贴你的实际画布URL>`。请核对 Node.js 22+，下载本版本提供的 `qorigin-canvas-mcp-0.1.6.tgz` 和 `SHA256SUMS-0.1.6`，校验后安装，注册 Codex MCP 并持续运行本机 Bridge。引导我在「画布助手 → Codex」输入一次性配对码，再列出并明确选择这张画布的连接。如需上传，先问我授权哪个本机素材目录。若你不在这台电脑运行，或不能保持 Bridge 在线，请明确说明。

## 安装与配对

需 Node.js 22+、本机 Codex CLI，以及可登录的画布。从本次候选交付目录获取压缩包与校验文件；正式发布后可在 [GitHub Releases](https://github.com/AlexCh121/canvas-mcp-dist/releases) 下载。然后执行：

```bash
shasum -a 256 -c SHA256SUMS-0.1.6
npm install -g ./qorigin-canvas-mcp-0.1.6.tgz
codex mcp add huihui-canvas -- qorigin-canvas-mcp mcp
qorigin-canvas-mcp serve
```

保持终端运行，在画布的「画布助手 → Codex」输入终端中的配对码。让 Codex 调用 `canvas_list_connections`，再用页面显示的连接 ID 调用 `canvas_select_connection`。需要新配对码时运行 `qorigin-canvas-mcp pair`。从早期 DEV 版本升级时移除旧的 `qorigin-canvas-dev` 注册。

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

刷新或 Bridge 重启后，在授权仍有效、账号和权限相同的情况下自动恢复。主动断开即撤销配对。授权为 24 小时，在线可续期，最长七天后需重新配对。登录失效、租约丢失或权限撤销时停止新写入。

## 配置与限制

使用其他获授权部署时，可显式配置 `QORIGIN_CANVAS_ORIGINS` 为其准确 Origin；空值拒绝启动。`QORIGIN_CANVAS_MCP_PORT` 修改本机端口，`QORIGIN_CANVAS_MCP_HOME` 修改私有目录。可通过 `QORIGIN_CANVAS_UPLOAD_MAX_FILE_BYTES`、`QORIGIN_CANVAS_UPLOAD_MAX_BATCH_BYTES`、`QORIGIN_CANVAS_UPLOAD_SNAPSHOT_BYTES` 缩小传输或快照预算。

本包需要配套网页与 Canvas Service 的上传和批次接口。已进行本地自动化验证，真实部署验收另行记录；本包通过压缩包分发，未发布到 npm。远程执行、无人值守、视频截帧、配音字幕、剪辑导出不在本版范围。临时媒体 URL 在到期前仍可使用。上传结果未知时不自动删除对象；已上传但未导入的对象需业务侧核查处理。

## 可靠性与批量保存

本候选基于已发布 0.1.5，实际工具定义见 `schema/customer-tools.v0.1.6.json`；保留 0.1.5 schema 供核对。批量保存要求网页、Canvas Service 均声明 `save_only_graph_v2`，能力缺失返回 `FEATURE_UNAVAILABLE`。注册名使用 `huihui-canvas`。

先调用 `canvas_get_mcp_capabilities`，再 validate/apply `save_only` 计划；apply 使用预备操作 ID，按原 ID 查询 `canvas_get_graph_operation` 与分页逐项回执。计划最多 200 项、2,000 条边变化、768 KiB（运行配置可收紧），每次短事务最多 10 项。更新已有节点须传配方指纹，参考素材须绑定具体版本；未知 `@[node:ID]` 明确拒绝。音频引用可保存，执行生成仍明确拒绝。

`canvas_get_graph_snapshot` 按 `prompt/references/parameters` 投影读取，后续分页及文本分段绑定 `expectedRevision`；原稿和展开提示词分别返回长度、UTF-8 hash 与 Unicode 码点偏移。响应过大请缩小页；展开超过上限明确拒绝，不返回伪空摘要。保存成功、模型兼容、可生成分别判断；付费生成仍需重新报价与确认。

连接移到页面管理，提供有界续期重试及 `canvas_get_connection_diagnostics`。同作用域 SSE 重连不取消已受理上传，无关 revision 变化不要求重传字节。明确退出、撤权、切换画布、授权到期和关闭浏览器仍可能中止后续工作。具体实测范围以发布验证记录为准。客户偶发断连、真实系统休眠/后台、外部代理失败及不支持的音频生成仍属明确限制。空闲编辑权可自动获取，真实草稿冲突和其他编辑者占用不会被覆盖。

已受理的 save-only 计划遇临时服务错误时，先安全核对服务端结果，再按同一推进请求继续。查询保留原操作 ID，并明确返回本地阻断原因；超时不许可换 ID 新建计划。真实草稿冲突、暂停控制变化或撤权会停止自动推进。

已确认导入的上传保持完成状态；若媒体元信息仍待补齐，查询原操作 ID 会按当前权限继续核对。补写绑定原 item 和素材版本，不重传已上传字节。探测失败仍明确 pending，不允许以此重新上传。
