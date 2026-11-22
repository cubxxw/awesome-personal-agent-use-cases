# Inbox triage · Which ones need my reply today?

[Home](../README.md) · [简体中文](../zh-CN/scenes/inbox-triage.md)

**A morning triage list Muse makes from your inbox: mail and messages sorted into "reply today, read later, waiting on material", each with its deadline, who is waiting on you, and what is missing. Replies are drafted first and sent only after you approve; only what you define as truly urgent interrupts you.**

## What you get

- **One short list** — replies needed today come first, each saying who is waiting, what they are waiting for, and by when. Newsletters and notifications sink to "read later" on their own.
- **Reply drafts** — every must-reply message arrives with a draft waiting for your approval. When you edit it before sending, Muse asks what it should learn from your edit — and drafts that way next time.
- **Tiered interruption** — ordinary mail only enters the list; only the senders and topics you mark urgent earn an instant alert.
- **Machine mail in its own pile** — deploy results, task reports and monitoring alerts sent by systems and agents go to the agent's own mailbox, never your personal inbox. Triage keeps them in their own section and surfaces only the ones that need your decision.

## Give this to Muse

Paste the whole block into your Muse. It builds the triage, then runs it with you.

```text
Build me an inbox triage that gives me one list every morning.

Scope: the inboxes and message sources I name, recent dates only. Classify by what the sender is actually asking for, not by the subject line.

The list has three sections:
1. Reply today — someone is waiting on me. For each: who, what they are waiting for, the deadline, and the source message.
2. Read later — nothing to do (newsletters, notifications, cc's). Titles only.
3. Waiting on material — attachments you cannot read or information that is incomplete. List them anyway and say what is missing; never pretend you read them.

Rules:
1. For every "reply today" item, draft the reply first. Send only after I approve or edit it; an unapproved draft stays on the list — never send on your own.
2. When I edit your draft, ask me before sending: what should you learn from this edit? Record the answer and draft that way from then on.
3. The urgency bar is mine to set (which people, which topics may interrupt me instantly). Anything not on it goes to the list only.
4. Replying, archiving and unsubscribing are three separate actions. Never bundle them.
5. Notices from machines and agents are triaged from the agent's own mailbox only — my personal inbox stops receiving that kind. They default to "read later"; only one that needs my decision moves up to "reply today".

Start now: ask me which inbox to connect and from which date, then show me the first list.
```

## How it runs

- **The list is the only morning stop** — however full the inbox gets, you read one list; when it is done, the replies are out and the rest is accounted for.
- **Drafts start sounding like you** — every edit teaches it once; after a few weeks most drafts need a glance, not a rewrite.
- **People and machines enter separately** — people reach you through your personal inbox, machines reach the agent through its own mailbox. In the morning you read one triaged list; neither inbox needs digging through yourself.

## Sources

- **Author account.** Triage across several inboxes, with sending kept in human hands. [A Hermes user's multi-inbox triage](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)
- **Community recipe.** Newsletters collected separately, with a bounded inbox scope. [Collect newsletter mail separately](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/inbox-declutter.md)
- **Collection summary.** A morning action list plus reply drafts waiting for approval. [Muse #355 - Morning brief and drafts awaiting approval](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1935-L1940) · [Original post](https://www.reddit.com/r/MetaAI/comments/1xryn81/ive_been_using_muse_as_a_personal_assistant_for_a/)
- **Collection summary.** Ordinary mail and urgent alerts take different exits. [Muse #265 - Only urgent mail interrupts me](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1634-L1639) · [Original post](https://www.instagram.com/reel/DfSKoatiebb/)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
