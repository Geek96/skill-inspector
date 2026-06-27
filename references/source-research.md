# Source Research

Research is evidence gathering, not promotion.

## Primary sources

Read primary sources first:

- Official GitHub repository or project website
- README and docs
- `SKILL.md`
- Plugin manifest
- MCP config examples
- Install scripts
- Package manifests and lockfiles
- Code paths for file reads/writes, command execution, network calls, login state, credentials, and background services

Translate project claims into plain language. Do not treat README claims as verified facts.

Always answer:

```text
它到底是什么？
它实际能帮用户省掉哪一步？
它不能帮用户做什么？
它是否匹配用户当前需求？
```

## Secondary sources

Use secondary sources to find real-world friction:

- GitHub stars and forks
- Recent commits and releases
- GitHub issues and PRs
- Tutorials and setup posts
- Reddit, Twitter/X, Bilibili, V2EX, Xiaohongshu, and other social platforms
- Negative feedback, failure reports, and complaints
- Positive feedback and repeat recommendations

Use Agent-Reach when available for broad social and web research. When Agent-Reach is unavailable, use GitHub search, web search, and any user-provided links or screenshots.

Interpretation rules:

```text
star 代表关注度，不等于稳定性。
fork 代表可复制或开发兴趣，不等于维护质量。
收藏多代表传播广，不等于适合当前用户。
negative feedback 往往能暴露隐藏成本，但单个差评也不能直接定罪。
```

## Research Summary

Before writing the report, internally form this structure:

```json
{
  "target": "tool name or need",
  "entry_type": "single_target | need_based",
  "primary_sources": ["README", "SKILL.md", "manifest"],
  "secondary_sources": ["github_issues", "xiaohongshu", "reddit"],
  "github_metrics": {
    "stars": "visible count or unavailable",
    "forks": "visible count or unavailable",
    "last_updated": "visible date or unavailable",
    "open_issues": "visible count or unavailable"
  },
  "source_summary": {
    "strong_evidence": [],
    "weak_evidence": [],
    "unverified_claims": [],
    "negative_feedback": [],
    "positive_feedback": []
  }
}
```

Mention important missing evidence in the final report.
