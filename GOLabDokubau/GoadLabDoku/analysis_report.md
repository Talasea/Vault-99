# Analyse der neuen Phasen der Cyber Kill Chain

## 1. Zusammenfassung der Ergebnisse
- **Initial Reconnaissance**: Erkennung der Active Directory Domäne (north.sevenkingdoms.local) und Benutzerstruktur mittels `ldapsearch` und `crackmapexec`.
- **Weaponization**: Kerberos TGS-REP und AS-REP Hashes extrahiert (kerberoast.txt, asrep_hashes.txt) und mit John/Hashcat geknackt.
- **Delivery & Exploitation**: Gültige Credentials (jon.snow:iknownothing, samwell.tarly:Heartsbane) gewonnen und SMB-Zugriff auf NETLOGON/SYSVOL sowie Freigaben erlangt.
- **Installation**: Download von sensiblen Dateien (script.ps1, secret.ps1, arya.txt, connys_textdatei.txt, Test.txt).
- **Command & Control**: Persistenz und Delegation nicht final analysiert.

## 2. Neue Ansätze und weitere Schritte
1. **Pass-the-Hash / Pass-the-Ticket**: Nutzung der geknackten Kerberos-Tickets zur lateralen Bewegung (z.B. weiterer RODCs).
2. **Abuse of Delegation**: Prüfen der `msDS-AllowedToDelegateTo` Attribute bei jon.snow zur Service-Delegation Ausnutzung.
3. **GPO Abuse**: Analyse des Group Policy Container `{EE353C6E-B5DD-4C0A-B3BB-9A58D54B703D}` (StarkWallpaper) zur Ausführung von GPO-basierten Backdoors.
4. **DCSync**: Mit sql_svc Account evtl. Replikationsrechte prüfen (`DS-Replication-Get-Changes` Delegate).
5. **Kerberoasting**: Erweiterung auf weitere ServicePrincipalNames (HTTP, CIFS) für weitere Accounts.

## 3. Genutzte Tools
- `GetUserSPNs.py` (Impacket): Extraktion von SPNs für Kerberoasting.
- `john`, `hashcat`: Offline-Cracking von Kerberos TGS-REP & AS-REP Hashes.
- `crackmapexec`: SMB-Service-Enumeration, User/Group/Share-Abfragen.
- `ldapsearch`: LDAP-Enumeration der Domänenstruktur und Objekte.
- `smbclient`: Download von Dateien aus NETLOGON, SYSVOL, Freigaben.
- `nmap`: Portscan zur Identifizierung gefilterter und offener AD-Ports.

## 4. Dokumentation und Notion-Format
- Diese Analyse wird als `.md` Dokument bereitgestellt.
- Für Notion: Duplizieren und in Notion importieren.

---

*Ende der Analyse*