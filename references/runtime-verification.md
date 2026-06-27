# Runtime Verification

Source review comes first. Do not run, install, log in, or connect credentials unless the user chooses a deeper mode and user approves the action.

## Easy To Verify

A tool is easy to verify when:

- It has clear installation steps.
- It has a minimal demo, sample prompt, or test command.
- It does not need a real account, production API key, or main cookie.
- It can run in a temporary folder or test repository.
- It does not modify important files by default.
- The result can be directly inspected.

## Not Easy To Verify

A tool is not easy to verify when:

- It needs a real account or main-account cookie.
- It needs production data, production API keys, server access, or database credentials.
- The install script is opaque.
- It may modify files or configuration broadly.
- It has no minimal example.
- The output is too subjective to validate meaningfully.

## Ask Before Running

If a minimal demo looks safe, ask:

```text
这个工具看起来可以安全地跑一个最小 demo。
要不要我在临时目录里试一下？
我会只做最小验证，不接真实账号，不碰你的真实项目。
```

If it does not look safe, say:

```text
我不建议现在直接运行它。
原因是：它需要真实账号登录 / 会写入本地配置 / 没有最小 demo。
更安全的做法是先读代码，或者准备测试账号和测试目录。
```

## Verification Checklist

When the user approves a demo, record:

- Whether installation follows README exactly
- Missing setup steps
- Extra dependencies
- Network access
- File reads/writes
- Login or credential prompts
- Demo success or failure
- Whether output matches project claims
- Errors, warnings, or hangs
- Background processes, caches, or config files left behind

## Result Explanation

If the user wants to see output, include:

```text
运行结果
实际输出
截图/日志摘要
和 README 宣传是否一致
这个结果能说明什么
这个结果不能说明什么
```
