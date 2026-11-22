# 高德地图

找具体分店、算路线、生成能在手机打开的地图和导航链接。

## 能做什么

```
输入: "望京SOHO附近的快递代收点和药店，算去三里屯的顺路走法"
输出: POI候选 → 确认店铺 → 路线方案 → 高德App链接
```

## 前置条件

1. **高德API Key**: 
   - 访问 https://lbs.amap.com/api/mcp-server/create-project-and-key
   - 创建应用，选择"Web服务"
   - 复制Key

2. **MCP配置** (HTTP transport):
   ```json
   {
     "transport": {
       "type": "streamableHttp",
       "url": "https://mcp.amap.com/mcp?key=<YOUR_KEY>"
     }
   }
   ```

⚠️ **SSE已下线** (2026-03-17): 不要用 `sse://` 配置

## 测试

```
搜索"北京市 停车场"
预期: 返回POI列表，包含name、address、location
```

## 能力列表

- POI搜索: 关键词 → 候选列表
- 路线规划: 起终点 → 距离、时间、分段指引
- 专属地图: 多个地点 → `amapuri://` 链接
- 导航链接: 目的地坐标 → 导航入口
- 打车链接: 起终点 → 打车入口(不是已下单)
- 城市天气: 城市/adcode → 预报

## 限制

- 营业时间、库存不保证准确
- 路况预测基于历史数据
- 打车链接≠已叫到车
- 需要手机安装高德App打开链接

## 参考

- [快速接入](https://lbs.amap.com/api/mcp-server/gettingstarted) - 更新2026-03-17
- [能力概述](https://lbs.amap.com/api/mcp-server/summary) - 更新2026-03-17

**核对日期**: 2026-11-22 (Asia/Singapore)
