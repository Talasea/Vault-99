


**Benötigte Hardware:**

- Raspberry Pi 4B
- Micro-SD-Karte (mindestens 16 GB)
- Netzteil für den Raspberry Pi
- Zusätzlicher WLAN-Adapter (der den Monitor-Modus unterstützt, z. B. Alfa AWUS036ACH)

**Schritt 1: Raspberry Pi OS installieren:**

1. **Raspberry Pi Imager herunterladen:**
    - Besuchen Sie die offizielle Raspberry Pi-Website und laden Sie den Raspberry Pi Imager für Ihr Betriebssystem herunter:
    - [Raspberry Pi OS - Raspberry Pi](https://www.raspberrypi.com/software/)
2. **Raspberry Pi OS installieren:**
    - Führen Sie den Raspberry Pi Imager aus.
    - Wählen Sie "Raspberry Pi OS (64-bit)" als Betriebssystem.
    - Wählen Sie Ihre Micro-SD-Karte als Ziel.
    - Klicken Sie auf "Schreiben", um das Betriebssystem auf die SD-Karte zu installieren.
3. **Raspberry Pi starten:**
    - Legen Sie die Micro-SD-Karte in den Raspberry Pi ein und starten Sie ihn.
    - Verbinden Sie den Raspberry Pi mit einem Monitor, einer Tastatur und einer Maus.
    - Oder falls sie eine headless installation wünschen, muss SSH bei der OS installation in den erweiterten einstellungen aktiviert werden.

**Schritt 2: Netzwerk-Konfiguration:**

1. **WLAN-Adapter konfigurieren:**
    - Schließen Sie den zusätzlichen WLAN-Adapter an den Raspberry Pi an.
    - Überprüfen Sie, ob der Adapter erkannt wird (mit `iwconfig` oder `ifconfig`).
2. **Access Point einrichten:**
    - Installieren Sie `hostapd` und `dnsmasq`:
        - `sudo apt update`
        - `sudo apt install hostapd dnsmasq`
    - Konfigurieren Sie `hostapd` (z. B. in `/etc/hostapd/hostapd.conf`):
        - Fügen Sie die entsprechenden Konfigurationen für Ihren WLAN-Access Point hinzu (SSID, Kanal, etc.).
    - Konfigurieren Sie `dnsmasq` (z. B. in `/etc/dnsmasq.conf`):
        - Fügen Sie die Konfiguration für die IP-Adressvergabe hinzu.
    - Aktivieren sie die Konfigurationen durch, systemctl start hostapd, systemctl start dnsmasq.
3. **IP-Weiterleitung aktivieren:**
    - `sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"`
    - Damit der Raspberry Pi Internetverkehr weiterleiten kann.
4. **NAT (Network Address Translation) einrichten:**
    - `sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE`
    - Ersetzen Sie `wlan0` durch die Schnittstelle, die mit Ihrem Internet verbunden ist.
    - Um die iptables konfiguration dauerhaft zu speichern, muss „iptables-persistent“ installiert werden.

**Schritt 3: Software installieren:**

1. **Aircrack-ng:**
    - `sudo apt install aircrack-ng`
    - Für WLAN-Audits und das Erfassen von WLAN-Paketen.
2. **Wireshark:**
    - `sudo apt install wireshark`
    - Für die Netzwerkanalyse.
3. **Bettercap:**
    - Bettercap ist ein sehr umfangreiches Tool, und sollte daher mit bedacht eingesetzt werden.
    - Bettercap installation anleitung sind im internet zu finden.
4. **Weitere Tools:**
    - Installieren Sie weitere Tools nach Bedarf (z. B. Kismet, Ettercap).

**Schritt 4: Konfiguration und Automatisierung:**

1. **Skripte erstellen:**
    - Erstellen Sie Skripte, um die Konfiguration und den Start der benötigten Dienste zu automatisieren.
2. **Weboberfläche (optional):**
    - Installieren Sie einen Webserver (z. B. Apache oder Nginx) und erstellen Sie eine Webanwendung, um die Konfiguration und Überwachung zu erleichtern.
3. **Regelmäßige Updates:**
    - Führen sie regelmäßige System updates durch (sudo apt update && sudo apt upgrade).

**Wichtige Hinweise:**

- Die Konfiguration eines sicheren WLAN-Access Points erfordert ein tiefes Verständnis von Netzwerksicherheit.
- Verwenden Sie starke Passwörter und aktivieren Sie die Verschlüsselung.
- Achten Sie auf die Einhaltung der geltenden Gesetze und Vorschriften.

------



**Weboberfläche einrichten (Apache & PHP):**

**1. Installation von Apache und PHP:**

- **Apache installieren:**
    - Öffnen Sie ein Terminal auf Ihrem Raspberry Pi.
    - Führen Sie die folgenden Befehle aus, um Apache zu installieren:
        - `sudo apt update`
        - `sudo apt install apache2`
    - Starten und aktivieren Sie den Apache-Webserver:
        - `sudo systemctl start apache2`
        - `sudo systemctl enable apache2`
    - Überprüfen Sie, ob Apache funktioniert, indem Sie die IP-Adresse Ihres Raspberry Pi in einem Webbrowser eingeben. Sie sollten die Apache-Standardseite sehen.
- **PHP installieren:**
    - Führen Sie die folgenden Befehle aus, um PHP und die Apache-PHP-Integration zu installieren:
        - `sudo apt install php libapache2-mod-php`
    - Starten Sie Apache neu, um die PHP-Module zu laden:
        - `sudo systemctl restart apache2`

**2. Erstellen der Webanwendung:**

- **Webverzeichnis:**
    - Das Standard-Webverzeichnis von Apache ist `/var/www/html/`. Hier werden Ihre Webdateien gespeichert.
- **PHP-Datei erstellen (index.php):**
    - Erstellen Sie eine Datei namens `index.php` im Webverzeichnis:
        - `sudo nano /var/www/html/index.php`
    - Fügen Sie den folgenden Beispielcode ein:

PHP

```
    <!DOCTYPE html>
    <html>
    <head>
    <title>WiFi Pineapple-Steuerung</title>
    </head>
    <body>
    <h1>WiFi Pineapple-Steuerung</h1>
    <p><a href="start_ap.php">Access Point starten</a></p>
    <p><a href="stop_ap.php">Access Point stoppen</a></p>
    </body>
    </html>
```

- **PHP-Skripte erstellen (start_ap.php, stop_ap.php):**
    - Erstellen Sie die Dateien `start_ap.php` und `stop_ap.php` im selben Verzeichnis:
        - `sudo nano /var/www/html/start_ap.php`
        - `sudo nano /var/www/html/stop_ap.php`
    - Fügen Sie den folgenden Beispielcode in `start_ap.php` ein:

PHP

```
    <?php
    echo "Access Point wurde gestartet.";
    shell_exec("sudo /usr/local/bin/start_ap.sh");
    ?>
```

```
* Fügen sie den folgenden Beispielcode in „stop\_ap.php“ ein. Bitte beachten Sie, das sie ein Script erstellen müssen das die AP Funktion wieder abschaltet, da dies sehr von der erstellten Konfiguration abhängt, kann hier kein sinnvoller Beispielcode hinterlegt werden.
```

PHP

```
    <?php
    echo "Access Point wurde gestoppt.";
    shell_exec("sudo /usr/local/bin/stop_ap.sh");
    ?>
```

- **Wichtig:**
    - Die Verwendung von `shell_exec()` mit `sudo` in Webanwendungen birgt erhebliche Sicherheitsrisiken. Stellen Sie sicher, dass Sie alle Sicherheitsmaßnahmen ergreifen, um unbefugten Zugriff zu verhindern.

**3. Sicherheitsmaßnahmen:**

- **Beschränken Sie den Zugriff:**
    - Konfigurieren Sie die Apache-Firewall (z. B. mit `ufw`), um den Zugriff auf die Weboberfläche zu beschränken.
    - Verwenden Sie `.htaccess`-Dateien, um die Verzeichnisse zu schützen.
- **Starke Passwörter:**
    - Verwenden Sie starke Passwörter für alle Benutzerkonten.
- **Sichere Authentifizierung:**
    - Implementieren Sie eine sichere Authentifizierungsmethode (z. B. HTTP-Authentifizierung oder eine benutzerdefinierte Anmeldeseite).
- **Code-Injection verhindern:**
    - stellen sie sicher, dass ihre Webanwendung, vor Code Injection geschützt ist.

**4. Zusätzliche Funktionen:**

- **Überwachung:**
    - Fügen Sie Funktionen hinzu, um den Status des WLAN-Access Points, verbundene Geräte und andere relevante Informationen anzuzeigen.
- **Konfiguration:**
    - Erstellen Sie eine Benutzeroberfläche, um die `hostapd`- und `dnsmasq`-Konfigurationen anzupassen.
- **Protokollierung:**
    - Implementieren Sie eine Protokollierungsfunktion, um Ereignisse und Aktivitäten aufzuzeichnen.

**Wichtige Hinweise:**

- Testen Sie die Weboberfläche gründlich in einer isolierten Umgebung, bevor Sie sie im Produktiveinsatz verwenden.
- Achten Sie auf die Sicherheit Ihrer Webanwendung, insbesondere wenn Sie Root-Befehle ausführen.
- Passen Sie die Weboberfläche an Ihre spezifischen Bedürfnisse und Anforderungen an.
- Es ist immer empfehlenswert sich in das Thema Webserver sicherheit ein zuarbeiten, bevor eine solche Anwendung erstellt wird.



----------------------------------------------------------


**1. Skripte zur Automatisierung:**

**a) Startskript für hostapd und dnsmasq:**

