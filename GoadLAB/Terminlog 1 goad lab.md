Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-08-22 14:27 CEST
Nmap scan report for localhost (192.168.20.10)
Host is up (0.019s latency).
Not shown: 987 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 12:27:21Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2025-04-13T16:42:45
|_Not valid after:  2026-04-13T16:42:45
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2025-04-13T16:42:45
|_Not valid after:  2026-04-13T16:42:45
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2025-04-13T16:42:45
|_Not valid after:  2026-04-13T16:42:45
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:kingslanding.sevenkingdoms.local
| Not valid before: 2025-04-13T16:42:45
|_Not valid after:  2026-04-13T16:42:45
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local
| Not valid before: 2025-04-12T16:22:47
|_Not valid after:  2025-10-12T16:22:47
| rdp-ntlm-info: 
|   Target_Name: SEVENKINGDOMS
|   NetBIOS_Domain_Name: SEVENKINGDOMS
|   NetBIOS_Computer_Name: KINGSLANDING
|   DNS_Domain_Name: sevenkingdoms.local
|   DNS_Computer_Name: kingslanding.sevenkingdoms.local
|   DNS_Tree_Name: sevenkingdoms.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-08-22T12:28:06+00:00
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
Service Info: Host: KINGSLANDING; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-08-22T12:28:07
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: -3s, deviation: 0s, median: -3s

Nmap scan report for localhost (192.168.20.11)
Host is up (0.021s latency).
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 12:27:21Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:winterfell.north.sevenkingdoms.local
| Not valid before: 2025-04-13T17:05:17
|_Not valid after:  2026-04-13T17:05:17
445/tcp  open  microsoft-ds?
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:winterfell.north.sevenkingdoms.local
| Not valid before: 2025-04-13T17:05:17
|_Not valid after:  2026-04-13T17:05:17
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:winterfell.north.sevenkingdoms.local
| Not valid before: 2025-04-13T17:05:17
|_Not valid after:  2026-04-13T17:05:17
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:winterfell.north.sevenkingdoms.local
| Not valid before: 2025-04-13T17:05:17
|_Not valid after:  2026-04-13T17:05:17
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: NORTH
|   NetBIOS_Domain_Name: NORTH
|   NetBIOS_Computer_Name: WINTERFELL
|   DNS_Domain_Name: north.sevenkingdoms.local
|   DNS_Computer_Name: winterfell.north.sevenkingdoms.local
|   DNS_Tree_Name: sevenkingdoms.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-08-22T12:28:07+00:00
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local
| Not valid before: 2025-04-12T16:31:49
|_Not valid after:  2025-10-12T16:31:49
Service Info: Host: WINTERFELL; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -3s, deviation: 0s, median: -3s
| smb2-time: 
|   date: 2025-08-22T12:28:17
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required

Nmap scan report for localhost (192.168.20.12)
Host is up (0.020s latency).
Not shown: 988 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
53/tcp   open  domain        Simple DNS Plus
88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 12:27:26Z)
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
389/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
| ssl-cert: Subject: commonName=meereen.essos.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:meereen.essos.local
| Not valid before: 2025-04-13T16:43:00
|_Not valid after:  2026-04-13T16:43:00
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds (workgroup: ESSOS)
464/tcp  open  kpasswd5?
593/tcp  open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp  open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)
| ssl-cert: Subject: commonName=meereen.essos.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:meereen.essos.local
| Not valid before: 2025-04-13T16:43:00
|_Not valid after:  2026-04-13T16:43:00
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
3268/tcp open  ldap          Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=meereen.essos.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:meereen.essos.local
| Not valid before: 2025-04-13T16:43:00
|_Not valid after:  2026-04-13T16:43:00
3269/tcp open  ssl/ldap      Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
| ssl-cert: Subject: commonName=meereen.essos.local
| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1::<unsupported>, DNS:meereen.essos.local
| Not valid before: 2025-04-13T16:43:00
|_Not valid after:  2026-04-13T16:43:00
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=meereen.essos.local
| Not valid before: 2025-04-12T16:22:52
|_Not valid after:  2025-10-12T16:22:52
| rdp-ntlm-info: 
|   Target_Name: ESSOS
|   NetBIOS_Domain_Name: ESSOS
|   NetBIOS_Computer_Name: MEEREEN
|   DNS_Domain_Name: essos.local
|   DNS_Computer_Name: meereen.essos.local
|   DNS_Tree_Name: essos.local
|   Product_Version: 10.0.14393
|_  System_Time: 2025-08-22T12:28:10+00:00
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
Service Info: Host: MEEREEN; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: required
| smb2-time: 
|   date: 2025-08-22T12:28:21
|_  start_date: 2025-08-13T14:05:32
|_clock-skew: mean: -13m22s, deviation: 39m55s, median: -4s
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: meereen
|   NetBIOS computer name: MEEREEN\x00
|   Domain name: essos.local
|   Forest name: essos.local
|   FQDN: meereen.essos.local
|_  System time: 2025-08-22T14:28:18+02:00

