# 高德地图 POI 与导航

找具体地点、比较路线、生成手机能打开的地图和导航链接。

## 能做什么

```
任务: "望京SOHO附近的快递代收点和药店，算去三里屯的顺路走法"
结果: POI候选列表 → 确认具体店铺 → 分段路线方案 → 高德App可打开的链接
```

输出示例：
- 专属地图链接: `amapuri://openFeature?...` (多个地点一起显示)
- 导航链接: `amapuri://route/plan?...` (单个目的地导航)
- 打车链接: `amapuri://showHailCarPage?...` (打开打车界面)

## 第一步: 获取高德API Key

1. 访问 https://lbs.amap.com/api/mcp-server/create-project-and-key
2. 注册/登录高德开放平台
3. 控制台 → 应用管理 → 我的应用 → 创建新应用
4. 添加Key，选择"Web服务"类型
5. 复制生成的Key (格式类似: `1234567890abcdef1234567890abcdef`)

⚠️ **待核实**: 实名要求、免费配额具体数字、商业许可条件

## 第二步: 配置MCP Host

### 方案A: Claude Desktop (已验证的参考)

**适用**: macOS/Windows桌面用户

1. **找到配置文件**:
   ```bash
   # macOS
   ~/Library/Application Support/Claude/claude_desktop_config.json
   
   # Windows
   %APPDATA%\Claude\claude_desktop_config.json
   ```

2. **添加高德MCP配置**:
   ```json
   {
     "mcpServers": {
       "amap": {
         "url": "https://mcp.amap.com/mcp?key=YOUR_ACTUAL_KEY_HERE"
       }
     }
   }
   ```
   
   将 `YOUR_ACTUAL_KEY_HERE` 替换为你的真实Key

3. **重启Claude Desktop**

4. **验证连接**:
   在对话中输入: "搜索北京市朝阳区的停车场"
   
   预期: Claude调用高德MCP返回POI列表

