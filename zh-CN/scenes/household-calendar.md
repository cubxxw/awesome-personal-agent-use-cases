# 家庭日程板 · 这周谁要去哪

[首页](../../README.zh-CN.md) · [English](../../scenes/household-calendar.md)

**一个 Muse 替全家维护的日程板：把学校通知、群消息和共享日历合成一张周视图，管每个人的安排、改期、冲突和谁负责接送。有变化先报你确认，再写进日历。**

## 你能得到什么

- **一张全家周视图**——每个人这周的安排在一页上：时间、地点、谁负责接送，一眼看完。
- **改期和冲突先被挑出来**——组织方改了时间，旧安排标失效、新安排顶上；同一时间撞上的两件事、还没人认领的接送，单独列给你。
- **每天一份通知摘要**——学校群、收件箱里的新通知先收成几条，哪些要办、哪些只是告知，分开放。

## 把这段交给 Muse

整段复制给你的 Muse，它照着把日程板建出来，然后陪你跑起来。

```text
帮我建一个家庭日程板，名字叫「家庭日程」。

数据从这里来：我授权你读的共享日历，和我指定的收件箱/群消息。通知里出现新安排或改期，先提议给我看，不要直接改日历。

规则：
1. 一张周视图：按人列这周的安排——日期时间、事项、地点、谁负责接送。每项标来源（哪条通知、哪个日历）。
2. 改期以组织方的最新确认为准：新安排生效，旧记录标「已失效」，不删，方便回查。
3. 冲突单独列：同一个人同一时间有两件事、接送时间撞上别的安排、接送还没人认领——都进「待协调」，不要替任何人承诺。
4. 「收到通知」和「日历里已经确认」是两个状态，分开记。写进共享日历、转发给家人之前，先给我看，我确认了才动。
5. 每天把新通知收成一份小摘要：有变化的在前，只是告知的在后。

现在就开始：先把日程板建起来，然后问我先接哪个日历、哪个收件箱。
```

## 它怎么运转

- **进料靠连接，不靠你转发**——日历和收件箱接上后，新通知自己进来，你只处理被挑出来的变化和冲突。
- **周视图是全家人的唯一版本**——改期、冲突、接送都回到这一页对齐，不再各翻各的聊天记录。
- **确认权在人**——Muse 负责发现和提议，写日历、认领接送、对外转发，都由家人拍板。

## 来源

- **社区做法。** 汇总多个日历，从家庭消息中提取要处理的事项。[家庭日历汇总](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/family-calendar-household-assistant.md)
- **合集摘要。** 把学校群消息和邮件收成家庭摘要。[Muse 133 - 把学校群消息变成摘要](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1379-L1384) · [原始发布入口](https://x.com/fnthawar/status/2101684383396589932)
- **合集摘要。** 把学校活动提成日历日期，对外发信另行确认。[Muse 290 - 学校通知提取成日历日期](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1809-L1814) · [原始发布入口](https://www.facebook.com/kdgunn/posts/pfbid02Vn3FpWEDASZZGzbpuBuKoG9zHCe4p6tBwTih44YPmaSMk7Gr5oJMDuHUztnvQxNEl)
- **作者自述。** 家庭共用对话和日常摘要的长期记录。[家庭助理 Sebastian 的记录](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)

## 搭建方法

[定时任务](../usecases/scheduled-task.md) · [统一收件箱](../usecases/capture-inbox.md) · [平台怎么选](../BUILDER.md)
