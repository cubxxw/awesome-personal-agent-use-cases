# 飞书文档

读写云文档、知识库。**区分两种MCP**：远程(只读文档)和本地(包含日历/多维表)。

## 两种接法

### 远程文档MCP (官方托管)

**能力**: 搜索、读取、创建/更新文档，不支持多维表格/日历

**配置**: 官方HTTP `/mcp`端点，支持UAT/TAT
- UAT: 用户身份
- TAT: 应用身份(需文档授权)

**权限**: 需要创建自建应用、申请API权限

### 本地OpenAPI MCP (自部署)

**能力**: 消息、群组、日历、多维表格

**配置**: 本地stdio启动，包装飞书API

**权限**: 
- 读群消息需要敏感权限+机器人在群
- 不能读取所有私聊

## 前置条件

1. **飞书开发者账号**
2. **创建自建应用**
3. **申请对应权限** (根据用途)
4. **企业权限审批** (如需要)

⚠️ **组织限制**: 
- 管理员政策影响可用范围
- 个人≠企业全数据
- 敏感权限需要审批

## 测试

需要实际飞书账号和应用权限，本文档不包含测试步骤。

## 参考

- [远程MCP](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)
- [本地MCP概述](https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN)

(文档未标注更新时间)

**核对日期**: 2026-11-22 (Asia/Singapore)
