# A workflow you can run again

[Home](../README.md) · [简体中文](../zh-CN/usecases/repeatable-workflow.md)

Turn a recurring job into setup you can reuse. Start with one input, a fixed output, and a review step. Meeting notes to follow-ups are one example.

## Sample result

**Decision** · Keep the original files in the handover package [M1].

| Next step | Owner | Due | Evidence |
| --- | --- | --- | --- |
| Draft the handover checklist | Ari | 24 November | M2 |
| Verify access to the shared folder | To confirm | To confirm | M3 |

## Try it once

Paste this block. The notes are fictional.

```text
Turn these notes into a handover draft. Give me one Decisions section and one Next steps table.
Each action needs a description, an owner, a due date, and its source ID.
Use To confirm when the notes do not name an owner or date.
Return the draft only. I will confirm assignments and send anything that needs to go out.

M1 | The group decides to keep the original files in the handover package.
M2 | Ari: I'll draft the handover checklist by 2026-11-24.
M3 | The shared folder access still needs to be checked. Nobody has claimed it.
```

## Use it again

1. Save the instructions as a template. Give each new input an ID, such as the meeting date and project. Keep the raw notes reachable.
2. Run it on the next input. If you use files, save the draft somewhere you can review and use the same draft location when you rerun the same input.
3. Check the output before copying anything to a task board or sending it. When a tool sends or writes after your approval, inspect the receipt or the updated destination.

This also works for weekly reports, bug reports, and document checks with a stable review checklist. Once the template has held up on several real inputs, you can package it for a compatible agent. [Agent Skills specification](https://agentskills.io/specification)

**Check it** · Ari's item has a date. M3 stays unassigned. Repeat the same input and compare your draft. Keep the two-step preview and approval if you automate any later action.
