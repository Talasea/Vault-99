# Lösung & Dokumentation zur Lernaufgabe „DataSecure GmbH“

Dieser Leitfaden beschreibt die empfohlene Vorgehensweise, um die in der Lernaufgabe formulierten Anforderungen vollständig umzusetzen. Er folgt derselben Tagesstruktur wie die Aufgabe und enthält konkrete PowerShell-Befehle, Screenshots-Hinweise, Best-Practice-Tipps sowie Verweise auf Microsoft-Dokumentationen.

## Tag 1 – Planung und Design

### 1.1 Forest-Design
1. **Namenskonzept** festlegen:  
   - Interne DNS-Suffixe ausschließlich `.local` (kein öffentliches DNS-Leak-Risiko).  
   - Öffentliche UPN-Suffixe via Azure AD später ergänzen.
2. **Domains & Forests**:  
   ```text
   Forest 1: datasecure.local
     ├── prod.datasecure.local
     ├── dev.datasecure.local
     └── dmz.datasecure.local
   Forest 2: techinno.local (Staging-Forest für Migration)
   ```
3. **Trusts**: Zwei-Wege-Forest-Trust mit *Selective Authentication* (siehe Active Directory Domains & Trusts).  
   > `netdom trust techinno.local /d:datasecure.local /twoway /SelectiveAuth:Yes`
4. **Standorte & Subnetze** konfigurieren (Active Directory Sites & Services).  
   - Standort‐Links mit `IP Cost` ≥ 100 für MPLS Backup.
5. **FSMO-Rollen** zuweisen:  
   - Schema & Domain-Naming: `DC-MU1`  
   - PDC & RID: `DC-MU2`  
   - Infrastrukturmaster: Standortabhängig (Berlin)
   > `Move-ADDirectoryServerOperationMasterRole –Identity "DC-MU2" –OperationMasterRole PDCEmulator,RIDMaster`

### 1.2 DSGVO-Analyse
- PowerShell-Export aller Attribute mit Personenbezug:  
  ```powershell
  Get-ADUser -Filter * ‑Properties * | Select Name,Surname,GivenName,mail | Export-Csv users-pii.csv
  ```
- Klassifikation gemäß GDPR: **Personal Data** vs. **Sensitive** (keine Gesundheitsdaten speichern!).
- Aufbewahrungsrichtlinie: 24 Monate nach Austritt -> automatischer Lösch-Workflow (AD Recycle Bin + skriptgesteuerte `Remove-ADUser`).

---

## Tag 2 – Grundinstallation

### 2.1 Domain Controller
- Baseline‐Image mit **Windows Server 2022 Core** + `sconfig`.  
- AD DS installieren:  
  ```powershell
  Install-WindowsFeature AD-Domain-Services ‑IncludeManagementTools
  Install-ADDSForest ‑DomainName datasecure.local ‑NoRebootOnCompletion $true
  ```
- RODC Hamburg:  
  ```powershell
  Install-ADDSDomainController ‑DomainName datasecure.local ‑ReadOnlyReplica
  ```
- **Secured-Core**: HVCI, VBS & Credential Guard via GPO aktivieren.

### 2.2 OU-Struktur
```powershell
New-ADOrganizationalUnit "München" –Path "DC=datasecure,DC=local"
```

---

## Tag 3 – Sicherheit

### 3.1 PKI
1. Offline-Root installieren (`SetupCA.cmd /Type Root /Offline`).
2. Sub-CA per `Add-WindowsFeature ADCS-Certification-Authority,ADCS-Web-Enrollment`.
3. Auto-Enrollment via GPO:  
   `Computer Configuration → Policies → Windows Settings → Security → PKI`.

### 3.2 LDAPS Test
```
openssl s_client -connect dc-mu1.datasecure.local:636 -showcerts
```

---

## Tag 4 – GPO

| Bereich | Richtlinie | Wert |
|---------|------------|------|
| Kennwort | Mindestlänge | 14 Zeichen |
| Lockout | Sperrschwelle | 10 Fehlversuche |
| Audit | DS Changes | Success/Failure |

Verwenden Sie **Starter GPO „Security Compliance Windows Server 2022“** (Microsoft Security Baseline).

---

## Tag 5 – Hybrid & NPS

### Azure AD Connect
```powershell
.
AADConnect.msi /Quiet
```
- Synchronisation prüfen: `Start-ADSyncSyncCycle –PolicyType Delta`.

### NPS
- Rolle hinzufügen: `Install-WindowsFeature NPAS –IncludeManagementTools`.
- Zertifikat „NPS‐Server“ anfordern.

---

## Tag 6 – DR

- **Windows Server Backup** Zeitplan: täglich System State.  
- Restore-Test in isoliertem VLAN (LAB).  
- Dokumentation aller Restore‐Schritte in Runbook.

---

## Tag 7 – Monitoring & Compliance

- **Event Forwarding** an zentralen `SIEM-VM` (Graylog/ELK).  
- Monthly GDPR Report via `Get-WinEvent` + `Export-Csv`.

---

## Anhang A – PowerShell-Snippet Sammlung
```powershell
# OU Export
Get-ADOrganizationalUnit -Filter * | Select Name,DistinguishedName | Export-Csv ous.csv
```

## Anhang B – Prüfliste DSGVO-Konformität
- [ ] Datenschutzerklärung für Mitarbeiter veröffentlicht
- [ ] Verzeichnis von Verarbeitungstätigkeiten aktualisiert
- [ ] Lösch-Workflows getestet
- [ ] MFA für Administratoren

---
**Ende der Dokumentation**
