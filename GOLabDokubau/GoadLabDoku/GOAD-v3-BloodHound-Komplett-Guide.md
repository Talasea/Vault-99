# GOAD v3 Lab - BloodHound Installation und Reconnaissance Guide

## Detaillierte Schritt-für-Schritt Anleitung für das GOAD Lab

---

## Teil 1: BloodHound Community Edition Installation

### Schritt 1.1: Voraussetzungen prüfen

**System-Requirements:**
- Kali Linux (empfohlen) oder Ubuntu/Debian-basierte Distribution
- Docker und Docker-Compose
- Mindestens 4GB RAM für BloodHound CE
- 10GB freier Speicherplatz

**Netzwerk-Setup für GOAD Lab:**
- **Dein Subnetz**: 192.168.20.0/24
- **Hosts**: 192.168.20.10-23 (basierend auf deinem nmap-Scan)

### Schritt 1.2: Docker Installation
```bash
# System updaten
sudo apt update && sudo apt upgrade -y

# Docker installieren
sudo apt install -y docker.io docker-compose

# Docker Service starten und aktivieren
sudo systemctl start docker
sudo systemctl enable docker

# Benutzer zur Docker-Gruppe hinzufügen (optional)
sudo usermod -aG docker $USER
# Neuanmeldung erforderlich oder: newgrp docker
```

### Schritt 1.3: BloodHound CE Installation mit CLI Tool
```bash
# BloodHound CLI Tool herunterladen
mkdir /opt/bloodhound && cd /opt/bloodhound
wget https://github.com/SpecterOps/bloodhound-cli/releases/latest/download/bloodhound-cli-linux-amd64.tar.gz

# Extrahieren
tar -xzf bloodhound-cli-linux-amd64.tar.gz
rm bloodhound-cli-linux-amd64.tar.gz

# Ausführbar machen
chmod +x bloodhound-cli

# BloodHound CE installieren
sudo ./bloodhound-cli install
```

**Wichtig:** Nach der Installation wird ein **zufälliges Admin-Passwort** im Terminal angezeigt. **Unbedingt notieren!**

### Schritt 1.4: BloodHound CE starten und konfigurieren
```bash
# BloodHound CE starten
sudo ./bloodhound-cli start

# Status prüfen
sudo ./bloodhound-cli status
```

**Web-Interface öffnen:**
- URL: `http://127.0.0.1:8080/ui/login`
- Username: `admin`
- Password: Das angezeigte zufällige Passwort

**Beim ersten Login:**
1. Mit dem generierten Passwort anmelden
2. Neues sicheres Passwort setzen
3. Dark Mode aktivieren (optional): Settings → Appearance → Dark Theme

---

## Teil 2: BloodHound Python Ingestor Installation

### Schritt 2.1: bloodhound-python installieren
```bash
# Über Kali Repository (empfohlen)
sudo apt update
sudo apt install -y bloodhound.py

# Alternative: Über pip
pip3 install bloodhound

# Impacket Tools installieren (falls nicht vorhanden)
sudo apt install -y python3-impacket
```

### Schritt 2.2: Installation verifizieren
```bash
# Testen ob bloodhound-python verfügbar ist
bloodhound-python --help

# Impacket Tools testen
secretsdump.py --help
```

---

## Teil 3: GOAD Lab Reconnaissance mit BloodHound

### Schritt 3.1: Initiale Netzwerk-Validierung
```bash
# Nmap-Scan basierend auf deinen Ergebnissen wiederholen
nmap -Pn -sS -p 53,80,88,135,139,389,445,636,1433,3268,3269,3389 192.168.20.10,11,12,22,23

# DNS-Server testen
dig @192.168.20.10 sevenkingdoms.local
dig @192.168.20.11 north.sevenkingdoms.local  
dig @192.168.20.12 essos.local
```

