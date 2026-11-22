# 坚果云 WebDAV 文件同步

通过WebDAV协议访问坚果云，实现跨设备文件存储。

## 能做什么

- 上传文件到坚果云
- 下载云端文件
- 列出目录内容
- 删除/移动文件

## 前置条件

1. **坚果云账号**: 注册 https://www.jianguoyun.com/
2. **应用授权密码**: 用于WebDAV登录 (不是网页登录密码)

## 第一步: 生成应用授权密码

**来源**: [坚果云帮助 - WebDAV开启方法](https://help.jianguoyun.com/?p=2064)

### 网页端操作

1. 打开坚果云官网 https://www.jianguoyun.com/ 并登录
2. 点击右上角账户名 → 【账户信息】→ 【安全选项】
3. 找到"第三方应用管理"，选择"添加应用密码"
4. 输入名称 (如: MCP)，点击"生成密码"
5. 复制生成的密码 (16位随机密码)

⚠️ **重要**: 此密码只显示一次，请立即保存

### 移动端操作

iOS: 设置 → 第三方应用管理 → 添加应用密码  
Android: 设置 → 第三方应用管理 → 添加

## 第二步: 配置WebDAV客户端

### 连接参数

**来源**: [坚果云帮助](https://help.jianguoyun.com/?p=2064)

- **服务器地址**: `https://dav.jianguoyun.com/dav/`
- **账号**: 你的坚果云邮箱
- **密码**: 应用授权密码 (不是网页登录密码)

### Python示例

需要安装 `webdav3-client`:

```bash
pip install webdav3-client
```

**代码**:

```python
from webdav3.client import Client

options = {
    'webdav_hostname': 'https://dav.jianguoyun.com/dav/',
    'webdav_login': 'your_email@example.com',  # 替换为你的坚果云邮箱
    'webdav_password': 'your_app_password'     # 替换为应用授权密码
}

client = Client(options)

# 列出根目录文件
files = client.list()
for file in files:
    print(file)

# 上传文件
client.upload_sync(remote_path='test.txt', local_path='local_test.txt')

# 下载文件
client.download_sync(remote_path='test.txt', local_path='downloaded.txt')

# 检查文件是否存在
exists = client.check('test.txt')
print(f'文件存在: {exists}')
```

## 测试

### 离线语法测试

```bash
$ python3 -c "
code = '''
from webdav3.client import Client
options = {
    'webdav_hostname': 'https://dav.jianguoyun.com/dav/',
    'webdav_login': 'test@example.com',
    'webdav_password': 'testpass'
}
client = Client(options)
'''
compile(code, '<string>', 'exec')
print('✅ 代码语法正确')
"
```

预期输出: `✅ 代码语法正确`

⚠️ **端到端测试**: 需要真实坚果云账号和应用密码，本文档未进行实际连接测试

## 限制

根据[官方帮助](https://help.jianguoyun.com/?p=2064):

- **上传大小**: 单文件最大500M (默认，私有云可调整)
- **访问频率**: 
  - 免费版: 30分钟内不超过600次请求
  - 付费版: 30分钟内不超过1500次请求
- **目录数**: 单次请求最多750个文件/文件夹，需分页加载

## 常见问题

### 问题1: 401 Unauthorized

原因:
- 使用了网页登录密码 (应使用应用授权密码)
- 应用授权密码过期或删除

解决: 重新生成应用授权密码

### 问题2: 连接超时

检查:
1. 网络是否正常
2. 服务器地址是否正确: `https://dav.jianguoyun.com/dav/`

### 问题3: 文件同步不完整

原因: 目录超过750个文件/文件夹，需分页加载

解决: 检查WebDAV客户端是否支持分页

## 关闭或撤销

1. 登录坚果云网页版
2. 账户信息 → 安全选项 → 第三方应用管理
3. 删除对应的应用密码

---

## 已核对的原文依据

所有配置和说明已核对以下官方文档原文:

1. **坚果云帮助 - WebDAV开启方法** (https://help.jianguoyun.com/?p=2064) - 发布于2021-01-05
   - 服务器地址: `https://dav.jianguoyun.com/dav/`
   - 生成应用授权密码: 网页端【账户信息】→【安全选项】→【第三方应用管理】→【添加应用密码】
   - 移动端: iOS【设置】→【第三方应用管理】，Android【设置】→【第三方应用管理】
   - 上传限制: 默认500M
   - 访问频率: 免费版30分钟600次，付费版30分钟1500次
   - 目录数限制: 单次请求750个，需分页

2. **Python webdav3-client**: PyPI标准包 (https://pypi.org/project/webdav3-client/)

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**官方文档**: https://help.jianguoyun.com/?p=2064  
**离线测试**: ✅ Python代码语法正确  
**未实测**: 真实WebDAV连接
