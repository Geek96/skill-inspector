<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-7C3AED?style=for-the-badge" alt="AI Agent Skill"/>
  <img src="https://img.shields.io/badge/version-1.1.1-10B981?style=for-the-badge" alt="Version 1.1.1"/>
  <img src="https://img.shields.io/github/license/Geek96/skill-inspector?style=for-the-badge&color=6B7280" alt="MIT License"/>
</p>

<h1 align="center">🔎 skill-inspector</h1>

<p align="center">
  <strong>A risk-first AI agent skill for reviewing agent capabilities before you install them</strong>
  <br/>
  <code>primary sources → risk model → runtime verification → Obsidian review library</code>
  <br/><br/>
  Works with <strong>Claude Code</strong> · <strong>Codex CLI</strong> · <strong>Gemini CLI</strong> · and any agent that reads <code>.md</code> skills
</p>

<p align="center">
  <strong>English</strong> | <a href="README.zh-CN.md">简体中文</a>
</p>

---

## ✨ Features

- **Risk-first reviews** — puts credential, filesystem, shell, browser-login, and cloud risks near the top.
- **Single target review** — audit one AI skill, MCP server, plugin, GitHub repo, or agent tool.
- **Need-based discovery** — turn a capability request into candidate search, shortlist, comparison, and recommendation.
- **Primary-source discipline** — reads README, `SKILL.md`, manifests, package files, install scripts, and code paths before trusting claims.
- **Secondary-source research** — uses GitHub metrics, issues, PRs, tutorials, social posts, and Agent-Reach when available.
- **Runtime verification gates** — does not run, install, log in, or connect credentials until the user chooses a deeper review mode and approves.
- **Credential handling model** — distinguishes no credentials, test credentials, low-privilege real credentials, and controlled production credentials.
- **Obsidian review library** — saves Dataview-ready review notes, comparison notes, MOC pages, and `[[wiki-links]]`.
- **Agent-agnostic** — plain Markdown skill files; no proprietary runtime required.

---

## 📦 Installation

All files are plain `.md` skill instructions. Pick your agent below.

### Claude Code

```bash
npx skills add Geek96/skill-inspector
```

### Codex CLI

```bash
git clone https://github.com/Geek96/skill-inspector.git
cd skill-inspector
```

Add the repository path to your project instructions or skill search path:

```markdown
## Skills
Load skill from: /path/to/skill-inspector/
```

### Other Agents

Any agent that can read Markdown skills can use this repository:

1. Clone the repo.
2. Point the agent to this directory.
3. Load `SKILL.md` as the skill entrypoint.

---

## 🧭 What It Reviews

| Target | What skill-inspector checks |
| --- | --- |
| AI skill | Trigger scope, instructions, hidden runtime expectations, output quality |
| MCP server | Setup cost, credentials, network calls, filesystem access, login state |
| Plugin | Manifest, bundled skills, servers, install behavior, update path |
| Agent tool | Shell execution, browser automation, account access, background processes |
| GitHub repo | Maintenance, releases, issues, install scripts, package manifests |

---

## 🧩 Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    skill-inspector                           │
│                  (risk-first review skill)                   │
│                                                             │
│  User asks: "Should I install this?" / "Find me a tool"      │
│         │                                                   │
│         ▼                                                   │
│  ┌────────────────┐    ┌──────────────────┐                 │
│  │ Primary sources │───▶│ Secondary signals │                 │
│  │ README / code   │    │ GitHub / social   │                 │
│  └────────┬───────┘    └────────┬─────────┘                 │
│           │                     │                            │
│           ▼                     ▼                            │
│  ┌────────────────┐    ┌──────────────────┐                 │
│  │ Risk model      │───▶│ Verification plan │                 │
│  │ credentials     │    │ demo or no-demo   │                 │
│  └────────┬───────┘    └────────┬─────────┘                 │
│           │                     │                            │
│           ▼                     ▼                            │
│        Chat report      Obsidian / Dataview library          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Review Modes

| Mode | Use when | Runtime behavior |
| --- | --- | --- |
| **Ordinary User Mode** | You only need a recommendation | No install, no login, no demo |
| **Hands-On Trial Mode** | You approve a minimal test | Temporary folder, no real account by default |
| **Developer Audit Mode** | You may depend on the tool long-term | Inspect code paths, credentials, writes, network calls, rollback |

By default, skill-inspector does **not** run tools, install packages, log in, or connect credentials.

---

## 📚 Obsidian Output

When asked to save reviews, the skill produces a Dataview-friendly library:

```text
Skill Reviews/
├── 00_Index.md
├── Research/
├── Content-Creation/
├── Knowledge-Management/
├── Development/
├── Automation/
├── Risky-Or-Needs-Caution/
└── Comparisons/
```

Review notes include:

- YAML frontmatter
- Quick Reference table
- `[!abstract]`, `[!warning]`, `[!info]` callouts
- `[[credential-risk]]` and other wiki-links
- comparison notes for 3-5 candidates
- Dataview fields such as `risk_level`, `recommendation`, `review_status`, `requires_credentials`, and `verification_level`

---

## 📖 Example Prompts

```text
> 帮我看看这个 MCP server 值不值得装
> 比较几个能生成小红书图文的 agent skill
> 把这些候选工具做成 Obsidian review library
> 这个 GitHub repo 会不会需要主账号 cookie？
> 我可以跑一个最小 demo，你按开发者审计模式看
```

---

## 📁 Project Structure

```text
skill-inspector/
├── SKILL.md                         # skill entrypoint
├── references/
│   ├── review-workflow.md            # single target vs need-based discovery
│   ├── source-research.md            # primary and secondary evidence
│   ├── risk-model.md                 # low / medium / high / not recommended
│   ├── runtime-verification.md       # demo gates and verification checklist
│   ├── credential-handling.md        # API key, CLI, login, cookie handling
│   └── obsidian-library.md           # Obsidian + Dataview rules
├── templates/
│   ├── chat-report.md
│   ├── obsidian-review.md
│   └── comparison-note.md
├── examples/
├── scripts/validate_skill.py
├── .claude-plugin/plugin.json        # version source of truth
├── CHANGELOG.md
├── CLAUDE.md                         # contribution and version rules
├── README.md
└── README.zh-CN.md
```

---

## 🔖 Versioning

This repository follows the same version rules as `paper-research-skill`:

- Version source of truth: `.claude-plugin/plugin.json`
- Every user-facing skill/template/documentation change increments `PATCH`
- When `PATCH` reaches 10, carry to `MINOR` and reset `PATCH` to 0
- `MAJOR` changes require explicit human approval
- `CHANGELOG.md` is updated on `MINOR` releases, not every patch
- GitHub Releases are created on `MINOR` releases

See [CLAUDE.md](CLAUDE.md) for the full commit checklist.

---

## 📄 License

MIT © [Geek96](https://github.com/Geek96)
