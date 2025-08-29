# Naabu Installation auf Ubuntu - Schritt-für-Schritt Anleitung

## 📋 Übersicht

Naabu ist ein High-Speed Portscanner von ProjectDiscovery, geschrieben in Go. Diese Anleitung führt dich durch die komplette Installation auf Ubuntu.

---

## 🔧 Schritt 1: Systemvoraussetzungen prüfen

### Ubuntu-Version prüfen
```bash
lsb_release -a
# Empfohlen: Ubuntu 20.04 oder neuer
```

### System aktualisieren
```bash
sudo apt update && sudo apt upgrade -y
```

### Grundlegende Tools installieren
```bash
sudo apt install -y curl wget git unzip build-essential
```

---

## 🐹 Schritt 2: Go-Language installieren

### Methode 1: APT Repository (einfach)
```bash
# Go installieren
sudo apt install -y golang-go

# Version prüfen (mindestens 1.20 benötigt)
go version
```

### Methode 2: Neueste Go-Version (empfohlen)
```bash
# Falls APT-Version zu alt ist (< 1.20)
# Neueste Go-Version herunterladen
GO_VERSION="1.21.5"
wget https://go.dev/dl/go${GO_VERSION}.linux-amd64.tar.gz

# Alte Go-Version entfernen (falls vorhanden)
sudo rm -rf /usr/local/go

# Neue Version installieren
sudo tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz

# PATH-Variable setzen
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc

# Installation prüfen
go version
# Sollte zeigen: go version go1.21.5 linux/amd64
```

---

## 📦 Schritt 3: Libpcap installieren (Erforderlich für Naabu)

```bash
# Libpcap-Bibliothek installieren (für Packet Capturing)
sudo apt install -y libpcap-dev

# Installation verifizieren
dpkg -l | grep libpcap-dev
```

---

## ⚡ Schritt 4: Naabu installieren

### Methode 1: Go Install (empfohlen)
```bash
# Neueste Version über Go installieren
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest

# Binary nach /usr/local/bin verschieben (optional, für systemweite Verfügbarkeit)
sudo mv ~/go/bin/naabu /usr/local/bin/

# Installation prüfen
naabu -version
```

### Methode 2: Binary Download (schneller)
```bash
# Neueste Version automatisch ermitteln
NAABU_VERSION=$(curl -s "https://api.github.com/repos/projectdiscovery/naabu/releases/latest" | grep -Po '"tag_name": "v\K[0-9.]+')

# Binary herunterladen
wget https://github.com/projectdiscovery/naabu/releases/download/v${NAABU_VERSION}/naabu_${NAABU_VERSION}_linux_amd64.zip

# Entpacken
unzip naabu_${NAABU_VERSION}_linux_amd64.zip

# Nach /usr/local/bin verschieben
sudo mv naabu /usr/local/bin/

# Ausführbar machen
sudo chmod +x /usr/local/bin/naabu

# Aufräumen
rm naabu_${NAABU_VERSION}_linux_amd64.zip LICENSE.md README.md

# Installation prüfen
naabu -version
```

---

## 🚀 Schritt 5: Performance-Optimierung (Optional)

### Raw Socket Berechtigung setzen
```bash
# Für bessere Performance (Root-Rechte nicht mehr nötig)
sudo setcap cap_net_raw=+eip /usr/local/bin/naabu

# Verifizierung
getcap /usr/local/bin/naabu
# Sollte zeigen: /usr/local/bin/naabu = cap_net_raw+eip
```

### Systemlimits erhöhen (für große Scans)
```bash
# File Descriptor Limits erhöhen
echo 'fs.file-max = 65536' | sudo tee -a /etc/sysctl.conf
echo '* soft nofile 65536' | sudo tee -a /etc/security/limits.conf
echo '* hard nofile 65536' | sudo tee -a /etc/security/limits.conf

# Änderungen anwenden
sudo sysctl -p
```

---

## ✅ Schritt 6: Installation testen

