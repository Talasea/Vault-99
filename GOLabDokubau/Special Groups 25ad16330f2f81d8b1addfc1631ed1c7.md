# Special Groups

Cypher_Query: MATCH (g:Group) WHERE g.name CONTAINS "ACROSS" OR g.name CONTAINS "DRAGONS" OR g.name CONTAINS "SPYS" RETURN g.name, g.domain
Expected_Results: AcrossTheSea, DragonsFriends, Spys groups
GOAD_Specific: Yes
Hops_Count: 2-3
Query_Name: Cross-Forest Groups
Risk_Level: High