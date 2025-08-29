# Cross-Domain Attacks

Cypher_Query: MATCH (d1:Domain)-[r:TrustedBy]->(d2:Domain) RETURN d1.name, type(r), d2.name
Expected_Results: sevenkingdoms.local ↔ essos.local trust relationships
GOAD_Specific: Yes
Hops_Count: Variable
Query_Name: Cross-Forest Trusts
Risk_Level: High