# 手机文件分享 (可选进阶)

⚠️ **需要自建HTTPS endpoint**，不是开箱即用。

## 能做什么

```
手机点分享 → 快捷指令/Tasker → POST到你的endpoint → 处理并返回
```

## iOS快捷指令

1. 创建快捷指令
2. 添加"从共享表单获取"
3. 添加"获取URL内容" - POST到 `https://your-domain.com/api/share`
4. 开启"在共享表单中显示"

## Android Tasker

1. 创建Task
2. 添加HTTP Request动作
3. 配置桌面按钮或分享菜单触发

## 阻点

**必须自己实现**:
- HTTPS接收服务器
- API鉴权机制
- 文件存储逻辑
- 响应处理

**不能假设**:
- Muse不是常驻公网服务
- localhost不跨设备
- 云端Agent访问不到手机本地地址

## 最小endpoint示例

```python
# 仅供参考，需要自己部署到公网HTTPS服务
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/share", methods=["POST"])
def share():
    data = request.json
    # 自己实现: 验证、存储、处理
    return jsonify({"status": "ok"})
```

**部署**: 阿里云/腾讯云/AWS等，需要域名、SSL证书

## 参考

- iOS: [快捷指令文档](https://support.apple.com/guide/shortcuts/run-a-shortcut-from-another-app-apd163eb9f95/ios)
- Android: [Tasker官网](https://tasker.joaoapps.com/)

**核对日期**: 2026-11-22 (Asia/Singapore)
