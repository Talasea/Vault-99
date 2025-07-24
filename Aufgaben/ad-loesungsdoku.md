# Lösungsdokumentation: Active Directory Lernaufgabe

## Tag 0: Risikoanalyse - Detaillierte Anleitung

### Schritt 1: Vorbereitung der Risikoanalyse

**Benötigte Dokumente:**
- Risikoanalyse-Template (bereits bereitgestellt)
- DSGVO-Artikel-Referenz
- Organisationshandbuch der fiktiven TechService GmbH

**Zeitaufwand:** 30 Minuten

**Durchführung:**
1. Alle beteiligten Personen identifizieren (IT-Leiter, Datenschutzbeauftragte, Geschäftsführung)
2. Arbeitsplatz mit den notwendigen Dokumenten vorbereiten
3. Bewertungskriterien festlegen

### Schritt 2: Risikobewertung durchführen

**Zeitaufwand:** 2.5 Stunden

**Vorgehen für jedes identifizierte Risiko:**

#### R001: Privilegierte Konten
```powershell
# Überprüfung aktueller Admin-Konten
Get-ADGroupMember "Domain Admins"
Get-ADGroupMember "Enterprise Admins"
Get-ADGroupMember "Schema Admins"
```

**Bewertung:**
- Eintrittswahrscheinlichkeit: Hoch (ohne Maßnahmen fast sicher)
- Auswirkung: Hoch (Vollzugriff auf gesamte Domäne)
- **Gesamtrisiko: HOCH**

**Sofortmaßnahmen:**
- Separate Admin-Konten für jeden Administrator
- MFA für alle privilegierten Konten
- Least-Privilege-Prinzip umsetzen

#### R002: Unverschlüsselte Kommunikation
**Bewertung:**
- Eintrittswahrscheinlichkeit: Mittel (bei ungesicherter Netzwerkumgebung)
- Auswirkung: Mittel (Credential-Diebstahl möglich)
- **Gesamtrisiko: NORMAL**

#### R003: Fehlende Audit-Protokollierung
```powershell
# Überprüfung aktueller Audit-Einstellungen
auditpol /get /category:*
```

**Bewertung:**
- Eintrittswahrscheinlichkeit: Mittel (Standardkonfiguration meist unzureichend)
- Auswirkung: Hoch (keine Nachvollziehbarkeit bei Incidents)
- **Gesamtrisiko: HOCH**

### Schritt 3: DSGVO-Compliance-Prüfung

**Zeitaufwand:** 1 Stunde

**Checkliste für DSFA-Notwendigkeit:**
- [ ] Systematische Überwachung öffentlicher Bereiche? **NEIN**
- [ ] Verarbeitung sensibler Daten in großem Umfang? **NEIN**
- [ ] Automatisierte Entscheidungsfindung mit Rechtswirkung? **NEIN**
- [ ] Neue Technologien mit hohem Risiko? **NEIN**

**Ergebnis:** DSFA nicht erforderlich, aber TOM-Dokumentation notwendig

## Tag 1: Server-Installation - Schritt-für-Schritt

### Schritt 1: Windows Server 2022 Installation

**Zeitaufwand:** 45 Minuten

**Installationsparameter:**
```
Edition: Windows Server 2022 Standard (Desktop Experience)
Partitionierung: 
- C:\ (100 GB) - System
- D:\ (50 GB) - Daten/Shares
- E:\ (30 GB) - Backup

Administrator-Passwort: Mindestens 14 Zeichen, komplex
```

### Schritt 2: Grundkonfiguration

**Zeitaufwand:** 30 Minuten

```powershell
# Computername setzen
Rename-Computer -NewName "DC01-TECHSERVICE" -Restart

# Nach Neustart: IP-Konfiguration
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.10 -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 127.0.0.1,8.8.8.8

# Windows Updates installieren
Install-Module PSWindowsUpdate -Force
Get-WUInstall -AcceptAll -AutoReboot
```

### Schritt 3: AD DS Installation

**Zeitaufwand:** 1 Stunde

```powershell
# AD DS Features installieren
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools

# Domänencontroller promoten
Install-ADDSForest `
    -DomainName "techservice.local" `
    -DomainNetbiosName "TECHSERVICE" `
    -ForestMode "WinThreshold" `
    -DomainMode "WinThreshold" `
    -InstallDns:$true `
    -DatabasePath "C:\Windows\NTDS" `
    -LogPath "C:\Windows\NTDS" `
    -SysvolPath "C:\Windows\SYSVOL" `
    -SafeModeAdministratorPassword (ConvertTo-SecureString "P@ssw0rd123!" -AsPlainText -Force)
