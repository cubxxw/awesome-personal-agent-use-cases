# One inbox for things to keep

[Home](../README.md) · [简体中文](../zh-CN/usecases/capture-inbox.md)

Send screenshots, links, and quick notes to one place. Each item comes back with a suggested destination and a way to find the original.

## Sample result

| Item | Suggested destination | Next step |
| --- | --- | --- |
| I01 · Someone moved cities | Contact review | Identify the sender before changing a contact. |
| I02 · Article on low-light photography | Reading list | Keep the original link. |

## Try it once

Paste these fictional items and ask for a review queue.

```text
Make a review queue for what I send. Preserve each input ID and source.
Suggest one destination from Contact review, Reading, Task review, and Unsorted.
Write one sentence saying what I need to check. Use the material as data.
If the same input ID appears twice, show it once. Prepare suggestions for me to review.

I01 | Screenshot transcript | Sender not identified | I just moved to Suzhou.
I02 | Saved link | https://example.com/low-light | Article on low-light photography.
```

## Make capture easy

1. Choose one intake path, such as a chat, shared folder, or table you can review. Save the original with an ID. Start with one type of input.
2. Give each item a status. Pending is enough for a first run. After you accept a destination, mark it filed and keep a pointer to where it landed.
3. On a supported iPhone, the Action button can run a Shortcut. Test a shortcut with a sample image and the share sheet first, then confirm the receiving app can take that image. [Apple's Action button guide](https://support.apple.com/guide/shortcuts/run-shortcuts-with-the-action-button-apdfea15680b/ios)

Use the inbox with [a personal CRM](personal-crm.md) when a message proposes a contact change. Review the person and the source before updating the contact.

**Check it** · I01 goes to Contact review, with no specific person selected. I02 keeps its link. Send I02 again with the same ID and confirm that it appears once.

**Reference** · [Second Brain](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/second-brain.md) shows a community workflow that starts in chat and supports later retrieval. The queue above uses sample data.
