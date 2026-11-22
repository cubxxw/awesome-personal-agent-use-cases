# Agent mailbox · An inbox of its own

[Home](../README.md) · [简体中文](../zh-CN/scenes/agent-mailbox.md)

**A mailbox that belongs to the agent alone, fully separate from your personal inbox: it holds the verification codes and service notices it receives, the reports other agents and systems send it, the feedback people write to it, and the identity it sends from. It cannot see your personal mail, and anything it sends is drafted for you first — it goes out only after you approve.**

## What you get

- **An address you can publish** — sign up for services with it, give it to your project's users for feedback, put it on a product page. Everything that arrives is the agent's business, not yours.
- **One fixed landing spot for codes and notices** — services the agent registers, verifies or watches on your behalf send their mail here. It reads and handles them itself, and only brings you the ones that need your decision.
- **A postal route between agents** — other agents mail their reports, handoff notes and results here; yours receives and files them. Different tools and different vendors can still reach each other.
- **Sending passes through you** — it drafts, you approve, then it sends. Ask at any time what came in and what went out today, and it can tell you.

## Give this to Muse

Paste the whole block into your Muse. It sets the mailbox up, then runs it with you.

```text
Set up a dedicated mailbox for the agent, separate from my personal inbox.

Register an address with the agent-mailbox service I name (if there isn't one yet) and record it. This mailbox is for the agent only: it does not read my personal inbox, and my personal inbox is not connected to it.

The mailbox handles four kinds of mail:
1. Verification codes and service notices — sign-ups, verifications, renewals, status changes all land here.
2. Reports from machines and agents — deploy results, task receipts, monitoring alerts.
3. Feedback addressed to the agent — questions and suggestions from my project's users and collaborators.
4. The agent's own outgoing mail — replies, notices and handoff notes sent from this address.

Rules:
1. Sending, replying and forwarding are always drafted for me first and go out only after I approve. If the service has its own confirmation step, use it — never work around it.
2. Triage what arrives: file what can be handled directly (archived, entered into the ledger, stored away) and report only what needs my decision and anything abnormal. Silence when there is nothing.
3. A verification code is used only for the sign-up or login the agent is performing right then; it is not kept or forwarded afterwards. A code request whose origin does not check out gets asked about before use.
4. This address may be published, but my personal email, phone number and other personal details never appear in its signature or in mail it sends.
5. Keep a daily tally of what was received, what was sent, and what is still waiting for my approval, so you can account for it when I ask.

Start now: create or confirm the address, then ask me what the first thing it should receive is.
```

## How it runs

- **Isolation is the default** — if stray mail ever leads the agent astray, the damage stops at this one mailbox. Your personal mail and contacts stay out of reach.
- **It is the intake for many other scenes** — the subscription ledger takes renewal notices from here, inbox triage takes machine reports from here, handoff notes are sent and received from here. The mailbox produces no lists itself; once the intake is clean, the other scenes run on their own.

## Sources

- **Official product.** The QQ Mail team's mailbox service for agents: isolated from personal mail, authorized by WeChat scan, CLI access, two-stage confirmation for write actions. [Agent Mail](https://agent.qq.com/) · [Setup doc](https://agent.qq.com/doc/cli-setup.md)
- **Walkthrough.** Creating an address, binding an agent, and using it in natural language or by CLI. [Agent Mail setup guide (Tencent Cloud Developer Community)](https://developer.cloud.tencent.com/article/2701501)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
