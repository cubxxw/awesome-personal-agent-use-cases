# Friends and contacts · Remember where we left off

[Home](../README.md) · [简体中文](../zh-CN/scenes/personal-crm.md)

**One page per person. Everything you know about them, where you left off, and what you promised — kept current by your Muse, checked by you in seconds.**

## What you get

**A dossier per person** — one page that holds:
- Who they are: confirmed details only, each with its source
- Your history: every interaction on a dated timeline — who said what, to whom, when
- Open loops: follow-ups with dates, promises in stages (intended → agreed → scheduled → done)
- Two separate notes: *their* stated boundaries, and *your* goals for the relationship

**A pre-meeting card** — before you meet someone, Muse generates a one-screen brief from the dossier: their boundaries first, confirmed facts, what you already promised, your goals, and the unknowns listed as questions. The card is read-only and dated; gaps are shown, never filled in by guessing.

**A review queue** — anything Muse can't confidently attach to a person (an unidentified sender, a shared nickname) waits here for your call instead of being filed under a guess.

## Give this to Muse

Copy the whole block into Muse. It builds the Space, then runs it with you.

```text
Build me a contacts Space called "Friends and contacts".

Structure — one dossier per person, stored as plain text I can read and edit:
- Top of each dossier: current confirmed facts, each fact followed by its source in brackets.
- Below: an append-only timeline of interactions, newest last. Each entry: date, who said it, who it was said to, who was only mentioned, and a short verbatim excerpt.
- A follow-ups section: item, due date, and stage — intended, agreed, scheduled, done, or cancelled.
- Two separate fields: "Their boundaries" (only what they have expressed) and "My goals" (what I want from the relationship). Never mix them.

Rules:
1. One person, one dossier. People who share a name or nickname stay in separate dossiers until I confirm they are the same person.
2. Every fact is labelled: confirmed (with source), unknown (your inference — say so), or withdrawn. When I withdraw a fact, remove it from the dossier's confirmed section and from every brief or card built on it.
3. If you cannot tell who a message is from or who it belongs to, put it in a "To review" list and ask me. Never file it under a guess.
4. "I approved sending" and "it was actually sent" are different facts. Record both, separately.
5. Before I meet someone, generate a pre-meeting card from their dossier: their boundaries, confirmed facts with sources, my open promises with their stage, my goals, and a list of unknowns as questions for me. Show the card's date. If the dossier is thin, say so on the card instead of padding it.

Start now: create the Space, then ask me for the first three people to add.
From then on: when I tell you something about a person in chat, propose the dossier update and show me the exact change before saving it.
```

## Your part (two minutes, whenever)

- Confirm or reject proposed updates — nothing enters a dossier unconfirmed.
- Clear the "To review" queue when Muse asks: one tap per item, person A, person B, or discard.
- Glance at the pre-meeting card before the meeting; that glance is the quality check.

## How to check it

- Ask Muse: "What do I know about [person]?" Every fact in the answer must trace to a source you recognise. One fact you can't trace = the dossier needs a cleanup pass.
- Mention a shared nickname. Muse must ask which person you mean, not pick one.
- Withdraw a fact, then ask for the pre-meeting card again. The fact must be gone from the card too.

## Decision boundary

Muse proposes, you confirm: identity merges, dossier changes, and anything sent to another person always wait for your yes.

## Sources

- **Community recipe.** A different build of the same idea — automatic email/calendar scanning into a database table, briefings over chat. [OpenClaw Personal CRM](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/personal-crm.md)
- **Collection summary.** This assistant role included birthday and gift reminders as part of a deliberately narrow brief. [Muse #261 - Use confirmed birthdays to surface reminders](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1606-L1611) · [Original post](https://www.instagram.com/reel/DfFqwbsA9kx/)

## Building blocks

[Durable contact record](../usecases/personal-crm.md) · [Capture inbox](../usecases/capture-inbox.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Platform routes](../BUILDER.md)
