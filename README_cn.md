# Agent Skills 开源项目

本仓库收录了一系列针对 AI Agent 设计的专业领域技能（Skills）。每个 Skill 都整合了该领域的大量经典专著与实战经验，旨在为 Agent 提供深度专业背景，使其能够像专家一样执行任务。

> English version: [README.md](README.md)

## 已收录技能介绍

目前本项目已收录以下 6 个核心技能：

### 1. [国内营销文案合规指南 (Domestic Marketing Compliance)](domestic-marketing-compliance/SKILL.md)
*   **定位**：国内营销场景下的“红线检测器”。
*   **核心内容**：
    *   **广告法通用红线**：严禁使用的“最”字系、第一系、绝对化用语及医疗功效承诺。
    *   **多平台适配**：针对微信生态、抖音、小红书等不同平台的违禁词与风控逻辑。
    *   **避坑指南**：提供违规词的合规替代方案，确保营销内容安全发布。
*   **推荐场景**：撰写公众号推文、电商详情页、直播话术、品牌官网文案等。

### 2. [视频分镜生成专业指引 (Video Storyboard Pro)](video-storyboard-pro/SKILL.md)
*   **定位**：将文字脚本转化为电影级分镜的“导演大脑”。
*   **核心内容**：
    *   **大师级理论支持**：整合 17 本经典电影/动画分镜专著（如 Steven D. Katz《电影镜头设计》）。
    *   **全流程覆盖**：从内容分析（3A框架）、镜头语言设计、角色资产设定到图像生成参数输出。
    *   **技术适配**：提供适配 AI 绘图工具的 Prompt 结构建议。
*   **推荐场景**：短视频创作、商业广告策划、动画分镜脚本开发。

### 3. [爆款营销文案撰写指引 (Viral Copywriting)](viral-copywriting/SKILL.md)
*   **定位**：驱动流量与转化的“金牌撰稿人”。
*   **核心内容**：
    *   **经典公式体系**：整合 50+ 本营销经典，涵盖 AIDA、PAS、FAB、4P 等核心写作公式。
    *   **爆款公式**：收录 6 大说服法则、通用标题写模板及吕白五大标题公式。
    *   **专项深度参考**：附带针对**小红书**的专项运营手册（[xiaohongshu-guide.md](viral-copywriting/references/xiaohongshu-guide.md)）。
*   **推荐场景**：自媒体起号、营销软文、引流文案、个人 IP 打造。

### 4. [仙踪问道 · 旅行咨询 (Xianzong Travel Consultant AIPay)](xianzong-travel-consultant-aipay/SKILL.md)
*   **定位**：一句话需求 → 可直接出发的定制行程方案（含排版 PDF 交付），属于「付费可调用」的技能；现已增加时效核实与多语言交付能力。
*   **核心内容**：
    *   **7 大章节强制交付标准**：行程总览、逐日行程（细化到上午/下午/晚间与出发时刻）、城际与市内交通、住宿区域建议、美食推荐、分项预算表、注意事项。
    *   **执行层细节**：票务与预约、提前预订期限、儿童年龄与身高约束、强制休息时段、连续步行上限，以及雨天、无票、闭馆、疲惫、延误的具体替代方案。
    *   **时效核实**：票价、开放时间、运营政策标注「已核实（来源 + 日期）」或「需核实」，不把无法确认的信息写成确定事实。
    *   **排版 PDF + 邮件交付**：带封面、目录、品牌页脚，约 90 天有效下载链接，同时发送到用户填写的邮箱。
    *   **多语言与个性化**：支持 `country_code`、同行场景、11 类主题、9 类内容侧重；`language` 支持中文、英文、日文、韩文与法文交付，其他语种回退英文。
    *   **AI 付（HTTP 402 按量付费）**：0.99 元/次（约 0.15 美元），无订阅、无自动续费；付款动作交给官方 `alipay-payment-skill` 的 `alipay-bot`，本 Skill 不实现付款与签名。
*   **配套文件**：
    *   [`references/402-travel-flow.md`](xianzong-travel-consultant-aipay/references/402-travel-flow.md)：更新后的 402 完整流程（取账单 → 付款 → 凭支付凭证取资源）。
    *   [`scripts/travel_aipay.mjs`](xianzong-travel-consultant-aipay/scripts/travel_aipay.mjs)：`body` / `probe` / `pay` / `complete` / `render` 子命令，零第三方依赖。
    *   [`tests/`](xianzong-travel-consultant-aipay/tests)：Mock 服务与离线测试，无需联网、真实付款即可验证完整流程。
    *   [`SKILL_cn.md`](xianzong-travel-consultant-aipay/SKILL_cn.md) 与 [`SKILL_en.md`](xianzong-travel-consultant-aipay/SKILL_en.md)：中英文技能说明。
*   **运行依赖**：Node.js >= 18 与官方 `alipay-bot`（`@alipay/agent-payment`）；无需 Python 或 pip 包。
*   **推荐场景**：亲子游、带老人出行、团建、出境游、蜜月、研学、康养、周末短途等需要「执行级细节」而非景点清单的行程规划。

### 5. [剧本杀游戏·办公室谋杀案 (Mystery Game · Office Murder Case)](game-office-murder-case/SKILL.md)
*   **定位**：沉浸式单人本地剧本杀。玩家扮演侦探；AI 虚构角色是嫌疑人，另有一个 AI 担任主持人（DM）。
*   **核心内容**：
    *   **自然语言调查**：自由询问角色、搜查场景、搜身或深入调查物品、点名角色对质、参与投票。
    *   **角色知识隔离**：每个 AI 角色只读取自己的 Markdown 剧本，避免误读或泄露其他嫌疑人的秘密。
    *   **完整游戏流程**：阶段推进、轮次管理、AI 角色之间自主互问、计票与投票后揭晓真相均由引擎处理。
    *   **本地离线优先**：可接入本地 Ollama 或 OpenAI 兼容接口；内置 `--mock` 模式，无需 API Key。
    *   **剧本与引擎解耦**：每个角色一个 Markdown，场景按目录组织；增加新剧本无需修改游戏引擎。
