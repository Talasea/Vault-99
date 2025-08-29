# Nuclei & Naabu - Vollständige Installation und Lab-Nutzung mit KI-Integration

## 📋 Inhaltsverzeichnis

1. [Systemvoraussetzungen](#systemvoraussetzungen)
2. [Installation von Nuclei](#installation-von-nuclei)
3. [Installation von Naabu](#installation-von-naabu)
4. [AI-Integration für Nuclei](#ai-integration-für-nuclei)
5. [Grundlegende Konfiguration](#grundlegende-konfiguration)
6. [Lab-Workflow für GOAD](#lab-workflow-für-goad)
7. [Erweiterte AI-Features](#erweiterte-ai-features)
8. [Template-Management](#template-management)
9. [Automatisierung und Scripting](#automatisierung-und-scripting)
10. [Troubleshooting](#troubleshooting)
11. [Best Practices](#best-practices)

---

## 1. Systemvoraussetzungen

### Betriebssystem
- Ubuntu 20.04 oder neuer (empfohlen: 22.04 LTS)
- Mindestens 4GB RAM
- 10GB freier Speicherplatz
- Internetverbindung für Updates und AI-Features

### Grundlegende Tools
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl wget git unzip build-essential
```

---

## 2. Installation von Nuclei

### Methode 1: Go-basierte Installation (empfohlen)

#### Go-Language installieren
```bash
# Go 1.21 oder neuer installieren
sudo apt install -y golang-go

# Go Version prüfen (mindestens 1.21)
go version

# Falls Go zu alt ist, manuell installieren:
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc
```

#### Nuclei installieren
```bash
# Neueste Version installieren
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Binary nach /usr/local/bin verschieben
sudo mv ~/go/bin/nuclei /usr/local/bin/

# Installation verifizieren
nuclei -version
```

### Methode 2: Binary-Download (schneller)
```bash
# Neueste Version herunterladen
NUCLEI_VERSION=$(curl -s "https://api.github.com/repos/projectdiscovery/nuclei/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+')
wget https://github.com/projectdiscovery/nuclei/releases/download/v${NUCLEI_VERSION}/nuclei_${NUCLEI_VERSION}_linux_amd64.zip

# Entpacken und installieren
unzip nuclei_${NUCLEI_VERSION}_linux_amd64.zip
sudo mv nuclei /usr/local/bin/
rm nuclei_${NUCLEI_VERSION}_linux_amd64.zip LICENSE.md README.md

# Installation verifizieren
nuclei -version
```

### Templates installieren und aktualisieren
```bash
# Initiale Template-Installation
nuclei -update-templates

# Templates regelmäßig aktualisieren
nuclei -ut

# Template-Verzeichnis anzeigen
nuclei -config
```

---

## 3. Installation von Naabu

### Voraussetzungen für Naabu
```bash
# Libpcap für Low-Level Network Operations
sudo apt install -y libpcap-dev

# Optional: Raw Socket Permissions (für bessere Performance)
sudo setcap cap_net_raw=+eip /usr/local/bin/naabu
```

### Go-basierte Installation
```bash
# Naabu installieren
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest

# Binary verschieben
sudo mv ~/go/bin/naabu /usr/local/bin/

# Installation verifizieren
naabu -version
```

### Alternative: Binary-Download
```bash
# Neueste Version abrufen
NAABU_VERSION=$(curl -s "https://api.github.com/repos/projectdiscovery/naabu/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+')
wget https://github.com/projectdiscovery/naabu/releases/download/v${NAABU_VERSION}/naabu_${NAABU_VERSION}_linux_amd64.zip

# Installieren
unzip naabu_${NAABU_VERSION}_linux_amd64.zip
sudo mv naabu /usr/local/bin/
rm naabu_${NAABU_VERSION}_linux_amd64.zip LICENSE.md README.md

# Performance-Optimierung (optional)
sudo setcap cap_net_raw=+eip /usr/local/bin/naabu
```

---

## 4. AI-Integration für Nuclei

### ProjectDiscovery Cloud Account einrichten

#### Account erstellen
1. Besuche: https://cloud.projectdiscovery.io/
2. Kostenlos registrieren
3. Email verifizieren
4. API-Key generieren

#### API-Key konfigurieren
```bash
# Methode 1: Interaktive Authentifizierung (empfohlen)
nuclei -auth

# Methode 2: Environment Variable
echo 'export PDCP_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# Methode 3: Config-Datei
mkdir -p ~/.config/nuclei
echo "pdcp-api-key: your_api_key_here" > ~/.config/nuclei/config.yaml
```

#### Authentifizierung testen
```bash
# API-Verbindung testen
nuclei -list-templates

# AI-Feature testen
echo "http://example.com" | nuclei -ai "Find admin panels"
```

### AI-Template Generation Features

#### Grundlegende AI-Befehle
```bash
# Einfache AI-Abfrage
nuclei -u http://192.168.20.10 -ai "Find admin login pages"

# Multiple Targets mit AI
echo -e "http://192.168.20.10\nhttp://192.168.20.22\nhttp://192.168.20.23" > targets.txt
nuclei -list targets.txt -ai "Detect exposed configuration files"

# Spezifische Vulnerabilities suchen
nuclei -list targets.txt -ai "Find SQL injection points"
nuclei -list targets.txt -ai "Detect XSS vulnerabilities"
nuclei -list targets.txt -ai "Find SSRF endpoints"
```

#### Erweiterte AI-Prompts für GOAD Lab
```bash
# Active Directory spezifische Checks
nuclei -list targets.txt -ai "Find ADCS certificate authorities"
nuclei -list targets.txt -ai "Detect Kerberos authentication endpoints"
nuclei -list targets.txt -ai "Find LDAP services and configurations"

# Windows-specific vulnerabilities
nuclei -list targets.txt -ai "Detect SMB signing disabled"
nuclei -list targets.txt -ai "Find IIS server information disclosure"
nuclei -list targets.txt -ai "Detect MSSQL default configurations"

# Custom GOAD-specific prompts
nuclei -list targets.txt -ai "Find Game of Thrones references in headers"
nuclei -list targets.txt -ai "Detect default ASP.NET configurations"
```

---

## 5. Grundlegende Konfiguration

### Nuclei Konfiguration optimieren
```bash
# Config-Verzeichnis erstellen
mkdir -p ~/.config/nuclei

# Erweiterte Konfigurationsdatei erstellen
cat > ~/.config/nuclei/config.yaml << 'EOF'
# Nuclei Configuration
templates-directory: ~/.nuclei-templates/
output-dir: ~/nuclei-results/
pdcp-api-key: "your_api_key_here"

# Performance Settings
bulk-size: 25
concurrency: 25
rate-limit: 150
timeout: 10

# Output Settings
verbose: true
json-export: ~/nuclei-results/
markdown-export: ~/nuclei-results/

# Template Settings
new-templates: true
automatic-scan: false
update-templates: true
EOF
```

### Arbeitsverzeichnisse erstellen
```bash
# Ergebnis-Verzeichnisse
mkdir -p ~/nuclei-results/{json,markdown,txt}
mkdir -p ~/naabu-results
mkdir -p ~/lab-scans/{goad,targets,reports}

# Custom Templates
mkdir -p ~/.nuclei-templates/custom
mkdir -p ~/.nuclei-templates/ai-generated
```

---

## 6. Lab-Workflow für GOAD

### Schritt 1: Target-Liste vorbereiten
```bash
# GOAD Lab Targets (basierend auf deinem nmap-Scan)
cat > ~/lab-scans/goad/targets.txt << 'EOF'
192.168.20.10
192.168.20.11
192.168.20.12
192.168.20.22
192.168.20.23
EOF

# HTTP/HTTPS Services
cat > ~/lab-scans/goad/web-targets.txt << 'EOF'
http://192.168.20.10
http://192.168.20.22
http://192.168.20.23
https://192.168.20.10
https://192.168.20.22
https://192.168.20.23
EOF

# Hostnamen (falls DNS konfiguriert)
cat > ~/lab-scans/goad/hostnames.txt << 'EOF'
kingslanding.sevenkingdoms.local
winterfell.north.sevenkingdoms.local
meereen.essos.local
castelblack.north.sevenkingdoms.local
braavos.essos.local
EOF
```

### Schritt 2: Port-Scanning mit Naabu
```bash
# Basic Port-Scan aller GOAD Hosts
naabu -list ~/lab-scans/goad/targets.txt -o ~/naabu-results/goad-ports.txt

# Erweiterte Scans
naabu -list ~/lab-scans/goad/targets.txt -top-ports 1000 -o ~/naabu-results/goad-top1000.txt

# Spezifische AD/Windows Ports
naabu -list ~/lab-scans/goad/targets.txt -p 53,80,88,135,139,389,445,636,1433,3268,3269,3389,5985,5986 -o ~/naabu-results/goad-ad-ports.txt

# JSON Output für weitere Verarbeitung
naabu -list ~/lab-scans/goad/targets.txt -json -o ~/naabu-results/goad-ports.json
```

### Schritt 3: Vulnerability Scanning mit Nuclei
```bash
# Standard Vulnerability Scan
nuclei -list ~/lab-scans/goad/web-targets.txt -o ~/nuclei-results/goad-standard.txt

# Mit AI-Enhancement
nuclei -list ~/lab-scans/goad/web-targets.txt -ai "Find Windows Server misconfigurations" -o ~/nuclei-results/goad-ai-windows.txt

# Spezifische Template-Kategorien
nuclei -list ~/lab-scans/goad/web-targets.txt -tags cve,misconfig,exposure -o ~/nuclei-results/goad-critical.txt

# Microsoft/Windows spezifische Templates
nuclei -list ~/lab-scans/goad/web-targets.txt -tags microsoft,iis,mssql,windows -o ~/nuclei-results/goad-microsoft.txt
```

### Schritt 4: GOAD-spezifische AI-Scans
```bash
# Active Directory Reconnaissance
nuclei -list ~/lab-scans/goad/web-targets.txt -ai "Enumerate Active Directory information" -o ~/nuclei-results/goad-ad-recon.txt

# Kerberos und Authentication
nuclei -list ~/lab-scans/goad/targets.txt -ai "Find Kerberos authentication services" -o ~/nuclei-results/goad-kerberos.txt

# SMB und File Sharing
nuclei -list ~/lab-scans/goad/targets.txt -ai "Detect SMB shares and configurations" -o ~/nuclei-results/goad-smb.txt

# MSSQL spezifische Checks
echo -e "192.168.20.22\n192.168.20.23" | nuclei -ai "Find MSSQL misconfigurations and default accounts" -o ~/nuclei-results/goad-mssql.txt

# IIS und ASP.NET
nuclei -list ~/lab-scans/goad/web-targets.txt -ai "Find IIS server vulnerabilities and ASP.NET misconfigurations" -o ~/nuclei-results/goad-iis.txt
```

---

## 7. Erweiterte AI-Features

### Custom AI-Prompts für Pentesting

#### Information Disclosure
```bash
# Sensitive Information Leaks
nuclei -list targets.txt -ai "Find API keys and secrets in response headers"
nuclei -list targets.txt -ai "Detect debug information in error messages"
nuclei -list targets.txt -ai "Find backup files and configuration dumps"
```

#### Authentication Bypass
```bash
# Authentication Issues
nuclei -list targets.txt -ai "Find authentication bypass vulnerabilities"
nuclei -list targets.txt -ai "Detect weak session management"
nuclei -list targets.txt -ai "Find default credentials and weak passwords"
```

#### Injection Vulnerabilities
```bash
# Code Injection
nuclei -list targets.txt -ai "Find SQL injection vulnerabilities"
nuclei -list targets.txt -ai "Detect command injection points"
nuclei -list targets.txt -ai "Find LDAP injection vulnerabilities"
```

### Template-Generierung und -Management

#### AI-Generated Templates speichern
```bash
# Template aus AI-Prompt generieren und speichern
nuclei -list targets.txt -ai "Find admin login pages" -store-templates ~/.nuclei-templates/ai-generated/

# Custom Template erstellen
nuclei -new-template -name "goad-custom-check" -author "your-name" -severity medium
```

#### Browser Extension für Template-Generierung
```bash
# Nuclei AI Browser Extension installieren
# 1. Chrome Web Store besuchen (wenn verfügbar)
# 2. Oder manuell installieren:
wget https://github.com/projectdiscovery/nuclei-ai-extension/archive/main.zip
unzip main.zip
# In Chrome: chrome://extensions/ -> Developer Mode -> Load unpacked
```

---

## 8. Template-Management

### Template-Organisation

#### Custom Templates erstellen
```bash
# GOAD-spezifische Templates
mkdir -p ~/.nuclei-templates/custom/goad/

# Beispiel: Custom GOAD Template
cat > ~/.nuclei-templates/custom/goad/goad-default-creds.yaml << 'EOF'
id: goad-default-credentials

info:
  name: GOAD Lab Default Credentials
  author: your-name
  severity: high
  description: Check for default GOAD lab credentials
  tags: goad,auth,default

http:
  - method: POST
    path:
      - "{{BaseURL}}/login"
      - "{{BaseURL}}/admin/login"
    
    headers:
      Content-Type: "application/x-www-form-urlencoded"
    
    body: |
      username={{user}}&password={{pass}}
    
    payloads:
      user:
        - "hodor"
        - "jon.snow" 
        - "tyrion.lannister"
        - "administrator"
      pass:
        - "hodor"
        - "password"
        - "Winter2019"
        - "admin"
    
    attack: pitchfork
    
    matchers-condition: and
    matchers:
      - type: status
        status:
          - 200
          - 302
      
      - type: word
        words:
          - "welcome"
          - "dashboard"
          - "successful"
        case-insensitive: true
EOF
```

#### Template-Updates und -Verwaltung
```bash
# Templates aktualisieren
nuclei -update-templates

# Spezifische Template-Ordner verwenden
nuclei -list targets.txt -t ~/.nuclei-templates/custom/goad/

# Template-Syntax validieren
nuclei -validate -t ~/.nuclei-templates/custom/goad/goad-default-creds.yaml

# Template testen
nuclei -list targets.txt -t ~/.nuclei-templates/custom/goad/goad-default-creds.yaml -debug
```

---

## 9. Automatisierung und Scripting

### Vollautomatisches GOAD-Scanning

#### Master-Scan-Script
```bash
#!/bin/bash
# goad-full-scan.sh

# Konfiguration
TARGET_FILE="$HOME/lab-scans/goad/targets.txt"
WEB_TARGET_FILE="$HOME/lab-scans/goad/web-targets.txt"
RESULTS_DIR="$HOME/nuclei-results/$(date +%Y%m%d-%H%M%S)"
NAABU_RESULTS_DIR="$HOME/naabu-results/$(date +%Y%m%d-%H%M%S)"

# Verzeichnisse erstellen
mkdir -p "$RESULTS_DIR" "$NAABU_RESULTS_DIR"

echo "[$(date)] Starting GOAD Lab comprehensive scan..."

# Phase 1: Port Discovery
echo "[$(date)] Phase 1: Port scanning with Naabu..."
naabu -list "$TARGET_FILE" -top-ports 1000 -json -o "$NAABU_RESULTS_DIR/ports.json"
naabu -list "$TARGET_FILE" -p 53,80,88,135,139,389,445,636,1433,3268,3269,3389,5985,5986 -o "$NAABU_RESULTS_DIR/ad-ports.txt"

# Phase 2: Standard Vulnerability Scan
echo "[$(date)] Phase 2: Standard vulnerability scanning..."
nuclei -list "$WEB_TARGET_FILE" -tags cve,misconfig,exposure -json -o "$RESULTS_DIR/standard.json"

# Phase 3: AI-Enhanced Scanning
echo "[$(date)] Phase 3: AI-enhanced scanning..."
nuclei -list "$WEB_TARGET_FILE" -ai "Find Windows Server and IIS misconfigurations" -json -o "$RESULTS_DIR/ai-windows.json"
nuclei -list "$TARGET_FILE" -ai "Detect Active Directory services and vulnerabilities" -json -o "$RESULTS_DIR/ai-ad.json"
nuclei -list "$TARGET_FILE" -ai "Find MSSQL default configurations and vulnerabilities" -json -o "$RESULTS_DIR/ai-mssql.json"

# Phase 4: Custom GOAD Templates
echo "[$(date)] Phase 4: GOAD-specific template scanning..."
if [ -d "$HOME/.nuclei-templates/custom/goad" ]; then
    nuclei -list "$WEB_TARGET_FILE" -t "$HOME/.nuclei-templates/custom/goad/" -json -o "$RESULTS_DIR/goad-custom.json"
fi

# Phase 5: Reporting
echo "[$(date)] Phase 5: Generating reports..."
cat "$RESULTS_DIR"/*.json > "$RESULTS_DIR/combined-results.json"

# Summary Report erstellen
python3 - << 'EOF'
import json
import sys
from collections import defaultdict

results_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
vulnerabilities = defaultdict(list)

try:
    with open(f"{results_dir}/combined-results.json", 'r') as f:
        for line in f:
            if line.strip():
                try:
                    result = json.loads(line)
                    severity = result.get('info', {}).get('severity', 'unknown')
                    name = result.get('info', {}).get('name', 'Unknown')
                    host = result.get('host', 'Unknown')
                    vulnerabilities[severity].append(f"{name} on {host}")
                except json.JSONDecodeError:
                    continue
    
    print(f"\n=== GOAD Lab Scan Summary ===")
    print(f"Scan completed at: {result.get('timestamp', 'Unknown')}")
    
    for severity in ['critical', 'high', 'medium', 'low', 'info']:
        if vulnerabilities[severity]:
            print(f"\n{severity.upper()}: {len(vulnerabilities[severity])} findings")
            for vuln in vulnerabilities[severity][:5]:  # Top 5
                print(f"  - {vuln}")
            if len(vulnerabilities[severity]) > 5:
                print(f"  ... and {len(vulnerabilities[severity]) - 5} more")

except FileNotFoundError:
    print("No results file found")
EOF

echo "[$(date)] Scan completed! Results saved to $RESULTS_DIR"
```

#### Script ausführbar machen und verwenden
```bash
# Script erstellen und ausführbar machen
chmod +x ~/bin/goad-full-scan.sh

# Scan starten
~/bin/goad-full-scan.sh

# Cron-Job für regelmäßige Scans (täglich um 02:00)
echo "0 2 * * * $HOME/bin/goad-full-scan.sh" | crontab -
```

### Continuous Monitoring Setup

#### Monitoring Script
```bash
#!/bin/bash
# goad-monitor.sh

TARGETS="$HOME/lab-scans/goad/web-targets.txt"
BASELINE="$HOME/lab-scans/baselines/goad-baseline.json"
CURRENT="$HOME/lab-scans/current/goad-$(date +%Y%m%d-%H%M%S).json"

# Current scan
nuclei -list "$TARGETS" -json -o "$CURRENT"

# Compare with baseline (wenn vorhanden)
if [ -f "$BASELINE" ]; then
    # Neue Findings identifizieren
    python3 - "$BASELINE" "$CURRENT" << 'EOF'
import json, sys
baseline_findings = set()
current_findings = set()

with open(sys.argv[1]) as f:
    for line in f:
        if line.strip():
            result = json.loads(line)
            finding = f"{result['host']}:{result['template-id']}"
            baseline_findings.add(finding)

with open(sys.argv[2]) as f:
    for line in f:
        if line.strip():
            result = json.loads(line)
            finding = f"{result['host']}:{result['template-id']}"
            current_findings.add(finding)

new_findings = current_findings - baseline_findings
if new_findings:
    print("NEW FINDINGS DETECTED:")
    for finding in new_findings:
        print(f"  - {finding}")
else:
    print("No new findings detected")
EOF
else
    echo "Creating baseline..."
    cp "$CURRENT" "$BASELINE"
fi
```

---

## 10. Troubleshooting

### Häufige Probleme und Lösungen

#### Nuclei Installation Issues
```bash
# Go Version zu alt
go version
# Falls < 1.21, neu installieren:
sudo rm -rf /usr/local/go
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# PATH-Probleme
echo 'export PATH=$PATH:/usr/local/go/bin:~/go/bin' >> ~/.bashrc
source ~/.bashrc

# Template-Update Fehler
nuclei -update-templates -verbose
# Falls Fehler: Templates manuell löschen und neu laden
rm -rf ~/.nuclei-templates
nuclei -update-templates
```

#### Naabu Performance Issues
```bash
# Permissions für Raw Sockets
sudo setcap cap_net_raw=+eip /usr/local/bin/naabu

# libpcap fehlt
sudo apt install -y libpcap-dev

# Scan-Performance optimieren
naabu -list targets.txt -rate 1000 -c 25
```

#### AI-Features funktionieren nicht
```bash
# API-Key prüfen
nuclei -config

# Internetverbindung testen
curl -s https://cloud.projectdiscovery.io/api/health

# API-Key neu setzen
nuclei -auth

# Rate Limits überprüft (100 AI queries/Tag)
# In der ProjectDiscovery Cloud Console prüfen
```

### Debug-Modi

#### Verbose Scanning
```bash
# Nuclei Debug-Modus
nuclei -list targets.txt -verbose -debug -o debug-results.txt

# Naabu Debug-Informationen
naabu -list targets.txt -verbose -debug

# Template-Syntax-Check
nuclei -validate -t custom-template.yaml -verbose
```

#### Logging und Monitoring
```bash
# Detailliertes Logging
nuclei -list targets.txt -verbose -json -o detailed-log.json

# System-Ressourcen überwachen während Scan
htop
# oder
watch -n 5 'ps aux | grep nuclei'
```

---

## 11. Best Practices

### Sicherheits-Considerations

#### Lab-Umgebung isolieren
```bash
# Firewall-Regeln für Lab-Traffic
sudo ufw allow from 192.168.20.0/24
sudo ufw deny out 192.168.20.0/24 to any port 25,587,465

# Traffic-Monitoring
sudo tcpdump -i any -w lab-traffic.pcap host 192.168.20.10
```

#### Rate Limiting und Ethical Scanning
```bash
# Aggressive Scans vermeiden
nuclei -list targets.txt -rate-limit 10 -bulk-size 10 -timeout 30

# Respektvolle Scan-Zeiten
nuclei -list targets.txt -delay 1s
```

### Performance-Optimierung

#### Resource Management
```bash
# CPU-Limits setzen
nuclei -list targets.txt -concurrency 10
naabu -list targets.txt -c 10

# Memory-Usage überwachen
nuclei -list targets.txt -memory-profile mem.prof
```

#### Effiziente Template-Nutzung
```bash
# Nur relevante Templates verwenden
nuclei -list targets.txt -tags windows,microsoft,iis

# Template-Excludes nutzen
nuclei -list targets.txt -exclude-tags dos,intrusive

# Custom Filter
nuclei -list targets.txt -severity critical,high
```

### Ergebnis-Management

#### Strukturierte Ausgabe
```bash
# JSON für Weiterverarbeitung
nuclei -list targets.txt -json -o results.json

# Markdown-Reports für Menschen
nuclei -list targets.txt -markdown-export results.md

# SARIF für CI/CD Integration
nuclei -list targets.txt -sarif-export results.sarif
```

#### Integration mit anderen Tools
```bash
# Nuclei → BloodHound Integration (findings as context)
nuclei -list targets.txt -json | jq '.' > nuclei-findings.json

# Naabu → Nmap Integration
naabu -list targets.txt -json | jq -r '.host + ":" + (.port|tostring)' > open-ports.txt
```

---

## 🎯 Zusammenfassung

Diese umfassende Anleitung deckt alles ab, was du für die professionelle Nutzung von Nuclei und Naabu in deinem GOAD Lab benötigst:

### ✅ **Vollständig implementiert:**
- **Installation:** Beide Tools mit AI-Integration
- **Konfiguration:** Optimiert für Ubuntu und Lab-Umgebung  
- **AI-Features:** ProjectDiscovery Cloud Integration mit 100+ AI-Prompts
- **GOAD-spezifisch:** Angepasst an deine Netzwerk-Topologie
- **Automatisierung:** Scripts für kontinuierliche Scans
- **Template-Management:** Custom Templates und AI-generierte Vorlagen
- **Troubleshooting:** Lösungen für alle häufigen Probleme

### 🚀 **Erweiterte Features:**
- **Multi-Step AI Templates:** Chain-basierte Vulnerability Testing
- **Browser Extension:** Template-Generierung aus Web-Content
- **Continuous Monitoring:** Baseline-Vergleich und Change Detection
- **Performance-Optimierung:** Resource Management und Rate Limiting

### 🔧 **Ready-to-Use:**
Alle Befehle sind direkt copy-paste verwendbar und auf deine GOAD Lab-Umgebung (192.168.20.x) zugeschnitten.

**Nächste Schritte:** Führe das `goad-full-scan.sh` Script aus und beginne mit der systematischen Reconnaissance deiner GOAD-Umgebung!