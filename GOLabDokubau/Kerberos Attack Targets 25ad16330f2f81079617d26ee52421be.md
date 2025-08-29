# Kerberos Attack Targets

Cypher_Query: MATCH (u:User) WHERE u.dontreqpreauth=true RETURN u.name, u.domain, u.description
Expected_Results: brandon.stark@NORTH.SEVENKINGDOMS.LOCAL, missandei@ESSOS.LOCAL
GOAD_Specific: Yes
Hops_Count: 1
Query_Name: ASREPRoastable Users
Risk_Level: High