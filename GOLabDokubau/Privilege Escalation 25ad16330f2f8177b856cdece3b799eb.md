# Privilege Escalation

Cypher_Query: MATCH p=(n)-[r:GenericAll]->(m) WHERE n.domain <> m.domain RETURN n.name, m.name, n.domain, m.domain LIMIT 10
Expected_Results: Cross-domain GenericAll relationships
GOAD_Specific: Yes
Hops_Count: 1
Query_Name: GenericAll Rights (Dangerous)
Risk_Level: Critical