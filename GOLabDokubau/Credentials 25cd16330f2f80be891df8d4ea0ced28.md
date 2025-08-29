# Credentials

# GOAD Lab - Comprehensive Overview: Vulnerabilities, Users & Compromised Credentials

## 1. Summary of All Identified Vulnerabilities

| Schwachstelle | Betroffene Hosts | Schweregrad | Empfehlung |
| --- | --- | --- | --- |
| SMB Signing deaktiviert | BRAAVOS (192.168.20.23) | Kritisch | SMB-Signierung erzwingen (GPO/Registry) |
| SMB Signing optional | CASTELBLACK (192.168.20.22) | Hoch | SMB-Signierung verpflichtend aufnehmen |
| HTTP TRACE aktiviert | KINGSLANDING, CASTELBLACK, BRAAVOS | Hoch | TRACE in IIS deaktivieren |
| Anonymer LDAP Bind | alle Domain Controller (192.168.20.10-12) | Mittel | Anonymous LDAP-Bind blockieren |
| Selbst-signierte Zertifikate | alle Windows-Hosts | Mittel | Vertrauenswürdige CA-Zertifikate einsetzen |
| Gastaccount aktiviert | MEEREEN, BRAAVOS | Niedrig | Gastkonto deaktivieren |
| Zeitabweichungen (Kerberos) | MEEREEN, BRAAVOS | Niedrig | NTP-Synchronisierung korrigieren |
| Kerberoasting (Service Accounts) | jon.snow, sansa.stark, sql_svc | Kritisch | Service Account Härtung, starke Passwörter |
| AS-REP Roasting (PreAuthDisabled) | brandon.stark | Hoch | Pre-Auth forceren, Passwortkomplexität steigern |
| XP_CMDSHELL auf SQL Server potenziell | CASTELBLACK, BRAAVOS | Hoch | xp_cmdshell deaktivieren, least privilege |

---

## 2. Kompromittierte Credentials & Passwörter

### 2.1 Erfolgreich geknackte Passwörter

| Benutzername | Domain | Passwort | Angriffsmethode | Status | Verwendung |
| --- | --- | --- | --- | --- | --- |
| **jon.snow** | north.sevenkingdoms.local | **iknownothing** | Kerberoasting | ✅ Bestätigt | SMB-Login, WinRM, SQL-Zugriff |
| **brandon.stark** | north.sevenkingdoms.local | **iseedeadpeople** | AS-REP Roasting | ✅ Bestätigt | Domain-Authentifizierung |
| **samwell.tarly** | north.sevenkingdoms.local | **Heartsbane** | Default/Bekannt | ✅ Bestätigt | SMB-Share-Zugriff auf CASTELBLACK |
| **hodor** | north.sevenkingdoms.local | **hodor** | Default/Schwach | ✅ Bestätigt | Initial SPN-Enumeration |

### 2.2 In Bearbeitung befindliche Hashes

| Benutzername | Domain | Hash-Typ | Status | Geschätzte Zeit |
| --- | --- | --- | --- | --- |
| **sansa.stark** | north.sevenkingdoms.local | Kerberos TGS | 🔄 Wird geknackt | 2-24 Stunden |
| **sql_svc** | north.sevenkingdoms.local | Kerberos TGS | 🔄 Wird geknackt | 1-12 Stunden |
| **administrator** | sevenkingdoms.local | NTLM | 🔄 DCSync ausstehend | Nach DCSync |
| **administrator** | essos.local | NTLM | 🔄 DCSync ausstehend | Nach DCSync |

### 2.3 Service Principal Names (SPNs) und zugehörige Accounts

| Service Principal Name | Account | Domain | Status |
| --- | --- | --- | --- |
| **CIFS/thewall.north.sevenkingdoms.local** | jon.snow | north.sevenkingdoms.local | ✅ Kompromittiert |
| **HTTP/thewall.north.sevenkingdoms.local** | jon.snow | north.sevenkingdoms.local | ✅ Kompromittiert |
| **HTTP/eyrie.north.sevenkingdoms.local** | sansa.stark | north.sevenkingdoms.local | 🔄 In Bearbeitung |
| **MSSQLSvc/castelblack.north.sevenkingdoms.local** | sql_svc | north.sevenkingdoms.local | 🔄 In Bearbeitung |
| **MSSQLSvc/castelblack.north.sevenkingdoms.local:1433** | sql_svc | north.sevenkingdoms.local | 🔄 In Bearbeitung |

