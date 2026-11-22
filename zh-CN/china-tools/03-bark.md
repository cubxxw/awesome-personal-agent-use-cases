# Bark 通知推送 (iOS)

向iPhone推送通知，用于异步任务完成提醒。

## 能做什么

当Agent完成长时间任务后，通过Bark向你的iPhone发送推送通知。

示例:
- 数据爬取完成
- 文件处理完毕
- 定时任务触发

## 前置条件

1. **iOS设备**
2. **安装Bark App**: App Store搜索"Bark"
3. **获取推送Key**: 打开Bark App，复制你的设备Key

## 配置方式

### 方式A: MCP配置 (推荐)

**来源**: [Bark官方教程 - MCP节](https://bark.day.app/tutorial.md)

在MCP Host(如Cursor)中添加配置(逐字引用官方):

```json
{
  "mcpServers": {
    "bark": {
      "type": "http",
      "url": "https://api.day.app/mcp/{key}"
    }
  }
}
```

⚠️ 注意: 将 `{key}` 替换为你的Bark设备Key (在Bark App中获取)

### 方式B: 直接HTTP调用

**来源**: [Bark官方教程 - POST JSON](https://bark.day.app/tutorial.md)

从代码中直接调用(无需MCP):

```bash
curl -X "POST" "https://api.day.app/your_key" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d '{
  "body": "推送内容",
  "title": "推送标题",
  "sound": "minuet",
  "group": "分组"
}'
```

将 `your_key` 替换为你的设备Key

## 测试推送

### 测试1: 基础推送

**输入** (在MCP Host或curl):
```json
{
  "body": "测试消息",
  "title": "测试标题"
}
```

**预期**: iPhone收到Bark通知，显示标题和内容

### 测试2: 带分组和声音

**输入**:
```json
{
  "body": "任务已完成",
  "title": "Agent通知",
  "group": "工作",
  "sound": "calypso"
}
```

**预期**: 收到通知，归类到"工作"分组，播放calypso声音

## 支持的参数

根据[官方教程](https://bark.day.app/tutorial.md):

- `body`: 推送内容 (必需)
- `title`: 推送标题
- `device_key`: 设备Key (当URL路径为/push时使用)
- `group`: 分组
- `sound`: 声音 (如minuet, calypso等)
- `icon`: 图标URL
- `url`: 点击推送跳转的URL
- `badge`: 角标数字
- `copy`: 复制内容
- `subtitle`: 副标题

详细参数说明见官方文档的"请求参数"部分

## 常见问题

### 问题1: 未收到推送

**检查**:
1. Key是否正确
2. iPhone是否联网
3. Bark App是否在后台运行
4. 系统通知权限是否开启

### 问题2: 推送延迟

原因: Bark依赖Apple推送服务(APNs)，可能有延迟

解决: 正常现象，延迟通常在数秒内

### 问题3: 声音不响

检查:
1. iPhone是否静音模式
2. sound参数是否正确(见官方支持列表)

## 关闭或撤销

1. 删除MCP配置
2. 在Bark App中可以重置设备Key (原Key失效)

## 安全建议

- 不要将Key分享给他人
- 不要在公开代码中直接写入Key
- 如Key泄露，在Bark App中重置

---

## 已核对的原文依据

所有配置和说明已核对以下官方文档原文:

1. **Bark官方教程** (https://bark.day.app/tutorial.md) - 访问日期2026-11-22
   - MCP配置 (MCP节): `{"servers":{"bark":{"type":"http","url":"https://api.day.app/mcp/{key}"}}}`
   - POST JSON格式: `curl -X "POST" "https://api.day.app/your_key" -H 'Content-Type: application/json; charset=utf-8' -d '{"body":"...","title":"..."}'`
   - 支持的参数: body, title, device_key, group, sound, icon, url, badge, copy, subtitle
   - URL格式: `/:key/:body`, `/:key/:title/:body`, `/:key/:title/:subtitle/:body`, `/push`

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**官方文档**: https://bark.day.app/tutorial.md  
**未实测**: 真实设备推送
