---
name: odoo-rl-rules
description: Odoo CLI Reinforcement Learning rules layer. Triggers to enforce strict coding constraints, field naming conventions, and performance guidelines for Odoo module development.
---

# Odoo CLI Constraints and RL Rules

You are acting as an enforcer of Odoo's strictest performance and structural rules.

## 1. Naming Conventions
*   Custom modules must always start with the project prefix.
*   Custom fields injected into base models must start with `x_` to avoid future core conflicts, unless building an entirely new custom model.

## 2. ORM Performance Rules (No N+1)
*   **NEVER** loop over recordsets to execute `write()` or `search()`.
*   Always use batched operations. For example, instead of `for rec in records: rec.write({'state': 'done'})`, use `records.write({'state': 'done'})`.
*   When fetching relational data in loops, ensure records are pre-fetched or use `read_group`.

## 3. Security (ir.model.access)
*   Every new model MUST have a corresponding `ir.model.access.csv` entry.
*   Agents must refuse to create a model if they do not also define access rules.

## 4. Views and Inherits
*   Always use `xpath` accurately when inheriting views.
*   Never overwrite a core view's architecture completely; only append or replace targeted nodes.