**Erwartete Hosts (aus deinem nmap-Report):**
- `192.168.20.10` - kingslanding.sevenkingdoms.local (DC01)
- `192.168.20.11` - winterfell.north.sevenkingdoms.local (DC02) 
- `192.168.20.12` - meereen.essos.local (DC03)
- `192.168.20.22` - castelblack.north.sevenkingdoms.local (SRV02, MSSQL)
- `192.168.20.23` - braavos.essos.local (SRV03, MSSQL)

### Schritt 3.2: Anonymous LDAP Enumeration
```bash
# Anonymous LDAP Bind testen (Domain: sevenkingdoms.local)
ldapsearch -x -h 192.168.20.10 -s base namingcontexts
ldapsearch -x -h 192.168.20.10 -b "DC=sevenkingdoms,DC=local" "(objectclass=*)" | head -20

# Domain: north.sevenkingdoms.local
ldapsearch -x -h 192.168.20.11 -s base namingcontexts
ldapsearch -x -h 192.168.20.11 -b "DC=north,DC=sevenkingdoms,DC=local" "(objectclass=*)" | head -20

# Domain: essos.local
ldapsearch -x -h 192.168.20.12 -s base namingcontexts
ldapsearch -x -h 192.168.20.12 -b "DC=essos,DC=local" "(objectclass=*)" | head -20
```

### Schritt 3.3: BloodHound Datensammlung (Anonymous)
```bash
# Anonymous Collection für alle drei Domains
# Domain 1: sevenkingdoms.local
bloodhound-python -u '' -p '' -d sevenkingdoms.local -dc kingslanding.sevenkingdoms.local -ns 192.168.20.10 -c all --dns-tcp

# Domain 2: north.sevenkingdoms.local  
bloodhound-python -u '' -p '' -d north.sevenkingdoms.local -dc winterfell.north.sevenkingdoms.local -ns 192.168.20.11 -c all --dns-tcp

# Domain 3: essos.local
bloodhound-python -u '' -p '' -d essos.local -dc meereen.essos.local -ns 192.168.20.12 -c all --dns-tcp
```

**Falls Anonymous Bind fehlschlägt:**
```bash
# SMB Null Sessions testen
smbclient -L //192.168.20.10 -N
smbclient -L //192.168.20.11 -N
smbclient -L //192.168.20.12 -N
smbclient -L //192.168.20.22 -N
smbclient -L //192.168.20.23 -N

# RPC Null Sessions
rpcclient -U '' -N 192.168.20.10
rpcclient> enumdomusers
rpcclient> enumdomgroups
rpcclient> quit
```

### Schritt 3.4: Authenticated Collection (mit gefundenen Credentials)
```bash
# GOAD Lab hat oft schwache Default-Credentials
# Teste bekannte schwache Accounts:

# crackmapexec für Credential Testing
crackmapexec smb 192.168.20.10-23 -u 'guest' -p '' --continue-on-success
crackmapexec smb 192.168.20.10-23 -u 'hodor' -p 'hodor' --continue-on-success

# Wenn Credentials gefunden (z.B. hodor:hodor):
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local -dc winterfell.north.sevenkingdoms.local -ns 192.168.20.11 -c all --dns-tcp

# Alle Collection Methods für umfassende Daten
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local -dc 192.168.20.11 -c All,GPOLocalGroup --dns-tcp
```

---

## Teil 4: BloodHound Datenanalyse

### Schritt 4.1: Daten in BloodHound CE importieren
1. **BloodHound CE öffnen**: `http://127.0.0.1:8080/ui/login`
2. **Daten hochladen**:
   - Links: "Upload Data" → "Select Files"
   - ZIP-Dateien auswählen (erstellt von bloodhound-python)
   - Drag & Drop funktioniert auch
3. **Import bestätigen**: Warten bis "Import completed" erscheint

### Schritt 4.2: GOAD-spezifische Cypher Queries

**Domain Admins aller Domains finden:**
```cypher
MATCH (n:User)-[:MemberOf*1..]->(g:Group) 
WHERE g.name CONTAINS 'DOMAIN ADMINS' 
RETURN n.name, g.name ORDER BY g.name
```

