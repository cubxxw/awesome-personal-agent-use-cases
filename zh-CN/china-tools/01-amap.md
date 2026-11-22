# 高德地图 POI 与导航

找具体地点、规划路线、生成手机可打开的高德App链接。

## 能做什么

根据[官方能力概述](https://lbs.amap.com/api/mcp-server/summary)，工具可以:
- 关键词/周边搜索POI
- 地理编码/逆地理编码
- 步行/骑行/驾车/公交路径规划
- 距离测量
- 天气查询
- 生成专属地图链接(导入高德App)
- 生成导航/打车唤端链接

## 第一步: 获取高德API Key

1. 访问 https://lbs.amap.com/api/mcp-server/create-project-and-key
2. 注册/登录高德开放平台
3. 创建应用并添加Key，选择"Web服务"类型
4. 复制生成的Key

## 第二步: 配置MCP到Cursor

**官方参考客户端**: Cursor (根据官方[快速接入](https://lbs.amap.com/api/mcp-server/gettingstarted)文档)

### 方案A: Streamable HTTP (官方推荐)

**来源**: [快速接入 - 1.3节](https://lbs.amap.com/api/mcp-server/gettingstarted)

1. 安装Cursor并登录
2. 进入Cursor设置界面配置MCP
3. 添加以下配置(逐字引用官方):

```json
{
  "mcpServers": {
    "amap-maps-streamableHTTP": {
      "url": "https://mcp.amap.com/mcp?key=您在高德官网上申请的key"
    }
  }
}
```

将 `您在高德官网上申请的key` 替换为你的真实Key

4. 返回Cursor设置界面查看MCP服务工具状态
5. 选择Agent模式 (CTRL/CMD + L)
6. 开始使用

### 方案B: Node.js I/O

**来源**: [快速接入 - 2.4节](https://lbs.amap.com/api/mcp-server/gettingstarted)

**前置条件**:
- Node.js >= v22.14.0
- npm镜像源为 `https://registry.npmjs.org/` (检查命令: `npm config get registry`)

**配置**(逐字引用官方):

```json
{
  "mcpServers": {
    "amap-maps": {
      "command": "npx",
      "args": ["-y", "@amap/amap-maps-mcp-server"],
      "env": {
        "AMAP_MAPS_API_KEY": "您在高德官网上申请的key"
      }
    }
  }
}
```

将 `您在高德官网上申请的key` 替换为你的真实Key

## 第三步: 测试

在Cursor Agent模式中输入:

```
搜索北京市朝阳区的停车场
```

预期: 工具返回POI列表，包含地点名称、地址、经纬度等信息

## 完整能力列表

根据[官方能力概述](https://lbs.amap.com/api/mcp-server/summary) (更新2026-03-17):

| 能力 | 输入 | 输出 |
|------|------|------|
| 关键词搜索 | keywords, city(可选) | POI列表 |
| 周边搜索 | keywords, location, radius(可选) | POI列表 |
| 详情搜索 | POI ID | 详细信息 |
| 地理编码 | address, city(可选) | 经纬度 |
| 逆地理编码 | location | 行政区划地址 |
| IP定位 | IP地址 | 省市adcode |
| 天气查询 | city/adcode | 预报天气 |
| 步行路径规划 | origin, destination | 规划方案 |
| 骑行路径规划 | origin, destination | 规划方案 |
| 驾车路径规划 | origin, destination | 规划方案 |
| 公交路径规划 | origin, destination, city, cityd | 规划方案 |
| 距离测量 | origin, destination | 距离、时间 |
| 生成专属地图 | 行程名称、详情、途径点位 | 唤端链接 |
| 导航到目的地 | 目的地经纬度 | 唤端链接 |
| 打车 | 起终点经纬度 | 唤端链接 |

⚠️ **字段说明**: 具体的输入输出字段名见官方返回结果，本表格仅列出主要参数类型

## 使用示例

```
用户: 我在望京SOHO，想去三里屯，顺路找个药店

过程:
1. 工具搜索望京SOHO周边的药店
2. 返回药店候选列表
3. 用户选择某个药店
4. 工具规划路线: 望京SOHO → 药店 → 三里屯
5. 返回距离、时间、分段指引
6. 生成高德App可打开的链接

结果: 工具会返回可在手机打开高德的链接(具体链接格式由工具返回)
```

## 限制

- 搜索结果的POI营业时间、库存等信息可能过时
- 路况预测基于历史数据
- 打车/导航链接需要手机安装高德App
- 免费版API有调用配额限制(具体数字见控制台)

## 故障排查

### 问题1: 配置后Cursor不显示MCP工具

**检查**:
1. Key是否正确填写
2. JSON格式是否正确
3. Cursor是否重启
4. Node.js版本是否 >= v22.14.0 (仅方案B)
5. npm镜像源是否为默认源 (仅方案B)

### 问题2: 工具调用返回错误

常见原因:
- Key无效或已删除
- 超出每日调用配额
- 服务暂时不可用

解决: 登录[高德控制台](https://console.amap.com/)查看Key状态和配额

### 问题3: 手机无法打开唤端链接

原因:
- 未安装高德App
- 系统不支持唤端协议

测试: 先用简单链接测试能否唤起高德App

## 关闭或撤销

1. 在Cursor设置中删除MCP配置
2. (可选) 在高德控制台删除API Key

---

## 已核对的原文依据

所有配置和说明已核对以下官方文档原文:

1. **快速接入** (https://lbs.amap.com/api/mcp-server/gettingstarted) - 更新2026-03-17
   - Streamable HTTP配置 (1.3节): `{"mcpServers":{"amap-maps-streamableHTTP":{"url":"https://mcp.amap.com/mcp?key=..."}}}`
   - Node.js I/O配置 (2.4节): `{"mcpServers":{"amap-maps":{"command":"npx","args":["-y","@amap/amap-maps-mcp-server"],"env":{"AMAP_MAPS_API_KEY":"..."}}}}`
   - Node.js版本要求: v22.14.0或更高
   - npm镜像源检查: `npm config get registry` → https://registry.npmjs.org/

2. **能力概述** (https://lbs.amap.com/api/mcp-server/summary) - 更新2026-03-17
   - 12大核心能力列表
   - 每个工具的输入输出参数说明

3. **创建Key** (https://lbs.amap.com/api/mcp-server/create-project-and-key) - 更新2026-11-21
   - Key获取流程

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**参考客户端**: Cursor (官方文档指定)  
**未实测**: 真实API Key调用、唤端链接格式
