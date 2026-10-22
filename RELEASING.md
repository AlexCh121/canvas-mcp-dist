# 更新当前可安装版本

`latest.json` 是公开安装指引使用的稳定入口。它指向仓库中已经提交的一个不可变压缩包和对应版本校验文件；不要把尚未验收的候选包设为当前版本。GitHub 的 `releases/latest` 目前不是这个仓库的安装依据。

1. 将新版本的 `.tgz` 和 `SHA256SUMS-<版本>` 加入仓库，并把相同的校验行追加到总文件 `SHA256SUMS`。不要覆盖旧版本文件。
2. 执行 `python3 scripts/update-latest.py <新压缩包文件名>`。脚本读取包内版本与 CLI 名、核对压缩包 SHA256，然后更新 `latest.json`。
3. 执行 `python3 scripts/update-latest.py --check` 和 `shasum -a 256 -c SHA256SUMS-<版本>`。
4. 新资产和校验文件就绪后，最后更新 `latest.json`，并将这些内容一起合入 `main`。公开 Quickstart 无须改版本号；包名或 CLI 改名后，清单会记录新值。

若新版本修改了配对、状态目录或环境变量，仍需单独更新升级说明并验证旧安装迁移。修改 `latest.json` 不能替代真实部署验收。


## 正式发布与候选版转正

明确获准正式发布时，先核对已发布包与校验，使用 `scripts/update-latest.py` 更新安装指针，将 `release.json` 的 `prerelease` 设为 false，再提交到 main。Actions 校验当前安装指针、下载并核对原 Release 包，随后将其转为正式版本并设为 GitHub Latest。

原 tag、压缩包和校验文件保持不变；转正说明写在 Release 正文，不重打同号压缩包。正式发布状态不能替代生产服务部署或未完成场景的验收，已知限制继续保留。
