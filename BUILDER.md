# Build a scenario

[Home](README.md) · [简体中文](zh-CN/BUILDER.md)

Start with the result you want. Then pick the smallest set of capabilities that can produce and verify it.

| When you need to… | Building block | Check before adding more |
| --- | --- | --- |
| Get an answer at a set time | [Scheduled delivery](usecases/scheduled-task.md) | Run once and verify the destination and time zone. |
| Hear only about changes | [Change watch](usecases/change-watch.md) | Try a hit, a quiet run and a failed fetch. |
| Update the same contact | [Durable contact record](usecases/personal-crm.md) | Review one change, reopen in a new session and find its source. |
| See what is due next | [Date ledger](usecases/renewal-ledger.md) | Match one deadline to its original notice. |
| Send material to one place | [Capture inbox](usecases/capture-inbox.md) | Save an original and retrieve it later by ID. |
| Assign the same kind of work again | [Repeatable workflow](usecases/repeatable-workflow.md) | Check the expected result and replay the same input once. |

## Platform routes

Each route links to the relevant product documentation. Run the small check in your account before adding real data or a recurring action.

| Route | Fit | First check |
| --- | --- | --- |
| [Muse Spaces](https://apps.apple.com/us/app/muse-from-meta/id6760173601) | A custom contact or project panel you return to | Save one reviewed change to the original record and reopen it. |
| [OpenClaw automation](https://docs.openclaw.ai/automation/cron-jobs) | Scheduled work from approved inputs | Run one job and confirm what was read and where it went. |
| [ChatGPT Space pages](https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt) | Review material, tables and handoff notes together | Reopen the same page and confirm which action can update it. |
| [Manus Projects](https://manus.im/docs/features/projects) | Repeat jobs with shared project instructions and files | Start another task and verify it sees the intended version. |
| [Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) | Repeated work on files in a selected folder | Preview a two-file batch and check the saved result and originals. |
| [Codex project instructions](https://developers.openai.com/codex/guides/agents-md) | Transfer project context and instructions between coding sessions | Give a new session the handoff and see whether it can locate and verify the latest artifact. |

## Combine the pieces

- [Bills](scenes/renewal-ledger.md) · Capture notices, confirm dates in the ledger, then schedule delivery.
- [Personal CRM](scenes/personal-crm.md) · Drop a screenshot into the inbox, confirm the sender and update the existing card. Pull the card into a [meeting brief](scenes/meeting-prep.md) when needed.
- [Agent handoff](scenes/agent-handoff.md) · Save the artifact and the last checked result in a file the next session can open. Verify permissions separately.

For an iPhone intake, the [Action Button documentation](https://support.apple.com/guide/shortcuts/run-shortcuts-with-the-action-button-apdfea15680b/ios) describes launching a shortcut. Verify that your destination accepts the image and returns a traceable item before routing it to the contact workflow.
