![DevOS: Predictability Over Perfection](assets/devos-hero.svg?v=1786143843)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — 4つのファイルで、IDEエージェントにプロジェクトのルール、現在のタスク、および履歴を与えます。**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```

![DevOS 4-File Context Architecture](assets/devos-architecture.svg?v=1786143843)

## クイックスタート

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# IDEエージェントを再起動します — これで毎回のチャットでプロジェクトのコンテキストを読み込みます。
```

## なぜDevOSなのか？

IDEエージェントは毎回のチャットをゼロから始めます。DevOSは彼らに記憶（あなたのルール、タスク、履歴）を与えることで、推測をやめ、構築を始めさせます。

## DevOS vs. 生のプロンプト

単一の `.cursorrules` やプロンプトパックは、チャットごとに数千トークンを消費します。DevOSはそれらを4つの構造化ファイルとオンデマンドルーティングに置き換えます。

| 機能 | 生のプロンプト (.cursorrules / CLAUDE.md) | DevOS |
|---|---|---|
| **消費トークン** | チャットごとに5,000+トークン | ~700トークンのみ読み込み |
| **セッション履歴** | 新規チャットでゼロにリセット | `worklog.md` から進捗を復元 |
| **スキル読み込み** | 全ルールを一律読み込み | オンデマンドで最大2〜3スキル |
| **スコープの規律** | 無視可能な曖昧な提案 | 応答前に制約を厳格チェック |
| **プロジェクト境界** | 未定義 | `IDENTITY.md` で明確に定義 |


## 機能

| 機能 | 役割 |
|---|---|
| **11のスキル** | タスクに必要な推論ループのみを読み込む |
| **スキルの調整** | タスクを自動的に適切なスキルにルーティングする |
| **ガバナンス** | エージェントが新しいスキルを提案し、あなたが承認する |
| **コンテキスト圧縮** | 肥大化する前に履歴をアーカイブする |
| **意味論的辞書** | あなたの略語を決定論的な行動にマッピングする |

## ドキュメントとコミュニティ

私たちは信頼、予測可能性、コラボレーションを重視します。
- [Changelog](CHANGELOG.md) - リリース履歴。
- [Contributing Guidelines](CONTRIBUTING.md) - すべてのPRをレビューします。`good first issue`から始めてください。
- [Code of Conduct](CODE_OF_CONDUCT.md) - コミュニティ標準。

## プロジェクト構造

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← プロジェクトに合わせて記入
│   ├── GROUNDING.md         ← エージェントの行動調整
│   └── SKILL_ROUTING.md     ← スキルの決定木
├── current.md               ← タスクの揮発性状態
├── worklog.md               ← 追記専用の履歴
└── skills/                  ← 11の厳選されたスキルディレクトリ
```

## ライセンス

MIT
