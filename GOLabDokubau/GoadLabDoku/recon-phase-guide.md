# Cyber Kill Chain - Reconnaissance Phase: Erweiterte Anleitung

## Executive Summary

Diese erweiterte Anleitung fokussiert sich auf die **erste Phase der Cyber Kill Chain** - die Reconnaissance-Phase. Basierend auf deinen GOAT Lab-Scan-Ergebnissen zeige ich dir zusätzliche Tools und Techniken, um eine umfassendere Aufklärung der Active Directory-Umgebung durchzuführen.

---

## 🎯 Reconnaissance Phase - Überblick

Die Reconnaissance-Phase gliedert sich in zwei Hauptkategorien:

### Passive Reconnaissance (OSINT)
- **Ziel**: Informationen sammeln ohne direkte Interaktion mit dem Zielsystem
- **Vorteil**: Keine Logs, keine Detektion
- **Nachteil**: Begrenzte Informationen

### Active Reconnaissance  
- **Ziel**: Direkte Interaktion mit Zielsystemen
- **Vorteil**: Detaillierte technische Informationen
- **Nachteil**: Kann entdeckt werden, hinterlässt Spuren

---

## 🔍 Phase 1: Passive OSINT-Reconnaissance

### DNS-Enumeration erweitern

```bash
# Umfassende DNS-Enumeration
dig ANY sevenkingdoms.local
dig ANY north.sevenkingdoms.local  
dig ANY essos.local

# DNS Zone Transfer versuchen
dig axfr sevenkingdoms.local @192.168.20.10
dig axfr north.sevenkingdoms.local @192.168.20.11
dig axfr essos.local @192.168.20.12

# DNS Brute Force mit verschiedenen Wordlists
dnsrecon -d sevenkingdoms.local -t brt -D ~/SecLists/Discovery/DNS/subdomains-top1million-110000.txt
dnsrecon -d sevenkingdoms.local -t std

# DNS Cache Snooping
dnsrecon -d sevenkingdoms.local -t snoop -n 192.168.20.10
```

### OSINT-Tools für weitere Aufklärung

```bash
# TheHarvester für Email/Subdomain-Enumeration
theHarvester -d sevenkingdoms.local -b all -l 500 -f harvester_results

# Fierce für DNS-Enumeration
fierce -dns sevenkingdoms.local --wordlist ~/SecLists/Discovery/DNS/fierce-hostlist.txt

# DNSMap für Subdomain-Discovery
dnsmap sevenkingdoms.local -w ~/SecLists/Discovery/DNS/subdomains-top1million-110000.txt

# Amass für umfassende Asset Discovery
amass enum -passive -d sevenkingdoms.local -o amass_results.txt
amass enum -active -d sevenkingdoms.local -brute -o amass_active.txt
```

---

## 🎯 Phase 2: Active Directory spezifische Reconnaissance

### LDAP-Enumeration vertiefen

```bash
# Detaillierte LDAP-Enumeration mit ldapsearch
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=user)" sAMAccountName userPrincipalName description

# Nach Service Principal Names suchen
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "servicePrincipalName=*" servicePrincipalName sAMAccountName

# Gruppen-Enumeration
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=group)" sAMAccountName member description

# Computer-Accounts finden
ldapsearch -x -H ldap://192.168.20.10 -s sub -b "DC=sevenkingdoms,DC=local" "(objectClass=computer)" sAMAccountName operatingSystem

# Domain Policy abfragen
ldapsearch -x -H ldap://192.168.20.10 -s base -b "DC=sevenkingdoms,DC=local" "(objectClass=*)" lockoutThreshold lockoutDuration maxPwdAge
```

### Enum4linux für umfassende Windows/Samba-Enumeration

```bash
# Vollständige enum4linux-Scans auf alle Hosts
enum4linux -a 192.168.20.10 > enum4linux_dc01.txt
enum4linux -a 192.168.20.11 > enum4linux_dc02.txt  
enum4linux -a 192.168.20.12 > enum4linux_dc03.txt
enum4linux -a 192.168.20.22 > enum4linux_sql01.txt
enum4linux -a 192.168.20.23 > enum4linux_sql02.txt

# Spezifische enum4linux-Optionen
enum4linux -U 192.168.20.10  # Nur User-Enumeration
enum4linux -G 192.168.20.10  # Nur Gruppen-Enumeration
enum4linux -S 192.168.20.10  # Nur Share-Enumeration
enum4linux -P 192.168.20.10  # Password Policy
enum4linux -o 192.168.20.10  # OS Information
```

