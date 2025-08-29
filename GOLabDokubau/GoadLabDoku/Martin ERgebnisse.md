**

nmap -sn 192.168.20.0/24   

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:28 CEST

Nmap scan report for 192.168.20.1

Host is up (0.034s latency).

Nmap scan report for 192.168.20.10

Host is up (0.052s latency).

Nmap scan report for 192.168.20.11

Host is up (0.047s latency).

Nmap scan report for 192.168.20.12

Host is up (0.067s latency).

Nmap scan report for 192.168.20.22

Host is up (0.046s latency).

Nmap scan report for 192.168.20.23

Host is up (0.046s latency).

Nmap done: 256 IP addresses (6 hosts up) scanned in 10.90 seconds

--------------------------------------------------------

nslookup 192.168.20.10

** server can't find 10.20.168.192.in-addr.arpa: NXDOMAIN

nslookup 192.168.20.11

** server can't find 11.20.168.192.in-addr.arpa: NXDOMAIN

  

nslookup 192.168.20.12

** server can't find 12.20.168.192.in-addr.arpa: NXDOMAIN

--------------------------------------------------------------------------

nmap -A -Pn 192.168.20.1

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 14:21 CEST

Nmap scan report for 192.168.20.1

Host is up (0.048s latency).

Not shown: 997 filtered tcp ports (no-response)

PORT STATE SERVICE  VERSION

53/tcp  open  domain   Unbound

80/tcp  open  http nginx

|_http-title: Did not follow redirect to https://192.168.20.1/

443/tcp open  ssl/http nginx

|_http-title: pfSense - Login

| ssl-cert: Subject: commonName=vpn.goad.lab

| Subject Alternative Name: DNS:vpn.goad.lab

| Not valid before: 2024-07-05T14:32:40

|_Not valid after:  2034-07-03T14:32:40

| tls-alpn:

|   h2

|   http/1.1

|   http/1.0

|_  http/0.9

|_ssl-date: TLS randomness does not represent time

Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port

Device type: general purpose

Running (JUST GUESSING): FreeBSD 11.X (88%)

OS CPE: cpe:/o:freebsd:freebsd:11.2

Aggressive OS guesses: FreeBSD 11.2-RELEASE (88%)

No exact OS matches for host (test conditions non-ideal).

Network Distance: 1 hop

  

TRACEROUTE (using port 53/tcp)

HOP RTT  ADDRESS

1   46.83 ms 192.168.20.1

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 45.88 seconds

-----------------------------------------------------------------------------------------------------

nmap -A -Pn 192.168.20.10

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:31 CEST

Nmap scan report for 192.168.20.10

Host is up (0.078s latency).

Not shown: 985 closed tcp ports (reset)

PORT STATE SERVICE   VERSION

53/tcp   open  domain    Simple DNS Plus

80/tcp   open  http      Microsoft IIS httpd 10.0

| http-methods:

|_  Potentially risky methods: TRACE

|_http-title: IIS Windows Server

|_http-server-header: Microsoft-IIS/10.0

88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 11:31:46Z)

135/tcp  open  msrpc     Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

389/tcp  open  ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local

| Not valid before: 2025-04-13T16:42:45

|_Not valid after:  2026-04-13T16:42:45

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

445/tcp  open  microsoft-ds?

464/tcp  open  kpasswd5?

593/tcp  open  ncacn_http Microsoft Windows RPC over HTTP 1.0

636/tcp  open  ssl/ldap  Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local

| Not valid before: 2025-04-13T16:42:45

|_Not valid after:  2026-04-13T16:42:45

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

3268/tcp open  ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local

| Not valid before: 2025-04-13T16:42:45

|_Not valid after:  2026-04-13T16:42:45

3269/tcp open  ssl/ldap

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:kingslanding.sevenkingdoms.local

| Not valid before: 2025-04-13T16:42:45

|_Not valid after:  2026-04-13T16:42:45

