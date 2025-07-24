


Im Rahmen der Netzwerksicherheit und Systemadministration ist der Port-Scan eine fundamentale Technik, um Informationen über ein Zielsystem zu gewinnen.

**Was ist ein Port-Scan?**

Ein Port-Scan ist ein Verfahren, bei dem systematisch überprüft wird, welche Netzwerkports eines Zielsystems offen, geschlossen oder gefiltert sind. Netzwerkports sind Kommunikationsendpunkte, die es Anwendungen und Diensten ermöglichen, über ein Netzwerk zu kommunizieren. Jeder Port ist einer bestimmten Anwendung oder einem bestimmten Dienst zugeordnet.

**Zweck eines Port-Scans:**

- **Identifizierung offener Dienste:**
    - Erkennung, welche Anwendungen oder Dienste auf einem System aktiv sind.
    - Dies ist entscheidend für die Bewertung der Sicherheitslage eines Systems.
- **Schwachstellenanalyse:**
    - Offene Ports können potenzielle Einfallstor (backdoor) für Angreifer sein.
    - Ein Port-Scan hilft, diese potenziellen Schwachstellen zu identifizieren.
- **Netzwerkaufklärung:**
    - Port-Scans werden verwendet, um die Netzwerkstruktur und die vorhandenen Systeme zu erkunden.
- **Firewall-Überprüfung:**
    - Überprüfung, ob Firewalls ordnungsgemäß konfiguriert sind und unerwünschte Ports blockieren.

**Arten von Port-Scans:**

- **TCP-SYN-Scan (Half-Open Scan):**
    - Sendet ein SYN-Paket und wartet auf eine SYN-ACK-Antwort.
    - Ermöglicht eine schnelle und unauffällige Überprüfung offener Ports.
- **TCP-Connect-Scan:**
    - Versucht, eine vollständige TCP-Verbindung herzustellen.
    - Ist zuverlässig, aber leichter zu erkennen.
- **UDP-Scan:**
    - Sendet UDP-Pakete an die Zielports.
    - Ermöglicht die Überprüfung von UDP-basierten Diensten.
- **FIN/NULL/Xmas-Scans:**
    - Sendet spezielle TCP-Pakete, um Firewall-Regeln zu umgehen.
    - Kann Informationen über den Zustand von Ports liefern.

**Wichtige Werkzeuge:**

- **Nmap:** Ein weit verbreitetes und leistungsstarkes Werkzeug für Port-Scans.
- **Wireshark:** Ein Netzwerkprotokollanalysator, der zur Überwachung des Netzwerkverkehrs verwendet werden kann.

**Rechtliche und ethische Überlegungen:**

- Port-Scans ohne Genehmigung können illegal sein.
- Es ist wichtig, die geltenden Gesetze und Vorschriften einzuhalten.
- In einer Professionellen umgebung, werden Portscans in der regel in der „Rules of engagement“ festgelegt.

Port-Scans sind ein unverzichtbares Werkzeug für Netzwerkadministratoren und Sicherheitsexperten. Sie ermöglichen es, die Sicherheit von Systemen zu bewerten und potenzielle Schwachstellen zu identifizieren.


Beispiel : 

Schritt-für-Schritt-Beispiel eines Port-Scans mit Nmap, einem der gängigsten Werkzeuge für diese Aufgabe:

**Szenario:**

- Zielsystem: Eine virtuelle Maschine mit der IP-Adresse 192.168.1.100.
- Angreifer-System: Kali Linux.

**Schritt-für-Schritt-Vorgehensweise:**

1. **Öffnen Sie ein Terminal:**
    
    - Starten Sie ein Terminalfenster in Kali Linux.
2. **Grundlegender TCP-SYN-Scan:**
    
    - Führen Sie den folgenden Befehl aus, um einen grundlegenden TCP-SYN-Scan durchzuführen:
        - `nmap -sS 192.168.1.100`
    - Dieser Befehl sendet SYN-Pakete an die gängigsten TCP-Ports des Zielsystems und zeigt an, welche Ports offen sind.
    - Die Option -sS steht hierbei für SYN-Scan.
3. **Detaillierter Scan mit Versionserkennung:**
    
    - Um detailliertere Informationen über die offenen Ports und die laufenden Dienste zu erhalten, führen Sie den folgenden Befehl aus:
        - `nmap -sV 192.168.1.100`
    - Die Option -sV bedeutet Versionserkennung und versucht die Version der Softwäre, welche auf den gefundenen Ports läuft herauszufinden.
4. **Scan aller TCP-Ports:**
    
    - Um alle 65535 TCP-Ports zu scannen, führen Sie den folgenden Befehl aus:
        - `nmap -p 1-65535 192.168.1.100`
    - Die Option -p gibt an, welche Ports gescannt werden sollen.
5. **UDP-Scan:**
    
    - Um UDP-Ports zu scannen, führen Sie den folgenden Befehl aus:
        - `nmap -sU 192.168.1.100`
    - Die Option -sU bedeutet UDP-Scan.
    - UDP Scans können länger dauern als TCP Scans.
6. **Ergebnisse analysieren:**
    
    - Nmap zeigt die Ergebnisse des Scans im Terminal an.
    - Die Ergebnisse enthalten Informationen über offene, geschlossene und gefilterte Ports sowie die laufenden Dienste.

**Beispielausgabe:**

```
Nmap scan report for 192.168.1.100
Host is up (0.00029s latency).
Not shown: 996 closed ports
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open http Apache httpd 2.4.29 ((Ubuntu))
443/tcp open https Apache httpd 2.4.29 ((Ubuntu))
3306/tcp open mysql MySQL 5.7.29-0ubuntu0.18.04.1
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 4.88 seconds
```