### RPCclient für detaillierte RPC-Enumeration

```bash
# RPC-Verbindung mit Null Session
rpcclient -U "" -N 192.168.20.10

# Innerhalb der rpcclient-Session:
# enumdomusers      # Domain-User auflisten
# enumdomgroups     # Domain-Gruppen auflisten  
# querydominfo      # Domain-Informationen
# enumalsgroups domain  # Lokale Gruppen
# lookupnames administrator  # SID für User
# lookupsids S-1-5-21-[DOMAIN-SID]-500  # User für SID

# RPC-Befehle direkt ausführen
rpcclient -U "" -N 192.168.20.10 -c "enumdomusers;quit"
rpcclient -U "" -N 192.168.20.10 -c "querydominfo;quit"
```

---

## 🔧 Phase 3: Erweiterte Netzwerk-Reconnaissance

### Nmap-Scans erweitern

```bash
# UDP-Scan für zusätzliche Services
nmap -sU -sV -T4 192.168.20.0/24 --top-ports 1000

# Umfassende Script-Scans
nmap -sC -sV -p- 192.168.20.10 --script=ldap-*,smb-*,dns-*
nmap -sC -sV -p- 192.168.20.22,23 --script=ms-sql-*,smb-*

# SMB-Vulnerability-Scans
nmap --script smb-vuln-* 192.168.20.10,22,23

# SSL/TLS-Enumeration falls HTTPS gefunden wird
nmap --script ssl-enum-ciphers,ssl-cert 192.168.20.23 -p 443

# Active Directory spezifische Scripts
nmap --script ldap-rootdse,ldap-search 192.168.20.10-12 -p 389
```

### SMB-Enumeration vertiefen

```bash
# Detaillierte SMB-Share-Analyse
smbclient -L //192.168.20.23 -N
smbclient //192.168.20.23/all -N
smbclient //192.168.20.23/public -N
smbclient //192.168.20.23/CertEnroll -N

# SMBMap für Berechtigungsanalyse  
smbmap -H 192.168.20.23 -u null -p ""
smbmap -H 192.168.20.23 -R --depth 3

# CrackMapExec für umfassende SMB-Enumeration
crackmapexec smb 192.168.20.0/24 --shares
crackmapexec smb 192.168.20.0/24 --users
crackmapexec smb 192.168.20.0/24 --groups  
crackmapexec smb 192.168.20.0/24 --local-users
crackmapexec smb 192.168.20.0/24 --rid-brute
crackmapexec smb 192.168.20.0/24 --sessions
```

---

## 🩸 Phase 4: BloodHound für AD-Relationship-Mapping

### BloodHound Python Ingestor

```bash
# BloodHound Python installieren
pip3 install bloodhound

# Datensammlung mit verschiedenen Collection-Methoden
bloodhound-python -d sevenkingdoms.local -u '' -p '' -ns 192.168.20.10 -c All --zip
bloodhound-python -d north.sevenkingdoms.local -u '' -p '' -ns 192.168.20.11 -c All --zip  
bloodhound-python -d essos.local -u '' -p '' -ns 192.168.20.12 -c All --zip

# Spezifische Collection-Methoden
bloodhound-python -d sevenkingdoms.local -u '' -p '' -ns 192.168.20.10 -c Group,LocalAdmin,Session,Trusts --zip
```

### Neo4j und BloodHound Setup

```bash
# Neo4j starten
sudo neo4j console

# BloodHound starten
bloodhound

# Daten importieren und analysieren
# - Upload ZIP-Files über BloodHound GUI
# - Nutze vordefinierte Queries für Privilege Escalation Paths
```

---

## 🌐 Phase 5: Web-Service Reconnaissance  

### Gobuster-Scans optimieren

