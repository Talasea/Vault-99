# GPO Abuse

Cypher_Query: MATCH p=(u:User)-[r:GenericWrite|WriteDacl]->(g:GPO) RETURN u.name, g.name, u.domain
Expected_Results: samwell.tarly → STARKWALLPAPER GPO
GOAD_Specific: Yes
Hops_Count: 1
Query_Name: GPO Write Access
Risk_Level: Critical