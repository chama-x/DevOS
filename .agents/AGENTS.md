---
trigger: always_on
---

<skill_calibration source="SkillsBench (arXiv:2602.12670)">
  <description>Calibrate how hard to search for / trust a Skill before starting a task, based on empirical measurement rather than instinct.</description>
  
  <rule id="CAL-1" name="DOMAIN_PRIORITY">
    <description>Search effort must scale with empirical domain deltas. The less a domain resembles common software engineering, the harder you search.</description>
    <tier level="1" domains="Healthcare, Manufacturing">Do not proceed on baseline knowledge alone. Actively search for a curated skill before attempting.</tier>
    <tier level="2" domains="Cybersecurity, Natural Science, Energy, Office">Worth a genuine search pass, not just a cursory check.</tier>
    <tier level="3" domains="Finance, Media">Search if easy to find; don't burn much budget hunting.</tier>
    <tier level="4" domains="Robotics, Mathematics, Software Engineering">Baseline knowledge is adequate. Don't spend cycles hunting.</tier>
  </rule>

  <rule id="CAL-2" name="NO_FABRICATION">
    <description>If you can't find a real curated skill, say so and proceed on direct reasoning. Do NOT fabricate a pseudo-skill mid-task (measurably worse than no skill).</description>
  </rule>

  <rule id="CAL-3" name="SKILL_LIMIT">
    <description>When multiple skills seem relevant, select the 2-3 most directly applicable. Stacking 4+ skills measurably hurts performance due to cognitive overhead.</description>
  </rule>

  <rule id="CAL-4" name="PREFER_CONCRETE">
    <description>Prefer lean, concrete skills (with steps and examples) over exhaustive reference-manual style bundles.</description>
  </rule>

  <rule id="CAL-5" name="REDUNDANCY_CHECK">
    <description>If a task sits inside well-documented territory and a skill looks generic or contradicts known patterns, weight it cautiously. Skills can hurt.</description>
  </rule>

  <rule id="CAL-6" name="VERIFY_APPLICATION">
    <description>After selecting a skill, verify your own output actually reflects its specific guidance (exact values, named methods, cited conventions).</description>
  </rule>
</skill_calibration>
