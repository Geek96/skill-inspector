# Changelog

All notable user-facing changes to **skill-inspector** are documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
Version scheme: `MAJOR.MINOR.PATCH`

---

## [1.1.0] — 2026-06-29

### Added
- Obsidian wiki preflight choices: output language, review depth, and dated topic directory naming.
- Compact Obsidian library structure: `YYYY-MM-DD-topic-summary/skills` and `YYYY-MM-DD-topic-summary/comparison`.
- Detailed candidate note requirements, including substantive function summaries, inputs, outputs, fit, non-fit, risks, install commands, and evidence.
- Comparison dashboard requirements for ranking, function map, recommended workflow, risks, install commands, and evidence.
- Fixed Obsidian templates:
  - `templates/obsidian-vault-readme.md`
  - `templates/obsidian-skill-review-detailed.md`
  - `templates/obsidian-comparison-dashboard.md`

### Changed
- Obsidian output now defaults to Chinese body text when the user does not specify a language.
- Obsidian guidance now permits titles, section headings, YAML keys, Dataview fields, command names, package names, tool names, and code blocks to remain English while body text follows the selected language.
- Replaced the legacy bulky `Skill Reviews/00_Index.md` category-tree default with a simpler library layout.

