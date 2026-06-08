# Finance, Investment, And Market Analysis

Use this type for posts about finance, investing, stocks, funds, crypto assets, macro, policy impact, market structure, brokers, exchanges, companies, industries, and asset analysis.

The target reader is a professional from a non-financial industry. Start from basics, connect concepts to common life scenarios, and then expand into multi-dimensional analysis.

Do not write like a trading recommendation, a shallow news summary, or a dense sell-side research report.

When the article involves AI infrastructure, semiconductors, photonics, CPO, datacenter power, neoclouds, supply-chain bottlenecks, or ticker thesis generation, invoke the `serenity-supply-chain-thesis` skill when useful.

## Core Writing Principle

The article should help the reader understand:

- What the concept, event, policy, company, asset, or market phenomenon is.
- Why it matters.
- How it works.
- Who is affected.
- What has changed recently.
- What risks, assumptions, and uncertainties remain.

Use plain Chinese, but keep analytical rigor.

## Default Article Structure

Use this high-level structure unless the user requests a different organization:

1. Why this topic matters.
2. Understand it through a common life scenario.
3. Basic concepts and key mechanisms.
4. What happened recently, with an explicit as-of date.
5. Multi-dimensional impact analysis.
6. Common misconceptions and risk boundaries.
7. Variables to watch next.
8. References.

Adjust the structure according to the topic. Some topics may need more conceptual explanation; others may need more policy, market, or company analysis.

## Reader Model

Assume the reader is smart but not trained in finance.

Do not assume the reader already understands terms such as:

- Valuation, liquidity, interest rate, duration, leverage, margin, market maker, ETF, options, futures, basis, spread, volatility, drawdown, beta, alpha, risk premium, discount rate, exchange rate, offshore market, onshore market, custody, clearing, settlement, and counterparty risk.

Explain necessary terms before relying on them.

## Life-Scenario Anchoring

When introducing abstract financial concepts, connect them to common life scenarios.

Examples:

- Liquidity: whether a house, car, or second-hand product can be sold quickly without a large discount.
- Interest rate: the cost of borrowing and the opportunity cost of holding money.
- Leverage: using borrowed money to enlarge both gains and losses.
- Duration: how sensitive a future cash-flow asset is to changes in interest rates.
- Valuation: how much people are willing to pay today for uncertain future cash flows.

Use these scenarios to build intuition, then move back to the financial mechanism.

## Concept, Mechanism, Event, And Impact

Separate four layers in the explanation:

- **Concept**: what the term means.
- **Mechanism**: how it works.
- **Event**: what happened, when it happened, and what changed.
- **Impact**: who is affected and how.

Do not mix these layers into one vague explanation.

## Real-Time And Date Discipline

Finance, investment, policy, and market articles are time-sensitive. Verify current information before writing when the topic involves recent or changeable facts.

Check whether:

- A policy, regulation, or official interpretation has a newer version.
- A regulator, exchange, broker, or company has issued a later clarification.
- Company announcements, earnings reports, guidance, or filings have been updated.
- Market prices, interest rates, exchange rates, index levels, fund flows, or valuation data are current enough for the claim being made.
- A news event has later corrections, denials, or follow-up developments.

Use concrete dates. Avoid vague terms such as "recently", "currently", or "now" unless the sentence also gives the specific date or as-of date.

When useful, state:

```text
截至 YYYY-MM-DD，...
```

## Multi-Dimensional Analysis

Unlike technical deep dives, this category often benefits more from multi-dimensional analysis than from a single deep mechanism.

Analyze the topic from relevant dimensions such as:

- Policy and regulation.
- Market liquidity and sentiment.
- Institutions and intermediaries.
- Retail investors.
- Companies and industries.
- Asset pricing and valuation.
- Interest rates, exchange rates, inflation, and macro conditions.
- Time horizon: short-term reaction versus long-term structural impact.
- Global comparison.
- Operational, compliance, liquidity, valuation, credit, currency, and tail risks.

Avoid using one single cause to explain everything. Financial markets usually reflect multiple variables interacting at the same time.

## Facts, Interpretation, Scenario, And Opinion

Keep a clear boundary between:

- **Facts**: confirmed events, rules, data, documents, prices, or announcements.
- **Interpretation**: analysis based on confirmed facts.
- **Scenario**: possible future paths that are not confirmed.
- **Opinion**: the author's judgment.

The article does not need to label every sentence, but the writing must not blur these categories.

Use cautious language for inference:

```text
可能 / 倾向于 / 更像是 / 仍需观察 / 在这个假设下 / 如果后续...
```

Do not turn correlation into causation without evidence.

## Risk And Advice Boundary

Do not present the article as personalized investment advice.

Prefer framing such as:

```text
这不是一个“该不该买”的问题，而是一个“这个变量会怎样改变风险收益结构”的问题。
```

Discuss risks naturally in the analysis instead of adding only a mechanical disclaimer at the end.

When relevant, highlight:

- Policy risk.
- Liquidity risk.
- Valuation risk.
- Currency risk.
- Credit risk.
- Leverage and forced liquidation risk.
- Information asymmetry.
- Operational and compliance risk.
- Tail risk.

## Visual Requirements

Use generated bitmap images with `image2` or `banana` when available. Do not use SVG.

Useful visuals include:

- Policy or event timeline.
- Capital-flow diagram.
- Relationship diagram among regulators, exchanges, brokers, companies, funds, and investors.
- Layering diagram such as primary/secondary market, onshore/offshore market, or exchange/OTC market.
- Comparison table for channels, assets, rules, fees, risks, and constraints.
- Scenario matrix: optimistic, neutral, pessimistic.
- Risk map across policy, liquidity, valuation, currency, credit, and operational dimensions.

If image generation is unavailable, put the image prompt at the intended image location using the fallback format defined in `references/common.md`.

## Common Misconceptions

Include a misconception section when useful.

Examples:

- "Price going up means risk is lower."
- "High dividend yield always means undervaluation."
- "Policy tightening affects everyone in the same way."
- "A company being good does not automatically mean the stock is cheap."
- "A low valuation multiple is not always a bargain."
- "High liquidity in normal times does not guarantee liquidity in stress."

Explain when a statement is true, when it is false, and what assumptions it depends on.

## What To Watch Next

Near the end, list the variables readers should keep watching.

Examples:

- Next policy document or regulatory clarification.
- Earnings report, guidance, or filing.
- Interest rates, exchange rates, inflation, or liquidity indicators.
- Trading volume, spreads, fund flows, short interest, or volatility.
- Company-specific execution milestones.
- Industry supply, demand, inventory, pricing, and capacity changes.

This section should help readers follow future developments without pretending the future is certain.

## Source Discipline

Prefer sources in this order:

1. Official laws, regulations, policy documents, regulator notices, and exchange rules.
2. Company filings, announcements, earnings releases, and investor presentations.
3. Central banks, statistical agencies, exchanges, and official datasets.
4. Fund, broker, rating agency, or index-provider documents.
5. Reputable financial media and analyst reports.

Do not invent sources, data, policy language, quotes, or market prices.
