root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# dig ANY sevenkingdoms.local @192.168.20.10

; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> ANY sevenkingdoms.local @192.168.20.10
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53651
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;sevenkingdoms.local.		IN	ANY

;; ANSWER SECTION:
sevenkingdoms.local.	600	IN	A	192.168.20.10
sevenkingdoms.local.	3600	IN	NS	kingslanding.sevenkingdoms.local.
sevenkingdoms.local.	3600	IN	SOA	kingslanding.sevenkingdoms.local. hostmaster.sevenkingdoms.local. 297 900 600 86400 3600

;; ADDITIONAL SECTION:
kingslanding.sevenkingdoms.local. 3600 IN A	192.168.20.10

;; Query time: 20 msec
;; SERVER: 192.168.20.10#53(192.168.20.10) (TCP)
;; WHEN: Mon Aug 25 11:26:52 CEST 2025
;; MSG SIZE  rcvd: 154



(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# dnsrecon -d sevenkingdoms.local -t brt -D /home/tala/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
[*] Using the dictionary file: /home/tala/SecLists/Discovery/DNS/subdomains-top1million-110000.txt (provided by user)
[*] brt: Performing host and subdomain brute force against sevenkingdoms.local...
[+] 0 Records Found
(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# dig ANY sevenkingdoms.local @192.168.20.10

; <<>> DiG 9.18.30-0ubuntu0.24.04.2-Ubuntu <<>> ANY sevenkingdoms.local @192.168.20.10
;; global options: +cmd
;; Got answer:
;; WARNING: .local is reserved for Multicast DNS
;; You are currently testing what happens when an mDNS query is leaked to DNS
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 53651
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 2

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;sevenkingdoms.local.           IN      ANY

;; ANSWER SECTION:
sevenkingdoms.local.    600     IN      A       192.168.20.10
sevenkingdoms.local.    3600    IN      NS      kingslanding.sevenkingdoms.local.
sevenkingdoms.local.    3600    IN      SOA     kingslanding.sevenkingdoms.local. hostmaster.s



(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# # Detaillierte LDAP-Enumeration mit ldapsearch
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName description

# Nach Service Principal Names suchen
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "servicePrincipalName=*" servicePrincipalName sAMAccountName

# Gruppen-Enumeration
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=group)" sAMAccountName member description

# Computer-Accounts finden
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=computer)" sAMAccountName operatingSystem

# Domain Policy abfragen
ldapsearch -x -H ldap://192.168.20.10 -s base -b "DC=sevenkingdoms,DC=local" "(objectClass=*)" lockoutThreshold lockoutDuration maxPwdAge
# extended LDIF
#
# LDAPv3
# base <DC=sevenkingdoms,DC=local> with scope subtree
# filter: (objectClass=user)
# requesting: sAMAccountName userPrincipalName description 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4563

# numResponses: 1
# extended LDIF
#
# LDAPv3
# base <DC=sevenkingdoms,DC=local> with scope subtree
# filter: servicePrincipalName=*
# requesting: servicePrincipalName sAMAccountName 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4563

# numResponses: 1
# extended LDIF
#
# LDAPv3
# base <DC=sevenkingdoms,DC=local> with scope subtree
# filter: (objectClass=group)
# requesting: sAMAccountName member description 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4563

# numResponses: 1
# extended LDIF
#
# LDAPv3
# base <DC=sevenkingdoms,DC=local> with scope subtree
# filter: (objectClass=computer)
# requesting: sAMAccountName operatingSystem 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4563

# numResponses: 1
# extended LDIF
#
# LDAPv3
# base <DC=sevenkingdoms,DC=local> with scope baseObject
# filter: (objectClass=*)
# requesting: lockoutThreshold lockoutDuration maxPwdAge 
#

# search result
search: 2
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this opera
 tion a successful bind must be completed on the connection., data 0, v4563



root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# enum4linux -U 192.168.20.10  # Nur User-Enumeration
enum4linux -G 192.168.20.10  # Nur Gruppen-Enumeration
enum4linux -S 192.168.20.10  # Nur Share-Enumeration
enum4linux -P 192.168.20.10  # Password Policy
enum4linux -o 192.168.20.10  # OS Information
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:51:39 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 =======================================( Users on 192.168.20.10 )=======================================


[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED



[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED

enum4linux complete on Mon Aug 25 11:51:50 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:51:51 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ======================================( Groups on 192.168.20.10 )======================================


[+] Getting builtin groups:


[+]  Getting builtin group memberships:


[+]  Getting local groups:


[+]  Getting local group memberships:


[+]  Getting domain groups:


[+]  Getting domain group memberships:

enum4linux complete on Mon Aug 25 11:52:02 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:52:02 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 =================================( Share Enumeration on 192.168.20.10 )=================================

do_connect: Connection to 192.168.20.10 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 192.168.20.10

enum4linux complete on Mon Aug 25 11:52:13 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:52:13 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ===========================( Password Policy Information for 192.168.20.10 )===========================


[E] Unexpected error from polenum:



[+] Attaching to 192.168.20.10 using a NULL share

[+] Trying protocol 139/SMB...

	[!] Protocol failed: Cannot request session (Called Name:192.168.20.10)

[+] Trying protocol 445/SMB...

	[!] Protocol failed: SAMR SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.



[E] Failed to get password policy with rpcclient


enum4linux complete on Mon Aug 25 11:52:24 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:52:24 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ==================================( OS information on 192.168.20.10 )==================================


[E] Can't get OS info with smbclient


[+] Got OS info for 192.168.20.10 from srvinfo: 
do_cmd: Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED

enum4linux complete on Mon Aug 25 11:52:35 2025




(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# # Vollständige enum4linux-Scans auf alle Hosts
enum4linux -a 192.168.20.10 > enum4linux_dc01.txt
enum4linux -a 192.168.20.11 > enum4linux_dc02.txt  
enum4linux -a 192.168.20.12 > enum4linux_dc03.txt
enum4linux -a 192.168.20.22 > enum4linux_sql01.txt
enum4linux -a 192.168.20.23 > enum4linux_sql02.txt

# Spezifische enum4linux-Optionen
enum4linux -U 192.168.20.10  # Nur User-Enumeration
enum4linux -G 192.168.20.10  # Nur Gruppen-Enumeration
enum4linux -S 192.168.20.10  # Nur Share-Enumeration
enum4linux -P 192.168.20.10  # Password Policy
enum4linux -o 192.168.20.10  # OS Information
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:53:19 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 =======================================( Users on 192.168.20.10 )=======================================


[E] Couldn't find users using querydispinfo: NT_STATUS_ACCESS_DENIED



[E] Couldn't find users using enumdomusers: NT_STATUS_ACCESS_DENIED

enum4linux complete on Mon Aug 25 11:53:30 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:53:30 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ======================================( Groups on 192.168.20.10 )======================================


[+] Getting builtin groups:


[+]  Getting builtin group memberships:


[+]  Getting local groups:


[+]  Getting local group memberships:


[+]  Getting domain groups:


[+]  Getting domain group memberships:

enum4linux complete on Mon Aug 25 11:53:41 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:53:42 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 =================================( Share Enumeration on 192.168.20.10 )=================================

do_connect: Connection to 192.168.20.10 failed (Error NT_STATUS_RESOURCE_NAME_NOT_FOUND)

	Sharename       Type      Comment
	---------       ----      -------
Reconnecting with SMB1 for workgroup listing.
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 192.168.20.10

enum4linux complete on Mon Aug 25 11:53:52 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:53:52 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ===========================( Password Policy Information for 192.168.20.10 )===========================


[E] Unexpected error from polenum:



[+] Attaching to 192.168.20.10 using a NULL share

[+] Trying protocol 139/SMB...

	[!] Protocol failed: Cannot request session (Called Name:192.168.20.10)

[+] Trying protocol 445/SMB...

	[!] Protocol failed: SAMR SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.



[E] Failed to get password policy with rpcclient


enum4linux complete on Mon Aug 25 11:54:04 2025

"my" variable $which_output masks earlier declaration in same scope at ./enum4linux.pl line 280.
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Mon Aug 25 11:54:04 2025

 =========================================( Target Information )=========================================

Target ........... 192.168.20.10
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.20.10 )===========================


[E] Can't find workgroup/domain



 ===================================( Session Check on 192.168.20.10 )===================================


[+] Server 192.168.20.10 allows sessions using username '', password ''


 ================================( Getting domain SID for 192.168.20.10 )================================

Domain Name: SEVENKINGDOMS
Domain Sid: S-1-5-21-2535930937-3240925528-3053620292

[+] Host is part of a domain (not a workgroup)


 ==================================( OS information on 192.168.20.10 )==================================


[E] Can't get OS info with smbclient


[+] Got OS info for 192.168.20.10 from srvinfo: 
do_cmd: Could not initialise srvsvc. Error was NT_STATUS_ACCESS_DENIED

enum4linux complete on Mon Aug 25 11:54:15 2025



root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# smbclient -L //192.168.20.23 -N
smbclient //192.168.20.23/all -N
smbclient //192.168.20.23/public -N
smbclient //192.168.20.23/CertEnroll -N

# SMBMap für Berechtigungsanalyse  
smbmap -H 192.168.20.23 -u null -p ""
smbmap -H 192.168.20.23 -R --depth 3

# CrackMapExec für umfassende SMB-Enumeration
crackmapexec smb 192.168.20.0/24 --shares
crackmapexec smb 192.168.20.0/24 --users
crackmapexec smb 192.168.20.0/24 --groups  
crackmapexec smb 192.168.20.0/24 --local-users
crackmapexec smb 192.168.20.0/24 --rid-brute
crackmapexec smb 192.168.20.0/24 --sessions

	Sharename       Type      Comment
	---------       ----      -------
	ADMIN$          Disk      Remote Admin
	all             Disk      Basic RW share for all
	C$              Disk      Default share
	CertEnroll      Disk      Active Directory Certificate Services share
	IPC$            IPC       Remote IPC
	public          Disk      Basic Read share for all domain users
SMB1 disabled -- no workgroup available
Try "help" to get a list of possible commands.
smb: \> smbmap -H 192.168.20.23 -u null -p ""
smbmap -H 192.168.20.23 -R --depth 3
smbmap: command not found
smb: \> clear
clear: command not found
smb: \> clear
clear: command not found
smb: \> exit
Try "help" to get a list of possible commands.
smb: \> clear
clear: command not found
smb: \> exit
Try "help" to get a list of possible commands.
smb: \> ^C
Der Befehl 'smbmap' wurde nicht gefunden, kann aber installiert werden mit:
apt install smbmap
Der Befehl 'smbmap' wurde nicht gefunden, kann aber installiert werden mit:
apt install smbmap
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [-] Error getting user: list index out of range
SMB         192.168.20.10   445    KINGSLANDING     [-] Error getting user: list index out of range
SMB         192.168.20.12   445    MEEREEN          [-] Error getting user: list index out of range
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [-] Error enumerating shares: [Errno 32] Broken pipe
SMB         192.168.20.11   445    WINTERFELL       [-] Error getting user: list index out of range
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [-] Error getting user: list index out of range
SMB         192.168.20.22   445    CASTELBLACK      [-] Error enumerating shares: [Errno 32] Broken pipe
SMB         192.168.20.10   445    KINGSLANDING     [-] Error enumerating shares: STATUS_USER_SESSION_DELETED
SMB         192.168.20.12   445    MEEREEN          [-] Error enumerating shares: Could not get nt error code 91 from impacket: SMB SessionError: 0x5b
SMB         192.168.20.11   445    WINTERFELL       [-] Error enumerating shares: STATUS_USER_SESSION_DELETED
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.23   445    BRAAVOS          [*] Trying to dump local users with SAMRPC protocol
SMB         192.168.20.12   445    MEEREEN          [*] Trying to dump local users with SAMRPC protocol
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [*] Trying to dump local users with SAMRPC protocol
SMB         192.168.20.10   445    KINGSLANDING     [*] Trying to dump local users with SAMRPC protocol
SMB         192.168.20.11   445    WINTERFELL       [*] Trying to dump local users with SAMRPC protocol
SMB         192.168.20.11   445    WINTERFELL       [+] Enumerated domain user(s)
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\Guest                          Built-in account for guest access to the computer/domain
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\arya.stark                     Arya Stark
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\sansa.stark                    Sansa Stark
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\brandon.stark                  Brandon Stark
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\rickon.stark                   Rickon Stark
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\hodor                          Brainless Giant
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\jon.snow                       Jon Snow
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\samwell.tarly                  Samwell Tarly (Password : Heartsbane)
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\jeor.mormont                   Jeor Mormont
SMB         192.168.20.11   445    WINTERFELL       north.sevenkingdoms.local\sql_svc                        sql service
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [-] Error enumerating domain group using dc ip 192.168.20.22: SMB SessionError: STATUS_ACCESS_DENIED({Access Denied} A process has requested access to an object but has not been granted those access rights.)
SMB         192.168.20.23   445    BRAAVOS          [-] Error enumerating domain group using dc ip 192.168.20.23: SMB SessionError: STATUS_ACCESS_DENIED({Access Denied} A process has requested access to an object but has not been granted those access rights.)
SMB         192.168.20.10   445    KINGSLANDING     [-] Error enumerating domain group using dc ip 192.168.20.10: NTLM needs domain\username and a password
SMB         192.168.20.12   445    MEEREEN          [-] Error enumerating domain group using dc ip 192.168.20.12: NTLM needs domain\username and a password
SMB         192.168.20.11   445    WINTERFELL       [-] Error enumerating domain group using dc ip 192.168.20.11: NTLM needs domain\username and a password
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
usage: crackmapexec [-h] [-t THREADS] [--timeout TIMEOUT] [--jitter INTERVAL]
                    [--no-progress] [--verbose] [--debug] [--version]
                    {ftp,ldap,mssql,rdp,smb,ssh,vnc,winrm,wmi} ...
crackmapexec: error: unrecognized arguments: --local-users
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
SMB         192.168.20.22   445    CASTELBLACK      [-] Error creating DCERPC connection: SMB SessionError: STATUS_ACCESS_DENIED({Access Denied} A process has requested access to an object but has not been granted those access rights.)
SMB         192.168.20.23   445    BRAAVOS          [-] Error creating DCERPC connection: SMB SessionError: STATUS_ACCESS_DENIED({Access Denied} A process has requested access to an object but has not been granted those access rights.)
SMB         192.168.20.10   445    KINGSLANDING     [-] Error connecting: LSAD SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.
SMB         192.168.20.12   445    MEEREEN          [-] Error connecting: LSAD SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.
SMB         192.168.20.11   445    WINTERFELL       [-] Error connecting: LSAD SessionError: code: 0xc0000022 - STATUS_ACCESS_DENIED - {Access Denied} A process has requested access to an object but has not been granted those access rights.
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
SMB         192.168.20.11   445    WINTERFELL       [*] Windows 10.0 Build 17763 x64 (name:WINTERFELL) (domain:north.sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.10   445    KINGSLANDING     [*] Windows 10.0 Build 17763 x64 (name:KINGSLANDING) (domain:sevenkingdoms.local) (signing:True) (SMBv1:False)
SMB         192.168.20.22   445    CASTELBLACK      [*] Windows 10.0 Build 17763 x64 (name:CASTELBLACK) (domain:north.sevenkingdoms.local) (signing:False) (SMBv1:False)
SMB         192.168.20.23   445    BRAAVOS          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:BRAAVOS) (domain:essos.local) (signing:False) (SMBv1:True)
SMB         192.168.20.12   445    MEEREEN          [*] Windows Server 2016 Standard Evaluation 14393 x64 (name:MEEREEN) (domain:essos.local) (signing:True) (SMBv1:True)
Running CME against 256 targets ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# # Nmap SQL-Scripts mit Debug-Informationen
nmap -p 1433 --script ms-sql-info,ms-sql-config,ms-sql-dump-hashes,ms-sql-empty-password,ms-sql-brute 192.168.20.22,23 -d

# Impacket mssqlclient für direkte Verbindung
impacket-mssqlclient -windows-auth guest@192.168.20.22
impacket-mssqlclient guest@192.168.20.23

# SQLMap für SQL-Injection-Tests (falls Web-Interface gefunden)
sqlmap -u "http://192.168.20.23/login.asp" --dbs --batch
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-08-25 12:06 CEST
--------------- Timing report ---------------
  hostgroups: min 1, max 100000
  rtt-timeouts: init 1000, min 100, max 10000
  max-scan-delay: TCP 1000, UDP 1000, SCTP 1000
  parallelism: min 0, max 0
  max-retries: 10, host-timeout: 0
  min-rate: 0, max-rate: 0
---------------------------------------------
NSE: Using Lua 5.4.
NSE: Arguments from CLI: 
NSE: Loaded 5 scripts for scanning.
NSE: Script Pre-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
Initiating Ping Scan at 12:06
Scanning 2 hosts [4 ports/host]
Packet capture filter (device tun0): dst host 10.2.0.6 and (icmp or icmp6 or ((tcp) and (src host 192.168.20.22 or src host 192.168.20.23)))
We got a ping packet back from 192.168.20.23: id = 17051 seq = 0 checksum = 48484
We got a ping packet back from 192.168.20.22: id = 8632 seq = 0 checksum = 56903
Completed Ping Scan at 12:06, 0.03s elapsed (2 total hosts)
Overall sending rates: 252.80 packets / s, 9606.27 bytes / s.
mass_rdns: Using DNS server 127.0.0.53
Initiating Parallel DNS resolution of 2 hosts. at 12:06
mass_rdns: 0.00s 0/2 [#: 1, OK: 0, NX: 0, DR: 0, SF: 0, TR: 2]
Completed Parallel DNS resolution of 2 hosts. at 12:06, 0.16s elapsed
DNS resolution of 2 IPs took 0.16s. Mode: Async [#: 1, OK: 2, NX: 0, DR: 0, SF: 0, TR: 2, CN: 0]
Initiating SYN Stealth Scan at 12:06
Scanning 2 hosts [1 port/host]
Packet capture filter (device tun0): dst host 10.2.0.6 and (icmp or icmp6 or ((tcp) and (src host 192.168.20.22 or src host 192.168.20.23)))
Discovered open port 1433/tcp on 192.168.20.23
Discovered open port 1433/tcp on 192.168.20.22
Completed SYN Stealth Scan at 12:06, 0.02s elapsed (2 total ports)
Overall sending rates: 80.84 packets / s, 3556.99 bytes / s.
NSE: Script scanning 2 hosts.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:06
NSE: [ms-sql-info 192.168.20.23:1433] brandedVersion: 2005, #lookup: 5
NSE: [ms-sql-info 192.168.20.22:1433] brandedVersion: 2005, #lookup: 5
NSE: [ms-sql-info 192.168.20.23:1433] brandedVersion: 2019, #lookup: 29
NSE: Starting ms-sql-info against 192.168.20.23:1433.
NSE: [ms-sql-info 192.168.20.22:1433] brandedVersion: 2019, #lookup: 29
NSE: Starting ms-sql-info against 192.168.20.22:1433.
NSE: Starting ms-sql-empty-password against 192.168.20.23:1433.
NSE: Starting ms-sql-empty-password against 192.168.20.22:1433.
NSE: ms-sql-info against 192.168.20.23:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: ms-sql-info against 192.168.20.22:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: ms-sql-empty-password against 192.168.20.23:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: ms-sql-empty-password against 192.168.20.22:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

Completed NSE at 12:06, 0.07s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:06
NSE: Starting ms-sql-brute against 192.168.20.22:1433.
NSE: ms-sql-brute against 192.168.20.22:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: Starting ms-sql-brute against 192.168.20.23:1433.
NSE: ms-sql-brute against 192.168.20.23:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:06
NSE: Starting ms-sql-dump-hashes against 192.168.20.23:1433.
NSE: ms-sql-dump-hashes against 192.168.20.23:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: Starting ms-sql-config against 192.168.20.23:1433.
NSE: ms-sql-config against 192.168.20.23:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: Starting ms-sql-dump-hashes against 192.168.20.22:1433.
NSE: ms-sql-dump-hashes against 192.168.20.22:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

NSE: Starting ms-sql-config against 192.168.20.22:1433.
NSE: ms-sql-config against 192.168.20.22:1433 threw an error!
attempt to index a nil value
stack traceback:
	[C]: in for iterator 'for iterator'
	/usr/bin/../share/nmap/nselib/mssql.lua:3334: in function </usr/bin/../share/nmap/nselib/mssql.lua:3327>
	(...tail calls...)

Completed NSE at 12:06, 0.00s elapsed
Nmap scan report for localhost (192.168.20.22)
Host is up, received echo-reply ttl 127 (0.018s latency).
Scanned at 2025-08-25 12:06:34 CEST for 0s

PORT     STATE SERVICE  REASON
1433/tcp open  ms-sql-s syn-ack ttl 127
Final times for host: srtt: 18402 rttvar: 14072  to: 100000

Nmap scan report for localhost (192.168.20.23)
Host is up, received echo-reply ttl 127 (0.018s latency).
Scanned at 2025-08-25 12:06:34 CEST for 0s

PORT     STATE SERVICE  REASON
1433/tcp open  ms-sql-s syn-ack ttl 127
Final times for host: srtt: 18323 rttvar: 14151  to: 100000

NSE: Script Post-scanning.
NSE: Starting runlevel 1 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 2 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
NSE: Starting runlevel 3 (of 3) scan.
Initiating NSE at 12:06
Completed NSE at 12:06, 0.00s elapsed
Read from /usr/bin/../share/nmap: nmap-protocols nmap-services.
Nmap done: 2 IP addresses (2 hosts up) scanned in 0.39 seconds
           Raw packets sent: 10 (392B) | Rcvd: 9 (828B)
impacket-mssqlclient: Befehl nicht gefunden.
impacket-mssqlclient: Befehl nicht gefunden.
        ___
       __H__
 ___ ___[']_____ ___ ___  {1.8.4#stable}
|_ -| . [']     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 12:06:34 /2025-08-25/

[12:06:34] [INFO] testing connection to the target URL
[12:06:34] [CRITICAL] page not found (404)
it is not recommended to continue in this kind of cases. Do you want to quit and make sure that everything is set up properly? [Y/n] Y
[12:06:34] [WARNING] HTTP error codes detected during run:
404 (Not Found) - 1 times
[12:06:34] [WARNING] your sqlmap version is outdated



(myenv) root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# # Nikto für Web-Vulnerability-Scanning
nikto -h http://192.168.20.23 -C all

# WhatWeb für Technology-Detection  
whatweb http://192.168.20.23 -v

# HTTProbe für HTTP-Service-Discovery
echo "192.168.20.23" | httprobe -p http:80,https:443,http:8080,https:8443
- Nikto v2.1.5
---------------------------------------------------------------------------
+ Target IP:          192.168.20.23
+ Target Hostname:    192.168.20.23
+ Target Port:        80
+ Start Time:         2025-08-25 12:04:14 (GMT2)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ Retrieved x-powered-by header: ASP.NET
+ Server leaks inodes via ETags, header found with file /, fields: 0x2efdd26194acdb1:0 
+ The anti-clickjacking X-Frame-Options header is not present.
+ Retrieved x-aspnet-version header: 4.0.30319
+ Server banner has changed from 'Microsoft-IIS/10.0' to 'Microsoft-HTTPAPI/2.0' which may suggest a WAF, load balancer or proxy is in place
+ Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST 
+ 6544 items checked: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2025-08-25 12:12:19 (GMT2) (485 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
Der Befehl 'whatweb' wurde nicht gefunden, kann aber installiert werden mit:
apt install whatweb
httprobe: Befehl nicht gefunden.