- **Zweck:** Dieses Skript startet `hostapd` und `dnsmasq` automatisch nach dem Systemstart.
- **Schritte:**
    1. **Erstellen Sie ein Skript:**
        - Öffnen Sie einen Texteditor (z. B. `nano`) und erstellen Sie eine Datei namens `start_ap.sh`:
            - `sudo nano /usr/local/bin/start_ap.sh`
        - Fügen Sie folgenden Inhalt hinzu:

Bash

```
#!/bin/bash
sudo systemctl start hostapd
sudo systemctl start dnsmasq
sudo sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
```

- Ersetzen sie „wlan0“ durch ihren tatsächlichen Wlan adapter. 2. **Skript ausführbar machen:** * `sudo chmod +x /usr/local/bin/start_ap.sh` 3. **Skript beim Systemstart ausführen:** * Fügen Sie einen Eintrag in `/etc/rc.local` hinzu (vor `exit 0`): * `sudo nano /etc/rc.local` * Fügen Sie folgende Zeile hinzu: * `/usr/local/bin/start_ap.sh` 4. Nun wird das erstellte Script, bei jedem Systemstart automatisch ausgeführt.

**b) Skript zur Konfiguration von iptables:**

- **Zweck:** Dieses Skript konfiguriert `iptables` automatisch nach dem Systemstart.
- **Schritte:**
    1. **Installieren Sie `iptables-persistent`:**
        - `sudo apt install iptables-persistent`
        - Befolgen Sie die Anweisungen, um die aktuelle `iptables`-Konfiguration zu speichern.
    2. Nun werden die Iptables Regeln bei jedem Systemstart geladen.

