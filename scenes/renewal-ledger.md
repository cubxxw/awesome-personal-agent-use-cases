# Bills and subscriptions · Tell me before I’m charged again

[Home](../README.md) · [简体中文](../zh-CN/scenes/renewal-ledger.md)

A renewal shortlist with the next date, billing channel and notice for each decision.

## Sample result

- **24 November · Paper Cloud · CNY 48**. Decide whether to renew. A two-day lead time puts the reminder on 22 November [A2].
- **Video Pass · check for overlap.** Two channels appear in B1 and B2. Confirm the accounts.
- **Studio trial · date unknown.** Ask for the next charge date. Evidence T1.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Use these notices to build a subscription ledger as of 2026-11-20.
Show the confirmed charges due by 2026-11-27 and preview reminders two days ahead. Put missing dates and possible overlaps in a review section. Record the actual billing channel and cite an input ID for every row. Keep evidence of past charges separate from future dates. Propose next steps here only.
A1 | Paper Cloud | website | charge on 2026-10-24 | CNY 48
A2 | Paper Cloud | website | next renewal 2026-11-24 | CNY 48
B1 | Video Pass | app store | active | next charge 2026-12-02
B2 | Video Pass | video bundle | active | next charge 2026-12-09
T1 | Studio trial | welcome message | charge date unknown
```

## With a connected tool

Search one approved mailbox for receipts and renewal notices in an agreed date range. Save the service, account, billing channel, currency, next date and source in a table you control. Send one test reminder for a confirmed date before enabling a recurring check.

## How to check it

A2 alone goes in the coming week, with a reminder preview for 22 November. B1 and B2 are two records with a possible overlap. T1 has no invented date. Import A2 twice and check that the same notice is recorded once.

## Decision boundary

You decide what to keep or cancel. Record a cancellation only after the billing provider confirms it. Record a refund after the payment record shows it.

## How the cases fit together

The receipt search, duplicate-charge report and cancellation flow all need the same subscription record. They describe different states of that record. A receipt proves a past charge. A renewal notice supports a future date. A cancellation confirmation can change the status.

- Use two past receipts to find a possible recurring charge. Follow up for the actual renewal date.
- Use the same table for membership expiry or a return deadline. Swap the decision and keep the date and its source.

## Sources

- **Collection summary.** The collection attributes one forgotten renewal to a six-month receipt review. Entries 17 and 213 describe the same account. [Muse #213 - Find a recurring charge in the receipts](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L386-L391) · [Original post](https://x.com/idobn/status/2097570513107272175)
- **Collection summary.** The reported duplicate used two billing channels. The account and billing channel belong in the ledger even when the service name matches. [Muse #334 - One service paid through two channels](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L519-L524) · [Original post](https://www.threads.com/@jamiancpolk/post/Dfk4Qj0kQht)
- **Collection summary.** The collection describes a read-only audit followed by selected cancellations and a dashboard update. It leaves the refund outcome open. [Muse #317 - Subscription list followed by cancellation review](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L505-L510) · [Original post](https://www.facebook.com/reel/1471540751575508/)

## Building blocks

[Date ledger](../usecases/renewal-ledger.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Capture inbox](../usecases/capture-inbox.md) · [Platform routes](../BUILDER.md)
