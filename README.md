# Agent Skills 开源项目

本仓库收录了一系列针对 AI Agent 设计的专业领域技能（Skills）。每个 Skill 都整合了该领域的大量经典专著与实战经验，旨在为 Agent 提供深度专业背景，使其能够像专家一样执行任务。

## 已收录技能介绍

目前本项目已收录以下 3 个核心技能：

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

## 如何贡献
欢迎提交新的领域 Skill！请确保您的 Skill：
- 具有清晰的元数据（Name, Description, Tags）。
- 引用了权威的理论来源或经过验证的实战数据。
- 结构清晰，易于 AI 理解。