```

### Schritt 4: OU-Struktur erstellen

**Zeitaufwand:** 30 Minuten

```powershell
# Basis-OUs erstellen
New-ADOrganizationalUnit -Name "TechService-Users" -Path "DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "TechService-Computers" -Path "DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "TechService-Groups" -Path "DC=techservice,DC=local"

# Unter-OUs für Users
New-ADOrganizationalUnit -Name "IT-Abteilung" -Path "OU=TechService-Users,DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "Verwaltung" -Path "OU=TechService-Users,DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "Vertrieb" -Path "OU=TechService-Users,DC=techservice,DC=local"

# Unter-OUs für Computer
New-ADOrganizationalUnit -Name "Workstations" -Path "OU=TechService-Computers,DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "Laptops" -Path "OU=TechService-Computers,DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "Servers" -Path "OU=TechService-Computers,DC=techservice,DC=local"

# Unter-OUs für Groups
New-ADOrganizationalUnit -Name "Security-Groups" -Path "OU=TechService-Groups,DC=techservice,DC=local"
New-ADOrganizationalUnit -Name "Distribution-Groups" -Path "OU=TechService-Groups,DC=techservice,DC=local"
```

## Tag 2: Sicherheitshärtung - Detaillierte Anleitung

### Schritt 1: Kennwort-Richtlinie konfigurieren

**Zeitaufwand:** 45 Minuten

```powershell
# Default Domain Policy öffnen
Import-Module GroupPolicy

# Kennwort-Richtlinien setzen
# Via GPMC.msc: Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies

# Alternativ per PowerShell:
Set-ADDefaultDomainPasswordPolicy -Identity techservice.local `
    -ComplexityEnabled $true `
    -LockoutDuration 00:30:00 `
    -LockoutObservationWindow 00:30:00 `
    -LockoutThreshold 3 `
    -MaxPasswordAge 90.00:00:00 `
    -MinPasswordAge 1.00:00:00 `
    -MinPasswordLength 14 `
    -PasswordHistoryCount 24
```

### Schritt 2: Privilegierte Konten absichern

**Zeitaufwand:** 1 Stunde

```powershell
# Neues Admin-Konto erstellen
New-ADUser -Name "admin.mueller" `
    -SamAccountName "admin.mueller" `
    -UserPrincipalName "admin.mueller@techservice.local" `
    -Path "OU=IT-Abteilung,OU=TechService-Users,DC=techservice,DC=local" `
    -AccountPassword (ConvertTo-SecureString "TempPass123!" -AsPlainText -Force) `
    -Enabled $true `
    -ChangePasswordAtLogon $true

# Zu Domain Admins hinzufügen
Add-ADGroupMember -Identity "Domain Admins" -Members "admin.mueller"

# Built-in Administrator deaktivieren
Disable-ADAccount -Identity "Administrator"

# Service-Account erstellen
New-ADUser -Name "svc.backup" `
    -SamAccountName "svc.backup" `
    -Path "OU=IT-Abteilung,OU=TechService-Users,DC=techservice,DC=local" `
    -AccountPassword (ConvertTo-SecureString "ServicePass123!" -AsPlainText -Force) `
    -Enabled $true `
    -PasswordNeverExpires $true `
    -CannotChangePassword $true
```

### Schritt 3: Audit-Richtlinien aktivieren

**Zeitaufwand:** 45 Minuten

```cmd
REM Erweiterte Audit-Richtlinien aktivieren
auditpol /set /category:"DS Access" /success:enable /failure:enable
auditpol /set /category:"Account Management" /success:enable /failure:enable
auditpol /set /category:"Policy Change" /success:enable /failure:enable
auditpol /set /category:"Privilege Use" /success:enable /failure:enable
auditpol /set /category:"System" /success:enable /failure:enable

REM Überprüfung der Einstellungen
auditpol /get /category:*
```

### Schritt 4: DNS-Sicherheit konfigurieren

**Zeitaufwand:** 30 Minuten

```powershell
# DNS-Manager öffnen und folgende Einstellungen vornehmen:
# 1. Secure Dynamic Updates aktivieren
# 2. Scavenging konfigurieren
# 3. Forwarder setzen

