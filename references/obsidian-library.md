# Obsidian Review Library

Only use this format when the user asks to save a review, create an Obsidian note, generate a Dataview-friendly version, or build a comparison note.

## Visual Style

Follow the style of `paper-research-skill` outputs:

- YAML frontmatter
- Quick Reference table
- Obsidian callouts such as `[!abstract]`, `[!warning]`, `[!info]`
- `[[wiki-links]]`
- Dataview-friendly fields
- MOC index pages
- Comparison notes

## Folder Structure

```text
Skill Reviews/
├── 00_Index.md
├── 01_Research/
│   ├── Literature/
│   ├── Web-Search/
│   └── Social-Media/
├── 02_Content-Creation/
│   ├── Xiaohongshu/
│   ├── Writing/
│   └── Image-Video/
├── 03_Knowledge-Management/
│   ├── Obsidian/
│   ├── Zotero/
│   └── Notion/
├── 04_Development/
│   ├── Coding-Agent/
│   ├── Code-Review/
│   └── Deployment/
├── 05_Automation/
│   ├── Browser/
│   ├── Filesystem/
│   └── Workflow/
├── 06_Risky-Or-Needs-Caution/
│   ├── Account-Login/
│   ├── File-Writing/
│   ├── Server-Access/
│   └── Auto-Publishing/
└── 99_Comparisons/
```

## MOC Dataview Examples

````markdown
# Skill Review Index

## 高推荐

```dataview
TABLE risk_level, recommendation, category, stars, last_updated
FROM "Skill Reviews"
WHERE recommendation = "recommended"
SORT reviewed_at DESC
```

## 高风险

```dataview
TABLE risk_level, main_risk, requires_credentials
FROM "Skill Reviews"
WHERE risk_level = "high"
SORT reviewed_at DESC
```
````

## Required Frontmatter Fields

- `title`
- `type: skill-review`
- `category`
- `risk_level`
- `recommendation`
- `review_status`
- `reviewed_at`
- `source_primary`
- `source_secondary`
- `requires_credentials`
- `requires_login`
- `requires_cli`
- `verification_level`
