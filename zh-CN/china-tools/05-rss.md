# RSS订阅

优先原生RSS，RSSHub作为补充(有限制)。

## 原生RSS

网站自带的RSS feed，无中间服务。

**示例**:
```
GitHub Releases: https://github.com/{user}/{repo}/releases.atom
Hacker News: https://news.ycombinator.com/rss
```

**优点**: 直接、稳定、无限流

**MCP包装**: 用标准RSS解析库定时读取

## RSSHub (第三方)

把无RSS的网站转成RSS，**不是原平台官方API**。

### 公共实例

- rsshub.app (美国)
- 其他实例见 https://docs.rsshub.app/zh/guide/instances

**限制**:
- 有缓存延迟
- 微博/知乎等反爬严格路由不保证可用
- 不能绕过登录/验证码
- 公共实例可能暴露订阅内容

### 自建部署

需要: Node.js / Docker

```bash
# Docker方式
docker run -d -p 1200:1200 diygod/rsshub

# 访问: http://localhost:1200
```

**好处**: 自己控制、不限流

**成本**: 服务器、流量、维护

## 测试

```python
# 安装: pip install feedparser
import feedparser

# 测试原生RSS
feed = feedparser.parse('https://news.ycombinator.com/rss')
print(f"标题: {feed.feed.title}")
print(f"条目数: {len(feed.entries)}")
```

## 不能做什么

- ❌ 不是任意公众号全文获取
- ❌ 不能绕过平台登录限制
- ❌ 路由失败时不编造内容

## 参考

- [RSSHub文档](https://docs.rsshub.app/zh/)
- [FAQ](https://docs.rsshub.app/zh/guide/faqs)

**核对日期**: 2026-11-22 (Asia/Singapore)
