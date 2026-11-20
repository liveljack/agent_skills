---
name: xianzong-travel-aipay
version: "1.4.1"
display_name: "仙踪问道 · 旅行咨询"
display_name_en: "Xianzong Wendao · Travel Consultation"
description_zh: "根据目的地、人数、预算和偏好生成逐日旅行方案及分项预算，并提供交通住宿建议。支持中英文交付和排版 PDF。"
description_en: "Create a day-by-day travel plan and itemized budget from destination, party, budget, and preferences, with transport and lodging advice and typeset PDF delivery."
description: >-
  根据目的地、出行日期、人数、预算和偏好生成逐日旅行方案、交通住宿建议、分项预算及排版 PDF。
  当用户需要旅行行程规划、亲子游、老人游、自由行、团建或境外出行安排时使用。
  产出：逐日行程、预算表、注意事项和 PDF 下载链接。
allowed-tools: Bash(node:*), Bash(alipay-bot:*)
metadata:
  version: "1.4.1"
  category: travel
  openclaw:
    category: travel
    requires:
      env: []
      bins: ["node"]
      anyBins: ["alipay-bot"]
      node: ">=18"
    install:
      - kind: node
        package: "@alipay/agent-payment@1.0.31"
        bins: [alipay-bot]
        integrity: "sha512-+bMtwDsJdpuKMxf2nIAA2n0Sm3yxGIBX24LhfjhHGA0lCLTbxkMJvVLglXd99FPGETVl3k9Y7Rx+CTnswGHcrQ=="
  permissions:
    network:
      - "https://api.riyuexinzhu.com"
    filesystem:
      - "~/.xianzong-travel-aipay"
---

# 仙踪问道 · 旅行咨询

本 Skill 根据目的地、出行日期、同行人数、预算和偏好，生成可读的逐日旅行方案。交付内容包括旅行行程正文、交通住宿建议、分项预算、注意事项和排版 PDF。

方案会标注无法核实时效信息，不会把未核实的票价、开放时间或预约规则写成确定事实。具体票务、班次、开放时间和政策应以官方渠道核实为准。

## 能力范围

适用场景包括：

- 国内或境外城市的 2 至 14 天行程规划；
- 亲子游、老人同行、团建和休闲度假；
- 交通衔接、住宿区域、餐饮偏好和预算估算；
- 中文、英文、日文、韩文和法文交付；
- 行程突发变化时的替代安排建议。

本 Skill 不提供实时订票、代订酒店、签证代办、代付款、实时救助或旅行社资质以外的代办服务。

## 交付内容

| 内容 | 说明 |
|---|---|
| 行程正文 | 按天列出景点、时段、交通衔接、休息安排和用餐建议 |
| 预算表 | 按交通、住宿、餐饮、门票等项目列示估算，可按人数和晚数核算 |
| 注意事项 | 列出同行人差异、预约要求、季节影响和待核实事项 |
| PDF | 排版 PDF，下载链接通常有约 90 天有效期，成功交付时也发送到填写的邮箱 |
| 参考资料 | 可附目的地景点、交通、住宿、美食等检索摘要 |

一次咨询聚焦一个行程。如日期、人数或预算发生明显变化，应重新提交咨询要素。

## 使用方式

一次请求应包含目的地、天数或日期、同行人数、预算范围和出行偏好。邮箱用于接收 PDF。

示例：

> 帮我规划杭州三日亲子游，2 名成人、1 名 6 岁儿童，预算 5000 元以内，希望少走路。

示例：

> 请用英文规划北京四日三晚家庭行程，2 名成人、1 名 8 岁儿童，预算约 8000 元，包含熊猫或动物主题活动。

输入越具体，方案越容易对齐实际约束。但用户未提供的信息会按通用假设处理，不会自动获取私人日历、航班或账户信息。

## 付款与交付

当前服务按次计价。实际金额以接口下发账单为准；计费方式为按次结算，不订阅、不自动续费。

1. Agent 校验 `query` 与 `email`；参数错误时不产生账单。
2. 付款前向用户说明行程需求和邮箱将发送到指定官方服务，用于账单生成与方案交付。
3. 用户确认后，调用官方支付工具完成支付确认和查单。
4. 使用原订单、原请求体和原资源地址取回方案。
5. 展示正文、PDF 链接和必要的核实说明，不重复扣费。

