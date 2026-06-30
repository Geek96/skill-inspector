# CLAUDE.md — Contribution Rules for skill-inspector

This file tells agents and human contributors how to maintain this repository consistently.

---

## ⚠️ Versioning — EVERY COMMIT MUST FOLLOW

> **MANDATORY**: Agent 每次 commit 前必须执行版本检查。不执行 = 违规。
> **禁止跳版本号**：Agent 只能递增 PATCH（最后一位），绝对不能跳版本。

Version format: `MAJOR.MINOR.PATCH` — stored in `.claude-plugin/plugin.json` as the `version` field. This is the single source of truth.

| Component | Rule | Who controls |
| --- | --- | --- |
| **PATCH** | +1 on every commit that changes skill/template/user-facing content | Agent automatic |
| **MINOR** | Auto-increment when PATCH reaches **10**, reset PATCH to 0 | Agent automatic carry |
| **MAJOR** | Only when user explicitly says "bump major" or "breaking change" | Human only |

### 🔴 Pre-Commit Checklist（每次 commit 前必做）

```text
□ 1. cat .claude-plugin/plugin.json → 读取当前版本号
□ 2. 本次 commit 改了 SKILL.md / references/ / templates/ / examples/ / README.md / CHANGELOG.md？
     → YES: PATCH +1（只 +1，不跳）
     → NO:  不 bump
□ 3. PATCH = 10？→ PATCH 归零，MINOR +1
□ 4. 在同一个 commit 中更新 plugin.json 的 version
□ 5. 同步更新 README.md 和 README.zh-CN.md 顶部 badge 中的版本号
□ 6. commit message 中包含版本号
```

**跳过 bump**: `.gitignore`, `LICENSE`, 纯注释（无行为变化）

### Examples

| Before | Action | After | OK? |
| --- | --- | --- | --- |
| `1.0.3` | patch | `1.0.4` | ✅ |
| `1.0.9` | patch carry | `1.1.0` | ✅ |
| `1.1.9` | patch carry | `1.2.0` | ✅ |
| `1.2.4` | user says "bump major" | `2.0.0` | ✅ |
| `1.0.5` | agent jumps | `1.4.0` | ❌ |
| `1.3.0` | agent bumps major | `2.0.0` | ❌ |

---

## Changelog & Release

### 三层记录体系

| 层级 | 文件 | 粒度 | 何时写 |
| --- | --- | --- | --- |
| **Git log** | git commit messages | 每次 commit | 自动 |
| **CHANGELOG.md** | `CHANGELOG.md` | 每次 MINOR 进位 | 进位时汇总该轮所有 patch |
| **GitHub Release** | GitHub Releases | 每次 MINOR 进位 | 与 CHANGELOG 同步 |

### CHANGELOG 规则

> **不逐 PATCH 写 CHANGELOG**。在 MINOR 进位时（如 1.0.9 → 1.1.0），回顾该 MINOR 周期内所有 commit，汇总为一个 release entry。

**写入内容（汇总时）：**

- 新增 skill / template / reference
- Skill 输出格式或行为变化
- 风险模型、凭据规则、运行验证规则变化
- Obsidian/Dataview 模板结构变化
- 影响用户判断的 bug fix
- Breaking change（标记 `⚠️ Breaking`）

**跳过：**

- `.gitignore`, `LICENSE`, `CLAUDE.md` 内部编辑
- 非模板文字的 typo 修复
- 输出行为不变的重构

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) style.
Group entries under: `Added`, `Changed`, `Fixed`, `Removed`.

### Release 规则

在 MINOR 进位时执行：

1. 更新 `CHANGELOG.md`
2. `git tag v{{version}}`
3. `gh release create v{{version}}`
4. 不在 PATCH 级别打 tag 或发 release

---

## Commit Messages

Use Conventional Commits:

```text
feat(skill-inspector): short description (v1.0.1)
fix(skill-inspector): short description (v1.0.2)
docs: short description (v1.0.3)
```

Always include the version bump in the commit that triggers it. Do not make a separate "bump version" commit.

---

## Skill File Rules

- Root `SKILL.md` is the skill entrypoint.
- Every reusable template lives in `templates/`.
- Heavy review instructions live in `references/`.
- Run `python3 scripts/validate_skill.py` before commit.
- Reports must keep risk near the top and mark missing evidence as unverified.
