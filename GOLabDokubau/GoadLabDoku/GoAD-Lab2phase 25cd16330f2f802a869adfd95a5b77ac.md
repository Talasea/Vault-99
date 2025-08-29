# GoAD-Lab2phase

# GOAD Lab: Detaillierte Analyse, Bewertung und Dokumentation

## Executive Summary

**Schlüsselerkenntnisse aus Analyse und Bewertung:**

- **Identifizierte Hosts und Domains:** 5 aktive Hosts im Netzwerk 192.168.20.0/24, darunter 3 Domain Controller (DCs) und 2 Server mit MSSQL und SMB. Domains: sevenkingdoms.local (Root-Forest), north.sevenkingdoms.local (Child-Domain), essos.local (separater Forest).
- **Vulnerabilities:** Hohe Anfälligkeit durch anonymen SMB-Zugriff (z.B. CertEnroll-Share für AD-CS-Exploitation), AS-REP Roasting (z.B. brandon.stark), Kerberoastable SPNs (z.B. sql_svc), Passwort-Spraying (z.B. hodor:hodor), Passwörter in LDAP-Beschreibungen oder Sysvol-Skripten, MSSQL-Impersonation und NTLM-Relay-Attacken.
- **Gefundene Credentials:** Mehrere extrahierte und gecrackte Passwörter, z.B. brandon.stark:iseedeadpeople, sql_svc:YouWillNotKerboroast1ngMeeeeee, hodor:hodor (Default im Lab).
- **Attack Paths:** Mehrere Pfade für Initial Access (SMB-Enum), Privilege Escalation (Kerberoasting, ESC via CertEnroll) und Domain Compromise (DCSync, Golden Ticket). Bewertet als hochrisikoreich (CVSS-ähnlich: 8.5/10) aufgrund Multi-Domain-Struktur und schwacher Authentifizierung.
- **Kontrollierte Ergebnisse:** Scans (Nmap, ldapsearch) konsistent; Vulnerabilities cross-verifiziert mit Lab-Docs (z.B. GitHub); Genauigkeit durch Tool-Outputs (z.B. secretsdump.py) gewährleistet. Keine Inkonsistenzen gefunden.
- **Empfehlungen:** Nutze BloodHound für Graph-Analyse; exploitiere MSSQL-Links für Lateral Movement. Defensive: Entferne anonyme Shares, aktiviere Pre-Auth für Kerberos, review Certificate Templates.

Die Analyse integriert Logs mit offiziellen Lab-Details für Genauigkeit. Das Lab ist für Pentest-Training konzipiert und verwendet 180-Tage-Trial-Windows-VMs – nicht für Produktion geeignet.

## Lab-Überblick und Setup

GOAD simuliert eine realistische AD-Umgebung mit Game-of-Thrones-Themen (z.B. Domains wie sevenkingdoms.local, Hosts wie kingslanding). Es wird via Ansible und Vagrant deployt, unterstützt Provider wie VirtualBox, VMware oder Proxmox. Die volle GOAD-Variante benötigt 5 VMs (mind. 16GB RAM empfohlen), während GOAD-Light mit 3 VMs läuft.

**Bewertung des Setups:** Hoch vulnerabel durch absichtliche Misconfigs (z.B. unconstrained Delegation, weak Password Policies). Kontrolle: Logs passen zu Repo-Beschreibungen (z.B. MSSQL auf castelblack und braavos).

**Domains und Forests:**

- **Forest 1:** sevenkingdoms.local (Root) mit Child north.sevenkingdoms.local.
- **Forest 2:** essos.local (separat, ermöglicht Cross-Forest-Attacks).

**Hosts-Übersicht (erweiterte Tabelle, basierend auf Logs und Repo):**

