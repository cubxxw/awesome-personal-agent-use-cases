# File cabinet · Find that invoice months later

[Home](../README.md) · [简体中文](../zh-CN/scenes/file-filing.md)

**A file cabinet Muse keeps for the documents you will need again — invoices, receipts, warranties, contracts. Originals stay untouched; it builds a searchable index: which merchant, which date, how much, and where the original lives. Months later, one question brings it back.**

## What you get

- **A searchable index** — one row per file: name, merchant, date, amount, category, and where the original is. Ask by merchant, amount or month.
- **Preview before filing** — first a destination list: which file should go to which folder. Only after you approve does it copy anything; originals are always kept.
- **Duplicate alerts** — the same invoice arriving from two inboxes (same number, same amount) is flagged "possible duplicate" for you to compare. Nothing is merged or deleted automatically.

## Give this to Muse

Paste the whole block into your Muse. It builds the cabinet, then runs it with you.

```text
Build me a file cabinet. Index first — do not move any originals.

Scope: the inbox or folders I name, read-only. Look for the files I will need again: invoices, receipts, warranties, contracts.

Each index row records: file name, merchant, date, amount, category, source (which message, which folder), and where the original lives. A field you cannot read is marked "to check" — never guess it.

Rules:
1. Possible duplicates — same invoice number, or same merchant + date + amount — are flagged for me to compare. Never merge them, never delete either copy.
2. Filing starts with a preview: a suggested folder for every file. Only after I approve the whole list do you copy files over. Originals stay where they are; the index records the new location.
3. Moving and deleting are separate permissions. Approving a filing is not permission to delete an original.

Start now: ask me which inbox or folder to start with, then show me an index preview.
```

## How it runs

- **Index first, tidying second** — however messy the folders are, the index already makes things findable; reorganizing the folders never blocks using it.
- **New files file themselves** — a new receipt or warranty gets an index row as it arrives, so the cabinet never goes stale.

## Sources

- **Author account.** PDF invoices pulled from several inboxes and filed under the author's own categories. [Filing PDF invoices from email](https://www.reddit.com/r/openclaw/comments/1s5z1xp/i_gave_my_mac_mini_a_brain_a_security_system_and/)
- **Collection summary.** Receipts for one small business extracted from mail and filed. [Muse #356 - File a small business's receipts from email](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1942-L1946)
- **Author account.** Keyword search first for candidates, then full-text reading to classify. [Find candidates in email first, then judge what they are](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Choosing a platform](../BUILDER.md)
