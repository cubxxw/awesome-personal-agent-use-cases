# Project board · Which one is stuck and why?

[Home](../README.md) · [简体中文](../zh-CN/scenes/project-board.md)

A persistent view of project status, blocker, next step and the event that changed it.

## Sample result

- **P1 · Waiting on images** [E2]. Next, confirm when the supplier can send them.
- **P2 · Ready for review** [E3]. The draft is saved. It has not been published.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Update a preview of these project cards. Give each project its status, blocker, one next step and the evidence. Keep a locally ready item separate from a released item. Preserve the old state in history and ask about unclear ownership.
P1 | project Docs | status In progress
P2 | project Brief | status In progress
E2 | P1 | supplier images missing, no delivery date
E3 | P2 | draft available for review in shared folder, release not requested
```

## With a connected tool

Use one table, page or set of files as the main record. Give projects stable IDs. Confirm a proposed change before saving it. Share a derived view with only the fields other people need.

## How to check it

P1 changes to Waiting. P2 changes to Ready for review. Replay E2 and confirm the history contains one event. Reopening the board should show the reason without rereading the chat.

## Decision boundary

The board summarizes evidence. A status such as Shipped needs a release receipt or a confirmation from the owner.

## How the cases fit together

The state-management recipe emphasizes an event history, and dashboards emphasize a current view. Keep both close enough that you can see what changed without rereading every message.

- Track a few personal projects with a small next-step column.
- Use a Muse Space or a plain table and make a brief from the same state at the start of the week.

## Sources

- **Community recipe.** The recipe records the state, reasoning, blockers and next actions with history. [Event-driven project state](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/project-state-management.md)
- **Community recipe.** The recipe refreshes several sources into one dashboard and attaches a separate alert condition. [Dynamic dashboard](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/dynamic-dashboard.md)
- **Collection summary.** The collection describes separate spaces for daily learning, planning and meals. The learning topics varied by depth. [Muse #329 - Build small recurring-use Spaces](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1872-L1877) · [Original post](https://www.threads.com/@muse/post/DfkXlR9Gt7e)

## Building blocks

[Repeatable workflow](../usecases/repeatable-workflow.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Platform routes](../BUILDER.md)