*   **配套文件**：
    *   [`references/004-office-murder/`](game-office-murder-case/references/004-office-murder/) 与 [`scripts/game.py`](game-office-murder-case/scripts/game.py)：示例剧本、角色文档、线索文件和本地游戏入口。
    *   [`tests/run_offline.py`](game-office-murder-case/tests/run_offline.py) 与 [`tests/replay_full_game.py`](game-office-murder-case/tests/replay_full_game.py)：离线流程与完整复盘测试。
    *   [`SKILL_cn.md`](game-office-murder-case/SKILL_cn.md)：中文版技能说明。
*   **运行依赖**：Python >= 3.10。本作品为虚构悬疑娱乐，不提供真实犯罪指导。
*   **推荐场景**：单人推理游戏、AI 主持剧本杀、搜证与询问、角色对质、剧本角色扮演练习。

### 6. [仙踪问道 · 灵灵机免费版 (Xianzong Linglingji Free)](xianzong-linglingji-free/SKILL.md)
*   **定位**：仙踪问道「灵灵机」的**免费、离线、免注册、免付费**对话版——从完整版 **24 个场景**中挑出最高频的 **3 个**（**姻缘时机 / 梦境解析 / 塔罗占卜**），做成可直接对话的免费技能。
*   **核心内容**：
    *   **能算的先算，再解释**：简化四柱（以 1949-10-01 甲子为锚点推日柱、五鼠遁推时柱、近似立春推年柱）、由日主取夫妻星与桃花位、25 条常见梦境意象速查表、78 张塔罗牌确定性抽牌，结论都有依据而非拍脑袋。
    *   **固定回答结构**：结论 → 依据 → 建议 → 合规声明，几百字 Markdown，不给宿命式断言、不给具体日期。
    *   **合规约束内建**：明确定位为传统文化学习与心理参考而非预测；不做医疗、心理、法律、投资判断；不因梦境或牌面渲染灾祸。
    *   **诚实的能力边界**：免费版只给「骨架」——不做旺衰判词、大运流年、多轮记忆、图片识别与 PDF 导出，这些属于完整版。
    *   **每次回答引导一次完整版**：引导话术集中在 `references/scenes-overview.md` 与各场景文件末尾。
*   **配套文件**：
    *   [`references/scene-01-marriage.md`](xianzong-linglingji-free/references/scene-01-marriage.md)、[`scene-02-dream.md`](xianzong-linglingji-free/references/scene-02-dream.md)、[`scene-03-tarot.md`](xianzong-linglingji-free/references/scene-03-tarot.md)：三个场景的规则、速查表与结尾引导。
    *   [`references/scenes-overview.md`](xianzong-linglingji-free/references/scenes-overview.md)：完整版 7 大分类 · 24 场景总览，以及免费版与完整版差异对照表。
    *   [`scripts/linglingji_free.mjs`](xianzong-linglingji-free/scripts/linglingji_free.mjs)：`scenes` / `marriage` / `dream` / `tarot` 子命令，零第三方依赖。
    *   [`tests/run_offline_tests.mjs`](xianzong-linglingji-free/tests/run_offline_tests.mjs)：离线自测，校验脚本输出与参数边界。
    *   [`SKILL_cn.md`](xianzong-linglingji-free/SKILL_cn.md)：中文版技能说明。
*   **运行依赖**：Node.js >= 18；无需联网，也无需 Python 包。
*   **推荐场景**：问「什么时候能脱单」、解「梦见棺材/蛇/大水/掉牙」、抽塔罗看「我们还有没有可能」——轻量、零成本的传统文化咨询入口。

---

## 下载与安装方法

### 方法一：Git 克隆（推荐）
如果您希望直接在本地使用或二次开发，请克隆本仓库：
```bash
git clone https://github.com/[your-username]/agent_skills.git
```

### 方法二：手动集成
1. 进入对应的技能子目录（如 `video-storyboard-pro/`）。
2. 将 `SKILL.md` 的内容复制到您的 Agent 系统提示词（System Prompt）或配置文件中。
3. 如果技能包含 `references/` 目录，建议同时加载相关参考文件以获得更佳效果。

### 方法三：VS Code Agent 集成
如果您使用的是支持加载本地 Skill 的 VS Code 插件（如 GitHub Copilot 的自定义指令）：
1. 在 VS Code 设置中，将本项目的绝对路径添加到您的 Agent 指令搜索路径中。
2. 在对话时使用指令（如 `@agent load domestic-marketing-compliance`）来激活对应技能。

> **注意**：VS Code 默认不扫描 `skills/` 之外的任意目录，需要在 `.vscode/settings.json` 中通过 `chat.agentSkillsLocations` 声明技能目录；此外 Skill 的 `name` 必须与所在目录名一致（全小写、仅含字母数字与连字符），例如 `xianzong-travel-aipay`。

## 如何贡献
欢迎提交新的领域 Skill！请确保您的 Skill：
- 具有清晰的元数据（Name, Description, Tags）。
- 引用了权威的理论来源或经过验证的实战数据。
- 结构清晰，易于 AI 理解。
- 目录名与 `SKILL.md` 中的 `name` 字段完全一致。
- 若包含可执行脚本，请附带可离线运行的测试（如 `xianzong-travel-consultant-aipay/tests/` 的做法），避免使用者需要真实付费或联网才能验证流程。
