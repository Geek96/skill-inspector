#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ".claude-plugin/plugin.json",
    "README.md",
    "README.zh-CN.md",
    "CHANGELOG.md",
    "CLAUDE.md",
    "SKILL.md",
    "references/review-workflow.md",
    "references/source-research.md",
    "references/risk-model.md",
    "references/runtime-verification.md",
    "references/credential-handling.md",
    "references/obsidian-library.md",
    "templates/chat-report.md",
    "templates/obsidian-review.md",
    "templates/comparison-note.md",
    "examples/single-target-input.md",
    "examples/need-based-input.md",
    "examples/expected-chat-report-outline.md",
    "examples/expected-obsidian-review-outline.md",
    "examples/expected-comparison-outline.md",
]

REQUIRED_SKILL_PHRASES = [
    "Read `references/review-workflow.md`",
    "Read `references/source-research.md`",
    "Read `references/risk-model.md`",
    "Read `references/runtime-verification.md`",
    "Read `references/credential-handling.md`",
    "Read `references/obsidian-library.md` when the user asks for Obsidian",
    "single target",
    "need-based discovery",
    "Final Output Contract",
]

REQUIRED_TEMPLATE_PHRASES = [
    "一句话结论",
    "推荐程度",
    "风险等级",
    "它到底是什么",
    "适合谁 / 不适合谁",
    "安装前检查清单",
    "是否建议运行 demo",
    "证据来源",
]

REQUIRED_WORKFLOW_PHRASES = [
    "Entry A: Single Target Review",
    "Entry B: Need-Based Discovery And Comparison",
    "3-5",
    "1-2",
    "Ordinary User Mode",
    "Hands-On Trial Mode",
    "Developer Audit Mode",
    "Do not guess the user's skill level",
]

REQUIRED_SOURCE_RESEARCH_PHRASES = [
    "Primary sources",
    "Secondary sources",
    "Agent-Reach",
    "GitHub stars",
    "forks",
    "issues",
    "negative feedback",
    "README claims",
    "source_summary",
]

REQUIRED_RISK_PHRASES = [
    "Low Risk",
    "Medium Risk",
    "High Risk",
    "Not Recommended",
    "风险是什么",
    "可能后果",
    "降低风险",
    "Do not treat stars, saves, or README claims as proof",
    "main-account cookies",
]

REQUIRED_RUNTIME_PHRASES = [
    "Easy To Verify",
    "Not Easy To Verify",
    "Ask Before Running",
    "temporary folder",
    "minimal demo",
    "Do not run",
    "user approves",
    "这个工具看起来可以安全地跑一个最小 demo",
]

REQUIRED_CREDENTIAL_PHRASES = [
    "凭据使用要匹配用户目标",
    "不接凭据",
    "测试凭据",
    "低权限真实凭据",
    "受控生产凭据",
    "API key",
    "CLI",
    "login",
    "How to revoke",
]

REQUIRED_OBSIDIAN_PHRASES = [
    "type: skill-review",
    "risk_level",
    "recommendation",
    "review_status",
    "reviewed_at",
    "Quick Reference",
    "[!abstract]",
    "[!warning]",
    "[[credential-risk]]",
    "Skill Reviews/",
    "99_Comparisons",
    "Dataview",
]

REQUIRED_OBSIDIAN_EXPECTED_PHRASES = [
    "type: skill-review",
    "source_primary",
    "source_secondary",
    "risk_level",
    "recommendation",
    "review_status",
    "reviewed_at",
    "Quick Reference",
    "[!abstract]",
    "[!warning]",
    "[[credential-risk]]",
]

REQUIRED_COMPARISON_PHRASES = [
    "候选列表",
    "横向对比表",
    "推荐排序",
    "功能匹配度",
    "风险等级",
    "安装成本",
    "维护状态",
    "适合人群",
]

REQUIRED_FINAL_SKILL_PHRASES = [
    "Do not run, install, log in, or connect credentials",
    "risk near the top",
    "Mark missing evidence as unverified",
    "Agent-Reach",
    "GitHub stars",
    "forks",
    "main-account cookies",
]

REQUIRED_README_PHRASES = [
    "skill-inspector",
    "AI agent skill",
    "risk-first",
    "single target",
    "need-based discovery",
    "Obsidian",
    "Dataview",
    "Runtime verification",
    "Credential handling",
    "version",
]

REQUIRED_CLAUDE_PHRASES = [
    "Versioning",
    "EVERY COMMIT MUST FOLLOW",
    "PATCH",
    "MINOR",
    "MAJOR",
    ".claude-plugin/plugin.json",
    "CHANGELOG.md",
    "GitHub Release",
    "commit message",
]