**2. Weboberfläche (optional):**

**a) Installation eines Webservers (Apache):**

- **Schritte:**
    1. **Apache installieren:**
        - `sudo apt update`
        - `sudo apt install apache2`
    2. **Apache starten und aktivieren:**
        - `sudo systemctl start apache2`
        - `sudo systemctl enable apache2`

**b) Erstellen einer einfachen Webanwendung (PHP):**

- **Schritte:**
    1. **PHP installieren:**
        - `sudo apt install php libapache2-mod-php`
    2. **Eine PHP-Datei erstellen:**
        - Erstellen Sie eine Datei namens `index.php` im Apache-Webverzeichnis (`/var/www/html/`):
            - `sudo nano /var/www/html/index.php`
        - Fügen Sie folgenden Beispielcode hinzu:

PHP

```
    <?php
    echo "<h1>WiFi Pineapple-Steuerung</h1>";
    echo "<p><a href='start_ap.php'>Access Point starten</a></p>";
    echo "<p><a href='stop_ap.php'>Access Point stoppen</a></p>";
    ?>
```

- **Erstellen von PHP Skripten zum starten und stoppen.**
    - Um die Befehle auszuführen, müssen PHP Skripte erstellt werden, diese müssen im selben Ordner liegen wie die „index.php“ Datei.
    - Die Skripte benötigen root rechte um die Systembefehle auszuführen. Hier sollte sehr vorsichtig vorgegangen werden, um keine Sicherheitslücken zu reißen.
    - Um Root befehle auszuführen kann „sudo“ in Verbindung mit „shell_exec()“ verwendet werden.
    - Beispiel „start_ap.php“:

