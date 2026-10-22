# huihui 无限画布 MCP v0.1.5 / Infinite Canvas MCP v0.1.5

正式发布 / Release

下载本页的压缩包、`SHA256SUMS-0.1.5` 和中英文安装说明。需 Node.js 22+、同机 Codex、持续运行的本机 Bridge，以及已部署配套功能的画布网页和 Canvas Service。生产入口：[https://lc.tatakeji.cn/](https://lc.tatakeji.cn/)。注册名为 `huihui-canvas`，命令与技术包名保持 `qorigin-canvas-mcp` / `@qorigin/canvas-mcp`。

- 独立节点可在其他节点生成时继续提交；同节点及占用输入保持冲突保护。保留旧结果，支持同节点重做及版本切回。
- 批量上传最多 20 项，显式授权本机素材目录，按真实字节识别格式。初始传输预算为单文件 64 MiB、整批 512 MiB、最多四路传输、网页待传 Blob 128 MiB；业务/部署较小限制优先，MiB = 1,048,576 字节。
- 免费业务动作在画布自动执行；客户端自己的工具审批仍由客户端控制。收费逐项报价确认，旧报价或输入变化时安全拒绝，不自动重复扣费。
- 原生生成队列固定操作与素材版本；网页在线时推进。刷新后重新展开「画布助手 → Codex」恢复；面板关闭时不保证后台推进。未知结果只查原操作 ID。
- DEV 已验证图视频重叠完成、六图队列中途刷新后无手动继续、三节点再次生成并保留旧版、版本切回、确认期间真实改价拒绝、编辑租约接管阻断旧写入、撤销配对阻断读写、64 MiB/超一字节边界及上传恢复/重放。新增六图各结算 45 积分，账本每任务一笔。
- **已知限制：HEIC 可上传保存，但目前无法预览或读取宽高；视觉读取/模型参考优先用 PNG/JPEG。** HEIF 与模型兼容性另验。真实成员撤权、最终估价至原子扣费预留间的竞态、手工确认期间改输入、六视频无干预恢复、整批并发容量和完整结果依赖链尚未完成验收。

按用户明确要求，本版本已转为正式发布并设为当前安装版本，`latest.json` 与 GitHub Latest 均指向 0.1.5。保留原 v0.1.5 tag、压缩包及校验值；附件中最初的“预发布”字样是打包时状态，以本页当前发布状态为准。配套生产服务部署与完整创作验收独立记录，上述未验证项仍如实保留。云端 Agent 独立问题不作为本机 MCP 阻塞项。视频截帧、配音字幕、剪辑导出和远程无人值守不在本版范围。签名媒体 URL 到期前仍可用；未知上传不自动删除对象。

Download the archive, version checksum and bilingual guides attached to this release. Requires Node.js 22+, Codex and the browser on the same computer, a running Bridge, and matching Canvas Web/Service APIs. Register as `huihui-canvas`; the CLI remains `qorigin-canvas-mcp`.

This release adds concurrent independent generation, up to 20 local uploads per batch, automatic free Canvas actions, durable queues, pairing recovery and operation reconciliation. Paid items still require exact confirmation. DEV checks covered overlapping image/video tasks, a six-image queue across refresh, regeneration/version selection, real confirmation-time price changes, lease takeover, pairing revocation, upload recovery/idempotency and the 64 MiB file boundary. Runtime and tool schema match the tested candidate; only the bundled guides were updated for publication.

HEIC storage works, but preview decoding and dimensions currently fail; use PNG/JPEG for visual reading and model references. Membership revocation, the narrower final-estimate/atomic-hold race, manual input changes during confirmation, uninterrupted six-video recovery, aggregate upload capacity and dependent generation chains remain unverified. Promoted to a regular release at the user's explicit request; latest.json and GitHub Latest now select 0.1.5. The original tag, archive and checksums are retained. Prerelease wording inside the original attachments reflects their packaging date; this page records the current status. Matching production deployment acceptance remains separate. Remote/unattended execution, video frame extraction, dubbing and editing/export are outside this release.

SHA256 (`qorigin-canvas-mcp-0.1.5.tgz`): `182b33e4e9d397a7c22ede8455b8bf27a24fae0dc108ada76b7da96f7338ac73`