REQUIRED_PLUGIN_PHRASES = [
    '"name": "skill-inspector"',
    '"version":',
    '"skills"',
    '"./"',
]

FORBIDDEN_FILLER = [
    "T" + "BD",
    "implement " + "later",
    "fill " + "in details",
    "类似" + "上面",
    "酌情" + "处理",
]


def read(relative_path: str) -> str:
    path = ROOT / relative_path
    if not path.exists():
        raise AssertionError(f"Missing required file: {relative_path}")
    return path.read_text(encoding="utf-8")


def assert_contains(text: str, phrase: str, file_name: str) -> None:
    if phrase not in text:
        raise AssertionError(f"{file_name} must contain: {phrase}")


def main() -> int:
    for relative_path in REQUIRED_FILES:
        read(relative_path)

    for relative_path in REQUIRED_FILES:
        text = read(relative_path)
        for phrase in FORBIDDEN_FILLER:
            if phrase in text:
                raise AssertionError(f"{relative_path} contains filler text: {phrase}")

    skill = read("SKILL.md")
    for phrase in REQUIRED_SKILL_PHRASES:
        assert_contains(skill, phrase, "SKILL.md")

    for phrase in REQUIRED_FINAL_SKILL_PHRASES:
        assert_contains(skill, phrase, "SKILL.md")

    workflow = read("references/review-workflow.md")
    for phrase in REQUIRED_WORKFLOW_PHRASES:
        assert_contains(workflow, phrase, "references/review-workflow.md")

    source_research = read("references/source-research.md")
    for phrase in REQUIRED_SOURCE_RESEARCH_PHRASES:
        assert_contains(source_research, phrase, "references/source-research.md")

    risk_model = read("references/risk-model.md")
    for phrase in REQUIRED_RISK_PHRASES:
        assert_contains(risk_model, phrase, "references/risk-model.md")

    runtime_verification = read("references/runtime-verification.md")
    for phrase in REQUIRED_RUNTIME_PHRASES:
        assert_contains(runtime_verification, phrase, "references/runtime-verification.md")

    credential_handling = read("references/credential-handling.md")
    for phrase in REQUIRED_CREDENTIAL_PHRASES:
        assert_contains(credential_handling, phrase, "references/credential-handling.md")

    obsidian_reference = read("references/obsidian-library.md")
    obsidian_template = read("templates/obsidian-review.md")
    for phrase in REQUIRED_OBSIDIAN_PHRASES:
        assert_contains(obsidian_reference + "\n" + obsidian_template, phrase, "Obsidian reference/template")

    comparison_template = read("templates/comparison-note.md")
    for phrase in REQUIRED_COMPARISON_PHRASES:
        assert_contains(comparison_template, phrase, "templates/comparison-note.md")

    expected_obsidian = read("examples/expected-obsidian-review-outline.md")
    for phrase in REQUIRED_OBSIDIAN_EXPECTED_PHRASES:
        assert_contains(expected_obsidian, phrase, "examples/expected-obsidian-review-outline.md")

    expected_comparison = read("examples/expected-comparison-outline.md")
    for phrase in REQUIRED_COMPARISON_PHRASES:
        assert_contains(expected_comparison, phrase, "examples/expected-comparison-outline.md")

    chat_template = read("templates/chat-report.md")
    expected_outline = read("examples/expected-chat-report-outline.md")
    for phrase in REQUIRED_TEMPLATE_PHRASES:
        assert_contains(chat_template, phrase, "templates/chat-report.md")
        assert_contains(expected_outline, phrase, "examples/expected-chat-report-outline.md")

    readme = read("README.md")
    readme_zh = read("README.zh-CN.md")
    for phrase in REQUIRED_README_PHRASES:
        assert_contains(readme, phrase, "README.md")
    for phrase in ["skill-inspector", "AI agent skill", "风险优先", "Obsidian", "Dataview", "版本"]:
        assert_contains(readme_zh, phrase, "README.zh-CN.md")

    claude = read("CLAUDE.md")
    for phrase in REQUIRED_CLAUDE_PHRASES:
        assert_contains(claude, phrase, "CLAUDE.md")

    plugin = read(".claude-plugin/plugin.json")
    for phrase in REQUIRED_PLUGIN_PHRASES:
        assert_contains(plugin, phrase, ".claude-plugin/plugin.json")

    print("skill-inspector validation passed")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
