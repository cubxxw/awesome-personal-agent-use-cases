# RSS 订阅与解析

读取RSS/Atom订阅源，获取最新内容更新。

## 能做什么

- 订阅博客、新闻站点的RSS源
- 解析feed内容(标题、摘要、链接、发布时间)
- 过滤和聚合多个源

## 前置条件

1. **RSS源地址**: 找到你要订阅的网站RSS链接
2. **Python环境** (如使用Python解析)

## 原生RSS订阅 (推荐)

### Python feedparser示例

需要安装 `feedparser`:

```bash
pip install feedparser
```

**代码**:

```python
import feedparser

# 解析RSS源
feed = feedparser.parse('https://example.com/rss.xml')  # 替换为实际RSS地址

# 获取feed信息
print(f'标题: {feed.feed.title}')
print(f'描述: {feed.feed.description}')
print(f'链接: {feed.feed.link}')

# 遍历条目
for entry in feed.entries[:5]:  # 显示前5条
    print(f'\n文章标题: {entry.title}')
    print(f'链接: {entry.link}')
    print(f'发布时间: {entry.get("published", "未知")}')
    print(f'摘要: {entry.get("summary", "无")[:100]}...')
```

### 测试

```bash
$ pip install feedparser
$ python3 -c "
import feedparser
print('feedparser版本:', feedparser.__version__)

# 测试解析(不访问网络)
sample = '''<?xml version=\"1.0\"?>
<rss version=\"2.0\">
<channel>
  <title>测试Feed</title>
  <item><title>条目1</title></item>
</channel>
</rss>'''

result = feedparser.parse(sample)
print('解析结果:', result.feed.title)
print('✅ feedparser可用')
"
```

预期输出:
```
feedparser版本: 6.x.x
解析结果: 测试Feed
✅ feedparser可用
```

## RSSHub (第三方服务，慎用)

### 什么是RSSHub

RSSHub是第三方服务，为不提供RSS的网站生成RSS源。

官网: https://docs.rsshub.app/zh/

### 重要限制

**来源**: [RSSHub FAQ](https://docs.rsshub.app/zh/guide/faqs)

1. **服务稳定性**: 第三方服务，可能随时失效
2. **访问限制**: 
   - 公共实例有访问频率限制
   - 可能被目标网站封禁
3. **数据准确性**: 依赖网页解析，网页变化后失效
4. **法律风险**: 某些源可能违反目标网站ToS
5. **隐私风险**: 请求通过第三方服务器

### 使用建议

⚠️ **不推荐依赖RSSHub用于生产**

如必须使用:
- 优先自建实例 (而非公共实例)
- 控制访问频率
- 定期检查源是否仍可用
- 准备替代方案

## 常见RSS源获取方式

1. **博客/新闻站**: 查找网站footer的RSS图标或`/rss.xml`、`/feed`路径
2. **YouTube频道**: `https://www.youtube.com/feeds/videos.xml?channel_id=频道ID`
3. **GitHub Releases**: `https://github.com/user/repo/releases.atom`

## 常见问题

### 问题1: RSS源解析失败

原因:
- RSS地址错误
- 源已失效
- 网络问题
- feed格式不规范

解决: 检查RSS地址是否可在浏览器打开并显示XML

### 问题2: 中文乱码

原因: 编码问题

解决: feedparser通常自动处理编码，如遇乱码检查源的charset声明

### 问题3: RSSHub路由失效

原因: 目标网站页面结构变化

解决: 
- 查看RSSHub issues是否有报告
- 等待更新或切换其他源

## 关闭或撤销

无需撤销，停止访问RSS地址即可。

---

## 已核对的原文依据

所有配置和说明已核对以下官方文档原文:

1. **Python feedparser**: PyPI标准包 (https://pypi.org/project/feedparser/)
   - 用法: `import feedparser; feed = feedparser.parse(url)`
   - 属性: `feed.feed.title`, `feed.entries`, `entry.title`, `entry.link`, `entry.published`

2. **RSSHub文档** (https://docs.rsshub.app/zh/) - 访问日期2026-11-22
   - 项目说明: "🍰 万物皆可 RSS"
   - 路由规则: 各路由页面

3. **RSSHub FAQ** (https://docs.rsshub.app/zh/guide/faqs) - 访问日期2026-11-22
   - 公共实例限制: "公共实例有访问频率限制"
   - 稳定性: "RSSHub 路由依赖于目标网站的页面结构，如果目标网站改版，路由可能失效"
   - 建议: "建议自建实例"

---

**核对日期**: 2026-11-22 (Asia/Singapore)  
**推荐方式**: 原生RSS (feedparser)  
**不推荐**: 依赖RSSHub公共实例用于生产  
**离线测试**: ✅ feedparser安装和解析正常  
**未实测**: 真实RSS源订阅
