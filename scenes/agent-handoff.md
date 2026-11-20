# Agent handoff · Pick up the project in a different session

[Home](../README.md) · [简体中文](../zh-CN/scenes/agent-handoff.md)

A portable handoff with the current artifact, checked result, limits and next action.

## Sample result

- **Artifact.** draft-v2.md [H1].
- **Checked.** Preview opened and all three links worked locally [H2].
- **Next.** Ask for a release review. No release receipt [H3].

## Try it with material you have

Paste the full block below. The input is fictional.

```text
Write a handoff for the next session or tool. Include goal, artifact path, verified result and its limits, unresolved work, next step and permissions. Cite record IDs. Keep the next action reviewable and require fresh approval for outside writes.
H1 | goal: publish a library page | latest artifact draft-v2.md
H2 | local preview opened | 3 internal links checked
H3 | review pending | no remote publication receipt
```

## With a connected tool

Put the handoff beside the output in a folder you can access later. Start a fresh session using only this note and the referenced files. Check what the next tool can read and which actions need a fresh grant.

## How to check it

The next session can find draft-v2.md and knows exactly what ran. It can explain what still needs review. The original result is preserved if it has to stop.

## Decision boundary

Only pass material needed for the next job. A saved prompt or an earlier approval does not grant the next tool access automatically.

## How the cases fit together

One agent can produce a report and another can file it. You can also move the same routine to a different tool. Both depend on a visible handoff artifact and on stating what the next step may do.

- Carry a brief and source list from research into drafting.
- Transfer a project between tool sessions by sharing only the small set of documents and checked results.

## Sources

- **Community recipe.** The recipe describes role separation and shared memory as the interface between roles. [Shared context for a specialized agent team](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/multi-agent-team.md)
- **Collection summary.** The summary identifies a concrete handoff: a scheduled report sent by email and then placed in a dashboard. [Muse #386 - Send a report to another agent for archiving](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L2023-L2028) · [Original post](https://www.threads.com/@sonia.elyss/post/DfvpdVUFOSv)
- **Collection summary.** The collection reports moving an existing Claude prompt into Muse and scheduling the resulting routine. It does not publish operation receipts. [Muse #225 - Move an existing workflow between agents](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L2515-L2520) · [Original post](https://x.com/NewtonJonesIV/status/2098022398721143207)

## Building blocks

[Repeatable workflow](../usecases/repeatable-workflow.md) · [Capture inbox](../usecases/capture-inbox.md) · [Platform routes](../BUILDER.md)