---

## 3. User- und Account-Übersicht aller Server

### 3.1 Domain Controller: KINGSLANDING (192.168.20.10 - sevenkingdoms.local)

| Benutzer | SamAccountName | Passwort Status | Rolle/Group Membership | Beschreibung |
| --- | --- | --- | --- | --- |
| Administrator | administrator | 🔄 Unbekannt | Domain Admins | Default domain admin |
| Guest | guest | ❌ Deaktiviert | Guests | Default guest account |
| krbtgt | krbtgt | 🔄 Unbekannt | None | Kerberos Ticket-Granting |
| jon.snow | jon.snow | ✅ **iknownothing** | Night Watch | Kerberoastable, constrained |
| brandon.stark | brandon.stark | ✅ **iseedeadpeople** | None | AS-REP vulnerable |
| sansa.stark | sansa.stark | 🔄 In Bearbeitung | Stark | Kerberoastable |
| samwell.tarly | samwell.tarly | ✅ **Heartsbane** | Domain Users | Default user |
| sql_svc | sql_svc | 🔄 In Bearbeitung | None | SQL Service Account |

### 3.2 Domain Controller: WINTERFELL (192.168.20.11 - north.sevenkingdoms.local)

| Benutzer | SamAccountName | Passwort Status | Rolle/Group Membership | Beschreibung |
| --- | --- | --- | --- | --- |
| Administrator | administrator | 🔄 Unbekannt | Domain Admins | Child domain admin |
| Guest | guest | ❌ Deaktiviert | Guests | Default guest account |
| krbtgt | krbtgt | 🔄 Unbekannt | None | Kerberos TGT |
| jon.snow | jon.snow | ✅ **iknownothing** | Night Watch | **KOMPROMITTIERT** |
| brandon.stark | brandon.stark | ✅ **iseedeadpeople** | None | **KOMPROMITTIERT** |
| sansa.stark | sansa.stark | 🔄 In Bearbeitung | Stark | SPN user |
| samwell.tarly | samwell.tarly | ✅ **Heartsbane** | Domain Users | **KOMPROMITTIERT** |
| sql_svc | sql_svc | 🔄 In Bearbeitung | None | SQL Service Account |
| hodor | hodor | ✅ **hodor** | Domain Users | **KOMPROMITTIERT** |

### 3.3 Domain Controller: MEEREEN (192.168.20.12 - essos.local)

| Benutzer | SamAccountName | Passwort Status | Rolle/Group Membership | Beschreibung |
| --- | --- | --- | --- | --- |
| Administrator | administrator | 🔄 Unbekannt | Domain Admins | Forest root admin |
| Guest | guest | ✅ **Leer/Anonym** | Guests | **KOMPROMITTIERT** (Anonym) |
| krbtgt | krbtgt | 🔄 Unbekannt | None | Kerberos TGT |
| jon.snow | jon.snow | ✅ **iknownothing** | None | Cross-forest user |
| brandon.stark | brandon.stark | ✅ **iseedeadpeople** | None | Cross-forest user |
| sansa.stark | sansa.stark | 🔄 In Bearbeitung | None | Cross-forest user |
| samwell.tarly | samwell.tarly | ✅ **Heartsbane** | Domain Users | Default user |
| sql_svc | sql_svc | 🔄 In Bearbeitung | None | Cross-forest SQL account |

### 3.4 SQL Server: CASTELBLACK (192.168.20.22)

| Benutzer | Konto | Passwort Status | Rolle/Group Membership | Beschreibung |
| --- | --- | --- | --- | --- |
| sql_svc | NORTH\sql_svc | 🔄 In Bearbeitung | SQL SysAdmin | SQL Service Account |
| jon.snow | NORTH\jon.snow | ✅ **iknownothing** | SQL User | **SMB-Zugriff bestätigt** |
| samwell.tarly | NORTH\samwell.tarly | ✅ **Heartsbane** | SQL User | **SMB-Share-Zugriff** |
| brandon.stark | NORTH\brandon.stark | ✅ **iseedeadpeople** | SQL User | Cross-domain user |
| administrator | NORTH\administrator | 🔄 Unbekannt | sysadmin | SQL Server Admin |

### 3.5 SQL Server: BRAAVOS (192.168.20.23)

