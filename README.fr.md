# DevOS

![DevOS Architecture](assets/DevOS.jpg)

Déposez le dossier `.agents` dans n'importe quel espace de travail. Le prochain agent qui l'ouvrira lira quatre fichiers avant sa première réponse — ce ne sera pas un simple chatbot générique avec un accès au terminal.

## Ce qu'il fait

Un agent d'IDE fraîchement lancé ne connaît pas votre projet, vos standards, vos erreurs fréquentes, ni ce qui s'est passé hier. DevOS comble ces lacunes avec quatre fichiers :

| Fichier | Ce qu'il fait |
|---|---|
| `rules/IDENTITY.md` | Votre déclaration de ce qu'est le projet, à quoi ressemble le travail terminé, et où l'agent a de l'autonomie par rapport aux décisions que vous validez. |
| `rules/GROUNDING.md` | Calibrage comportemental — comment l'agent implémente, communique, repère ses propres erreurs, et démarre chaque session. |
| `current.md` | Ce sur quoi l'agent travaille en ce moment, ce qu'il ne touche pas, et quand la tâche est terminée. |
| `worklog.md` | Ce qui a été fait avant — pour que la prochaine session ne reparte pas de zéro. |

Deux fichiers de règles sont injectés dans chaque conversation (~700 jetons). Deux fichiers dynamiques sont lus au démarrage de la session. C'est tout le système.

## Installation

Copiez `.agents/` à la racine de votre projet. Remplissez `rules/IDENTITY.md` pour votre projet. C'est fait.

## Ce qui est inclus

Au-delà des quatre fichiers de base, DevOS est livré avec :

- **11 compétences (skills) sélectionnées** — des boucles de raisonnement étroites et des contraintes de sortie pour des tâches spécifiques, et non des documents de référence génériques que l'agent pourrait survoler.
- **Calibrage des compétences** — le routage SkillsBench charge uniquement les compétences dont une tâche a besoin, au lieu d'empiler les onze dans le contexte.
- **Gouvernance de l'évolution** — les agents proposent de nouvelles compétences et du vocabulaire, mais seul l'humain approuve.
- **Compression de contexte** — l'archivage automatique empêche les fichiers de mémoire de croître indéfiniment.
- **Dictionnaire sémantique** — associe vos raccourcis et préférences à un comportement déterministe de l'agent.

## Philosophie

DevOS est construit sur quatre directives basées sur des preuves :

1. **Demandez, ne supposez pas** — exprimez les incertitudes avant de continuer (+3,7 % de réussite des tâches).
2. **Implémentation minimum viable** — le code le plus petit qui fonctionne, pas d'abstraction spéculative.
3. **Discipline de la portée** — ne touchez qu'à ce que la tâche exige (les agents par défaut triplent leur taux de pannes sur les tâches de maintenance).
4. **Définissez le succès, puis itérez** — sachez à quoi ressemble le résultat avant d'écrire du code.

Et un principe de conception : **la prévisibilité avant la perfection.** L'humain n'a pas besoin d'un agent parfait. Il a besoin d'un agent dont il peut apprendre le comportement, vérifier la portée, et dont il peut compenser les modes de défaillance.

## Structure du projet

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← Remplissez ceci pour votre projet
│   ├── GROUNDING.md         ← Calibrage comportemental de l'agent
│   ├── EVOLUTION.md         ← Boucle d'apprentissage gouvernée
│   ├── SKILL_ROUTING.md     ← Arbre de décision des compétences
│   └── business_context.md  ← Modèle de graphe de connaissances
├── AGENTS.md                ← Règles de calibrage des compétences
├── current.md               ← État de la tâche (volatile)
├── worklog.md               ← Historique (ajout seulement)
├── memory/
│   ├── user_lexicon.md      ← Dictionnaire sémantique
│   └── rejected_proposals.md
├── skills/                  ← 11 dossiers de compétences sélectionnées
├── telemetry/
│   └── runs.md
└── archive/
    └── index.md
```

## Licence

MIT
