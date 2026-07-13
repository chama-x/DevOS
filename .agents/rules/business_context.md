---
trigger: always_on
---
<knowledge_graph_framework>
  <project_name>Business Context & Routing</project_name>

  <organization_profile>
    <company>[Company Name]</company>
    <core_business>[Describe the business]</core_business>
    <key_personnel>
      <person name="[Name]" role="[Role]" />
    </key_personnel>
  </organization_profile>

  <methodology name="joint_brain">
    <description>
      We are modeling this business not as flat files, but as an Enterprise Knowledge Graph (Spider Web Map).
      To maintain high accuracy without hallucinations, you must strictly map and query data using this vocabulary:
    </description>
    
    <core_pillars>
      <pillar name="[Pillar 1]">[Description]</pillar>
      <pillar name="[Pillar 2]">[Description]</pillar>
    </core_pillars>

    <entity_types>
      <entity type="user">[Description]</entity>
      <entity type="system">[Description]</entity>
    </entity_types>

    <edge_types>
      <edge type="manages">Person to System</edge>
      <edge type="flows_to">Data flowing from one service to another</edge>
    </edge_types>

    <domain_rules>
      <rule>Never assume data is clean or perfectly structured. Always think in terms of the Knowledge Graph (Who + What + How) before touching the codebase.</rule>
      <rule>Always rely on fuzzy matching and robust error handling when building data extraction pipelines.</rule>
    </domain_rules>
  </methodology>

  <technology_stack_mandates>
    <rule type="negative_constraint" category="dependencies">
      DO NOT use npm or yarn. pnpm is the permanently mandated package manager. Next.js is the mandated web application framework (do not default to standard React or Vite for web apps).
    </rule>
  </technology_stack_mandates>
</knowledge_graph_framework>
