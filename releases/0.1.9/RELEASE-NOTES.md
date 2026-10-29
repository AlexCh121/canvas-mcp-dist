# huihui Canvas MCP 0.1.9

相对 0.1.8，本版新增以下能力，保留全部 42 个工具及已有连接诊断/恢复功能。

- 跨画布复用配对：用户明确勾选后，可在同站点、同账号和团队的画布复用授权，最长 7 天。每张画布仍有独立连接 ID，执行前须明确选择目标；退出或断开会撤销复用授权及其子连接。需要配套 Canvas Web。
- 上传附带提示词：canvas_upload_materials 的每个文件可带 title 和 prompt（最多 20,000 字符）。名称与多行提示词可随素材保存到图片节点，不另建文本节点、不调用模型；已有图片不会自动补回原提示词。需要配套 Canvas Service 声明 upload_prompt_v1，缺少能力时明确拒绝，不静默丢弃提示词。
- 模型配置指引：明确先查询可用模型、配置节点，再报价执行，减少要求用户手动选模型或点生成。仍保留画布中的付费报价确认；这属于工具指引优化，不保证外部 Agent 的全部行为。

## 安装与配套要求

本次发布 MCP 0.1.9 正式版并更新默认安装入口。配套网页和后端由同事于本次发布当晚独立部署，新增能力须待对应服务上线后生效；本包发布不操作数据库。请下载 v0.1.9 的 qorigin-canvas-mcp-0.1.9.tgz 和 SHA256SUMS-0.1.9，并先校验 SHA256。Node.js 22+，注册名 huihui-canvas，未发布到 npm。

升级前停止旧 Bridge，安装后重启 MCP 客户端和 Bridge；保留原私有目录及从用户提供画布 URL 提取的准确 Origin，不要删除原绑定。浏览器、Bridge 与本机 Agent 应运行于同一台电脑。原提示词需由调用方明确附带；图片文件本身不保证包含提示词。

## 验证与边界

沿用已完成的 13 项本机 Bridge 集成结果，覆盖配对复用、账号/团队隔离、撤销及原有连接恢复；DEV 已验证真实上传、多行提示词原样保存、显示名称和重放不增加节点。运行代码与已验证候选包逐文件一致，本次仅更正包内安装文档。未调用真实模型、未产生生成积分消耗。

客户真实复杂剧本、外部 WorkBuddy、系统休眠及长时运行仍待验收。30/60/70 分钟相关续期验证使用模拟时钟，不等于客户电脑真实长稳测试。未知写入继续查询原 operationId，不能据超时换 ID 重传或重复扣费。

---

This release extends 0.1.8 while retaining all 42 tools and the existing connection diagnosis/recovery behavior. It adds explicit pairing reuse across canvases within the same Origin/account/team (up to seven days, separate connection IDs), optional per-upload names and prompts, and clearer configure-before-quote generation guidance.

Cross-canvas reuse requires matching Canvas Web. Upload prompt/name persistence requires matching Canvas Service with upload_prompt_v1; unsupported services reject prompt uploads explicitly. Publication does not deploy services or migrations. The default installer selects 0.1.9 in latest.json. Matching Web and backend deployment is scheduled separately for the same release evening; new capabilities require that rollout. This is a GitHub tarball distribution, not an npm release.

Verify qorigin-canvas-mcp-0.1.9.tgz with SHA256SUMS-0.1.9. Requires Node.js 22+. Stop the previous Bridge before installation, restart the MCP client/Bridge afterward, and retain the original private directory and exact Origin derived from your authorized canvas URL. The caller must provide the original prompt; existing uploads are not automatically backfilled. Paid generation still requires the exact browser quote approval.

Existing validation includes 13 local Bridge integration checks and DEV real uploads with verbatim multiline prompts, names and idempotent replay. Runtime files match the validated candidate; only packaging documentation was corrected. No real model calls or generation credits were used. Customer WorkBuddy/background/sleep/long-duration scenarios remain pending; simulated clock checks do not prove real long-duration behavior.
