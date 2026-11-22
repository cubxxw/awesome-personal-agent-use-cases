# 坚果云 WebDAV 原件持久存储

**核对日期**: 2026-11-22 (Asia/Singapore)  
**官方文档**: [坚果云第三方应用授权WebDAV开启方法](https://help.jianguoyun.com/?p=2064)

## 用户需求

"以后我找某次出差材料,能看到原始PDF、对应确认邮件和当时整理的说明,而不是只剩一段聊天摘要。"

## 具体结果

1. **跨设备访问**: 手机保存的文件,电脑能打开
2. **原件保留**: PDF/图片/文档原样存储
3. **元数据分离**: 文件说明保存在单独的索引中
4. **版本历史**: 坚果云自带版本管理(根据套餐)
5. **搜索入口**: 通过文件名、标签或全文索引查找

## 适用环境

### Host要求

✅ **可用**:
- 本地MCP Host (通过WebDAV客户端)
- 云端Agent (需要能访问 https://dav.jianguoyun.com)
- 任何支持WebDAV协议的环境

### OS要求

- 服务端: 坚果云云端 (无OS限制)
- 客户端: Windows / macOS / Linux / iOS / Android

## 前置条件

### 1. 坚果云账号

**注册**:
1. 访问 https://www.jianguoyun.com
2. 注册个人账号
3. 完成邮箱验证

**⚠️ 待核实**:
- 实名要求
- 商业使用条款
- 具体免费额度数字

**已知限制** (来自2021年官方文档):
- 上传大小限制
- 访问频率限制  
- 单次列举文件数量限制

**⚠️ 注意**: 以上数字来自2021年发布的文档,当前套餐需要在官网确认。

### 2. 生成应用密码

**步骤**:
1. 登录坚果云网页版
2. 进入 账户信息 → 安全选项
3. 点击"添加应用密码"
4. 输入应用名称 (如 "Personal Agent")
5. 记录生成的密码 (只显示一次)

**安全要点**:
- 应用密码不是账号密码
- 可以单独吊销
- 建议每个应用使用独立密码

### 3. WebDAV客户端或工具

**方式A - WebDAV库** (Python示例):

```bash
pip install webdavclient3
```

**方式B - 命令行工具**:

```bash
# Linux/macOS
brew install cadaver

# Windows
# 使用WinSCP或其他WebDAV客户端
```

## 配置步骤

### 步骤1: 测试WebDAV连接

**使用curl测试**:

```bash
curl -u "your_email@example.com:your_app_password" \
     https://dav.jianguoyun.com/dav/ \
     -X PROPFIND
```

**预期响应**: XML格式的目录列表

**失败则检查**:
- 邮箱地址是否正确
- 应用密码是否正确
- 网络是否能访问坚果云

### 步骤2: Python WebDAV工具示例

**安装依赖**:

```bash
pip install webdavclient3
```

**基础封装** (`jianguoyun_client.py`):

```python
from webdav3.client import Client
import os
from pathlib import Path

class JianGuoYunClient:
    def __init__(self, email, app_password):
        self.client = Client({
            'webdav_hostname': 'https://dav.jianguoyun.com/dav/',
            'webdav_login': email,
            'webdav_password': app_password,
            'webdav_timeout': 30
        })
    
    def list_files(self, remote_path='/'):
        """列出目录内容"""
        try:
            files = self.client.list(remote_path)
            return [f for f in files if f != remote_path]
        except Exception as e:
            return {"error": str(e)}
    
    def upload_file(self, local_path, remote_path):
        """上传文件"""
        try:
            self.client.upload_sync(
                remote_path=remote_path,
                local_path=local_path
            )
            return {"success": True, "path": remote_path}
        except Exception as e:
            return {"error": str(e)}
    
    def download_file(self, remote_path, local_path):
        """下载文件"""
        try:
            self.client.download_sync(
                remote_path=remote_path,
                local_path=local_path
            )
            return {"success": True, "path": local_path}
        except Exception as e:
            return {"error": str(e)}
    
    def file_exists(self, remote_path):
        """检查文件是否存在"""
        return self.client.check(remote_path)

# 使用示例
if __name__ == "__main__":
    client = JianGuoYunClient(
        email="your_email@example.com",
        app_password="your_app_password"
    )
    
    # 列出根目录
    files = client.list_files('/')
    print("根目录文件:", files)
    
    # 上传测试
    result = client.upload_file(
        local_path='./test.txt',
        remote_path='/agent-files/test.txt'
    )
    print("上传结果:", result)
```

### 步骤3: 创建目录结构

**推荐结构**:

```
/agent-files/              # Agent专用目录
├── inbox/                 # 新文件暂存
├── processed/             # 已处理文件
│   ├── documents/        # 文档
│   ├── images/           # 图片
│   └── receipts/         # 票据
├── metadata/             # 元数据和索引
│   └── index.json        # 文件索引
└── archive/              # 归档
```

**创建目录**:

```python
def setup_directories(client):
    """创建初始目录结构"""
    dirs = [
        '/agent-files/inbox/',
        '/agent-files/processed/documents/',
        '/agent-files/processed/images/',
        '/agent-files/processed/receipts/',
        '/agent-files/metadata/',
        '/agent-files/archive/'
    ]
    
    for d in dirs:
        try:
            if not client.file_exists(d):
                client.client.mkdir(d)
                print(f"创建目录: {d}")
        except Exception as e:
            print(f"创建 {d} 失败: {e}")
```

## 最小测试

### 测试1: 上传文本文件

**创建测试文件**:

```bash
echo "这是测试内容,当前时间: $(date)" > test-upload.txt
```

**Python测试脚本**:

```python
from jianguoyun_client import JianGuoYunClient
import os

# 配置 (从环境变量读取)
EMAIL = os.environ.get("JGY_EMAIL")
PASSWORD = os.environ.get("JGY_APP_PASSWORD")

client = JianGuoYunClient(EMAIL, PASSWORD)

# 上传
result = client.upload_file(
    local_path='./test-upload.txt',
    remote_path='/agent-files/test-upload.txt'
)

if 'error' in result:
    print(f"❌ 上传失败: {result['error']}")
else:
    print(f"✅ 上传成功: {result['path']}")
    
    # 验证: 下载回来对比
    client.download_file(
        remote_path='/agent-files/test-upload.txt',
        local_path='./test-download.txt'
    )
    
    with open('./test-upload.txt') as f1, \
         open('./test-download.txt') as f2:
        if f1.read() == f2.read():
            print("✅ 内容校验通过")
        else:
            print("❌ 内容不一致")
```

**预期输出**:
```
✅ 上传成功: /agent-files/test-upload.txt
✅ 内容校验通过
```

### 测试2: 文件列表

**测试脚本**:

```python
files = client.list_files('/agent-files/')
print("目录内容:")
for f in files:
    print(f"  - {f}")
```

**预期输出**:
```
目录内容:
  - inbox/
  - processed/
  - metadata/
  - archive/
  - test-upload.txt
```

### 测试3: 检查文件是否存在

```python
paths = [
    '/agent-files/test-upload.txt',
    '/agent-files/not-exist.txt'
]

for path in paths:
    exists = client.file_exists(path)
    status = "✅ 存在" if exists else "❌ 不存在"
    print(f"{path}: {status}")
```

## 完整使用场景

### 场景: 保存手机分享的文件

**流程**:

```
手机分享文件 (通过02-phone-share)
   ↓
接收端收到文件数据
   ↓
生成文件名: {timestamp}_{original_name}
   ↓
上传到坚果云 /agent-files/inbox/
   ↓
创建元数据记录
   ↓
返回: 文件ID和访问路径
   ↓
(可选) Bark推送通知
```

**代码实现**:

```python
import uuid
from datetime import datetime
from pathlib import Path
import json

def save_shared_file(client, file_data, original_name, note=""):
    """保存分享的文件"""
    
    # 1. 生成唯一文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_id = str(uuid.uuid4())[:8]
    ext = Path(original_name).suffix
    new_name = f"{timestamp}_{file_id}{ext}"
    
    # 2. 保存文件到本地临时目录
    temp_path = f"/tmp/{new_name}"
    with open(temp_path, 'wb') as f:
        f.write(file_data)
    
    # 3. 上传到坚果云
    remote_path = f"/agent-files/inbox/{new_name}"
    result = client.upload_file(temp_path, remote_path)
    
    if 'error' in result:
        return {"error": result['error']}
    
    # 4. 创建元数据
    metadata = {
        "file_id": file_id,
        "original_name": original_name,
        "remote_path": remote_path,
        "timestamp": timestamp,
        "note": note,
        "size_bytes": Path(temp_path).stat().st_size,
        "uploaded_at": datetime.now().isoformat()
    }
    
    # 5. 保存元数据到索引
    save_metadata(client, metadata)
    
    # 6. 清理临时文件
    Path(temp_path).unlink()
    
    return {
        "success": True,
        "file_id": file_id,
        "remote_path": remote_path,
        "metadata": metadata
    }

def save_metadata(client, metadata):
    """保存元数据到索引文件"""
    index_path = '/agent-files/metadata/index.json'
    
    # 下载现有索引
    local_index = '/tmp/index.json'
    if client.file_exists(index_path):
        client.download_file(index_path, local_index)
        with open(local_index) as f:
            index = json.load(f)
    else:
        index = {"files": []}
    
    # 添加新记录
    index["files"].append(metadata)
    
    # 上传更新后的索引
    with open(local_index, 'w') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    client.upload_file(local_index, index_path)
```

## 进阶功能

### 1. 自动分类

```python
def auto_classify(filename, content_type):
    """根据文件类型自动分类"""
    
    if content_type.startswith('image/'):
        return '/agent-files/processed/images/'
    elif filename.endswith('.pdf'):
        return '/agent-files/processed/documents/'
    elif 'receipt' in filename.lower() or 'invoice' in filename.lower():
        return '/agent-files/processed/receipts/'
    else:
        return '/agent-files/processed/documents/'
```

### 2. 全文搜索索引

```python
def build_search_index(client):
    """构建搜索索引"""
    index_data = {
        "files": [],
        "last_updated": datetime.now().isoformat()
    }
    
    # 递归扫描所有文件
    for category in ['documents', 'images', 'receipts']:
        base_path = f'/agent-files/processed/{category}/'
        files = client.list_files(base_path)
        
        for f in files:
            if f.endswith('/'):
                continue  # 跳过目录
            
            # 获取文件信息
            file_info = {
                "path": f"{base_path}{f}",
                "name": f,
                "category": category
            }
            
            # 对于文本文件,提取内容
            if f.endswith('.txt'):
                content = download_and_extract_text(client, f"{base_path}{f}")
                file_info["content_preview"] = content[:200]
            
            index_data["files"].append(file_info)
    
    # 保存索引
    with open('/tmp/search_index.json', 'w') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)
    
    client.upload_file('/tmp/search_index.json', 
                      '/agent-files/metadata/search_index.json')
    
    return index_data
```

### 3. 文件去重

```python
import hashlib

def calculate_file_hash(file_path):
    """计算文件SHA256哈希"""
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            sha256.update(chunk)
    return sha256.hexdigest()

def check_duplicate(client, file_hash, index):
    """检查是否重复文件"""
    for existing in index.get("files", []):
        if existing.get("sha256") == file_hash:
            return {
                "is_duplicate": True,
                "existing_file": existing
            }
    return {"is_duplicate": False}
```

## 重开/持久化

### 数据持久化

**✅ 自动持久化**:
- 文件保存在坚果云云端
- 多设备自动同步
- 版本历史自动保留

**⚠️ 本地缓存**:
- WebDAV客户端不会自动缓存
- 每次访问都是实时请求
- 需要网络连接

### 索引维护

**定期重建索引**:

```python
# 建议每天重建一次
def scheduled_index_rebuild():
    client = JianGuoYunClient(EMAIL, PASSWORD)
    print(f"开始重建索引: {datetime.now()}")
    index = build_search_index(client)
    print(f"索引完成,共 {len(index['files'])} 个文件")
```

**增量更新**:

```python
def incremental_index_update(client, new_files):
    """增量更新索引"""
    # 下载现有索引
    # 添加新文件
    # 上传更新后的索引
    pass
```

## 关闭/撤销方法

### 1. 吊销应用密码

1. 登录坚果云网页版
2. 账户信息 → 安全选项
3. 找到对应应用密码
4. 点击"删除"

**副作用**:
- 所有使用该密码的连接立即失败
- 文件仍然保留在坚果云

### 2. 清理文件

**谨慎操作**:

```python
def cleanup_agent_files(client, confirm=False):
    """清理Agent文件目录"""
    if not confirm:
        print("⚠️ 此操作将删除所有文件,请设置 confirm=True")
        return
    
    # 删除整个目录
    client.client.clean('/agent-files/')
    print("✅ 已清理 /agent-files/")
```

**建议**:
- 先下载备份
- 分类清理,不要一次全删
- 保留元数据索引

### 3. 停用WebDAV工具

```bash
# 卸载Python库
pip uninstall webdavclient3

# 删除配置
rm ~/.webdav_config

# 清理凭证
unset JGY_EMAIL
unset JGY_APP_PASSWORD
```

## 已知限制

### 1. 官方限制 (2021年文档)

⚠️ **待核实当前值**:
- 上传文件大小限制
- API访问频率限制
- 单次列举文件数量限制

**来源**: [官方文档](https://help.jianguoyun.com/?p=2064), 发表2021-01-05

### 2. WebDAV协议限制

- 不支持部分上传(断点续传)
- 大文件上传超时风险
- 并发上传有限制

### 3. 网络依赖

- 需要稳定网络连接
- 国内访问速度良好
- 海外访问可能较慢

### 4. 同步延迟

- 多设备同步有延迟
- 版本冲突可能发生
- 需要手动处理冲突

## 故障排查

### 问题1: 认证失败

**错误信息**: `401 Unauthorized`

**可能原因**:
- 邮箱地址错误
- 应用密码错误
- 密码已过期/被吊销

**解决方法**:
1. 重新生成应用密码
2. 检查邮箱大小写
3. 确认密码复制完整

### 问题2: 上传失败

**错误信息**: `507 Insufficient Storage` 或超时

**可能原因**:
- 账户空间不足
- 文件太大
- 网络超时

**解决方法**:
1. 检查账户剩余空间
2. 分片上传大文件
3. 增加超时时间

### 问题3: 文件列表为空

**可能原因**:
- 路径不存在
- 权限不足
- 目录确实为空

**解决方法**:
1. 检查路径拼写
2. 确认目录已创建
3. 用网页版核实

### 问题4: 中文文件名乱码

**可能原因**:
- 编码问题
- 客户端不支持UTF-8

**解决方法**:
```python
# 确保使用UTF-8编码
filename_utf8 = filename.encode('utf-8').decode('utf-8')
```

## 参考链接

- [坚果云第三方应用授权WebDAV开启方法](https://help.jianguoyun.com/?p=2064) - 发表2021-01-05
- [Zotero7连接坚果云示例](https://help.jianguoyun.com/?p=3168) - 发表2024-11-02 (用于核对WebDAV地址)

**WebDAV协议**:
- [RFC 4918 - WebDAV规范](https://datatracker.ietf.org/doc/html/rfc4918)
- [WebDAV Python库文档](https://github.com/ezhov-evgeny/webdav-client-python-3)

---

**最后更新**: 2026-11-22  
**核对日期**: 2026-11-22 (Asia/Singapore)  
**证据等级**: ⭐⭐ (官方WebDAV已确认,具体配额待核实)  
**未验证部分**: 当前免费额度数字、商业使用条款、2021年后的限制变化
