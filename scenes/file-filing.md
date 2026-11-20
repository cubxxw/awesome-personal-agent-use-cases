# Documents and records · Find that invoice months later

[Home](../README.md) · [简体中文](../zh-CN/scenes/file-filing.md)

A searchable file index with source, suggested folder and duplicates to review.

## Sample result

- **F1 · Software**. Keep its source message and amount CNY 90.
- **F2 · Possible duplicate of F1.** Same invoice number. Compare the files.
- **F3 · Review.** The scan is hard to read.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Draft an index for these receipts. Include filename, vendor, date, total, source ID and suggested folder. Show possible duplicates and uncertain fields. Keep each original. Open no external links and make no file changes.
F1 | april.pdf | Paper Cloud | no. PC-41 | 2026-04-12 | CNY 90 | invoice email
F2 | forwarded.pdf | Paper Cloud | no. PC-41 | 2026-04-12 | CNY 90 | forwarded copy
F3 | scan.pdf | vendor and amount unreadable | uploaded photo
```

## With a connected tool

Search within one approved folder or mailbox and first preview a source-to-destination list. Move copies only after checking destinations and retaining a way back to the original source.

## How to check it

F1 and F2 are flagged for comparison and not silently merged. F3 is visible for review. Verify one file by finding it from the index without looking in the original inbox.

## Decision boundary

File access, relocation and deletion have different effects. Approve moves in advance and leave originals available.

## How the cases fit together

The invoice cases show filing across inboxes or around a single business topic. The email-retrieval account adds an earlier step: pull likely candidates first, then inspect the text before filing.

- Switch to warranties, purchase confirmations or other documents you may need later.
- For a folder already full of files, create the index first and reorganize only if retrieval improves.

## Sources

- **Author account.** The author reports reading invoices from multiple mailboxes and classifying PDFs into a local filing scheme. [An author reports filing PDF invoices](https://www.reddit.com/r/openclaw/comments/1s5z1xp/i_gave_my_mac_mini_a_brain_a_security_system_and/)
- **Collection summary.** The collection describes email search and filing for one business context. It does not supply the actual folder or files. [Muse #356 - File receipts for a small stall](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1942-L1946)
- **Author account.** The author retrieved candidates by query and classified the message bodies separately. [Retrieving email candidates before classification](https://moontowermeta.com/unlocking-my-email-with-ai/amp/)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Platform routes](../BUILDER.md)
