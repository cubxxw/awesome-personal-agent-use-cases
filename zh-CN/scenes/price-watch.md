# 购物与比价 · 降到预算再叫我

[首页](../../README.zh-CN.md) · [English](../../scenes/price-watch.md)

收到一条带价格、检查时间和出处的提醒，方便打开原页面核对。

## 先看结果

- **Q2 命中**。L 区同排连座 4 张，含费 480 元。
- **Q3 待查**。看到标价，没看到手续费。

## 手头有材料就能试

复制下面整段。里面的材料都是虚构样例。

```text
先查这一批报价。我找 L 区 4 张连座，含全部费用不超过 500 元。每个结果带报价编号和最近检查时间。条件齐全才标命中，缺字段的列到待核对。先给清单，不预订、不下单。
Q1 | 10:00 | L 区 3 张连座 | 含费 CNY 420
Q2 | 10:05 | L 区 4 张连座 | 每张 CNY 110，全部费用另计 CNY 40
Q3 | 10:06 | L 区 4 张连座 | 标价 CNY 440，费用未知
```

## 已经接了工具

先确认票源能读到全部比价字段，约定最晚盯到哪天。有命中时打开票源复查。定时检查时，只为新的有效变化发一次提醒。

## 怎么验收

只有 Q2 达标。Q1 张数不合，Q3 留待查。访问失败时也要在结果里看得出来。

## 做到哪一步

提醒给你的是线索。付款前你需要看页面上的实际库存、价格和条款。

## 这些案例怎么合在一起

球票和航班共用一个盯价规则，先约定什么才算同条件。直飞案例里，通知到了却没排到座位，所以提醒和成交要分别记。

- 换成机票时先对航线和停靠条件，再按实际乘客数和行李算总价。
- 改成普通商品时，先匹配型号，再把运费一起算进预算。

## 来源

- **合集摘要**。盯价条件同时涉及张数、区域和总价。找到票源和成交各有自己的回执。 [Muse 162 - 盯同区四张球票的价格](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1057-L1062) · [原始发布入口](https://x.com/BradyHannaKC/status/2112961536168005898)
- **合集摘要**。摘要记录了提醒、去柜台排候补和没有拿到座位的过程。 [Muse 377 - 收到直飞提醒，候补没抢上](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L896-L901) · [原始发布入口](https://www.facebook.com/yourbossbaesteph/posts/pfbid037xRCh2jX5qXJjYEJ6Y3kGBYhqemmHzoUSWpozcxxGxSLotH8F1j84htxwkCkrYWRl)

## 搭建方法

[变化监控](../usecases/change-watch.md) · [定时任务](../usecases/scheduled-task.md) · [平台怎么选](../BUILDER.md)
