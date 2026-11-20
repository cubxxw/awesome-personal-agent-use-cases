# Travel · Put all the bookings on one page

[Home](../README.md) · [简体中文](../zh-CN/scenes/trip-brief.md)

A trip sheet with local times, confirmation sources and the gaps to check before leaving.

## Sample result

- **11 December, 06:20 JST · Arrival** [F1].
- **Hotel date to check.** Booking H1 begins on 10 December, before local arrival.
- **Transfer pending.** T1 gives a pickup day and no confirmed time.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Make a trip sheet from these confirmations. Sort by local date and time, preserve time zones and source IDs, and flag any dates that might conflict. Add a guest-facing version with dates and places only. Do not modify a booking.
F1 | depart 2026-12-10 22:40 SGT | arrive 2026-12-11 06:20 JST | flight confirmed
H1 | check-in 2026-12-10 15:00 JST | Central Hotel | confirmed
T1 | 2026-12-11 JST | station pickup | time pending
```

## With a connected tool

Read the trip’s confirmation emails or files and link only the entries that belong to that trip. Make the personal trip sheet first. Review a shorter copy separately when sharing it.

## How to check it

The flight arrives on 11 December at destination time. The hotel date is a check, not an invented booking change. T1 stays pending.

## Decision boundary

You approve any itinerary change or sharing. Keep booking numbers, costs and details about other travelers out of the guest-facing copy unless needed.

## How the cases fit together

A master itinerary preserves every booking reference. A host-facing copy selectively uses that same itinerary. Keeping one primary sheet allows a change to flow into both views.

- With only confirmations, assemble the itinerary in chat and verify each link before traveling.
- If a host needs to know when you arrive, derive a small copy from the same confirmed records.

## Sources

- **Collection summary.** The itinerary brought confirmation numbers and the source messages together. [Muse #153 - Gather confirmations into one itinerary](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L718-L723) · [Original post](https://x.com/matthew_verni/status/2112120235016716442)
- **Collection summary.** The same travel information was reduced to dates, cities and lodging for the recipient. [Muse #245 - A version of the itinerary for the host](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L775-L780) · [Original post](https://www.facebook.com/groups/1412054144392596/permalink/1448423130755697/)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Platform routes](../BUILDER.md)
