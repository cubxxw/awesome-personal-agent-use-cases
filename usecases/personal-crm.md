# Personal CRM

[Home](../README.md) · [简体中文](../zh-CN/usecases/personal-crm.md)

Give the people you care about a contact card you can update and use before you meet. Start with one person and one message.

## Sample result

| Contact | Current | Proposed | Evidence |
| --- | --- | --- | --- |
| P01 · Lin Lan | Nanjing | Suzhou · needs review | M02 · 20 November |

Once approved, the same card shows Suzhou as the current city. The earlier value remains in its history. A future meeting brief can cite M02.

## Try it once

Paste this into your agent. Both records and the person are fictional.

```text
Review the new message against my contact card. Propose the fields that should change, with old value, new value, and source ID. Leave the original card as it is for now.
Use the confirmed person ID. Ask me to identify the person if it is unclear. If no field changes, say "Nothing to update." Keep guesses separate and leave unmentioned fields alone.

Contact P01 | Lin Lan | Current city: Nanjing
Message M02 | 2026-11-20 | Sender confirmed as P01 | I just moved from Nanjing to Suzhou.
```

If the proposal is right, save it in the same card with the source and date. Ask for a one-line briefing in a new chat using that saved card. That second run checks whether you can reuse the record later.

## Give the record a home

- **A sheet or plain files.** Keep a Contacts sheet with person ID, current facts, and a source ID. Put incoming messages and proposed changes in a separate review list. Review and copy accepted changes yourself on the first run.
- **Muse Space.** Ask Muse to build a contact dashboard with a contact list and a review queue. Use the sample to confirm each change goes onto the existing card after you approve it. [Muse product listing](https://apps.apple.com/us/app/muse-from-meta/id6760173601)
- **ChatGPT Space.** A page can hold a table and a short meeting brief. Test the write path and any reminders in your own setup. [Pages in Space](https://help.openai.com/en/articles/20001549-getting-started-with-space-in-chatgpt)

To try the Muse Space route, follow the sample with this request.

```text
Use the fictional records above to build a Contacts Space with a contact view and a review queue.
Show the name, current city, and source on the contact card. Put M02 in review first.
After I confirm, update only P01's city and preserve the old value and M02. Show where I can review or undo it.
Use the sample data only. Leave mail and contacts disconnected.
```

Add birthday reminders or a meeting brief once the underlying dates and contact identities are confirmed. For screenshots and other incoming material, see [one inbox](capture-inbox.md).

**Check it** · Only P01's city should change. Submitting M02 again after the update should give no new change. If another Lin Lan appears in the list and the next sender is unclear, the change stays in review.

**Reference** · [OpenClaw Personal CRM](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/main/usecases/personal-crm.md) is a community implementation using a database and periodic sync. This page uses a smaller review-first starter.
