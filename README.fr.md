![DevOS: Predictability Over Perfection](assets/devos-hero.svg?v=1786143843)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — Donnez à tout agent IDE les règles, la tâche actuelle et l'historique de votre projet en quatre fichiers.**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```

![DevOS 4-File Context Architecture](assets/devos-architecture.svg?v=1786143843)

## Démarrage Rapide

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# Redémarrez votre agent IDE — il lit désormais le contexte de votre projet à chaque chat.
```

## Pourquoi DevOS ?

Les agents IDE repartent de zéro à chaque chat. DevOS leur donne une mémoire — vos règles, votre tâche, votre historique — pour qu'ils arrêtent de deviner et commencent à construire.

## DevOS vs. Prompts Ad-hoc (.cursorrules, Instructions Personnalisées)

Remplacez les packs de prompts dispersés, les fichiers uniques `.cursorrules` et les instructions ad-hoc par un moteur de contexte déterministe en 4 fichiers.

| Capacité | Prompts bruts (.cursorrules / CLAUDE.md) | Moteur DevOS |
|---|---|---|
| **Architecture** | Empreinte texte monolithique (gaspille le contexte) | 4 fichiers modulaires (~700 tokens) |
| **Mémoire de Session** | Amnésie : réinitialisation complète à chaque chat | Continue : restaure la progression via `worklog.md` |
| **Chargement** | Charge toutes les règles d'un coup (cause des hallucinations) | Calibré : routage dynamique de 2–3 compétences max |
| **Discipline d'Activité** | Suggestions floues (l'agent refactorise au hasard) | Application stricte via les contrôles `GROUNDING.md` |
| **Limites du Projet** | Implicites ou non déclarées | Autonomie explicite et règles d'or dans `IDENTITY.md` |

## Fonctionnalités

| Fonctionnalité | Ce qu'elle fait |
|---|---|
| **11 Compétences** | Charge uniquement la boucle de raisonnement requise |
| **Calibrage** | Route automatiquement les tâches vers la bonne compétence |
| **Gouvernance** | Les agents proposent des règles ; vous approuvez |
| **Compression** | Archive l'historique avant qu'il ne croisse indéfiniment |
| **Dictionnaire sémantique** | Transforme vos raccourcis en comportements déterministes |

## Documentation & Communauté

Nous privilégions la confiance, la prévisibilité et la collaboration.
- [Changelog](CHANGELOG.md) - Historique des versions.
- [Guide de Contribution](CONTRIBUTING.md) - Nous examinons chaque PR. Commencez par un `good first issue`.
- [Code de Conduite](CODE_OF_CONDUCT.md) - Nos standards.

## Structure du projet

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← Remplissez ceci pour votre projet
│   ├── GROUNDING.md         ← Calibrage comportemental de l'agent
│   └── SKILL_ROUTING.md     ← Arbre de décision des compétences
├── current.md               ← État de la tâche (volatile)
├── worklog.md               ← Historique (ajout seulement)
└── skills/                  ← 11 dossiers de compétences sélectionnées
```

## Licence

MIT