PHP

```
    <?php
    echo "Access Point wurde gestartet";
    shell_exec("sudo /usr/local/bin/start_ap.sh");
    ?>
```

- **Sicherheitsmaßnahmen:**
    - Beschränken Sie den Zugriff auf die Weboberfläche durch Konfiguration der Apache-Firewall.
    - Verwenden Sie starke Passwörter und sichere Authentifizierungsmethoden.
    - Seien sie sehr vorsichtig mit der ausführung von Root befehlen innerhalb einer Webanwendung.

**Wichtige Hinweise:**

- Testen Sie die Skripte gründlich, bevor Sie sie im Produktiveinsatz verwenden.
- Achten Sie auf die Sicherheit der Weboberfläche, insbesondere wenn Sie Root-Befehle ausführen.
- Passen Sie die Skripte und die Weboberfläche an Ihre spezifischen Bedürfnisse an.





------------------------------------------------------------
**1. Dedizierter Netzwerk-Sniffer/Packet Analyzer:**

- **Zweck:**
    - Richten Sie den zweiten Raspberry Pi als dedizierten Netzwerk-Sniffer ein, um den Netzwerkverkehr zu überwachen und zu analysieren.
    - Dies ermöglicht eine kontinuierliche Überwachung, ohne die Ressourcen Ihres Haupt-Pentesting-Laptops zu belasten.
- **Schritte:**
    1. **Raspberry Pi OS Lite installieren:**
        - Um Ressourcen zu sparen, installieren Sie Raspberry Pi OS Lite (ohne Desktop-Umgebung) auf der Micro-SD-Karte.
    2. **Netzwerk-Sniffer-Software installieren:**
        - Installieren Sie Wireshark, tcpdump oder andere Netzwerk-Sniffer-Tools:
            - `sudo apt update`
            - `sudo apt install wireshark tcpdump`
        - Um Wireshark ohne Grafische oberfläche zu verwenden, kann Tshark verwendet werden.
    3. **WLAN-Adapter konfigurieren:**
        - Schließen Sie einen WLAN-Adapter mit Monitor-Modus an den Raspberry Pi an.
        - Konfigurieren Sie den Adapter, um den Netzwerkverkehr zu erfassen.
    4. **Automatisierung:**
        - Erstellen Sie Skripte, um die Netzwerk-Sniffer-Software automatisch zu starten und die erfassten Daten zu speichern.
        - Die Erfassung von Daten kann nach bestimmten Filtern erfolgen.
    5. **Fernzugriff:**
        - Konfigurieren Sie SSH, um per Fernzugriff auf den Raspberry Pi zuzugreifen und die erfassten Daten zu analysieren.

**2. VPN-Gateway/Proxy:**

