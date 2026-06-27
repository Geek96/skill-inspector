# Credential Handling

Core rule:

```text
凭据使用要匹配用户目标。
能不接就不接；必须接时，用最小权限、最小范围、可撤销的方式接。
```

## Credential Levels

```text
0. 不接凭据：只做判断
1. 测试凭据：看 demo
2. 低权限真实凭据：个人试用
3. 受控生产凭据：团队/长期使用前审计
```

## By User Intent

### Just deciding whether it is worth installing

Do not use API key, CLI login, account login, or cookies. Use docs, code, issues, and social evidence.

### Seeing a demo result

Prefer test keys, test accounts, low-permission tokens, and free quota. If credentials are unavailable, state what cannot be verified.

### Preparing for personal real use

Guide configuration only after explaining permissions, cost, data exposure, and account risk. Prefer minimum permissions.

### Preparing for long-term or team use

Audit credential storage, log leakage, permission scope, revocation, rollback, and maintenance.

## For Every Credential Request

Explain:

- Why it is needed
- What permissions it opens
- What can go wrong
- How to reduce risk
- How to revoke it

## Sensitive Credential Red Flags

These are not absolutely forbidden, but require strong warning and safer alternatives:

- Main-account cookies
- Production API keys
- Server root access
- High-permission cloud tokens
- Production database connection strings
- Private SSH keys
- Permissions that can publish, delete, or modify content
