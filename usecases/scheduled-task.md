# Scheduled task

[Home](../README.md) · [简体中文](../zh-CN/usecases/scheduled-task.md)

Pick a time and get a short list of what needs your attention. The same setup can produce a morning brief, a Friday renewal check, or a Sunday review of your reading notes.

## Sample result

> Today, 20 November · Asia/Singapore
>
> - 10:00 · Website review call [C1].
> - By 15:00 · Confirm the page title for the editor [T1].

## Try it once

Paste the block below into your agent. The data is fictional and sufficient for the first run.

```text
Generate a short action list for 2026-11-20 in Asia/Singapore. Use only the records below.
Give me today's dated events and deadlines, in time order. Include the source ID on each line.
Skip background notes. If the records are available and nothing is due, say "Nothing due today."
If a source could not be read, name it instead of treating it as empty. Deliver the result in this chat.

C1 | Calendar | 2026-11-20 10:00 | Website review call
T1 | Task list | 2026-11-20 15:00 | Confirm the page title for the editor
N1 | Note | No date | Consider reorganizing my bookmarks
```

## Make it recurring

1. Replace the sample with one source you can read, such as your calendar or a dated list. Keep the scope small enough to check by hand.
2. Supply a schedule, a time zone, and the private destination. Try one scheduled delivery a few minutes ahead and inspect what actually arrived.
3. Give a quiet result its own rule. A daily brief may say nothing is due. A watch for changes can stay quiet. Confirm you can pause the schedule and see when it last ran.

[OpenClaw Cron](https://docs.openclaw.ai/automation/cron-jobs) and [ChatGPT scheduled tasks](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt) document scheduling. Check which data your scheduled run can read. For a renewal check, start from [a confirmed date list](renewal-ledger.md).

**Check it** · C1 and T1 appear, N1 stays out. Retry once with tomorrow's items only, then with a missing source. Those runs should give different feedback.

**Reference** · [Custom Morning Brief](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/custom-morning-brief.md) is an OpenClaw community setup. The dates above are sample data.
