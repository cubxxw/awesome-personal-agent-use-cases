# Family and routines · Who needs to be where this week?

[Home](../README.md) · [简体中文](../zh-CN/scenes/household-calendar.md)

A shared week view with confirmed events, clashes and pickups still to arrange.

## Sample result

- **24 November at 15:00 · Music practice** [S2, replacing S1].
- **Pick-up needs a decision.** The only assigned adult is already booked [C1].

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Make a household list for the week of 23 November. Show the latest confirmed schedule, conflicts, and unassigned pickups. Keep a source ID on each item. If an organizer explicitly changes a date, mark the old entry superseded. Produce a preview only.
S1 | music practice | 2026-11-23 15:00 | original notice
S2 | music practice moved to 2026-11-24 15:00 | confirmed by organizer
C1 | 2026-11-24 14:30-16:00 | assigned adult has a call
C2 | music practice | pick-up needed | no alternate owner
```

## With a connected tool

Connect a calendar or shared inbox you’re allowed to read. Extract dates from notices before proposing a shared-calendar change. An adult reviews changed times, conflicts and who can do the pickup.

## How to check it

S2 supersedes S1. The 24 November conflict appears once. C2 remains unassigned and should not become a presumed commitment.

## Decision boundary

Ask before updating a shared calendar or forwarding private material. Treat a notice and a confirmed calendar event as separate records.

## How the cases fit together

A school-message digest and a shared calendar both reduce repeated checking. The digest collects what changed. The week view reconciles that against existing commitments.

- Summarize the notices once a day so someone can pick out the items that need action.
- Use a weekly view with time, destination and pickup owner to catch overlaps.

## Sources

- **Community recipe.** The recipe brings calendar events and actionable household messages into one view. [Family calendar aggregation](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/family-calendar-household-assistant.md)
- **Collection summary.** The report bundles school messages and email for the family to review. [Muse #133 - Turn school messages into a digest](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1379-L1384) · [Original post](https://x.com/fnthawar/status/2101684383396589932)
- **Collection summary.** The account combines school date extraction with approval before sending a reply. [Muse #290 - Put school dates on a calendar](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1809-L1814) · [Original post](https://www.facebook.com/kdgunn/posts/pfbid02Vn3FpWEDASZZGzbpuBuKoG9zHCe4p6tBwTih44YPmaSMk7Gr5oJMDuHUztnvQxNEl)
- **Author account.** The author describes using a shared chat setup for household routines and a digest with source checks. [The Sebastian family assistant](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)

## Building blocks

[Scheduled delivery](../usecases/scheduled-task.md) · [Capture inbox](../usecases/capture-inbox.md) · [Platform routes](../BUILDER.md)