**Kerberoastable Users (Service Accounts):**
```cypher
MATCH (n:User) 
WHERE n.hasspn=true 
RETURN n.name, n.serviceprincipalnames, n.pwdlastset 
ORDER BY n.pwdlastset ASC
```

**ASREPRoastable Users:**
```cypher
MATCH (u:User) 
WHERE u.dontreqpreauth=true 
RETURN u.name, u.description, u.enabled
```

**Unconstrained Delegation (Kritisch!):**
```cypher
MATCH (c:Computer) 
WHERE c.unconstraineddelegation=true 
RETURN c.name, c.operatingsystem
```

**Shortest Path zu Domain Admin (Beispiel für hodor):**
```cypher
MATCH (u:User {name:"HODOR@NORTH.SEVENKINGDOMS.LOCAL"}), 
      (g:Group) WHERE g.name CONTAINS 'DOMAIN ADMINS'
MATCH p=shortestPath((u)-[*1..]->(g)) 
RETURN p LIMIT 5
```

**Cross-Domain Trusts:**
```cypher
MATCH (n:Domain)-[r:TrustedBy]->(m:Domain) 
RETURN n.name, type(r), m.name
```

**Local Admin Rights:**
```cypher
MATCH p=(u:User)-[r:AdminTo]->(c:Computer) 
RETURN u.name, c.name 
ORDER BY u.name
```

**RDP Rights:**
```cypher
MATCH p=(u:User)-[r:CanRDP]->(c:Computer) 
RETURN u.name, c.name
ORDER BY c.name
```

**MSSQL Admin Rights (für castelblack/braavos):**
```cypher
MATCH p=(u:User)-[r:SQLAdmin]->(c:Computer) 
WHERE c.name CONTAINS 'CASTELBLACK' OR c.name CONTAINS 'BRAAVOS'
RETURN u.name, c.name
```

### Schritt 4.3: GOAD-spezifische Attack Paths identifizieren

**GPO Abuse Möglichkeiten:**
```cypher
MATCH p=(u:User)-[r:GenericWrite|WriteDacl|WriteOwner]->(g:GPO)
RETURN u.name, type(r), g.name, g.description
```

**GenericAll/GenericWrite Rights:**
```cypher
MATCH p=(n)-[r:GenericAll|GenericWrite]->(m) 
WHERE n.name <> m.name
RETURN n.name, type(r), m.name, labels(m) 
LIMIT 25
```

**Cross-Forest Gruppen (GOAD-spezifisch):**
```cypher
MATCH (g:Group) 
WHERE g.name CONTAINS 'ACROSS' OR g.name CONTAINS 'DRAGONS' OR g.name CONTAINS 'SPYS'
RETURN g.name, g.domain
```

---

## Teil 5: Kontinuierliche Reconnaissance

### Schritt 5.1: Session Loop Collection (falls RDP/WinRM Zugang vorhanden)
```bash
# Auf einem kompromittierten Windows-System:
# SharpHound.exe herunterladen von: https://github.com/BloodHoundAD/SharpHound/releases

# Session Loop für bewegliche Targets
.\SharpHound.exe --CollectionMethods Session --Loop --LoopDuration 02:00:00 --LoopInterval 00:10:00

# Oder vollständige Collection
.\SharpHound.exe -c All,GPOLocalGroup -d north.sevenkingdoms.local --zipfilename north_complete.zip
```

### Schritt 5.2: Automatisiertes Monitoring Script
```bash
#!/bin/bash
# goad-bloodhound-monitor.sh

DOMAINS=("sevenkingdoms.local" "north.sevenkingdoms.local" "essos.local")
DCS=("192.168.20.10" "192.168.20.11" "192.168.20.12")
USER="hodor"  # Anpassen an gefundene Credentials
PASS="hodor"

echo "[$(date)] Starting GOAD BloodHound monitoring..."

for i in "${!DOMAINS[@]}"; do
    domain="${DOMAINS[$i]}"
    dc="${DCS[$i]}"
    
    echo "[$(date)] Collecting data for $domain via $dc..."
    
    bloodhound-python -u "$USER" -p "$PASS" -d "$domain" -dc "$dc" -ns "$dc" \
        -c Session,LoggedOn --dns-tcp --zip
    
    # Automatischer Import in BloodHound CE (über API - optional)
    # curl -X POST -F "file=@${domain}_*.zip" http://127.0.0.1:8080/api/v2/file-upload
done

echo "[$(date)] Monitoring cycle completed. Sleeping 15 minutes..."
sleep 900
```

