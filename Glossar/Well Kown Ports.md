https://www.ionos.de/digitalguide/server/knowhow/tcp-und-udp-ports/



### Well Kown Ports

|Port|TCP|UDP|Name|Beschreibung|
|---|---|---|---|---|
|1|||tcpmux|TCP Port Multiplexer|
|5|||rje|Remote Job Entry (Jobferneingabe)|
|7|||echo|Echo-Service|
|9|||discard|Null-Service für Prüfzwecke|
|11|||systat|Systeminformationen|
|13|||daytime|Zeit- und Datumsangaben|
|17|||qotd|Sendet Zitat des Tages|
|18|||msp|Übermittelt Textnachrichten|
|19|||chargen|Sendet eine endlose Zeichenkette|
|20|||ftp-data|FTP-Datenübertragung|
|21|||ftp|FTP-Verbindung|
|22|||ssh|Secure Shell Service|
|23|||telnet|Telnet-Service|
|25|||smtp|Simple Mail Transfer Protocol|
|37|||time|Maschinenlesbares Zeitprotokoll|
|39|||rlp|Resource Location Protocol|
|42|||nameserver|Name-Service|
|43|||nicname|WHOIS-Verzeichnisservice|
|49|||tacacs|Terminal Access Controller Access Control System|
|50|||re-mail-ck|Remote Mail Checking|
|53|||domain|Namensauflösung per DNS|
|67|||bootps|Bootstrap Protocol Services|
|68|||bootpc|Bootstrap Client|
|69|||tftp|Trivial File Transfer Protocol|
|70|||gopher|Dokumentensuche|
|71|||genius|Geniusprotokoll|
|79|||finger|Liefert Kontaktinformationen von Benutzern|
|80|||http|Hypertext Transfer Protocol|
|81||||Torpark: Onion-Routing (inoffiziell)|
|82||||Torpark: Control (inoffiziell)|
|88|||kerberos|Netzwerkauthentifizierungssystem|
|101|||hostname|NIC Host Name|
|102|||Iso-tsap|ISO-TSAP-Protocol|
|105|||csnet-ns|Mailbox-Mailserver|
|107|||rtelnet|Remote Telnet|
|109|||pop2|Post Office Protocol v2 für die E-Mail-Kommunikation|
|110|||pop3|Post Office Protocol v3 für die E-Mail-Kommunikation|
|111|||sunrpc|RPC-Protokoll für NFS|
|113|||auth|Authentifizierungsservice|
|115|||sftp|Simple File Transfer Protocol (einfache Version von FTP)|
|117|||uucp-path|Dateiübertragung zwischen Unix-Systemen|
|119|||nntp|Übertragung von Nachrichten in Newsgroups|
|123|||ntp|Dienst zur Zeitsynchronisierung|
|137|||netbios-ns|NETBIOS Name Service|
|138|||netbios-dgm|NETBIOS Datagram Service|
|139|||netbios-ssn|NETBIOS Session Service|
|143|||imap|Internet Message Access Protocol für E-Mail-Kommunikation|
|161|||snmp|Simple Network Management Protocol|
|162|||snmptrap|Simple Network Management Protocol Trap|
|177|||xdmcp|X Display Manager|
|179|||bgp|Border Gateway Protocol|
|194|||irc|Internet Relay Chat|
|199|||smux|SNMP UNIX Multiplexer|
|201|||at-rtmp|AppleTalk Routing|
|209|||qmtp|Quick Mail Transfer Protocol|
|210|||z39.50|Bibliographisches Informationssystem|
|213|||ipx|Internetwork Packet Exchange|
|220|||imap3|IMAP v3 für die E-Mail-Kommunikation|
|369|||rpc2portmap|Coda Filesystem Portmapper|
|370|||codaauth2|Coda Filesystem Authentication Service|
|389|||ldap|Lightweight Directory Access Protocol|
|427|||svrloc|Service Location Protocol|
|443|||https|HTTPS (HTTP über SSL/TLS)|
|444|||snpp|Simple Network Paging Protocol|
|445|||microsoft-ds|SMB über TCP/IP|
|464|||kpasswd|Passwortänderung für Kerberos|
|500|||isakmp|Sicherheitsprotokoll|
|512|||exec|Remote Process Execution|
|512|||comsat/biff|Mail-Client und -Server|
|513|||login|Anmeldung an Remote-Computer|
|513|||who|Whod User Logging Daemon|
|514|||shell|Remote Shell|
|514|||syslog|Unix System Logging Service|
|515|||printer|Line Printer Daemon-Druckservices|
|517|||talk|Talk Remote Calling|
|518|||ntalk|Network Talk|
|520|||efs|Extended Filename Server|
|520|||router|Routing Information Protocol|
|521|||ripng|Routing Information Protocol für IPv6|
|525|||timed|Zeitserver|
|530|||courier|Courier Remote Procedure Call|
|531|||conference|Chat über AIM und IRC|
|532|||netnews|Netnews Newsgroup Service|
|533|||netwall|Notfall-Broadcasts|
|540|||uucp|Unix-to-Unix Copy Protocol|
|543|||klogin|Kerberos v5 Remote Login|
|544|||kshell|Kerberos v5 Remote Shell|
|546|||dhcpv6-client|DHCP v6 Client|
|547|||dhcpv6-server|DHCP v6 Server|
|548|||afpovertcp|Apple Filing Protocol über TCP|
|554|||rtsp|Steuerung von Streams|
|556|||remotefs|Remote Filesystem|
|563|||nntps|NNTP über SSL/TLS|
|587|||submission|Message Submission Agent|
|631|||ipp|Internet Printing Protocol|
|631||||Common Unix Printing System (inoffiziell)|
|636|||ldaps|LDAP über SSL/TLS|
|674|||acap|Application Configuration Access Protocol|
|694|||ha-cluster|Heartbeat-Service|
|749|||kerberos-adm|Kerberos v5 Administration|
|750|||kerberos-iv|Kerberos v4 Services|
|873|||rsync|rsync Dateitransfer-Services|
|992|||telnets|Telnet über SSL/TLS|
|993|||imaps|IMAP über SSL/TLS|
|995|||pop3s|POP3 über SSL/TLS|

