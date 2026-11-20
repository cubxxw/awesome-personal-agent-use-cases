# Email and messages · Which ones need my reply today?

[Home](../README.md) · [简体中文](../zh-CN/scenes/inbox-triage.md)

A short inbox list with urgent replies, items to review later and messages that need no action.

## Sample result

- **Reply before 15:00 · E1.** The supplier needs the proof approved today.
- **Read later · E2.** Newsletter, no stated action.
- **Check · E3.** Attachment not available.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Sort these messages into Reply today, Review later and Needs information. Use what the sender actually asks for. Preserve the deadline and input ID. For a reply, give a one-line draft and leave it unsent. Keep inaccessible attachments visible.
E1 | supplier | Please confirm the proof by 15:00 today.
E2 | newsletter | This week's reading list.
E3 | colleague | See the attached request | attachment unavailable
```

## With a connected tool

Start with one mailbox or chat and a short time window. Read messages, return a private queue, then compare it with what you would answer yourself. Add urgent alerts only after defining when an interruption is justified.

## How to check it

E1 contains the stated 15:00 deadline. E2 stays outside the reply queue. E3 remains visible as incomplete. An unsent draft still needs you to act.

## Decision boundary

Sending, archiving and unsubscribing are separate actions. Review the proposed action and recipient before using any write access.

## How the cases fit together

A newsletter digest and a multi-inbox assistant both decide what deserves attention. The latter can add a draft or an urgent alert without combining them with permission to send.

- Use a quiet newsletter digest when you only need to catch up.
- Use the same sorting rule for a busy project chat. Only requests addressed to you go into the reply queue.

## Sources

- **Author account.** The writer describes using Hermes across several inboxes and retaining the decision to send. [Several months triaging email with Hermes](https://www.reddit.com/r/hermesagent/comments/1w7dtpp/what_i_learned_after_running_hermes_as_my/)
- **Community recipe.** The setup gives newsletters a separate digest and recommends a scoped inbox. [Inbox de-clutter](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/inbox-declutter.md)
- **Collection summary.** The collection describes a routine with morning priorities and email drafts that still require review. [Muse #355 - Morning briefing and reply drafts](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1935-L1940) · [Original post](https://www.reddit.com/r/MetaAI/comments/1xryn81/ive_been_using_muse_as_a_personal_assistant_for_a/)
- **Collection summary.** The assistant screened multiple inboxes and used a separate interruption channel for urgent items. [Muse #265 - Only interrupt for urgent email](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1634-L1639) · [Original post](https://www.instagram.com/reel/DfSKoatiebb/)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Platform routes](../BUILDER.md)
