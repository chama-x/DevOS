![DevOS: Predictability Over Perfection](assets/devos-hero.svg?v=1786143843)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — Dale a cualquier agente IDE las reglas, tarea actual e historial de tu proyecto en cuatro archivos.**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```

![DevOS 4-File Context Architecture](assets/devos-architecture.svg?v=1786143843)

## Inicio Rápido

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# Reinicia tu agente IDE — ahora leerá el contexto de tu proyecto en cada chat.
```

## ¿Por qué DevOS?

Los agentes IDE comienzan cada chat desde cero. DevOS les da una memoria — tus reglas, tu tarea, tu historial — para que dejen de adivinar y comiencen a construir.

## DevOS vs. Prompts Ad-hoc (.cursorrules, Instrucciones Personalizadas)

Reemplaza paquetes de prompts dispersos, archivos únicos `.cursorrules` e instrucciones ad-hoc con un motor de contexto determinista de 4 archivos.

| Capacidad | Prompts y Paquetes (.cursorrules / CLAUDE.md) | Motor DevOS |
|---|---|---|
| **Arquitectura** | Volcado de texto monolítico (desperdicia contexto) | 4 archivos núcleo modulares (~700 tokens) |
| **Memoria de Sesión** | Amnesia: se reinicia completamente en cada chat | Continua: restaura el progreso mediante `worklog.md` |
| **Carga de Habilidades** | Carga todas las reglas a la vez (causa alucinaciones) | Calibrada: enrutamiento dinámico carga máx. 2–3 habilidades |
| **Disciplina de Alcance** | Sugerencias difusas (los agentes refactorizan al azar) | Control estricto mediante chequeos en `GROUNDING.md` |
| **Límites de Proyecto** | Implícitos o no declarados | Autonomía explícita y líneas rojas en `IDENTITY.md` |

## Características

| Característica | Qué hace |
|---|---|
| **11 Habilidades** | Carga solo el bucle de razonamiento que necesita una tarea |
| **Calibración** | Enruta las tareas a la habilidad correcta automáticamente |
| **Gobernanza** | Los agentes proponen nuevas habilidades; tú apruebas |
| **Compresión** | Archiva el historial antes de que crezca sin límite |
| **Diccionario Semántico** | Mapea tus atajos hacia comportamientos deterministas |

## Documentación y Comunidad

Priorizamos la confianza, la predictibilidad y la colaboración.
- [Changelog](CHANGELOG.md) - Historial de lanzamientos.
- [Guía de Contribución](CONTRIBUTING.md) - Revisamos todos los PR. Comienza con issues `good first issue`.
- [Código de Conducta](CODE_OF_CONDUCT.md) - Nuestros estándares.

## Estructura del Proyecto

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← Completa esto para tu proyecto
│   ├── GROUNDING.md         ← Calibración de comportamiento del agente
│   └── SKILL_ROUTING.md     ← Árbol de decisión de habilidades
├── current.md               ← Estado volátil de la tarea
├── worklog.md               ← Historial (solo adición)
└── skills/                  ← 11 directorios de habilidades seleccionadas
```

## Licencia

MIT
