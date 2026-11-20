#!/usr/bin/env python3
"""完整对局的复现脚本：跑一整局，并在每一步记录「文件状态」。

回答两个问题：
  1. 一局能不能从头走到结算？
  2. 过程中到底有哪些文件变了？

用法
----
    python tests/replay_full_game.py --mock            # 离线、秒级
    python tests/replay_full_game.py                   # 真实模型，约 3 分钟
    python tests/replay_full_game.py --state <自定义状态文件>

每次跑完会输出：
  · 每一步的动作、回复摘要、阶段/轮次
  · 状态文件（默认 `~/.jubensha/game-office-murder-case/test_state.json`）的大小与 mtime
  · `references/` 的哈希（必须不变）
  · 结算结果
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import load_script  # noqa: E402
from game import Err, Game  # noqa: E402

import agents as agents_mod  # noqa: E402

CASE = "004-office-murder"
EXPECTED_SLUG = "game-office-murder-case"

# 复现序列模拟可观察的真人行为，不指定凶手、不预先给投票答案。
SCRIPT = [
    ("A同事，你17:40在做什么？", "质询角色：了解公开口径"),
    ("轮到你们了", "结束本轮：让所有角色互相发问"),
    ("我投A同事", "阶段一投票：只选择中性候选，不预设凶手"),
    ("我要搜查文件柜", "阶段二搜证：寻找可交叉比对的事实"),
    ("轮到你们了", "阶段二：让角色继续互相发问"),
    ("C经理，案发时段你在哪里？", "阶段二追问：追问时间线"),
    ("深入调查办公桌的擦拭痕迹，针对A同事", "深入调查：验证线索粒度"),
    ("搜一下B女士的身", "搜身：验证人物线索"),
    ("进入投票", "推进投票阶段"),
]

# 真人终投由当前候选列表决定；占位名绝不指向凶手。最终复现前追加中性候选投票。

# 品牌名：只允许在结算那一步的回复里出现（开局横幅由 CLI 打印，不属于 handle 输出）
BRAND_NAME = "仙踪问道"


# 过度引导标记：出现即视为体验失败（替玩家列矛盾/给可照抄的提问）
OVER_GUIDE_MARKERS = (
    "建议下一批",
    "可照抄",
    "硬伤",
    "矛盾点",
    "可疑度",
    "印证状态",
    "孤证",
    "证据链",
)


def tree_hash(path: Path) -> tuple[str, int]:
    """目录下所有文件的聚合哈希（用于证明剧本没被改动）。"""
    h = hashlib.sha256()
    files = sorted(p for p in path.rglob("*") if p.is_file())
    for f in files:
        h.update(f.relative_to(path).as_posix().encode())
        h.update(f.read_bytes())
    return h.hexdigest()[:16], len(files)


def inspect_state(state_path: Path, script_dir: str, enforce_default_location: bool = True) -> tuple[dict | None, list[str]]:
    """校验测试存档落点、JSON 完整性和剧本归属。"""
    errors: list[str] = []
    expected_parent = Path.home() / ".jubensha" / EXPECTED_SLUG
    if enforce_default_location:
        if state_path.parent != expected_parent:
            errors.append(f"状态目录越界：{state_path.parent} != {expected_parent}")
        if state_path.name != "test_state.json":
            errors.append(f"测试文件名不是 test_state.json：{state_path.name}")
    if not state_path.exists():
        return None, ["状态文件尚未落盘"]
    try:
        data = json.loads(state_path.read_text(encoding="utf-8"))
    except Exception as err:
        return None, [f"状态 JSON 解析失败：{err}"]
    if data.get("script_dir") != script_dir:
        errors.append(f"script_dir 错误：{data.get('script_dir')!r} != {script_dir!r}")
    if data.get("script") not in (script_dir, "004 办公室谋杀案"):
        errors.append(f"script 名称异常：{data.get('script')!r}")
    return data, errors


def snapshot(game: Game, state_path: Path, refs: Path) -> str:
    s = state_path.stat() if state_path.exists() else None
    h, n = tree_hash(refs)
    size = f"{s.st_size}B" if s else "—"
    mtime = time.strftime("%H:%M:%S", time.localtime(s.st_mtime)) if s else "—"
    return f"{state_path.name} {size:>7s} (mtime {mtime}) | references/ {h} ({n} 文件，未变)"


def main() -> int:
    ap = argparse.ArgumentParser(description="剧本杀完整对局复现")
    ap.add_argument("--mock", action="store_true", help="离线确定性代理")
    ap.add_argument("--state", default=None, help="状态文件路径")
    ap.add_argument("--script", default=CASE, help="references 下的剧本目录名")
    args = ap.parse_args()

    refs = ROOT / "references" / args.script
    script = load_script.load(str(refs))
    slug = str(script.meta.get("英文名") or args.script)
    if slug != EXPECTED_SLUG:
        print(f"[状态校验失败] 剧本 slug 为 {slug!r}，期望 {EXPECTED_SLUG!r}")
        return 1
    # 测试状态写在 ~/.jubensha/<slug>/test_state.json，不碰真实存档 state.json
    state_path = Path(args.state) if args.state else (Path.home() / ".jubensha" / slug / "test_state.json")
    if args.state is None:
        expected_state_path = Path.home() / ".jubensha" / EXPECTED_SLUG / "test_state.json"
        if state_path != expected_state_path:
            print(f"[状态校验失败] 默认测试路径错误：{state_path} != {expected_state_path}")
            return 1
    state_path.parent.mkdir(parents=True, exist_ok=True)
    if state_path.exists():
        state_path.unlink()

    if args.mock:
        agent = agents_mod.MockAgents(script)
    else:
        import llm

        cfg = llm.load_config()
        if cfg is None:
            print("未检测到 LLM 配置；改用 --mock 或先跑 scripts/llm.py init")
            return 1
        agent = agents_mod.LLMAgents(llm.ChatClient(cfg))

    game = Game(script, agent, state_path)
    refs_hash_before, refs_files = tree_hash(refs)

    print(f"\n=== 复现开始：{args.script} ===")
    print(f"references/ 初始哈希 {refs_hash_before}（{refs_files} 个文件）")
    print(f"状态文件：{state_path}")
    print(f"代理：{'Mock（离线）' if args.mock else 'LLM（' + str(cfg['model']) + '）'}\n")

    total_start = time.time()
    flow_fail = 0
    meaningful_steps = 0
    brand_steps: list[int] = []
    steps = list(SCRIPT)
    candidate = script.ai_names[0] if script.ai_names else ""
    if candidate:
        steps.append((f"我投{candidate}", "终投：选择中性候选，测试不预设凶手"))

    culprit = script.culprit
    for idx, (text, label) in enumerate(steps, 1):
        t0 = time.time()
        try:
            reply = game.handle(text)
            status = "ok"
            before = snapshot(game, state_path, refs)
            state_data, state_errors = inspect_state(state_path, args.script, args.state is None)
            if state_errors:
                flow_fail += 1
                print(f"     [状态失败] {' | '.join(state_errors)}")
            elif state_data:
                print(
                    f"     [状态正常] script_dir={state_data.get('script_dir')} round={state_data.get('round')} phase={state_data.get('phase_index')} result={'有' if state_data.get('result') else '无'}"
                )
            if "我投" in text or "轮到你们了" in text or "搜" in text or "质询" in text:
                meaningful_steps += 1
        except Err as err:
            reply, status = f"[拒绝] {err}", "拒绝"
            flow_fail += 1

        if game.state.get("result") is None:
            ai_text = []
            forbidden_hits = []
            for row in game.state["public_log"]:
                speaker = str(row.get("speaker", ""))
                text_out = str(row.get("text", ""))
                if speaker in script.characters:
                    ai_text.append(text_out)
                    char = script.characters[speaker]
                    forbidden_hits += [w for w in char.forbidden if w and w in text_out]
                elif speaker == "DM":
                    ai_text.append(text_out)
            ai_text.append(str(reply))
            ai_text.append("\n".join(game.state.get("ai_window_text") or []))
            prefinal = "\n".join(ai_text)
            banned = agents_mod.has_ban(prefinal)
            over_guided = [m for m in OVER_GUIDE_MARKERS if m in prefinal]
            if forbidden_hits or banned or over_guided:
                flow_fail += 1
                print(f"     [体验失败] 结算前 AI/DM 出现禁透词、推理结论或过度引导：{forbidden_hits[:3]} | ban={banned} | over={over_guided}")
        cost = time.time() - t0
        if BRAND_NAME in str(reply):
            brand_steps.append(idx)
        client = getattr(agent, "client", None)
        money = f" {client.calls}次" if client else ""

        print(f"[{idx:02d}] {label}")
        print(f"     说：{text}")
        print(f"     → ({status}, {cost:.1f}s{money}) {reply[:110].replace(chr(10), ' ')}")
        print(f"     {snapshot(game, state_path, refs)}")
        print()

    print(game.hint() + "\n")

    result = game.state.get("result")
    print("=== 结算 ===")
    if result:
        last = len(script.phases) - 1
        votes = {k.split(":", 1)[1]: v for k, v in game.state["votes"].items() if k.startswith(f"{last}:")}
        for who, tgt in votes.items():
            print(f"  {who} → {tgt}")
        print(f"  计票：{result['tally']}")
        print(f"  得票最多：{result['top']}｜凶手：{result['culprit']}")
        print(f"  胜者：{result['winner']}")
    else:
        print("  未走到结算（有步骤被拒绝）")

    final_state, final_state_errors = inspect_state(state_path, args.script, args.state is None)
    if final_state_errors:
        flow_fail += 1
    print("\n=== 最终 state.json 校验 ===")
    if final_state_errors:
        for error in final_state_errors:
            print(f"  ✘ {error}")
    else:
        print(f"  ✔ 路径：{state_path}")
        print(f"  ✔ script_dir：{final_state.get('script_dir')}")
        print(f"  ✔ round/phase：{final_state.get('round')}/{final_state.get('phase_index')}")
        print(f"  ✔ result：{'已结算' if final_state.get('result') else '未结算'}")

    refs_hash_after, _ = tree_hash(refs)
    print("\n=== 文件变化核对 ===")
    print(f"  references/ 前：{refs_hash_before}")
    print(f"  references/ 后：{refs_hash_after}  → {'未变 ✔' if refs_hash_before == refs_hash_after else '被修改 ✘'}")
    print(f"  唯一变化的文件：{state_path}")
    print(f"  整局耗时：{time.time() - total_start:.0f} 秒")
    if getattr(agent, "client", None):
        print(f"  整局调用：{agent.client.calls} 次")

    print(f"  有意义步骤：{meaningful_steps}/{len(steps)}")
    if args.state is None and state_path.exists():
        state_path.unlink()
        print(f"  测试存档已清理：{state_path}")
    last_step = len(steps)
    stray_brand = [i for i in brand_steps if i != last_step]
    if stray_brand:
        flow_fail += 1
        print(f"     [体验失败] 品牌在非结算步骤出现（打扰度超标）：{stray_brand}")
    if last_step not in brand_steps:
        print("     [提示] 结算未展示品牌收尾")
    print(f"  品牌曝光步骤：{brand_steps or '无'}（期望只有 [{last_step}]）")
    print(f"  体验失败计数：{flow_fail}")
    return 0 if result and flow_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
