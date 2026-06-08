# Verdvana Deep Blog Writer

这是一个用于 Codex / Agent Skills 的深度博客写作 skill，面向 Verdvana 风格的中文长文写作、改写、润色和结构设计。

它适合生成或维护以下三类文章：

1. 模块的算法或功能解析以及 RTL 实现。
2. 芯片、FPGA、AI、网络等技术的入门和深入研究。
3. 金融、投资、股票、市场分析等基础知识和深入研究。

这个 skill 的设计目标不是写百科词条，也不是生成松散的 AI 风格文章，而是帮助文章具备清晰结构、严谨事实、图文说明、可读表达和可持续扩展的写作规则。

## 使用方式

在支持 Agent Skills 的环境中，把整个目录作为一个 skill 使用：

```text
skills/deep-blogs-writer
```

调用时可以直接说：

```text
使用 deep-blogs-writer，帮我写一篇关于以太网芯片设计入门的文章。
```

也可以指定类型：

```text
使用 deep-blogs-writer，按第二类技术研究文章的规则，帮我写一篇 DFT 入门与深入研究。
```

如果文章涉及 RTL 或 testbench 编写，第一类规则会要求调用 `rtl-coding` skill。

## 目录结构

```text
deep-blogs-writer/
├── README.md
├── SKILL.md
├── assets/
│   └── post_template.md
└── references/
    ├── common.md
    ├── fact_checking.md
    ├── structure.md
    ├── style.md
    └── types/
        ├── finance_investment_market.md
        ├── module_algorithm_rtl.md
        └── technology_research.md
```

## 文件说明

### `SKILL.md`

Skill 的主入口和路由文件。

Codex 会先读取这里，根据用户请求判断文章类型，再决定读取哪些规则文件。

### `references/common.md`

所有文章都必须遵守的公共规则，包括：

- 文件命名：`YYYY-MM-DD-文章名字.md`
- Jekyll front matter 格式
- 最多 3 个 tag
- 最多三级标题
- 一级标题前使用 `----` 分隔
- 文章结尾使用 `----`
- 图片、表格、参考资料规则
- 排版克制和最终自检

### `references/style.md`

通用文风规则。

用于控制文章不要变成空泛的 AI 腔、百科式堆砌或过度装饰的格式化文本。

### `references/structure.md`

通用结构规则。

用于新建文章、大纲设计或大幅重构。具体文章类型的结构优先级高于这里。

### `references/fact_checking.md`

事实核查规则。

当文章涉及政策、市场、公司、价格、技术标准、产品规格、近期事件等可能变化的信息时，需要使用这里的规则进行核查，并在文章最后的参考资料章列出来源。

### `references/types/module_algorithm_rtl.md`

第一类文章规则：模块的算法或功能解析以及 RTL 实现。

适合写：

- 模块功能解析
- 算法到硬件实现
- 架构与接口设计
- 子模块划分
- SystemVerilog RTL
- 顶层集成
- testbench、验证和性能测试

写 RTL 或 testbench 时需要调用 `rtl-coding` skill。

### `references/types/technology_research.md`

第二类文章规则：芯片、FPGA、AI、网络等技术的入门和深入研究。

适合写：

- 以太网、PCIe、CXL 等协议或系统技术
- DFT、CDC、低功耗、先进封装等芯片技术
- FPGA 架构、工具链和应用
- AI 模型、AI 芯片、AI 基础设施
- 网络、数据中心、计算机系统

这类文章要求由简入深，研究历史脉络，避免百科式名词罗列，并用图文说明技术结构、机制、工程约束和演进方向。

### `references/types/finance_investment_market.md`

第三类文章规则：金融、投资、股票、市场分析等基础知识和深入研究。

适合写：

- 金融和投资基础知识
- 股票、基金、债券、加密资产
- 市场结构、券商渠道、交易机制
- 宏观、政策、监管和市场影响
- 公司、行业、资产分析

这类文章面向非金融行业从业者，要求从基础和生活场景讲起，保持实时性，区分事实、解释、情景和观点，并进行多维度分析。

如果第三类文章涉及 AI 基建、半导体、光通信、CPO、数据中心电力、neocloud、供应链瓶颈或 ticker thesis，可以在必要时调用 `serenity-supply-chain-thesis` skill 辅助分析。

### `assets/post_template.md`

Jekyll 文章模板。

新建文章时可以以它为起点。

## 图片规则

文章应在合适位置使用图片辅助说明。

除流程图、状态机状态转移图、时序图之外，其他图应优先使用图片生成引擎生成位图，例如 `image2` 或 `banana`。不要使用 SVG。

如果当前环境不能生成图片，应在图片位置写出图片生成 prompt，方便后续手动生成。

## 参考资料规则

所有参考资料统一放在最后一章。

优先使用：

1. 官方文档、标准、法律法规、监管文件。
2. 公司公告、财报、产品文档。
3. 标准组织、交易所、央行、统计机构等官方数据。
4. 论文、白皮书、会议资料。
5. 高质量媒体和分析报告。

不要编造来源、链接、数据、日期、政策表述或市场价格。

## 扩展新文章类型

如果后续需要增加新的文章类型：

1. 在 `references/types/` 下新增一个 Markdown 文件。
2. 在 `SKILL.md` 的 `Blog Type Routing` 中增加一条路由。
3. 把新类型的专属规则放进对应文件。
4. 公共格式规则仍放在 `references/common.md`。

这样可以避免 `SKILL.md` 越来越臃肿，也方便不同类型文章独立演进。