未经用户明确确认，不执行付款命令。状态不明确时先查原订单，不重新付款。

## 遇到问题

| 情况 | 处理方式 |
|---|---|
| 返回账单但尚未付款 | 等待用户在官方支付入口确认，不重复取账单 |
| 已付款且资源正在生成 | 使用同一订单稍后查询，不重新付款 |
| 参数被拒，HTTP 400 | 补齐目的地、日期、人数、预算或邮箱后重试；通常未扣费 |
| 凭证失效，带凭证后返回 402 | 核对官方账单与订单状态，再决定下一步 |
| 服务端 5xx 或瞬时不可用 | 同一订单允许有限重试，不替换请求内容 |
| 业务返回失败且 HTTP 为 200 | 原样报告业务原因，不继续支付或交付重复结果 |
| PDF 链接生成失败 | 正文仍可使用；重新咨询前先确认是否需要再次计费 |

已成功交付的订单不重复计费。PDF 链接如临近或超过有效期，可重新发起咨询。

## 数据与隐私

发起查询时，会把以下字段发送到旅行咨询官方服务：

- 行程需求 `query`；
- 接收 PDF 的邮箱 `email`；
- 用户选择的语言、地区、同行和主题参数。

该数据用于生成账单、校验支付、生成方案、发送 PDF 和履约核对。邮箱主要用于本次方案交付，状态文件和支付凭证保存在用户本机，不回显到对话正文。

付款前必须披露：行程需求和邮箱会发送到 `https://api.riyuexinzhu.com/aipay/travel_consultant`，用于生成账单及付款后交付方案。未经披露不得静默发送。

---

# Agent 执行说明

## 工作域

使用本 Skill 的典型任务包括旅行行程规划、旅游攻略、亲子游、老人游、团建行程、境外出行安排和排版 PDF 行程方案。

如果只是执行通用付款、买单或查询账单，不属于本 Skill，应移交官方支付能力。

## 职责边界

本 Skill 负责：

1. 收集并校验行程要素与邮箱；
2. 组装请求并取出账单；
3. 等待用户确认；
4. 调用官方支付与查单能力；
5. 使用同一订单取资源并展示交付结果。

本 Skill 不自行构造支付宝签名、不伪造支付凭证、不改造 `Payment-Needed`、不自行发起履约回执，也不绕过服务端验付。

## 请求契约

资源地址：`POST https://api.riyuexinzhu.com/aipay/travel_consultant`

请求头：`Content-Type: application/json`。携带支付凭证取货时，`Payment-Proof` 只能来自官方支付工具。

| 字段 | 必填 | 说明 |
|---|---|---|
| `query` | 是 | 行程需求，建议包含目的地、天数、同行人、预算、节奏和偏好 |
| `email` | 是 | 接收 PDF 的邮箱；格式非法时不创建账单 |
| `language` | Agent 调用时强制传入 | `zh`、`en`、`ja`、`ko`、`fr`；未明确语言时使用 `zh` |
| `country_code` | 否 | ISO 3166-1 alpha-2，如 `CN`、`IT`、`JP` |
| `intro_type` | 否 | 0 全部，1 城市地理，2 景点，3 美食，4 购物，5 交通，6 住宿，7 游玩攻略，8 历史文化 |
| `topic_type` | 否 | 0 全部，1 户外探险，2 文化历史，3 自然风光，4 美食购物，5 城市观光，6 研学教育，7 亲子游玩，8 康养休闲，9 人文胜迹，10 纪念场馆 |
| `is_group_suitable` | 否 | 1 是，0 否 |
| `is_family_suitable` | 否 | 1 是，0 否 |
| `is_leisure` | 否 | 1 是，0 否 |
| `is_with_ref` | 否 | 1 返回参考资料，默认；0 不返回 |
| `options` | 否 | 扩展字段，可覆盖同名字段 |

空 `query` 或非法 `email` 应在取账单前被拒绝，不产生账单。

## 调用方法

使用相对 Skill 目录的脚本：