---

## Teil 6: Troubleshooting

### Problem 1: "No data collected" von bloodhound-python
**Lösung:**
```bash
# DNS explizit angeben
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 -ns 192.168.20.11 -c all --dns-tcp

# Verbose Mode für Debugging
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 -v --dns-tcp

# Einzelne Collection Methods testen
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 -c Group --dns-tcp
```

### Problem 2: BloodHound CE zeigt keine Attack Paths
**Lösung:**
```bash
# Mehr Session-Daten sammeln
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 -c Session,LoggedOn --dns-tcp

# ACL-Daten sammeln (falls fehlen)
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 -c ACL --dns-tcp
```

### Problem 3: LDAP Connection Timeout
**Lösung:**
```bash
# Längere Timeouts setzen
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 --dns-timeout 30 --dns-tcp

# Disable Pooling bei Problemen
bloodhound-python -u hodor -p hodor -d north.sevenkingdoms.local \
    -dc 192.168.20.11 --disable-pooling --dns-tcp
```

### Problem 4: Docker/BloodHound CE startet nicht
**Lösung:**
```bash
# Container Status prüfen
sudo docker ps -a

# Logs anzeigen
sudo docker logs bloodhound-ce_bloodhound_1

# Services neu starten
cd /opt/bloodhound
sudo ./bloodhound-cli stop
sudo ./bloodhound-cli start

# Port-Konflikte prüfen
sudo netstat -tulpn | grep :8080
```

---

## Teil 7: Nächste Schritte (Phase 2 Vorbereitung)

### Erkannte Schwachstellen dokumentieren:
1. **Schwache Passwords**: `hodor:hodor`, potentiell weitere
2. **Kerberoastable Accounts**: Service-Accounts mit SPNs
3. **ASREPRoastable Users**: Accounts ohne Kerberos Pre-Auth
4. **Unconstrained Delegation**: Kritische Privilege Escalation
5. **MSSQL Services**: Lateral Movement Möglichkeiten (castelblack/braavos)
6. **SMB Signing Disabled**: NTLM Relay Angriffe möglich
7. **Cross-Domain Trusts**: Forest-übergreifende Angriffe

### Attack Paths priorisieren:
1. **Password Spraying** → Initial Foothold
2. **Kerberoasting** → Service Account Compromise
3. **MSSQL Trusted Links** → Lateral Movement (castelblack ↔ braavos)
4. **GPO Abuse** → Privilege Escalation
5. **Cross-Forest Trust Abuse** → Full Domain/Forest Compromise

### Tools für Phase 2 vorbereiten:
- **Rubeus** (Kerberos Attacks)
- **SharpGPOAbuse** (GPO Manipulation)  
- **Impacket** (MSSQL, WMI, SMB)
- **Responder** (NTLM Relay)
- **CrackMapExec** (Lateral Movement)

---

## Zusammenfassung

✅ **BloodHound CE erfolgreich installiert und konfiguriert**  
✅ **Alle drei GOAD Domains (sevenkingdoms.local, north.sevenkingdoms.local, essos.local) enumeriert**  
✅ **Kritische Attack Paths identifiziert**  
✅ **Cross-Domain und Cross-Forest Schwachstellen erkannt**  
✅ **MSSQL Services und SMB-Signing Probleme dokumentiert**  

**Das GOAD Lab ist jetzt vollständig für die nächsten Phasen der Cyber Kill Chain vorbereitet!**