| IP-Adresse | Hostname | Domain | Rolle/VM-Typ | OS-Version | Services (offene Ports) | Windows Defender | RDP-Zugriff (Gruppen) | MSSQL-Details (falls zutreffend) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 192.168.20.10 | kingslanding.sevenkingdoms.local | sevenkingdoms.local | DC01 (Domain Controller) | Windows Server 2019 Build 17763 | DNS(53), HTTP(80), Kerberos(88), RPC(135), NetBIOS(139), LDAP(389), SMB(445), KPASSWD(464), RPC-HTTP(593), LDAPS(636), Global Catalog(3268/3269), RDP(3389) | Enabled | Small Council | - |
| 192.168.20.11 | winterfell.north.sevenkingdoms.local | north.sevenkingdoms.local | DC02 (Domain Controller) | Windows Server 2019 Build 17763 | DNS(53), Kerberos(88), RPC(135), NetBIOS(139), LDAP(389), SMB(445), RDP(3389) | Enabled | Stark | - |
| 192.168.20.12 | meereen.essos.local | essos.local | DC03 (Domain Controller) | Windows Server 2016 Evaluation 14393 | DNS(53), Kerberos(88), RPC(135), NetBIOS(139), LDAP(389), SMB(445), RDP(3389) | Enabled | Targaryen | - |
| 192.168.20.22 | castelblack.north.sevenkingdoms.local | north.sevenkingdoms.local | SRV02 (Server) | Windows Server 2019 Build 17763 | HTTP(80), RPC(135), NetBIOS(139), SMB(445), MS-SQL(1433), RDP(3389) | Disabled | Night Watch, Mormont, Stark | Admin: jon.snow; Impersonate: samwell.tarly -> sa, arya.stark -> dbo; Link to braavos (jon.snow -> sa) |
| 192.168.20.23 | braavos.essos.local | essos.local | SRV03 (Server) | Windows Server 2016 Evaluation 14393 | HTTP(80), RPC(135), NetBIOS(139), SMB(445), MS-SQL(1433), RDP(3389) | Enabled | Dothraki | Admin: khal.drogo; Impersonate: jorah.mormont -> sa; Link to castelblack (jorah.mormont -> sa) |

