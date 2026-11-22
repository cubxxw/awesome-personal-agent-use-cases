# Bark通知

异步处理结果推送到iPhone，可点击打开链接。

## 能做什么

```
Agent处理完成 → Bark推送 → iPhone通知 → 点击打开结果链接
```

## 前置条件

1. **Bark App**: 
   - App Store搜索"Bark"
   - 安装后获得device key

2. **HTTP接口**: 
   ```bash
   curl -X POST https://api.day.app/push \
     -H "Content-Type: application/json" \
     -d '{
       "device_key": "<YOUR_KEY>",
       "title": "处理完成",
       "body": "文件已保存",
       "url": "https://example.com/result"
     }'
   ```

3. **或MCP配置**:
   ```
   https://api.day.app/mcp/<YOUR_KEY>
   ```

## 测试

```bash
# 发送测试通知
curl -X POST https://api.day.app/push \
  -H "Content-Type: application/json" \
  -d '{
    "device_key": "你的key",
    "title": "测试",
    "body": "这是测试消息"
  }'

# 预期: iPhone收到通知
```

## 限制

- 仅支持iOS
- 需要APNs连通(中国网络可能不稳定)
- 推送成功≠用户已读
- device_key是凭证，不要公开

## 参考

- [使用教程](https://bark.day.app/tutorial.md) - 未标注更新时间
- [MCP配置](https://bark.day.app/) - 官方首页

**核对日期**: 2026-11-22 (Asia/Singapore)
