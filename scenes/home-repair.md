# Home and repairs · Find who fixed it last time

[Home](../README.md) · [简体中文](../zh-CN/scenes/home-repair.md)

The right work order, a contact lead to verify and any missing details for a new quote.

## Sample result

- **Living room unit M8 · F1.** That work order identifies Pine Service.
- **Check first.** The phone number is from the old record. Verify it before sharing your address.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Identify who previously repaired living room unit M8. Give the match, service date, source, and the detail I need to verify. Keep other equipment separate. If no record matches, list the model, specification and photos needed for a quote request.
F1 | living room AC M8 | 2026-04-05 | Pine Service | work order and contact on file
F2 | hall AC N4 | 2026-06-16 | River Service | service receipt
F3 | living room AC | 2026-11-18 | owner note | new fault, appointment not made
```

## With a connected tool

Search one mailbox or folder you choose for the model number, work orders and invoices. When no exact match exists, return a shortlist or collect details for a comparable quotation.

## How to check it

F1 is the only exact match. F2 stays out. Show F3 as a new issue and avoid treating the old contact as a confirmed new booking.

## Decision boundary

Get confirmation before sending a message, sharing a photo or booking work. Keep a quote and an agreed visit in separate fields.

## How the cases fit together

The repair lead begins with a past work order. The door-quote example begins with a spec sheet and photos. Both help a person contact the right provider, with different evidence at the start.

- Store the last contact and invoice beside the appliance model. A later lookup should return both.
- With no usable record, collect comparable specs and ask for quote drafts before contacting anyone.

## Sources

- **Collection summary.** The author describes searching Gmail for a previously used contractor. This edition could not reopen the post directly. [Look up the last repair provider](https://x.com/drsnow/status/2103462003025084763)
- **Collection summary.** The buyer supplied dimensions and photos and received offers. The collection records quotations rather than a selected contractor. [Muse #196 - Ask for comparable local repair quotes](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L1535-L1540) · [Original post](https://x.com/derekreyn22/status/2116579704110985606)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Platform routes](../BUILDER.md)
