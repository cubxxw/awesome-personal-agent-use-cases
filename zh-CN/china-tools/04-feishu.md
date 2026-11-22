# 飞书文档 (待验证，不推荐新手)

⚠️ **配置步骤未完整核实**，本文档仅说明官方能力范围和阻点，不提供可直接执行的配置。

## 阻点说明

### 阻点1: 官方文档未提供可复现的endpoint获取方式

官方 [开发者调用远程MCP](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN) 页面描述了"HTTP `/mcp`调用方式"，但：

- 未明确实际endpoint URL格式
- 未说明如何获取具体的MCP服务地址
- UAT/TAT获取流程未在该页详细描述

### 阻点2: 两种MCP能力矛盾

**远程MCP文档**称:
- "搜索、读取、新建、更新文档"
- "部分工具只支持UAT"

但同时又说:
- "获取文档暂不支持多维表格、电子表格、任务和日程内容"

这里"创建/更新"与"只读"的关系需要在实际测试后明确。

### 阻点3: 权限申请流程缺失

文档要求"创建自建应用、申请API权限"，但：
- 哪些权限对应哪些MCP工具
- 敏感权限的审批条件
- 个人vs企业的权限差异

这些在所读页面未详细说明。

## 官方能力范围(已核实存在)

### 远程MCP (官方托管)

**来源**: [开发者调用远程MCP](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)

**所读页面确认的工具**:
- 搜索文档
- 读取文档
- 新建文档
- 更新文档
- 列知识空间文档
- 读取/添加评论

**明确限制**:
- 不支持多维表格内容
- 不支持电子表格内容
- 不支持任务和日程内容

**身份类型**:
- UAT: 用户身份 (代表已授权用户)
- TAT: 应用身份 (需要文档单独授权)

### 本地OpenAPI MCP (自部署)

**来源**: [本地MCP概述](https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN)

**覆盖范围**:
- 消息
- 群组
- 日历
- 多维表格

**示例**:
- 群消息汇总到多维表格
- 初始化项目多维表
- 创建群聊和机器人发卡片

**限制**:
- 读取群内所有消息需要敏感权限
- 机器人必须在群中
- 不能无限制读取私人聊天
- 灰度API暂不支持
- 图片/文件上传下载API暂不支持

## 如果要尝试配置(风险自负)

### 前置条件

1. **飞书账号**
2. **开放平台开发者权限**
3. **企业管理员协助**(如需敏感权限)

### 远程MCP尝试路径(未完整验证)

1. 登录 https://open.feishu.cn
2. 创建企业自建应用
3. 申请文档相关API权限
4. 获取应用凭证(App ID、App Secret)
5. ⚠️ **endpoint获取方式未明确**
6. 配置到MCP Host

### 本地MCP尝试路径(未完整验证)

1. 查找官方CLI工具(所读概述未给出安装命令)
2. ⚠️ **启动命令未在概述页明确**
3. 配置stdio transport到Host

## 为什么不推荐新手

1. **endpoint不明确**: 远程MCP没有类似"https://mcp.feishu.cn/xxx"的公开地址
2. **配置步骤缺失**: 官方文档描述了能力，但未给出可复现的配置步骤
3. **权限复杂**: 涉及企业审批、敏感权限、机器人配置
4. **能力分散**: 远程和本地两套系统，能力不重叠

## 替代方案

如果只需要读写文档：
- 使用飞书官方客户端
- 或等待更完整的配置文档

如果需要自动化：
- 考虑飞书开放API(非MCP)
- 参考 https://open.feishu.cn/document/server-docs/docs

## 参考文档

已实际访问，访问日期: 2026-11-22 (Asia/Singapore)

- [开发者调用远程MCP](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN) - 未标注更新时间
- [本地MCP概述](https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN) - 未标注更新时间

## 结论

**不计入完整路径**。等待:
1. 官方提供明确endpoint获取方式
2. 完整的配置步骤文档
3. 清晰的权限申请流程

或由实际配置成功的用户贡献经验。

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**状态**: 待验证，配置步骤未完整核实  
**建议**: 新手跳过此项，优先使用高德、坚果云、Bark等步骤明确的工具
