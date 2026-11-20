# After a meeting · Who agreed to do what?

[Home](../README.md) · [简体中文](../zh-CN/scenes/meeting-followups.md)

A reviewable list of decisions, confirmed work and questions still missing an owner.

## Sample result

- **Decision D1.** Keep the originals in the handoff folder.
- **Action D2 · Ari · by 24 November.** Write the checklist draft.
- **Pending D3.** Access needs checking. Owner and date are open.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Make a follow-up draft with Decisions, Agreed actions and Open questions. Cite each input ID. Keep the exact owner and date for agreements. For unassigned work say they are open. Do not create tasks or send it yet.
D1 | Team agreed to keep the original files in the handoff folder.
D2 | Ari: I will draft the checklist by 2026-11-24.
D3 | Someone should check the shared folder access.
```

## With a connected tool

Use an approved transcript or notes and give the meeting a stable ID. Review ownership and due dates before creating tasks. If the notes change, compare the draft with the previous version and update the existing task only when the change is confirmed.

## How to check it

D2 alone has both an owner and a deadline. D3 stays open. Running the same notes twice should not create duplicate follow-ups.

## Decision boundary

Drafting the list, sending it and creating destination tasks are separate states. Track a write as complete after its receipt is visible.

## How the cases fit together

The meeting recipe shows how to extract a proposed action. The project-state recipe explains where a confirmed action or blocker can live across later meetings.

- Use the same draft format for a call transcript, a chat decision or handwritten meeting notes.
- Keep action IDs when pushing an approved list to a board, so the meeting can be rerun.

## Sources

- **Community recipe.** The recipe uses a transcript to identify decisions, owners and dates before handing work into a tracker. [Meeting notes and action items](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/meeting-notes-action-items.md)
- **Community recipe.** The recipe records the state, reasoning, blockers and next actions with history. [Event-driven project state](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/project-state-management.md)

## Building blocks

[Repeatable workflow](../usecases/repeatable-workflow.md) · [Capture inbox](../usecases/capture-inbox.md) · [Platform routes](../BUILDER.md)