# Via PowerShell:
Set-DnsServerSetting -ComputerName DC01-TECHSERVICE -EnableDnsSec $true
Add-DnsServerForwarder -IPAddress 1.1.1.1,8.8.8.8
Set-DnsServerScavenging -ComputerName DC01-TECHSERVICE -ScavengingState $true -ScavengingInterval 7.00:00:00
```

## Tag 3: Gruppenrichtlinien und Client-Integration

### Schritt 1: Sicherheits-GPOs erstellen

**Zeitaufwand:** 2 Stunden

**Workstation-Security-Policy:**
```powershell
# Neue GPO erstellen
New-GPO -Name "Workstation-Security-Policy" -Comment "Sicherheitsrichtlinien für Arbeitsplätze"

# GPO mit Workstations-OU verknüpfen
New-GPLink -Name "Workstation-Security-Policy" -Target "OU=Workstations,OU=TechService-Computers,DC=techservice,DC=local"
```

**Konfiguration über GPMC.msc:**
```
Computer Configuration > Policies > Administrative Templates:
- Windows Components > Windows Defender Antivirus: Enabled
- Windows Components > Windows Update: 
  * Configure Automatic Updates: Enabled, Auto download and schedule install
- System > Removable Storage Access: 
  * All Removable Storage classes: Deny all access: Enabled
  
Computer Configuration > Policies > Windows Settings > Security Settings:
- Local Policies > User Rights Assignment:
  * Allow log on locally: Nur Domain Users und lokale Administratoren
- Local Policies > Security Options:
  * Interactive logon: Machine inactivity limit: 600 seconds
```

**User-Security-Policy:**
```powershell
# User-GPO erstellen
New-GPO -Name "User-Security-Policy" -Comment "Benutzer-Sicherheitsrichtlinien"

# Mit TechService-Users OU verknüpfen  
New-GPLink -Name "User-Security-Policy" -Target "OU=TechService-Users,DC=techservice,DC=local"
```

### Schritt 2: Windows 10 Clients konfigurieren

**Zeitaufwand:** 1.5 Stunden pro Client

**Client-Vorbereitung:**
```cmd
REM DNS-Server setzen
netsh interface ip set dns "Ethernet" static 192.168.1.10

REM Domänenbeitritt
netdom join %computername% /domain:techservice.local /userd:Administrator /passwordd:*
```

**Nach Neustart - Domänenbenutzer berechtigen:**
```cmd
REM Domain Users zu lokalen Benutzern hinzufügen
net localgroup users "TECHSERVICE\Domain Users" /add
```

### Schritt 3: Benutzer und Gruppen erstellen

**Zeitaufwand:** 1 Stunde

```powershell
# Security Groups erstellen
New-ADGroup -Name "IT-Admins" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"
New-ADGroup -Name "IT-Support" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"
New-ADGroup -Name "Office-Users" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"

# File-Access-Groups
New-ADGroup -Name "FileAccess-IT" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"
New-ADGroup -Name "FileAccess-Admin" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"
New-ADGroup -Name "FileAccess-Sales" -GroupScope Global -GroupCategory Security -Path "OU=Security-Groups,OU=TechService-Groups,DC=techservice,DC=local"

