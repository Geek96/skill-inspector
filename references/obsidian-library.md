# Obsidian Review Library

Use this format when the user asks to save a review, create an Obsidian note, generate a Dataview-friendly version, build a comparison wiki, or produce a reusable evaluation library.

## Preflight Choices

Before creating or updating an Obsidian evaluation wiki, ask or infer these choices. If the user already gave a preference, follow it directly.

| Choice | Options | Default |
|---|---|---|
| Output language | 中文 / English / 双语 | 中文 |
| Review depth | 快速对比 / 详细评估 / 开发者审计 | 详细评估 |
| Directory naming | `YYYY-MM-DD-topic-summary` | latest relevant update date + concise topic |

Language rule:

- If the user chooses Chinese, all body text must be Chinese. Titles, section headings, YAML keys, Dataview fields, command names, package names, tool names, and code blocks may remain English.
- If the user chooses English, body text should be English.
- If the user chooses bilingual, keep tool names and source terminology in English, and explain conclusions in Chinese.
- Do not silently mix languages in body paragraphs.

## Folder Structure

Use a compact structure. Do not create bulky category trees unless the user explicitly asks for them.

```text
SkillEvaluation/
└── YYYY-MM-DD-topic-summary/
    ├── README.md
    ├── comparison/
    │   └── <topic> Comparison.md
    └── skills/
        ├── <candidate-one>.md
        ├── <candidate-two>.md
        └── <candidate-three>.md
```

Rules:

- `SkillEvaluation/` is the long-lived container.
- Each review run gets one dated topic subdirectory.
- Use the latest relevant update date found during research, not necessarily today's date.
- Do not create `00_Index.md` by default.
- Do not create `Skill Reviews/`, `01_Research/`, or `99_Comparisons/` by default.
- Put candidate notes directly in `skills/`.
- Put comparison dashboards directly in `comparison/`.

## Visual Style

Use Obsidian-native visual structure, but avoid decorative clutter.

Required elements:

- YAML frontmatter with Dataview-friendly fields.
- One top abstract callout at the beginning.
- A quick decision table near the top.
- A detailed function summary for every candidate.
- Fit / not-fit sections.
- Risk callouts near the relevant content.
- Wiki links between comparison and candidate notes.
- Dataview snippets only when they add real navigation value.

Recommended callouts:

```markdown
> [!abstract]
> 一句话总结这个候选的本质、最佳用途和主要风险。

> [!info]
> 适合补充选择逻辑、工作流说明或组合建议。

> [!warning]
> 用于凭据、文件写入、外部 API、主账号 cookie、生产数据、删除/覆盖文件等风险。

> [!tip]
> 用于给用户可执行的选择建议或安全试用路径。
```

## Required Candidate Note Sections

Use this order for `skills/<candidate>.md`:

1. YAML frontmatter
2. H1 title
3. Abstract callout
4. Quick Reference
5. Detailed Function Summary
6. Inputs
7. Outputs
8. Best Fit
9. Not A Good Fit
10. Main Risks
11. Install Command
12. Evidence

The `Detailed Function Summary` section must be substantive. It should explain:

- what the tool actually does
- what input it expects
- what transformation or workflow it performs
- what artifacts it outputs
- what step it saves for the user
- what it does not do
- how it differs from adjacent candidates

Do not write only one-sentence summaries such as "用于画论文图". That is not enough for a wiki.

## Required Comparison Note Sections

Use this order for `comparison/<topic> Comparison.md`:

1. YAML frontmatter
2. H1 title
3. Abstract callout
4. Recommendation Ranking
5. Function Map
6. Recommended Workflow
7. Risk Notes
8. Install Commands
9. Evidence Notes

The comparison note should act as a dashboard. It should let the user decide quickly without opening every candidate note, while still linking to candidate details.

## Required Frontmatter Fields

Candidate notes:

- `title`
- `type: skill-review`
- `category`
- `risk_level`
- `recommendation`
- `rank`
- `review_status`
- `reviewed_at`
- `language`
- `source_primary`
- `source_secondary`
- `requires_credentials`
- `requires_login`
- `requires_cli`
- `verification_level`
- `stars`
- `forks`
- `installs`
- `last_updated`
- `main_risk`

Comparison notes:

- `title`
- `type: skill-comparison`
- `category`
- `reviewed_at`
- `language`
- `review_status`
- `source_primary`
- `source_secondary`

README:

- `title`
- `type: skill-evaluation-readme`
- `category`
- `reviewed_at`
- `language`

## Fixed Templates

Use these templates when generating a wiki:

- `templates/obsidian-vault-readme.md`
- `templates/obsidian-skill-review-detailed.md`
- `templates/obsidian-comparison-dashboard.md`

Existing legacy templates are still acceptable for chat snippets, but the three templates above are preferred for full Obsidian libraries.

