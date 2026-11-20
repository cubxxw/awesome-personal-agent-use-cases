# Shopping and tickets · Tell me when it fits my budget

[Home](../README.md) · [简体中文](../zh-CN/scenes/price-watch.md)

A timestamped alert for a comparable offer, with the full price and a link to inspect.

## Sample result

- **Q2 matches.** Four seats together in section L, CNY 480 including fees.
- **Q3 needs a check.** The seller shows a base price but no total fee.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Check one batch of offers. I need four adjacent seats in section L, at no more than CNY 500 including all fees. Keep the offer ID and latest observed time. Return a match only when the criteria are visible. Put incomplete offers separately. Do not reserve or buy.
Q1 | 10:00 | 3 adjacent section L | CNY 420 incl. fees
Q2 | 10:05 | 4 adjacent section L | 4 x CNY 110 + CNY 40 total fees
Q3 | 10:06 | 4 adjacent section L | CNY 440 before fees | fees unknown
```

## With a connected tool

Pick a source that exposes all comparison fields and an end date for the watch. Try one read. Recheck a matching offer on its own page before acting. If you schedule checks, notify once per materially changed match.

## How to check it

Q2 is the only hit. Q1 is the wrong quantity, and Q3 remains incomplete. An inaccessible listing should be visible as a failed check.

## Decision boundary

An alert is a lead. Check inventory and terms yourself before paying.

## How the cases fit together

Tickets and flights can share one watch rule once comparable terms are defined. One air-travel example also records a hit that never secured a seat, so the card needs a separate purchase state.

- For flights, include route, stops, traveler count and required baggage in the comparable price.
- For a saved product, match the exact model before looking at shipping and price.

## Sources

- **Collection summary.** The watch combined a seat count, section and budget. A match and a completed purchase are separate steps. [Muse #162 - Watch four seats within a budget](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1057-L1062) · [Original post](https://x.com/BradyHannaKC/status/2112961536168005898)
- **Collection summary.** The collection describes an alert and an unsuccessful standby attempt. A hit can be useful without securing inventory. [Muse #377 - A direct flight alert that did not secure a seat](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L896-L901) · [Original post](https://www.facebook.com/yourbossbaesteph/posts/pfbid037xRCh2jX5qXJjYEJ6Y3kGBYhqemmHzoUSWpozcxxGxSLotH8F1j84htxwkCkrYWRl)

## Building blocks

[Change watch](../usecases/change-watch.md) · [Scheduled delivery](../usecases/scheduled-task.md) · [Platform routes](../BUILDER.md)