### Basis-Test
```bash
# Version anzeigen
naabu -version

# Hilfe anzeigen
naabu -h

# Lokalen Host scannen (Test)
naabu -host 127.0.0.1 -p 22,80,443
```

### GOAD Lab Test
```bash
# Für dein GOAD Lab (angepasst an deine IPs)
naabu -host 192.168.20.10 -p 80,88,389,445,3389

# Top 100 Ports scannen
naabu -host 192.168.20.10 -top-ports 100

# Multiple Hosts aus Datei
echo -e "192.168.20.10\n192.168.20.11\n192.168.20.12" > targets.txt
naabu -list targets.txt -top-ports 1000
```

---

## ⚙️ Schritt 7: Konfiguration optimieren

### Config-Datei erstellen
```bash
# Konfigurationsverzeichnis erstellen
mkdir -p ~/.config/naabu

# Basis-Konfiguration erstellen
cat > ~/.config/naabu/config.yaml << 'EOF'
# Naabu Configuration für GOAD Lab

# Performance Settings
rate: 1000              # Pakete pro Sekunde
retries: 2              # Wiederholungen bei Fehlern
timeout: 1000           # Timeout in Millisekunden
concurrency: 25         # Parallel Worker

# Scan Settings
ping: true              # ICMP Ping für Host Discovery
verify: true            # Ports mit TCP verifizieren
scan-type: "s"          # SYN Scan (s) oder CONNECT (c)

# Output Settings
verbose: true           # Ausführliche Ausgabe
json: false            # JSON-Output
output: "scan-results.txt"  # Output-Datei

# Network Settings
interface: "eth0"       # Netzwerk-Interface
exclude-cdn: true       # CDN IPs überspringen

# Common AD/Windows Ports für GOAD
ports: "21,22,23,25,53,80,88,110,111,135,139,143,389,443,445,636,993,995,1433,1521,3268,3269,3389,5985,5986"
EOF
```

### Erweiterte Alias erstellen
```bash
# Nützliche Aliases für GOAD Lab
cat >> ~/.bashrc << 'EOF'

# Naabu Aliases für GOAD Lab
alias naabu-quick='naabu -top-ports 100'
alias naabu-full='naabu -p -'
alias naabu-ad='naabu -p 53,88,135,389,445,636,3268,3269,3389,5985,5986'
alias naabu-web='naabu -p 80,443,8080,8443'
alias naabu-db='naabu -p 1433,1521,3306,5432'
alias naabu-goad='naabu -list ~/goad-targets.txt -config ~/.config/naabu/config.yaml'
EOF

# Aliases aktivieren
source ~/.bashrc
```

---

## 🎯 Schritt 8: Praktische Nutzung für GOAD Lab

### Target-Liste erstellen
```bash
# GOAD Lab Hosts (angepasst an deine Umgebung)
cat > ~/goad-targets.txt << 'EOF'
192.168.20.10
192.168.20.11
192.168.20.12
192.168.20.22
192.168.20.23
EOF
```

### Standard-Scans
```bash
# Basis-Scan aller GOAD Hosts
naabu -list ~/goad-targets.txt -o goad-ports.txt

# AD-spezifische Ports
naabu -list ~/goad-targets.txt -p 53,88,135,389,445,636,3268,3269,3389,5985,5986 -o goad-ad-ports.txt

# Top 1000 Ports mit JSON-Output
naabu -list ~/goad-targets.txt -top-ports 1000 -json -o goad-full-scan.json

# Verbose Scan mit Details
naabu -list ~/goad-targets.txt -verbose -verify -o goad-verbose.txt
```

### Integration mit anderen Tools
```bash
# Naabu → Nuclei Pipeline
naabu -list ~/goad-targets.txt -json -silent | jq -r '.host + ":" + (.port|tostring)' > open-ports.txt

# Naabu → Nmap für Service Detection
naabu -list ~/goad-targets.txt -silent | awk -F: '{print $1}' | sort -u > live-hosts.txt
```

---

## 🔧 Troubleshooting

