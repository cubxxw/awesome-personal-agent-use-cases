# 怎么搭一个场景

[首页](../README.zh-CN.md) · [English](../BUILDER.md)

先看场景要交付什么，再挑能完成这一小步的做法。比如联系人卡先能改一条记录、关掉重开还能找到，再考虑接更多消息。

| 需要哪一步 | 搭建方法 | 先验收什么 |
| --- | --- | --- |
| 到点收到结果 | [定时任务](usecases/scheduled-task.md) | 手动核对一次结果，再试一次送达。 |
| 有变化才通知 | [变化监控](usecases/change-watch.md) | 命中、没变化和读取失败各试一次。 |
| 长期更新同一张卡 | [联系人卡](usecases/personal-crm.md) | 确认一处修改，重新打开时还能查到原消息。 |
| 知道下次什么时候要做决定 | [日期台账](usecases/renewal-ledger.md) | 一条日期能在原通知中核对。 |
| 把材料先放进一处 | [统一收件箱](usecases/capture-inbox.md) | 收一份材料，下次能找回原件。 |
| 同类任务反复做 | [复用流程](usecases/repeatable-workflow.md) | 对照完成标准，用同一输入复跑一次。 |

## 平台入口

下面是各产品公开说明里的出发点。换成自己的账户和资料，先核对权限、产物和接收位置。

| 工具 | 从哪种玩法开始 | 做一次检查 |
| --- | --- | --- |
| [Muse Spaces](https://apps.apple.com/us/app/muse-from-meta/id6760173601) | 经常回看的联系人或项目面板 | 手工确认一条改动，重新打开看原记录有没有更新。 |
| [OpenClaw 定时](https://docs.openclaw.ai/automation/cron-jobs) | 定期读取获准的输入并投递 | 先运行一次，核对实际读了什么、送到哪。 |
| [ChatGPT Space 页面](https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt) | 把材料、表和交接记录放在一起 | 重新打开同一页，确认当前产品和账号用什么方式更新。 |
| [Manus Projects](https://manus.im/docs/features/projects) | 沿用同一组说明和文件反复做一类任务 | 新开一次任务，看能否读到打算使用的版本。 |
| [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) | 在指定文件夹里处理文档 | 先预览两份文件的批次，核对保存位置和原件。 |
| [Codex 项目说明](https://developers.openai.com/codex/guides/agents-md) | 在项目里交接上下文和检查结果 | 给一个新会话交接说明，检查它能否找到并核对最新产物。 |

## 把几步接起来

- [账单](scenes/renewal-ledger.md)先收通知，再确认台账日期，最后才设提醒。
- [联系人](scenes/personal-crm.md)先将截图放进收件箱，确认人物后改原卡。见面前，拿这张卡出一页[会前准备](scenes/meeting-prep.md)。
- [Agent 交接](scenes/agent-handoff.md)先把产物和上次核对结果存成一份能打开的文件。后续工具读写哪里，要单独验一次。

想用 iPhone 快速收图，可以先让操作按钮运行快捷指令。目标应用能否接收图片、是否返回能找到的记录，用一张样例图试清楚再接联系人流程。 [Apple 操作按钮指南](https://support.apple.com/guide/shortcuts/run-shortcuts-with-the-action-button-apdfea15680b/ios)
