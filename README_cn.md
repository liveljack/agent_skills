# Agent Skills 开源项目

本仓库收录了一系列针对 AI Agent 设计的专业领域技能（Skills）。每个 Skill 都整合了该领域的大量经典专著与实战经验，旨在为 Agent 提供深度专业背景，使其能够像专家一样执行任务。

> English version: [README.md](README.md)

## 已收录技能介绍

目前本项目已收录以下 4 个核心技能：

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
*   **定位**：一句话需求 → 可直接出发的定制行程方案（含排版 PDF 交付），属于「付费可调用」的技能。
*   **核心内容**：
    *   **7 大章节强制交付标准**：行程总览、逐日行程（细化到上午/下午/晚间与出发时刻）、城际与市内交通、住宿区域建议、美食推荐、分项预算表、注意事项，正文不少于 800 字。
    *   **执行层细节**：票务与预约写成硬约束（闭馆日、放票时间、无现场售票、儿童身高门槛），并给出雨天/无票/闭馆/疲惫/延误的替代方案与体能兜底（强制休息时段、连续步行上限、提前离园条件）。
    *   **排版 PDF + 邮件交付**：带封面、目录、品牌页脚，约 90 天有效下载链接，同时发送到用户填写的邮箱。
    *   **多语言与个性化**：`country_code`（境内/境外）+ 3 种出行人群 + 11 类主题 + 9 类内容侧重可自由组合；`language` 控制正文语言（PDF 封面与邮件目前为中文）。
    *   **AI 付（HTTP 402 按量付费）**：0.99 元/次（约 0.15 美元），无订阅、无自动续费；付款动作全部交给官方 `alipay-payment-skill` 的 `alipay-bot`，本 Skill 不实现付款与签名。
*   **配套文件**：
    *   [`references/402-travel-flow.md`](xianzong-travel-consultant-aipay/references/402-travel-flow.md)：402 全流程（取账单 → 付款 → 凭支付凭证取资源）。
    *   [`scripts/travel_aipay.mjs`](xianzong-travel-consultant-aipay/scripts/travel_aipay.mjs)：`body` / `probe` / `pay` / `complete` / `render` 子命令，零第三方依赖。
    *   [`tests/`](xianzong-travel-consultant-aipay/tests)：离线测试（`mock_server.mjs` + `run_offline_tests.mjs`），无需联网与付款即可验证全流程。
    *   [`SKILL_cn.md`](xianzong-travel-consultant-aipay/SKILL_cn.md)：中文版技能说明。
*   **运行依赖**：Node.js >= 18 与官方 `alipay-bot`（`@alipay/agent-payment`）；无需 Python 或 pip 包。
*   **推荐场景**：亲子游、带老人出行、团建、出境游、蜜月、研学、康养、周末短途等需要「执行级细节」而非景点清单的行程规划。

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
