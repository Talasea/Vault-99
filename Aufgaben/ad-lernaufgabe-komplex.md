# Komplexe Active Directory Lernaufgabe: DataSecure GmbH Migration & Compliance

## Unternehmensszenario

Die **DataSecure GmbH** ist ein mittelständisches IT-Dienstleistungsunternehmen mit Hauptsitz in München und Niederlassungen in Berlin und Hamburg. Das Unternehmen beschäftigt 350 Mitarbeiter und bietet Cloud-Services, Cybersecurity-Beratung und Softwareentwicklung an.

### Aktuelle Situation
- Veraltete Windows Server 2016 Infrastruktur
- Dezentrale Verwaltung führt zu Sicherheitslücken
- DSGVO-Compliance-Defizite
- Wachsende Anzahl von Remote-Arbeitsplätzen
- Geplante Übernahme der TechInno AG (80 Mitarbeiter)

### Ihr Auftrag
Sie sind als Senior Active Directory Administrator beauftragt, eine vollständige Infrastruktur-Modernisierung durchzuführen, die höchste Sicherheitsstandards und DSGVO-Compliance gewährleistet.

## Technische Anforderungen

### Infrastruktur-Spezifikationen
- **Server**: Windows Server 2022 Standard/Datacenter
- **Clients**: Windows 10/11 Pro (300 Workstations)
- **Virtuelle Umgebung**: VMware vSphere 7.0 oder Hyper-V
- **Netzwerk**: 3 Standorte über MPLS verbunden
- **Internet**: Redundante Internetanbindung pro Standort

### Compliance-Anforderungen
- **DSGVO/GDPR**: Vollständige Konformität erforderlich
- **ISO 27001**: Vorbereitung für Zertifizierung
- **BSI IT-Grundschutz**: Orientierung an deutschen Standards
- **Branchenspezifische Anforderungen**: IT-Dienstleister

## Aufgabenstellung (5-7 Arbeitstage)

### Tag 1: Planung und Design

#### Aufgabe 1.1: Forest-Struktur entwerfen
Entwerfen Sie eine Multi-Domain-Forest-Struktur für:
- **Hauptdomain**: datasecure.local
- **Produktionsumgebung**: prod.datasecure.local  
- **Entwicklungsumgebung**: dev.datasecure.local
- **DMZ-Services**: dmz.datasecure.local
- **Übernahme-Vorbereitung**: Separater Forest für TechInno AG

**Deliverables:**
- Forest-Vertrauensstellungen-Diagramm
- DNS-Struktur-Planung
- Sites und Replikations-Topologie
- FSMO-Rollen-Verteilung

Aufgabe1.15

#### Aufgabe 1.2: DSGVO-Compliance-Analyse
Führen Sie eine umfassende Datenanalyse durch:
- Identifizierung aller personenbezogenen Daten in AD
- Kategorisierung nach DSGVO-Klassifikation
- Definition von Aufbewahrungsrichtlinien
- Betroffenenrechte-Implementierungsplan

### Tag 2: Grundinstallation und Konfiguration

#### Aufgabe 2.1: Domain Controller Setup
Installieren und konfigurieren Sie:
- **München**: 2 DCs (1 Primary, 1 Secondary)
- **Berlin**: 1 DC mit Global Catalog
- **Hamburg**: 1 RODC (Read-Only Domain Controller)

**Besondere Anforderungen:**
- Secured-Core Server Konfiguration
- DNS-over-HTTPS Implementierung
- Windows Server 2022 erweiterte Sicherheitsfeatures

#### Aufgabe 2.2: Organisationsstruktur
Erstellen Sie eine realistische OU-Struktur:

```
DataSecure GmbH
├── München
│   ├── IT-Administration
│   ├── Entwicklung
│   ├── Consulting
│   └── Verwaltung
├── Berlin
│   ├── Cloud-Services
│   ├── Cybersecurity
│   └── Support
├── Hamburg
│   ├── Vertrieb
│   ├── Marketing
│   └── Projektmanagement
├── Service-Accounts
├── Server
└── Compliance-Objekte
```

### Tag 3: Erweiterte Sicherheitskonfiguration

#### Aufgabe 3.1: PKI-Implementierung
Implementieren Sie eine vollständige PKI-Infrastruktur:
- **Root CA**: Offline Enterprise Root CA
- **Subordinate CAs**: Pro Standort eine Issuing CA
- **Certificate Templates**: Für verschiedene Verwendungszwecke
- **Auto-Enrollment**: Für Computer und Benutzer

**Zertifikat-Typen:**
- Computer Authentication
- User Authentication  
- Code Signing (für Entwicklung)
- Web Server (für interne Services)
- LDAPS (für sichere LDAP-Kommunikation)

#### Aufgabe 3.2: LDAPS-Konfiguration
Konfigurieren Sie LDAP over SSL:
- Zertifikat-Deployment auf allen DCs
- Port 636 Konfiguration
- Client-seitige Konfiguration
- Verbindungstests

### Tag 4: Group Policy Management

#### Aufgabe 4.1: Komplexe GPO-Struktur
Erstellen Sie umfassende Group Policies:

**Sicherheits-GPOs:**
- Password Policy (DSGVO-konform)
- Account Lockout Policy
- User Rights Assignment
- Security Options (Geräteklassen)
- Windows Defender Konfiguration

**Compliance-GPOs:**
- Audit Policy Konfiguration
- Event Log Größen und Retention
- Registry-Einstellungen für Compliance
- Software Restriction Policies