```bash
# Verschiedene Wordlists testen
gobuster dir -u http://192.168.20.23 -w ~/SecLists/Discovery/Web-Content/common.txt -t 20 -q
gobuster dir -u http://192.168.20.23 -w ~/SecLists/Discovery/Web-Content/big.txt -t 20 -q

# File-Extensions scannen
gobuster dir -u http://192.168.20.23 -w ~/SecLists/Discovery/Web-Content/common.txt -x php,asp,aspx,jsp,txt,pdf -t 20

# Vhost-Enumeration
gobuster vhost -u http://192.168.20.23 -w ~/SecLists/Discovery/DNS/subdomains-top1million-110000.txt

# Alternative: Dirb verwenden
dirb http://192.168.20.23 ~/SecLists/Discovery/Web-Content/common.txt -r -S
```

### Alternative Web-Enumeration Tools

```bash
# Nikto für Web-Vulnerability-Scanning
nikto -h http://192.168.20.23 -C all

# WhatWeb für Technology-Detection  
whatweb http://192.168.20.23 -v

# HTTProbe für HTTP-Service-Discovery
echo "192.168.20.23" | httprobe -p http:80,https:443,http:8080,https:8443
```

---

## 🗃️ Phase 6: Database-Service Reconnaissance

### MS SQL Server-Enumeration

```bash
# Nmap SQL-Scripts mit Debug-Informationen
nmap -p 1433 --script ms-sql-info,ms-sql-config,ms-sql-dump-hashes,ms-sql-empty-password,ms-sql-brute 192.168.20.22,23 -d

# Impacket mssqlclient für direkte Verbindung
impacket-mssqlclient -windows-auth guest@192.168.20.22
impacket-mssqlclient guest@192.168.20.23

# SQLMap für SQL-Injection-Tests (falls Web-Interface gefunden)
sqlmap -u "http://192.168.20.23/login.asp" --dbs --batch
```

---

## 📋 Phase 7: Information Gathering & Documentation

### Automatisierte Scan-Orchestrierung

```bash
#!/bin/bash
# recon_automation.sh

TARGET_RANGE="192.168.20.0/24"
DOMAIN="sevenkingdoms.local"
OUTPUT_DIR="recon_$(date +%Y%m%d_%H%M%S)"

mkdir -p $OUTPUT_DIR

echo "[+] Starting comprehensive reconnaissance..."

# Nmap Scans
nmap -sS -sV -sC -O $TARGET_RANGE -oA $OUTPUT_DIR/nmap_comprehensive &
nmap -sU --top-ports 1000 $TARGET_RANGE -oA $OUTPUT_DIR/nmap_udp &

# DNS Enumeration
dnsrecon -d $DOMAIN -t std -j $OUTPUT_DIR/dnsrecon.json &
fierce -dns $DOMAIN > $OUTPUT_DIR/fierce.txt &

# SMB Enumeration  
crackmapexec smb $TARGET_RANGE --shares > $OUTPUT_DIR/cme_shares.txt &
crackmapexec smb $TARGET_RANGE --users > $OUTPUT_DIR/cme_users.txt &

# Wait for background jobs
wait

echo "[+] Reconnaissance completed. Results in: $OUTPUT_DIR"
```

### Structured Information Collection

```bash
# Host-Discovery-Matrix erstellen
echo "IP,Hostname,OS,Services,Shares,Users" > hosts_matrix.csv

# Für jeden gefundenen Host detaillierte Informationen sammeln
for ip in 192.168.20.10 192.168.20.11 192.168.20.12 192.168.20.22 192.168.20.23; do
    echo "[+] Enumerating $ip..."
    
    # Host-Info sammeln
    hostname=$(nmap -sn $ip | grep -oP '(?<=\()[^)]*(?=\))' | head -1)
    os=$(nmap -O $ip | grep "OS details" | cut -d: -f2 | xargs)
    
    # Services
    services=$(nmap -sS --top-ports 1000 $ip | grep "open" | wc -l)
    
    # SMB-Shares
    shares=$(crackmapexec smb $ip --shares 2>/dev/null | grep -c "READ\|WRITE" || echo "0")
    
    # Users  
    users=$(crackmapexec smb $ip --users 2>/dev/null | grep -c "username:" || echo "0")
    
    echo "$ip,$hostname,$os,$services,$shares,$users" >> hosts_matrix.csv
done
```