3389/tcp open  ms-wbt-server Microsoft Terminal Services

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=kingslanding.sevenkingdoms.local

| Not valid before: 2025-04-12T16:22:47

|_Not valid after:  2025-10-12T16:22:47

| rdp-ntlm-info:

|   Target_Name: SEVENKINGDOMS

|   NetBIOS_Domain_Name: SEVENKINGDOMS

|   NetBIOS_Computer_Name: KINGSLANDING

|   DNS_Domain_Name: sevenkingdoms.local

|   DNS_Computer_Name: kingslanding.sevenkingdoms.local

|   DNS_Tree_Name: sevenkingdoms.local

|   Product_Version: 10.0.17763

|_  System_Time: 2025-08-22T11:32:29+00:00

5985/tcp open  http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-server-header: Microsoft-HTTPAPI/2.0

|_http-title: Not Found

5986/tcp open  ssl/http  Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_ssl-date: 2025-08-22T11:32:38+00:00; -5s from scanner time.

|_http-title: Not Found

| ssl-cert: Subject: commonName=VAGRANT-2019

| Subject Alternative Name: DNS:VAGRANT-2019, DNS:vagrant-2019

| Not valid before: 2024-06-12T06:56:50

|_Not valid after:  2027-06-12T06:56:50

| tls-alpn:

|_  http/1.1

|_http-server-header: Microsoft-HTTPAPI/2.0

Device type: general purpose

Running: Microsoft Windows 2019

OS CPE: cpe:/o:microsoft:windows_server_2019

OS details: Windows Server 2019

Network Distance: 2 hops

Service Info: Host: KINGSLANDING; OS: Windows; CPE: cpe:/o:microsoft:windows

  

Host script results:

| smb2-security-mode:

|   3:1:1:

|_ Message signing enabled and required

| smb2-time:

|   date: 2025-08-22T11:32:30

|_  start_date: N/A

|_clock-skew: mean: -4s, deviation: 0s, median: -5s

  

TRACEROUTE (using port 143/tcp)

HOP RTT  ADDRESS

1   40.69 ms 10.2.0.1

2   40.70 ms 192.168.20.10

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 69.01 seconds

----------------------------------------------------------------

nmap -A -Pn 192.168.20.11

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:33 CEST

Nmap scan report for 192.168.20.11

Host is up (0.066s latency).

Not shown: 986 closed tcp ports (reset)

PORT STATE SERVICE   VERSION

53/tcp   open  domain    Simple DNS Plus

88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 11:34:02Z)

135/tcp  open  msrpc     Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

389/tcp  open  ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:winterfell.north.sevenkingdoms.local

| Not valid before: 2025-04-13T17:05:17

|_Not valid after:  2026-04-13T17:05:17

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

445/tcp  open  microsoft-ds?

464/tcp  open  kpasswd5?

593/tcp  open  ncacn_http Microsoft Windows RPC over HTTP 1.0

636/tcp  open  ssl/ldap  Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:winterfell.north.sevenkingdoms.local

| Not valid before: 2025-04-13T17:05:17

|_Not valid after:  2026-04-13T17:05:17

3268/tcp open  ldap      Microsoft Windows Active Directory LDAP (Domain: sevenkingdoms.local0., Site: Default-First-Site-Name)

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:winterfell.north.sevenkingdoms.local

| Not valid before: 2025-04-13T17:05:17

|_Not valid after:  2026-04-13T17:05:17

3269/tcp open  ssl/ldap

| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:winterfell.north.sevenkingdoms.local

| Not valid before: 2025-04-13T17:05:17

|_Not valid after:  2026-04-13T17:05:17

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

3389/tcp open  ms-wbt-server Microsoft Terminal Services

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

| rdp-ntlm-info:

|   Target_Name: NORTH

|   NetBIOS_Domain_Name: NORTH

|   NetBIOS_Computer_Name: WINTERFELL

|   DNS_Domain_Name: north.sevenkingdoms.local

|   DNS_Computer_Name: winterfell.north.sevenkingdoms.local

