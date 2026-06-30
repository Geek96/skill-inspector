<p align="center">
  <img src="https://img.shields.io/badge/AI_Agent-Skill-7C3AED?style=for-the-badge" alt="AI Agent Skill"/>
  <img src="https://img.shields.io/badge/version-1.1.1-10B981?style=for-the-badge" alt="Version 1.1.1"/>
  <img src="https://img.shields.io/github/license/Geek96/skill-inspector?style=for-the-badge&color=6B7280" alt="MIT License"/>
</p>

<h1 align="center">🔎 skill-inspector</h1>

<p align="center">
  <strong>风险优先的 AI agent skill 审计工具 —— 安装前先看清楚它会动什么</strong>
  <br/>
  <code>一手来源 → 风险模型 → 运行验证 → Obsidian Review Library</code>
</p>

<p align="center">
  <a href="README.md">English</a> | <strong>简体中文</strong>
</p>

---

## ✨ 功能亮点

- **风险优先** — 把凭据、文件写入、shell、浏览器登录态、云服务权限放在报告前面。
- **单目标审计** — 审一个 AI skill、MCP server、plugin、GitHub repo 或 agent tool。
- **需求型发现** — 用户只说需求时，自动找候选、短列、横向比较、排序推荐。
- **一手来源优先** — 先读 README、`SKILL.md`、manifest、安装脚本、package 文件和关键代码路径。
- **二手信号校准** — 看 GitHub stars/forks/issues/PR、教程、社媒反馈和 Agent-Reach 搜索结果。
- **运行验证门槛** — 默认不运行、不安装、不登录、不接凭据；只有用户选择更深模式并批准后才跑最小 demo。
- **凭据处理模型** — 区分不接凭据、测试凭据、低权限真实凭据、受控生产凭据。
- **Obsidian 知识库** — 生成 Dataview 友好的审计笔记、比较笔记、MOC 和 `[[wiki-links]]`。

---

## 🚀 快速开始

```bash
npx skills add Geek96/skill-inspector
```

或者直接克隆：

```bash
git clone https://github.com/Geek96/skill-inspector.git
```

任何能读取 Markdown skill 的 agent 都可以使用根目录的 `SKILL.md`。

---

## 🧭 它适合审什么

| 对象 | 会重点看什么 |
| --- | --- |
| AI skill | 触发范围、隐藏前置条件、输出格式、是否会要求运行命令 |
| MCP server | 安装成本、凭据、网络请求、文件读写、登录态 |
| Plugin | manifest、 bundled skills、server、安装和更新路径 |
| Agent tool | shell 执行、浏览器自动化、账号权限、后台进程 |
| GitHub repo | 维护状态、release、issue、安装脚本、package manifest |

---

## 🧩 工作流

```text
用户问题：这个工具值不值得装？有没有更好的替代？
        │
        ▼
读取一手来源：README / SKILL.md / manifest / scripts / package
        │
        ▼
读取二手信号：GitHub metrics / issues / tutorials / social feedback
        │
        ▼
风险建模：文件、账号、凭据、网络、shell、后台服务
        │
        ▼
输出：聊天报告 / 横向对比表 / Obsidian Dataview 笔记
```

---

## 📝 审计模式

| 模式 | 适合场景 | 是否运行 |
| --- | --- | --- |
| **普通使用者模式** | 只想知道值不值得装 | 不运行 |
| **熟练试用者模式** | 愿意在临时目录跑最小 demo | 用户批准后运行 |
| **开发者审计模式** | 长期使用或要公开推荐 | 读代码、看权限、记录回滚方式 |

默认行为：不运行、不安装、不登录、不接凭据。

---

## 📚 Obsidian / Dataview 输出

当用户要求保存成 Obsidian review library 时，会生成：

- YAML frontmatter
- Quick Reference 表格
- `[!abstract]` / `[!warning]` / `[!info]` callout
- `[[credential-risk]]` 等 wiki-link
- 候选工具横向比较
- Dataview 字段：`risk_level`、`recommendation`、`review_status`、`requires_credentials`、`verification_level`

---

## 📁 项目结构

```text
skill-inspector/
├── SKILL.md
├── references/
│   ├── review-workflow.md
│   ├── source-research.md
│   ├── risk-model.md
│   ├── runtime-verification.md
│   ├── credential-handling.md
│   └── obsidian-library.md
├── templates/
│   ├── chat-report.md
│   ├── obsidian-review.md
│   └── comparison-note.md
├── examples/
├── scripts/validate_skill.py
├── .claude-plugin/plugin.json
├── CHANGELOG.md
├── CLAUDE.md
├── README.md
└── README.zh-CN.md
```

---

## 🔖 版本规则

版本规则与 `paper-research-skill` 相同：

- 版本唯一来源：`.claude-plugin/plugin.json`
- 每次用户可见的 skill、template、README、CHANGELOG 修改都递增 `PATCH`
- `PATCH` 到 10 时自动进位到 `MINOR`
- `MAJOR` 只能由用户明确授权
- `CHANGELOG.md` 和 GitHub Release 只在 `MINOR` 进位时汇总

完整规则见 [CLAUDE.md](CLAUDE.md)。
