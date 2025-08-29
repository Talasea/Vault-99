# Phase Analysis and Next Steps

## Übersicht der neuen Phasen der Cyber Kill Chain

---

### 1. Reconnaissance (Vertieft)
- **Durchgeführte Aktionen**: LDAP/SMB-Abfragen, Kerberoasting, AS-REP-Brute-Forcing
- **Ergebnisse**:
  - Kerberoast-Hashes von `sansa.stark`, `jon.snow`, `sql_svc` extrahiert
  - Passwort `iknownothing` für `jon.snow` über John the Ripper geknackt
  - AS-REP für `brandon.stark` geknackt: Passwort `iseedeadpeople`
  - Anschließender Zugriffserhalt via CrackMapExec auf Windows-Hosts

### 2. Lateral Movement
- **Durch Tools**: `crackmapexec`, `smbclient`
- **Ergebnisse**:
  - Erfolgreiche Anmeldung als `jon.snow` auf `WINTERFELL` und `CASTELBLACK`
  - Enumeration von Shares, Gruppen und Benutzern auf `WINTERFELL`
  - Zugriff auf NETLOGON (`script.ps1`, `secret.ps1`)
  - Mit `samwell.tarly:Heartsbane` Zugriff auf \`//192.168.20.22/public` und Herunterladen von `arya.txt`

### 3. Privilege Escalation
- **Hinweise**:
  - `jon.snow` gehört zu sensiblen Gruppen (`Domain Admins`, `Stark`)
  - GPO "StarkWallpaper" identifiziert
  - AdminSDHolder-Container beobachtet erhöhte Rechte

### 4. Exfiltration und Persistence
- **Momentaner Stand**: GEO-Lab-Daten sichern (NETLOGON/SYSVOL Dateien)
- **Geplante Schritte**:
  - Analyse von `secret.ps1` und `script.ps1` auf Credentials oder Persistence
  - Abgleich mit GPO-Inhalten in SYSVOL auf ungewöhnliche Skripte

## Dokumentation der genutzten Tools

| Tool                  | Zweck                                             |
|-----------------------|---------------------------------------------------|
| impacket/GetUserSPNs  | Kerberoasting Hash-Extraktion                     |
| John the Ripper       | Offline-Knacken von Kerberos-Hashes               |
| hashcat               | AS-REP-Brute-Force Angriff                        |
| CrackMapExec (CME)    | SMB-Login, Share-/User-/Group-Enumeration         |
| smbclient             | Manuelles Durchsuchen und Herunterladen von Dateien |
| ldapsearch            | LDAP-Dump des AD-Schemas und Objekte               |
| nmap                  | Netzwerk- und Port-Scan                            |

## Neue Ansätze und weitere Schritte

1. **GPO-Analyse**: Überprüfe `SYSVOL\Policies\{EE353C6E-B5DD-...}` auf schadhafte Skripte.
2. **Credential Dumping**: Nutze `Invoke-Mimikatz` aus NETLOGON-Skripten, um LSASS-Dumps zu extrahieren.
3. **DC-Recon**: Versuche über LDAPS auf Domain Controller mit `iseedeadpeople` und `iknownothing`.
4. **Persistence Mechanismen**: Suche nach neuen Scheduled Tasks/SERVICES via `wmic` oder `PowerShell`.
5. **Exfiltration**: Sichere relevante Skripte und AD-Konfigurationsdateien (GPO, ServicePrincipals).

---

*Ende des Berichts*