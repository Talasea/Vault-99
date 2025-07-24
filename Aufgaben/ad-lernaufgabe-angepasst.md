# Angepasste Active Directory Lernaufgabe für kleine Umgebung

## Szenariobeschreibung

### Unternehmenskontext

Die fiktive TechService GmbH ist ein mittelständisches IT-Dienstleistungsunternehmen mit 15 Mitarbeitern, das eine moderne, sichere und DSGVO-konforme Active Directory-Infrastruktur auf Basis von Windows Server 2022 implementieren möchte.

### Laborumgebung
- **1x Windows Server 2022** (Domain Controller, DNS, File Server)
- **3x Windows 10 Enterprise Clients** (verschiedene Abteilungen)
- **Virtualisierte Umgebung** (VMware/Hyper-V)

## Lernaufgabe: 5-Tage-Implementierungsplan

### Voraussetzung: Tag 0 - Risikoanalyse
**Zeitaufwand**: 4 Stunden

Bevor die technische Implementierung beginnt, muss eine umfassende Risikoanalyse durchgeführt werden:

1. **Risikobewertung durchführen**
   - Verwendung der bereitgestellten Risikomatrix
   - Identifikation aller 8 Hauptrisiken (R001-R008)
   - Bewertung nach Eintrittswahrscheinlichkeit und Auswirkung
   - Dokumentation der Risikobehandlungsmaßnahmen

2. **DSGVO-Compliance prüfen**
   - Prüfung der Notwendigkeit einer Datenschutz-Folgenabschätzung
   - Klassifizierung der zu verarbeitenden Datenarten
   - Definition von Aufbewahrungsfristen
   - Identifikation der erforderlichen technischen und organisatorischen Maßnahmen

3. **Freigabeentscheidung**
   - Bewertung des Gesamtrisikos
   - Entscheidung über Implementierungsfreigabe
   - Festlegung von Auflagen und Überwachungsmaßnahmen

### Tag 1 - Servergrundkonfiguration und AD-Installation
**Zeitaufwand**: 6-8 Stunden

1. **Servervorbereitungen**
   - Windows Server 2022 Installation
   - Statische IP-Konfiguration (192.168.1.10/24)
   - Computername festlegen: DC01-TECHSERVICE
   - Windows Updates installieren
   - Firewall-Grundkonfiguration

2. **Active Directory Domain Services Installation**
   - AD DS Rolle installieren
   - Domäne: techservice.local
   - NetBIOS-Name: TECHSERVICE
   - Forest-/Domain-Funktionsebene: Windows Server 2016
   - DNS-Server-Rolle mitinstallieren
   - SYSVOL- und NTDS-Pfade definieren

3. **Grundlegende OU-Struktur erstellen**
   ```
   techservice.local
   ├── TechService-Users
   │   ├── IT-Abteilung
   │   ├── Verwaltung
   │   └── Vertrieb
   ├── TechService-Computers
   │   ├── Workstations
   │   ├── Laptops
   │   └── Servers
   └── TechService-Groups
       ├── Security-Groups
       └── Distribution-Groups
   ```

### Tag 2 - Sicherheitshärtung und Kennwort-Richtlinien
**Zeitaufwand**: 6-8 Stunden

1. **Kennwort-Richtlinie konfigurieren**
   - Minimale Kennwortlänge: 14 Zeichen
   - Kennwort-Historie: 24 Kennwörter
   - Maximales Kennwortalter: 90 Tage
   - Komplexitätsanforderungen aktiviert
   - Account-Lockout nach 3 Fehlversuchen

2. **Privilegierte Konten absichern**
   - Separate Administratorkonten erstellen
   - Built-in Administrator deaktivieren
   - Service-Accounts mit minimalen Rechten
   - Admin-Gruppen bereinigen (nur erforderliche Mitglieder)

3. **Audit-Richtlinien aktivieren**
   - Directory Service Changes
   - Account Management
   - Privilege Use
   - Policy Change
   - System Events
   - Object Access (für kritische Objekte)

4. **DNS-Sicherheit**
   - DNS-Scavenging konfigurieren
   - Secure Dynamic Updates aktivieren
   - Forwarder zu sicheren DNS-Servern (1.1.1.1, 8.8.8.8)

### Tag 3 - Gruppenrichtlinien und Client-Integration
**Zeitaufwand**: 6-8 Stunden

1. **Sicherheits-GPOs erstellen**
   - **Workstation-Security-Policy**:
     - Windows Defender aktiviert
     - Windows Update automatisch
     - USB-Speicher-Beschränkungen
     - Lokale Anmeldung nur für autorisierte Benutzer
     - Bildschirmschoner mit Kennwort nach 10 Min

   - **User-Security-Policy**:
     - Software-Installation verhindern
     - Registry-Zugriff beschränken
     - Systemsteuerung-Zugriff einschränken
     - Wechselmedien-Richtlinien

2. **Windows 10 Clients in Domäne aufnehmen**
   - DNS-Server auf DC01 konfigurieren
   - Domänenbeitritt durchführen
   - Domain Users zu lokalen Benutzern hinzufügen
   - Gruppenrichtlinien-Anwendung testen