| Benutzer | Konto | Passwort Status | Rolle/Group Membership | Beschreibung |
| --- | --- | --- | --- | --- |
| sql_svc | ESSOS\sql_svc | 🔄 In Bearbeitung | SQL SysAdmin | SQL Service Account |
| jon.snow | ESSOS\jon.snow | ✅ **iknownothing** | SQL User | Cross-domain user |
| samwell.tarly | ESSOS\samwell.tarly | ✅ **Heartsbane** | SQL User | Cross-domain user |
| brandon.stark | ESSOS\brandon.stark | ✅ **iseedeadpeople** | SQL User | Cross-domain user |
| administrator | ESSOS\administrator | 🔄 Unbekannt | sysadmin | SQL Server Admin |
| guest | ESSOS\guest | ✅ **Leer/Anonym** | Guests | **SMB-Anonym-Zugriff** |

---

## 4. Erfolgreiche Verbindungen und Zugriffswege

### 4.1 Bestätigte SMB-Zugriffe

| Benutzer | Passwort | Erfolgreicher Zugriff auf | Share-Zugriffe |
| --- | --- | --- | --- |
| **jon.snow** | **iknownothing** | 192.168.20.11 (WINTERFELL) | ✅ NETLOGON, ✅ SYSVOL |
| **samwell.tarly** | **Heartsbane** | 192.168.20.22 (CASTELBLACK) | ✅ ALL (arya.txt, connys_textdatei.txt, Test.txt) |
| **guest** | **(leer)** | 192.168.20.12 (MEEREEN) | ✅ Anonymer Zugriff |
| **guest** | **(leer)** | 192.168.20.23 (BRAAVOS) | ✅ Anonymer Zugriff |

### 4.2 Heruntergeladene und analysierte Dateien

