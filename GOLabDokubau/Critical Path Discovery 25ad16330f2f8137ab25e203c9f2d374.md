# Critical Path Discovery

Cypher_Query: MATCH (u:User {name:"HODOR@NORTH.SEVENKINGDOMS.LOCAL"}), (g:Group) WHERE g.name CONTAINS "DOMAIN ADMINS" MATCH p=shortestPath((u)-[*1..]->(g)) RETURN p
Expected_Results: Direct path via password reuse or GPO abuse
GOAD_Specific: Yes
Hops_Count: 1-2
Query_Name: Shortest Path to Domain Admin (hodor)
Risk_Level: Critical