- **Zweck:**
    - Richten Sie den Raspberry Pi als VPN-Gateway oder Proxy ein, um Ihren Netzwerkverkehr zu verschlüsseln und zu anonymisieren.
    - Dies ist besonders nützlich bei Pentesting in öffentlichen Netzwerken.
- **Schritte:**
    1. **VPN-Software installieren:**
        - Installieren Sie OpenVPN, WireGuard oder andere VPN-Software.
    2. **VPN-Konfiguration:**
        - Konfigurieren Sie den Raspberry Pi als VPN-Server oder -Client.
    3. **Proxy-Server einrichten (optional):**
        - Installieren Sie Squid oder einen anderen Proxy-Server.
    4. **Netzwerk-Konfiguration:**
        - Konfigurieren Sie die IP-Weiterleitung und NAT, um den VPN-Verkehr weiterzuleiten.
    5. **Automatisierung:**
        - Richten sie Automatische Verbindungen zum VPN Anbieter ein.

**3. Dedizierte Angriffsplattform:**

- **Zweck:**
    - Nutzen Sie den Raspberry Pi als dedizierte Angriffsplattform, um Angriffe zu starten, ohne Ihren Haupt-Pentesting-Laptop zu belasten.
- **Schritte:**
    1. **Kali Linux installieren (optional):**
        - Installieren Sie Kali Linux auf der Micro-SD-Karte, um eine umfassende Sammlung von Pentesting-Tools zu erhalten.
    2. **Angriffswerkzeuge installieren:**
        - Installieren Sie die benötigten Angriffswerkzeuge, z. B. Metasploit, Nmap, etc.
    3. **Fernzugriff:**
        - Konfigurieren Sie SSH oder VNC, um per Fernzugriff auf den Raspberry Pi zuzugreifen.
    4. **Isolation:**
        - Platzieren sie den Pi in einem Separierten Netzwerk um das Hauptnetzwerk vor fehlkonfigurationen zu schützen.

**Zusätzliche Überlegungen:**

- **Stromversorgung:**
    - Stellen Sie sicher, dass Sie eine zuverlässige Stromversorgung für beide Raspberry Pis haben.
- **Netzwerkverbindung:**
    - Verwenden Sie Ethernet-Kabel, um eine stabile und schnelle Netzwerkverbindung zu gewährleisten.
- **Sicherheit:**
    - Halten Sie Ihre Software und Systeme auf dem neuesten Stand, um Sicherheitslücken zu vermeiden.
    - nutzen sie lange und sichere passwörter.


-------------------------------------------------------------

Schritt-für-Schritt-Anleitung, wie Sie einen Raspberry Pi Zero (W) als tragbaren Netzwerk-Sniffer einrichten können:

**Vorbereitung:**

- **Hardware:**
    - Raspberry Pi Zero W
    - Micro-SD-Karte (mindestens 8 GB)
    - Micro-USB-Netzteil
    - Optional: USB-OTG-Adapter (falls Sie eine Tastatur oder Maus anschließen möchten)
- **Software:**
    - Raspberry Pi OS Lite (für eine schlanke Installation)
    - tcpdump oder Tshark (für die Paketerfassung)

**Schritt 1: Raspberry Pi OS Lite installieren:**

1. **Raspberry Pi Imager herunterladen:**
    - Besuchen Sie die offizielle Raspberry Pi-Website und laden Sie den Raspberry Pi Imager herunter.
2. **Raspberry Pi OS Lite installieren:**
    - Führen Sie den Raspberry Pi Imager aus.
    - Wählen Sie "Raspberry Pi OS (other)" und dann "Raspberry Pi OS Lite (64-bit)" aus.
    - Wählen Sie Ihre Micro-SD-Karte als Ziel.
    - Klicken Sie auf "Schreiben", um das Betriebssystem auf die SD-Karte zu installieren.
