# skill-inspector 测评报告：paper-research-skill

## 一句话结论

paper-research-skill 适合已经使用 Zotero 和 Obsidian 的研究者，用来把论文发现、整理和笔记沉淀串成工作流；新手应先做源代码审查和最小 demo。

## 推荐程度

recommended-with-caution。功能目标清晰，但依赖链较长，需要确认 CLI、账号登录和本地文件写入边界。

## 风险等级

medium。主要风险是本地文献库写入、外部 API key 使用和 Obsidian vault 修改。

## 它到底是什么

它本质上是论文研究工作流 skill，不是自动判断论文质量的专家系统。它能减少检索、摘要、归档和笔记串联的重复劳动。

## 适合谁 / 不适合谁

适合已经有 Zotero、Obsidian 和 Claude Code 使用习惯的人。不适合只想一次性读一篇论文、没有本地知识库、或不愿处理 API key 的用户。

## 主要坑点

- 需要确认是否会写入 Zotero 条目、Obsidian vault 或本地缓存。
- 如果依赖第三方搜索 API，额度、隐私和撤销方式要提前看清。

## 安装前检查清单

☐ 是否需要 API key  
☐ 是否需要 CLI  
☐ 是否需要登录账号  
☐ 是否会写本地文件  
☐ 是否有最小 demo  
☐ 是否需要浏览器扩展或后台服务  
☐ 是否涉及自动发布、删除、评论、点赞或服务器操作

## 是否建议运行 demo

建议只在临时 vault、测试 Zotero library 或复制出来的论文样本上运行最小 demo，不接主账号 cookie。

## 开发者审计细节

- 文件读写：重点检查 Obsidian vault、Zotero storage 和下载目录。
- 命令执行：确认安装脚本、CLI 调用和后台服务是否透明。
- 网络请求：识别论文搜索、模型 API 和元数据服务的请求目标。
- 凭据处理：优先使用低权限测试 key，并记录撤销方式。
- 维护状态：查看 stars、forks、最近提交、issues 和 README 更新是否一致。

## 证据来源

- 第一信源：README、SKILL.md、安装脚本和仓库源码。
- 第二信源：GitHub issues、讨论区和用户反馈。
- 未验证内容：实际摘要质量、长期稳定性和复杂 vault 下的写入行为。
