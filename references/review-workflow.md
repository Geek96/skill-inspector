# Review Workflow

Use this workflow to decide what kind of review the user needs.

## Entry A: Single Target Review

Use when the user gives one specific skill, MCP server, plugin, agent tool, GitHub repo, or URL.

Flow:

1. Identify the target name and source URL.
2. Read primary sources.
3. Research secondary sources.
4. Explain what the tool actually is and is not.
5. Evaluate setup cost, dependency transparency, maintenance, risk, reputation, and user fit.
6. Judge whether a minimal runtime demo is easy to verify.
7. Ask before running anything.
8. Output a layered report.

## Entry B: Need-Based Discovery And Comparison

Use when the user describes a capability but has not chosen a tool.

Flow:

1. Turn the user's need into 2-4 search phrases.
2. Search for candidate skills/tools through GitHub, Agent-Reach, and web search.
3. Shortlist 3-5 candidates.
4. Run lightweight reviews for every candidate.
5. Deep-review 1-2 candidates when the evidence or user need justifies it.
6. Compare function, risk, setup cost, maintenance, reputation, and fit.
7. Recommend a ranked choice with caveats.

## Review Depth Selection

Do not guess the user's skill level. Explain the modes and let the user choose.

### Ordinary User Mode

Use when the user only wants to know whether the tool is worth installing.

Common scenarios:

- Student or content creator avoiding setup traps.
- New agent user who wants a plain recommendation.
- User wants to know whether the tool helps their goal.

Focus on functional truth, setup burden, obvious risks, and fit.

### Hands-On Trial Mode

Use when the user is willing to run a minimal demo in a temporary folder or test repository.

Common scenarios:

- User can use a terminal.
- User accepts installing dependencies.
- User wants to see output before trusting the tool.

Focus on whether the README works, hidden dependencies, minimal demo success, and unexpected file writes.

### Developer Audit Mode

Use when the user is willing to inspect code, install scripts, permission behavior, and failure modes.

Common scenarios:

- User wants long-term use.
- User plans to recommend it publicly.
- User may put it in a team workflow.
- Tool touches important data, accounts, or infrastructure.

Focus on command execution, file reads/writes, credential handling, network requests, maintenance, and rollback.

Suggested prompt:

```text
我可以按三种深度继续：普通使用者模式、熟练试用者模式、开发者审计模式。你想按哪种模式测？
```

## Report Sequence

Default order:

1. 一句话结论
2. 推荐程度
3. 风险等级
4. 它到底是什么
5. 适合谁 / 不适合谁
6. 主要坑点
7. 安装前检查清单
8. 是否建议运行 demo
9. 开发者审计细节
10. 证据来源

If the risk is high or not recommended, lead with risk before describing attractive features.