3. **SSH aktivieren (für Headless-Betrieb):**
    - Erstellen Sie nach dem Schreiben des Images eine leere Datei namens "ssh" im Boot-Verzeichnis der Micro-SD-Karte.
4. **WLAN konfigurieren (optional):**
    - Erstellen Sie im Boot-Verzeichnis eine Datei namens "wpa_supplicant.conf" und fügen Sie Ihre WLAN-Konfigurationsdaten hinzu:

```
    country=DE
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
    ssid="Ihr_WLAN_SSID"
    psk="Ihr_WLAN_Passwort"
    }
```

**Schritt 2: Raspberry Pi Zero W starten und verbinden:**

1. **Micro-SD-Karte einlegen und starten:**
    - Legen Sie die Micro-SD-Karte in den Raspberry Pi Zero W ein und schließen Sie das Netzteil an.
2. **Mit dem Netzwerk verbinden:**
    - Wenn Sie die WLAN-Konfiguration vorgenommen haben, sollte sich der Raspberry Pi Zero W automatisch mit Ihrem WLAN verbinden.
    - Andernfalls verbinden Sie ihn über ein USB-Ethernet-Adapter.
3. **SSH-Verbindung herstellen:**
    - Ermitteln Sie die IP-Adresse des Raspberry Pi Zero W (z. B. über Ihren Router).
    - Öffnen Sie ein Terminal und stellen Sie eine SSH-Verbindung her:
        - `ssh pi@IP_Adresse_des_Pi`
        - Das Standardpasswort ist "raspberry".

**Schritt 3: Netzwerk-Sniffer-Software installieren:**

1. **System aktualisieren:**
    - `sudo apt update && sudo apt upgrade -y`
2. **tcpdump oder Tshark installieren:**
    - Für tcpdump: `sudo apt install tcpdump`
    - Für Tshark (Wireshark-Befehlszeilenversion): `sudo apt install tshark`

**Schritt 4: Pakete erfassen:**

1. **Paketerfassung starten (tcpdump):**
    - Um den gesamten Netzwerkverkehr zu erfassen:
        - `sudo tcpdump -i any -w capture.pcap`
    - Um den Verkehr auf einer bestimmten Schnittstelle zu erfassen (z. B. wlan0):
        - `sudo tcpdump -i wlan0 -w capture.pcap`
    - Um den Verkehr nach Filtern zu erfassen (z.B. nur TCP port 80):
        - `sudo tcpdump -i any tcp port 80 -w capture.pcap`
    - Die Option "-w capture.pcap" speichert die erfassten Pakete in einer Datei.
2. **Paketerfassung starten (Tshark):**
    - Um den gesamten Netzwerkverkehr zu erfassen:
        - `sudo tshark -i any -w capture.pcap`
    - Um den Verkehr nach Filtern zu erfassen:
        - `sudo tshark -i any -f "tcp port 80" -w capture.pcap`
3. **Erfasste Daten analysieren:**
    - Laden Sie die "capture.pcap"-Datei auf Ihren Haupt-Pentesting-Laptop herunter und analysieren Sie sie mit Wireshark.

**Schritt 5: Automatisierung (optional):**

1. **Skript erstellen:**
    - Erstellen Sie ein Skript, um die Paketerfassung automatisch zu starten, wenn der Raspberry Pi Zero W startet.
    - Verwenden Sie systemd, um das Skript als Dienst auszuführen.
2. **Fernzugriff konfigurieren:**
    - Konfigurieren Sie SSH, um den Raspberry Pi Zero W per Fernzugriff zu verwalten.
    - Verwenden sie Programme wie „scp“ um die pcap dateien herunter zu laden.

**Wichtige Hinweise:**

- Der Raspberry Pi Zero W hat begrenzte Ressourcen. Achten Sie darauf, die Paketerfassung zu stoppen, wenn sie nicht benötigt wird.
- Die erfassten Daten können vertrauliche Informationen enthalten. Behandeln Sie sie mit Vorsicht.
- Halten Sie sich an die Gesetzgebung.