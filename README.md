# Agent Skills

A collection of domain-specific skills designed for AI agents. Each skill distills a body of authoritative literature and field-tested practice into a compact instruction set, so an agent can perform that task at expert level instead of giving generic advice.

> 中文版：[README_cn.md](README_cn.md)

## Included Skills

This repository currently ships **4** core skills.

### 1. [Domestic Marketing Compliance](domestic-marketing-compliance/SKILL.md)

*   **What it is**: a "red-line detector" for marketing copy published in the Chinese market.
*   **Core contents**:
    *   **Advertising-law red lines**: banned superlatives ("no. 1", "the best", absolute claims) and prohibited medical-efficacy promises under the PRC Advertising Law.
    *   **Per-platform adaptation**: platform-specific forbidden terms and moderation logic for WeChat, Douyin, Xiaohongshu and similar channels.
    *   **Compliant rewrites**: concrete substitute phrasings for risky terms, so the copy can still be published.
*   **Good for**: WeChat official-account articles, e-commerce product pages, livestream scripts, brand website copy.

### 2. [Video Storyboard Pro](video-storyboard-pro/SKILL.md)

*   **What it is**: a "director's brain" that turns a written script into cinematic shot-by-shot storyboards.
*   **Core contents**:
    *   **Theory from master texts**: synthesizes 17 classic film and animation storyboard works (e.g. Steven D. Katz, *Film Directing Shot by Shot*).
    *   **End-to-end workflow**: content analysis (3A framework), shot-language design, character and asset sheets, and image-generation parameter output.
    *   **AI-tool adaptation**: prompt structures tuned for text-to-image generation.
*   **Good for**: short-video production, commercial advertising planning, animation storyboard development.

### 3. [Viral Copywriting](viral-copywriting/SKILL.md)

*   **What it is**: a "gold-medal copywriter" focused on traffic and conversion.
*   **Core contents**:
    *   **Classic formula library**: draws on 50+ marketing classics, covering AIDA, PAS, FAB, 4P and other core writing frameworks.
    *   **Viral patterns**: six persuasion principles, reusable headline templates, and the five headline formulas popularised by Lü Bai.
    *   **Topic-specific deep dive**: a dedicated **Xiaohongshu** playbook ([xiaohongshu-guide.md](viral-copywriting/references/xiaohongshu-guide.md)).
*   **Good for**: building new social accounts, marketing soft articles, lead-generation copy, personal brand building.

### 4. [Xianzong Travel Consultant AIPay](xianzong-travel-consultant-aipay/SKILL.md)

*   **What it is**: one line of requirements becomes an execution-ready custom itinerary with typeset PDF delivery — a **paid, pay-per-use** skill.
*   **Core contents**:
    *   **7 mandatory delivery sections**: trip overview, day-by-day schedule (down to morning/afternoon/evening and departure times), intercity and local transport, lodging-area advice, food recommendations, itemized budget, and important cautions — at least 800 characters of body text.
    *   **Execution-level detail**: ticketing and reservations written as hard constraints (closure days, ticket-release windows, no on-site sales, child height limits), plus concrete fallbacks for rain, sold-out tickets, closures, fatigue and delays, with stamina guards (mandatory rest windows, continuous-walking caps, early-exit conditions).
    *   **Typeset PDF + email delivery**: cover page, table of contents, branded footer, an ~90-day download link, and the PDF emailed to the address the user provides.
    *   **Personalization and language**: `country_code` (domestic / overseas) combined freely with 3 traveller types, 11 themes and 9 content focuses; `language` controls the answer body (PDF cover labels and the delivery email are currently Chinese only).
    *   **Alipay AI pay-per-use (HTTP 402)**: CNY 0.99 per call (approx USD 0.15), no subscription and no auto-renewal; all payment actions are delegated to the official `alipay-payment-skill` / `alipay-bot`, and this skill never implements payment or signing.
*   **Bundled files**:
    *   [`references/402-travel-flow.md`](xianzong-travel-consultant-aipay/references/402-travel-flow.md): the full 402 flow (obtain bill → pay → retrieve the resource with the payment proof).
    *   [`scripts/travel_aipay.mjs`](xianzong-travel-consultant-aipay/scripts/travel_aipay.mjs): `body` / `probe` / `pay` / `complete` / `render` subcommands, zero third-party dependencies.
    *   [`tests/`](xianzong-travel-consultant-aipay/tests): offline tests (`mock_server.mjs` + `run_offline_tests.mjs`) that exercise the whole flow without network access or real payment.
    *   [`SKILL_cn.md`](xianzong-travel-consultant-aipay/SKILL_cn.md): the Chinese edition of the skill instructions.
*   **Runtime requirements**: Node.js >= 18 and the official `alipay-bot` (`@alipay/agent-payment`); no Python or pip packages needed.
*   **Good for**: family trips with kids, travelling with elderly parents, team building, outbound travel, honeymoons, study travel, wellness trips, weekend getaways — any trip that needs execution-level detail rather than a list of attractions.

---

## Installation

### Option 1: Clone the repository (recommended)

Clone this repository if you want to use the skills locally or extend them:

```bash
git clone https://github.com/[your-username]/agent_skills.git
```

### Option 2: Manual integration

1. Open the skill directory you need (e.g. `video-storyboard-pro/`).
2. Copy the contents of `SKILL.md` into your agent's system prompt or configuration file.
3. If the skill ships a `references/` directory, load the relevant reference files as well for the best results.

### Option 3: VS Code agent integration

If you use a VS Code extension that loads local skills (for example GitHub Copilot custom instructions):

1. Add the absolute path of this repository to your agent's skill search locations.
2. Activate a skill in chat (e.g. `@agent load domestic-marketing-compliance`).

> **Note**: VS Code does not scan arbitrary directories by default — declare the skill directory through `chat.agentSkillsLocations` in `.vscode/settings.json`. In addition, a skill's `name` must exactly match its directory name (lowercase letters, digits and hyphens only), as in `xianzong-travel-aipay`.

### Verifying the paid skill offline

The travel-consultant skill ships a mock server, so you can validate the full 402 flow without network access or a real payment:

```bash
cd xianzong-travel-consultant-aipay
node tests/run_offline_tests.mjs
```

## Contributing

New domain skills are welcome. Please make sure your skill:

- Has clear metadata (name, description, tags).
- Cites authoritative sources or verified, field-tested data.
- Is structured so an agent can follow it directly.
- Has a directory name identical to the `name` field in `SKILL.md`.
- Ships offline-runnable tests if it contains executable scripts (see `xianzong-travel-consultant-aipay/tests/`), so users can verify the flow without paying or going online.

## License

See [LICENSE](LICENSE).

