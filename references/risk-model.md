# Risk Model

Risk is not a label to look smart. It is a practical explanation of what can go wrong.

## Honesty Rules

- Mark uncertain claims as uncertain.
- Do not invent implementation details.
- Do not exaggerate risk to sound cautious.
- Do not reduce risk because the tool is popular.
- Do not treat stars, saves, or README claims as proof.
- Do not soften serious safety issues with cute metaphors.
- Attach evidence to important judgments whenever possible.

## Low Risk

Mostly reads public information, generates text, or organizes information. It does not usually touch local files, accounts, secrets, or servers.

## Medium Risk

Reads or writes local files, calls external APIs, depends on login state, or requires browser extensions. It can often be tested safely with a temporary folder, test account, and backups.

## High Risk

Runs shell commands, changes many files, reads secrets, operates servers, automates posting/commenting/liking, modifies system configuration, or keeps background services running.

## Not Recommended

Use when permissions are unclear, install scripts are suspicious, dangerous operations are undocumented, or the project is poorly maintained while touching important files, accounts, secrets, or infrastructure.

## Required Risk Explanation

For each important risk, write:

```text
风险是什么：
明确说它会动什么，或者可能要求用户交出什么权限。

可能后果：
说明配置错、权限过大、误操作、泄露或风控可能造成什么结果。

降低风险：
给具体做法，例如测试目录、测试账号、低权限 key、备份、只读 token、运行后撤销。
```

## High-Risk Triggers

Highlight these actions near the top of the report:

- Deleting, moving, or overwriting files
- Running shell commands
- Reading `.env`, SSH keys, tokens, cookies, or browser sessions
- Using main-account cookies
- Posting, liking, commenting, sending messages, or deleting content
- Operating cloud servers, databases, or production APIs
- Installing unknown binaries
- Running long-lived background services
- Uploading local files to third-party services
