# Chip, FPGA, Algorithm, AI, Network, Hardware Design, And Technology Research

Use this type for technical analysis and research posts when the prompt does not explicitly ask for RTL implementation. This includes chips, FPGA, algorithms, AI, network technologies, chip internal interconnect buses, hardware design, protocols, datacenter systems, computer architecture, and engineering tools.

The article should be systematic technical research, not an encyclopedia entry. Do not write as a list of terms followed by shallow definitions.

## Core Writing Principle

Write from simple to deep:

1. Build intuition.
2. Explain the structure.
3. Analyze the key mechanisms.
4. Discuss engineering constraints.
5. Clarify boundaries, misconceptions, and future directions.

Every major section should be driven by a real question, not by a generic label.

Prefer headings such as:

```text
为什么 FPGA 需要 LUT 而不是普通门电路
为什么片上互连往往比逻辑资源更影响性能
为什么 AI 芯片不能只看 TOPS
为什么网络带宽提高后延迟问题仍然存在
```

Avoid headings that only list nouns:

```text
架构
特点
应用
优势
```

## Default Article Structure

Use this high-level structure unless the user requests a different organization:

1. Why this technology matters.
2. Historical context and evolution.
3. Minimal background knowledge.
4. Core problem and intuition model.
5. Architecture or system structure.
6. Key mechanisms in depth.
7. Engineering implementation and real-world constraints.
8. Typical application scenarios.
9. Common misconceptions and boundaries.
10. Future evolution and further reading path.
11. References.

Adjust the structure according to the topic. Keep the progression from simple to deep.

## Opening

Do not start with a Wikipedia-style definition.

The opening should answer:

- What problem does this technology solve?
- Why is this problem important?
- What changed because this technology exists?
- Why should the reader care now?

After the motivation is clear, introduce the formal definition.

## Historical Context And Evolution

Research and explain the history of the technology, product, protocol, or field discussed by the article.

Use historical context to answer:

- What problem or limitation originally caused this technology to appear?
- What earlier technologies, products, protocols, or design methods did it replace or extend?
- What were the major milestones, standard versions, product generations, or research breakthroughs?
- Which technical, economic, or ecosystem constraints shaped its evolution?
- Why did the current architecture or dominant design become the mainstream path?

Examples:

- For Ethernet, explain the evolution from shared-medium Ethernet to switched Ethernet, higher speeds, full duplex, optical links, datacenter Ethernet, and modern congestion/lossless variants when relevant.
- For DFT, explain why testability became important as chip complexity increased, and how scan chains, BIST, ATPG, boundary scan, and compression evolved.

Do not turn the history section into a loose chronology. Connect each historical step to the technical problem it solved and the new tradeoff it introduced.

## Depth Layers

Build the article in three layers:

- **Intuition layer**: what it roughly is and what problem it solves.
- **Structure layer**: what components it contains and how data, signals, computation, or control moves through it.
- **Mechanism layer**: why the key mechanisms are designed this way, what constraints they face, and what tradeoffs they create.

Do not jump into terminology before the reader has a mental model.

## Terminology Discipline

Technical research posts often involve many terms. Introduce terms in dependency order.

- Do not explain a new term by relying on another unexplained term.
- When a term first appears, give a short explanation in context.
- Prefer explaining terms through the problem they solve and the structure they belong to.
- If many terms are unavoidable, include a compact terminology table after the intuitive overview, not at the very beginning.
- Do not let the article become a glossary. A terminology table should support the main explanation, not replace it.
- When using English abbreviations, expand them on first use when useful, then use the abbreviation consistently.

## Visual Requirements

The article should be rich in useful visuals.

Use diagrams where they help explain:

- Concepts and intuition.
- System architecture.
- Data flow or signal flow.
- Hardware/software/protocol layering.
- Comparison between technologies.
- Technical evolution timelines.
- Bottlenecks in performance, power, cost, bandwidth, latency, thermal design, or scaling.

Except for flowcharts, finite-state-machine transition diagrams, and timing diagrams, generate diagrams as bitmap images with `image2` or `banama/banana` when available. Do not use SVG.

If image generation is unavailable, put the image prompt at the intended image location using the fallback format defined in `references/common.md`.

## Engineering Constraints

Include an engineering constraints section when relevant. This section is a key difference between deep research and shallow explanation.

For chip and semiconductor topics, discuss relevant constraints such as:

- PPA: performance, power, and area.
- Process node, packaging, yield, and cost.
- Memory wall, interconnect bottlenecks, thermal limits, and power delivery.
- EDA, verification, tape-out, bring-up, and mass-production risk.

For FPGA topics, discuss relevant constraints such as:

- LUT, FF, BRAM, URAM, DSP, routing, clocking, and I/O resources.
- Timing closure.
- Resource utilization.
- Board-level and toolchain constraints.
- Latency, throughput, and reconfiguration tradeoffs.

For AI topics, discuss relevant constraints such as:

- Compute, memory capacity, memory bandwidth, and interconnect bandwidth.
- Training versus inference.
- Batch size, latency, throughput, utilization, and serving cost.
- Model architecture and hardware mapping.
- Datacenter power, cooling, networking, and supply-chain constraints.

For networking topics, discuss relevant constraints such as:

- Bandwidth, latency, jitter, packet loss, congestion, and tail latency.
- PHY, MAC, switching, routing, transport, and application layers.
- Buffers, queues, flow control, congestion control, and packet scheduling.
- Protocol overhead.
- Observability, troubleshooting, and failure isolation.

## Common Misconceptions And Boundaries

Include a section that corrects oversimplified views when useful.

Examples:

- "FPGA is always faster than CPU" is only true for suitable parallel or streaming workloads.
- "AI chips are just about TOPS" ignores memory bandwidth, utilization, software stack, and deployment constraints.
- "Higher bandwidth always means faster systems" ignores latency, congestion, packet size, and software overhead.
- "Advanced process nodes are always cheaper" ignores mask cost, yield, design cost, and packaging.

Use this section to clarify when a claim is true, when it is false, and what assumptions it depends on.

## Application Scenarios

When discussing applications, connect each application to the technical mechanism that makes it suitable.

Avoid vague lists such as:

```text
广泛应用于通信、AI、工业、汽车、云计算等领域。
```

Prefer concrete reasoning:

```text
FPGA 适合低延迟数据流处理，不是因为它“通用”，而是因为它可以把协议解析、缓存调度和计算流水线固化成并行硬件路径。
```

## Future Evolution And Reading Path

Near the end, give the reader a path forward:

- If the reader only wants an entry-level understanding, identify the concepts they should remember.
- If the reader wants engineering depth, identify the mechanisms, documents, or tools to study next.
- If the reader wants research or industry judgment, identify the technical and market variables worth tracking.

This section should connect the article to possible follow-up posts.

## Source Discipline

For technical facts, prefer sources in this order:

1. Standards organizations and official specifications.
2. Official documentation and product briefs.
3. Academic papers, white papers, and conference material.
4. Vendor technical blogs and engineering presentations.
5. Reputable media or analyst reports.

Verify technical parameters such as process node, bandwidth, power, latency, version number, release date, protocol capability, and performance claims.