**参考文档**: Claude Desktop MCP配置 (https://modelcontextprotocol.io/quickstart/user)

### 方案B: 官方Node包 (本地命令行)

**适用**: 有Node.js环境的用户

1. **安装Node.js** (需要 >= 22.14.0):
   ```bash
   node --version  # 检查版本
   ```

2. **安装高德MCP包**:
   ```bash
   npm install -g @amap/amap-maps-mcp-server
   ```

3. **配置Host** (以支持stdio的Host为例):
   ```json
   {
     "mcpServers": {
       "amap": {
         "command": "amap-maps-mcp",
         "env": {
           "AMAP_API_KEY": "YOUR_ACTUAL_KEY_HERE"
         }
       }
     }
   }
   ```

4. **测试** (如果Host支持手动调用):
   ```bash
   # 设置环境变量
   export AMAP_API_KEY="your_key"
   
   # 运行MCP服务器(前台测试)
   amap-maps-mcp
   ```

**参考文档**: 高德官方 [快速接入](https://lbs.amap.com/api/mcp-server/gettingstarted) - 更新2026-03-17

### 方案C: HTTP直接调用 (测试用)

**适用**: 验证Key是否有效

```bash
# 测试POI搜索
curl "https://restapi.amap.com/v3/place/text?key=YOUR_KEY&keywords=停车场&city=北京&output=json"
```

预期返回JSON包含 `status: "1"` 和POI列表

⚠️ **注意**: 这是REST API测试，不是MCP调用

## 关于Muse

**Muse配置未核实**: 本文档未确认Muse (https://apps.apple.com/us/app/muse-from-meta/id6760173601) 的具体MCP配置界面或方法。

根据官方安全说明 (https://security.muse.ai/, 2026-09-08)，Muse可以"编写自定义连接器"，但具体如何配置HTTP MCP endpoint未在公开文档找到。

**如果使用Muse**: 
- 高德endpoint: `https://mcp.amap.com/mcp?key=YOUR_KEY`
- 需要自己确认Muse的MCP配置方法
- 可能需要在Muse环境中运行命令或脚本

**本文档选用Claude Desktop作为参考**，因为其配置方法已公开。

## ❌ 不要使用的旧配置

高德官方SSE服务已于 **2026年3月17日下线**。

以下配置不再有效:
```
# ❌ 旧SSE配置(通常是https URL，不是sse://协议)
https://api.amap.com/v3/mcp-sse  # 此类endpoint已停用
```

来源: [高德MCP更新日志](https://lbs.amap.com/api/mcp-server/changelog) - 更新2026-03-17

## 第三步: 测试调用

### 测试1: POI搜索

**输入**:
```
搜索北京市朝阳区的快递代收点，返回前3个结果
```

**预期返回字段**:
- `name`: POI名称 (如"顺丰快递代收点")
- `address`: 详细地址
- `location`: 经纬度 "116.123,39.456"
- `id`: POI唯一标识

### 测试2: 路线规划

**输入**:
```
驾车路线: 从望京SOHO(116.481488,39.990464)到三里屯(116.447174,39.937676)
```

**预期返回**:
- `distance`: 距离(米)
- `duration`: 预计时间(秒)
- `steps`: 分段指引

### 测试3: 生成唤端链接

**输入**:
```
生成导航链接到三里屯坐标
```

**预期返回**: 
```
amapuri://route/plan?dlat=39.937676&dlon=116.447174&dev=0&t=0
```

**验证方法**: 
1. 复制链接
2. 在手机浏览器或备忘录粘贴
3. 点击链接应跳转到高德App

## 完整能力列表

根据官方文档 ([能力概述](https://lbs.amap.com/api/mcp-server/summary) - 更新2026-03-17)：

| 能力 | 输入 | 输出 | 说明 |
|------|------|------|------|
| POI搜索 | 关键词+城市/坐标 | POI候选列表 | 找门店、停车场等 |
| POI详情 | POI ID | 详细信息 | 核对具体分店 |
| 地理编码 | 地址 | 坐标 | 把地址变成可计算的位置 |
| 逆地理编码 | 坐标 | 地址 | 把坐标变成地址 |
| 路线规划 | 起终点坐标 | 距离、时间、方案 | 支持步行/骑行/驾车/公交 |
| 城市天气 | 城市/adcode | 天气预报 | 城市级预报，不到门牌 |
| 专属地图 | 多个途经点 | 地图唤端链接 | 多地点一起展示 |
| 导航链接 | 目的地坐标 | 导航唤端链接 | 进入导航模式 |
| 打车链接 | 起终点坐标 | 打车唤端链接 | 打开打车界面 |

## 实际运行示例

假设使用Claude Desktop已配置好：

```
用户: 我在望京SOHO，要去三里屯，中间想找个药店

Claude调用:
1. POI搜索"药店"，中心点望京SOHO，半径2000米
2. 返回候选药店列表
3. 用户选择某个药店
4. 计算路线: 望京SOHO → 药店 → 三里屯
5. 返回总距离、预计时间、各段路线
6. 生成专属地图链接(包含3个点)
7. 生成分段导航链接

用户点击链接 → 高德App打开 → 显示路线
```

## 限制与注意事项

### 数据准确性
- POI信息可能过时(营业时间、是否关闭)
- 路况预测基于历史数据，不是实时保证
- 官方文档未承诺POI详情的覆盖率

### 功能边界
- 打车链接 ≠ 已叫到车
- 导航链接 ≠ 已开始导航
- 天气预报 ≠ 精确到门牌的实时天气
- 不能查库存、不能预约、不能下单

### 技术依赖
- 需要手机安装高德App打开链接
- 唤端链接在iOS/Android行为可能略有不同
- API Key有配额限制(具体数字待确认)

## 故障排查

### 问题1: 配置后无响应

**检查**:
1. Key是否正确(长度32位)
2. Host是否重启
3. 网络是否能访问 `mcp.amap.com`

**验证Key**:
```bash
curl "https://restapi.amap.com/v3/config/district?key=YOUR_KEY"
```
返回 `status:"1"` 表示Key有效

### 问题2: 返回错误码

常见错误:
- `INVALID_USER_KEY`: Key错误或已删除
- `DAILY_QUERY_OVER_LIMIT`: 超出每日配额
- `SERVICE_NOT_AVAILABLE`: 服务暂时不可用

解决: 登录控制台查看Key状态和配额

### 问题3: 唤端链接无反应

**原因**:
- 手机未安装高德App
- 链接格式错误
- 系统不支持 `amapuri://` 协议

**测试**: 先用简单链接 `amapuri://` 看能否唤起App

## 参考文档

所有链接已实际访问，访问日期: 2026-11-22 (Asia/Singapore)

- [快速接入](https://lbs.amap.com/api/mcp-server/gettingstarted) - 更新2026-03-17
- [能力概述](https://lbs.amap.com/api/mcp-server/summary) - 更新2026-03-17
- [更新日志](https://lbs.amap.com/api/mcp-server/changelog) - 更新2026-03-17
- [创建应用和Key](https://lbs.amap.com/api/mcp-server/create-project-and-key) - 更新2026-11-21

**未核实**: Muse具体配置方法、免费配额数字、商业许可细则

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**参考Host**: Claude Desktop (MCP配置已公开)  
**未实测**: 高德API真实调用(无Key)、Muse配置方法
