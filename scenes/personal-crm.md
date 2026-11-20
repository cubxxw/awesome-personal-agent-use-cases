# Friends and contacts · Remember where we left off

[Home](../README.md) · [简体中文](../zh-CN/scenes/personal-crm.md)

One contact card with the latest confirmed details, last conversation and open follow-ups.

## Sample result

- **P01 · Lin Lan**. Review the city change from Nanjing to Suzhou [M02].
- **Leave M03 unlinked.** The sender with the same name has not been identified.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Suggest contact-card updates from the material below. Show the person ID, old and new values, and source. Leave the card unchanged pending approval. Remember only confirmed details and commitments. If the sender is not identified, keep the note in review.
P01 | Lin Lan | current city Nanjing | last conversation April
P02 | Lin Lan | colleague from another project
M02 | confirmed sender P01 | I moved to Suzhou this week.
M03 | sender shown as Lin Lan, identity unclear | Let's catch up sometime.
```

## With a connected tool

Start with a sheet or a contact Space you review yourself. Keep an ID for the contact, a source for each fact, and a queue for unclear changes. After reviewing a saved update, open the card in a new conversation and ask for a one-line pre-meeting brief.

## How to check it

Only P01’s city is proposed for change. M03 stays unlinked. Submit M02 again after confirming it and check the existing card instead of creating a second contact.

## Decision boundary

You confirm identity and any outbound message. Keep a suggestion to meet separate from an agreed date. Store details only as needed for the relationship.

## How the cases fit together

The CRM recipe makes the person and interaction record durable. The birthday example shows a way to use a confirmed date from that record. The same contact can feed a meeting brief later.

- Build a contact and review panel in Muse Space or a sheet. Start with the same two fictional messages.
- Use the card for a birthday reminder or to remember an open promise before meeting someone.

## Sources

- **Community recipe.** The recipe combines contacts, interaction history and meeting preparation. [OpenClaw Personal CRM](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/personal-crm.md)
- **Collection summary.** This assistant role included birthday and gift reminders as part of a deliberately narrow brief. [Muse #261 - Use confirmed birthdays to surface reminders](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1606-L1611) · [Original post](https://www.instagram.com/reel/DfFqwbsA9kx/)

## Building blocks

[Durable contact record](../usecases/personal-crm.md) · [Capture inbox](../usecases/capture-inbox.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Platform routes](../BUILDER.md)