|   DNS_Tree_Name: sevenkingdoms.local

|   Product_Version: 10.0.17763

|_  System_Time: 2025-08-22T11:34:45+00:00

| ssl-cert: Subject: commonName=winterfell.north.sevenkingdoms.local

| Not valid before: 2025-04-12T16:31:49

|_Not valid after:  2025-10-12T16:31:49

5985/tcp open  http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-title: Not Found

|_http-server-header: Microsoft-HTTPAPI/2.0

5986/tcp open  ssl/http  Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

| tls-alpn:

|_  http/1.1

|_http-title: Not Found

|_ssl-date: 2025-08-22T11:34:54+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=VAGRANT-2019

| Subject Alternative Name: DNS:VAGRANT-2019, DNS:vagrant-2019

| Not valid before: 2024-06-12T06:56:50

|_Not valid after:  2027-06-12T06:56:50

|_http-server-header: Microsoft-HTTPAPI/2.0

Device type: general purpose

Running: Microsoft Windows 2019

OS CPE: cpe:/o:microsoft:windows_server_2019

OS details: Windows Server 2019

Network Distance: 2 hops

Service Info: Host: WINTERFELL; OS: Windows; CPE: cpe:/o:microsoft:windows

  

Host script results:

| smb2-security-mode:

|   3:1:1:

|_ Message signing enabled and required

| smb2-time:

|   date: 2025-08-22T11:34:47

|_  start_date: N/A

|_clock-skew: mean: -5s, deviation: 0s, median: -5s

  

TRACEROUTE (using port 199/tcp)

HOP RTT  ADDRESS

1   44.89 ms 10.2.0.1

2   38.74 ms 192.168.20.11

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 62.34 seconds

-------------------------------------------------------------------

nmap -A -Pn 192.168.20.12

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:36 CEST

Nmap scan report for 192.168.20.12

Host is up (0.054s latency).

Not shown: 986 closed tcp ports (reset)

PORT STATE SERVICE   VERSION

53/tcp   open  domain    Simple DNS Plus

88/tcp   open  kerberos-sec  Microsoft Windows Kerberos (server time: 2025-08-22 11:36:32Z)

135/tcp  open  msrpc     Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

389/tcp  open  ldap      Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)

| ssl-cert: Subject: commonName=meereen.essos.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:meereen.essos.local

| Not valid before: 2025-04-13T16:43:00

|_Not valid after:  2026-04-13T16:43:00

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds (workgroup: ESSOS)

464/tcp  open  kpasswd5?

593/tcp  open  ncacn_http Microsoft Windows RPC over HTTP 1.0

636/tcp  open  ssl/ldap  Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

| ssl-cert: Subject: commonName=meereen.essos.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:meereen.essos.local

| Not valid before: 2025-04-13T16:43:00

|_Not valid after:  2026-04-13T16:43:00

3268/tcp open  ldap      Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

| ssl-cert: Subject: commonName=meereen.essos.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:meereen.essos.local

| Not valid before: 2025-04-13T16:43:00

|_Not valid after:  2026-04-13T16:43:00

3269/tcp open  ssl/ldap  Microsoft Windows Active Directory LDAP (Domain: essos.local, Site: Default-First-Site-Name)

| ssl-cert: Subject: commonName=meereen.essos.local

| Subject Alternative Name: othername: 1.3.6.1.4.1.311.25.1:<unsupported>, DNS:meereen.essos.local

| Not valid before: 2025-04-13T16:43:00

|_Not valid after:  2026-04-13T16:43:00

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

3389/tcp open  ms-wbt-server Microsoft Terminal Services

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

| ssl-cert: Subject: commonName=meereen.essos.local

| Not valid before: 2025-04-12T16:22:52

|_Not valid after:  2025-10-12T16:22:52

5985/tcp open  http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-server-header: Microsoft-HTTPAPI/2.0

|_http-title: Not Found

5986/tcp open  ssl/http  Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-title: Not Found

