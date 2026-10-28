# huihui Canvas MCP 0.1.7 正式发布

新增节点显示名读取与 `canvas_rename_node`：文本、图片、视频、音频和配置节点可独立改名，保留正文、素材版本和生成引用。同名允许；名称裁剪首尾空白后须为 1～200 字符。免费动作沿用自动执行与现有编辑权限、租约和节点忙保护。

普通写入沿用原操作 ID 和服务端原子回执；旧操作重放不会覆盖后续网页改名。节点忙返回阻塞信息，先查询阻塞的原操作；读取鉴权失败按具体原因恢复，不新建未知操作。修复分组网页携带 schema_version 导致普通 MCP 回执保存被拒绝的问题。

安装前核验本 Release 的 `qorigin-canvas-mcp-0.1.7.tgz` 与 `SHA256SUMS-0.1.7`；Node.js 22+，注册名 `huihui-canvas`，42 个工具。默认安装清单 latest.json 已选择 0.1.7。本包通过 GitHub 压缩包分发，未发布到 npm。

新改名工具需要网页与 Canvas Service 均支持 `node_display_name_v1`，服务未配套时明确拒绝。发布本包不会部署服务；生产服务由配套发布流程上线。使用你已登录且获授权的画布 URL，浏览器、Bridge 与 Agent 必须位于同一电脑；保持网页和 Bridge 在线。

验证：正式包 Bridge 8 项通过；DEV 候选真实 stdio 验证文本/图片改名、同名裁剪、正文和素材版本保护、后续网页改名不被原操作重放覆盖、一次丢回执恢复和刷新自动重连；前端聚焦 69 项、后端 API 36 项及独立 PostgreSQL 回执 11 项通过。正式包重打后另行验证版本和 42 工具 schema。未执行付费生成，积分消耗 0。

剩余限制：客户偶发长时断连根因、系统休眠/后台、多人撤权和真实改价竞态仍需后续验收。本轮真实网页仅测文本与图片改名；其他节点类型有本地覆盖。普通 @显示名不自动猜测素材绑定；音频引用生成、关闭网页或远程无人值守执行仍不支持。

---

# huihui Canvas MCP 0.1.7 release

Adds visible-name reads and `canvas_rename_node` for text, image, video, audio and config nodes. Renaming preserves text, media versions and generation references. Names are trimmed, contain 1–200 characters and may duplicate other names. Free actions retain normal edit permission, lease and node-busy checks.

Ordinary writes retain their original operation IDs and atomic server receipts. Replaying an earlier rename preserves later manual edits. Busy-node responses identify the blocking operation; inspect its original status before retrying. Read authorization errors require restoring the indicated access. Fixes ordinary MCP saves rejected when grouped Web sends schema_version.

Verify the archive against SHA256SUMS-0.1.7 before installation. Node.js 22+, registration huihui-canvas, 42 tools. latest.json selects 0.1.7. Distribution is a GitHub tarball, not an npm publication.

Renaming requires both Web and Canvas Service to advertise node_display_name_v1; an incompatible deployment refuses the write. Package publication does not deploy either service. Supply your authorized signed-in canvas URL and keep the browser, local Bridge and agent on the same computer.

Validation: 8 Bridge tests passed for the final package source. DEV acceptance covered text/image renaming, duplicate and trimmed names, content/version preservation, replay after manual editing, one deliberately lost receipt, and refresh reconnection. Focused checks: Web 69, Backend API 36, dedicated PostgreSQL receipt tests 11. Final tarball version and exact 42-tool schema are verified separately. No paid generation or credit spending.

Intermittent long-duration disconnects, system sleep/background behavior, multi-user revocation and real supplier-price races remain separate acceptance work. Only text/image names were exercised in the live browser this round. Display names do not infer @reference bindings. Audio-reference generation and closed-browser/unattended remote execution remain unsupported.
