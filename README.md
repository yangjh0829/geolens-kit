# GeoLens · 照片地理判读技能包

一个**自包含的 Agent Skill**：给一张照片，按 **26,177 条「线索 → 结论」判读规则**推断拍摄地，并给出可核验的证据链与 L0–L4 置信度。

整合自开源项目 [`xiaoyangtx996/Searching-skill`](https://github.com/xiaoyangtx996/Searching-skill)（网络迷踪判读规则库）与一个薄封装入口 `wlmz-easy`，统一改名为 **geolens**：一个名字、一个入口、完整规则随包附带，不再需要记住 `wlmz` / `wlmz-yun` / `Searching-skill:architecture` 这些内部 id。

---

## 一句话安装

**Windows（PowerShell）**

```powershell
.\install.ps1
```

**macOS / Linux**

```bash
bash install.sh
```

安装到 `~/.workbuddy/skills/geolens/`。WorkBuddy、Claude Code、Cursor、Codex、Gemini CLI 等任何会读 `SKILL.md` 的 agent 都能用。

自检：

```bash
python scripts/check.py
```

## 一句话调用

> **用 geolens 判这张图**：`<图片路径>`

只想查某条规则也可以：

> 按 geolens 的建筑规则看屋顶 / 用云识读规则看这张图的云

## 为什么有「强制流程」

原规则库踩过的坑：AI 自己判断「该加载哪几个领域」，在重庆案例里觉得「黄出租车多城都有」就跳过了区域层，结论停在 L2。所以本项目把防漏层写进 `SKILL.md` 并做成脚本：

| 门禁 | 要求 |
|---|---|
| `geo-sleuth/scripts/sweep.py` | 必须 `覆盖率: 27/27 技能已遍历 ✅`，零命中技能也要在表里 |
| `geo-sleuth/scripts/kb_search.py` | 报 L2+ 前区域层须有命中，或明确写「已搜区域层，0 命中」 |
| 7 个孤岛出口 | 山／船／飞机／火车／星空／密码／可推日期逐条交接 |
| 证据分级 | A 硬事实 / B 权威整理 / C 社区经验 / D 机器推断；**D 级只能当线索** |
| 输出 | 只用 L0–L4 一套档位，禁止与核验层内部档位混写 |

实测（Windows，Python 3.13）：

```
$ python geo-sleuth/scripts/sweep.py 白墙 平顶 竹林 晨雾 河
覆盖率: 27/27 技能已遍历 ✅   有命中 19 个（region 61 / landforms 60 / geo-sleuth 58 …）

$ python geo-sleuth/scripts/kb_search.py 白墙 平顶 徽派 竹林
元素领域命中 14 条，含「白墙黑瓦马头墙 → 指向徽派建筑流行区域」
```

## 包里有什么

| 内容 | 数量 / 路径 |
|---|---|
| 入口技能 | `SKILL.md`（`name: geolens`） |
| 路由表 | `INDEX.md` |
| 元素领域 | 24 个 `<领域>/SKILL.md`（云识读、基建、光影天文、车牌、铁路、建筑、地貌…） |
| 区域层 | `region/`：161+ 国家/省份文件，含 `china/中国通用.md` |
| 核验层 | `geo-sleuth/`：OSM／DEM 天际线／太阳影长／卫星图／街景比对脚本 |
| 强制脚本 | `sweep.py`、`kb_search.py`、`triage.py` |
| 方法论文档 | `docs/证据与置信度框架.md`、`docs/技能互联·产出手册.md` 等 |
| 可选识图服务 | `image-search-mcp/`（Google Lens / Bing / Yandex / 百度，需另行注册） |
| 原始入口存档 | `docs/_original/original-wlmz-SKILL.md`、`original-README.md` |

> 内部子技能的历史 id 仍是 `wlmz-*`，**故意不改**：`INDEX.md`、各领域 `SKILL.md`、`docs/` 里有大量交叉引用，改名会断链。对使用者只需记 `geolens`。

## ⚠️ 来源与许可

本仓库按使用者要求**完整打包**了第三方规则库正文，请务必了解其许可状态：

- **规则正文**（`INDEX.md`、24 个领域、`region/`、`docs/` 等）来自 [`xiaoyangtx996/Searching-skill`](https://github.com/xiaoyangtx996/Searching-skill)。**该上游仓库未附 LICENSE 文件**，法律上默认保留所有权利。
- **核验层** `geo-sleuth/` 来自 [`Oldcircle/geo-sleuth`](https://github.com/Oldcircle/geo-sleuth)，**MIT**，原版权与许可声明保持不变。
- **本仓库原创文件**（`SKILL.md` 的 geolens 入口、`README.md`、`NOTICE.md`、`LICENSE`、`install.*`、`scripts/check.py`）采用 MIT，见 `LICENSE`；该许可**不覆盖**上述第三方内容。

完整清单见 [`NOTICE.md`](NOTICE.md)。如你是相关内容的权利人并希望移除，请开 issue，会尽快处理。

仅供本地个人学习研究使用；不要用于定位未同意被找到的人，也不要用于私人住宅、学校、未成年人日常活动地点。

## 更新规则库

上游更新后，在临时目录 `git clone` 上游仓库，用 `git archive HEAD | tar -x` 导出并覆盖本包的对应目录，然后重新检查 `SKILL.md` 与 `INDEX.md` 是否被覆盖。

## 负责任地使用

只用在你自己的照片、或已获授权分析的照片上。结论必须能对应本次会话真正跑过的命令和产出文件；没跑过的写「未核实」。