---

## 🎯 Nächste Schritte nach Reconnaissance

### 1. Vulnerability Assessment
```bash
# Vulnerability-Scans basierend auf gefundenen Services
nmap --script vuln 192.168.20.0/24

# SMB-Vulnerabilities 
nmap --script smb-vuln-ms17-010,smb-vuln-ms08-067 192.168.20.0/24
```

### 2. Credential Harvesting Vorbereitung
```bash
# Usernames aus verschiedenen Quellen sammeln
cat $OUTPUT_DIR/*users* | grep -oE '[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+' | sort -u > usernames.txt

# Häufige Passwörter vorbereiten
cp ~/SecLists/Passwords/Common-Credentials/10k-most-common.txt passwords.txt
```

### 3. Attack Surface Mapping
- **Certificate Services**: CertEnroll-Share auf 192.168.20.23 analysieren
- **SQL Services**: Ports 1433 auf .22 und .23 für Brute-Force vorbereiten  
- **SMB Shares**: "all"-Share (READ/WRITE) für Lateral Movement
- **Active Sessions**: BRAAVOS\cloudbase-init und ESSOS\sql_svc als Ziele

---

## 🛡️ Stealth-Considerations

### Low-Profile Scanning
```bash
# Langsame Scans zur Vermeidung von Detection
nmap -T1 -sS 192.168.20.0/24  # Paranoid timing
nmap -T2 -sV 192.168.20.10-23 # Sneaky timing

# Fragmented Packets
nmap -f -sS 192.168.20.0/24

# Decoy Scans
nmap -D RND:10 192.168.20.0/24
```

### Log-Evasion
```bash
# Verschiedene Source-Ports verwenden
nmap --source-port 53 192.168.20.0/24
nmap --source-port 80 192.168.20.0/24

# Spoofed MAC-Addresses
nmap --spoof-mac 0 192.168.20.0/24
```

---

## 📊 Reporting & Documentation

### Reconnaissance Report Template
```markdown
# Reconnaissance Report - GOAT Lab

## Executive Summary
- **Total Hosts Discovered**: X
- **Active Directory Domains**: 3 (sevenkingdoms.local, north.sevenkingdoms.local, essos.local)  
- **Critical Services Found**: SMB, LDAP, MS SQL, Certificate Services
- **Risk Level**: HIGH

## Detailed Findings
[Detaillierte Auflistung der Findings...]

## Attack Paths Identified
1. Certificate Template Abuse via CertEnroll share
2. SQL Service Account Compromise
3. SMB Share Exploitation for Lateral Movement

## Recommendations
[Empfehlungen zur Absicherung...]
```

---

## 🔧 Tool Installation & Setup

```bash
# Alle wichtigen Tools installieren
sudo apt update && sudo apt install -y \
    nmap enum4linux smbclient rpcclient \
    dnsrecon fierce nikto dirb gobuster \
    crackmapexec bloodhound.py \
    impacket-scripts sqlmap

# Zusätzliche Tools via pip
pip3 install bloodhound dnspython requests

# SecLists klonen falls nicht vorhanden
git clone https://github.com/danielmiessler/SecLists ~/SecLists
```

---

## 💡 Pro-Tips für die Reconnaissance-Phase

1. **Dokumentiere alles**: Jeder Scan, jeder Fund, jede Anomalie
2. **Mehrere Ansätze**: Verwende verschiedene Tools für dieselbe Aufgabe
3. **Timing beachten**: Verteile Scans über Zeit um Detection zu vermeiden
4. **Pivot-Points identifizieren**: Suche nach Systemen für Lateral Movement
5. **Anomalien beachten**: Ungewöhnliche Services oder Konfigurationen untersuchen

Diese erweiterte Reconnaissance-Phase-Anleitung gibt dir die Tools und Techniken an die Hand, um eine umfassende Aufklärung der GOAT Lab-Umgebung durchzuführen und optimal für die nächsten Phasen der Cyber Kill Chain vorbereitet zu sein.