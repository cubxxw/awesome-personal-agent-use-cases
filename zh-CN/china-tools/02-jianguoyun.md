# 坚果云WebDAV

文件跨设备存储，原件保留，手机保存电脑能打开。

## 能做什么

```
手机保存文件 → WebDAV上传 → 电脑访问同一文件
支持: PDF、图片、文档，原样存储
```

## 前置条件

1. **坚果云账号**: https://www.jianguoyun.com 注册

2. **应用密码**:
   - 登录网页版 → 账户信息 → 安全选项
   - 添加应用密码
   - 记录密码(只显示一次)

3. **WebDAV地址**: `https://dav.jianguoyun.com/dav/`

## Python示例

```python
# 安装: pip install webdavclient3
from webdav3.client import Client

client = Client({
    'webdav_hostname': 'https://dav.jianguoyun.com/dav/',
    'webdav_login': 'your@email.com',
    'webdav_password': 'app_password'
})

# 上传
client.upload_sync(
    remote_path='/test.txt',
    local_path='./test.txt'
)

# 列表
files = client.list('/')
```

## 测试

```bash
# 创建测试文件
echo "test" > test.txt

# 用上面Python代码上传
# 检查: 登录坚果云网页版，查看文件是否出现
```

## 限制

- 上传大小、频率有限制(2021年文档，当前值待确认)
- 需要网络连接
- 不支持断点续传
- 商业使用条款待核对

## 参考

- [WebDAV开启](https://help.jianguoyun.com/?p=2064) - 发表2021-01-05

**核对日期**: 2026-11-22 (Asia/Singapore)