### Registered Ports

| Port  | TCP | UDP | Name         | Beschreibung                                    |
| ----- | --- | --- | ------------ | ----------------------------------------------- |
| 1080  |     |     | socks        | SOCKS Proxy                                     |
| 1433  |     |     | ms-sql-s     | Microsoft SQL Server                            |
| 1434  |     |     | ms-sql-m     | Microsoft SQL Monitor                           |
| 1494  |     |     | ica          | Citrix ICA Client                               |
| 1512  |     |     | wins         | Windows Internet Name Service                   |
| 1524  |     |     | ingreslock   | Ingres DBMS                                     |
| 1701  |     |     | l2tp         | Layer 2 Tunneling Protocol / Layer 2 Forwarding |
| 1719  |     |     | h323gatestat | H.323                                           |
| 1720  |     |     | h323hostcall | H.323                                           |
| 1812  |     |     | radius       | RADIUS-Authentifikation                         |
| 1813  |     |     | radius-acct  | RADIUS-Zugang                                   |
| 1985  |     |     | hsrp         | Cisco HSRP                                      |
| 2008  |     |     |              | Teamspeak 3 Accounting (inoffiziell)            |
| 2010  |     |     |              | Teamspeak 3 Webliste (inoffiziell)              |
| 2049  |     |     | nfs          | Network File System                             |
| 2102  |     |     | zephyr-srv   | Zephyr Server                                   |
| 2103  |     |     | zephyr-clt   | Zephyr Client                                   |
| 2104  |     |     | zephyr-hm    | Zephyr Host Manager                             |
| 2401  |     |     | cvspserver   | Concurrent Versions System                      |
| 2809  |     |     | corbaloc     | Common Object Request Broker Architecture       |
| 3306  |     |     | mysql        | MySQL Datenbankservice (auch für MariaDB)       |
| 4321  |     |     | rwhois       | Remote Whois Service                            |
| 5999  |     |     | cvsup        | CVSup                                           |
| 6000  |     |     | X11          | X Windows System Services                       |
| 11371 |     |     | pgpkeyserver | Öffentlicher Keyserver für PGP                  |
| 13720 |     |     | bprd         | Symantec/Veritas NetBackup                      |
| 13721 |     |     | bpdbm        | Symantec/Veritas Database Manager               |
| 13724 |     |     | vnetd        | Symantec/Veritas Network Utility                |
| 13782 |     |     | bpcd         | Symantec/Veritas NetBackup                      |
| 13783 |     |     | vopied       | Symantec/Veritas VOPIE                          |
| 22273 |     |     | wnn6         | Kana/Kanji-Konvertierung                        |
| 23399 |     |     |              | Skype (inoffiziell)                             |
| 25565 |     |     |              | Minecraft                                       |
| 26000 |     |     | quake        | Quake und andere Mehrspieler-Games              |
| 27017 |     |     |              | MongoDB                                         |
| 33434 |     |     | traceroute   | Netzwerk-Tracking                               |