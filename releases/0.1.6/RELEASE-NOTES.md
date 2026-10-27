# huihui Canvas MCP 0.1.6 预发布说明

使用你已获授权的画布 URL，登录并打开自己的画布，保持本机 Bridge 运行完成配对。

本版本修复已确认的连接恢复、上传和批量保存问题，建议先受控灰度；客户偶发断连根因仍在追踪，不能理解为所有断连已根治。本次先公开发布本机安装包；配套 Canvas Service 和 Canvas Web 的生产部署由同批发布负责人执行。默认安装指针暂时保留 0.1.5，生产部署验收后再切换。

- 连接归页面持有，收起面板不断开；续期/恢复具备预算、退避、单飞、原请求幂等和脱敏诊断。
- 闲置释放编辑权后，免费写入按既有流程取得空闲租约；草稿冲突和其他编辑者保持保护。
- 已受理上传独立于消息流；回执丢失按原身份核对，已上传只补导入。完成上传仍待补媒体信息时可查询原操作继续补原素材版本，不重传字节。
- 新增 save-only 批量配方/固定版本引用/逐项回执/revision 快照；临时保存错误沿同一推进请求有界重试。长文本使用 Unicode 分页与 hash 验证完整性；保存不生成、不扣费。

DEV 证据：上传中重启 Bridge 后 20 项全完成、元信息 20/20 ready，每项 attempt=1；原 154 项/960 固定引用完成、原 ID 重放无重复，5,400 码点长文三页 hash 一致；丢已提交回执同请求重放无重复；闲置新写自动恢复；普通网页上传通过。自动化包含专用真 PG 42 项、Web 57 项、Bridge 7 项，安装包 fresh SDK 为 huihui-canvas/41 工具/schema 一致。本轮无生成或积分消耗。

仍需跟进：客户偶发断连真实时间线/长稳/系统休眠；真人撤权及供应商真实改价竞态；原客户缺图清单逐镜核对。音频参考生成、自然 @显示名称猜绑定、关闭网页/远程无人值守不支持；实际模型输入仍按能力和报价校验。外部代理、浏览器系统挂起及不支持格式保持明确限制。

先部署匹配 Canvas Service/Canvas Web，再分发本机 0.1.6；主线 d13→d14 与 DEV d16 不可互换。公开安装说明不列具体 DEV 域名。源码和验证边界见[发布记录](https://github.com/AlexCh121/canvas-mcp-dist/blob/main/releases/0.1.6/RELEASE-MANIFEST.json)。下载本 Release 的 tgz 与 SHA256SUMS-0.1.6 后，执行 shasum -a 256 -c SHA256SUMS-0.1.6。

---

# huihui Canvas MCP 0.1.6 prerelease

Use your authorized Canvas URL. Sign in, open your canvas and keep the local Bridge running for pairing.

This prerelease fixes confirmed upload, idle-write and batch-save failures. Use a controlled rollout; reported intermittent disconnects remain under investigation. This release publishes the local package first. Matching Canvas Service/Web production deployment is coordinated separately. latest.json remains at 0.1.5 until that rollout is accepted.

Page-owned connections survive closing the assistant panel. Renewal and resume use bounded, idempotent recovery. Idle writes acquire an available edit lease without overwriting drafts or taking another editor's lease. Accepted uploads are independent of the message stream; confirmed objects are not retransmitted. Querying the original operation can repair missing metadata on its original media version while preserving the committed import. Save-only graph plans provide fixed references, durable item receipts and revision-bound Unicode/hash snapshots; transient advances replay the same request.

DEV verification: 20 mixed uploads completed across a Bridge restart, all metadata ready, one transfer attempt per item; the original 154-item plan with 960 fixed references completed without duplicate nodes; 5,400 Unicode code points read back across three pages with matching hash; a committed response was deliberately lost and the identical advance replayed safely. Idle-write recovery and normal browser upload also passed. Focused tests: Backend PostgreSQL 42, Web 57, Bridge 7; fresh tarball SDK reports huihui-canvas, version 0.1.6 and the exact 41-tool schema. No generation or credit spending occurred.

Real intermittent-disconnect timelines, system sleep, real permission revocation, supplier-price races and the customer's full missing-reference checklist are not certified by these tests. Audio-reference generation, display-name guessing, closed-browser and unattended remote execution remain unsupported. Model inputs still require capability validation, quotes and paid confirmation.

Deploy matching Canvas Service/Web first, then distribute 0.1.6. Production migration d13-to-d14 and DEV d16 are distinct. Verify SHA256SUMS-0.1.6 and consult the [release manifest](https://github.com/AlexCh121/canvas-mcp-dist/blob/main/releases/0.1.6/RELEASE-MANIFEST.json) and the installation instructions.