Nmap scan report for localhost (192.168.20.13)
Host is up.
All 1000 scanned ports on localhost (192.168.20.13) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.14)
Host is up.
All 1000 scanned ports on localhost (192.168.20.14) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.15)
Host is up.
All 1000 scanned ports on localhost (192.168.20.15) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.16)
Host is up.
All 1000 scanned ports on localhost (192.168.20.16) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.17)
Host is up.
All 1000 scanned ports on localhost (192.168.20.17) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.18)
Host is up.
All 1000 scanned ports on localhost (192.168.20.18) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.19)
Host is up.
All 1000 scanned ports on localhost (192.168.20.19) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.20)
Host is up.
All 1000 scanned ports on localhost (192.168.20.20) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.21)
Host is up.
All 1000 scanned ports on localhost (192.168.20.21) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)

Nmap scan report for localhost (192.168.20.22)
Host is up (0.019s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: IIS Windows Server
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ms-sql-ntlm-info: ERROR: Script execution failed (use -d to debug)
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-08-13T14:05:10
|_Not valid after:  2055-08-13T14:05:10
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-08-22T12:28:48+00:00; -3s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: NORTH
|   NetBIOS_Domain_Name: NORTH
|   NetBIOS_Computer_Name: CASTELBLACK
|   DNS_Domain_Name: north.sevenkingdoms.local
|   DNS_Computer_Name: castelblack.north.sevenkingdoms.local
|   DNS_Tree_Name: sevenkingdoms.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-08-22T12:28:07+00:00
| ssl-cert: Subject: commonName=castelblack.north.sevenkingdoms.local
| Not valid before: 2025-04-12T16:38:33
|_Not valid after:  2025-10-12T16:38:33
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: -3s, deviation: 0s, median: -3s
| smb2-time: 
|   date: 2025-08-22T12:28:25
|_  start_date: N/A

Nmap scan report for localhost (192.168.20.23)
Host is up (0.019s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-title: IIS Windows Server
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds
1433/tcp open  ms-sql-s      Microsoft SQL Server 2019 15.00.2000.00; RTM
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
|_ms-sql-info: ERROR: Script execution failed (use -d to debug)
|_ms-sql-ntlm-info: ERROR: Script execution failed (use -d to debug)
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2025-08-13T14:05:09
|_Not valid after:  2055-08-13T14:05:09
3389/tcp open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2025-08-22T12:28:47+00:00; -4s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: ESSOS
|   NetBIOS_Domain_Name: ESSOS
|   NetBIOS_Computer_Name: BRAAVOS
|   DNS_Domain_Name: essos.local
|   DNS_Computer_Name: braavos.essos.local
|   DNS_Tree_Name: essos.local
|   Product_Version: 10.0.14393
|_  System_Time: 2025-08-22T12:28:08+00:00
| ssl-cert: Subject: commonName=braavos.essos.local
| Not valid before: 2025-04-12T16:36:10
|_Not valid after:  2025-10-12T16:36:10
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -19m59s, deviation: 48m49s, median: -4s
| smb2-time: 
|   date: 2025-08-22T12:28:27
|_  start_date: 2025-08-13T14:05:07
| smb-os-discovery: 
|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)
|   Computer name: braavos
|   NetBIOS computer name: BRAAVOS\x00
|   Domain name: essos.local
|   Forest name: essos.local
|   FQDN: braavos.essos.local
|_  System time: 2025-08-22T14:28:30+02:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Post-scan script results:
| clock-skew: 
|   -19m59s: 
|     192.168.20.23 (localhost)
|     192.168.20.12 (localhost)
|   -3s: 
|     192.168.20.11 (localhost)
|     192.168.20.10 (localhost)
|_    192.168.20.22 (localhost)
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 14 IP addresses (14 hosts up) scanned in 110.54 seconds
root@tala-HP-255-15-6-inch-G10-Notebook-PC:/home/tala# nmap -Pn --script vuln 192.168.10.10-23         
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-08-22 14:29 CEST
Nmap scan report for localhost (192.168.10.10)
Host is up (0.018s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.11)
Host is up (0.018s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.12)
Host is up (0.018s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.13)
Host is up (0.020s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.14)
Host is up (0.020s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.15)
Host is up (0.012s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.16)
Host is up (0.016s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.17)
Host is up (0.019s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.18)
Host is up (0.019s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.19)
Host is up (0.020s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.20)
Host is up (0.022s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.21)
Host is up (0.022s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.22)
Host is up (0.034s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp

Nmap scan report for localhost (192.168.10.23)
Host is up (0.021s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE  SERVICE
25/tcp closed smtp
