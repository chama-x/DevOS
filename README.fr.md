# AgentOS : Le Cadre MAS Autogéré

![Architecture AgentOS](assets/CortanaAgentOS.jpg)

Les IDE modernes sont livrés avec de puissants agents LLM de base, mais dans leur état par défaut, ils sont essentiellement des chatbots sans état avec un accès au terminal. Ils souffrent de "Négligence de l'Idempotence" (casser le code en réessayant de mauvaises modifications), de gonflement du contexte (épuisement de la mémoire), et du syndrome du "Modèle Dieu" (essayer de résoudre des problèmes de 100k tokens dans une fenêtre de 4k tokens).

Nous avons conçu un **Cadre de Contexte AgentOS Personnalisé** qui se place au-dessus de l'agent IDE. Au moment où un agent "frais" se réveille dans cet environnement, il est instantanément transformé par des fichiers de configuration locaux en un **Superviseur Autogéré, Stratifié par les Risques**.

## Fonctionnalités Principales

### 1. Autonomie Stratifiée par les Risques (Risk-Tiered Autonomy)
Les agents frais traitent toutes les tâches de la même manière. Notre AgentOS injecte un système strict d'autonomie à 4 niveaux :
- **T0** : Lectures, recherches, linting (Auto-Procédure).
- **T1** : Modifications d'un seul fichier (Auto-Procédure. Doit d'abord faire un `git commit` d'un point de contrôle).
- **T2** : Refactorisations de plusieurs fichiers (Approbation par lots).
- **T3** : Suppressions, Injection Externe, modifications d'Authentification (Révision Obligatoire par l'Équipe Rouge).

### 2. Idempotence & Le Noyau de Récupération (The Recovery Kernel)
Chaque mutation doit d'abord vérifier si son effet existe déjà. Si un remplacement de texte chirurgical échoue, l'agent a droit à *une seule* tentative. Au deuxième échec, il doit abandonner, empêchant ainsi les boucles d'exécution infinies.

### 3. Compression de Mémoire Transactionnelle (Transactional Memory Compression)
Lorsque la mémoire de `worklog.md` dépasse 4 000 tokens, l'agent exécute une boucle transactionnelle en 5 étapes : Distiller → Ajouter → Vérifier → Tronquer → Valider (Commit). Cela offre une garantie à 100 % contre la perte de données de contexte lors des plantages du LLM.

### 4. Délégation Frontalière (Frontier Delegation - Supervisor/Worker MAS)
Lorsqu'une tâche nécessite une logique extrême (40k+ tokens), l'OS déclenche un paquet de transfert. L'agent nettoie les secrets et les clés API, et compile un prompt dense pour un Modèle Frontal (Frontier Model) externe. Lorsque le code revient, il est injecté textuellement, analysé statiquement, et présenté comme un `git diff` pour une révision humaine de niveau T3.

### 5. Verrou Constitutionnel & Échafaudage de l'OS (Constitutional Lock & OS Scaffolding)
L'agent ne peut pas réécrire ses propres garde-fous. Toute modification du répertoire `.agents/rules/` est classée de manière permanente comme une **action T3**. De plus, si des fichiers principaux manquent au démarrage, l'agent déclenchera automatiquement un questionnaire à choix multiples pour échafauder l'espace de travail.

## Installation
Il suffit de déposer le dossier `.agents` à la racine de votre espace de travail, et votre agent se transformera instantanément en le Superviseur V2 !