### Problem 1: "Permission denied" Fehler
```bash
# Lösung: Capabilities setzen oder als Root ausführen
sudo setcap cap_net_raw=+eip /usr/local/bin/naabu

# Oder mit sudo ausführen
sudo naabu -host 192.168.20.10
```

### Problem 2: "command not found: naabu"
```bash
# PATH prüfen
echo $PATH

# Go bin-Verzeichnis zu PATH hinzufügen
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc

# Oder Binary manuell verschieben
sudo cp ~/go/bin/naabu /usr/local/bin/
```

### Problem 3: Libpcap Fehler
```bash
# Libpcap neu installieren
sudo apt install --reinstall libpcap-dev

# Development-Pakete installieren
sudo apt install -y libpcap0.8-dev

# Falls weiterhin Probleme:
sudo apt install -y libpcap-dev build-essential
```

### Problem 4: Langsame Scans
```bash
# Rate erhöhen (Vorsicht in produktiven Netzen!)
naabu -host target -rate 5000

# Concurrency erhöhen
naabu -host target -c 50

# Timeout reduzieren
naabu -host target -timeout 500
```

### Problem 5: Go-Version zu alt
```bash
# Aktuelle Go-Version installieren
sudo rm -rf /usr/local/go
wget https://go.dev/dl/go1.21.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.5.linux-amd64.tar.gz

# PATH aktualisieren
export PATH=$PATH:/usr/local/go/bin
go version
```

---

## 📊 Erweiterte Features

### Host Discovery
```bash
# Nur Host Discovery (kein Port-Scan)
naabu -list ~/goad-targets.txt -sn

# Host Discovery mit verschiedenen Methoden
naabu -host 192.168.20.10 -ping -pe -ps 80 -pa 443

# ARP Ping (lokales Netz)
naabu -list ~/goad-targets.txt -arp-ping
```

### Passive Enumeration
```bash
# Shodan Integration (passiv)
naabu -host 192.168.20.10 -passive

# DNS Port Scan
naabu -host sevenkingdoms.local -p 53 -scan-all-ips
```

### Automation Scripts
```bash
#!/bin/bash
# goad-port-monitor.sh
TARGET_LIST="$HOME/goad-targets.txt"
BASELINE="$HOME/goad-baseline-ports.txt"
CURRENT="$HOME/goad-current-ports.txt"

# Aktueller Scan
naabu -list "$TARGET_LIST" -top-ports 1000 -silent > "$CURRENT"

# Vergleich mit Baseline
if [ -f "$BASELINE" ]; then
    echo "=== Neue Ports gefunden ==="
    comm -13 <(sort "$BASELINE") <(sort "$CURRENT")
    echo "=== Geschlossene Ports ==="
    comm -23 <(sort "$BASELINE") <(sort "$CURRENT")
else
    echo "Erstelle Baseline..."
    cp "$CURRENT" "$BASELINE"
fi

# Ergebnisse archivieren
cp "$CURRENT" "$HOME/goad-ports-$(date +%Y%m%d-%H%M%S).txt"
```

---

## 📝 Zusammenfassung

### ✅ **Installation erfolgreich:**
- Ubuntu-System vorbereitet
- Go-Language installiert (Version 1.21+)
- Libpcap-Bibliothek installiert
- Naabu erfolgreich installiert und konfiguriert
- Performance-Optimierungen angewendet

### 🚀 **Bereit für GOAD Lab:**
- Target-Listen für deine IPs (192.168.20.x) erstellt
- Konfiguration für AD-Umgebung optimiert
- Aliases und Scripts für effiziente Nutzung
- Integration mit anderen Pentest-Tools vorbereitet

### 🛠️ **Nächste Schritte:**
1. Führe ersten Test-Scan durch: `naabu-goad`
2. Integriere mit Nuclei für Vulnerability Scanning
3. Erstelle Monitoring-Scripts für kontinuierliche Reconnaissance

**Naabu ist jetzt einsatzbereit für dein GOAD Lab!**