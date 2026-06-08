# Module Algorithm, Function Analysis, And RTL Implementation

Use this type for posts about a specific module's algorithm, function, architecture, interface, timing behavior, RTL implementation, verification, and design tradeoffs.

## Default Article Structure

Use this high-level structure unless the user requests a different organization:

1. Module overview.
2. Top-level architecture and interface.
3. Submodule A.
4. Submodule B.
5. Additional submodules as needed.
6. Top-level integration and RTL.
7. Simulation, verification, and performance testing.
8. Design tradeoffs and extension directions.
9. References.

Adjust the number of submodule chapters according to the actual design.

## Chapter 1: Module Overview

The first chapter should briefly introduce:

- The module's function.
- Typical application scenarios.
- Where the module sits in a larger system.
- Relevant official documentation links, if available.
- Design goals and constraints.

When relevant, include design goals and constraints such as:

- Target throughput.
- Target latency.
- Assumed clock frequency.
- Input/output protocol.
- Backpressure support.
- Parameterization requirements.
- Area, power, or FPGA resource constraints.
- CDC, reset, low-power, or clocking assumptions.

## Chapter 2: Top-Level Architecture And Interface

The second chapter should explain the overall module architecture and its input/output signals.

Include an architecture diagram that shows:

- Top-level input and output signals.
- Major internal blocks.
- Main datapath and control path.
- Configuration, status, error, debug, clock, and reset paths when relevant.

To save image area, signals in the same group may be merged into a wide bus line. The diagram should still make the signal grouping clear.

Also include:

- A signal table for top-level input/output signals.
- A division of the architecture into submodules or logical blocks.
- A short explanation of why this partitioning helps the later discussion.
- A clear distinction between datapath, control path, configuration path, status/error path, and clock/reset path when relevant.

Recommended signal table columns:

```text
信号名 | 方向 | 位宽 | 时钟域 | 复位值 | 分类 | 源模块 | 目的模块 | 描述
```

Not every column is required for every article. Keep the fields that are useful and omit fields that would become empty noise.

Recommended signal categories:

```text
data / valid-ready / control / config / status / error / debug / clock-reset
```

## Submodule Chapters

After the top-level chapter, describe each submodule according to the architecture partition.

For each submodule, include the following parts when applicable:

1. Responsibility boundary.
2. Submodule architecture diagram.
3. Submodule input/output signal table.
4. Function, algorithm, or protocol behavior.
5. Implementation notes.
6. SystemVerilog RTL code.

### Responsibility Boundary

Before detailed explanation, state:

- What this submodule is responsible for.
- What this submodule is not responsible for.
- Assumptions made about upstream inputs.
- Guarantees provided to downstream modules.

### Submodule Architecture And Signals

The submodule architecture diagram should show internal datapath, control logic, key registers, FIFOs, memories, counters, FSMs, and interfaces when relevant.

Use a signal table similar to the top-level signal table:

```text
信号名 | 方向 | 位宽 | 时钟域 | 复位值 | 分类 | 源模块 | 目的模块 | 描述
```

### Function Or Algorithm Explanation

Use the most suitable format for the logic being explained:

- Use Mermaid only for flowcharts and finite-state-machine transition diagrams.
- Use WaveDrom for timing diagrams.
- Use LaTeX for formulas and algorithmic equations.
- Use Markdown tables for simple comparisons and state descriptions.
- Use HTML tables only when complex formatting is needed.
- For diagrams other than flowcharts, FSM transition diagrams, and timing diagrams, use generated bitmap images with `image2` or `banana` when available. Do not use SVG.

The explanation should cover normal behavior, boundary cases, stalls/backpressure, reset behavior, and error handling when relevant.

### RTL Implementation Notes

Before showing code, explain the implementation choices:

- Parameters and localparams.
- Register and combinational logic partitioning.
- FSM states and transitions.
- Pipeline stage partitioning.
- Ready/valid or request/acknowledge handling.
- Memory, FIFO, counter, and buffer usage.
- Boundary conditions.
- Synthesis considerations.

### RTL Code

- When writing or modifying RTL code, invoke the `rtl-coding` skill.
- RTL code must be written in SystemVerilog.
- Prefer synthesizable RTL over pseudocode.
- Keep module interfaces explicit and consistent with the signal tables.
- Use clear parameter names and stable reset behavior.
- Avoid simulation-only constructs in synthesizable modules unless explicitly marked.

## Top-Level Integration And RTL

After all submodules are introduced, include an integration chapter.

This chapter should:

- Reuse the top-level architecture to show how submodules connect.
- Explain data movement, control coordination, and backpressure across submodules.
- Provide the top-level SystemVerilog RTL code.
- Keep top-level ports consistent with the top-level signal table.

## Simulation, Verification, And Performance Testing

Include a verification chapter after integration.

This chapter should include:

- Invocation of the `rtl-coding` skill when writing or modifying SystemVerilog testbench code.
- A SystemVerilog testbench or verification scaffold.
- A table listing each test case and its purpose.
- Directed tests.
- Random tests when useful.
- Corner-case tests.
- Backpressure or stall tests.
- Reset tests.
- Parameter sweep tests when the module is parameterized.
- Assertions or SVA checks where useful.
- Coverage goals when useful.
- Performance tests for throughput, latency, stalls, or resource-sensitive behavior.

For algorithm modules, verify RTL output against a software golden model when possible:

```text
input vectors -> software golden model -> RTL output -> automatic comparison
```

For protocol or control modules, emphasize:

```text
protocol legality assertions + scenario coverage + key waveform checks
```

## Design Tradeoffs And Extension Directions

Near the end of the article, include a chapter about design reasoning when useful.

Discuss:

- Why the module is partitioned this way.
- Why this FSM, pipeline, buffer, or memory structure was chosen.
- Area, performance, latency, and power tradeoffs.
- FPGA resource tradeoffs when relevant.
- How to scale to higher throughput or lower latency.
- How to add more configuration, protocol support, or corner-case handling.
