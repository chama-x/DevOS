# DevOS

![DevOS: Predictability Over Perfection](assets/devos-bento-hero.jpg)

`.agents` ෆෝල්ඩරය ඕනෑම workspace එකකට එකතු කරන්න. ඊළඟට එය විවෘත කරන agent තම පළමු ප්‍රතිචාරයට පෙර ගොනු හතරක් කියවයි — එය terminal access සහිත සාමාන්‍ය chatbot කෙනෙකු පමණක් නොවේ.

## මෙය කුමක් කරයිද

අලුත් IDE agent කෙනෙකුට ඔබේ project එක, ඔබේ ප්‍රමිති, ඔබේ දෝෂ රටා (failure patterns), හෝ ඊයේ සිදු වූ දේ ගැන කිසිම අවබෝධයක් නැත. DevOS මෙම හිඩැස් ගොනු හතරක් (four files) හරහා පුරවයි:

| File | What It Does |
|---|---|
| `rules/IDENTITY.md` | project එක යනු කුමක්ද, අවසන් වූ වැඩක් පෙනෙන්නේ කෙසේද, සහ agent ට ස්වයං පාලනයක් ඇති තැන් සහ ඔබ තීරණ ගන්නා තැන් පිළිබඳ ඔබේ ප්‍රකාශනයයි. |
| `rules/GROUNDING.md` | හැසිරීම් ක්‍රමාංකනය (Behavioral calibration) — agent ක්‍රියාත්මක කරන ආකාරය, සන්නිවේදනය කරන ආකාරය, තමන්ගේම වැරදි අල්ලා ගන්නා ආකාරය සහ සෑම session එකක්ම ආරම්භ කරන ආකාරය. |
| `current.md` | agent මේ මොහොතේ වැඩ කරමින් සිටින්නේ කුමක් මතද, ස්පර්ශ නොකරන්නේ මොනවාද, සහ එය අවසන් වන්නේ කවදාද යන්න. |
| `worklog.md` | මින් පෙර කළ දේ — මීළඟ session එක බිංදුවෙන් ආරම්භ නොවීම සඳහා. |

රීති ගොනු දෙකක් සෑම සංවාදයකටම ඇතුළත් කෙරේ (~700 tokens). dynamic ගොනු දෙකක් session එක ආරම්භයේදී කියවනු ලැබේ. සම්පූර්ණ පද්ධතියම එයයි.

![DevOS 4-File Context Architecture](assets/devos-architecture-infographic.jpg)

## ස්ථාපනය

`.agents/` ඔබේ project root එකට copy කරන්න. ඔබේ project එක සඳහා `rules/IDENTITY.md` සම්පූර්ණ කරන්න. එපමණයි.

## ඇතුළත් වන දෑ

core files හතරට අමතරව, DevOS පහත දෑ සමඟ පැමිණේ:

- **11 curated skills** — agent විසින් ඉක්මනින් කියවා දමන සාමාන්‍ය විමර්ශන ලේඛන (generic reference docs) වෙනුවට, නිශ්චිත කාර්යයන් සඳහා සීමා කරන ලද තර්කන ලූප සහ ප්‍රතිදාන සීමාවන් (output constraints).
- **Skill calibration** — SkillsBench මාර්ගගත කිරීම (routing) මගින් කුසලතා එකොළහම එකට පැටවීම වෙනුවට, කාර්යයකට අවශ්‍ය කුසලතා පමණක් පටවනු ලැබේ.
- **Evolution governance** — agents නව කුසලතා සහ වචන මාලාවන් යෝජනා කරයි, නමුත් අනුමත කරන්නේ පරිශීලකයා (human) පමණි.
- **Context compression** — ස්වයංක්‍රීය සංරක්ෂණය මගින් මතක ගොනු සීමාවකින් තොරව වර්ධනය වීම වළක්වයි.
- **Semantic dictionary** — ඔබේ කෙටි යෙදුම් සහ මනාපයන්, agent ගේ නිශ්චිත හැසිරීම් (deterministic behavior) වෙත යොමු කරයි.

## දර්ශනය

DevOS ගොඩනගා ඇත්තේ සාක්ෂි සහිත නියෝග හතරක් මතය:

1. **Ask, don't assume** — ඉදිරියට යාමට පෙර අවිනිශ්චිතතා මතු කරන්න (+3.7% task success).
2. **Minimum viable implementation** — වැඩ කරන කුඩාම කේතය, අනුමාන කිරීමේ (speculative) වියුක්ත කිරීම් නැත.
3. **Scope discipline** — කාර්යයට අවශ්‍ය දේ පමණක් ස්පර්ශ කරන්න (නඩත්තු කාර්යයන්හිදී සාමාන්‍ය agents ඔවුන්ගේ breaking-change rate එක තුන් ගුණයකින් වැඩි කරයි).
4. **Define success, then loop** — කේතය ලිවීමට පෙර 'අවසන් වූ (done)' යන්න පෙනෙන්නේ කෙසේදැයි දැන ගන්න.

සහ එක් සැලසුම් මූලධර්මයක්: **පරිපූර්ණත්වයට වඩා පුරෝකථනය කිරීමේ හැකියාව (predictability over perfection).** මිනිසාට පරිපූර්ණ agent කෙනෙකු අවශ්‍ය නොවේ. අවශ්‍ය වන්නේ, හැසිරීම් ඉගෙන ගත හැකි, විෂය පථය තහවුරු කළ හැකි සහ අසාර්ථක වීමේ ක්‍රම (failure modes) සඳහා වන්දි ගෙවිය හැකි agent කෙනෙකි.

## Project Structure (ව්‍යාපෘති ව්‍යුහය)

```
.agents/
├── rules/
│   ├── IDENTITY.md          ← ඔබේ ව්‍යාපෘතිය සඳහා මෙය සම්පූර්ණ කරන්න
│   ├── GROUNDING.md         ← Agent ගේ හැසිරීම් ක්‍රමාංකනය
│   ├── EVOLUTION.md         ← පාලනය කළ ඉගෙනුම් ලූපය
│   ├── SKILL_ROUTING.md     ← කුසලතා තීරණ ගස
│   └── business_context.md  ← දැනුම් ප්‍රස්තාර (Knowledge graph) අච්චුව
├── AGENTS.md                ← කුසලතා ක්‍රමාංකන රීති
├── current.md               ← තාවකාලික කාර්යය තත්ත්වය (Volatile task state)
├── worklog.md               ← Append-only ඉතිහාසය
├── memory/
│   ├── user_lexicon.md      ← Semantic ශබ්දකෝෂය
│   └── rejected_proposals.md
├── skills/                  ← තෝරාගත් කුසලතා 11 ක නාමාවලි
├── telemetry/
│   └── runs.md
└── archive/
    └── index.md
```

## බලපත්‍රය

MIT
