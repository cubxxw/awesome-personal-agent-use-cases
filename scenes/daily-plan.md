# Start the workday · What actually needs me today?

[Home](../README.md) · [简体中文](../zh-CN/scenes/daily-plan.md)

A morning action list with time constraints, the next move and anything blocked.

## Sample result

- **10:00 · Review call** [C1].
- **By 15:00 · Confirm the page title** [T1].
- **Waiting · T2.** The supplier has not provided the files.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Build a workday action list for 2026-11-20 in Asia/Singapore. Give at most three items. Keep hard times and deadlines, and put externally blocked items in Waiting. Explain any missing source. Use only these records.
C1 | calendar | 2026-11-20 10:00 | website review call
T1 | due 2026-11-20 15:00 | confirm page title
T2 | supplier is responsible for sending files | no delivery yet
N1 | no date | reorganize bookmarks sometime
```

## With a connected tool

Connect one calendar and one task list you can verify. Try a manual brief with the same sources before setting delivery. If either source fails to load, mark it in the next brief.

## How to check it

C1 and T1 retain their times. T2 is waiting on someone else. N1 stays out. A day with no commitments and a missing calendar should look different.

## Decision boundary

The brief is a derived view. Changes to the calendar or task owner go through the underlying record.

## How the cases fit together

Morning briefings prioritize what the person can act on. A refreshing dashboard can hold the wider context. Give the daily output a clear cutoff and keep the source visible.

- Run it before opening email or as a short end-of-day review.
- Use the same outline for a weekly plan with a different window, then see how many items actually need attention.

## Sources

- **Community recipe.** The recipe combines scheduled delivery and inputs such as tasks and calendar context. [Custom morning brief](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/custom-morning-brief.md)
- **Collection summary.** The reported brief prioritizes deadlines, people awaiting replies and one focus for the day. [Muse #331 - A one-page morning action list](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1886-L1891) · [Original post](https://www.facebook.com/groups/1707928907613821/permalink/1708459510894094/)
- **Collection summary.** The collection describes a routine with morning priorities and email drafts that still require review. [Muse #355 - Morning briefing and reply drafts](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1935-L1940) · [Original post](https://www.reddit.com/r/MetaAI/comments/1xryn81/ive_been_using_muse_as_a_personal_assistant_for_a/)
- **Community recipe.** The recipe refreshes several sources into one dashboard and attaches a separate alert condition. [Dynamic dashboard](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/dynamic-dashboard.md)

## Building blocks

[Scheduled delivery](../usecases/scheduled-task.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Platform routes](../BUILDER.md)
