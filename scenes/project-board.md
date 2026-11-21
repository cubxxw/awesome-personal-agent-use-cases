# Project board · Which one is stuck, and where?

[Home](../README.md) · [简体中文](../zh-CN/scenes/project-board.md)

**A project board Muse maintains for you: one card per project covering its current state, what it is blocked on, and whose next action unblocks it. State changes only on checkable events — a finished draft is not a publication, and "live" requires a release receipt.**

## What you get

- **A board you can read at a glance** — every card states four things: status, blocker (stuck on what, waiting on whom), one concrete next step, and the source behind the status. Open it and you know which project to push today.
- **A status history** — every change leaves one line: the date and what caused it. Months later you can still tell the story of how a project got here.
- **Preview before saving** — updates arrive as a preview and are written only after you confirm; the same event delivered twice is still recorded once.

## Give this to Muse

Paste the whole block into your Muse. It builds the board, then runs it with you.

```text
Build me a project board, one card per project.

Each card records: project name and ID, current status, blocker (stuck on what, waiting on whom), next step (one action with a named owner), and the status source (which message, which receipt).

Rules:
1. Status changes only on checkable events: a receipt arrived, a person confirmed, a file appeared. Your guess or my second-hand report is not enough — mark it "to confirm".
2. "Draft ready", "submitted", "published" and "delivered" are different states, recorded separately. Before marking anything published or delivered, require a release receipt or the owner's confirmation.
3. Updates come as a preview first; save only after I confirm. The same event arriving twice is recorded once.
4. When the owner of a next step is unclear, write "owner to assign" — never assign someone on my behalf.

Start now: set up the board, then ask me which projects go on it first and which material each status should be checked against.
```

## How it runs

- **The board is the single source of project state** — the morning action list and weekly reviews read status from here instead of each keeping their own version.
- **Shared views carry only the needed fields** — when collaborators need a look, generate a view with just their fields; internal notes never leak into it.

## Sources

- **Community recipe.** Project state updated by sourced events, with blockers and next steps traceable. [Update project state from events](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/project-state-management.md)
- **Community recipe.** Several sources refreshed into one place, with threshold changes alerted separately. [Multi-source dashboard](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/dynamic-dashboard.md)
- **Collection summary.** Small long-lived panels in Spaces that stay reviewable. [Muse #329 - Small long-lived panels in Spaces](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1872-L1877) · [Original post](https://www.threads.com/@muse/post/DfkXlR9Gt7e)

## Building blocks

[Repeatable workflow](../usecases/repeatable-workflow.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
