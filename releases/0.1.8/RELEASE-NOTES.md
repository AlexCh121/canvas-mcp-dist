# huihui Canvas MCP 0.1.8

本次发布客户本机 MCP 包，默认安装版本更新为 0.1.8，保留 0.1.7 的全部 42 个工具。网页前端稍后发布：包内连接状态、离线诊断及 Bridge 故障记录可先使用；网页遇到模糊恢复拒绝时保留绑定、最多三次重试的修复，须等待配套前端部署。发布本包不会部署任何服务，无新增后端或数据库迁移。

修复连接状态误判：分别显示传输、网页响应和授权状态，近期网页 ACK 或工具回执才能证明已响应；流存在、心跳已发送或一次超时均不能证明网页正常或授权到期。新会话可选中有效离线绑定做诊断，也可直接传原 connectionId 查询；业务工具仍需网页在线及正常权限。

恢复拒绝不再一律声明到期，具体原因仅在本机安装授权后的诊断中提供。新增最多 100 条白名单生命周期事件及心跳确认记录，Bridge 诊断文件保留 30 天，与授权凭据分开写入，可在重启后核查；可选诊断存储错误不撤销授权。不记录凭证、提示词或媒体 URL。

安装：核验本 Release 的 qorigin-canvas-mcp-0.1.8.tgz 与 SHA256SUMS-0.1.8；Node.js 22+，注册名 huihui-canvas。升级先停止旧 Bridge、安装并重启 MCP 客户端及 Bridge，保持原私有目录与用户提供画布 URL 的准确 Origin，不要先删除原绑定。浏览器、Bridge 和 Agent 须在同一电脑。本包不在 npm 发布。

验证：Bridge 12 项、网页聚焦 51 项及网页类型检查通过；解包 stdio 为 0.1.8 / 42 工具，schema 一致。覆盖真实 ACK、Bridge 重启、原绑定恢复、恢复请求幂等、错误身份、真实到期和旧 token 拒绝。30/60/70 分钟续期为模拟时钟验证，不能替代真实浏览器长稳；未消耗积分。本版未部署前端或改动生产服务。

客户原始断流触发原因、真实后台/系统休眠、长时运行及多账号撤权仍需验收，不宣称已解决全部掉线。未知操作继续查询原 operationId，超时不许可换 ID 重传、重复生成或重复扣费。

---

This release publishes the local MCP package and selects 0.1.8 as the default installation, retaining all 42 tools from 0.1.7. Canvas Web will be deployed separately. Package-side connection states, offline diagnosis and Bridge evidence are available first; preserving ambiguous rejected resume bindings and bounded same-request retries require the matching Web update. No backend change or migration is introduced.

Transport presence, recent browser response and authorization are reported separately. A recent browser ACK or tool result is required for connected. New MCP sessions can select valid offline bindings for diagnosis or query the original connectionId directly. Business execution still requires an online browser and normal permissions. A timeout, missing local binding or sent heartbeat does not prove expiry.

Resume rejections distinguish verified expiry from unverified failures. Detailed reasons remain behind local installation authorization. Bounded redacted lifecycle evidence survives Bridge restarts in a separate diagnostic store: up to 100 events per binding, 30-day file retention, throttled heartbeat writes. Diagnostic storage errors cannot revoke authorization or overwrite rotated credentials.

Verify the archive with SHA256SUMS-0.1.8. Requires Node.js 22+, registration huihui-canvas. Stop the old Bridge before upgrading, retain the original private directory and exact Origin derived from your authorized canvas URL, and restart the MCP client and Bridge. Do not delete the original pairing first. Browser, Bridge and agent must run on the same computer. Distribution is a GitHub tarball, not an npm publication.

Validation: 12 Bridge tests, 51 focused Web tests and Web type checking passed. Unpacked stdio version and all 42 tools match the schema. Coverage includes real ACK, process restart, original binding recovery, idempotent resume, rejected identity, verified expiry and stale-token rejection. The 30/60/70-minute scenarios use simulated time. No credits spent; no Web or production-service deployment performed by this release.

The original customer disconnect trigger and real-browser background/sleep/long-duration behavior remain under investigation. This release does not claim to fix every disconnect. Preserve the original operationId for unknown writes; a timeout never authorizes a duplicate upload, generation or charge.
