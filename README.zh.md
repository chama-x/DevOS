![DevOS: Predictability Over Perfection](assets/devos-hero.svg?v=1786143843)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — 用四个文件，让任何 IDE 智能体拥有你项目的规则、当前任务和历史记录。**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```

![DevOS 4-File Context Architecture](assets/devos-architecture.svg?v=1786143843)

## 快速开始

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# 重启你的 IDE 智能体 —— 它现在每次对话都会读取项目上下文。
```

## 为什么选择 DevOS？

IDE 智能体每次对话都从零开始。DevOS 赋予它们记忆——你的规则、你的任务、你的历史——这样它们就不再瞎猜，而是直接开始工作。

## DevOS 与 单文件 Prompt (.cursorrules) 对比

| 特性 | 单个 `.cursorrules` / 提示词列表 | DevOS |
|---|---|---|
| **架构设计** | 单个庞大文件（导致上下文膨胀） | 4 个模块化文件 + 动态技能路由 |
| **会话记忆** | 每次新对话都重置 | 通过 `worklog.md` 跨会话持久化 |
| **Token 预算** | 无条件加载 5000+ Token | 仅基础 ~700 Token；技能按需加载 |
| **范围约束** | 软性建议（经常被智能体忽略） | 通过 `GROUNDING.md` 强制约束 |
| **自主权控制** | 边界模糊 | 在 `IDENTITY.md` 中显式声明自主权 |

## 功能特性

| 特性 | 作用 |
|---|---|
| **11 项技能** | 仅加载任务所需的推理循环 |
| **技能校准** | 自动将任务路由到正确的技能 |
| **演进治理** | 智能体提出新技能，由你来批准 |
| **上下文压缩** | 在历史记录无限膨胀前进行归档 |
| **语义字典** | 将你的简写映射为确定性行为 |

## 文档与社区

我们重视信任、可预测性和协作。
- [更新日志](CHANGELOG.md) - 查看发布历史。
- [贡献指南](CONTRIBUTING.md) - 我们会审查每一个 PR，请从 `good first issue` 开始。
- [行为准则](CODE_OF_CONDUCT.md) - 我们的社区标准。

## 项目结构

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← 为你的项目填写此文件
│   ├── GROUNDING.md         ← 智能体行为校准
│   └── SKILL_ROUTING.md     ← 技能决策树
├── current.md               ← 易失性任务状态
├── worklog.md               ← 仅追加的历史记录
└── skills/                  ← 11 个精选技能目录
```

## 许可证

MIT