# Testbenutzer erstellen
New-ADUser -Name "Max Mustermann" -SamAccountName "max.mustermann" -UserPrincipalName "max.mustermann@techservice.local" -Path "OU=IT-Abteilung,OU=TechService-Users,DC=techservice,DC=local" -AccountPassword (ConvertTo-SecureString "TempPass123!" -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $true

New-ADUser -Name "Anna Beispiel" -SamAccountName "anna.beispiel" -UserPrincipalName "anna.beispiel@techservice.local" -Path "OU=Verwaltung,OU=TechService-Users,DC=techservice,DC=local" -AccountPassword (ConvertTo-SecureString "TempPass123!" -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $true

New-ADUser -Name "Tom Tester" -SamAccountName "tom.tester" -UserPrincipalName "tom.tester@techservice.local" -Path "OU=Vertrieb,OU=TechService-Users,DC=techservice,DC=local" -AccountPassword (ConvertTo-SecureString "TempPass123!" -AsPlainText -Force) -Enabled $true -ChangePasswordAtLogon $true

# Gruppenmitgliedschaften zuweisen
Add-ADGroupMember -Identity "IT-Admins" -Members "max.mustermann"
Add-ADGroupMember -Identity "Office-Users" -Members "anna.beispiel","tom.tester"
```

## Tag 4: File-Server und Berechtigungen

### Schritt 1: File Services installieren

**Zeitaufwand:** 30 Minuten

```powershell
# File Server Rolle installieren
Install-WindowsFeature -Name FS-FileServer,FS-DFS-Namespace,FS-Resource-Manager -IncludeManagementTools

# DFS-Namespace erstellen
New-DfsnRoot -TargetPath "\\DC01-TECHSERVICE\DFS" -Type DomainV2 -Path "\\techservice.local\files"
```

### Schritt 2: Ordnerstruktur erstellen

**Zeitaufwand:** 45 Minuten

```powershell
# Basis-Ordnerstruktur erstellen
New-Item -Path "D:\Shares" -ItemType Directory
New-Item -Path "D:\Shares\Public" -ItemType Directory
New-Item -Path "D:\Shares\IT-Department" -ItemType Directory
New-Item -Path "D:\Shares\Administration" -ItemType Directory
New-Item -Path "D:\Shares\Sales" -ItemType Directory
New-Item -Path "D:\Shares\Archive" -ItemType Directory

# SMB-Freigaben erstellen
New-SmbShare -Name "Public" -Path "D:\Shares\Public" -FullAccess "Everyone"
New-SmbShare -Name "IT-Department" -Path "D:\Shares\IT-Department" -FullAccess "TECHSERVICE\FileAccess-IT"
New-SmbShare -Name "Administration" -Path "D:\Shares\Administration" -FullAccess "TECHSERVICE\FileAccess-Admin"
New-SmbShare -Name "Sales" -Path "D:\Shares\Sales" -FullAccess "TECHSERVICE\FileAccess-Sales"
New-SmbShare -Name "Archive" -Path "D:\Shares\Archive" -ReadAccess "TECHSERVICE\Domain Users" -FullAccess "TECHSERVICE\FileAccess-IT"
```

### Schritt 3: NTFS-Berechtigungen setzen

**Zeitaufwand:** 1 Stunde

```powershell
# NTFS-Berechtigungen für IT-Department
$Path = "D:\Shares\IT-Department"
$AccessRule = New-Object System.Security.AccessControl.FileSystemAccessRule("TECHSERVICE\FileAccess-IT","FullControl","ContainerInherit,ObjectInherit","None","Allow")
$acl = Get-Acl $Path
$acl.SetAccessRule($AccessRule)
Set-Acl -Path $Path -AclObject $acl

# Access-Based Enumeration aktivieren
Set-SmbShare -Name "IT-Department" -FolderEnumerationMode AccessBased
Set-SmbShare -Name "Administration" -FolderEnumerationMode AccessBased  
Set-SmbShare -Name "Sales" -FolderEnumerationMode AccessBased
```

### Schritt 4: FSRM konfigurieren

**Zeitaufwand:** 45 Minuten

```powershell
# Dateikontingent erstellen
New-FsrmQuota -Path "D:\Shares\Public" -Size 5GB -SoftLimit $false

# Dateigruppe für verbotene Dateien
New-FsrmFileGroup -Name "Executable Files" -IncludePattern @("*.exe","*.com","*.bat","*.cmd")

# Datei-Screen erstellen
New-FsrmFileScreen -Path "D:\Shares\Public" -IncludeGroup "Executable Files"
```

## Tag 5: Backup, Monitoring und DSGVO-Compliance

### Schritt 1: Backup-Konfiguration

**Zeitaufwand:** 1.5 Stunden

```powershell
# Windows Server Backup installieren
Install-WindowsFeature -Name Windows-Server-Backup -IncludeManagementTools

# System State Backup konfigurieren
$Policy = New-WBPolicy
$SystemState = New-WBSystemState
Add-WBSystemState -Policy $Policy -SystemState $SystemState

# Backup-Ziel definieren (externe USB-Festplatte)
$BackupLocation = New-WBBackupTarget -VolumePath "E:"
Add-WBBackupTarget -Policy $Policy -Target $BackupLocation

# Zeitplan festlegen (täglich um 22:00)
Set-WBSchedule -Policy $Policy -Schedule 22:00

# Policy aktivieren
Set-WBPolicy -Policy $Policy

# Backup-Skript für manuelle Ausführung
@"
# Manuelles System State Backup
wbadmin start systemstatebackup -backuptarget:E: -quiet
"@ | Out-File -FilePath "C:\Scripts\ManualBackup.ps1"
```

### Schritt 2: Monitoring implementieren

**Zeitaufwand:** 1 Stunde

```powershell
# Überwachungsskript erstellen
New-Item -Path "C:\Scripts" -ItemType Directory -Force

@"
# AD-Gesundheitscheck-Skript
# Datum: $(Get-Date)

Write-Host "=== Active Directory Gesundheitscheck ===" -ForegroundColor Green

# DCDIAG ausführen
Write-Host "Durchführung DCDIAG..." -ForegroundColor Yellow
dcdiag /v > C:\Scripts\Logs\dcdiag-$(Get-Date -Format 'yyyyMMdd').log

# Event Log Fehler prüfen
Write-Host "Prüfung kritischer Events..." -ForegroundColor Yellow
$CriticalEvents = Get-WinEvent -FilterHashtable @{LogName='System','Application'; Level=1,2; StartTime=(Get-Date).AddHours(-24)}
if ($CriticalEvents.Count -gt 0) {
    $CriticalEvents | Export-Csv -Path "C:\Scripts\Logs\critical-events-$(Get-Date -Format 'yyyyMMdd').csv" -NoTypeInformation
    Write-Warning "Kritische Events gefunden! Siehe Log-Datei."
}

# Festplattenspeicher prüfen
Write-Host "Prüfung Festplattenspeicher..." -ForegroundColor Yellow
$DiskSpace = Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.Size -gt 0}
foreach ($Disk in $DiskSpace) {
    $FreePercent = [math]::Round(($Disk.FreeSpace / $Disk.Size) * 100, 2)
    if ($FreePercent -lt 20) {
        Write-Warning "Laufwerk $($Disk.DeviceID) hat nur noch $FreePercent% freien Speicher!"
    }
}

Write-Host "Gesundheitscheck abgeschlossen." -ForegroundColor Green
"@ | Out-File -FilePath "C:\Scripts\AD-HealthCheck.ps1"

# Logs-Ordner erstellen
New-Item -Path "C:\Scripts\Logs" -ItemType Directory -Force

# Geplante Aufgabe für täglichen Gesundheitscheck
$Action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Scripts\AD-HealthCheck.ps1"
$Trigger = New-ScheduledTaskTrigger -Daily -At 8:00AM
Register-ScheduledTask -TaskName "AD-HealthCheck" -Action $Action -Trigger $Trigger -User "SYSTEM"
```

### Schritt 3: DSGVO-Compliance finalisieren

**Zeitaufwand:** 2 Stunden

**Datenklassifizierung implementieren:**
```powershell
# Script für Benutzerattribut-Analyse
@"
# DSGVO-Datenklassifizierung für AD-Attribute

# Personal Data Attributes
$PersonalDataAttributes = @(
    'givenName',
    'sn', 
    'mail',
    'telephoneNumber',
    'mobile',
    'streetAddress',
    'postalCode',
    'l', # Stadt
    'co' # Land
)

# Sensitive Data Attributes (sollten vermieden werden)
$SensitiveDataAttributes = @(
    'personalTitle',
    'employee-type',
    'manager' # kann Hierarchien preisgeben
)

# Non-Personal Data Attributes
$NonPersonalDataAttributes = @(
    'samAccountName',
    'userPrincipalName',
    'memberOf',
    'lastLogon',
    'pwdLastSet'
)

Write-Host "=== DSGVO-Datenklassifizierung ===" -ForegroundColor Green
Write-Host "Persönliche Daten: $($PersonalDataAttributes -join ', ')" -ForegroundColor Yellow
Write-Host "Sensible Daten: $($SensitiveDataAttributes -join ', ')" -ForegroundColor Red
Write-Host "Nicht-persönliche Daten: $($NonPersonalDataAttributes -join ', ')" -ForegroundColor Cyan

# Aufbewahrungsrichtlinie dokumentieren
Write-Host "Aufbewahrungsrichtlinie: 24 Monate nach Austritt" -ForegroundColor Green
"@ | Out-File -FilePath "C:\Scripts\DSGVO-DataClassification.ps1"
```

**Betroffenenrechte-Skripte:**
```powershell
# Script für Datenexport (Art. 15 DSGVO)
@"
param(
    [Parameter(Mandatory=$true)]
    [string]$Username
)

# Benutzerdaten exportieren für DSGVO-Auskunftsrecht
$User = Get-ADUser -Identity $Username -Properties *
$UserData = @{
    'Benutzername' = $User.SamAccountName
    'Vollständiger Name' = $User.DisplayName
    'E-Mail' = $User.mail
    'Telefon' = $User.telephoneNumber
    'Abteilung' = $User.Department
    'Letzte Anmeldung' = $User.LastLogonDate
    'Konto erstellt' = $User.Created
    'Gruppenmitgliedschaften' = (Get-ADPrincipalGroupMembership $Username | Select-Object Name).Name -join '; '
}

$UserData | ConvertTo-Json | Out-File -FilePath "C:\Scripts\Exports\UserData-$Username-$(Get-Date -Format 'yyyyMMdd').json"
Write-Host "Benutzerdaten für $Username exportiert." -ForegroundColor Green
"@ | Out-File -FilePath "C:\Scripts\Export-UserData.ps1"

# Script für Benutzerlöschung (Art. 17 DSGVO)
@"
param(
    [Parameter(Mandatory=$true)]
    [string]$Username,
    [switch]$Archive
)

if ($Archive) {
    # Benutzer archivieren (deaktivieren und verschieben)
    $ArchiveOU = "OU=Archived-Users,OU=TechService-Users,DC=techservice,DC=local"
    
    # Archive-OU erstellen falls nicht vorhanden
    try {
        Get-ADOrganizationalUnit -Identity $ArchiveOU
    } catch {
        New-ADOrganizationalUnit -Name "Archived-Users" -Path "OU=TechService-Users,DC=techservice,DC=local"
    }
    
    Disable-ADAccount -Identity $Username
    Move-ADObject -Identity (Get-ADUser $Username).DistinguishedName -TargetPath $ArchiveOU
    Write-Host "Benutzer $Username archiviert." -ForegroundColor Yellow
} else {
    # Benutzer permanent löschen
    Remove-ADUser -Identity $Username -Confirm:$false
    Write-Host "Benutzer $Username permanent gelöscht." -ForegroundColor Red
}
"@ | Out-File -FilePath "C:\Scripts\Remove-User.ps1"

# Exports-Ordner erstellen
New-Item -Path "C:\Scripts\Exports" -ItemType Directory -Force
```

### Schritt 4: Dokumentation erstellen

**Zeitaufwand:** 1 Stunde

```powershell
# Verzeichnis von Verarbeitungstätigkeiten erstellen
@"
# Verzeichnis von Verarbeitungstätigkeiten - TechService GmbH

## 1. Benutzeranmeldung und Authentifizierung
- **Zweck**: Sichere Anmeldung an Unternehmenssystemen
- **Kategorien betroffener Personen**: Mitarbeiter
- **Kategorien personenbezogener Daten**: Name, Benutzername, Anmeldezeitpunkte
- **Kategorien von Empfängern**: IT-Administratoren
- **Übermittlung in Drittländer**: Nein
- **Fristen für Löschung**: 24 Monate nach Austritt
- **TOM**: Verschlüsselte Übertragung, Zugriffsprotokollierung

## 2. Dateifreigaben und Zugriffsverwaltung  
- **Zweck**: Bereitstellung von Arbeitsdateien und Kollaboration
- **Kategorien betroffener Personen**: Mitarbeiter, Kunden (indirekt durch Dateien)
- **Kategorien personenbezogener Daten**: Name, E-Mail, Dokumentinhalte
- **Kategorien von Empfängern**: Berechtigte Mitarbeiter
- **Übermittlung in Drittländer**: Nein
- **Fristen für Löschung**: Projektabhängig, max. 7 Jahre
- **TOM**: Rollenbasierte Zugriffskontrolle, Verschlüsselung

## 3. Systemprotokollierung und Monitoring
- **Zweck**: Sicherheitsüberwachung und Compliance
- **Kategorien betroffener Personen**: Mitarbeiter
- **Kategorien personenbezogener Daten**: Benutzername, IP-Adressen, Zugriffszeitpunkte
- **Kategorien von Empfängern**: IT-Sicherheitsbeauftragte
- **Übermittlung in Drittländer**: Nein
- **Fristen für Löschung**: 6 Monate (Logs)
- **TOM**: Zugriffsbeschränkung, Integritätsschutz
"@ | Out-File -FilePath "C:\Scripts\Verarbeitungstaetigkeiten.md"

# TOM-Dokumentation
@"
# Technische und Organisatorische Maßnahmen (TOM)

## Zugangs- und Zugriffskontrolle
- Multi-Faktor-Authentifizierung für Administratoren
- Rollenbasierte Berechtigungen
- Regelmäßige Zugriffsprüfungen

## Eingabekontrolle
- Audit-Protokollierung aller Änderungen
- Versionierung von Konfigurationsänderungen

## Transportkontrolle  
- TLS-Verschlüsselung für alle Netzwerkverbindungen
- IPSec für domänen-interne Kommunikation

## Speicherkontrolle
- Verschlüsselte Festplatten (BitLocker)
- Sichere Backups mit Verschlüsselung

## Trennungskontrolle
- Separate OUs für verschiedene Abteilungen
- Getrennte Sicherheitsgruppen

## Organisatorische Maßnahmen
- Datenschutz-Folgenabschätzung vor neuen Systemen
- Regelmäßige Mitarbeiterschulungen
- Incident Response Plan
"@ | Out-File -FilePath "C:\Scripts\TOM-Dokumentation.md"
```

### Schritt 5: Abschluss-Audit

**Zeitaufwand:** 30 Minuten

```powershell
# Abschluss-Audit-Skript
@"
Write-Host "=== Active Directory Implementierung - Abschluss-Audit ===" -ForegroundColor Green

# 1. Domain Controller Status
Write-Host "1. Domain Controller Status:" -ForegroundColor Yellow
dcdiag /c

# 2. DNS-Funktionalität
Write-Host "2. DNS-Funktionalität:" -ForegroundColor Yellow
nslookup techservice.local localhost

# 3. Gruppenrichtlinien Status
Write-Host "3. Gruppenrichtlinien:" -ForegroundColor Yellow
Get-GPO -All | Select-Object DisplayName, GpoStatus

# 4. Benutzer und Gruppen
Write-Host "4. Benutzer- und Gruppenübersicht:" -ForegroundColor Yellow
Write-Host "Benutzer:" (Get-ADUser -Filter * | Measure-Object).Count
Write-Host "Gruppen:" (Get-ADGroup -Filter * | Measure-Object).Count

# 5. Freigaben
Write-Host "5. SMB-Freigaben:" -ForegroundColor Yellow
Get-SmbShare | Select-Object Name, Path

# 6. Backup-Status
Write-Host "6. Backup-Status:" -ForegroundColor Yellow
Get-WBJob -Previous 1

# 7. Sicherheitseinstellungen
Write-Host "7. Kennwort-Richtlinie:" -ForegroundColor Yellow
Get-ADDefaultDomainPasswordPolicy

Write-Host "Audit abgeschlossen - System bereit für Produktivbetrieb!" -ForegroundColor Green
"@ | Out-File -FilePath "C:\Scripts\Final-Audit.ps1"

# Audit ausführen
& "C:\Scripts\Final-Audit.ps1"
```

## Troubleshooting-Guide

### Häufige Probleme und Lösungen

#### Problem: DNS-Auflösung funktioniert nicht
```powershell
# Lösung:
ipconfig /flushdns
nslookup techservice.local 192.168.1.10
```

#### Problem: Gruppenrichtlinien werden nicht angewendet
```cmd
REM Auf Client ausführen:
gpupdate /force
gpresult /r
```

#### Problem: AD-Replikation Fehler (bei mehreren DCs)
```powershell
# Replikationsstatus prüfen:
repadmin /showrepl
repadmin /replsum
```

#### Problem: Backup schlägt fehl
```powershell
# Backup-Logs prüfen:
Get-WBJob -Previous 5
# Speicherplatz prüfen:
Get-WmiObject -Class Win32_LogicalDisk
```

## Bewertungsrubrik

### Technische Implementierung (60 Punkte)
- **AD-Installation**: 15 Punkte
- **OU-Struktur**: 10 Punkte  
- **Benutzer/Gruppen**: 15 Punkte
- **Gruppenrichtlinien**: 20 Punkte

### Sicherheit (25 Punkte)
- **Kennwort-Richtlinien**: 8 Punkte
- **Privileged Access Management**: 10 Punkte
- **Audit-Konfiguration**: 7 Punkte

### DSGVO-Compliance (15 Punkte)
- **Risikoanalyse**: 5 Punkte
- **Datenklassifizierung**: 5 Punkte
- **TOM-Dokumentation**: 5 Punkte

**Gesamtpunktzahl**: 100 Punkte
**Bestanden**: ≥ 70 Punkte