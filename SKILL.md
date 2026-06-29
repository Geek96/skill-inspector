---
name: skill-inspector
version: "1.1.0"
description: Use when the user wants to evaluate, audit, compare, or decide whether to install an AI skill, MCP server, plugin, agent tool, or GitHub repo that extends agent capabilities.
---

# Skill Inspector

Use this skill when the user asks whether a skill/tool is worth installing, safe to use, suitable for their need, or when they want to discover and compare tools for a capability.

## Required Workflow

1. Read `references/review-workflow.md`.
2. Read `references/source-research.md`.
3. Read `references/risk-model.md`.
4. Read `references/runtime-verification.md`.
5. Read `references/credential-handling.md`.
6. Read `references/obsidian-library.md` when the user asks for Obsidian, a review library, Dataview-friendly Markdown, saved notes, or horizontal comparison notes.
7. Classify the request as single target or need-based discovery.
8. Use primary sources first, then secondary sources.
9. Report uncertainty honestly.
10. Do not run, install, log in, or connect credentials unless the user chooses a deeper review mode and explicitly approves the action.

## Final Output Contract

For normal chat or terminal use, return these sections:

- 一句话结论
- 推荐程度
- 风险等级
- 它到底是什么
- 适合谁 / 不适合谁
- 主要坑点
- 安装前检查清单
- 是否建议运行 demo
- 开发者审计细节
- 证据来源

When comparing candidates, add:

- 候选列表
- 横向对比表
- 推荐排序

When the user asks for Obsidian output, use the templates and rules in `references/obsidian-library.md`.

## Quality Bar

- Explain the tool's real function in plain language.
- Put risk near the top.
- Give concrete consequences and mitigations for important risks.
- Include GitHub stars, forks, maintenance signals, and issue/social evidence when available.
- Do not treat stars, saves, or README claims as proof of quality.
- Do not guess the user's skill level; explain review modes and let the user choose.
- Mark missing evidence as unverified.
- Use Agent-Reach for secondary-source research when available.
- Include GitHub stars and forks when available, but explain that they are attention signals, not quality proof.
- Treat main-account cookies as a serious credential risk.
- For runtime actions, apply `references/runtime-verification.md` and `references/credential-handling.md`; the rule "Do not run, install, log in, or connect credentials" is the default until the user chooses and approves a deeper mode.
