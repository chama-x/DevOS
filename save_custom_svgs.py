import time
import glob

architecture_svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="1200" height="500">
  <defs>
    <!-- Filters -->
    <filter id="cardShadow" x="-12%" y="-12%" width="130%" height="140%">
      <feDropShadow dx="0" dy="6" stdDeviation="14" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
    <filter id="insetShadow" x="-5%" y="-5%" width="112%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
    <filter id="glowCyan" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glowCyanSoft" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="14"/>
    </filter>
    <filter id="glowGreen" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="ambientBlur" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="55"/>
    </filter>
    <filter id="subtleGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Gradients -->
    <linearGradient id="cardGrad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1c2128"/>
      <stop offset="100%" stop-color="#161b22"/>
    </linearGradient>
    <linearGradient id="cardShine" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.025"/>
      <stop offset="25%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="topAccentL" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0"/>
      <stop offset="50%" stop-color="#58a6ff" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="topAccentR" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#3fb950" stop-opacity="0"/>
      <stop offset="50%" stop-color="#3fb950" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#3fb950" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="arrowStroke" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0.4"/>
      <stop offset="50%" stop-color="#79c0ff" stop-opacity="1"/>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0.4"/>
    </linearGradient>
    <linearGradient id="arrowHead" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#79c0ff"/>
      <stop offset="100%" stop-color="#58a6ff"/>
    </linearGradient>
    <radialGradient id="orbCyan" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="orbGreen" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0%" stop-color="#3fb950" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#3fb950" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vignette" cx="0.5" cy="0.5" r="0.75">
      <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.25"/>
    </radialGradient>

    <!-- Patterns -->
    <pattern id="dotGrid" x="0" y="0" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="11" cy="11" r="0.4" fill="#21262d" opacity="0.4"/>
    </pattern>

    <!-- Clip Paths -->
    <clipPath id="clipLeft"><rect x="46" y="116" width="498" height="330" rx="10"/></clipPath>
    <clipPath id="clipRight"><rect x="656" y="116" width="498" height="330" rx="10"/></clipPath>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Fira+Code:wght@400;500&amp;display=swap');
    .inter { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif; }
    .mono  { font-family: 'Fira Code', 'Cascadia Code', 'JetBrains Mono', Consolas, 'Courier New', monospace; }
  </style>

  <!-- ════════════════════════════════════════════ -->
  <!--                  BACKGROUND                  -->
  <!-- ════════════════════════════════════════════ -->
  <rect width="1200" height="500" fill="#0d1117"/>
  <rect width="1200" height="500" fill="url(#dotGrid)" opacity="0.5"/>

  <!-- Ambient orbs -->
  <ellipse cx="290" cy="250" rx="260" ry="200" fill="url(#orbCyan)" filter="url(#ambientBlur)"/>
  <ellipse cx="910" cy="250" rx="260" ry="200" fill="url(#orbGreen)" filter="url(#ambientBlur)"/>

  <!-- Vignette -->
  <rect width="1200" height="500" fill="url(#vignette)"/>


  <!-- ════════════════════════════════════════════ -->
  <!--                 LEFT CARD                    -->
  <!-- ════════════════════════════════════════════ -->
  <g>
    <!-- Card body -->
    <rect x="28" y="38" width="534" height="424" rx="16" fill="url(#cardGrad)" stroke="#30363d" stroke-width="1" filter="url(#cardShadow)"/>
    <!-- Shine overlay -->
    <rect x="28" y="38" width="534" height="424" rx="16" fill="url(#cardShine)"/>
    <!-- Top accent glow -->
    <rect x="28" y="38" width="534" height="2" rx="1" fill="url(#topAccentL)"/>

    <!-- ── Badge ── -->
    <rect x="50" y="56" width="72" height="22" rx="6" fill="#58a6ff" opacity="0.1"/>
    <rect x="50" y="56" width="72" height="22" rx="6" fill="none" stroke="#58a6ff" stroke-width="0.6" opacity="0.35"/>
    <text x="86" y="71.5" class="inter" font-size="9.5" font-weight="600" fill="#58a6ff" text-anchor="middle" letter-spacing="1.6">INPUT</text>

    <!-- ── Title ── -->
    <text x="50" y="101" class="inter" font-size="16" font-weight="600" fill="#e6edf3">The Context Constraint <tspan fill="#8b949e" font-weight="400" font-size="14.5">(GROUNDING.md)</tspan></text>

    <!-- ── Code Block Container ── -->
    <g clip-path="url(#clipLeft)">
      <rect x="46" y="116" width="498" height="330" fill="#0d1117"/>
      <!-- Top bar -->
      <rect x="46" y="116" width="498" height="30" fill="#161b22"/>
      <!-- Separator -->
      <line x1="46" y1="146" x2="544" y2="146" stroke="#21262d" stroke-width="1"/>
      <!-- Line number gutter -->
      <rect x="46" y="146" width="42" height="300" fill="#080b10" opacity="0.5"/>
      <line x1="88" y1="146" x2="88" y2="446" stroke="#21262d" stroke-width="0.5" opacity="0.4"/>
    </g>
    <rect x="46" y="116" width="498" height="330" rx="10" fill="none" stroke="#21262d" stroke-width="1" filter="url(#insetShadow)"/>

    <!-- Window dots -->
    <circle cx="66" cy="131" r="4.5" fill="#ff5f57" opacity="0.85"/>
    <circle cx="82" cy="131" r="4.5" fill="#febc2e" opacity="0.85"/>
    <circle cx="98" cy="131" r="4.5" fill="#28c840" opacity="0.85"/>

    <!-- Filename -->
    <text x="534" y="135.5" class="inter" font-size="11" font-weight="500" fill="#8b949e" text-anchor="end">GROUNDING.md</text>

    <!-- ── Line Numbers ── -->
    <text class="mono" font-size="11.5" fill="#484f58" text-anchor="end">
      <tspan x="82" y="172">1</tspan>
      <tspan x="82" y="198">2</tspan>
      <tspan x="82" y="224">3</tspan>
      <tspan x="82" y="250">4</tspan>
      <tspan x="82" y="276">5</tspan>
    </text>

    <!-- ── Code Text ── -->
    <!-- Line 1: ## Scope Discipline -->
    <text x="100" y="172" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#ff7b72">## </tspan><tspan fill="#d2a8ff" font-weight="500">Scope Discipline</tspan>
    </text>

    <!-- Line 2: (blank) -->

    <!-- Line 3: Never refactor adjacent code. -->
    <text x="100" y="224" class="mono" font-size="12.5" fill="#c9d1d9">Never refactor adjacent code.</text>

    <!-- Line 4: Fix only your own mess. -->
    <!-- Subtle highlight behind the key constraint -->
    <rect x="97" y="238" width="183" height="19" rx="3" fill="#58a6ff" opacity="0.04"/>
    <text x="100" y="250" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#79c0ff">Fix only</tspan><tspan> your own mess.</tspan>
    </text>

    <!-- Line 5: Do not touch working systems outside the task scope. -->
    <text x="100" y="276" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#79c0ff">Do not touch</tspan><tspan> working systems outside the task scope.</tspan>
    </text>

    <!-- Blinking cursor -->
    <rect x="100" y="286" width="7.5" height="15" rx="1.5" fill="#58a6ff" opacity="0.75">
      <animate attributeName="opacity" values="0.75;0;0.75" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>


  <!-- ════════════════════════════════════════════ -->
  <!--              ARROW CONNECTOR                 -->
  <!-- ════════════════════════════════════════════ -->
  <g>
    <!-- Wide ambient glow -->
    <line x1="572" y1="250" x2="628" y2="250" stroke="#58a6ff" stroke-width="12" opacity="0.15" filter="url(#glowCyanSoft)"/>

    <!-- Glow behind main line -->
    <line x1="574" y1="250" x2="622" y2="250" stroke="#58a6ff" stroke-width="4" opacity="0.35" filter="url(#glowCyan)"/>

    <!-- Main line -->
    <line x1="574" y1="250" x2="618" y2="250" stroke="url(#arrowStroke)" stroke-width="2" stroke-linecap="round"/>

    <!-- Arrowhead -->
    <path d="M620,250 L632,250 L622,241 M622,259 L632,250" fill="none" stroke="url(#arrowHead)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" filter="url(#subtleGlow)"/>

    <!-- Connection dots -->
    <circle cx="568" cy="250" r="3" fill="#58a6ff" opacity="0.45"/>
    <circle cx="568" cy="250" r="1.5" fill="#79c0ff" opacity="0.8"/>
    <circle cx="636" cy="250" r="3" fill="#3fb950" opacity="0.45"/>
    <circle cx="636" cy="250" r="1.5" fill="#7ee787" opacity="0.8"/>

    <!-- Traveling dot animation -->
    <circle r="2.5" fill="#79c0ff" opacity="0.9" filter="url(#subtleGlow)">
      <animateMotion dur="2.5s" repeatCount="indefinite" keyTimes="0;0.4;0.6;1" keySplines="0.4 0 0.2 1;0.4 0 0.2 1;0.4 0 0.2 1" calcMode="spline" path="M574,250 L628,250"/>
      <animate attributeName="opacity" values="0;0.9;0.9;0" dur="2.5s" repeatCount="indefinite"/>
    </circle>

    <!-- Label -->
    <text x="600" y="278" class="inter" font-size="8" font-weight="700" fill="#58a6ff" text-anchor="middle" letter-spacing="2.5" opacity="0.5">APPLIES</text>
  </g>


  <!-- ════════════════════════════════════════════ -->
  <!--                 RIGHT CARD                   -->
  <!-- ════════════════════════════════════════════ -->
  <g>
    <!-- Card body -->
    <rect x="638" y="38" width="534" height="424" rx="16" fill="url(#cardGrad)" stroke="#30363d" stroke-width="1" filter="url(#cardShadow)"/>
    <!-- Shine overlay -->
    <rect x="638" y="38" width="534" height="424" rx="16" fill="url(#cardShine)"/>
    <!-- Top accent glow -->
    <rect x="638" y="38" width="534" height="2" rx="1" fill="url(#topAccentR)"/>

    <!-- ── Badge ── -->
    <rect x="660" y="56" width="82" height="22" rx="6" fill="#3fb950" opacity="0.1"/>
    <rect x="660" y="56" width="82" height="22" rx="6" fill="none" stroke="#3fb950" stroke-width="0.6" opacity="0.35"/>
    <text x="701" y="71.5" class="inter" font-size="9.5" font-weight="600" fill="#3fb950" text-anchor="middle" letter-spacing="1.6">OUTPUT</text>

    <!-- ── Title ── -->
    <text x="660" y="101" class="inter" font-size="16" font-weight="600" fill="#e6edf3">The Agent Execution</text>

    <!-- ── Terminal Container ── -->
    <g clip-path="url(#clipRight)">
      <rect x="656" y="116" width="498" height="330" fill="#0d1117"/>
      <!-- Top bar -->
      <rect x="656" y="116" width="498" height="30" fill="#161b22"/>
      <!-- Separator -->
      <line x1="656" y1="146" x2="1154" y2="146" stroke="#21262d" stroke-width="1"/>
    </g>
    <rect x="656" y="116" width="498" height="330" rx="10" fill="none" stroke="#21262d" stroke-width="1" filter="url(#insetShadow)"/>

    <!-- Window dots -->
    <circle cx="676" cy="131" r="4.5" fill="#ff5f57" opacity="0.85"/>
    <circle cx="692" cy="131" r="4.5" fill="#febc2e" opacity="0.85"/>
    <circle cx="708" cy="131" r="4.5" fill="#28c840" opacity="0.85"/>

    <!-- Terminal title -->
    <text x="1144" y="135.5" class="inter" font-size="11" font-weight="500" fill="#8b949e" text-anchor="end">agent — zsh</text>

    <!-- ── Terminal Text ── -->
    <!-- Line 1: Plan: Update the API route. -->
    <text x="672" y="170" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#3fb950" font-weight="500">Plan:</tspan><tspan> Update the API route.</tspan>
    </text>

    <!-- Line 2: Wait, I noticed the adjacent auth middleware is outdated. -->
    <!-- Subtle warning highlight -->
    <rect x="669" y="182" width="468" height="19" rx="3" fill="#f0883e" opacity="0.03"/>
    <text x="672" y="198" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#f0883e">Wait</tspan><tspan>, I noticed the adjacent auth middleware is outdated.</tspan>
    </text>

    <!-- Line 3: ❯ Checking GROUNDING.md constraint... -->
    <text x="672" y="234" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#58a6ff" font-weight="500">❯</tspan><tspan fill="#79c0ff"> Checking </tspan><tspan fill="#d2a8ff">GROUNDING.md</tspan><tspan fill="#79c0ff"> constraint...</tspan>
    </text>

    <!-- Line 4: Constraint found: 'Fix only your own mess.' -->
    <!-- Subtle highlight behind the matched constraint -->
    <rect x="669" y="246" width="370" height="19" rx="3" fill="#7ee787" opacity="0.035"/>
    <text x="672" y="260" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#f0883e" font-weight="500">Constraint found:</tspan><tspan> </tspan><tspan fill="#7ee787">'Fix only your own mess.'</tspan>
    </text>

    <!-- Line 5: ✓ I will leave the middleware alone. -->
    <!-- Subtle success highlight -->
    <rect x="669" y="280" width="335" height="19" rx="3" fill="#3fb950" opacity="0.04"/>
    <text x="672" y="296" class="mono" font-size="12.5" fill="#c9d1d9">
      <tspan fill="#3fb950" font-weight="500">✓</tspan><tspan fill="#3fb950"> I will leave the middleware alone.</tspan>
    </text>

    <!-- Blinking cursor -->
    <rect x="672" y="306" width="7.5" height="15" rx="1.5" fill="#3fb950" opacity="0.75">
      <animate attributeName="opacity" values="0.75;0;0.75" dur="1.1s" repeatCount="indefinite"/>
    </rect>
  </g>


  <!-- ════════════════════════════════════════════ -->
  <!--            DECORATIVE DETAILS                -->
  <!-- ════════════════════════════════════════════ -->

  <!-- Subtle corner accents -->
  <path d="M28,60 L28,38 Q28,38 38,38" fill="none" stroke="#58a6ff" stroke-width="0.5" opacity="0.2"/>
  <path d="M1172,60 L1172,38 Q1172,38 1162,38" fill="none" stroke="#3fb950" stroke-width="0.5" opacity="0.2"/>

  <!-- Bottom-right watermark -->
  <text x="1172" y="484" class="inter" font-size="8.5" font-weight="500" fill="#30363d" text-anchor="end" letter-spacing="1">REPOSITORY ARCHITECTURE</text>