| tls-alpn:

|   h2

|_  http/1.1

|_ssl-date: 2025-08-22T11:37:50+00:00; -6s from scanner time.

| ssl-cert: Subject: commonName=VAGRANT-2016

| Subject Alternative Name: DNS:VAGRANT-2016, DNS:vagrant-2016

| Not valid before: 2024-06-16T03:56:03

|_Not valid after:  2027-06-16T03:56:03

|_http-server-header: Microsoft-HTTPAPI/2.0

No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).

TCP/IP fingerprint:

OS:SCAN(V=7.95%E=4%D=8/22%OT=53%CT=1%CU=39271%PV=Y%DS=2%DC=T%G=Y%TM=68A8569

OS:7%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=10C%TI=I%II=I%SS=S%TS=A)SEQ

OS:(SP=104%GCD=1%ISR=108%TI=I%II=I%SS=S%TS=A)SEQ(SP=105%GCD=1%ISR=10D%TI=I%

OS:II=I%SS=S%TS=A)SEQ(SP=106%GCD=1%ISR=109%TI=I%II=I%SS=S%TS=A)SEQ(SP=107%G

OS:CD=1%ISR=10E%TI=I%II=I%SS=S%TS=A)OPS(O1=M578NW8ST11%O2=M578NW8ST11%O3=M5

OS:78NW8NNT11%O4=M578NW8ST11%O5=M578NW8ST11%O6=M578ST11)WIN(W1=2000%W2=2000

OS:%W3=2000%W4=2000%W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M578NW8NNS%C

OS:C=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=

OS:Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=80%

OS:IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

  

Network Distance: 2 hops

Service Info: Host: MEEREEN; OS: Windows; CPE: cpe:/o:microsoft:windows

  

Host script results:

| smb-os-discovery:

|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)

|   Computer name: meereen

|   NetBIOS computer name: MEEREEN\x00

|   Domain name: essos.local

|   Forest name: essos.local

|   FQDN: meereen.essos.local

|_  System time: 2025-08-22T13:37:41+02:00

| smb2-time:

|   date: 2025-08-22T11:37:42

|_  start_date: 2025-08-13T14:05:32

| smb2-security-mode:

|   3:1:1:

|_ Message signing enabled and required

| smb-security-mode:

|   account_used: guest

|   authentication_level: user

|   challenge_response: supported

|_  message_signing: required

|_clock-skew: mean: -13m25s, deviation: 39m57s, median: -6s

  

TRACEROUTE (using port 111/tcp)

HOP RTT  ADDRESS

1   74.35 ms 10.2.0.1

2   52.20 ms 192.168.20.12

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 100.05 seconds

------------------------------------------------------------------

nmap -A -Pn 192.168.20.22

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:40 CEST

Nmap scan report for 192.168.20.22

Host is up (0.11s latency).

Not shown: 992 closed tcp ports (reset)

PORT STATE SERVICE   VERSION

80/tcp   open  http      Microsoft IIS httpd 10.0

|_http-server-header: Microsoft-IIS/10.0

|_http-title: Site doesn't have a title (text/html).

| http-methods:

|_  Potentially risky methods: TRACE

135/tcp  open  msrpc     Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

445/tcp  open  microsoft-ds?

1433/tcp open  ms-sql-s  Microsoft SQL Server 2019 15.00.2000.00; RTM

| ms-sql-ntlm-info:

|   192.168.20.22:1433:

| Target_Name: NORTH

| NetBIOS_Domain_Name: NORTH

| NetBIOS_Computer_Name: CASTELBLACK

| DNS_Domain_Name: north.sevenkingdoms.local

| DNS_Computer_Name: castelblack.north.sevenkingdoms.local

| DNS_Tree_Name: sevenkingdoms.local

|_ Product_Version: 10.0.17763

| ms-sql-info:

|   192.168.20.22:1433:

| Version:

|   name: Microsoft SQL Server 2019 RTM