| Datei | Quelle | Größe | Inhalt/Bedeutung |
| --- | --- | --- | --- |
| **script.ps1** | [//192.168.20.11/NETLOGON](https://192.168.20.11/NETLOGON) | 165 Bytes | PowerShell-Skript aus GPO |
| **secret.ps1** | [//192.168.20.11/SYSVOL](https://192.168.20.11/SYSVOL) | 869 Bytes | **Potentiell Credentials enthaltend** |
| **arya.txt** | [//192.168.20.22/all](https://192.168.20.22/all) | 413 Bytes | "Subject: Quick Departure" - Benutzerdaten |
| **connys_textdatei.txt** | [//192.168.20.22/all](https://192.168.20.22/all) | Variable | Benutzerdaten |
| **Test.txt** | [//192.168.20.22/all](https://192.168.20.22/all) | Variable | "Hallo das ist nur ein Testtxt / wir sind bei Hauptwindos" |

### 4.3 LDAP-Enumeration Erfolge

| Host | Domain | Zugriffsmethode | Erhaltene Informationen |
| --- | --- | --- | --- |
| 192.168.20.10 | sevenkingdoms.local | Anonymous Bind | ✅ Naming Contexts, Base DN |
| 192.168.20.11 | north.sevenkingdoms.local | Anonymous + Auth | ✅ Vollständige User/Group-Listen |
| 192.168.20.12 | essos.local | Anonymous Bind | ✅ Naming Contexts, Domain SID |

### 4.4 WinRM/PowerShell-Zugriffe

| Benutzer | Passwort | Host | Zugriffslevel |
| --- | --- | --- | --- |
| **jon.snow** | **iknownothing** | 192.168.20.11 (WINTERFELL) | ✅ PowerShell Remote Session |
| **brandon.stark** | **iseedeadpeople** | 192.168.20.11 (WINTERFELL) | 🔄 Testing ausstehend |

---

## 5. Attack Timeline & Credentials Discovery

### 5.1 Chronologische Reihenfolge der Kompromittierung

```
Stunde 0-1: Reconnaissance
├── Netzwerk-Scanning (nmap, naabu)
├── Service-Enumeration (DNS, LDAP, SMB)
└── Anonyme LDAP-Abfragen erfolgreich

Stunde 1-2: Initial Exploitation
├── GetUserSPNs.py mit hodor:hodor → SPN-Liste erhalten
├── GetNPUsers.py → brandon.stark AS-REP Hash
├── Hashcat → brandon.stark:iseedeadpeople GEKNACKT
└── John the Ripper → jon.snow:iknownothing GEKNACKT

Stunde 2-3: Lateral Movement
├── crackmapexec → Credential-Validierung erfolgreich
├── smbclient → NETLOGON/SYSVOL-Zugriff (jon.snow)
├── smbclient → ALL-Share-Zugriff (samwell.tarly)
└── evil-winrm → PowerShell-Session etabliert

Stunde 3-4: Advanced Enumeration
├── Authentifizierte LDAP-Dumps
├── BloodHound-Datensammlung vorbereitet
├── SQL Server-Enumeration
└── Weitere SPN-Hashes gesammelt (sansa.stark, sql_svc)

```

### 5.2 Credential-Cracking Statistics

| Hash-Typ | Anzahl Hashes | Erfolgreich geknackt | Erfolgsrate | Durchschnittliche Zeit |
| --- | --- | --- | --- | --- |
| AS-REP (18200) | 1 | 1 | 100% | < 5 Minuten |
| Kerberos TGS (13100) | 5 | 1 | 20% | 15 Minuten - 2 Stunden |
| NTLM (1000) | 0 | 0 | - | Ausstehend (DCSync) |

### 5.3 Wordlist-Effektivität

| Wordlist | Erfolgreiche Cracks | Verwendung |
| --- | --- | --- |
| **/usr/share/wordlists/rockyou.txt** | 2 (jon.snow, brandon.stark) | Primäre Wordlist |
| **Common-Passwords** | 0 | Backup-Wordlist |
| **Custom GOAD Wordlist** | 1 (hodor:hodor) | Domain-spezifische Begriffe |

---

## 6. Next Steps & Priority Actions

### 6.1 Immediate Actions (High Priority)

| Aktion | Ziel | Erwartetes Ergebnis | Geschätzte Zeit |
| --- | --- | --- | --- |
| **DCSync Attack** | Alle Domain Controller | Vollständige Credential-DB | 1-2 Stunden |
| **Golden Ticket Generation** | north.sevenkingdoms.local | Persistente Domain Admin-Rechte | 30 Minuten |
| **SQL xp_cmdshell Exploitation** | CASTELBLACK, BRAAVOS | System-Level Command Execution | 1 Stunde |
| **BloodHound Analysis** | Alle Domänen | Attack Path Optimization | 2 Stunden |

### 6.2 Credential Expansion (Medium Priority)

| Ziel | Methode | Erwartetes Ergebnis |
| --- | --- | --- |
| **sansa.stark** Hash-Crack | John/Hashcat + erweiterte Wordlists | Weitere Domain-Credentials |
| **sql_svc** Hash-Crack | Fokus auf SQL-spezifische Passwörter | SQL Server Service Control |
| **Administrator** Hashes | DCSync auf alle DCs | Complete Domain Takeover |
| **Cross-Domain Trusts** | Trust-Relationship-Exploitation | Enterprise Admin Escalation |

### 6.3 Persistence & C2 (Low Priority)

| Mechanismus | Implementierung | Persistenz-Level |
| --- | --- | --- |
| **GPO-basierte Persistence** | Malicious Startup Scripts | Domain-weit, hohe Stealth |
| **Service Creation** | Custom Windows Services | Pro Host, mittlere Detectability |
| **Registry Persistence** | Run Keys, WMI Events | User-Level, niedrige Stealth |
| **C2 Infrastructure** | PowerShell Empire/Covenant | Command & Control |

---

## 7. Risk Assessment

### 7.1 Current Compromise Level

```
Domain Compromise Status:
├── sevenkingdoms.local: 40% (mehrere User, kein Admin)
├── north.sevenkingdoms.local: 60% (mehrere User, PowerShell-Zugriff)
└── essos.local: 30% (Cross-Domain User, Anonymous Access)

SQL Server Compromise:
├── CASTELBLACK: 70% (SMB-Share-Zugriff, Domain User Auth)
└── BRAAVOS: 50% (Anonymous SMB, Cross-Domain Auth)

Overall Lab Compromise: ~50%

```

### 7.2 Critical Assets Status

| Asset Type | Total | Compromised | Percentage | Risk Level |
| --- | --- | --- | --- | --- |
| **Domain Controllers** | 3 | 0 (Admin) | 0% | 🟡 Medium |
| **User Accounts** | ~15 | 4 | 27% | 🔴 High |
| **Service Accounts** | 3 | 1 | 33% | 🔴 High |
| **SQL Servers** | 2 | 0 (Admin) | 0% | 🟡 Medium |
| **SMB Shares** | ~10 | 4 | 40% | 🔴 High |

---

**Status: Significanter Initial Foothold etabliert - Ready for Privilege Escalation**

---