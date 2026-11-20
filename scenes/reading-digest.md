# News and reading · Only show me what matters to this topic

[Home](../README.md) · [简体中文](../zh-CN/scenes/reading-digest.md)

A small reading list with original sources, why each item belongs and what failed to load.

## Sample result

- **Read R1.** It is within the window and describes the exact feature under review.
- **R2 is a duplicate.** Keep the original R1 rather than repeat its summary.
- **R3 could not be read.** Relevance remains unconfirmed.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Make a reading brief on project handoff notes for the 24h ending 2026-11-20 09:00 SGT. Include up to three unique items. Give source ID, date and why it helps. Group duplicate original URLs. List unavailable sources separately and do not infer their content.
R1 | 2026-11-20 08:00 SGT | original=handoff-guide | text: a project handoff template adds a last verified result field
R2 | 2026-11-20 08:30 SGT | original=handoff-guide | repost of R1
R3 | source could not be opened | title: Working with project agents
R4 | 2026-11-20 07:00 SGT | text: updates to a photo editor filter
```

## With a connected tool

Start with sources you actually follow. Restrict the topic and time window first, then choose a delivery cadence. Flag a source with no new entries differently from a failed read.

## How to check it

Only R1 enters the shortlist. R2 is represented once and R3 appears in the source status. If no item qualifies, there is no filler.

## Decision boundary

The digest is for reading. Keep posting and subscribing as deliberate actions.

## How the cases fit together

Reddit, YouTube and multi-source tech digests share a process for selecting sources, discarding duplicates and delivering a shortlist. A published digest adds a testable extra detail: the reader can see when a source yielded nothing.

- Switch the reader’s question to a project or course topic without changing the shortlist format.
- Prefer the original release or paper over copies when several feeds repeat it.

## Sources

- **Author's published output.** The project includes an output from an actual run, with the empty source visible and old links deduplicated by its design. [A published digest with source health](https://github.com/ripplek/universal-feeds#see-it-in-action)
- **Community recipe.** The recipe takes selected communities and returns a read-only shortlist. [Daily Reddit digest](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/daily-reddit-digest.md)
- **Community recipe.** The recipe starts with selected channels and summarizes newly posted videos. [Daily YouTube digest](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/daily-youtube-digest.md)
- **Community recipe.** The recipe combines feeds and releases with deduplication and ranking. [Multi-source tech updates](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/multi-source-tech-news-digest.md)
- **Author account.** The author describes using a shared chat setup for household routines and a digest with source checks. [The Sebastian family assistant](https://ataary.com/meet-sebastian-how-i-built-a-self-learning-ai-assistant-on-openclaw/)

## Building blocks

[Scheduled delivery](../usecases/scheduled-task.md) · [Capture inbox](../usecases/capture-inbox.md) · [Platform routes](../BUILDER.md)