|   number: 15.00.2000.00

|   Product: Microsoft SQL Server 2019

|   Service pack level: RTM

|   Post-SP patches applied: false

|_ TCP port: 1433

|_ssl-date: 2025-08-22T11:40:55+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback

| Not valid before: 2025-08-13T14:05:10

|_Not valid after:  2055-08-13T14:05:10

3389/tcp open  ms-wbt-server Microsoft Terminal Services

|_ssl-date: 2025-08-22T11:40:55+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=castelblack.north.sevenkingdoms.local

| Not valid before: 2025-04-12T16:38:33

|_Not valid after:  2025-10-12T16:38:33

| rdp-ntlm-info:

|   Target_Name: NORTH

|   NetBIOS_Domain_Name: NORTH

|   NetBIOS_Computer_Name: CASTELBLACK

|   DNS_Domain_Name: north.sevenkingdoms.local

|   DNS_Computer_Name: castelblack.north.sevenkingdoms.local

|   DNS_Tree_Name: sevenkingdoms.local

|   Product_Version: 10.0.17763

|_  System_Time: 2025-08-22T11:40:47+00:00

5985/tcp open  http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-server-header: Microsoft-HTTPAPI/2.0

|_http-title: Not Found

5986/tcp open  wsmans?

| tls-alpn:

|_  http/1.1

|_ssl-date: 2025-08-22T11:40:55+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=VAGRANT-2019

| Subject Alternative Name: DNS:VAGRANT-2019, DNS:vagrant-2019

| Not valid before: 2024-06-12T06:56:50

|_Not valid after:  2027-06-12T06:56:50

Device type: general purpose

Running: Microsoft Windows 2019

OS CPE: cpe:/o:microsoft:windows_server_2019

OS details: Windows Server 2019

Network Distance: 2 hops

Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

  

Host script results:

|_clock-skew: mean: -4s, deviation: 0s, median: -5s

| smb2-security-mode:

|   3:1:1:

|_ Message signing enabled but not required

| smb2-time:

|   date: 2025-08-22T11:40:49

|_  start_date: N/A

  

TRACEROUTE (using port 23/tcp)

HOP RTT  ADDRESS

1   60.77 ms 10.2.0.1

2   60.89 ms 192.168.20.22

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 59.25 seconds

-----------------------------------------------------------------------

nmap -A -Pn 192.168.20.23

  

Starting Nmap 7.95 ( https://nmap.org ) at 2025-08-22 13:41 CEST

Nmap scan report for 192.168.20.23

Host is up (0.058s latency).

Not shown: 992 closed tcp ports (reset)

PORT STATE SERVICE   VERSION

80/tcp   open  http      Microsoft IIS httpd 10.0

|_http-title: IIS Windows Server

|_http-server-header: Microsoft-IIS/10.0

| http-methods:

|_  Potentially risky methods: TRACE

135/tcp  open  msrpc     Microsoft Windows RPC

139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn

445/tcp  open  microsoft-ds  Windows Server 2016 Standard Evaluation 14393 microsoft-ds

1433/tcp open  ms-sql-s  Microsoft SQL Server 2019 15.00.2000.00; RTM

| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback

| Not valid before: 2025-08-13T14:05:09

|_Not valid after:  2055-08-13T14:05:09

| ms-sql-info:

|   192.168.20.23:1433:

| Version:

|   name: Microsoft SQL Server 2019 RTM

|   number: 15.00.2000.00

|   Product: Microsoft SQL Server 2019

|   Service pack level: RTM

|   Post-SP patches applied: false

|_ TCP port: 1433

| ms-sql-ntlm-info:

|   192.168.20.23:1433:

| Target_Name: ESSOS

| NetBIOS_Domain_Name: ESSOS

| NetBIOS_Computer_Name: BRAAVOS

| DNS_Domain_Name: essos.local

| DNS_Computer_Name: braavos.essos.local

| DNS_Tree_Name: essos.local

|_ Product_Version: 10.0.14393

|_ssl-date: 2025-08-22T11:43:16+00:00; -5s from scanner time.

3389/tcp open  ms-wbt-server Microsoft Terminal Services

| ssl-cert: Subject: commonName=braavos.essos.local

| Not valid before: 2025-04-12T16:36:10

|_Not valid after:  2025-10-12T16:36:10

| rdp-ntlm-info:

|   Target_Name: ESSOS

|   NetBIOS_Domain_Name: ESSOS

|   NetBIOS_Computer_Name: BRAAVOS

|   DNS_Domain_Name: essos.local

|   DNS_Computer_Name: braavos.essos.local

|   DNS_Tree_Name: essos.local

|   Product_Version: 10.0.14393

|_  System_Time: 2025-08-22T11:43:06+00:00

|_ssl-date: 2025-08-22T11:43:16+00:00; -5s from scanner time.

5985/tcp open  http      Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-title: Not Found

|_http-server-header: Microsoft-HTTPAPI/2.0

5986/tcp open  ssl/http  Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)

