# 来源与许可声明

本仓库为个人整合包，包含三部分内容，许可状态不同。**请勿把 `LICENSE` 里的 MIT 理解为覆盖全仓库。**

## 1. 规则库正文（第三方，上游未附许可证）

- 来源：<https://github.com/xiaoyangtx996/Searching-skill>（项目名「Searching-skill · 网络迷踪判读规则库」，技能 id `wlmz`）
- 上游快照 commit：`1d7e4d8`（2026-10-04），经 `git archive HEAD` 导出
- 包含：`INDEX.md`、24 个 `<领域>/SKILL.md` 及 references、`region/`（161+ 国家/省份线索文件）、`docs/`（证据框架、技能互联手册、原始 README 与原始 `wlmz` 总技能存档）、`assets/`
- 规模：约 **26,177 条**「线索 → 结论」规则（上游 README 口径：元素层 2,807 + 区域层 23,370）
- **许可状态：上游仓库没有 LICENSE / NOTICE 文件**，默认「保留所有权利」。本仓库按使用者明确要求完整打包以便一键使用；如权利人有异议，请开 issue，将立即移除。
- 上游 README 自述：线索多为倾向性规律，需至少两条独立线索互证；图片未随包分发。

## 2. 核验层 `geo-sleuth/`（MIT）

- 来源：<https://github.com/Oldcircle/geo-sleuth>
- 许可证：**MIT**（上游 `LICENSE`）
- 包含：`geo-sleuth/SKILL.md`、`geo-sleuth/scripts/`（sweep.py / kb_search.py / triage.py / sun.py / board.py / terrain.py 等）、`geo-sleuth/references/`、`geo-sleuth/data/`
- 说明：这是 `wlmz` 规则库内嵌的核验层副本，与用户可能单独安装的市场版 `geo-sleuth` v2.0.2 并非同一份；本包不覆盖后者。
- 上游方法说明（README）：「方法来自拆解网络定位博主的 14 个视频、22 道题和一批实战记录」，不公开博主名单。
- 数据致谢（上游）：OpenStreetMap 贡献者（ODbL）、AWS Terrain Tiles、modood/Administrative-divisions-of-China、DINOv2（Meta AI）、CLIP（OpenAI）；`data/` 中源自维基百科的表格为 CC BY-SA 4.0。

## 3. 可选识图服务 `image-search-mcp/`（Node）

- 属于上游规则库自带组件，未注册、默认不启用；以图搜图用 Playwright 驱动 Google Lens / Bing / Yandex / 百度
- 依赖 `@modelcontextprotocol/sdk`、`playwright`（各自的包许可证见其 npm 页面）
- 单独使用时需自行 `npm install && npx playwright install chromium` 并在对应 agent 的 MCP 配置里注册

## 4. 本仓库原创部分（MIT）

以下文件由本整合包新写，采用 `LICENSE` 中的 MIT：

- `SKILL.md`（`name: geolens` 的完整入口与流程）
- `README.md`、`NOTICE.md`（本文件）、`LICENSE`
- `install.ps1`、`install.sh`、`scripts/check.py`、`.gitignore`
- `docs/_original/` 中两份上游文件为**存档**，许可按第 1 条处理

## 其他

- 规则中引用的 WMO《国际云图》、图寻语雀文档、Plonk It 汉化等第三方资料，版权归各自权利人。
- 本包仅用于本人照片或已获授权的照片，勿用于定位未同意被找到的人。