3. **Benutzer und Gruppen erstellen**
   - **Security Groups**:
     - IT-Admins (Domain Admins)
     - IT-Support (begrenzte Admin-Rechte)
     - Office-Users (Standard-Benutzer)
     - File-Access-Groups

   - **Testbenutzer pro Abteilung**:
     - max.mustermann@techservice.local (IT)
     - anna.beispiel@techservice.local (Verwaltung)
     - tom.tester@techservice.local (Vertrieb)

### Tag 4 - File-Server und Freigabe-Berechtigungen
**Zeitaufwand**: 6-8 Stunden

1. **File Services installieren**
   - File Server Rolle hinzufügen
   - DFS-Namespace konfigurieren
   - File Server Resource Manager (FSRM)

2. **Ordnerstruktur und Freigaben**
   ```
   D:\Shares\
   ├── Public (Alle: Lesen/Schreiben)
   ├── IT-Department (IT-Gruppe: Vollzugriff)
   ├── Administration (Verwaltung: Vollzugriff)
   ├── Sales (Vertrieb: Vollzugriff)
   └── Archive (Alle: Lesen, IT: Vollzugriff)
   ```

3. **NTFS- und Freigabe-Berechtigungen**
   - Security Groups für Ordner-Zugriff
   - Vererbung konfigurieren
   - Deny-Permissions vermeiden
   - Access-Based Enumeration aktivieren

4. **FSRM-Konfiguration**
   - Datei-Kontingente definieren
   - Dateigruppen für verbotene Dateitypen
   - E-Mail-Benachrichtigungen bei Überschreitungen

### Tag 5 - Backup, Monitoring und DSGVO-Compliance
**Zeitaufwand**: 6-8 Stunden

1. **Backup-Strategie implementieren**
   - Windows Server Backup installieren
   - System State Backup täglich
   - Bare Metal Recovery-Backup wöchentlich
   - Backup-Ziel: Externe USB-Festplatte und Netzwerkspeicher
   - Restore-Test durchführen

2. **Monitoring und Alerting**
   - Windows Event Forwarding konfigurieren
   - PowerShell-Skript für tägliche Gesundheitschecks
   - Critical Event Log Monitoring
   - Disk Space Monitoring
   - AD Replication Status (für zukünftige DCs)

3. **DSGVO-Compliance finalisieren**
   - **Datenklassifizierung**:
     - User-Attribute kategorisieren (Personal/Non-Personal/Sensitive)
     - Nicht erforderliche Attribute entfernen
     - Datenaufbewahrungsrichtlinien dokumentieren

   - **Betroffenenrechte implementieren**:
     - PowerShell-Skript für Datenexport (Art. 15 DSGVO)
     - Lösch-Workflow für ausgeschiedene Mitarbeiter (Art. 17 DSGVO)
     - Datenberichtigungsverfahren (Art. 16 DSGVO)

   - **Dokumentation erstellen**:
     - Verzeichnis von Verarbeitungstätigkeiten
     - TOM-Dokumentation (Technische und organisatorische Maßnahmen)
     - Incident Response Plan für Datenschutzverletzungen

4. **Abschluss-Audit**
   - Sicherheitsüberprüfung aller Konfigurationen
   - Penetrationstest der AD-Umgebung (optional)
   - Dokumentation aller Einstellungen
   - Übergabe an Betriebsteam

## Erweiterte Sicherheitsfeatures (optional)

### TLS/SSL-Verschlüsselung
- LDAPS-Zertifikat installieren
- Sichere Kanäle für LDAP erzwingen
- SMB-Verschlüsselung aktivieren

### Windows Defender Features
- Windows Defender ATP konfigurieren
- Device Guard Policies
- Credential Guard aktivieren

### Advanced Audit Features
- Privileged Access Management (PAM)
- Just-in-Time Administration
- PowerShell-Logging erweitert

## Bewertungskriterien

### Technische Umsetzung (60%)
- Korrekte AD-Installation und Konfiguration
- Funktionsfähige Gruppenrichtlinien
- Sichere Benutzer- und Gruppenverwaltung
- Backup- und Recovery-Fähigkeiten

### Sicherheit (25%)
- Implementierung der Sicherheitsrichtlinien
- Privileged Account Management
- Audit-Konfiguration
- Risikominimierung

### DSGVO-Compliance (15%)
- Datenschutzkonforme Konfiguration
- Betroffenenrechte-Implementierung
- Dokumentationsqualität
- TOM-Umsetzung

## Lernziele

Nach Abschluss der Aufgabe können die Teilnehmenden:
1. Eine sichere AD-Infrastruktur in kleinen Umgebungen planen und implementieren
2. DSGVO-konforme Einstellungen konfigurieren und dokumentieren
3. Risikobewertungen für IT-Systeme durchführen
4. Backup- und Disaster-Recovery-Strategien umsetzen
5. Monitoring und Alerting für AD-Umgebungen etablieren
6. Incident Response Pläne für Datenschutzverletzungen erstellen

## Benötigte Ressourcen

### Hardware/Virtualisierung
- Min. 16 GB RAM für Host-System
- 500 GB freier Festplattenspeicher
- Virtualisierungssoftware (VMware Workstation/Hyper-V)

### Software-Lizenzen
- Windows Server 2022 (Evaluation/Education)
- Windows 10 Enterprise (Evaluation/Education)
- Optionale Tools: RSAT, PowerShell ISE

### Dokumentation
- Risikoanalyse-Template
- DSGVO-Compliance-Checkliste
- Backup-Verfahrensanweisung
- Network-Diagramm der Infrastruktur