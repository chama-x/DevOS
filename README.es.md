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

## DevOS frente a Prompts de archivo único (.cursorrules)

| Característica | Archivo `.cursorrules` / Prompts únicos | DevOS |
|---|---|---|
| **Arquitectura** | Archivo gigante (sobrecarga el contexto) | 4 archivos modulares + enrutamiento dinámico |
| **Memoria de Sesión** | Se reinicia en cada nuevo chat | Se conserva entre sesiones vía `worklog.md` |
| **Uso de Tokens** | ~5.000+ tokens cargados siempre | ~700 tokens base; habilidades según demanda |
| **Disciplina de Alcance** | Sugerencias suaves (el agente las ignora) | Restricciones estrictas con `GROUNDING.md` |
| **Control de Autonomía** | Límites no definidos | Niveles explícitos declarados en `IDENTITY.md` |

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
