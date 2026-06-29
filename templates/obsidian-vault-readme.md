---
title: "{topic_title}"
type: skill-evaluation-readme
category: "{category}"
reviewed_at: "{reviewed_at}"
language: "{language}"
---

# {topic_title}

> [!abstract]
> {中文概括：这个库比较什么、解决什么选择问题、最终推荐用户先看哪里。}

## 推荐入口

- 横向比较：[[{comparison_note_title}]]
- 候选详情：`skills/`

## 本次评估范围

| 项目 | 内容 |
|---|---|
| 评估主题 | {topic_summary} |
| 评估深度 | {review_depth} |
| 输出语言 | {language_label} |
| 最新更新日期 | {latest_update_date} |
| 候选数量 | {candidate_count} |

## 创建前选择流程

1. 语言选择：中文 / English / 双语。
2. 深度选择：快速对比 / 详细评估 / 开发者审计。
3. 目录命名：使用 `YYYY-MM-DD-topic-summary`，日期取调研中发现的最新相关更新日期。

## 目录结构

```text
{directory_name}/
├── README.md
├── comparison/
│   └── {comparison_file_name}
└── skills/
    ├── {candidate_file_one}
    ├── {candidate_file_two}
    └── {candidate_file_three}
```