**Standort-spezifische GPOs:**
- Drucker-Assignments
- Netzlaufwerk-Mappings
- Proxy-Einstellungen
- Remote Desktop Konfiguration

#### Aufgabe 4.2: Advanced Audit Policy
Implementieren Sie erweiterte Audit-Richtlinien:
- Directory Service Changes
- Account Management
- Logon/Logoff Events
- Object Access
- Policy Change
- Privilege Use

### Tag 5: Integration und Automatisierung

#### Aufgabe 5.1: Azure AD Hybrid Join
Konfigurieren Sie Hybrid Azure AD:
- Azure AD Connect Installation
- Password Hash Synchronization
- Hybrid Join für Windows 10/11 Clients
- Conditional Access Policies
- Self-Service Password Reset

#### Aufgabe 5.2: NPS/RADIUS Integration
Implementieren Sie Network Policy Server:
- RADIUS-Server für WLAN-Authentifizierung
- PEAP-MS-CHAPv2 Konfiguration
- Network Access Protection (NAP)
- Certificate-based Authentication

### Tag 6: Disaster Recovery und Testing

#### Aufgabe 6.1: Backup-Strategie
Entwickeln und implementieren Sie:
- System State Backups aller DCs
- SYSVOL Backup und Replikation
- AD Database Backup-Verfahren
- Bare Metal Recovery Vorbereitung

#### Aufgabe 6.2: Disaster Recovery Testing
Führen Sie folgende Tests durch:
- Authoritative Restore eines gelöschten OUs
- Non-Authoritative Restore eines DCs
- SYSVOL Recovery
- Forest Recovery Simulation

### Tag 7: Monitoring, Compliance und Dokumentation

#### Aufgabe 7.1: Monitoring-Implementation
Konfigurieren Sie umfassendes Monitoring:
- PowerShell-Scripts für AD Health Checks
- Event Log Monitoring für Security Events
- Performance Counter Überwachung
- Automated Compliance Reports

#### Aufgabe 7.2: DSGVO-Compliance Validierung
Implementieren Sie DSGVO-Anforderungen:
- Betroffenenrechte-Workflows
- Datenportabilität-Scripts
- Right-to-be-forgotten Procedures
- Data Processing Records

## Zusätzliche Herausforderungen

### Advanced Scenario 1: Forest Trust zu TechInno AG
- Externe Forest Trust Konfiguration
- Cross-Forest Authentication
- Selective Authentication
- SID History Migration

### Advanced Scenario 2: Certificate Services Migration
- Migration von SHA-1 zu SHA-256
- Certificate Template Versioning
- Cross-Certification Setup
- Mobile Device Certificate Enrollment

### Advanced Scenario 3: Multi-Factor Authentication
- ADFS Integration mit Azure AD
- Smart Card Authentication
- Windows Hello for Business
- FIDO2 Token Integration

## Bewertungskriterien

### Technische Umsetzung (50%)
- Funktionalität der implementierten Lösung
- Best Practices Einhaltung
- Sicherheitskonfiguration
- Performance und Skalierbarkeit

### Compliance (25%)
- DSGVO-Konformität
- Audit-Trail Vollständigkeit
- Dokumentation der Datenverarbeitung
- Betroffenenrechte-Implementierung

### Dokumentation (25%)
- Vollständigkeit der technischen Dokumentation
- Verständlichkeit für andere Administratoren
- Troubleshooting-Guides
- Compliance-Nachweise



## Benötigte Ressourcen

### Hardware/Virtualisierung
- **Minimum**: 8 VMs mit je 4 GB RAM
- **Empfohlen**: 12 VMs mit je 8 GB RAM
- **Storage**: 500 GB verfügbarer Speicher
- **Network**: Isolierte VLAN-Struktur

### Software-Lizenzen
- Windows Server 2022 (Evaluation oder Education)
- Windows 10Pro (Evaluation)
- VMware Workstation/vSphere (Evaluation)
- Office 365/Azure AD (Testmandant)

### Zusätzliche Tools
- PowerShell 7.x
- RSAT Tools
- Wireshark für Netzwerkanalyse
- Certificate Management Tools
- Azure AD Connect

## Erfolgsmessung

Die Aufgabe gilt als erfolgreich abgeschlossen, wenn:

1. **Alle technischen Anforderungen** vollständig implementiert sind
2. **DSGVO-Compliance** nachweislich erfüllt ist
3. **Disaster Recovery Tests** erfolgreich durchgeführt wurden
4. **Monitoring und Alerting** funktionsfähig ist
5. **Vollständige Dokumentation** vorliegt
6. **Sicherheitsaudit** ohne kritische Findings bestanden wird

## Zeitrahmen und Meilensteine

| Tag | Meilenstein | Deliverables |
|-----|-------------|--------------|
| 1 | Design Approval | Forest Design, Compliance Plan |
| 2 | Basic Infrastructure | Funktionsfähige DCs, OU-Struktur |
| 3 | Security Baseline | PKI, LDAPS, Basic Security |
| 4 | Policy Framework | GPOs, Audit Policies |
| 5 | Integration Complete | Azure AD, NPS/RADIUS |
| 6 | DR Readiness | Backup/Recovery Procedures |
| 7 | Production Ready | Monitoring, Compliance Reports |

---

*Diese Aufgabe simuliert reale Enterprise-Anforderungen und bereitet auf komplexe AD-Implementierungen in kritischen Umgebungen vor. Der Schwierigkeitsgrad erfordert fundierte Kenntnisse in Windows Server Administration, Sicherheitskonzepten und Compliance-Anforderungen.*