# Design / 设计

[English index](README.md) · [中文目录](README.zh-CN.md) · [案例来源与筛选](zh-CN/EVIDENCE.md)

## English

The index has two levels: a domain someone already recognizes, then a concrete situation. The scenario page shows the result, a fictional first run, the connected setup, and how to verify it. Scheduling, stored records and reusable instructions are available from the builder guide and from the relevant scenes.

Give each source a stable ID. Combine cases when the reader needs roughly the same input, result and decision. Keep a separate scene when a different result or decision changes what the reader needs to check. The evidence index distinguishes author accounts, published outputs, instructions and collection summaries.

The first-run ranking adds up three editorial judgments. Reuse and first run each take one or two points. Source strength gets two points when at least one author account or published result was inspected, and one when the support is a recipe or collection summary. Treat the score as an ordering aid.

## 人先找到自己的事

读者先选熟悉的领域，再认出正在碰到的事。比如「下次扣款前叫我」。每个场景先给一份具体结果，再给一段能直接试的材料。需要长期运行时，再决定何时触发、把记录放哪。权限随动作单独核对。

OpenClaw 用例库的单页结构好用。读者能直接发一条链接，也能在同一页看依赖和用法。这里保留它的阅读路径，再把同一个需求下的不同平台与来源放到一起。 [Awesome OpenClaw Use Cases](https://github.com/hesamsheikh/awesome-openclaw-usecases)

## 怎么聚在一起

| 读到的案例 | 聚合后的判断 |
| --- | --- |
| Muse 合集第 17 和 213 条都讲同一次收据审计 | 依作者、事件和原帖去重。再用跨渠道扣费与取消确认案例检查台账该留哪些字段。 [账单与订阅](zh-CN/scenes/renewal-ledger.md) |
| Reddit、YouTube、多来源技术简报 | 保留来源范围、窗口、去重和投递，合成一份专题更新。读不到来源时，在输出里说明。 [资讯与阅读](zh-CN/scenes/reading-digest.md) |
| 票价和直飞提醒 | 共用监控规则。对齐完整价格和条件，有命中就报告。库存与付款由另外一步核对。 [购物与比价](zh-CN/scenes/price-watch.md) |
| 联系人卡、会前准备、会后跟进 | 联系人卡留长期事实。会前卡问这次要决定什么。会后清单保留已经确认的分工与期限。三个结果各有验收点。 [联系人](zh-CN/scenes/personal-crm.md) · [会前](zh-CN/scenes/meeting-prep.md) · [会后](zh-CN/scenes/meeting-followups.md) |

每条来源只存一次，可以支撑多页。依帖子、作者或同一份产物判断是否重复。给原帖添加摘要或重发时，视为同一条材料。单一账号、行业或地区才成立的条件，放到相关场景的搭法里。

## 首页排序

同一组场景按三项相加排序，各最多两分。并列沿用编辑顺序。首屏单独用账单做一个可试的起点。

- **复用**。同一输入和交付结构能换到两种具体材料或用途，记 2。已有一个明确用途，记 1。
- **上手**。用几条现成材料就能直接核对一次输出，记 2。真实反馈还要多一步，比如等新的报价、验证原文章节或检查目的地，记 1。
- **来源**。有看过的作者自述或公开产物，记 2。依据是搭建说明或合集摘要，记 1。分数用于目录编排，证据类型仍显示在案例页上。

## 维护

在 `data/catalog.json` 里维护场景、来源与聚合判断。用 `python3 scripts/catalog.py` 更新双语目录、场景页和来源索引。`python3 scripts/catalog.py --check` 检查生成结果和仓库里的页面链接。搭建步骤在 [Builder](zh-CN/BUILDER.md) 和 `usecases/` 中维护。
