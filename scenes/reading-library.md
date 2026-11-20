# Reading library · Find the thing I saved

[Home](../README.md) · [简体中文](../zh-CN/scenes/reading-library.md)

A saved link and its context, easy to recover later with a natural-language question.

## Sample result

- **L1 · A project diary template.** It mentions a last verified result field.
- **L2 points to the same source.** Add the new note to L1 instead of storing a second article.

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Organize these reading records by the original ID. Preserve my notes and the source, recording a duplicate pointer when useful. Then answer "Which saved item has a template for recording a verified result?" Cite the saved record. Mark unread items.
L1 | source U01 | project diary template | my note: it asks for the last verified result
L2 | source U01 | saved again from chat | my note: useful for handing off projects
L3 | source U02 | title only | reading status unread
```

## With a connected tool

Use one capture path, such as a chat or a notes folder. Keep the link or document ID and your own reason for saving it. Confirm you can retrieve the original in another session.

## How to check it

The answer cites L1 and preserves your notes from L2. L3 remains unread, rather than supplying details inferred from its title.

## Decision boundary

Search only the sources you choose. Keep original material visible and let a person decide what to retain.

## How the cases fit together

The searchable knowledge-base recipe starts with URLs. The second-brain recipe starts with a short message. The core is the same retrieval loop: save a source with context, then find it again.

- Store article links, a transcript excerpt or a study note under the same small format.
- Reuse saved evidence in a later research note without copying the full source again.

## Sources

- **Community recipe.** The recipe collects links and searches across saved material with references. [Search your saved sources](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/knowledge-base-rag.md)
- **Community recipe.** The system trades upfront organization for fast capture and later search. [Capture to retrieve later](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/second-brain.md)

## Building blocks

[Capture inbox](../usecases/capture-inbox.md) · [Repeatable workflow](../usecases/repeatable-workflow.md) · [Platform routes](../BUILDER.md)
