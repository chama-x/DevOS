# AgentOS: ස්වයං-පාලිත MAS රාමුව (Self-Governing MAS Framework)

![AgentOS Architecture](assets/CortanaAgentOS.jpg)

අලුත් IDE වල ප්‍රබල LLM ඒජන්තවරු (agents) හිටියත්, සාමාන්‍යයෙන් මේවා terminal එකට ප්‍රවේශය (access) තියෙන චැට්බොට්ලා (stateless chatbots) පමණයි. මොවුන්ට ගොඩක් වෙලාවට වැරදි කේත (code) එක දිගට වෙනස් කරන්න ගිහින් ගැටළු ඇතිවෙන (Idempotency Neglect) අවස්ථා වගේම, මතකය පිරිලා හිරවෙන (context bloat) ප්‍රශ්න එනවා. ඒ වගේම කුඩා මතකයක් ඇතුළේ ලොකු දේවල් කරන්න ගිහින් අසාර්ථක වෙන අවස්ථා (God Model syndrome) තියෙනවා.

අපි මේකට විසඳුමක් විදිහට IDE ඒජන්තයාට උඩින් වැඩ කරන **විශේෂිත AgentOS සන්දර්භ රාමුවක් (Custom AgentOS Context Framework)** හැදුවා. අලුත් ඒජන්තයෙක් මේ පරිසරයට ආපු ගමන්, අපේ දේශීය වින්‍යාස ගොනු (local configuration files) හරහා එයා ක්ෂණිකව **ස්වයං-පාලනයක් සහිත, අවදානම් කළමනාකරණය කරන අධීක්ෂකයෙක් (Self-Governing, Risk-Tiered Supervisor)** බවට පත්වෙනවා.

## ප්‍රධාන පහසුකම් (Core Features)

### 1. අවදානම් මට්ටම් අනුව පාලනය (Risk-Tiered Autonomy)
සාමාන්‍ය ඒජන්තවරු හැම වැඩක්ම එකම විදිහට දැක්කට, අපේ AgentOS එකේ දැඩි මට්ටම් 4ක පාලන පද්ධතියක් (4-Tier Autonomy system) තියෙනවා:
- **T0**: කේත කියවීම, සෙවීම, සහ වැරදි බැලීම (linting) - මේවා එයාට තනියම කරගෙන යන්න පුළුවන් (Auto-Proceed).
- **T1**: තනි ගොනුවක් (single-file) වෙනස් කිරීම - මේකටත් අවසර තියෙනවා, හැබැයි මුලින්ම `git commit` එකක් දාලා (checkpoint) ඉන්න ඕනේ.
- **T2**: ගොනු කිහිපයක් එකවර වෙනස් කිරීම (multi-file refactors) - මේකට කණ්ඩායම් වශයෙන් (batched) අවසර ගන්න ඕනේ.
- **T3**: කේත මකාදැමීම, පිටතින් කේත ඇතුල් කිරීම (external injection), සහ මුරපද (auth) වෙනස් කිරීම - මේවාට අනිවාර්යයෙන්ම පරිශීලකයෙකුගේ (Red Team Review) අවසරය ඕනෙමයි.

### 2. ආරක්ෂිතව කේත වෙනස් කිරීම (Idempotency & The Recovery Kernel)
කේතයක් වෙනස් කරන්න (mutation) කලින්, ඒ වෙනස කලින්ම වෙලාද කියලා ඒජන්තයා හොයලා බලනවා. කේතයේ තැනක් වෙනස් කරන්න ගිහින් (surgical text replacement) වැරදුනොත්, එයාට *එක්* පාරක් විතරක් ආයෙත් උත්සාහ කරන්න (retry) අවසර තියෙනවා. දෙවෙනි පාරත් වැරදුනොත් එයා වැඩේ නතර කරනවා. මේකෙන් එකම දේ දිගින් දිගටම කරලා (infinite execution loops) සිස්ටම් එක හිරවෙන එක නවතිනවා.

### 3. ආරක්ෂිත මතක සම්පීඩනය (Transactional Memory Compression)
ඒජන්තයාගේ මතකය (worklog.md) ටෝකන් 4,000 පැනපු ගමන්, එයා පියවර 5ක ආරක්ෂිත ක්‍රියාවලියක් (transactional 5-step loop) කරනවා: සාරාංශ කිරීම (Distill) → ගබඩා කිරීම (Append) → හරිද බැලීම (Verify) → පරණ ඒවා මැකීම (Truncate) → සේව් කිරීම (Commit). මේ නිසා LLM එක හිරවුණත් ඔයාගේ දත්ත නැතිවෙන්නේ නෑ (context data loss) කියලා සහතික කරනවා.

### 4. බර වැඩ වෙනත් අයට දීම (Frontier Delegation - Supervisor/Worker MAS)
කාර්යයක් ගොඩක් ලොකු නම් (ටෝකන් 40k+), OS එකෙන් වෙනම පැකේජයක් (handoff packet) හදනවා. ඒජන්තයා ඔයාගේ රහස්‍ය දත්ත (secrets) සහ API යතුරු අයින් කරලා, මේ වැඩේ පිටතින් ඉන්න වෙනත් AI මොඩල් එකකට (Frontier Model) දෙනවා. ඒ මොඩල් එකෙන් කේතය හදලා දුන්නම, ඒක වෙනස් නොකරම ගෙනල්ලා (injected verbatim), වැරදි බලලා (statically analyzed), ඔයාට `git diff` එකක් විදිහට පෙන්නනවා (T3 Review).

### 5. පද්ධතියේ ආරක්ෂාව (Constitutional Lock & OS Scaffolding)
ඒජන්තයාට තමන්ගේම නීති (guardrails) වෙනස් කරන්න බෑ. `.agents/rules/` ෆෝල්ඩරයේ කරන ඕනෑම වෙනස්කමක් **T3 ක්‍රියාවක්** විදිහටයි සලකන්නේ. ඒ වගේම, මුලින්ම වැඩක් පටන්ගන්නකොට අවශ්‍ය ෆයිල්ස් (core files) අඩු නම්, ඒජන්තයා ඔයාගෙන් අහලා (multi-select questionnaire) ඒ ටික ස්වයංක්‍රීයව හදලා දෙනවා (scaffold).

## ස්ථාපනය කරගන්නා ආකාරය (Installation)
ඔයාගේ ප්‍රොජෙක්ට් එකේ ප්‍රධාන ෆෝල්ඩරයට (root) `.agents` ෆෝල්ඩරය දාන්න විතරයි තියෙන්නේ. එතකොට ඔයාගේ ඒජන්තයා ක්ෂණිකව V2 Supervisor කෙනෙක් බවට පත්වෙයි!
