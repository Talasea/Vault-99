# Privilege Escalation

Cypher_Query: MATCH (c:Computer) WHERE c.unconstraineddelegation=true RETURN c.name, c.domain
Expected_Results: sansa.stark computer account (if applicable)
GOAD_Specific: Yes
Hops_Count: 1
Query_Name: Unconstrained Delegation
Risk_Level: Critical