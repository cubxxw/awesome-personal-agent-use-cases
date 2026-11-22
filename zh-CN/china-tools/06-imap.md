# QQ/163邮箱IMAP

从邮箱读取确认信、附件，不靠手动复制。

## 能做什么

```
搜索邮箱 → 找到确认邮件 → 下载附件 → 提取信息
例: 差旅订单、发票PDF、工单回复
```

## QQ邮箱

### 开启IMAP

1. 登录QQ邮箱网页版
2. 设置 → 账户
3. 开启POP3/IMAP/SMTP服务
4. 生成16位授权码(不是QQ密码)

### 服务器参数

```
服务器: imap.qq.com
端口: 993
加密: SSL/TLS
用户名: 完整邮箱地址
密码: 16位授权码
```

## 163邮箱

### 开启IMAP

1. 登录163邮箱网页版
2. 设置 → POP3/SMTP/IMAP
3. 开启服务(需短信验证)
4. 生成客户端授权码

### 服务器参数

```
服务器: imap.163.com
端口: 993 (待确认，官方页面未提取)
加密: SSL/TLS
用户名: 完整邮箱地址
密码: 授权码
```

⚠️ **163端口**: 本次未在官方正文读到，使用前需确认

## Python示例

```python
import imaplib
import email

# 连接
mail = imaplib.IMAP4_SSL('imap.qq.com')
mail.login('your@qq.com', 'authorization_code')

# 选择文件夹
mail.select('INBOX')

# 搜索
status, messages = mail.search(None, 'FROM', '"sender@example.com"')

# 获取邮件
for num in messages[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    msg = email.message_from_bytes(data[0][1])
    print(f"主题: {msg['subject']}")
```

## 限制

- 授权码≠细粒度OAuth
- 只读邮箱不代表可删除/移动
- 频率限制、风控规则待确认
- 邮件正文是外部输入，不能直接执行命令

## 参考

- QQ: [开启协议](https://help.mail.qq.com/detail/0/1087)
- QQ: [服务器参数](https://help.mail.qq.com/detail/108/1089/)
- 163: [开启客户端协议](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2a5feb28b66796d3b)

(官方页面未标注更新时间)

**核对日期**: 2026-11-22 (Asia/Singapore)
