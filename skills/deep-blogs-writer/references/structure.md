# Structure

Use this file when creating a new post, outline, or major restructure.

Type-specific structure rules in `references/types/` take priority. This file only provides shared structural habits.

## New Post Skeleton

When creating a new post:

1. Use the front matter format from `references/common.md`.
2. Start with a short opening that explains why the topic matters.
3. Use numbered sections with at most three heading levels.
4. Follow the selected type-specific structure.
5. Put references in the final numbered chapter.
6. End the article with `----`.

## Opening

The opening should not be a dictionary definition.

Prefer an opening that states:

- What problem, event, or question the article is addressing.
- Why the topic is worth understanding.
- What the article will help the reader see more clearly.

## Section Progression

Good posts usually move from:

```text
motivation -> context -> structure -> mechanism/analysis -> examples -> risks/boundaries -> next steps -> references
```

Do not force this exact order if the selected type file gives a better structure.

## Ending

End with a section that helps the reader retain the useful frame:

- For technical posts: summarize the mechanism, constraints, and next learning path.
- For RTL posts: summarize design tradeoffs, verification coverage, and extension directions.
- For finance/market posts: summarize what changed, what matters, and what variables to watch.

