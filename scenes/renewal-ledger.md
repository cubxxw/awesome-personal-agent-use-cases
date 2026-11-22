# Subscription ledger · Tell me before I'm charged again

[Home](../README.md) · [简体中文](../zh-CN/scenes/renewal-ledger.md)

**A subscription ledger Muse keeps for you: what you subscribe to, which channel charges you, how much, when the next charge lands, and whether you are paying twice. It calls you before the money leaves — keep or cancel is your call.**

## What you get

- **One table of everything you pay for** — one row per service: paying account, the actual billing channel, amount and currency, next charge date, and where the original notice is. Past charges and future charges recorded separately.
- **A warning before each charge** — two days ahead by default (adjustable), with what it costs, through which channel, and whether you have actually been using it.
- **Duplicate-subscription alerts** — the same service billed through two channels (an app store copy and a website copy, say) gets flagged on its own so you can check the accounts. This is how double payments hide.
- **A dedicated home for notices** — sign up for new services with the agent's own mailbox, and renewals, charges and verification codes land there. The ledger feeds straight from that mailbox instead of digging through your personal inbox.

## Give this to Muse

Paste the whole block into your Muse. It builds the ledger, then runs it with you.

```text
Build me a subscription ledger called "Subscriptions and bills".

Scan the receipt inbox I name, read-only. Start with the last two billing cycles of receipts to find what is still renewing, then use renewal notices to pin down each service's next charge date.

Each row records: service name, paying account, the actual billing channel, amount and currency, next charge date, and the source notice. A date you cannot find stays "to confirm" — never guess one.

Rules:
1. If one service shows two billing channels, flag it "possible duplicate" and remind me to check the accounts. Never merge them on your own.
2. Remind me two days before each charge (I can change the lead time), with the amount, the channel, and recent actual usage if you know it.
3. When I decide to cancel, record "decided to cancel". Only when the provider confirms does it become "cancelled". A refund counts only when the payment record shows it arrived; until then it stays on the ledger.
4. The same notice arriving twice still produces one row.
5. When I have an agent mailbox of my own, sign new subscriptions up with it and feed the ledger from its renewal and charge notices. A notice there only becomes a row once it matches a receipt in my personal inbox; anything that does not match gets flagged for me — never merge on your own.

Start now: set up the ledger, then ask me which inbox to scan and how far back.
```

## How it runs

- **Receipts and notices feed it** — a new receipt arrives and the ledger grows itself; you never have to remember to log a subscription.
- **The intake moves upstream** — services signed up with the agent mailbox drop their notices there the moment they are issued, so the ledger no longer waits for you to remember forwarding a receipt.
- **The reminder is its only noise** — no charge coming up, no message. When it speaks, money is about to leave.
- **Decision and execution stay separate** — you said cancel, the provider confirmed, the refund landed: three different facts, and the ledger keeps them apart.

## Sources

- **Collection summary.** Six months of receipts mined for forgotten subscriptions. [Muse #213 - Find renewing subscriptions in past receipts](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L386-L391) · [Original post](https://x.com/idobn/status/2097570513107272175)
- **Collection summary.** One service billed through two channels — a real case. [Muse #334 - One service, two billing channels](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L519-L524) · [Original post](https://www.threads.com/@jamiancpolk/post/Dfk4Qj0kQht)
- **Collection summary.** List every subscription first, then confirm cancellations one by one. [Muse #317 - List subscriptions, then confirm each cancellation](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L505-L510) · [Original post](https://www.facebook.com/reel/1471540751575508/)

## Building blocks

[Date ledger](../usecases/renewal-ledger.md) · [Scheduled task](../usecases/scheduled-task.md) · [Capture inbox](../usecases/capture-inbox.md) · [Choosing a platform](../BUILDER.md)
