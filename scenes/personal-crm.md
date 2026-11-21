# Friends and contacts · Remember where we left off

[Home](../README.md) · [简体中文](../zh-CN/scenes/personal-crm.md)

**One page per person: what you know, where you left off, what you promised. Muse maintains it; you check it in seconds.**

## What you get

- **A dossier per person** — confirmed facts with sources, an interaction timeline, open follow-ups, and two separate fields: *their* stated boundaries and *your* goals.
- **A pre-meeting card** — one screen generated from the dossier before you meet: boundaries first, then confirmed facts, your open promises, your goals, and the unknowns as questions. Dated, read-only, and it says so when the dossier is too thin.
- **A review queue** — anything Muse cannot attribute (unknown sender, shared nickname) waits here for your call. It never guesses its way into a dossier.

## Give this to Muse

Paste the whole block into your Muse. It builds the Space, then runs it with you.

```text
Build me a contacts Space called "Friends and contacts".

One plain-text dossier per person, readable and editable by me:
- Top: the currently confirmed facts, each with its source in parentheses. Include the person's contact channels — email, phone, WhatsApp, LinkedIn, any platform — as facts on the same dossier: one identity, many channels, never a separate entry per platform.
- Below: an append-only timeline of interactions, newest last, from every channel. Each entry: date, channel, who said it, who it was said to, who was only mentioned, and a short verbatim excerpt.
- Follow-ups: item, due date, stage — intent, agreed, scheduled, done, or dropped.
- Two separate fields: "Their boundaries" (only what they expressed themselves) and "My goals" (what I want). Never merge them.

Rules:
1. One person, one dossier. Same name or nickname stays separate until I confirm it is the same person.
2. Every fact carries a state: confirmed (with source), unknown (your inference — label it), or withdrawn. When I withdraw a fact, remove it from the confirmed section and from every brief or card built on it.
3. Anything you cannot attribute goes to a "To review" list and you ask me. Never guess it into a dossier.
4. "I approved sending" and "the system confirmed it was sent" are two different facts. Record both, separately.
5. Before I meet someone, generate a pre-meeting card from their dossier: their boundaries, confirmed facts with sources, my open promises with stages, my goals, and the unknowns as questions. Date the card. If the dossier is thin, say it is thin — never pad it.

Growing the base:
- From my accounts: watch the mail, calendar, and chat accounts I have connected. Someone who is not filed yet becomes a proposed dossier. Attach anything to an existing dossier only on a phone or email match — a name alone is never enough; the rest goes to To review.
- From my address book: when I import contacts, fill in channels and birthdays on existing dossiers by phone/email match. Unmatched entries go to To review, not into new dossiers.
- From my screen: when I show you something — a chat window, a business card, a profile page — extract the people in it and propose a new dossier or an update. Propose only; I confirm before anything is filed. Never scrape or file silently in the background.
- From chat history: when I give you an exported conversation, backfill the timeline with dated excerpts, and keep the full export as a local file the excerpts point to. Never paste whole transcripts into a dossier.
- By asking me: when a name keeps appearing unattributed, or a dossier is too thin before a meeting, ask me the one missing question instead of guessing.
- Across platforms: when I give you a new channel for someone who already has a dossier, attach it to that dossier and ask if it changes anything else.

Start now: set up the Space, then ask me for the first three people.
From then on: when I mention something about a person in chat, show me the proposed dossier update verbatim and save it only after I confirm.
```

## How it grows

A dossier system is only as good as its intake. Every channel below feeds the same propose-and-confirm gate, and merges happen on strong keys only — phone and email, never a name alone:

- **From your connected accounts** — a new sender in your mail, a new attendee on your calendar, a new chat contact: each becomes a proposed dossier, matched to an existing one by phone or email.
- **From your address book** — one import fills in channels and birthdays for people already filed; whatever matches nothing waits in the review queue.
- **From your screen** — show Muse a chat, a card, a profile page; it drafts the dossier or update (computer use as an input, never silent scraping).
- **From chat history** — export a conversation (WeChat, WhatsApp, Telegram) and the timeline backfills with dated excerpts; the full text stays in a local file the excerpts point to, never inside the dossier.
- **By asking you** — an unattributed name that keeps recurring, a gap before a meeting: Muse asks the one question that unblocks it, instead of guessing.
- **Across platforms** — email, WhatsApp, LinkedIn, phone are channels on one dossier, so a conversation that moves platforms stays one history.

## Sources

- **Community practice.** The same idea built the other way — auto-scan mail and calendar into a database table, briefings by chat query. [OpenClaw personal CRM](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/personal-crm.md)

## Building blocks

[Personal CRM](../usecases/personal-crm.md) · [Capture inbox](../usecases/capture-inbox.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
