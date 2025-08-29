# Kerberos Attack Targets

Cypher_Query: MATCH (u:User) WHERE u.hasspn=true RETURN u.name, u.serviceprincipalnames, u.domain
Expected_Results: jon.snow@NORTH.SEVENKINGDOMS.LOCAL (MSSQL SPN)
GOAD_Specific: Yes
Hops_Count: 1
Query_Name: Kerberoastable Service Accounts
Risk_Level: High