</svg>"""

hero_svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">
  <defs>
    <filter id="winShadow" x="-10%" y="-8%" width="125%" height="130%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="18" result="b1"/>
      <feOffset in="b1" dx="0" dy="12" result="o1"/>
      <feFlood flood-color="#000000" flood-opacity="0.5" result="c1"/>
      <feComposite in="c1" in2="o1" operator="in" result="s1"/>
      <feGaussianBlur in="SourceAlpha" stdDeviation="5" result="b2"/>
      <feOffset in="b2" dx="0" dy="3" result="o2"/>
      <feFlood flood-color="#000000" flood-opacity="0.3" result="c2"/>
      <feComposite in="c2" in2="o2" operator="in" result="s2"/>
      <feMerge><feMergeNode in="s1"/><feMergeNode in="s2"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="agentGlow" x="-40%" y="-80%" width="180%" height="260%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="5" result="b"/>
      <feFlood flood-color="#58a6ff" flood-opacity="0.35" result="c"/>
      <feComposite in="c" in2="b" operator="in" result="g"/>
      <feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="txtGlow" x="-5%" y="-25%" width="110%" height="150%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="1.8" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="8" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <linearGradient id="userGrad" x1="0" y1="0" x2="1" y2="0.7">
      <stop offset="0%" stop-color="#163b25"/>
      <stop offset="50%" stop-color="#163030"/>
      <stop offset="100%" stop-color="#162d48"/>
    </linearGradient>
    <linearGradient id="topLine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#58a6ff" stop-opacity="0"/>
      <stop offset="25%" stop-color="#58a6ff" stop-opacity="0.1"/>
      <stop offset="50%" stop-color="#bc8cff" stop-opacity="0.18"/>
      <stop offset="75%" stop-color="#58a6ff" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#58a6ff" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="bgGlow" cx="0.5" cy="0.42" r="0.52">
      <stop offset="0%" stop-color="#161b22" stop-opacity="0.5"/>
      <stop offset="70%" stop-color="#0d1117" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ambientBlue" cx="0.48" cy="0.4" r="0.35">
      <stop offset="0%" stop-color="#1a2744" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="ambientPurple" cx="0.62" cy="0.55" r="0.3">
      <stop offset="0%" stop-color="#2a1a44" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#0d1117" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="winClip">
      <rect x="60" y="38" width="1080" height="580" rx="14"/>
    </clipPath>
    <pattern id="dots" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
      <circle cx="15" cy="15" r="0.55" fill="#21262d" opacity="0.45"/>
    </pattern>
  </defs>

  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&amp;family=Fira+Code:wght@400;500&amp;display=swap');
    .ui{font-family:'Inter','SF Pro Display',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif}
    .code{font-family:'Fira Code','SF Mono','Cascadia Code','Consolas','Liberation Mono',monospace}
  </style>

  <!-- ════════════════ BACKGROUND ════════════════ -->
  <rect width="1200" height="675" fill="#0d1117"/>
  <rect width="1200" height="675" fill="url(#dots)"/>
  <rect width="1200" height="675" fill="url(#bgGlow)"/>
  <rect width="1200" height="675" fill="url(#ambientBlue)"/>
  <rect width="1200" height="675" fill="url(#ambientPurple)"/>

  <!-- Faint decorative brackets in background -->
  <text x="32" y="320" class="code" font-size="180" fill="#21262d" opacity="0.06">{</text>
  <text x="1098" y="520" class="code" font-size="160" fill="#21262d" opacity="0.05">}</text>
  <text x="180" y="640" class="code" font-size="100" fill="#21262d" opacity="0.04">&lt;/&gt;</text>

  <!-- ════════════════ WINDOW FRAME ════════════════ -->
  <g filter="url(#winShadow)">
    <rect x="60" y="38" width="1080" height="580" rx="14" fill="#0d1117"/>
  </g>
  <rect x="60" y="38" width="1080" height="2" fill="url(#topLine)"/>
  <rect x="60" y="38" width="1080" height="580" rx="14" fill="none" stroke="#30363d" stroke-width="1"/>

  <!-- ════════════════ WINDOW CONTENT ════════════════ -->
  <g clip-path="url(#winClip)">

    <!-- ──────── TITLE BAR ──────── -->
    <rect x="60" y="38" width="1080" height="42" fill="#161b22"/>
    <line x1="60" y1="80" x2="1140" y2="80" stroke="#21262d" stroke-width="1"/>

    <!-- macOS Traffic Lights -->
    <circle cx="82" cy="59" r="6.5" fill="#ff5f57"/>
    <circle cx="102" cy="59" r="6.5" fill="#febc2e"/>
    <circle cx="122" cy="59" r="6.5" fill="#28c840"/>
    <!-- Specular highlights -->
    <ellipse cx="80" cy="56.5" rx="3.2" ry="2.2" fill="#ff9a94" opacity="0.3"/>
    <ellipse cx="100" cy="56.5" rx="3.2" ry="2.2" fill="#ffe066" opacity="0.3"/>
    <ellipse cx="120" cy="56.5" rx="3.2" ry="2.2" fill="#6eff7e" opacity="0.3"/>
    <!-- Dot inner rings -->
    <circle cx="82" cy="59" r="4" fill="none" stroke="#000000" stroke-width="0.4" opacity="0.15"/>
    <circle cx="102" cy="59" r="4" fill="none" stroke="#000000" stroke-width="0.4" opacity="0.15"/>
    <circle cx="122" cy="59" r="4" fill="none" stroke="#000000" stroke-width="0.4" opacity="0.15"/>

    <!-- Window Title -->
    <text x="600" y="63.5" text-anchor="middle" class="ui" font-size="12.5" font-weight="500" fill="#8b949e">agents-playground — Cursor</text>

    <!-- Tab indicators in title bar -->
    <rect x="780" y="46" width="80" height="28" rx="6" fill="#21262d" opacity="0.5"/>
    <text x="820" y="64" text-anchor="middle" class="ui" font-size="10.5" fill="#8b949e">main.ts</text>
    <rect x="866" y="46" width="90" height="28" rx="6" fill="#0d1117" opacity="0.6"/>
    <text x="911" y="64" text-anchor="middle" class="ui" font-size="10.5" fill="#e6edf3">AI Chat</text>
    <circle cx="948" cy="55" r="3" fill="#bc8cff" opacity="0.6"/>


    <!-- ════════════════ LEFT PANE ════════════════ -->
    <rect x="60" y="80" width="310" height="518" fill="#0d1117"/>

    <!-- EXPLORER Header -->
    <text x="78" y="106" class="ui" font-size="10.5" font-weight="600" fill="#8b949e" letter-spacing="1.2">EXPLORER</text>
    <!-- Collapse icon -->
    <text x="346" y="106" class="ui" font-size="11" fill="#484f58">···</text>
    <line x1="78" y1="113" x2="356" y2="113" stroke="#21262d" stroke-width="0.5"/>

    <!-- ── File Tree ── -->

    <!-- 📁 src (dimmed) -->
    <g opacity="0.32">
      <g transform="translate(90,124)">
        <rect x="0" y="3" width="14" height="10" rx="1.5" fill="#8b949e"/>
        <rect x="0" y="1" width="6" height="4" rx="1" fill="#8b949e"/>
      </g>
      <text x="112" y="135" class="ui" font-size="13" fill="#c9d1d9">src</text>
    </g>

    <!-- 📁 public (dimmed) -->
    <g opacity="0.32">
      <g transform="translate(90,150)">
        <rect x="0" y="3" width="14" height="10" rx="1.5" fill="#8b949e"/>
        <rect x="0" y="1" width="6" height="4" rx="1" fill="#8b949e"/>
      </g>
      <text x="112" y="161" class="ui" font-size="13" fill="#c9d1d9">public</text>
    </g>

    <!-- 📁 .agents (HIGHLIGHTED) -->
    <!-- Glow background -->
    <rect x="68" y="175" width="296" height="28" rx="5" fill="#1a2744" opacity="0.18"/>
    <!-- Soft blue glow behind row -->
    <rect x="68" y="175" width="296" height="28" rx="5" fill="#58a6ff" opacity="0.04" filter="url(#softGlow)"/>
    <!-- Left accent bar -->
    <rect x="68" y="176" width="2.5" height="26" rx="1.25" fill="#58a6ff" opacity="0.85"/>

    <!-- Open folder icon (blue) -->
    <g transform="translate(90,176)">
      <path d="M0,4 L0,11.5 Q0,12.5 1,12.5 L13,12.5 Q14,12.5 14,11.5 L14,4.5 L8.5,4.5 L7.5,3.5 Q7,3 6.5,3 L1,3 Q0,3 0,4 Z" fill="#58a6ff" opacity="0.85"/>
      <path d="M2,5.5 L5,5.5 L5.8,4.5 Q6.2,4 6.8,4 L13.2,4 Q14,4 13.8,5 L12.5,11 Q12.3,12 11.5,12 L1.5,12 Q0.7,12 0.9,11 L2,6 Q2.2,5 2.5,5.5 Z" fill="#58a6ff" opacity="0.45"/>
    </g>
    <text x="112" y="189" class="ui" font-size="13" font-weight="600" fill="#58a6ff">.agents</text>
    <!-- Glow text overlay -->
    <text x="112" y="189" class="ui" font-size="13" font-weight="600" fill="#58a6ff" opacity="0.25" filter="url(#agentGlow)">.agents</text>

    <!-- Tree indent guide -->
    <line x1="100" y1="205" x2="100" y2="310" stroke="#1f3a5e" stroke-width="1" opacity="0.35"/>
    <!-- Tree branch connectors -->
    <line x1="100" y1="210" x2="106" y2="210" stroke="#1f3a5e" stroke-width="1" opacity="0.35"/>
    <line x1="100" y1="236" x2="106" y2="236" stroke="#1f3a5e" stroke-width="1" opacity="0.35"/>
    <line x1="100" y1="262" x2="106" y2="262" stroke="#1f3a5e" stroke-width="1" opacity="0.35"/>
    <line x1="100" y1="288" x2="106" y2="288" stroke="#1f3a5e" stroke-width="1" opacity="0.35"/>

    <!-- 📄 IDENTITY.md -->
    <g transform="translate(110,202)">
      <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.75"/>
      <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.75"/>
      <line x1="2.5" y1="7" x2="8.5" y2="7" stroke="#58a6ff" stroke-width="0.6" opacity="0.35"/>
      <line x1="2.5" y1="9.5" x2="7" y2="9.5" stroke="#58a6ff" stroke-width="0.6" opacity="0.35"/>
    </g>
    <text x="128" y="214" class="ui" font-size="12.5" fill="#c9d1d9">IDENTITY.md</text>
    <!-- Active file indicator dot -->
    <circle cx="356" cy="210" r="2.5" fill="#58a6ff" opacity="0.5"/>

    <!-- 📄 GROUNDING.md -->
    <g transform="translate(110,228)">
      <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <line x1="2.5" y1="7" x2="8.5" y2="7" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
      <line x1="2.5" y1="9.5" x2="7" y2="9.5" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
    </g>
    <text x="128" y="240" class="ui" font-size="12.5" fill="#c9d1d9">GROUNDING.md</text>

    <!-- 📄 current.md -->
    <g transform="translate(110,254)">
      <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <line x1="2.5" y1="7" x2="8.5" y2="7" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
      <line x1="2.5" y1="9.5" x2="7" y2="9.5" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
    </g>
    <text x="128" y="266" class="ui" font-size="12.5" fill="#c9d1d9">current.md</text>

    <!-- 📄 worklog.md -->
    <g transform="translate(110,280)">
      <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#58a6ff" stroke-width="0.85" opacity="0.6"/>
      <line x1="2.5" y1="7" x2="8.5" y2="7" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
      <line x1="2.5" y1="9.5" x2="7" y2="9.5" stroke="#58a6ff" stroke-width="0.6" opacity="0.3"/>
    </g>
    <text x="128" y="292" class="ui" font-size="12.5" fill="#c9d1d9">worklog.md</text>

    <!-- 📁 components (dimmed) -->
    <g opacity="0.32">
      <g transform="translate(90,318)">
        <rect x="0" y="3" width="14" height="10" rx="1.5" fill="#8b949e"/>
        <rect x="0" y="1" width="6" height="4" rx="1" fill="#8b949e"/>
      </g>
      <text x="112" y="329" class="ui" font-size="13" fill="#c9d1d9">components</text>
    </g>

    <!-- 📄 package.json (dimmed) -->
    <g opacity="0.32">
      <g transform="translate(90,344)">
        <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#8b949e" stroke-width="0.8"/>
        <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#8b949e" stroke-width="0.8"/>
      </g>
      <text x="112" y="356" class="ui" font-size="13" fill="#c9d1d9">package.json</text>
    </g>

    <!-- 📄 README.md (dimmed) -->
    <g opacity="0.32">
      <g transform="translate(90,370)">
        <path d="M0,1.5 Q0,0.5 1,0.5 L7.5,0.5 L11,4 L11,13.5 Q11,14.5 10,14.5 L1,14.5 Q0,14.5 0,13.5 Z" fill="none" stroke="#8b949e" stroke-width="0.8"/>
        <path d="M7.5,0.5 L7.5,4 L11,4" fill="none" stroke="#8b949e" stroke-width="0.8"/>
      </g>
      <text x="112" y="382" class="ui" font-size="13" fill="#c9d1d9">README.md</text>
    </g>

    <!-- Mini scrollbar track -->
    <rect x="364" y="80" width="4" height="518" rx="2" fill="#21262d" opacity="0.25"/>
    <rect x="364" y="115" width="4" height="90" rx="2" fill="#484f58" opacity="0.25"/>


    <!-- ════════════════ DIVIDER ════════════════ -->
    <line x1="370" y1="80" x2="370" y2="598" stroke="#30363d" stroke-width="1"/>


    <!-- ════════════════ RIGHT PANE ════════════════ -->
    <rect x="370" y="80" width="770" height="518" fill="#161b22"/>

    <!-- Chat Header Bar -->
    <rect x="370" y="80" width="770" height="38" fill="#1c2128"/>
    <line x1="370" y1="118" x2="1140" y2="118" stroke="#30363d" stroke-width="0.5"/>

    <!-- AI sparkle icon in header -->
    <g transform="translate(390,92)">
      <path d="M7,0 L8.3,5 L13,6.5 L8.3,8 L7,13 L5.7,8 L1,6.5 L5.7,5 Z" fill="#bc8cff" opacity="0.9"/>
      <path d="M11,1 L11.4,3.2 L13.5,3.5 L11.4,3.8 L11,6 L10.6,3.8 L8.5,3.5 L10.6,3.2 Z" fill="#bc8cff" opacity="0.5"/>
    </g>
    <text x="412" y="104" class="ui" font-size="13" font-weight="600" fill="#e6edf3">AI Chat</text>
    <text x="468" y="104" class="ui" font-size="11" fill="#30363d">│</text>
    <text x="480" y="104" class="ui" font-size="11.5" fill="#8b949e">agent-assistant</text>

    <!-- Active status pill -->
    <rect x="586" y="93" width="50" height="18" rx="9" fill="#0d1117" opacity="0.5"/>
    <circle cx="598" cy="102" r="3" fill="#3fb950"/>
    <text x="606" y="106" class="ui" font-size="10" font-weight="500" fill="#3fb950" opacity="0.85">active</text>

    <!-- Model badge -->
    <rect x="1088" y="93" width="42" height="18" rx="5" fill="#21262d" opacity="0.6"/>
    <text x="1109" y="106" text-anchor="middle" class="ui" font-size="9.5" font-weight="500" fill="#8b949e">4o</text>


    <!-- ════════════════ CHAT BUBBLES ════════════════ -->

    <!-- ── User Bubble (right-aligned) ── -->
    <rect x="752" y="140" width="350" height="54" rx="14" fill="url(#userGrad)"/>
    <rect x="752" y="140" width="350" height="54" rx="14" fill="none" stroke="#2ea043" stroke-width="0.5" opacity="0.2"/>

    <!-- User avatar -->
    <circle cx="1084" cy="155" r="9" fill="#238636" opacity="0.35"/>
    <text x="1084" y="159" text-anchor="middle" class="ui" font-size="10" font-weight="700" fill="#3fb950" opacity="0.9">U</text>

    <!-- User message -->
    <text x="1075" y="178" text-anchor="end" class="ui" font-size="13.5" font-weight="400" fill="#e6edf3">Add a date picker to the booking form.</text>

    <!-- Timestamp -->
    <text x="752" y="206" class="ui" font-size="9.5" fill="#484f58" opacity="0.7">2:34 PM</text>


    <!-- ── Interception indicator ── -->
    <rect x="398" y="214" width="180" height="20" rx="5" fill="#1a2744" opacity="0.15"/>
    <circle cx="410" cy="224" r="3" fill="#58a6ff" opacity="0.6">
      <animate attributeName="opacity" values="0.6;0.2;0.6" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="420" y="228" class="ui" font-size="9.5" font-weight="500" fill="#58a6ff" opacity="0.7">.agents intercept</text>


    <!-- ── System Bubble (left-aligned, terminal) ── -->
    <rect x="398" y="242" width="540" height="48" rx="8" fill="#0d1117"/>
    <rect x="398" y="242" width="540" height="48" rx="8" fill="none" stroke="#1a2744" stroke-width="1"/>

    <!-- Terminal header -->
    <circle cx="414" cy="256" r="2.5" fill="#ff5f57" opacity="0.4"/>
    <circle cx="424" cy="256" r="2.5" fill="#febc2e" opacity="0.4"/>
    <circle cx="434" cy="256" r="2.5" fill="#28c840" opacity="0.4"/>
    <text x="448" y="260" class="ui" font-size="9" fill="#484f58">.agents/rules</text>

    <!-- Terminal prompt & message -->
    <text x="414" y="278" class="code" font-size="12" fill="#3fb950" opacity="0.75">❯</text>
    <text x="430" y="278" class="code" font-size="12" fill="#58a6ff" filter="url(#txtGlow)">Reading .agents/rules/IDENTITY.md...</text>

    <!-- Loaded badge -->
    <rect x="830" y="264" width="92" height="20" rx="6" fill="#0d1117" stroke="#1a2744" stroke-width="0.6"/>
    <circle cx="845" cy="274" r="3" fill="#3fb950" opacity="0.85"/>
    <text x="854" y="278" class="ui" font-size="9.5" font-weight="500" fill="#8b949e">LOADED</text>


    <!-- ── Agent Bubble (left-aligned) ── -->
    <rect x="398" y="308" width="600" height="108" rx="14" fill="#21262d"/>
    <rect x="398" y="308" width="600" height="108" rx="14" fill="none" stroke="#30363d" stroke-width="0.5"/>

    <!-- AI Sparkle Icon (larger, more prominent) -->
    <g transform="translate(412,320)">
      <path d="M8,0 L9.5,5.5 L15,7.5 L9.5,9.5 L8,15 L6.5,9.5 L1,7.5 L6.5,5.5 Z" fill="#bc8cff" opacity="0.85"/>
      <path d="M13,1 L13.5,3.5 L16,4 L13.5,4.5 L13,7 L12.5,4.5 L10,4 L12.5,3.5 Z" fill="#bc8cff" opacity="0.5"/>
    </g>

    <!-- Agent label & timestamp -->
    <text x="436" y="333" class="ui" font-size="10.5" font-weight="600" fill="#bc8cff" opacity="0.85">AGENT</text>
    <text x="482" y="333" class="ui" font-size="10.5" fill="#484f58">· just now</text>

    <!-- Agent message - Line 1 -->
    <text x="416" y="356" class="ui" font-size="13.5" fill="#e6edf3">
      <tspan>Rule found: </tspan>
      <tspan fill="#f0883e" font-weight="500">'No custom date pickers — native</tspan>
    </text>

    <!-- Line 2 -->
    <text x="416" y="376" class="ui" font-size="13.5" fill="#e6edf3">
      <tspan fill="#f0883e" font-weight="500">HTML input only.'</tspan>
      <tspan fill="#e6edf3"> I will add a native HTML</tspan>
    </text>

    <!-- Line 3 with syntax-highlighted code -->
    <text x="416" y="396" class="code" font-size="12.5">
      <tspan fill="#8b949e">&lt;</tspan>
      <tspan fill="#79c0ff">input</tspan>
      <tspan fill="#c9d1d9"> </tspan>
      <tspan fill="#79c0ff">type</tspan>
      <tspan fill="#ff7b72">=</tspan>
      <tspan fill="#a5d6ff">'date'</tspan>
      <tspan fill="#8b949e">&gt;</tspan>
    </text>
    <text x="500" y="396" class="ui" font-size="13.5" fill="#e6edf3"> to the form.</text>

    <!-- Success check icon -->
    <circle cx="988" cy="360" r="10" fill="#0d1117" opacity="0.4"/>
    <path d="M983,360 L986,363 L993,356" fill="none" stroke="#3fb950" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" opacity="0.7"/>


    <!-- ════════════════ CHAT INPUT ════════════════ -->
    <rect x="398" y="554" width="714" height="38" rx="10" fill="#0d1117" stroke="#30363d" stroke-width="0.8"/>

    <!-- Attach icon -->
    <circle cx="418" cy="573" r="6" fill="none" stroke="#484f58" stroke-width="1.2"/>
    <line x1="418" y1="569" x2="418" y2="577" stroke="#484f58" stroke-width="1.2"/>

    <!-- Placeholder text -->
    <text x="434" y="578" class="ui" font-size="13" fill="#484f58">Ask the agent...</text>

    <!-- Send button -->
    <rect x="1084" y="560" width="20" height="26" rx="7" fill="#238636" opacity="0.4"/>
    <path d="M1091,569 L1098,573 L1091,577 Z" fill="#e6edf3" opacity="0.6"/>

    <!-- Keyboard shortcut hint -->
    <rect x="1036" y="564" width="40" height="18" rx="4" fill="#21262d" opacity="0.4"/>
    <text x="1056" y="577" text-anchor="middle" class="ui" font-size="9" fill="#484f58">⌘↵</text>


    <!-- ════════════════ STATUS BAR ════════════════ -->
    <rect x="60" y="598" width="1080" height="20" fill="#1c2128"/>
    <line x1="60" y1="598" x2="1140" y2="598" stroke="#30363d" stroke-width="0.5"/>

    <!-- Status items (left) -->
    <text x="78" y="612" class="ui" font-size="10" fill="#8b949e">⎇ main</text>
    <text x="138" y="612" class="ui" font-size="10" fill="#3fb950" opacity="0.7">✓ 0</text>
    <text x="162" y="612" class="ui" font-size="10" fill="#f0883e" opacity="0.7">⚠ 0</text>

    <!-- Agent status -->
    <circle cx="208" cy="608" r="3.5" fill="#3fb950" opacity="0.8"/>
    <text x="216" y="612" class="ui" font-size="10" font-weight="500" fill="#3fb950" opacity="0.75">.agents active</text>

    <!-- Status items (right) -->
    <text x="1122" y="612" text-anchor="end" class="ui" font-size="10" fill="#8b949e">Ln 24, Col 1</text>
    <text x="1050" y="612" text-anchor="end" class="ui" font-size="10" fill="#8b949e">UTF-8</text>
    <text x="1000" y="612" text-anchor="end" class="ui" font-size="10" fill="#8b949e">TypeScript</text>

  </g>

  <!-- Final crisp window border -->
  <rect x="60" y="38" width="1080" height="580" rx="14" fill="none" stroke="#30363d" stroke-width="1"/>

  <!-- ════════════════ SUBTLE BRAND MARK ════════════════ -->
  <text x="1160" y="662" text-anchor="end" class="ui" font-size="9" fill="#21262d" letter-spacing="0.5">.agents</text>

</svg>"""

with open("assets/devos-architecture.svg", "w") as f:
    f.write(architecture_svg)

with open("assets/devos-hero.svg", "w") as f:
    f.write(hero_svg)

print("Saved new custom SVGs.")

# Update timestamps on all README files
timestamp = int(time.time())
for filename in glob.glob("README*.md"):
    with open(filename, "r") as f:
        content = f.read()

    # Re-apply cache buster query string
    content = re.sub(r"assets/devos-hero\.svg\?v=\d+", f"assets/devos-hero.svg?v={timestamp}", content)
    content = re.sub(r"assets/devos-architecture\.svg\?v=\d+", f"assets/devos-architecture.svg?v={timestamp}", content)

    # In case there were un-versioned links
    content = content.replace("assets/devos-hero.svg\"", f"assets/devos-hero.svg?v={timestamp}\"")
    content = content.replace("assets/devos-architecture.svg\"", f"assets/devos-architecture.svg?v={timestamp}\"")

    with open(filename, "w") as f:
        f.write(content)
    print(f"Updated cache buster in {filename}")

