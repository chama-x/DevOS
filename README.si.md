![DevOS: Predictability Over Perfection](assets/devos-hero.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-success.svg)]()
[![GitHub stars](https://img.shields.io/github/stars/chama-x/DevOS?style=social)](https://github.com/chama-x/DevOS/stargazers)
[![CI](https://github.com/chama-x/DevOS/actions/workflows/ci.yml/badge.svg)](https://github.com/chama-x/DevOS/actions/workflows/ci.yml)

> **DevOS — ගොනු හතරක් හරහා ඕනෑම IDE agent කෙනෙකුට ඔබේ project එකේ නීති, වත්මන් කාර්යය සහ ඉතිහාසය ලබා දෙන්න.**

```text
> Agent initialized.
> Reading .agents/rules/IDENTITY.md... [Project boundaries loaded]
> Reading .agents/rules/GROUNDING.md... [Behavioral constraints loaded]
> Reading .agents/worklog.md... [Session history restored]
> Ready. 
```

![DevOS 4-File Context Architecture](assets/devos-architecture.svg)

## ඉක්මන් ආරම්භය

```bash
npx degit chama-x/DevOS/.agents .agents
vim .agents/rules/IDENTITY.md
# ඔබගේ IDE agent නැවත ආරම්භ කරන්න — එය දැන් සෑම chat එකකදීම ඔබගේ project context කියවයි.
```

## ඇයි DevOS?

IDE agents සෑම chat එකක්ම බිංදුවෙන් ආරම්භ කරයි. DevOS ඔවුන්ට මතකයක් ලබා දෙයි — ඔබේ නීති, කාර්යය, ඉතිහාසය — එවිට ඔවුන් අනුමාන කිරීම නවතා ගොඩනැගීම ආරම්භ කරයි.

## විශේෂාංග

| විශේෂාංගය | එය කුමක් කරයිද |
|---|---|
| **11 කුසලතා** | කාර්යයකට අවශ්‍ය තර්කන ලූපය පමණක් පටවයි |
| **කුසලතා ක්‍රමාංකනය** | කාර්යයන් ස්වයංක්‍රීයව නිවැරදි කුසලතාවයට යොමු කරයි |
| **පාලනය** | Agents නව කුසලතා යෝජනා කරයි; ඔබ අනුමත කරයි |
| **සන්දර්භය සම්පීඩනය** | ඉතිහාසය විශාල වීමට පෙර සංරක්ෂණය කරයි |
| **ශබ්දකෝෂය** | ඔබේ කෙටි යෙදුම් නිශ්චිත හැසිරීමකට සිතියම්ගත කරයි |

## ලේඛන සහ ප්‍රජාව

අපි විශ්වාසය, පුරෝකථනය කිරීමේ හැකියාව සහ සහයෝගීතාවයට ප්‍රමුඛත්වය දෙන්නෙමු.
- [Changelog](CHANGELOG.md) - නිකුත් කිරීමේ ඉතිහාසය.
- [Contributing Guidelines](CONTRIBUTING.md) - අපි සෑම PR එකක්ම සමාලෝචනය කරමු.
- [Code of Conduct](CODE_OF_CONDUCT.md) - ප්‍රජා ප්‍රමිතීන්.

## Project Structure (ව්‍යාපෘති ව්‍යුහය)

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← ඔබේ ව්‍යාපෘතිය සඳහා මෙය සම්පූර්ණ කරන්න
│   ├── GROUNDING.md         ← Agent ගේ හැසිරීම් ක්‍රමාංකනය
│   └── SKILL_ROUTING.md     ← කුසලතා තීරණ ගස
├── current.md               ← තාවකාලික කාර්යය තත්ත්වය (Volatile task state)
├── worklog.md               ← Append-only ඉතිහාසය
└── skills/                  ← තෝරාගත් කුසලතා 11 ක නාමාවලි
```

## බලපත්‍රය

MIT