```bash
SKILL_DIR=skills/aipay/xianzong-travel-aipay

node "$SKILL_DIR/scripts/travel_aipay.mjs" body \
  --query '杭州三日亲子游，2 大 1 小，预算 5000 元以内' \
  --email buyer@example.com --language zh

node "$SKILL_DIR/scripts/travel_aipay.mjs" probe \
  --query '杭州三日亲子游，2 大 1 小，预算 5000 元以内' \
  --email buyer@example.com --country-code CN --topic-type 7 \
  --is-family-suitable 1 --language zh

node "$SKILL_DIR/scripts/travel_aipay.mjs" pay --confirm --session-id '<当前会话标识>'

node "$SKILL_DIR/scripts/travel_aipay.mjs" complete --wait \
  --state-dir '~/.xianzong-travel-aipay'
```

子命令语义：

- `body`：组装并校验请求体，不发送网络请求；
- `probe`：发送未付款请求并保存账单载体；
- `pay`：调用官方支付工具，必须带 `--confirm`；
- `complete`：支付后取资源，可用 `--wait` 自动轮询；
- `render`：渲染已保存的交付响应。

## 状态与退出码

| 状态 | 含义 | 退出码 | 下一步 |
|---|---|---|---|
| 402 + Payment-Needed | 待支付账单已生成 | 0 | 等用户确认后执行 `pay --confirm` |
| 200 | 资源交付成功或幂等重放 | 0 | 展示结果，不追加回执 |
| 409 + Retry-After | 已付款，资源仍在生成 | 3 | 使用同一订单稍后查询，不重新付款 |
| 业务失败且 HTTP 200 | 已验付但业务未成功 | 4 | 原样报告，不重试、不重复付款 |
| 402 携凭证重发 | 支付凭证无效或过期 | 5 | 核对官方账单，不直接引导二次付款 |
| 400 | 参数被拒绝 | 2 | 修正参数后重发；未扣费 |
| 5xx | 服务端错误 | 6 | 网络类错误可有限重试一次 |

## 判读规则

成功交付以官方查询载荷和资源响应为准：查到 `success: true`、`resourceResponse.status: 200` 和正文内容时展示结果，不用 `resourceDelivered` 判断成功。

遇到 HTTP 409 时，按 `Retry-After` 后使用同一商户订单或支付交易号再次查询。不要把商户订单号传给交易号参数，也不要新建账单。

已履约但重复查询出现瞬时 402 时，先核对官方支付与订单状态，再按同一订单稍后重试，不重新付款。

## 执行流程

1. 收集 `query`、`email` 和 `language`；缺邮箱时停止并询问，不编造。
2. 执行 `body` 做本地校验，确认请求字段与语言。
3. 在执行 `probe` 前，明确披露行程需求和邮箱将发送到指定官方服务，用于账单生成和付款后交付。
4. 展示账单中的支付入口、商品名、金额和订单号；未经用户明确确认，不执行 `pay --confirm`。
5. 付款后用原订单和原请求体查询；409 按时间间隔重试，禁止重新付款。
6. 展示正文与完整 PDF 链接；不展示成本、内部计费字段或支付凭证。

## 知识库与核实边界

行程方案应区分已核实、待核实和无法核实的信息：

- 已核实：写明具体值、来源站点和核实日期；
- 待核实：保留官方渠道提示，不写成确定事实；
- 无法核实：说明未能核实，不补造价格或政策。

票价、开放时间、预约规则、交通班次和现场政策可能随时变化，以官方渠道最新公示为准。

## 安全边界

- 只调用已配置的旅行咨询资源地址，不修改生产配置或生产数据；
- 付款、查单和履约只走固定版本官方支付工具；
- 不读取系统凭据、不扫描家目录、不发送遥测；
- 支付凭证只落在本机私有状态目录，不回显、不提交到版本库；
- 不把商户订单号与支付宝交易号混用；
- 不生成或伪造官方支付工具之外的支付入口或签名；
- 不承诺实时准确、全部官方核验或不需要用户复核。

## 文件清单

| 路径 | 用途 |
|---|---|
| `SKILL_strict_cn.md` | 千问等严格审核平台的中文发布入口 |
| `scripts/travel_aipay.mjs` | 请求校验、账单、支付编排、取货与渲染 |
| `scripts/pack.sh` | 白名单打包，可选择中文一般版、严格中文审核版或英文版 |
| `references/402-travel-flow.md` | 402 流程和载荷判读 |
| `references/install-and-pack.md` | 安装、运行和打包说明 |