|_http-title: Not Found

| tls-alpn:

|   h2

|_  http/1.1

|_http-server-header: Microsoft-HTTPAPI/2.0

|_ssl-date: 2025-08-22T11:43:16+00:00; -5s from scanner time.

| ssl-cert: Subject: commonName=VAGRANT-2016

| Subject Alternative Name: DNS:VAGRANT-2016, DNS:vagrant-2016

| Not valid before: 2024-06-16T03:56:03

|_Not valid after:  2027-06-16T03:56:03

No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).

TCP/IP fingerprint:

OS:SCAN(V=7.95%E=4%D=8/22%OT=80%CT=1%CU=40703%PV=Y%DS=2%DC=T%G=Y%TM=68A857D

OS:9%P=x86_64-pc-linux-gnu)SEQ(SP=101%GCD=1%ISR=108%TI=I%II=I%SS=S%TS=A)SEQ

OS:(SP=103%GCD=1%ISR=10D%TI=I%II=I%SS=S%TS=A)SEQ(SP=104%GCD=1%ISR=107%TI=I%

OS:II=I%SS=S%TS=A)SEQ(SP=107%GCD=1%ISR=10B%TI=I%II=I%SS=S%TS=A)SEQ(SP=108%G

OS:CD=2%ISR=10C%TI=I%II=I%SS=S%TS=A)OPS(O1=M578NW8ST11%O2=M578NW8ST11%O3=M5

OS:78NW8NNT11%O4=M578NW8ST11%O5=M578NW8ST11%O6=M578ST11)WIN(W1=2000%W2=2000

OS:%W3=2000%W4=2000%W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M578NW8NNS%C

OS:C=Y%Q=)T1(R=Y%DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=

OS:Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=80%

OS:IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

  

Network Distance: 2 hops

Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

  

Host script results:

| smb2-time:

|   date: 2025-08-22T11:43:10

|_  start_date: 2025-08-13T14:05:07

| smb2-security-mode:

|   3:1:1:

|_ Message signing enabled but not required

| smb-os-discovery:

|   OS: Windows Server 2016 Standard Evaluation 14393 (Windows Server 2016 Standard Evaluation 6.3)

|   Computer name: braavos

|   NetBIOS computer name: BRAAVOS\x00

|   Domain name: essos.local

|   Forest name: essos.local

|   FQDN: braavos.essos.local

|_  System time: 2025-08-22T13:43:09+02:00

| smb-security-mode:

|   account_used: guest

|   authentication_level: user

|   challenge_response: supported

|_  message_signing: disabled (dangerous, but default)

|_clock-skew: mean: -15m05s, deviation: 42m24s, median: -6s

  

TRACEROUTE (using port 1025/tcp)

HOP RTT  ADDRESS

1   59.12 ms 10.2.0.1

2   59.10 ms 192.168.20.23

  

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 87.61 seconds

—-------------------------------------------------------------------------------------

  
**