# How this library is designed / 架构与收录思路

## English

The homepage has two levels. Choose a kind of help, then open one self-contained workflow. Each page shows a sample result and gives you fictional input to try before connecting an account.

Use a schedule for a recurring delivery, a saved record for something that must stay current, and a reusable instruction for work you hand off repeatedly. Combine them when useful. A renewal ledger holds confirmed dates. A scheduled task reads those dates and tells you what needs a decision.

Muse Space is one way to build the long-lived dashboard. The same review steps and fields can live in a sheet or local files. Keep setup notes and actual run evidence on the corresponding use-case page.

## 玩法是一个人愿意反复交给 Agent 的事

最小的一页要能回答两件事。读者能不能拿自己的材料换掉示例？跑完一遍后，能不能检查 Agent 交出了什么？把 Reddit 日报换成每周账单摘要，还是可以让定时任务读一份材料，把简短的结果交给自己。这个共性才值得占一个目录位置。

## 从 OpenClaw 用例库学到的

[Awesome OpenClaw Use Cases](https://github.com/hesamsheikh/awesome-openclaw-usecases) 在首页用一句话介绍每个用例，独立页面再放依赖、提示词和配置。[Reddit 日报](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/daily-reddit-digest.md) 和 [晨间简报](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/custom-morning-brief.md) 给了不同结果，背后都需要约定什么时候从哪里读、把结果交到哪里。[贡献规则](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/CONTRIBUTING.md) 也要求把用例写到别人能复现，并要求提交者验证实际流程。

这里沿用「短目录 → 单页玩法」。同一套流程的好例子收在一页。每页先展示结果和自带材料的一次试跑，再说明选什么产品、要哪些权限，以及怎么确认第二次还能工作。

## 首页只走两层

| 读者想交给 Agent 的事 | 进哪一页 |
| --- | --- |
| 主动跟进。我希望到点看到结果，或者有事变化再打扰我。 | 定时任务、变化监控 |
| 长期维护。我希望一处记录能随着新信息继续更新。 | 个人 CRM、到期台账 |
| 按需交办。我希望一丢材料就知道它去哪，或把熟悉的活交给它跑。 | 统一收件箱、复用流程 |

同一条消息可以先进入收件箱，经确认写入联系人卡，会前再由定时任务读这张卡。三个环节都能单独试。到期台账也一样，日期存在台账里，定时任务只在需要的时候读出来。

## 通用玩法与具体产品

| 需要的能力 | 先跑哪一步 | 可查的产品入口 |
| --- | --- | --- |
| 定时交付 | 用同样的材料手动跑一次，确认结果有用。 | [OpenClaw Cron](https://docs.openclaw.ai/automation/cron-jobs)、[ChatGPT 定时任务](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt) |
| 长期记录 | 选一张你能核对、修改和备份的表。 | [Muse Space](https://apps.apple.com/us/app/muse-from-meta/id6760173601)、[ChatGPT Space](https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt)、本地表格 |
| 重复流程 | 先把输入、交付格式和确认条件写成一段能复用的说明。 | 普通对话、[Agent Skills 规范](https://agentskills.io/specification) |

Muse 适合用来展示长期面板怎么长出来。目录用通用的玩法名，可以把同一套字段和确认规则用于表格、文件或其他 Agent。产品文档说明的是能力入口。能不能读取你那份材料、写回哪张表或定时送达，要在具体账号和版本上确认。

## Files

```text
README.md                 English index
README.zh-CN.md           中文索引
usecases/                 One page per workflow
zh-CN/usecases/           中文玩法页，与英文同名
CONTRIBUTING.md           Submission and evidence rules
```

Keep one page per reusable workflow. Add a different product or source to the same page when the reader still gets the same result. A product route can document requirements and link to official help, while an end-to-end reproduction needs a run and a visible result.