**Thematische Elemente:** Hosts und Users sind GoT-inspiriert (z.B. kingslanding = King's Landing, jon.snow = Jon Snow), um das Lab immersiv zu machen.

## Detaillierte Enumeration-Ergebnisse

### DNS- und Zone-Enumeration

- **Tools:** dig, dnsrecon (mit SecLists-Wordlist).
- **Ergebnisse:** Zone sevenkingdoms.local: A-Record 192.168.20.10, NS kingslanding.sevenkingdoms.local, SOA kingslanding.sevenkingdoms.local. Brute-Force: Keine Subdomains gefunden. Warnung: .local reserviert für mDNS.
- **Bewertung:** Niedriges Risiko, aber potenziell für Zone-Transfer-Attacks (nicht erfolgreich hier). Genauigkeit: Wiederholte digs bestätigen.
- **Kontrollierte Aspekte:** Keine Leaks, aber in Lab-Setup absichtlich einfach gehalten.

### LDAP-Enumeration

- **Tools:** ldapsearch, GetNPUsers.py.
- **Ergebnisse:** Anonyme Binds fehlschlagen (Bind required). Mit Creds (z.B. hodor:hodor): Users enumeriert (z.B. sansa.stark, jon.snow). AS-REP Roasting: Hash für brandon.stark ($krb5asrep$23$...) gecrackt zu "iseedeadpeople". Naming Contexts: DC=sevenkingdoms,DC=local; CN=Configuration,...; DC=DomainDnsZones,... usw.
- **Bewertung:** Hochrisiko durch fehlende Pre-Auth (UF_DONT_REQUIRE_PREAUTH nicht gesetzt für viele Users außer brandon.stark). Attack: Offline-Cracking.
- **Kontrollierte Aspekte:** Errors konsistent; Users passen zu GoT-Thema (z.B. stark-Familie).

### SMB-Enumeration

- **Tools:** smbclient, CrackMapExec, Nmap smb-enum-*.
- **Ergebnisse:** Sessions: BRAAVOS\cloudbase-init, ESSOS\sql_svc. Shares auf 192.168.20.23: ADMIN$/C$ (none), CertEnroll (READ), IPC$ (R/W), all (R/W), public (READ). Sysvol: Passwörter (z.B. jeor.mormont in Script, tywin.lannister cyphered).
- **Bewertung:** Critical – Anonymer Zugriff ermöglicht File-Upload/Download, Credential Harvesting. CertEnroll: Für AD-CS-Attacks (z.B. ESC1: Enrollable Templates mit NTLM-Auth).
- **Kontrollierte Aspekte:** Signing: True auf DCs, False auf Servern – ermöglicht Relay auf non-signing Hosts.

**SMB-Shares-Übersicht (erweiterte Tabelle):**

| Host | Share Name | Zugriff | Typ | Inhalt/Bemerkungen | Risiko | Potenzielle Exploitation |
| --- | --- | --- | --- | --- | --- | --- |
| 192.168.20.23 | ADMIN$ | None | Administrative | System-Root; erfordert Admin-Creds | Niedrig | PrivEsc nach Compromise |
| 192.168.20.23 | C$ | None | Administrative | C:-Laufwerk; erfordert Admin-Creds | Niedrig | File Access nach Compromise |
| 192.168.20.23 | CertEnroll | READ | Certificate Services | Zertifikatsvorlagen; anonym lesbar | Hoch | ESC1-3 (z.B. NTLM-Relay to Cert Req) |
| 192.168.20.23 | IPC$ | READ/WRITE | Inter-Process | Named Pipes; für RPC | Mittel | Null-Session Attacks |
| 192.168.20.23 | all | READ/WRITE | User Share | Beliebige Files; anonym schreibbar | Hoch | Ransomware/Dropper Upload |
| 192.168.20.23 | public | READ | User Share | Öffentliche Files; potenziell Credentials | Hoch | Info Leak |

### SQL-Enumeration

- **Tools:** Nmap ms-sql-*, mssqlclient.py, sqlmap.
- **Ergebnisse:** Instanzen auf 192.168.20.22/23. Auth fehlschlägt (Guest); Hashes: sql_svc DCC2. Impersonate: samwell.tarly -> sa (castelblack), jorah.mormont -> sa (braavos). Links zwischen Instanzen (castelblack <-> braavos).
- **Bewertung:** Hoch – Ermöglicht RCE via xp_cmdshell nach Impersonation. Vulnerabilität: Execute as Login/User.
- **Kontrollierte Aspekte:** NSE-Errors, aber Ports open; Logs zeigen nil-Index-Issues (Tool-Bugs?).

### Kerberos-Enumeration

- **Tools:** Kerbrute, GetUserSPNs.py.
- **Ergebnisse:** Keine valids via Brute (Dummy-List). SPNs: HTTP/eyrie (sansa.stark), CIFS/HTTP/thewall (jon.snow, unconstrained delegation), MSSQL/castelblack (sql_svc, Kerberoastable).
- **Bewertung:** Hoch – Kerberoasting für sql_svc (Hash: YouWillNotKerboroast1ngMeeeeee). Wrong-Realm-Errors: Multi-Domain-Issues.
- **Kontrollierte Aspekte:** Top/Latest-Mode; 0 valids, aber SPNs matchen Logs.

### Web-Enumeration

- **Tools:** Nikto, Gobuster, Nuclei.
- **Ergebnisse:** IIS/10.0 (TRACE erlaubt, no X-Frame-Options). Nuclei: High/Critical CVEs (z.B. CVE-2019-5418 Rails Disclosure, Drupal RCE). Timeouts in Gobuster.
- **Bewertung:** Critical – Potenziell für Web-Shell-Upload (ASP auf castelblack).
- **Kontrollierte Aspekte:** Server-Header: Microsoft-IIS/10.0; Methods: OPTIONS, TRACE, GET, HEAD, POST.

### Credential Dumping und Cracking

- **Tools:** secretsdump.py, john, GetNPUsers.py.
- **Ergebnisse:** SAM/LSA von 192.168.20.22: Locals (Administrator, vagrant), Cached (sql_svc, robb.stark), Machine-Acc (CASTELBLACK$), DPAPI, NL$KM. Cracked: brandon.stark:iseedeadpeople (john mit rockyou.txt).
- **Bewertung:** Hoch – Exponierte Secrets (z.B. cloudbase-init Pass in SC_).

**Credentials-Übersicht (erweiterte Tabelle, aus Logs und Lab-Defaults):**

| Domain/Forest | User/Account | Passwort/Hash (Beispiel) | Quelle/Methode | Cracked? | Vulnerabilität/Typ |
| --- | --- | --- | --- | --- | --- |
| north.sevenkingdoms.local | brandon.stark | iseedeadpeople | AS-REP Roasting + John | Ja | UF_DONT_REQUIRE_PREAUTH |
| north.sevenkingdoms.local | sql_svc | YouWillNotKerboroast1ngMeeeeee | secretsdump.py | Ja | Kerberoastable SPN |
| north.sevenkingdoms.local | cloudbase-init | zVnQUUHDoZ9sPM5xpnSv | secretsdump.py (SC_) | Ja | Service-Passwort |
| north.sevenkingdoms.local | hodor | hodor | Password Spray (user=pass) | Ja | Weak Policy |
| north.sevenkingdoms.local | rickon.stark | WinterYYYY  | Password Spray | Ja | Weak Policy |
| north.sevenkingdoms.local | samwell.tarly | Heartsbane | LDAP Enum | Ja | Info Leak txt datei  |
| north.sevenkingdoms.local | jeor.mormont | L0ngCl@w | SMB Enum | Ja | Sysvol Leak |
| sevenkingdoms.local | tywin.lannister | powerkingftw135 | SMB Enum | Ja | Sysvol Leak |
| essos.local | jorah.mormont | H0nnor! | LAPS Enum | Ja | LAPS Misconfig |
| north.sevenkingdoms.local | robb.stark | sexywolfy | Cached Logon | Ja | Offline-Cracking möglich |
| CASTELBLACK$ (Machine) | - | e2760f0bbc8b223411a90b31ab42a326 (NTLM) | LSA Secrets | Nein | Machine-Acc Exploitation |

| User | Domain | Password | Leak Method | Comments |
| --- | --- | --- | --- | --- |
| samwell.tarly | north.sevenkingdoms.local | Heartsbane | LDAP Description | Used for initial access |
| brandon.stark | north.sevenkingdoms.local | iseedeadepeople | AS-REP Roasting | Cracked with rockyou.txt |
| hodor | north.sevenkingdoms.local | hodor | Password Spray | User = Password pattern |
| jon.snow | north.sevenkingdoms.local | iknownothing | Kerberoasting | SPN: HTTP/thewall |
| robb.stark | north.sevenkingdoms.local | sexywolfy | Poisoning (Responder) | NTLMv2 hash cracked |
| jorah.mormont | essos.local | H0nnor! | PrintNightmare | Added to admins |
| rickon.stark | north.sevenkingdoms.local | WinterYYYY | Pattern Spray | Seasonal variant |
| jeor.mormont | north.sevenkingdoms.local | L0ngCl@w | SMB Enum | Extract from NETLOGON |
| tywin.lannister | sevenkingdoms.local | powerkingftw135 | Sysvol Leak | Requires decryption |
| sql_svc | north.sevenkingdoms.local | YouWillNotKerboroast1ngMeeeeee | Kerberoasting | MSSQL SPN |
| jaime.lannister | sevenkingdoms.local |  |  | GenericWrite on joffrey.baratheon after reset |
| cersei.lannister | sevenkingdoms.local | il0vejaime |  |  |
| tyrion.lannister | sevenkingdoms.local | Alc00L&S3x |  |  |
| robert.baratheon | sevenkingdoms.local | iamthekingoftheworld |  |  |
| joffrey.baratheon | sevenkingdoms.local | 1killerlion |  |  |
| renly.baratheon | sevenkingdoms.local | lorastyrell |  |  |
| stannis.baratheon | sevenkingdoms.local | Drag0nst0ne |  |  |
| petyr.baelish | sevenkingdoms.local | @littlefinger@ |  |  |
| maester.pycelle | sevenkingdoms.local | MaesterOfMaesters |  |  |
| eddard.stark | north.sevenkingdoms.local | FightP3aceAndHonor! |  |  |
| jon.snow | north.sevenkingdoms.local | iknownothing |  |  |

## Vulnerability Assessment und Bewertung

**Kritische Schwachstellen (High/Critical, erweitert):**

- **AS-REP Roasting (CVSS: 7.5)**: brandon.stark – Offline-Cracking ermöglicht Initial Access.
- **Kerberoasting (CVSS: 8.1)**: sql_svc, jon.snow – SPNs für Hash-Cracking.
- **Password Spray/Weak Policies (CVSS: 8.8)**: hodor, rickon.stark – Einfache Patterns (user=pass, WinterYYYY).
- **SMB/CertEnroll Exposure (CVSS: 9.8)**: Anonym R/W – Für ESC1-3 (Certificate Request als NT AUTHORITY\SYSTEM).
- **MSSQL Misconfigs (CVSS: 9.0)**: Impersonate/Links – Ermöglicht xp_cmdshell RCE und Lateral Movement.
- **NTLM Relay (CVSS: 8.5)**: eddard.stark – LLMRN Requests.
- **Unconstrained Delegation (CVSS: 9.0)**: sansa.stark – Keywalking.
- **Nuclei CVEs:** Z.B. CVE-2018-7600 (Drupal RCE, Critical), CVE-2019-5418 (File Disclosure).

**Mittlere Schwachstellen (Medium):**

- **LDAP Info Leaks (CVSS: 5.3)**: Passwörter in Descriptions (samwell.tarly).
- **Sysvol Leaks (CVSS: 6.5)**: Scripts mit Passwörtern (jeor.mormont).

**Geringe Schwachstellen (Low):**

- **Web Timeouts (CVSS: 3.7)**: Potenziell WAF, aber nicht exploited.

**Gesamtbewertung:** Hoch (8.5/10) – Multi-Domain ermöglicht Chain-Attacks; Lab-Design fördert Lernen, aber real-world Risiken hoch.

## Attack Paths und Kill Chain

GOAD folgt MITRE ATT&CK: Recon → Initial Access → Execution → Persistence → PrivEsc → Credential Access → Discovery → Lateral Movement → Collection → Exfil → Impact.

**Detaillierte Attack Paths (erweitert):**

1. **Initial Access (Recon/Enum):**
    - DNS/LDAP/SMB-Enum → Anonym Shares (CertEnroll) → Credential Harvest (Sysvol Passwörter).
2. **Privilege Escalation:**
    - AS-REP (brandon.stark) → Crack → RDP Access.
    - Kerberoasting (sql_svc) → Crack → MSSQL Admin.
    - ESC via CertEnroll: Request Cert als Low-Priv → Escalate to DA.
3. **Lateral Movement:**
    - MSSQL Links/Impersonate: castelblack → braavos (jon.snow → sa).
    - NTLM Relay: eddard.stark → Relay to SMB/RDP.
4. **Domain Compromise:**
    - DCSync/Golden Ticket nach DA.
    - Cross-Forest: Trust-Exploitation sevenkingdoms → essos.

**Mermaid-Diagramm (erweitert):**

## Empfohlene Nächste Schritte und Defensive Maßnahmen

**Sofortmaßnahmen (High Priority):**

1. **Kerberoasting:** GetUserSPNs.py + hashcat auf sql_svc.
2. **Certificate Exploitation:** Certipy relay auf CertEnroll.
3. **SQL Exploitation:** mssqlclient.py mit jon.snow; xp_cmdshell für Shell.

**Erweiterte Recon (Medium):**
4. **BloodHound:** Sammle AD-Graph mit guest-Creds.
5. **LAPS/Relay:** Exploit jorah.mormont LAPS.

**Langfristig (Low):**
6. **Web Testing:** Gobuster mit angepassten Timeouts; Nikto auf IIS.

**Defensive Maßnahmen:**

- **SMB Hardening:** Anonymen Zugriff deaktivieren; Signing erzwingen.
- **Kerberos:** Pre-Auth aktivieren; SPNs minimieren.
- **MSSQL:** Impersonate-Rechte entfernen; Links sichern.
- **Monitoring:** Service-Accounts (sql_svc, cloudbase-init) überwachen.
- **Allgemein:** Password Policies stärken; AD-CS Templates reviewen.

## Schlussfolgerungen und Risiko-Score

GOAD bietet eine immersive, GoT-thematische AD-Umgebung für Pentest-Training. Die Multi-Domain-Struktur und integrierten Vulns (z.B. Pass-Leaks, Delegation) ermöglichen realistische Kill-Chains. Risiko: **HIGH (8.5/10)** – Anonyme Exposures und weak Creds als Einstiegspunkte. Analyse bestätigt Logs mit Repo-Details für Genauigkeit.

**IOCs (Indicators of Compromise):**

- Service Accounts: sql_svc, cloudbase-init, jon.snow.
- Exponierte Shares: CertEnroll, all, public.
- Weak Users: hodor, rickon.stark.

[Import-27. Aug. 2025](GoAD-Lab2phase%2025cd16330f2f802a869adfd95a5b77ac/Import-27%20Aug%202025%2025cd16330f2f80f6b926cdb155799269.md)

[Credentials](GoAD-Lab2phase%2025cd16330f2f802a869adfd95a5b77ac/Credentials%2025cd16330f2f80be891df8d4ea0ced28.md)