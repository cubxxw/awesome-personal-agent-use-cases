# Price watch · Tell me when it fits my budget

[Home](../README.md) · [简体中文](../zh-CN/scenes/price-watch.md)

**A price watch Muse runs for you: you fix the conditions — what it is, which spec, and the all-in price ceiling — and it checks on schedule. It calls you only when an offer truly qualifies, and stays silent otherwise. Buying is always your move.**

## What you get

- **One alert when it qualifies** — price, spec, check time and the original page link, so you can verify and decide on the spot.
- **Only real matches count** — wrong seat count, wrong section, fees not yet counted: none of that is a hit. Offers with missing fields land in a "to check" list instead of being dressed up as deals.
- **A check log** — every check and its result is recorded, failed checks included, so you can see the watch is actually awake.

## Give this to Muse

Paste the whole block into your Muse. It builds the watch, then runs it with you.

```text
Build me a price watch.

First, fix the conditions with me: what we are watching (tickets, a flight, a product), the spec conditions (section, seat count, model, route and stop rules), the all-in price ceiling including every fee, and the last day to keep watching. If the conditions are not fully fixed, do not start checking.

Rules:
1. Check at the frequency we agree on, and log the time and result of every check. A failed check is logged too — never pretend you checked.
2. Only when every condition holds — right spec, all-in total at or under the ceiling — mark it a "hit" and alert me once, with the original page link.
3. Offers with missing fields (a headline price with unknown fees, say) go to "to check", never to hits.
4. One alert per hit. A new qualifying option earns a new alert.
5. You watch and report only — never book, never order. Before paying I will open the page myself and verify stock, price and terms.

Start now: ask me what to watch, fix the conditions one by one, then run the first check.
```

## How it runs

- **A hard threshold and silence otherwise** — on days nothing qualifies you hear nothing; when it speaks, there is a qualifying option.
- **Alerts and purchases stay separate** — the watch reports a lead. Whether it can actually be bought, and on what terms, is settled on the page you open before paying.

## Sources

- **Collection summary.** Watch conditions pinning seat count, section and all-in total at once. [Muse #162 - Watch four seats together in one section](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1057-L1062) · [Original post](https://x.com/BradyHannaKC/status/2112961536168005898)
- **Collection summary.** A nonstop alert arrived but the standby seat was not won — an alert and a purchase are different things. [Muse #377 - Nonstop alert, standby missed](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L896-L901) · [Original post](https://www.facebook.com/yourbossbaesteph/posts/pfbid037xRCh2jX5qXJjYEJ6Y3kGBYhqemmHzoUSWpozcxxGxSLotH8F1j84htxwkCkrYWRl)

## Building blocks

[Change watch](../usecases/change-watch.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
