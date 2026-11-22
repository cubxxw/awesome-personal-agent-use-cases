# 手机主动分享给 Agent

**核对日期**: 2026-11-22 (Asia/Singapore)  
**官方文档**: 
- iOS: [从其他App运行快捷指令](https://support.apple.com/guide/shortcuts/run-a-shortcut-from-another-app-apd163eb9f95/ios)
- Android: [Tasker官网](https://tasker.joaoapps.com/)

## 用户需求

"看到一份跟项目有关的文件,点分享,选项目,把原件保存进去。等我回电脑,继续拿这份原件工作。"

或者:

"把选中的公开网页链接和一句'为什么保存它'交给Agent。"

## 具体结果

你会拿到:

### iOS路径(快捷指令)

1. **共享表单入口**: 在其他App中点"分享",看到你的快捷指令
2. **内容传递**: 文字、链接、图片或文件传给你的HTTPS接收端  
3. **任务响应**: 立即返回简短结果,或返回任务ID供后续查询
4. **原件保存**: 文件保存到你指定的存储位置(如坚果云)

### Android路径(Tasker)

1. **触发方式**: 桌面按钮、分享菜单或设备事件
2. **HTTP请求**: 向你的Agent接口发送文件或数据
3. **响应保存**: 将处理结果保存到手机文件或显示通知
4. **设备状态**: 可选附带电量、网络等上下文信息

## 适用环境

### iOS快捷指令

**手机端**:
- iOS 14.0 或更高版本
- 需要安装「快捷指令」App(系统自带)

**接收端**:
- 你自己的HTTPS服务器 (可以是云端Agent环境)
- 需要公网可访问的URL
- 支持POST请求接收数据

### Android Tasker

**手机端**:
- Android 5.0+ (不同ROM后台策略不同)
- Tasker App (付费应用,有7天试用)

**接收端**:
- 同iOS,需要HTTPS服务器
- Tasker不要求特定Android版本的系统API

⚠️ **不适用的场景**:
- ❌ 云端Host访问不到 `127.0.0.1` (手机的本地地址)
- ❌ Muse等云端Agent不是手机后台服务
- ❌ 不能自动读取手机上所有App的数据

## 前置条件说明

### 共同前置条件

1. **接收端HTTPS服务**:
   - 公网可访问的URL
   - 支持POST请求
   - 可以接收JSON或multipart/form-data
   - 有鉴权机制(如API Key)

2. **存储位置** (可选):
   - 坚果云WebDAV (参见 [03-jianguoyun-webdav-storage.md](03-jianguoyun-webdav-storage.md))
   - 飞书云文档 (参见 [05-feishu-personal-docs.md](05-feishu-personal-docs.md))
   - 思源笔记本地API

3. **通知出口** (可选):
   - Bark推送 (iOS, 参见 [04-bark-mobile-notification.md](04-bark-mobile-notification.md))
   - Android通知 (通过Tasker)

### iOS特定条件

**已有能力** (Apple官方):
- ✅ 快捷指令可以加入共享表单
- ✅ 获取URL内容 动作支持POST
- ✅ 可以发送文件和JSON

**限制** (Apple官方明确):
- ⚠️ 来源App没有合适的可分享内容时,快捷指令可能不出现
- ⚠️ 不自动获得微信历史、相册全库或任意App数据
- ⚠️ 权限由用户及系统控制

**来源**: [Apple官方快捷指令文档](https://support.apple.com/guide/shortcuts/run-a-shortcut-from-another-app-apd163eb9f95/ios), 未标注更新时间

### Android特定条件

**已有能力** (Tasker官方):
- ✅ HTTP Request动作支持POST、文件上传
- ✅ 可以从分享菜单触发
- ✅ 可以附带设备状态信息

**限制** (Tasker官方明确):
- ⚠️ 文件读取受系统权限与Android存储规则限制
- ⚠️ 后台稳定性取决于ROM的省电策略
- ⚠️ 不是Android官方接口

**来源**: [Tasker官网](https://tasker.joaoapps.com/), 未标注更新时间

## iOS快捷指令完整路径

### 步骤1: 搭建接收端API

**最小示例** (Python Flask):

```python
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
API_KEY = os.environ.get("API_KEY")  # 从环境变量获取

@app.route("/api/share", methods=["POST"])
def handle_share():
    # 验证API Key
    auth = request.headers.get("Authorization")
    if auth != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401
    
    # 获取数据
    data = request.json
    content_type = data.get("type")  # text, url, file
    content = data.get("content")
    note = data.get("note")  # 用户的说明
    
    # 处理逻辑
    if content_type == "url":
        # 保存链接和笔记
        save_to_storage(content, note)
        return jsonify({
            "success": True,
            "message": "链接已保存",
            "id": "saved-123"
        })
    
    elif content_type == "file":
        # 接收base64编码的文件
        file_data = data.get("file_data")
        file_name = data.get("file_name")
        # 解码并保存
        save_file(file_name, file_data)
        return jsonify({
            "success": True,
            "message": f"文件 {file_name} 已保存"
        })
    
    return jsonify({"error": "Unknown type"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```

**部署**:
- 云服务器 (阿里云/腾讯云/AWS)
- Serverless函数 (阿里云函数计算/腾讯云云函数)
- 自托管服务器

**⚠️ 安全要求**:
- 必须使用HTTPS
- API Key不能写进快捷指令分享版本
- 限制请求频率
- 验证文件类型和大小

### 步骤2: 创建快捷指令

#### 2.1 保存链接版本

**快捷指令步骤**:

1. **接收输入**:
   - 添加"从共享表单获取"
   - 类型选择: URL、文本

2. **请求用户输入**:
   - 添加"询问输入"
   - 提示: "为什么保存这个链接?"
   - 输入类型: 文本

3. **发送HTTP请求**:
   - 添加"获取URL内容"
   - URL: `https://your-domain.com/api/share`
   - 方法: POST
   - 请求体: JSON
   - Headers:
     - `Content-Type`: `application/json`
     - `Authorization`: `Bearer <YOUR_API_KEY>`
   
   **请求体内容**:
   ```json
   {
     "type": "url",
     "content": "<共享表单输入>",
     "note": "<提供的输入>",
     "timestamp": "<当前日期>"
   }
   ```

4. **显示结果**:
   - 添加"显示通知"
   - 标题: "已保存"
   - 正文: 使用返回的 JSON 中的 `message`

**配置图示**:

```
[共享表单] 获取 → URL/文本
        ↓
[询问输入] "为什么保存?" → 用户笔记
        ↓
[获取URL内容] POST → your-domain.com/api/share
        ↓
[显示通知] "已保存"
```

#### 2.2 保存文件版本

**快捷指令步骤**:

1. **接收输入**:
   - 类型选择: 文件

2. **获取文件详情**:
   - 添加"获取文件详情" → 名称、大小

3. **编码文件** (对于小文件):
   - 添加"Base64编码"

4. **发送HTTP请求**:
   - 同上,请求体包含:
   ```json
   {
     "type": "file",
     "file_name": "<文件名称>",
     "file_data": "<Base64编码的内容>",
     "note": "<用户说明>"
   }
   ```

⚠️ **文件大小限制**:
- 快捷指令有内存限制
- 建议: 小于10MB直接传输
- 大文件: 先上传到临时存储,传URL

### 步骤3: 添加到共享表单

1. 打开刚创建的快捷指令
2. 点击设置图标(右上角)
3. 开启"在共享表单中显示"
4. 选择接受的类型: URL、文本、文件
5. 保存

### 步骤4: 测试

**测试1: 分享链接**

1. 打开Safari浏览器
2. 访问任意网页
3. 点击"分享"按钮
4. 找到你的快捷指令
5. 输入笔记
6. 查看通知确认成功

**预期**:
- 快捷指令出现在分享菜单
- 可以输入笔记
- 显示"已保存"通知
- 接收端收到请求

**测试2: 分享文件**

1. 打开文件App
2. 选择一个小文件 (< 1MB)
3. 分享到快捷指令
4. 确认接收端收到文件

## Android Tasker完整路径

### 步骤1: 安装Tasker

1. 访问 https://tasker.joaoapps.com/
2. 下载试用版或购买
3. 授予必要权限

**⚠️ 待核实**:
- 国内购买渠道和价格
- 所在地区是否可用
- 不同Android版本兼容性

### 步骤2: 创建Task

#### 2.1 简单POST请求

**配置步骤**:

1. 创建新Task: "分享到Agent"

2. 添加Action: HTTP Request
   - 服务器:端口: `your-domain.com:443`
   - 路径: `/api/share`
   - 方法: POST
   - Content Type: `application/json`
   - 请求体:
     ```json
     {
       "type": "text",
       "content": "%CLIP",
       "note": "从剪贴板分享",
       "device": "Android",
       "battery": "%BATT"
     }
     ```
   - Headers:
     ```
     Authorization: Bearer <YOUR_API_KEY>
     Content-Type: application/json
     ```

3. 添加Action: Flash (显示提示)
   - 文本: "已发送: %HTTPD"

#### 2.2 上传文件

**配置步骤**:

1. 添加Action: 选择文件
   - 变量: `%selected_file`

2. 添加Action: HTTP Request  
   - 文件上传: `%selected_file`
   - 其他同上

### 步骤3: 添加触发方式

#### 方式1: 桌面按钮

1. 长按桌面
2. 添加 Widgets → Tasker → Task Shortcut
3. 选择刚创建的Task

#### 方式2: 分享菜单

1. 创建Profile: Event → UI → Action Sent
2. Action: 选择"分享" (android.intent.action.SEND)
3. 链接到Task

⚠️ **限制**:
- 分享菜单集成在某些App可能不可见
- 系统版本和ROM影响可用性

### 步骤4: 测试

**测试1: 桌面按钮**

1. 复制文字到剪贴板
2. 点击桌面按钮
3. 查看提示确认发送

**测试2: 分享文件**

1. 文件管理器选择文件
2. 分享 → Tasker
3. 确认上传

## 最小测试方案

### 准备测试环境

**测试用接收端** (使用 webhook.site):

1. 访问 https://webhook.site
2. 获得唯一URL: `https://webhook.site/xxx-xxx-xxx`
3. 用这个URL替换你的API endpoint

**优点**:
- 无需搭建服务器
- 实时查看请求
- 方便调试

**限制**:
- 公开URL,不要传真实数据
- 仅用于测试,不用于生产

### iOS测试输入

**测试1: 纯文本**

```
在笔记App中选择一段文字:
"这是测试内容,包含中文和English"

分享到快捷指令
输入笔记: "测试用"
```

**预期响应**:
```json
{
  "type": "text",
  "content": "这是测试内容,包含中文和English",
  "note": "测试用",
  "timestamp": "2026-11-22T10:30:00+08:00"
}
```

**测试2: URL**

```
Safari访问: https://www.example.com
点击分享 → 选择快捷指令
输入笔记: "示例网站"
```

**预期响应**:
```json
{
  "type": "url",
  "content": "https://www.example.com",
  "note": "示例网站"
}
```

### Android测试输入

**测试1: 剪贴板**

```
复制文字: "测试内容123"
点击桌面按钮
```

**预期响应**:
```json
{
  "type": "text",
  "content": "测试内容123",
  "device": "Android",
  "battery": "85"
}
```

**失败识别**:
- 没有收到请求
- 返回401 Unauthorized
- 超时
- 文件内容损坏

## 进阶用法

### 组合1: 手机 → 云存储 → 电脑继续

**流程**:

```
手机分享文件
   ↓
快捷指令POST到接收端  
   ↓
Agent保存到坚果云WebDAV
   ↓
返回文件ID
   ↓
Bark推送通知(带文件链接)
   ↓
电脑打开坚果云继续编辑
```

**实现要点**:
- 接收端调用WebDAV API保存文件
- 返回坚果云的文件访问链接
- Bark通知带上可点击的链接

### 组合2: 批量保存阅读材料

**场景**: 刷微信公众号时保存感兴趣的文章

**流程**:

```
看到好文章 → 分享到快捷指令
   ↓
输入"为什么保存" → 快速笔记
   ↓
Agent提取: 标题、作者、链接、笔记
   ↓
保存到个人知识库(飞书/思源)
   ↓
自动打标签、去重
```

**⚠️ 限制**:
- 公众号文章可能只能获得分享链接
- 全文需要另行访问(可能需要登录)
- 不是自动全文归档

### 组合3: 临时文件快速处理

**场景**: 在外收到合同PDF,需要快速审查

**流程**:

```
邮件中收到PDF
   ↓
分享到快捷指令
   ↓
Agent: OCR识别关键信息
   ↓
返回: 金额、日期、对方公司
   ↓
推送到手机: "合同摘要"
   ↓
原文保存到WebDAV
```

**技术需要**:
- OCR服务 (阿里云/腾讯云OCR API)
- 关键词提取
- 结构化存储

## 重开/持久化

### 快捷指令

**不需要后台运行**:
- ✅ 每次手动分享时触发
- ✅ 接收端持续运行即可
- ❌ 不是自动监控手机

**持久化**:
- 快捷指令配置保存在iPhone
- iCloud同步(如果开启)
- 导入/导出 `.shortcut` 文件

### Tasker

**后台运行**:
- ⚠️ 取决于Android省电策略
- ⚠️ 部分ROM需要手动加白名单
- ✅ 可以设置开机自启

**持久化**:
- Tasker配置保存在本地
- 可以导出为XML备份
- Profile和Task可以独立导出

## 关闭/撤销方法

### iOS快捷指令

**停止使用**:

1. 打开快捷指令App
2. 找到对应快捷指令
3. 设置 → 关闭"在共享表单中显示"
4. 或直接删除快捷指令

**副作用**:
- 分享菜单中不再出现
- 已发送的数据不受影响

### Android Tasker

**停止使用**:

1. 打开Tasker
2. 禁用或删除Profile
3. 删除Task
4. 卸载Tasker App(如果完全不用)

**副作用**:
- 桌面按钮失效
- 分享菜单项消失

### 接收端

**关闭服务**:
- 停止HTTP服务
- 删除DNS记录
- 吊销SSL证书(可选)

**数据清理**:
- 删除已保存的文件
- 清理日志中的API Key
- 撤销关联的存储权限

## 已知限制

### iOS限制

1. **App兼容性**: 不是所有App都支持分享
2. **文件大小**: 大文件可能导致快捷指令崩溃
3. **网络**: 需要手机联网
4. **系统版本**: 老版本iOS功能可能有限

### Android限制

1. **ROM差异**: 不同厂商系统行为不同
2. **权限**: 存储权限限制越来越严
3. **后台**: 激进省电会杀后台
4. **兼容性**: Tasker在部分设备可能不稳定

### 通用限制

1. **不是自动化**: 需要用户主动分享
2. **网络依赖**: 离线时无法使用
3. **安全性**: HTTPS和鉴权必须正确配置
4. **成本**: 服务器、存储、OCR等有费用

## 故障排查

### 问题1: 快捷指令不出现在分享菜单

**iOS**:
1. 检查是否开启"在共享表单中显示"
2. 确认选择了正确的内容类型
3. 尝试重启快捷指令App
4. 系统版本是否支持

### 问题2: HTTP请求失败

**可能原因**:
- URL错误
- API Key错误
- 网络不通
- 服务器关闭
- HTTPS证书问题

**排查步骤**:
1. 用浏览器直接访问URL
2. 检查API Key是否正确
3. 查看服务器日志
4. 用curl测试请求
5. 检查防火墙设置

### 问题3: 文件上传失败

**可能原因**:
- 文件太大
- 格式不支持
- 权限不足
- 超时

**解决方法**:
1. 限制文件大小
2. 检查服务器配置
3. 增加超时时间
4. 改用分片上传

### 问题4: Android后台被杀

**解决方法**:
1. 加入省电白名单
2. 关闭电池优化
3. 锁定后台
4. 使用前台服务(进阶)

## 参考链接

### iOS官方文档

- [从其他App运行快捷指令](https://support.apple.com/guide/shortcuts/run-a-shortcut-from-another-app-apd163eb9f95/ios)
- [在快捷指令中请求API](https://support.apple.com/guide/shortcuts/request-your-first-api-apd58d46713f/ios)

(Apple文档未标注发表/更新时间)

### Android Tasker

- [Tasker官网](https://tasker.joaoapps.com/)
- [HTTP Request动作](https://tasker.joaoapps.com/userguide/en/help/ah_http_request.html)
- [Get Battery Info](https://tasker.joaoapps.com/userguide/en/help/ah_get_battery_info.html)

(Tasker文档未标注更新时间)

### 测试工具

- [Webhook.site](https://webhook.site) - HTTP请求测试
- [Postman](https://www.postman.com) - API测试
- [ngrok](https://ngrok.com) - 本地服务器公网暴露(测试用)

---

**最后更新**: 2026-11-22  
**核对日期**: 2026-11-22 (Asia/Singapore)  
**证据等级**: ⭐⭐ (官方文档存在但未完整端到端验证)  
**未验证部分**: 国内网络到各云服务商的实际连通性、不同Android ROM的兼容性
