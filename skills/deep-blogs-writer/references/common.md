# Common Rules

These rules apply to every blog post, regardless of category.

## File Naming

- Blog post filenames must use this pattern: `YYYY-MM-DD-article-title.md`.
- The date part must use four-digit year, two-digit month, and two-digit day.
- The article title part must not contain spaces or unusual characters.
- Prefer readable Chinese or ASCII title text. Avoid punctuation that may be fragile in file paths.

## Front Matter

Every generated post must begin with this exact front matter structure:

```yaml
---
layout: post
title:  "文章名字"
date:   YYYY-MM-DD HH:MM:SS +0800
tags:
  - tag1
  - tag2
  - tag3
---
```

- Replace the placeholder values with actual content.
- Do not include angle brackets such as `<文章名字>` in generated files.
- Use at most 3 tags.
- The `title` value should match the article title, not the full filename.

## Section Structure

- Articles may use at most three heading levels.
- First-level sections use `## 1 一级标题`.
- Second-level sections use `### 1.1 二级标题`.
- Third-level sections use `#### 1.1.1 三级标题`.
- Keep numbering consistent and sequential.
- Before every first-level section, insert a horizontal separator `----` with one blank line before and after it.
- The article must also end with `----`.
- Do not use `#` headings inside the body, because the front matter title already defines the post title.

Example:

```markdown
Intro paragraph.

----

## 1 一级标题

### 1.1 二级标题

#### 1.1.1 三级标题

----
```

## Tables

- Use standard Markdown tables for simple tables.
- Use HTML tables when the table needs complex presentation, such as color grouping, merged cells, custom alignment, or richer formatting.
- Keep table content factual and easy to scan.

## Images

- Use images where they help explain structure, flow, architecture, comparison, chronology, or abstract concepts.
- Except for flowcharts, finite-state-machine transition diagrams, and timing diagrams, all diagrams should be generated as bitmap images with an image generation engine such as `image2` or `banama/banana` when available.
- If image generation is unavailable, place the image-generation prompt at the intended image location so the user can generate it manually later.
- Do not use SVG images.
- Avoid purely decorative images; images should clarify the article.
- For a post named `YYYY-MM-DD-文章名字.md`, store images in a sibling folder named `文章名字/`.
- Reference images with relative paths such as `![说明](文章名字/01-architecture.png)`.
- Use numbered image filenames such as `01-overview.png`, `02-flow.png`, and `03-comparison.png`.

Suggested fallback format when no image can be generated:

```markdown
![待生成图片：简短描述](PROMPT: 这里写清楚图片生成提示词)
```

## References

- Put all reference materials with links in the final numbered chapter.
- The final first-level section should usually be named `参考资料`.
- Each reference should include source name, title, and link. Include publication date or access date when it helps clarify timeliness.
- Prefer official documentation, primary sources, standards documents, laws, papers, exchange announcements, company announcements, and reputable media.
- Do not cite low-quality reposts when primary sources are available.
- Do not scatter raw reference links throughout the body unless the user specifically asks for inline citations.
- Do not invent sources, quotes, facts, dates, numbers, or claims.
- Keep factual claims rigorous, logically consistent, and credible.
- If a claim is uncertain, time-sensitive, or source-dependent, verify it before using it or clearly mark the uncertainty.

## Formatting Restraint

- Use lists for comparisons, steps, and dense facts.
- Prefer paragraphs for reasoning and explanation.
- Avoid excessive bold text, blockquotes, nested lists, and decorative formatting.
- Do not use emoji in formal posts unless the user explicitly asks.

## Quality Bar

- Do not fabricate content that conflicts with known facts or basic logic.
- Prefer precise, modest claims over dramatic but unsupported claims.
- Keep the writing clear enough for the intended reader without losing technical or analytical rigor.

## Final Check

Before finishing a post, check:

- Filename follows `YYYY-MM-DD-article-title.md`.
- Front matter is valid and has at most 3 tags.
- Headings use no more than 3 levels and numbering is consistent.
- Every first-level section is preceded by `----`.
- The article ends with `----`.
- References are in the final chapter.
- No unsupported factual claims remain.
- Image prompts or image links are present where helpful.
