# 飞书文档 MCP (待验证)

⚠️ **状态**: 配置步骤未完整验证，不推荐作为首选方案

## 阻点说明

通过WebFetch核对飞书官方MCP文档后，发现以下阻点:

### 阻点1: Endpoint获取方式不明确

[官方远程MCP文档](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)提到:
- "开发者可以直接调用飞书官方提供的HTTP `/mcp`调用方式"
- "UAT/TAT获取方式"

但文档未明确:
- 实际的endpoint URL格式 (如: `https://xxx.feishu.cn/mcp`)
- 如何获取/生成该URL
- UAT/TAT的具体获取步骤

### 阻点2: 权限申请流程缺失

文档要求"创建自建应用、申请API权限"，但:
- 哪些权限对应哪些MCP工具
- 如何申请权限
- 审批条件是什么

这些在所读页面未详细说明。

### 阻点3: 能力边界模糊

远程MCP文档同时提到:
- "搜索、读取、新建、更新文档"
- 但又说"获取文档暂不支持多维表格、电子表格"

"新建、更新"与"暂不支持"的关系需明确。

## 官方能力范围 (已确认存在)

### 远程MCP (官方托管)

**来源**: [开发者调用远程MCP](https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)

**工具列表** (文档提到):
- 搜索文档
- 读取文档
- 新建文档
- 更新文档
- 列知识空间文档
- 读取/添加评论

**明确限制**:
- "获取文档暂不支持多维表格、电子表格、任务和日程内容"

**身份类型**:
- UAT: 用户身份
- TAT: 应用身份

### 本地MCP (自部署)

**来源**: [本地MCP概述](https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN)

**覆盖能力**:
- 消息
- 群组
- 日历
- 多维表格

**示例场景**:
- 群消息汇总到多维表格
- 初始化项目多维表
- 创建群聊和发送卡片

**限制**:
- 读取群内所有消息需要敏感权限
- 机器人必须在群中
- 不能无限制读取私人聊天
- 灰度API暂不支持
- 图片/文件上传下载API暂不支持

## 为什么标记为"待验证"

1. **Endpoint不明确**: 缺少可直接复制粘贴的endpoint URL
2. **配置步骤缺失**: 从零开始的完整配置流程未给出
3. **权限申请未说明**: 需要哪些权限、如何申请
4. **能力边界模糊**: 读写能力的确切范围需明确

## 替代方案

如需读写飞书文档:
1. 使用飞书官方客户端
2. 使用飞书开放API (非MCP): https://open.feishu.cn/document/server-docs/docs
3. 等待更完整的MCP配置文档

## 参考文档

已实际访问 (WebFetch核对):

1. **开发者调用远程MCP** (https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)
   - 访问日期: 2026-11-22
   - 提到: "HTTP `/mcp`调用方式"、UAT/TAT、工具列表
   - 缺失: 实际endpoint URL、获取步骤

2. **本地MCP概述** (https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN)
   - 访问日期: 2026-11-22
   - 覆盖: 消息、群组、日历、多维表格
   - 缺失: 具体安装和启动命令

## 结论

**不计入完整路径**，等待:
1. 官方补充endpoint获取方式
2. 完整的配置步骤文档
3. 清晰的权限申请流程

或由实际配置成功的用户贡献经验。

---

## 已核对的原文依据

通过WebFetch核对以下官方文档:

1. **开发者调用远程MCP** (https://open.feishu.cn/document/mcp_open_tools/developers-call-remote-mcp-server?lang=zh-CN)
   - 访问日期: 2026-11-22
   - 原文提到: "HTTP `/mcp`调用方式"、"UAT/TAT"、工具列表 (搜索、读取、新建、更新文档等)
   - 原文限制: "获取文档暂不支持多维表格、电子表格、任务和日程内容"
   - **缺失**: 实际endpoint URL格式和获取方法

2. **本地MCP概述** (https://open.feishu.cn/document/mcp_open_tools/mcp-overview?lang=zh-CN)
   - 访问日期: 2026-11-22
   - 原文能力: 消息、群组、日历、多维表格
   - **缺失**: 安装命令、启动方式

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**状态**: 待验证 (endpoint和配置步骤未明确)  
**建议**: 跳过此项，优先使用配置明确的工具
