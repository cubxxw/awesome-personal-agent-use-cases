# Renewals and deadlines

[Home](../README.md) · [简体中文](../zh-CN/usecases/renewal-ledger.md)

Keep a list of things that need a decision by a date. Start with three receipts or notices. Later you can add memberships, returns, or borrowed items.

## Sample result

| When | Decision | Evidence |
| --- | --- | --- |
| 24 November | Decide whether to renew Paper Cloud for CNY 48. | R1 · renewal notice |
| Date to check | Find the actual charge date for the Studio Pass trial. | R3 · welcome email |

The workshop membership is outside the current window. It stays in the full ledger.

## Try it once

Paste this into your agent. The services, amounts, and dates are fictional.

```text
Use only these notices. Make a list of decisions due from 2026-11-20 through 2026-11-27 inclusive.
Keep the service, amount and currency when known, date, decision, and source ID.
Put unknown dates under To check. Keep later dates in the full ledger.
Do not infer a billing date from "soon." Give me a review list in this chat.

R1 | Paper Cloud | Renewal notice | CNY 48 | 2026-11-24 | Decide whether to renew
R2 | Workshop membership | Confirmation | CNY 120 | 2026-12-03 | Decide whether to renew
R3 | Studio Pass trial | Welcome email | Unknown price | Trial ends soon | Confirm charge date
```

## Keep the ledger useful

1. Give each item an ID and a link or reference to the original notice. Keep the next known date, status, and decision together. If the provider identifies different accounts for the same service, store them separately.
2. Review new receipts or notices before writing back. A payment receipt can confirm a past charge. Record a future renewal date when you have evidence for that date.
3. Use [a scheduled task](scheduled-task.md) to read the confirmed dates. Keep “wants to cancel” and “cancelled” as separate statuses. Record the confirmation from the service when the cancellation is complete.

**Check it** · R1 is the only item due in the chosen window. R3 has no date and stays in review. Run the same notice twice and keep one entry for it.

**Reference** · For subscriptions billed through Apple or Google Play, consult the applicable account and billing instructions. [Apple subscriptions](https://support.apple.com/en-us/118428) · [Google Play subscriptions](https://support.google.com/googleplay/answer/7018481)
