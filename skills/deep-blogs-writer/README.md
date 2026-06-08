# Deep Blog Writer

Deep Blog Writer 是一个面向 AI Agent 的深度技术博客写作 skill。它把 Agent 调整成资深硬件工程师、技术研究员和长文作者的工作模式，用来生成技术正确、工程味足、结构清晰、对读者真正有启发的中文或英文长篇博客。

这个 skill 特别适合芯片、RTL、FPGA、ASIC、验证、计算机体系结构、网络芯片、数据中心基础设施、Linux、EDA、AI 基础设施和半导体技术等主题。它强调技术事实、设计取舍、实现细节、验证风险和调试经验，而不是市场叙事或投资观点。

## 安装

### 手动安装

1. 复制整个 `skills/deep-blogs-writer` 目录。
2. 放入你的 Agent 技能目录中。
3. 确认目录中包含 `SKILL.md`。
4. 在 Agent 中用自然语言调用。

```text
使用 deep-blogs-writer，写一篇关于 PCIe BAR 空间和 DMA 设计的深度博客。
```

### 从仓库导入

如果你的 Agent 支持从本地路径或 GitHub 导入技能，请选择这个具体目录：

```text
skills/deep-blogs-writer
```

## 核心能力

- 自动判断目标读者：专业工程读者或通用技术爱好者。
- 自动识别文章类型：教程、深度解析、架构分析、案例研究、技术行业分析、新闻分析或观点文。
- 写作前先做规划：确认读者、文章类型、关键概念、读者问题、详细大纲和逻辑流。
- 用 TL;DR 帮读者在 30 秒内理解核心结论。
- 避免泛泛开头，从真实工程问题、误解、调试故事或关键问题切入。
- 围绕读者真正困惑的问题组织文章，而不是围绕作者知识点堆叠内容。
- 强制包含非显然洞察，解释“为什么这样设计”“为什么替代方案被放弃”“隐藏 tradeoff 是什么”。
- 对硬件和系统主题优先讨论架构、机制、PPA、验证复杂度、时序影响、调试经验和量产风险。
- 在适合时生成 Mermaid 架构图、WaveDrom 时序图、对比表、时间线和封面图提示词。
- 对事实、假设、观点和推测做清晰区分，避免编造频率、吞吐、延迟、功耗、面积、制程、市场份额等数字。

## 适合什么时候用

当你希望 Agent 写出的文章不是“百科式介绍”，而是有工程判断、实践细节和深度解释的长文时，可以使用这个 skill。

示例：

```text
使用 deep-blogs-writer，写一篇面向 RTL 工程师的 AXI outstanding transaction 深度解析。
```

```text
用 deep-blogs-writer 帮我写一篇以太网 MAC、PCS、PMA 分层的技术博客，要有 Mermaid 图。
```

```text
使用 deep-blogs-writer，写一篇关于 CDC 问题为什么难 debug 的文章，面向有经验的芯片工程师。
```

```text
用 deep-blogs-writer 写一篇普通技术爱好者能看懂的 VPN 和代理区别教程。
```

## 输出结构

默认输出包括：

1. 标题
2. Executive Summary / TL;DR
3. Reader Questions
4. 正文
5. Key Takeaways
6. Further Reading
7. Suggested Cover Image Prompt

当主题需要时，还会加入：

- Mermaid 架构图、数据流图、状态机或流水线图。
- WaveDrom 时序图，用于解释 RTL、总线、握手、CDC、复位和 pipeline timing。
- 替代方案对比表。
- 技术演进时间线。

## 写作原则

Deep Blog Writer 的核心原则是：

- 技术准确性优先于表达流畅。
- 工程实践优先于行业评论。
- 设计取舍优先于概念罗列。
- 读者理解优先于文章长度。
- 工程价值优先于流量表达。
- 技术中立，不给投资建议，不做买卖评级，不推导证券结论。

对于技术资料，优先使用官方规格、标准文档、白皮书、技术手册、论文和会议资料。信息不确定时，应明确标注不确定性。

## 项目结构

```text
deep-blogs-writer/
├── README.md    # 面向人类的说明文档
└── SKILL.md     # 面向 AI Agent 的技能指令
```

## 兼容性

该 skill 使用通用的 `SKILL.md` 结构，适合支持 Agent Skills 的工具读取，也可以作为 Codex、Claude、Gemini、Antigravity 等 Agent 的本地上下文技能使用。
