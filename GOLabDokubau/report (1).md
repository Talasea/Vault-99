# Cyber Kill Chain Analysis - Phase: Exploitation & Post-Exploitation

## Zusammenfassung der neuen Ergebnisse

### Gecrackte Credentials
- **Brandon Stark** (AS-REP): Passwort `iseedeadpeople` via Hashcat[1]
- **Jon Snow** (TGS-REP): Passwort `iknownothing` via John the Ripper[2]
- **Samwell Tarly** (Password: `Heartsbane`) manuell genutzt für SMB-Share Zugriff

### Zugriff auf SMB-Shares
- **WINTERFELL** (192.168.20.11) NETLOGON & SYSVOL: Download von `script.ps1` (165 Bytes) und `secret.ps1` (869 Bytes)
- **CASTELBLACK** (192.168.20.22) ALL-Share: Zugriff mit `samwell.tarly:Heartsbane`, Download von `arya.txt` (413 Bytes)

### LDAP-Abfragen
- Vollständiger Abgleich aller Objekte unter `dc=north,dc=sevenkingdoms,dc=local` mit LDAP[3]
- Erkennung kritischer Objekte und Gruppen (Domain Admins, krbtgt)

## Dokumentation der genutzten Tools

| Tool                   | Zweck                                      | Ergebnis                          |
|------------------------|--------------------------------------------|-----------------------------------|
| `GetUserSPNs.py`       | Extrahieren von SPN-Hashes                 | Kerberoast-Hashes                 |
| `john`                 | Offline-Passwort-Cracking (kerb TGS)       | `iknownothing`                    |
| `hashcat`              | Offline-Passwort-Cracking (AS-REP)         | `iseedeadpeople`                  |
| `crackmapexec smb`     | SMB-Share-Enumeration & Authentifizierung   | Share-Zugriff, Downloads          |
| `smbclient`            | Manuelles SMB-Datei-Listing & -Download    | NETLOGON/SYSVOL, ALL-Share        |
| `ldapsearch`           | LDAP-Directory-Enumeration                 | Vollständiger AD-Abzug            |
| `nmap`                 | Port- und Dienst-Scan                      | Gefilterte AD-Ports auf BRAAVOS    |
| `enum4linux`           | SMB-Info-Abfrage (Fails)                   | Keine Domain-Info BRAAVOS         |

## Neue Ansätze & Weitere Schritte

1. **Credential Pivoting**: Nutzen der gewonnenen `samwell.tarly`- und `jon.snow`-Credentials, um interne Dienste (WinRM, DCOM) anzuzapfen.
2. **Abdeckung TGS-Hashes**: Versuchen, weitere TGS-Hashes mit alternativen Wordlists oder Rulesets zu knacken.
3. **LDAP-Mining**: Filtern nach sensiblen Attributen (z.B. `msDS-AllowedToDelegateTo`, `adminCount`), um Delegations- und Privilege-Escalation-Pfade zu identifizieren.
4. **GPO-Abgleich**: Auswertung der geladenen GPO-Container `{EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}` für potenzielle Angriffsflächen (z.B. script.ps1 in NETLOGON).
5. **Service Account Abuse**: Überprüfen von `sql_svc`, `krbtgt`, `cloudbase-init` auf schwache Einstellungen und potenzielle Kerberoast-Ziele.
6. **RID Bruteforce**: Einsatz von `impacket-rpcdump` gegen `WINTERFELL` und `CASTELBLACK`, um versteckte Gruppen oder ACL-Einträge auszulesen.
7. **Exfiltration via SMB**: Konfigurierte SMB-Share `all` für Konfig-Exfil mittels automatisierter Skripte.

## Weiteres Vorgehen

- Automatisierte Python-Skripte entwickeln, um LDAP-Dumps zu parsen und Alerts bei kritischen Funden zu generieren.
- Integration von `BloodHound` für graphbasierte AD-Analyse.
- Bewertung von PS-Remoting via `Invoke-Command` unter PowerShell-Session.
- Dokumentation aller Schritte in Notion mit Templates und Task-Checks.

---
*Ende des Reports*