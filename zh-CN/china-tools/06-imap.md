# QQ/163邮箱 IMAP 读取

通过IMAP协议读取邮件，用于邮件自动化处理。

## 能做什么

- 读取未读邮件
- 搜索邮件内容
- 标记邮件状态
- 获取附件

## 前置条件

1. **QQ邮箱或163邮箱账号**
2. **开启IMAP服务并获取授权码**

⚠️ **重要**: 第三方客户端登录时，密码栏填写授权码，不是邮箱网页登录密码

---

## QQ邮箱配置

### 第一步: 开启IMAP并获取授权码

**来源**: [QQ邮箱帮助 - 如何开启协议并获取授权码](https://help.mail.qq.com/detail/0/1087)

1. 登录 QQ邮箱网页版
2. 点击顶部"设置" → "账号与安全"
3. 找到"POP3/IMAP/SMTP/Exchange/CardDAV服务"区域
4. 点击IMAP旁边的"开启"开关
5. 按提示用手机发送短信验证
6. 验证通过后，页面弹出16位授权码
7. ⚠️ **立即复制并保存**，此授权码只显示一次

### 第二步: IMAP连接参数

**来源**: [QQ邮箱帮助](https://help.mail.qq.com/detail/108/1089/)

- **IMAP服务器**: `imap.qq.com`
- **端口**: 993 (SSL)
- **邮箱账号**: 你的完整QQ邮箱地址
- **密码**: 16位授权码 (不是QQ邮箱登录密码)

### Python示例 (QQ邮箱)

```python
import imaplib
import email
from email.header import decode_header

# 连接参数
IMAP_SERVER = 'imap.qq.com'
IMAP_PORT = 993
EMAIL = 'your_qq_number@qq.com'      # 替换为你的QQ邮箱
PASSWORD = 'your_16_digit_auth_code' # 替换为授权码

# 连接到QQ邮箱
mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(EMAIL, PASSWORD)

# 选择收件箱
mail.select('INBOX')

# 搜索未读邮件
status, messages = mail.search(None, 'UNSEEN')
email_ids = messages[0].split()

print(f'未读邮件数: {len(email_ids)}')

# 读取第一封未读邮件
if email_ids:
    status, msg_data = mail.fetch(email_ids[0], '(RFC822)')
    msg = email.message_from_bytes(msg_data[0][1])
    
    # 解码主题
    subject = decode_header(msg['Subject'])[0][0]
    if isinstance(subject, bytes):
        subject = subject.decode()
    
    print(f'主题: {subject}')
    print(f'发件人: {msg["From"]}')

# 关闭连接
mail.logout()
```

---

## 163邮箱配置

### 第一步: 开启IMAP并获取授权码

**来源**: [163邮箱帮助 - 如何开启客户端协议](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2a5feb28b66796d3b)

1. 登录 163邮箱网页版 (https://email.163.com/)
2. 点击上方"设置" → "POP/SMTP/IMAP选项"
3. 在客户端协议界面，选择开启IMAP
4. 点击"继续开启"，按提示扫码或手动发送短信验证
5. 验证成功后，页面展示客户端授权码 (16位字母数字组合)
6. ⚠️ **立即保存**，一个授权码只在开启时显示一次

### 第二步: IMAP连接参数

**来源**: [163邮箱帮助](https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2a5feb28b66796d3b)

官方文档提到"目前主流的常用新版本客户端...都已经支持网易邮箱一键登录...如果您需要设置正确的163邮箱服务器地址，信息如下"，但具体服务器地址未在所读页面完整列出。

⚠️ **待核实**: 163邮箱IMAP服务器地址和端口未在官方帮助页面明确给出

根据常见配置 (未经官方文档确认):
- **IMAP服务器**: `imap.163.com` (待官方确认)
- **端口**: 993 (SSL，待官方确认)
- **邮箱账号**: 你的完整163邮箱地址
- **密码**: 客户端授权码

---

## 测试

### 离线依赖测试

```bash
$ python3 -c "
import imaplib
import ssl
print('imaplib可用:', hasattr(imaplib, 'IMAP4_SSL'))
print('ssl可用:', hasattr(ssl, 'create_default_context'))
print('✅ IMAP依赖就绪')
"
```

预期输出:
```
imaplib可用: True
ssl可用: True
✅ IMAP依赖就绪
```

⚠️ **端到端测试**: 需要真实邮箱账号和授权码，本文档未进行实际IMAP连接测试

## 常见问题

### 问题1: 登录失败 (535错误)

原因:
- 使用了邮箱网页登录密码 (应使用16位授权码)
- IMAP服务未开启
- 授权码已过期或删除

解决: 检查是否使用授权码，重新生成授权码

### 问题2: 连接超时

检查:
1. 服务器地址和端口是否正确
2. 网络是否正常
3. 防火墙是否阻止

### 问题3: SSL错误

原因: SSL证书验证失败

解决: 确保Python ssl模块正常工作

## 安全建议

- 不要将授权码分享给他人
- 不要在公开代码中直接写入授权码
- 定期在邮箱安全设置中查看授权设备
- 如授权码泄露，立即在邮箱设置中停用

## 关闭或撤销

### QQ邮箱
1. 登录QQ邮箱网页版
2. 设置 → 账号与安全 → 设备管理 → 授权码管理
3. 停用或删除对应授权码

### 163邮箱
1. 登录163邮箱网页版
2. 设置 → POP/SMTP/IMAP → 管理授权码
3. 删除对应授权码

---

## 已核对的原文依据

所有配置和说明已核对以下官方文档原文:

1. **QQ邮箱帮助 - 如何开启协议并获取授权码** (https://help.mail.qq.com/detail/0/1087)
   - 开启流程: 设置 → 账号与安全 → POP3/IMAP/SMTP/Exchange/CardDAV服务 → 开启
   - 验证: 手机发送短信到指定号码
   - 授权码: 16位，只显示一次
   - 重要说明: "授权码 ≠ 邮箱密码"，"用户名填完整邮箱地址，密码栏填写16位授权码"

2. **QQ邮箱帮助 - 服务器参数** (https://help.mail.qq.com/detail/108/1089/)
   - IMAP服务器: imap.qq.com
   - 端口: 993 (SSL)

3. **163邮箱帮助 - 如何开启客户端协议** (https://help.mail.163.com/faqDetail.do?code=d7a5dc8471cd0c0e8b4b8f4f8e49998b374173cfe9171305fa1ce630d7f67ac2a5feb28b66796d3b)
   - 开启流程: 设置 → POP/SMTP/IMAP选项 → 开启IMAP
   - 验证: 扫码或手动发送短信
   - 授权码: 16位字母数字组合，只在开启时显示一次
   - ⚠️ 服务器地址未在所读页面明确给出

4. **Python imaplib**: Python标准库 (https://docs.python.org/3/library/imaplib.html)

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**QQ邮箱配置**: ✅ 完整 (官方文档确认)  
**163邮箱配置**: ⚠️ 服务器地址待官方确认  
**离线测试**: ✅ Python依赖就绪  
**未实测**: 真实IMAP连接
