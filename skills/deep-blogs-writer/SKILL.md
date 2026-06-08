---
name: deep-blogs-writer
description: Use when writing, editing, outlining, or polishing long-form Chinese blog posts with shared rules plus type-specific rules. Supports module algorithm/function analysis with RTL implementation, chip/FPGA/AI/network technology research, finance/investment/market analysis, and future blog categories.
---

# Deep Blogs Writer

## Workflow

1. Identify the blog type from the user request, topic, title, or existing file.
2. Always read `references/common.md`.
3. Read `references/style.md` when drafting, rewriting, or polishing prose.
4. Read `references/structure.md` when creating a new post, outline, or major restructure.
5. Read only the matching file under `references/types/`.
6. Read `references/fact_checking.md` and verify current sources when the topic involves current facts, policies, prices, laws, companies, market conditions, product specs, technical standards, or other time-sensitive claims.
7. Use `assets/post_template.md` as the starting skeleton when creating a new Jekyll post.
8. Produce the requested outline, draft, edit, rewrite, or review.

## Blog Type Routing

- **Module algorithm/function analysis and RTL implementation**: read `references/types/module_algorithm_rtl.md`.
  Use for posts focused on a specific module's algorithm, function, architecture, interface, timing behavior, RTL design, implementation details, verification points, or design tradeoffs.
- **Chip, FPGA, AI, network, and technical research**: read `references/types/technology_research.md`.
  Use for introductory or deep research posts about chips, FPGA, AI, networking, computer systems, protocols, architectures, engineering tools, and related technologies.
- **Finance, investment, and market analysis**: read `references/types/finance_investment_market.md`.
  Use for introductory or deep research posts about finance, investing, markets, macro, policy impact on markets, companies, assets, brokers, crypto markets, and market structure.

If the type is unclear, infer the closest type and briefly state the assumption.

## Extension Pattern

To add a new blog category:

1. Add a new Markdown file under `references/types/`.
2. Add one routing bullet above with the category name and when to use it.
3. Keep rules specific to that category in its own file.
