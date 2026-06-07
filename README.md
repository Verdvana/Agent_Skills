# Agent Skills

面向 Codex、Claude、Gemini、Antigravity 等 AI Agent 的中文技能目录。

本仓库采用类似 OpenDirectory 的组织方式：根目录负责介绍技能集合，每个技能放在 `skills/` 下的独立目录中。每个技能目录至少包含：

- `SKILL.md`：给 AI Agent 读取的技能说明、触发场景和执行流程。
- `README.md`：给人阅读的技能介绍、安装方式、使用示例和目录说明。

## 当前技能

| Skill | 简介 | 路径 |
| --- | --- | --- |
| AI 小康 | 模仿“小康”的中文口音和性格，带固定读音转换规则和低级炫耀感。 | [`skills/ai-xiaokang`](skills/ai-xiaokang) |

## 快速开始

### 方式一：手动安装

1. 打开目标技能目录，例如 `skills/ai-xiaokang`。
2. 将整个技能目录复制到你的 Agent 技能目录中。
3. 确保被安装的目录中包含 `SKILL.md`。
4. 在 Agent 中用自然语言触发该技能，例如：

```text
使用 ai-xiaokang，用小康口音回复我。
```

### 方式二：从仓库引用

如果你的 Agent 支持从 GitHub 或本地路径导入技能，可以直接选择某个技能目录，而不是导入整个仓库。

```text
skills/ai-xiaokang
```

## 仓库结构

```text
Agent_Skills/
├── README.md
├── LICENSE
└── skills/
    └── ai-xiaokang/
        ├── README.md
        └── SKILL.md
```

## 创建新技能

新增技能时，请使用小写字母、数字和连字符命名目录，例如：

```text
skills/my-new-skill/
├── README.md
└── SKILL.md
```

`SKILL.md` 应该保持精炼，重点写清楚：

- 什么时候应该使用这个技能。
- Agent 应该遵循什么流程。
- 是否需要读取额外的 `references/`、运行 `scripts/` 或使用 `assets/`。

`README.md` 面向人类读者，建议包含：

- 技能简介。
- 安装方式。
- 核心能力。
- 使用示例。
- 项目结构。

## 许可证

本仓库使用 Apache License 2.0。
