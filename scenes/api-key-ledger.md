# API key ledger · Every key, quota and expiry in one place

[Home](../README.md) · [简体中文](../zh-CN/scenes/api-key-ledger.md)

**An API key ledger Muse keeps for you: every platform's plan, how much quota each key has left, when it expires, and where the key lives. It re-checks quotas on a schedule and writes the real numbers back; you store each key in one place, copy it with one click, and ask Muse to read one back whenever you need it.**

## What you get

- **One board for everything** — subscriptions and API keys on a single board, one row per platform: plan, price, total quota, used and remaining, status, expiry date. A platform with two keys gets two rows, never merged.
- **Measured quotas, not guesses** — where a provider's own API reports usage, Muse checks it and writes the number back with its check date. Where no balance endpoint exists, the row says "dashboard only" instead of inventing a figure.
- **Dead keys caught the same week** — an expired token surfaces in the weekly check instead of failing mid-task when you actually need it. Replacement keys arrive through secure entry, never pasted into chat.
- **Keys you can actually get back** — paste a key into its row once: it sits masked, copies with one click, and Muse reads it back to you in chat when you ask. Keys in the secure vault are a second track: Muse can call with them, but nobody can read the value back out — keep a copy on the board if you want it copyable.
- **Cleanup stays your call** — mark each row keep, review, or cancel, then filter to just the cancel list. A mark is a decision record, not an execution: Muse confirms with you one by one before anything is cancelled.

## Give this to Muse

Paste the whole block into your Muse. It builds the ledger, then runs it with you.

```text
Build me an API key ledger that manages my platform subscriptions and API keys.

First the ledger itself: one row per platform recording plan, price, total quota, used and remaining (with the date it was checked), status, expiry or renewal date, and the key's name and where it is stored. The ledger holds metadata only — never a key value. A date you cannot find stays "to fill in", never a guess.

Then a board I can open (a Space or similar page): the ledger synced onto it, each row with a cleanup mark (keep / review / cancel), a "to clean up" filter, and expiry dates I can fill in inline.

Rules:
1. Where a provider API reports usage or account state, measure it (usage endpoints, account-info endpoints) and record the number with its date. Where no balance endpoint exists, mark the row "dashboard only" — never estimate.
2. Keys live on two tracks. Keys Muse calls with go into the secure vault: usable, never readable back. Keys I want to copy myself, I paste into the board row myself: stored masked, one click to copy, and you must be able to read them back to me from the board.
3. New keys arrive through secure entry, not pasted into chat. When a check finds a key expired or invalid, flag it the same day and tell me how to replace it.
4. Multiple accounts or keys on one platform stay separate rows, never merged — when two keys' quotas do not line up, they are usually two different accounts.
5. Check weekly, folded into a report I already get (such as a Monday morning brief), never as a new noise channel. Speak only when a balance drops below my line, a key is expired or invalid, or an expiry falls within 30 days. Silent otherwise.
6. A cleanup mark records my decision; it is not an execution. Before cancelling a subscription or deleting a key, confirm with me one by one.

Start now: build the ledger and the board, enter my current platforms one by one, and measure every quota that can be measured in the first pass.
```

## How it runs

- **The check rides an existing report** — quota updates land inside your weekly brief, and both the board and the ledger file are refreshed after each check.
- **Subscriptions and keys share one board** — the renewal ledger scene covers the charges side (billing channels, duplicates, next charge) in depth; this scene covers the keys and quotas side.
- **The split is written down** — which key sits in the vault, which on the board, which only in a local config: the ledger says so, so the next session (or the next agent) never has to guess.

## Sources

- **Provider API.** TikHub's account and key-status endpoint returns balance, key name, scopes and expiry in one read. [TikHub docs](https://docs.tikhub.io/)
- **Provider API.** Tavily's usage endpoint reports plan, used credits and remaining per account — which is how two keys turned out to belong to two different accounts. [Tavily docs](https://docs.tavily.com/)
- **Provider behavior.** Exa offers no balance endpoint; the balance is visible only on its dashboard billing page, so rows like it are marked "dashboard only". [Exa dashboard](https://dashboard.exa.ai/)

## Building blocks

[Date ledger](../usecases/renewal-ledger.md) · [Scheduled task](../usecases/scheduled-task.md) · [Choosing a platform](../BUILDER.md)
