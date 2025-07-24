

**Was ist OpenWrt?**

OpenWrt ist ein **Linux-basiertes Betriebssystem**, das als **Ersatz-Firmware** für viele handelsübliche Router dient. Im Gegensatz zu den oft eingeschränkten und proprietären Firmware-Versionen der Router-Hersteller bietet OpenWrt **volle Open-Source-Transparenz, umfangreiche Anpassungsmöglichkeiten und eine riesige Community**.

**Warum OpenWrt verwenden?**

- **Mehr Kontrolle:** Voller Zugriff auf das Betriebssystem und die Router-Konfiguration.
- **Erweiterte Funktionen:** Unterstützung für VPN-Server/Clients, Ad-Blocking, QoS (Quality of Service), erweiterte Netzwerkkonfiguration und vieles mehr.
- **Aktuelle Software:** Oft schnellere Bereitstellung von Sicherheitsupdates und neuen Funktionen als durch die Router-Hersteller.
- **Hardware-Flexibilität:** Unterstützt eine breite Palette von Routern und erweitert deren Lebensdauer.
- **Community-Support:** Große und aktive Community für Hilfe, Anleitungen und Weiterentwicklung.

**Überblick über die Einrichtung eines OpenWrt Routers**

Die Einrichtung eines OpenWrt Routers lässt sich grob in folgende Schritte unterteilen:

1. **Kompatibilitätsprüfung und Firmware-Download:** Sicherstellen, dass Ihr Router mit OpenWrt kompatibel ist und die passende Firmware-Datei herunterladen.
2. **OpenWrt Flashen (Installation):** Die Original-Firmware des Routers durch OpenWrt ersetzen. Dies kann je nach Router-Modell variieren.
3. **Erstkonfiguration (LuCI Webinterface):** Grundlegende Einstellungen über die grafische Benutzeroberfläche LuCI vornehmen.
4. **Grundlegende Netzwerkeinstellungen:** Internetverbindung (WAN), lokales Netzwerk (LAN) und WLAN konfigurieren.
5. **Sicherheitseinstellungen:** Wichtigste Sicherheitseinstellungen wie Passwortänderung und Firewall überprüfen.
6. **Erweiterte Konfiguration (LuCI und SSH):** Optionale und fortgeschrittene Einstellungen über das Webinterface oder die Kommandozeile (SSH) anpassen.
7. **Optionale Funktionen installieren:** Zusätzliche Softwarepakete für erweiterte Funktionen über den Paketmanager `opkg` installieren.

**Schritt-für-Schritt Anleitung zur Einrichtung eines OpenWrt Routers**

Hier ist eine detaillierte Anleitung, die Sie durch die einzelnen Schritte führt. Diese Anleitung ist allgemein gehalten, da der genaue Ablauf je nach Router-Modell und der verwendeten OpenWrt Version variieren kann. **Es ist extrem wichtig, die gerätespezifischen Anleitungen im OpenWrt Wiki (siehe "Wichtige Hinweise und Tipps" unten) zu Rate zu ziehen!**

**1. Kompatibilitätsprüfung und Firmware-Download**

- **Router-Kompatibilität prüfen:** Besuchen Sie die offizielle OpenWrt Webseite ([https://openwrt.org/
    
    ](https://www.google.com/url?sa=E&source=gmail&q=https://openwrt.org/)) und gehen Sie zum Bereich "Supported Devices" oder suchen Sie direkt nach Ihrem Router-Modell in der Suchleiste der Seite.
    - **Wichtig:** Stellen Sie sicher, dass Ihr _genaues_ Router-Modell (inklusive Hardware-Version, falls angegeben) in der Liste aufgeführt ist. Eine falsche Firmware kann Ihren Router unbrauchbar machen!
- **Firmware-Image herunterladen:** Sobald Sie die Kompatibilität bestätigt haben, suchen Sie die passende Firmware-Datei für Ihr Router-Modell im OpenWrt Wiki. In der Regel finden Sie dort Links zu "Factory" und "Sysupgrade" Images.
    - **"Factory" Image:** Wird für die **Erstinstallation** von OpenWrt verwendet, um die Original-Firmware zu ersetzen. Oft im Format `.bin` oder `.trx`.
    - **"Sysupgrade" Image:** Wird für **Updates** von einer bereits installierten OpenWrt Version verwendet. Oft im Format `.tar.gz`.
    - Für die Erstinstallation benötigen Sie in der Regel das **"Factory" Image**.

**2. OpenWrt Flashen (Installation)**

**Achtung: Dieser Schritt ist kritisch und kann bei Fehlern Ihren Router beschädigen! Gehen Sie äußerst sorgfältig vor und lesen Sie die gerätespezifischen Anleitungen im OpenWrt Wiki genau durch!**

Die Methode zum Flashen von OpenWrt ist **stark vom Router-Modell abhängig**. Es gibt keine universelle Methode. Häufige Methoden sind:

- **Webinterface des Original-Routers:
    
    [![Bildmotiv: Router Firmware Update page (generic example)](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQ1HWYhoQcmtmFOAjTE_etzCQ_YzWr2R1BcKpqptd05qVR_q_QZHKWZGTO9-Pyw)Wird in einem neuen Fenster geöffnet](https://www.lifewire.com/how-to-upgrade-your-wireless-routers-firmware-2487671)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcTbBzL2aA3P5GYeW_YdjJLb1tjZAHdtHt_r_TYBKL0zyJ48YzHRi_psLGw14rhgvIGL40Qq3z4M4jUgrZ6Ix8MQBlwiYLf2D65m2A)www.lifewire.com](https://www.lifewire.com/how-to-upgrade-your-wireless-routers-firmware-2487671)
    
    Router Firmware Update page (generic example)
    
    
    
    
    
    **Viele Router erlauben das Firmware-Update über ihr eigenes Webinterface. In manchen Fällen kann man dort das OpenWrt "Factory" Image hochladen und installieren. Dies ist oft die einfachste Methode, wenn sie unterstützt wird.
- **TFTP (Trivial File Transfer Protocol):** Bei einigen Routern muss OpenWrt über TFTP im "Recovery Mode" geflasht werden. Dies ist etwas komplexer und erfordert spezielle Software (TFTP-Client) und das Setzen des Routers in den Recovery-Modus (oft durch Drücken einer Reset-Taste beim Starten). Die genaue Vorgehensweise ist sehr gerätespezifisch.
- **Serielle Konsole (Seriell/UART):** Für fortgeschrittene Benutzer oder in Notfällen kann OpenWrt auch über eine serielle Konsole geflasht werden. Dies erfordert spezielle Hardware (Seriell-zu-USB Adapter) und Kenntnisse über die serielle Kommunikation.

**Generelle Schritte beim Flashen (Beispiel - kann für Ihr Router-Modell abweichen!):**

1. **Router vorbereiten:** Router ausschalten und vom Stromnetz trennen.
2. **Computer vorbereiten:** Verbinden Sie Ihren Computer **per Ethernet-Kabel** mit einem **LAN-Port** des Routers. Konfigurieren Sie Ihre Netzwerkkarte am Computer **statisch** auf eine IP-Adresse im gleichen Subnetz wie der Router im Recovery-Modus (oft 192.168.1.x oder 192.168.0.x). Details finden Sie in der gerätespezifischen Anleitung.
3. **Router in den Recovery-Modus versetzen:** Die genaue Methode, um den Router in den Recovery-Modus zu versetzen, ist **router-spezifisch**. Oft beinhaltet es das Drücken und Halten einer Reset-Taste beim Einschalten des Routers. **Lesen Sie die Anleitung für Ihr Router-Modell genau!**
4. **Firmware übertragen:** Je nach Methode (Webinterface, TFTP, Seriell) übertragen Sie das heruntergeladene OpenWrt "Factory" Image auf den Router. Bei TFTP benötigen Sie einen TFTP-Client und müssen die Datei oft unter einem bestimmten Namen (z.B. `firmware.bin` oder `code.bin`) auf dem TFTP-Server ablegen und den Router im Recovery-Modus starten, um die Übertragung zu initiieren.
5. **Warten:** Warten Sie geduldig, bis der Flash-Vorgang abgeschlossen ist. Unterbrechen Sie den Vorgang auf keinen Fall! Dies kann einige Minuten dauern. Die Status-LEDs des Routers können den Fortschritt anzeigen.
6. **Neustart:** Nach erfolgreichem Flashen sollte der Router neu starten und mit OpenWrt hochfahren.

**3. Erstkonfiguration (LuCI Webinterface)**

- **Computer verbinden:** Stellen Sie sicher, dass Ihr Computer weiterhin **per Ethernet-Kabel** mit dem Router verbunden ist. Konfigurieren Sie Ihre Netzwerkkarte wieder auf **DHCP** (automatische IP-Adressvergabe).
- **Webbrowser öffnen:** Starten Sie einen Webbrowser auf Ihrem Computer.
- **OpenWrt Adresse eingeben:** Geben Sie in die Adresszeile des Browsers `192.168.1.1` ein und drücken Sie Enter. Dies ist die **Standard-IP-Adresse
    
    [![Bildmotiv: Browser address bar with 192.168.1.1](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSYwk35v6Youtost3Rbm440hDD-0wM8uHyUBCnCyJ_Z3OA2QbBGqCFF6OoXDaK)Wird in einem neuen Fenster geöffnet](https://192168101.uno/192-168-1-1/)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQKRl5AH3a4I4h_tK0aHe9CvKLqQN_OeSJTZzamIpg1UiDl6TvXYvJDKxyknJlL3mE-p6mK3lLcaWaZhbwfpdXD-hSMgaofRA)192168101.uno](https://192168101.uno/192-168-1-1/)
    
    Browser address bar with 192.168.1.1
    
    
    
    
    
    **von OpenWrt.
- **LuCI Oberfläche:** Sie sollten nun die **LuCI Webinterface
    
    [![Bildmotiv: OpenWrt LuCI Web Interface](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwflIU--QWky-OvLFP4u2_G4fCpsqZH836IkTv2T6BMvQQzSFIr96fzmv-8Yrj)Wird in einem neuen Fenster geöffnet](https://medium.com/openwrt-iot/openwrt-adding-a-web-interface-4bcdf1279a6f)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcR-luPlDlD1SFs9hRigBPkt8jfeNrQl2lCButRF3S6a8RvvZStncCLDMwsM865Yfv2-I1NEaNUT9CW8qKM2Cq1JYOkgmA)medium.com](https://medium.com/openwrt-iot/openwrt-adding-a-web-interface-4bcdf1279a6f)
    
    OpenWrt LuCI Web Interface
    
    
    
    
    
    **Oberfläche von OpenWrt sehen.
    - **Hinweis:** Bei älteren OpenWrt Versionen oder bestimmten Konfigurationen kann es sein, dass Sie zunächst keine grafische Oberfläche haben und nur eine Kommandozeile per SSH zur Verfügung steht. In diesem Fall müssen Sie LuCI manuell installieren (siehe Abschnitt "Erweiterte Konfiguration").

**4. Grundlegende Netzwerkeinstellungen**

- **Passwort setzen:** **Das erste und wichtigste:** Setzen Sie ein **starkes Passwort** für den `root  [![Bildmotiv: OpenWrt LuCI System Administration page](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQy-Wf7OvomVwH3WokNSTew75FulmdrZspDOy5nqvxvYcOK8lXT50HoUjQ_n44-)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-quick-start/walkthrough_login)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-quick-start/walkthrough_login)  OpenWrt LuCI System Administration page      `-Benutzer! In der LuCI Oberfläche gehen Sie zu "System" -> "Administration" und geben Sie im Feld "Router Password" Ihr neues Passwort ein und bestätigen Sie es.
- **WAN Interface konfigurieren (Internetverbindung):**
    - Gehen Sie zu "Network" -> "Interfaces".
    - Suchen Sie das Interface mit der Bezeichnung "WAN" (oft `eth0.2` oder ähnlich, je nach Router).
    - Klicken Sie auf "Edit".
        
        [![Bildmotiv: OpenWrt LuCI Network Interfaces page](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTKaYozTBelXuWl8EStcVp2WQO61y27f2WQ1hvoAjU_tl8VLb18VI3HCewKDgdI)Wird in einem neuen Fenster geöffnet](https://m2m-tele.com/blog/2021/03/12/openwrt-configuration-users-guide-part-1-how-to-configure-network-2/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcSBkKD2nbd2r5tEO1CLr26ApFdX7bYPi7YPP6a8t5oLyj5t9-c8r5H0CHrvDd2ATDvooaW-Hnt36irzV50GRE_5iLxs22kB)m2m-tele.com](https://m2m-tele.com/blog/2021/03/12/openwrt-configuration-users-guide-part-1-how-to-configure-network-2/)
        
        OpenWrt LuCI Network Interfaces page
        
    - **Protokoll:** Wählen Sie das passende Protokoll für Ihren Internetanschluss:
        - **DHCP Client (Standard für die meisten Kabel- und DSL-Anschlüsse):** Wenn Ihr Router die IP-Adresse automatisch von Ihrem Provider beziehen soll. In den meisten Fällen die richtige Wahl.
        - **PPPoE:** Für DSL-Anschlüsse, bei denen Sie Zugangsdaten (Benutzername und Passwort) von Ihrem Provider benötigen. Geben Sie diese unter "PAP/CHAP Username" und "PAP/CHAP Password" ein.
        - **Static IP:** Wenn Sie eine feste IP-Adresse von Ihrem Provider haben. Geben Sie IP-Adresse, Netzmaske, Gateway und DNS-Server manuell ein.
    - Klicken Sie auf "Save & Apply".
- **WLAN konfigurieren:**
    - Gehen Sie zu "Network" -> "Wireless".
    - Sie sehen in der Regel ein oder mehrere "Generic 802.11bgn" (oder ähnlich) Geräte aufgeführt, die Ihr WLAN-Chip darstellen. Klicken Sie bei dem gewünschten WLAN-Gerät auf "Edit" oder "Enable".
        
        [![Bildmotiv: OpenWrt LuCI Wireless Overview page](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1z6CVkj7cBKNVbaxfH1UcbUg8oDDz-tyR4WvhjRa5I65BAxqSEwvwslbpS0cN)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-quick-start/walkthrough_wifi)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-quick-start/walkthrough_wifi)
        
        OpenWrt LuCI Wireless Overview page
        
    - **Interface Konfiguration:**
        - **ESSID:** Geben Sie einen Namen für Ihr WLAN-Netzwerk ein (SSID, z.B. "MeinHeimnetzwerk").
        - **Mode:** "Access Point" ist der Standardmodus für ein WLAN-Netzwerk.
        - **Channel:** Wählen Sie einen WLAN-Kanal. "Auto" funktioniert meist gut, aber bei Problemen kann es helfen, einen festen Kanal zu wählen.
        - **Encryption:** **Wählen Sie unbedingt eine sichere Verschlüsselungsmethode! "WPA2-PSK" oder "WPA3-SAE" (oder "WPA2/WPA3 Mixed") sind empfehlenswert.** Vermeiden Sie "WEP" oder "keine Verschlüsselung".
        - **Key:** Geben Sie ein **starkes WLAN-Passwort** (WLAN-Schlüssel) ein.
    - Klicken Sie auf "Save & Apply". Ihr WLAN-Netzwerk sollte nun aktiv sein. Verbinden Sie Ihre WLAN-Geräte.

**5. Sicherheitseinstellungen überprüfen**

- **Firewall:
    
    [![Bildmotiv: OpenWrt LuCI Firewall Settings page](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRefpAmt-qp7-GClTkqM2ObCqoZQR2BOtUQ3NelbvNO40Nk4tGybWWV51goBpFQ)Wird in einem neuen Fenster geöffnet](https://www.reddit.com/r/openwrt/comments/157g0ps/explain_luci_firewall_settings_page/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcQDsPs2pPiHN60JT0C5gSmR6KHemKpDPI1y39DsENKpXAWFU3erhAZR-PJSjvsHP1h8wtyE1tPnfR9SJQ_ptDxDc_3GRiAuyfM)www.reddit.com](https://www.reddit.com/r/openwrt/comments/157g0ps/explain_luci_firewall_settings_page/)
    
    OpenWrt LuCI Firewall Settings page
    
    
    
    
    
    **OpenWrt verfügt über eine vorkonfigurierte Firewall, die in der Regel gut funktioniert. Sie können die Firewall-Einstellungen unter "Network" -> "Firewall" überprüfen und anpassen.
    - **Zonen:** OpenWrt verwendet Zonen (z.B. "wan", "lan", "guest") um Netzwerkbereiche zu definieren und Regeln anzuwenden. Die Standardzonen sind in der Regel sinnvoll vorkonfiguriert (WAN-Zone blockiert eingehende Verbindungen, LAN-Zone erlaubt Verbindungen innerhalb des LANs).
    - **Portweiterleitungen (Port Forwards):** Wenn Sie Dienste in Ihrem lokalen Netzwerk aus dem Internet erreichbar machen möchten (z.B. Webserver, SSH-Server), müssen Sie Portweiterleitungen einrichten. Seien Sie hier vorsichtig und leiten Sie nur Ports weiter, die Sie wirklich benötigen.

**6. Erweiterte Konfiguration (LuCI und SSH)**

- **LuCI für allgemeine Einstellungen:** Für die meisten grundlegenden und fortgeschrittenen Konfigurationen ist die LuCI Webinterface ausreichend. Erkunden Sie die verschiedenen Menüpunkte (Network, System, Services, etc.).
- **SSH für Kommandozeile:** OpenWrt ist Linux-basiert. Für fortgeschrittenere Konfigurationen oder die Installation von Softwarepaketen ist der Zugriff über die Kommandozeile (SSH) oft notwendig und sehr mächtig.
    - **SSH aktivieren (falls nicht aktiv):** In der LuCI Oberfläche unter "System" -> "Administration" -> "SSH Access" stellen Sie sicher, dass "Password authentication" und/oder "Permit root login" aktiviert sind (für die erste Einrichtung). **Achtung:** Für den produktiven Einsatz ist es sicherer, die Passwort-Authentifizierung zu deaktivieren und nur Public-Key-Authentifizierung zu verwenden.
    - **SSH Client verwenden:** Verwenden Sie einen SSH-Client (z.B. PuTTY für Windows, Terminal unter Linux/macOS). Verbinden Sie sich mit der IP-Adresse Ihres Routers (Standard: `192.168.1.1`) und dem Benutzer `root  [![Bildmotiv: PuTTY SSH client connecting to OpenWrt](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTnFLADXq9bM9k3rvGowxIs4POm-kb63nBP1OpBNH318lIa2NTTD52bgNmnhsD_)Wird in einem neuen Fenster geöffnet](https://medium.com/openwrt-iot/openwrt-how-to-set-up-dropbear-public-key-authentication-d206bbbc8ca7)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcR-luPlDlD1SFs9hRigBPkt8jfeNrQl2lCButRF3S6a8RvvZStncCLDMwsM865Yfv2-I1NEaNUT9CW8qKM2Cq1JYOkgmA)medium.com](https://medium.com/openwrt-iot/openwrt-how-to-set-up-dropbear-public-key-authentication-d206bbbc8ca7)  PuTTY SSH client connecting to OpenWrt      `und Ihrem in LuCI gesetzten Passwort.
    - **Paketmanager `opkg`:** Über die SSH-Kommandozeile können Sie mit dem Paketmanager `opkg` Software installieren, aktualisieren und deinstallieren. Beispiele:
        - `opkg update` - Paketlisten aktualisieren.
        - `opkg install <paketname>` - Paket installieren (z.B. `opkg install luci-app-sqm` für SQM QoS).
        - `opkg remove <paketname>` - Paket deinstallieren.
    - **Konfigurationssystem `uci`:** OpenWrt verwendet das Unified Configuration Interface (UCI). Über die Kommandozeile können Sie Konfigurationsdateien direkt bearbeiten oder UCI-Kommandos verwenden, um Einstellungen zu ändern. Dies ist für fortgeschrittene Konfigurationen oft effizienter als die LuCI Oberfläche. Beispiel:
        - `uci set wireless.@wifi-iface[0].ssid='MeinNeuerWLANName'` - WLAN-Namen ändern.
        - `uci commit wireless` - Änderungen speichern.
        - `/etc/init.d/network reload` - Netzwerk neu starten, um Änderungen zu aktivieren.

**7. Optionale Funktionen installieren**

OpenWrt bietet eine riesige Auswahl an optionalen Funktionen, die Sie über den Paketmanager `opkg` installieren können. Einige beliebte Beispiele:

- **VPN Server/Client:** Pakete wie `openvpn-openssl`, `strongswan`, `wireguard` ermöglichen das Einrichten von VPN-Servern oder -Clients.
- **AdBlock:** Pakete wie `adblock` blockieren Werbung auf Netzwerkebene.
- **SQM (Smart Queue Management):** Pakete wie `sqm-scripts`, `luci-app-sqm` verbessern die Netzwerk-Performance, insbesondere bei überlasteten Verbindungen (Pufferbloating).
- **Datei-Sharing (NAS):** Pakete wie `samba36-server`, `nfs-kernel-server` ermöglichen das Freigeben von Dateien über USB-Festplatten, die am Router angeschlossen sind.
- **Dynamic DNS (DDNS):** Pakete wie `ddns-scripts` ermöglichen die Erreichbarkeit Ihres Heimnetzwerks über einen dynamischen DNS-Dienst, auch wenn Ihre öffentliche IP-Adresse wechselt.
- **und viele mehr...** Durchstöbern Sie die OpenWrt Paketlisten ([https://openwrt.org/packages/table/packages](https://www.google.com/search?q=https://openwrt.org/packages/table/packages)) oder suchen Sie in der LuCI Oberfläche unter "System" -> "Software".

**8. Troubleshooting**

- **Kein Zugriff auf die LuCI Oberfläche (192.168.1.1 funktioniert nicht):**
    - Überprüfen Sie die Ethernet-Kabelverbindung zwischen Computer und Router.
    - Stellen Sie sicher, dass der Router eingeschaltet ist und die Status-LEDs leuchten.
    - Überprüfen Sie die Netzwerkeinstellungen Ihres Computers (Netzwerkkarte auf DHCP gestellt?).
    - Versuchen Sie, den Router und Ihren Computer neu zu starten.
    - Setzen Sie den Router auf Werkseinstellungen zurück (siehe Router-Dokumentation oder OpenWrt Wiki für Ihr Modell).
- **Keine Internetverbindung nach Einrichtung:**
    - Überprüfen Sie die WAN-Interface Konfiguration (richtiges Protokoll, korrekte Zugangsdaten?).
    - Überprüfen Sie die Kabelverbindung zum Internetanschluss.
    - Starten Sie den Router und Ihr Modem/ONT neu.
    - Überprüfen Sie den Verbindungsstatus in der LuCI Oberfläche (Network -> Interfaces -> WAN). Werden Fehlermeldungen angezeigt?
    - Ist Ihr Internetanschluss aktiv und funktioniert grundsätzlich (z.B. mit dem Original-Router)?
- **WLAN-Verbindungsprobleme:**
    - Überprüfen Sie, ob das WLAN-Interface in LuCI aktiviert ist (Network -> Wireless).
    - Stellen Sie sicher, dass Sie den korrekten WLAN-Namen (SSID) auswählen und das richtige WLAN-Passwort eingeben.
    - Prüfen Sie die WLAN-Signalstärke und mögliche Störquellen.
    - Wechseln Sie den WLAN-Kanal in den WLAN-Einstellungen (Channel).

**9. Wichtige Hinweise und Tipps**

- **OpenWrt Wiki ist Ihre beste Ressource:** Das OpenWrt Wiki ([https://openwrt.org/](https://www.google.com/url?sa=E&source=gmail&q=https://openwrt.org/)) ist die zentrale Anlaufstelle für Dokumentation, Anleitungen und gerätespezifische Informationen. **Nutzen Sie es intensiv!**
- **Gerätespezifische Anleitungen:** Suchen Sie im Wiki nach Seiten speziell für Ihr Router-Modell ("Table of Hardware", "Router Model Installation Guide"). Dort finden Sie detaillierte Anleitungen zum Flashen, spezielle Konfigurationstipps und bekannte Probleme.
- **Backup der Konfiguration:** Sichern Sie Ihre OpenWrt Konfiguration regelmäßig (LuCI -> System -> Backup / Flash Firmware -> Backup). So können Sie im Fehlerfall schnell zu einer funktionierenden Konfiguration zurückkehren.
- **Vorsicht bei Kommandozeilen-Änderungen:** Seien Sie vorsichtig bei Änderungen über die Kommandozeile, besonders wenn Sie nicht mit Linux-Systemen vertraut sind. Falsche Befehle können das System instabil machen.
- **Community-Foren:** Bei Problemen oder Fragen hilft die OpenWrt Community in Foren und Mailinglisten oft sehr schnell und kompetent weiter.
- **Firmware aktuell halten:** Installieren Sie regelmäßig Updates für OpenWrt, um von Sicherheitsfixes und neuen Funktionen zu profitieren. Dies können Sie über LuCI ("System" -> "Software") oder die Kommandozeile (`opkg update && opkg upgrade`) tun.


Wichtige einstellungen  



**1. Sicherheit – Grundstein für ein sicheres Netzwerk**

- **Root-Passwort festlegen (Ändern des Standardpassworts):**
    
    - **Was ist das?**: Nach der Erstinstallation von OpenWrt ist kein Root-Passwort gesetzt. Dies ist ein **gravierendes Sicherheitsrisiko**! Das Root-Passwort schützt den administrativen Zugang zu Ihrem Router (Webinterface LuCI und SSH-Zugang).
    - **Warum wichtig?**: Ohne Root-Passwort ist Ihr Router **für jeden im Netzwerk und potenziell aus dem Internet offen wie ein Scheunentor**. Jeder könnte sich Zugriff verschaffen, Einstellungen ändern, Schadsoftware installieren und Ihr Netzwerk kompromittieren.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"System" -> "Administration"**. Im Bereich "Router-Passwort" geben Sie ein **starkes, sicheres Passwort** in die Felder "Passwort" und "Bestätigung" ein. Klicken Sie auf **"Speichern & Anwenden"**.
            
            [![Bildmotiv: OpenWrt LuCI System Administration page](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSrTghfjA6cSjNODCuuolo2IonSL88XcZevnzQLMrrsRHHuheSWZ_QYQRiYkdmT)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-quick-start/walkthrough_login)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-quick-start/walkthrough_login)
            
            OpenWrt LuCI System Administration page
            
        - **SSH-Kommandozeile:** Verbinden Sie sich per SSH mit Ihrem Router (z.B. mit PuTTY oder dem Terminal). Geben Sie den Befehl `passwd` ein und folgen Sie den Anweisungen, um ein neues Passwort zu setzen.
- **Firewall-Einstellungen überprüfen und verstehen:**
    
    - **Was ist das?**: Die OpenWrt Firewall (basierend auf `iptables` oder `nftables`) schützt Ihr Netzwerk vor unerwünschten Zugriffen von außen (aus dem Internet) und steuert den Datenverkehr innerhalb Ihres Netzwerks. OpenWrt kommt mit sinnvollen Standardeinstellungen.
    - **Warum wichtig?**: Eine korrekt konfigurierte Firewall ist essenziell, um Ihr Netzwerk und Ihre Geräte vor Angriffen aus dem Internet zu schützen. Die Standardeinstellungen von OpenWrt sind gut, aber es ist wichtig, sie zu verstehen und ggf. anzupassen.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"Netzwerk" -> "Firewall"**.
            
            - **Zonen:** OpenWrt verwendet Zonen (z.B. `wan`, `lan`). **"WAN"** (Wide Area Network) Zone ist das Interface zum Internet. **"LAN"** (Local Area Network) ist Ihr lokales Netzwerk. Die Standardeinstellungen sind in der Regel:
                - **WAN -> Reject:** Eingehende Verbindungen von WAN nach Router werden standardmäßig abgelehnt. Dies ist wichtig!
                - **Forwarding:** "Forwarding" regelt, was zwischen den Zonen erlaubt ist. Standardmäßig ist `lan -> wan` **akzeptiert**, `wan -> lan` **abgelehnt**. Dies bedeutet, dass Geräte im LAN ins Internet kommunizieren können, aber nicht umgekehrt (außer für etablierte Verbindungen).
            - **Portweiterleitungen (Port Forwards):** Nur einrichten, wenn Sie Dienste (z.B. Webserver, Überwachungskamera) in Ihrem lokalen Netzwerk aus dem Internet erreichbar machen wollen. Seien Sie hier sehr vorsichtig und leiten Sie nur Ports weiter, die Sie wirklich benötigen.
            
            [![Bildmotiv: OpenWrt LuCI Firewall Settings page](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRefpAmt-qp7-GClTkqM2ObCqoZQR2BOtUQ3NelbvNO40Nk4tGybWWV51goBpFQ)Wird in einem neuen Fenster geöffnet](https://www.reddit.com/r/openwrt/comments/157g0ps/explain_luci_firewall_settings_page/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcQDsPs2pPiHN60JT0C5gSmR6KHemKpDPI1y39DsENKpXAWFU3erhAZR-PJSjvsHP1h8wtyE1tPnfR9SJQ_ptDxDc_3GRiAuyfM)www.reddit.com](https://www.reddit.com/r/openwrt/comments/157g0ps/explain_luci_firewall_settings_page/)
            
            OpenWrt LuCI Firewall Settings page
            
        - **SSH-Kommandozeile:** Die Firewall-Konfiguration kann komplex sein und wird oft über die LuCI Oberfläche verwaltet. Für fortgeschrittene Konfigurationen können Sie `iptables` oder `nftables` Befehle direkt in der Kommandozeile verwenden (erfordert tiefere Linux/Netzwerkkenntnisse).
- **Software aktuell halten (Firmware-Updates):**
    
    - **Was ist das?**: Wie jedes Betriebssystem benötigt auch OpenWrt regelmäßige Updates, um Sicherheitslücken zu schließen und Fehler zu beheben.
    - **Warum wichtig?**: Software-Updates sind entscheidend, um Ihren Router und Ihr Netzwerk vor neuen Bedrohungen zu schützen. Veraltete Software kann Sicherheitslücken enthalten, die von Angreifern ausgenutzt werden können.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"System" -> "Software"**. Klicken Sie auf **"Paketliste aktualisieren..."**. Danach können Sie unter "Aktualisierbare Pakete" sehen, ob Updates verfügbar sind. Klicken Sie auf **"Aktualisiere alle..."** um alle Pakete zu aktualisieren.
            
            [![Bildmotiv: OpenWrt LuCI Software Update page](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSBJgFOPpMGM9386EsNmwqxGVoK04_sRrk1ZLCcAuo7EpZCPGvIxLZKvofeXTZf)Wird in einem neuen Fenster geöffnet](https://forum.openwrt.org/t/unable-to-flash-new-firmware-image/191101)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcT55JW9EEpQkODhUTe6stxsYOsTH0m1qAoq49mSyOzA9AYvN269NHHuWvjML6b0xEa4tu99APT_tBiF-8M_OeE_WAGy48077i9Ydgg)forum.openwrt.org](https://forum.openwrt.org/t/unable-to-flash-new-firmware-image/191101)
            
            OpenWrt LuCI Software Update page
            
        - **SSH-Kommandozeile:** Verbinden Sie sich per SSH und führen Sie die Befehle `opkg update` (um die Paketlisten zu aktualisieren) und `opkg upgrade` (um installierte Pakete zu aktualisieren) aus. **Achtung:** `opkg upgrade` kann in seltenen Fällen zu Problemen führen, besonders bei größeren Versionssprüngen. Für größere Updates (z.B. von OpenWrt 22.x auf 23.x) ist oft eine Neuinstallation (Neuflashen) empfehlenswert.

**2. Netzwerk-Grundeinstellungen – Basis für Ihre Verbindung**

- **WAN (Internet-Verbindung) konfigurieren:**
    
    - **Was ist das?**: Das WAN (Wide Area Network) Interface ist die Schnittstelle Ihres Routers zum Internet. Hier konfigurieren Sie, wie der Router die Internetverbindung aufbaut (z.B. über DSL, Kabel, Ethernet).
    - **Warum wichtig?**: Ohne korrekte WAN-Konfiguration kann Ihr Router keine Internetverbindung aufbauen und Ihre Geräte im Netzwerk haben keinen Internetzugang.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"Netzwerk" -> "Interfaces"**. Suchen Sie das Interface mit dem Namen **"WAN"**. Klicken Sie auf **"Bearbeiten" (Edit)**.
            
            - **Protokoll:** Wählen Sie das passende Protokoll für Ihren Internetanschluss:
                - **DHCP-Client:** (Standard für Kabel- und viele DSL-Anschlüsse) Wählen Sie dies, wenn Ihr Router die IP-Adresse automatisch von Ihrem Internetprovider beziehen soll. In den meisten Fällen die richtige Wahl.
                - **PPPoE:** (Häufig für DSL-Anschlüsse in Deutschland) Wählen Sie dies, wenn Sie Zugangsdaten (Benutzername und Passwort) von Ihrem Internetprovider benötigen. Geben Sie diese unter **"PAP/CHAP Benutzername"** und **"PAP/CHAP Passwort"** ein.
                - **Statische IP-Adresse:** Nur wählen, wenn Sie von Ihrem Internetprovider eine feste IP-Adresse erhalten haben. Geben Sie dann die **"IPv4-Adresse"**, **"IPv4-Netzmaske"**, **"IPv4-Gateway"** und **"Primäre/Sekundäre DNS-Server"** manuell ein.
            - Klicken Sie auf **"Speichern & Anwenden"**.
            
            [![Bildmotiv: OpenWrt LuCI Network Interfaces page](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTKaYozTBelXuWl8EStcVp2WQO61y27f2WQ1hvoAjU_tl8VLb18VI3HCewKDgdI)Wird in einem neuen Fenster geöffnet](https://m2m-tele.com/blog/2021/03/12/openwrt-configuration-users-guide-part-1-how-to-configure-network-2/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcSBkKD2nbd2r5tEO1CLr26ApFdX7bYPi7YPP6a8t5oLyj5t9-c8r5H0CHrvDd2ATDvooaW-Hnt36irzV50GRE_5iLxs22kB)m2m-tele.com](https://m2m-tele.com/blog/2021/03/12/openwrt-configuration-users-guide-part-1-how-to-configure-network-2/)
            
            OpenWrt LuCI Network Interfaces page
            
        - **SSH-Kommandozeile:** Die WAN-Konfiguration kann auch über die Kommandozeile mit `uci` erfolgen. Beispiel für DHCP-Client (Standard):
            
            Bash
            
            ```
            uci set network.wan.proto='dhcp'
            uci commit network
            /etc/init.d/network reload
            ```
            
- **LAN (Lokales Netzwerk) konfigurieren:**
    
    - **Was ist das?**: Das LAN (Local Area Network) Interface definiert Ihr lokales Netzwerk, d.h. den Bereich, in dem Ihre Geräte (Computer, Smartphones, Smart-Home-Geräte etc.) miteinander kommunizieren und Internetzugang erhalten. Hier wird auch der DHCP-Server für die automatische IP-Adressvergabe konfiguriert.
    - **Warum wichtig?**: Die LAN-Konfiguration bestimmt die IP-Adressbereiche, den DHCP-Server und grundlegende Einstellungen für Ihr lokales Netzwerk.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"Netzwerk" -> "Interfaces"**. Suchen Sie das Interface mit dem Namen **"LAN"**. Klicken Sie auf **"Bearbeiten" (Edit)**.
            - **IPv4-Adresse:** Standardmäßig `192.168.1.1`. Sie können diese bei Bedarf ändern (z.B. auf `192.168.0.1`), **achten Sie aber darauf, dass Sie den IP-Adressbereich nicht mit anderen Netzwerken überlappen.**
            - **IPv4-Netzmaske:** Standardmäßig `255.255.255.0`. In den meisten Heimnetzwerken korrekt.
            - **DHCP-Server:** Stellen Sie sicher, dass der DHCP-Server aktiviert ist ("DHCP-Server aktivieren"). Im Reiter **"DHCP-Server"** können Sie den **"Start"** und **"Ende"** des IP-Adressbereichs definieren, der automatisch an Geräte vergeben wird (z.B. Start: `192.168.1.100`, Ende: `192.168.1.250`). Sie können auch die **"Lease Time"** (Gültigkeitsdauer der IP-Adresse) anpassen.
                
                [![Bildmotiv: OpenWrt LuCI LAN Interface DHCP Server settings](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSqhnJv_9fRe7aHj-6_00oatkqULL6_cignDsb4K93A5tLOE_31q_To-iitSk_l)Wird in einem neuen Fenster geöffnet](https://www.encrypted.at/specifying-a-tftp-server-dhcp-option-in-openwrt/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcSqtqEpho2S5VAwXqGTtIMwCl5gDAaMruNheTnzZWsUAHKZhK6KHtYRGkQvSjE81NfFRF_9jn8dD8SqHa_OE53rQQScqEqcf9M8EQ)www.encrypted.at](https://www.encrypted.at/specifying-a-tftp-server-dhcp-option-in-openwrt/)
                
                OpenWrt LuCI LAN Interface DHCP Server settings
                
            - Klicken Sie auf **"Speichern & Anwenden"**.
        - **SSH-Kommandozeile:** Beispiel für die Änderung der LAN IP-Adresse und DHCP-Bereich:
            
            Bash
            
            ```
            uci set network.lan.ipaddr='192.168.0.1'
            uci set dhcp.lan.start='100'
            uci set dhcp.lan.limit='150'
            uci commit network
            uci commit dhcp
            /etc/init.d/network reload
            /etc/init.d/dhcp reload
            ```
            
- **WLAN (Drahtloses Netzwerk) einrichten:**
    
    - **Was ist das?**: Konfiguration Ihres drahtlosen Netzwerks (WLAN oder WiFi). Hier definieren Sie den WLAN-Namen (SSID), das Passwort, die Verschlüsselungsmethode, den Kanal etc.
    - **Warum wichtig?**: WLAN ermöglicht drahtlose Verbindungen für Ihre Geräte. Eine sichere und gut konfigurierte WLAN-Einrichtung ist entscheidend für die Nutzung des Internets mit mobilen Geräten und die Sicherheit Ihres drahtlosen Netzwerks.
    - **Wie konfigurieren?**:
        - **LuCI (Webinterface):** Gehen Sie zu **"Netzwerk" -> "Drahtlos"**.
            
            - Sie sehen in der Regel ein oder mehrere Geräte (Radios) für 2.4 GHz und 5 GHz WLAN. Klicken Sie bei dem gewünschten Funkgerät auf **"Bearbeiten" (Edit)** oder **"Aktivieren" (Enable)** (falls deaktiviert).
            - **Gerätekonfiguration (Reiter "Allgemeine Einstellungen"):**
                - **Modus:** "Access Point" ist der Standardmodus für ein WLAN-Netzwerk.
                - **Kanal:** "Auto" ist oft eine gute Wahl. Bei Problemen (Interferenzen) können Sie einen festen Kanal wählen (testen Sie verschiedene Kanäle, um den besten zu finden).
                - **Frequenzband:** Wählen Sie das gewünschte Frequenzband (2.4 GHz oder 5 GHz). 5 GHz ist schneller und weniger überlastet, hat aber eine geringere Reichweite. 2.4 GHz hat eine größere Reichweite, ist aber oft stärker durch andere WLANs und Geräte überlastet. Moderne Router unterstützen oft beide Frequenzbänder gleichzeitig (Dual-Band WLAN).
            - **Interface Konfiguration (Reiter "Wireless Security" oder "Drahtlose Sicherheit"):**
                - **Verschlüsselung:** **Wählen Sie unbedingt eine sichere Verschlüsselungsmethode! "WPA2-PSK" oder "WPA3-SAE" (oder "WPA2/WPA3 Mixed") sind empfehlenswert.** Vermeiden Sie **"WEP"** oder **"Keine Verschlüsselung"**.
                - **Schlüssel (Passwort):** Geben Sie ein **starkes WLAN-Passwort** (WLAN-Schlüssel) ein.
            - **Interface Konfiguration (Reiter "Erweiterte Einstellungen" oder "Advanced Settings"):** Hier können Sie erweiterte Einstellungen wie z.B. WLAN-Standard (802.11 b/g/n/ac/ax), Kanalbreite etc. anpassen (für die meisten Nutzer sind die Standardwerte ausreichend).
            - Klicken Sie auf **"Speichern & Anwenden"**.
            
            [![Bildmotiv: OpenWrt LuCI Wireless Overview page](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1z6CVkj7cBKNVbaxfH1UcbUg8oDDz-tyR4WvhjRa5I65BAxqSEwvwslbpS0cN)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-quick-start/walkthrough_wifi)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-quick-start/walkthrough_wifi)
            
            OpenWrt LuCI Wireless Overview page
            
        - **SSH-Kommandozeile:** Beispiel für das Setzen der SSID und des WLAN-Passworts (WPA2-PSK):
            
            Bash
            
            ```
            uci set wireless.@wifi-iface[0].ssid='MeinNeuesWLANNetzwerk'
            uci set wireless.@wifi-iface[0].encryption='psk2'
            uci set wireless.@wifi-iface[0].key='MeinSuperSicheresWLANPasswort'
            uci commit wireless
            wifi reload
            ```
            

**3. Optionale, aber nützliche Einstellungen (je nach Bedarf)**

- **Zeitzone und NTP-Server einstellen:** (System -> System -> System) Korrekte Zeit ist wichtig für Logdateien, Zeitpläne (z.B. Kindersicherung) und Zertifikate. Wählen Sie Ihre Zeitzone und stellen Sie sicher, dass ein NTP-Server konfiguriert ist (Standardeinstellungen sind meist gut).
- **DHCP-Leases überprüfen und statische DHCP-Leases vergeben:** (Netzwerk -> DHCP und DNS -> Statische DHCP-Leases) Hier sehen Sie, welche Geräte aktuell eine IP-Adresse von Ihrem Router erhalten haben (aktive DHCP-Leases). Sie können hier auch statische DHCP-Leases vergeben, um bestimmten Geräten immer die gleiche IP-Adresse zuzuweisen (nützlich für Server, Drucker etc.).
- **Gast-WLAN einrichten:** (Netzwerk -> Drahtlos -> Funkgerät hinzufügen) Richten Sie ein separates WLAN für Gäste ein. Dies erhöht die Sicherheit, da Gäste so keinen Zugriff auf Ihr Hauptnetzwerk haben.
- **VPN-Client oder VPN-Server konfigurieren:** (VPN -> WireGuard/OpenVPN, je nachdem, welches VPN Protokoll Sie nutzen möchten) OpenWrt ist ideal für die Einrichtung von VPNs. Sie können Ihren Router als VPN-Client konfigurieren, um Ihren gesamten Internetverkehr über ein VPN zu leiten, oder als VPN-Server, um von unterwegs sicher auf Ihr Heimnetzwerk zuzugreifen.
- **Quality of Service (QoS) / Smart Queue Management (SQM):** (Netzwerk -> SQM QoS) SQM kann die Netzwerk-Performance verbessern, insbesondere bei überlasteten Verbindungen (z.B. bei Uploads oder Downloads), indem es Pufferbloating reduziert und den Datenverkehr intelligent priorisiert.



ADONS Erweiterungen 

**1. Sicherheits-Addons - Schutz für Ihr Netzwerk**

- **VPN-Client und VPN-Server (z.B. `openvpn-openssl`, `wireguard-tools`, `strongswan`):**
    - **Funktion:** Ermöglichen es, Ihren Router als VPN-Client zu konfigurieren (um Ihren gesamten Internetverkehr über ein VPN zu leiten) oder als VPN-Server (um von unterwegs sicher auf Ihr Heimnetzwerk zuzugreifen).
    - **Warum wichtig?**: **Erhöhte Privatsphäre und Sicherheit** im Internet (VPN-Client), **sicherer Fernzugriff** auf Ihr Heimnetzwerk (VPN-Server), **Umgehung von Geoblocking**.
    - **Beliebte Pakete:**
        - `openvpn-openssl` und `luci-app-openvpn`: Für das etablierte OpenVPN Protokoll.
            
            [![Bildmotiv: OpenWrt LuCI OpenVPN Client configuration](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS827JGAtF99G7_xjQn20z7C-UQ8dLOkDvOIwWnE3hBd7qfKYUdLZ5baX2e3NcD)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-user/services/vpn/openvpn/client-luci)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-user/services/vpn/openvpn/client-luci)
            
            OpenWrt LuCI OpenVPN Client configuration
            
        - `wireguard-tools` und `luci-app-wireguard`: Für das modernere und oft schnellere WireGuard Protokoll.
            
            [![Bildmotiv: OpenWrt LuCI WireGuard Client configuration](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDgswprC0i9zkKg3fqVXXGGKN0kDRf8A_LzPJVktRdcISQ_KVSj3s9uGAmMnuX)Wird in einem neuen Fenster geöffnet](https://www.vpnunlimited.com/help/manuals/open-wrt-wireguard-setup)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcQ8Q8Iwx5o0Fr_Kr_kARDYBcu88Q96KibcOKZy_aqmNGuijoMoMc1fCxMTPdTHhFYhWnbWwKRz8DVGEP1t80jk8ytdAYD8_k9HnFwR6AtY)www.vpnunlimited.com](https://www.vpnunlimited.com/help/manuals/open-wrt-wireguard-setup)
            
            OpenWrt LuCI WireGuard Client configuration
            
        - `strongswan` und `luci-app-strongswan`: Für IPSec-basierte VPNs, oft für Unternehmensanbindungen.
- **Firewall Erweiterungen (z.B. `iptables`, `nftables`, `firewall-packages`):**
    - **Funktion:** OpenWrt hat bereits eine sehr gute integrierte Firewall. Diese Pakete bieten zusätzliche Funktionen, wie z.B. erweiterte Regeln, Intrusion Detection/Prevention Systeme (IDS/IPS) oder verbesserte Protokollierung.
    - **Warum wichtig?**: **Erhöhung der Netzwerksicherheit**, Schutz vor Angriffen und unerwünschtem Datenverkehr, detailliertere Kontrolle des Netzwerkverkehrs.
    - **Beliebte Pakete:**
        - `firewall-packages`: Enthält verschiedene nützliche Erweiterungen für die OpenWrt Firewall (z.B. `iptables-mod-conntrack-extra`, `iptables-mod-ipopt`).
        - `snort` oder `suricata`: Leistungsfähige IDS/IPS-Systeme (sind aber ressourcenintensiv und eher für fortgeschrittene Nutzer).
- **BanIP (z.B. `banip` und `luci-app-banip`):**
    - **Funktion:** Blockiert automatisch IP-Adressen, die verdächtiges Verhalten zeigen (z.B. wiederholte fehlgeschlagene Login-Versuche, Portscans) basierend auf verschiedenen Blacklists und Regeln.
    - **Warum wichtig?**: **Proaktiver Schutz** vor Brute-Force-Angriffen und unerwünschten Zugriffen, **Reduzierung von Log-Spam**.
    - **Beliebtes Paket:** `banip` und das zugehörige LuCI-App `luci-app-banip` für einfache Konfiguration im Webinterface.
        
        [![Bildmotiv: OpenWrt LuCI BanIP configuration](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTG9sW2VQ2dSijAmvXuGLm1ZMPdXIXAtj7u47w_WsiWxdidSRNUW-GSLZxGByba)Wird in einem neuen Fenster geöffnet](https://prafiles.in/banip-openwrt-ip-list-blocker/)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSWlVIvYy12N-c_lKEEKdAi6ySb5LyVD1P4z2jyOjpAAYKoKykdJk_a6ovDCX8mvNexBZf5aKTYgC1QG4kbcKFyy0E81W8)prafiles.in](https://prafiles.in/banip-openwrt-ip-list-blocker/)
        
        OpenWrt LuCI BanIP configuration
        

**2. Netzwerk-Performance und Optimierung**

- **SQM (Smart Queue Management) (z.B. `sqm-scripts` und `luci-app-sqm`):**
    - **Funktion:** Verbessert die Netzwerk-Performance, insbesondere bei überlasteten Verbindungen (Pufferbloating), indem es den Datenverkehr intelligent priorisiert und Warteschlangen verwaltet.
    - **Warum wichtig?**: **Reduziert Latenz und Jitter**, was zu einem **flüssigeren Interneterlebnis** führt, besonders wichtig für Online-Gaming, Videokonferenzen und VoIP. Hilft gegen "Bufferbloat", das typische Problem bei vollen Upload- oder Download-Leitungen.
    - **Beliebtes Paket:** `sqm-scripts` und das LuCI-App `luci-app-sqm` für einfache Konfiguration.
        
        [![Bildmotiv: OpenWrt LuCI SQM QoS configuration](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTOBIImMRQIuFHO6lmLkbFyj_376b7vcFXbp6-gUiPR2BruzIaD_tZwbQKHZbyW)Wird in einem neuen Fenster geöffnet](https://www.youtube.com/watch?v=OPtFTcX92lw)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcSg-IUWG8CFYnlyzc2Hu641oPbwT1I4yvlIlgdH-i46sw1qkFzHEP3ZG4a1_MDcfCUfjA0ho3Du2a4FyApH4L1SPtX9i5fxHlQX)www.youtube.com](https://www.youtube.com/watch?v=OPtFTcX92lw)
        
        OpenWrt LuCI SQM QoS configuration
        
- **AdBlock (z.B. `adblock` und `luci-app-adblock`):**
    - **Funktion:** Blockiert Werbung auf Netzwerkebene für alle Geräte in Ihrem Netzwerk. Funktioniert für Webbrowser, Apps, Smart-TVs etc.
    - **Warum wichtig?**: **Werbefreies Surfen**, **schnellere Seitenladezeiten**, **reduzierter Datenverbrauch**, **erhöhte Privatsphäre** (Tracking-Blockierung).
    - **Beliebtes Paket:** `adblock` und das LuCI-App `luci-app-adblock` für einfache Konfiguration und Black-/Whitelisting.
        
        [![Bildmotiv: OpenWrt LuCI AdBlock configuration](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQQlwP1myqn5SzKstQ6cm5A23enK3VjYV7-BQESAXijaA5h-VTdhMZd80Jp0cJ0)Wird in einem neuen Fenster geöffnet](https://blog.51sec.org/2021/03/install-adblock-in-your-openwrt-router.html)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcQu2XEmJ90qFttBUzzetmxkkE8ezQFfDMP5xJdFIJWrk2AZ_JE0Qa-SvRSrP47E7yz34G5nwEoU3YY1WEc7dqHaE18h-pFnIKA)blog.51sec.org](https://blog.51sec.org/2021/03/install-adblock-in-your-openwrt-router.html)
        
        OpenWrt LuCI AdBlock configuration
        
- **mwan3 (MultiWAN) (z.B. `mwan3` und `luci-app-mwan3`):**
    - **Funktion:** Ermöglicht die Nutzung von **mehreren Internetverbindungen gleichzeitig** (z.B. DSL und Mobilfunk) für **Load Balancing** (Verteilung des Traffics auf mehrere Verbindungen) oder **Failover** (automatische Umschaltung auf eine Backup-Verbindung bei Ausfall der Hauptverbindung).
    - **Warum wichtig?**: **Erhöhte Ausfallsicherheit**, **höhere Bandbreite** (in Load Balancing Modi), **bessere Lastverteilung**.
    - **Beliebtes Paket:** `mwan3` und das LuCI-App `luci-app-mwan3` für die Konfiguration von MultiWAN Szenarien.
        
        [![Bildmotiv: OpenWrt LuCI mwan3 MultiWAN configuration](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwjooURHh0PX8XGUuZdCBNFBVegUkQypLWOkhkLniLjscOQ1XFNTTLiZm_pnxg)Wird in einem neuen Fenster geöffnet](https://www.youtube.com/watch?v=vHWYH_5ooEY)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcSg-IUWG8CFYnlyzc2Hu641oPbwT1I4yvlIlgdH-i46sw1qkFzHEP3ZG4a1_MDcfCUfjA0ho3Du2a4FyApH4L1SPtX9i5fxHlQX)www.youtube.com](https://www.youtube.com/watch?v=vHWYH_5ooEY)
        
        OpenWrt LuCI mwan3 MultiWAN configuration
        

**3. Speicher und Dateifreigabe**

- **USB-Storage Unterstützung (Kernelmodule und Dateisystem-Tools):**
    - **Funktion:** Ermöglichen die Nutzung von USB-Festplatten oder USB-Sticks, die an den Router angeschlossen werden, für verschiedene Zwecke. Grundvoraussetzung für viele NAS-Funktionen.
    - **Warum wichtig?**: **Erweiterung des Speicherplatzes** des Routers, Basis für NAS-Funktionen, Medienserver, Download-Clients etc.
    - **Wichtige Pakete:**
        - Kernelmodule für Dateisysteme (z.B. `kmod-fs-ext4`, `kmod-fs-ntfs`, `kmod-fs-vfat`).
        - Tools zur Dateisystemverwaltung (z.B. `block-mount`, `e2fsprogs`, `ntfs-3g`).
- **Samba (z.B. `samba4-server` und `luci-app-samba4`):**
    - **Funktion:** Macht Ihren Router zu einem **Netzwerk-Dateiserver (NAS)**. Ermöglicht den Zugriff auf Dateien auf angeschlossenen USB-Speichern von Windows, macOS und Linux Computern im Netzwerk über das SMB/CIFS Protokoll.
    - **Warum wichtig?**: **Zentrale Dateifreigabe** im Heimnetzwerk, einfache Möglichkeit, Dateien zwischen verschiedenen Geräten auszutauschen, **Backup-Ziel** für Computer.
    - **Beliebtes Paket:** `samba4-server` (modernere Samba 4 Version) und das LuCI-App `luci-app-samba4` für einfache Konfiguration. Es gibt auch `samba36-server` (ältere Version).
        
        [![Bildmotiv: OpenWrt LuCI Samba configuration](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkPU3TRVVsIsBRZ9sbqQOTGbZ5Fh5ERTks2dMZw6fnTWR8wisvmvSNhLAxXcty)Wird in einem neuen Fenster geöffnet](https://openwrt.org/docs/guide-user/services/nas/usb-storage-samba-webinterface)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSwzdLoRcW4W7ixxkJW77ptkQJ5MihawAKRYTZ8yv-MfyQD7Lp9RBMar77ctnEcckOnDOcXfq01m8QsD6skqpyHd4IFP10)openwrt.org](https://openwrt.org/docs/guide-user/services/nas/usb-storage-samba-webinterface)
        
        OpenWrt LuCI Samba configuration
        
- **MiniDLNA/ReadyMedia (z.B. `minidlna` und `luci-app-minidlna`):**
    - **Funktion:** Macht Ihren Router zu einem **DLNA/UPnP Medienserver**. Ermöglicht das Streaming von Mediendateien (Filme, Musik, Fotos) auf DLNA-fähige Geräte im Netzwerk (Smart-TVs, Spielekonsolen, Media-Player).
    - **Warum wichtig?**: **Zentrale Medienbibliothek**, einfache Wiedergabe von Medien auf verschiedenen Geräten im Wohnzimmer.
    - **Beliebtes Paket:** `minidlna` und das LuCI-App `luci-app-minidlna` für einfache Konfiguration. Auch bekannt als `ReadyMedia` in neueren OpenWrt Versionen.
        
        [![Bildmotiv: OpenWrt LuCI MiniDLNA configuration](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTv0-kDF5Mn7p7W6q5MG9DZ400NA5OUNot_ULD7bX1GLUqLoQrRFDHzXV-sKc_d)Wird in einem neuen Fenster geöffnet](https://forum.openwrt.org/t/openwrt-dlna-media-server-how-to-page/51556)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcT55JW9EEpQkODhUTe6stxsYOsTH0m1qAoq49mSyOzA9AYvN269NHHuWvjML6b0xEa4tu99APT_tBiF-8M_OeE_WAGy48077i9Ydgg)forum.openwrt.org](https://forum.openwrt.org/t/openwrt-dlna-media-server-how-to-page/51556)
        
        OpenWrt LuCI MiniDLNA configuration
        
- **Download-Clients (z.B. `transmission-daemon`, `aria2` und zugehörige LuCI Apps):**
    - **Funktion:** Ermöglichen das Herunterladen von Dateien direkt auf den Router (und angeschlossenen USB-Speicher), z.B. über BitTorrent (`transmission-daemon`) oder HTTP/FTP/Metalink (`aria2`).
    - **Warum wichtig?**: **Autonomes Herunterladen** ohne laufenden Computer, zentrale Download-Verwaltung, Zugriff auf Downloads über das Netzwerk.
    - **Beliebte Pakete:**
        - `transmission-daemon` und `luci-app-transmission`: Beliebter BitTorrent Client.
            
            [![Bildmotiv: OpenWrt LuCI Transmission configuration](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKcd6vbddKRV4v5dLkXtTAIPtrtfgH6bBYZ955Y8qV_V2tdWMv_o1DPmbWF5Vp)Wird in einem neuen Fenster geöffnet](https://github.com/openwrt/luci/issues/4697)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcQMWyctgi21E3pB8xn4iBFazkndTUvaPmX-zdFv06DZ-mByF8axuc_CClAiYh_1yRIIVp9Y2iFuFB2ATC5ZrlssaIhE-Q)github.com](https://github.com/openwrt/luci/issues/4697)
            
            OpenWrt LuCI Transmission configuration
            
        - `aria2` und `luci-app-aria2`: Vielseitiger Download-Client für verschiedene Protokolle, oft schneller als `wget`.

**4. WLAN-Erweiterungen**

- **WLAN-Roaming (z.B. `wpad-mesh-openssl` oder `wpad-wolfssl`):**
    - **Funktion:** Ermöglicht **nahtloses WLAN-Roaming** zwischen mehreren Access Points (OpenWrt Routern), die im Mesh-Modus arbeiten oder das 802.11r Fast Transition Protokoll unterstützen. Geräte wechseln automatisch zum Access Point mit dem besten Signal, ohne die Verbindung zu unterbrechen.
    - **Warum wichtig?**: **Verbesserte WLAN-Abdeckung** in größeren Wohnungen oder Häusern, **unterbrechungsfreies WLAN** beim Bewegen zwischen verschiedenen Bereichen.
    - **Wichtige Pakete:** `wpad-mesh-openssl` oder `wpad-wolfssl` (ersetzen den Standard `wpad-basic-wolfssl` oder `wpad-basic-openssl`). Zusätzlich ggf. `hostapd-utils` und `wpa-supplicant-utils`. Konfiguration erfordert etwas mehr Aufwand und ist geräteabhängig.
- **WLAN-Scheduler (z.B. `wifischedule` und `luci-app-wifischedule`):**
    - **Funktion:** Ermöglicht das **zeitgesteuerte Ein- und Ausschalten des WLANs**. Nützlich, um das WLAN nachts automatisch abzuschalten oder den WLAN-Zugang für Kinder zeitlich zu begrenzen.
    - **Warum wichtig?**: **Energie sparen**, **Kontrolle über WLAN-Nutzungszeiten**, **Reduzierung der WLAN-Strahlung** (optionaler Aspekt).
    - **Beliebtes Paket:** `wifischedule` und das LuCI-App `luci-app-wifischedule` für einfache Konfiguration von Zeitplänen.
        
        [![Bildmotiv: OpenWrt LuCI Wifi Schedule configuration](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR-xTVT3HohgHagItYykD1_a8cm_Tk5KMhkS6ntqEldgtO-AwbB3HBauiNDgvKf)Wird in einem neuen Fenster geöffnet](https://forum.openwrt.org/t/wifi-configuration/25710)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcT55JW9EEpQkODhUTe6stxsYOsTH0m1qAoq49mSyOzA9AYvN269NHHuWvjML6b0xEa4tu99APT_tBiF-8M_OeE_WAGy48077i9Ydgg)forum.openwrt.org](https://forum.openwrt.org/t/wifi-configuration/25710)
        
        OpenWrt LuCI Wifi Schedule configuration
        

**5. Systemüberwachung und -verwaltung**

- **System-Monitoring (z.B. `collectd`, `collectd-mod-...`, `luci-app-statistics`):**
    - **Funktion:** Sammelt System- und Netzwerk-Metriken (CPU-Last, Speicherauslastung, Netzwerk-Traffic, WLAN-Signalstärke etc.) und stellt diese grafisch dar (z.B. in LuCI oder über externe Tools wie Grafana).
    - **Warum wichtig?**: **Überwachung der Router-Performance**, **Fehleranalyse**, **Identifizierung von Netzwerk-Engpässen**, **Langzeit-Analyse** des Netzwerkverhaltens.
    - **Beliebte Pakete:**
        - `collectd`: Kernpaket für die Datenerfassung.
        - `collectd-mod-...`: Verschiedene Module für `collectd` zur Überwachung verschiedener Aspekte (z.B. `collectd-mod-cpu`, `collectd-mod-interface`, `collectd-mod-wireless`).
        - `luci-app-statistics`: LuCI App zur grafischen Darstellung der gesammelten Daten im Webinterface.
            
            [![Bildmotiv: OpenWrt LuCI Statistics graphs](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQzC9wH86EPeZ5_Wtcwhx24iQmriVh-pooys1zxJmGZE7Peg7LKuWWFNBTrTSzm)Wird in einem neuen Fenster geöffnet](https://github.com/openwrt/luci/issues/5689)[![](https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcQMWyctgi21E3pB8xn4iBFazkndTUvaPmX-zdFv06DZ-mByF8axuc_CClAiYh_1yRIIVp9Y2iFuFB2ATC5ZrlssaIhE-Q)github.com](https://github.com/openwrt/luci/issues/5689)
            
            OpenWrt LuCI Statistics graphs
            
- **DDNS (Dynamic DNS) (z.B. `ddns-scripts` und `luci-app-ddns`):**
    - **Funktion:** Ermöglicht den **Zugriff auf Ihr Heimnetzwerk über einen festen Domainnamen**, auch wenn Ihre öffentliche IP-Adresse sich regelmäßig ändert (was bei den meisten privaten Internetanschlüssen der Fall ist).
    - **Warum wichtig?**: **Einfacher Fernzugriff** auf Dienste in Ihrem Heimnetzwerk (z.B. Webserver, Überwachungskamera, VPN-Server), auch wenn Sie keine statische IP-Adresse haben.
    - **Beliebtes Paket:** `ddns-scripts` und das LuCI-App `luci-app-ddns` für die Konfiguration verschiedener DDNS-Dienste.
        
        [![Bildmotiv: OpenWrt LuCI Dynamic DNS configuration](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcShmE81hDGepSYxKUHxkabcDW6VfKmAr6NTR4mWLOwrLd7WzvEZOamlaKhRM2Hl)Wird in einem neuen Fenster geöffnet](https://myonlineportal.net/dyndns/how_to_openwrt)[![](https://encrypted-tbn3.gstatic.com/favicon-tbn?q=tbn:ANd9GcTBhJVZj0kMwGSvfIqIPPCRlNbOYbvE4VkDRqSdD3dUTyXyYgb90hcq4nqjeGyUgJQ79JSH-oHcVizsQIDVBWf3jTtv0k_UU3pEWuf_)myonlineportal.net](https://myonlineportal.net/dyndns/how_to_openwrt)
        
        OpenWrt LuCI Dynamic DNS configuration
        
- **LuCI Erweiterungen (Themes, Apps, Sprachpakete):**
    - **Funktion:** **Verbesserung und Anpassung des LuCI Webinterfaces**. Themes verändern das Aussehen, Apps fügen neue Funktionen hinzu, Sprachpakete übersetzen die Oberfläche in andere Sprachen.
    - **Warum wichtig?**: **Benutzerfreundlichkeit**, **Personalisierung**, **zusätzliche Funktionen** im Webinterface.
    - **Beliebte Pakete:**
        - `luci-theme-...`: Verschiedene LuCI Themes zur optischen Anpassung (z.B. `luci-theme-bootstrap`, `luci-theme-material`).
        - `luci-i18n-german`: Deutsches Sprachpaket für LuCI (und weitere Sprachpakete für andere Sprachen).
        - Viele weitere LuCI Apps, die Funktionen für bestimmte Pakete oder Bereiche hinzufügen (siehe Beispiele oben bei den einzelnen Kategorien).

**6. Smart Home / Automatisierung (Ausblick - noch weniger "Kern", aber wachsendes Interesse)**

- **MQTT Broker (z.B. `mosquitto` und `luci-app-mosquitto`):**
    - **Funktion:** Macht Ihren Router zu einem **MQTT Broker**, der als zentrale Kommunikationsplattform für Smart Home Geräte dient. MQTT ist ein leichtgewichtiges Protokoll für Machine-to-Machine Kommunikation und beliebt im Smart Home Bereich.
    - **Warum wichtig?**: **Grundlage für Smart Home Automatisierung** mit MQTT-basierten Geräten und Software (z.B. Home Assistant, Node-RED).
    - **Beliebtes Paket:** `mosquitto` und das LuCI-App `luci-app-mosquitto`.
- **Node-RED (z.B. `node-red` und `luci-app-node-red`):**
    - **Funktion:** Ein **visueller Flow-basierter Editor** zur Automatisierung verschiedener Aufgaben, ideal für Smart Home Automatisierung. Kann mit MQTT, HTTP, Netzwerkprotokollen, Sensoren, Aktoren und vielem mehr interagieren.
    - **Warum wichtig?**: **Einfache Erstellung von Automatisierungen** ohne Programmierung, **flexible Integration** verschiedener Geräte und Dienste, **mächtiges Werkzeug** für Smart Home Szenarien.
    - **Beliebtes Paket:** `node-red` und das LuCI-App `luci-app-node-red`. Erfordert etwas mehr Ressourcen (RAM, Flash-Speicher).
        
        [![Bildmotiv: NodeRED flow editor](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTFRBa0gUpaxRTC9lICXxU8K0ivHOY2cy4n9sCztu5I9Hk7K8bNZa7WBmnWz3Vv)Wird in einem neuen Fenster geöffnet](https://nodered.org/docs/user-guide/editor/)[![](https://encrypted-tbn2.gstatic.com/favicon-tbn?q=tbn:ANd9GcR_rU1KC3FzGZ3Zz2DT18zDESrMy8NSiedDogtlj7PKLOhBKK3KxO6qBJBi41y9Z-saBf3RQv6eKBgWMryqFxHDAyZnh6Q)nodered.org](https://nodered.org/docs/user-guide/editor/)
        
        NodeRED flow editor
        

**Installation von Paketen in OpenWrt**

Pakete in OpenWrt werden über den **Paketmanager `opkg`** installiert. Es gibt mehrere Wege, Pakete zu installieren:

- **LuCI Webinterface:** (Einfachste Methode für die meisten Nutzer)
    - Gehen Sie zu **"System" -> "Software"**.
    - Im Feld "Paket herunterladen und installieren" geben Sie den **Paketnamen** ein (z.B. `luci-app-sqm`) und klicken auf **"OK"**.
    - Warten Sie, bis die Installation abgeschlossen ist.
    - **Vorher:** Klicken Sie auf **"Paketliste aktualisieren..."** um sicherzustellen, dass Sie die aktuelle Paketliste haben.
- **SSH-Kommandozeile:** (Für fortgeschrittene Nutzer oder wenn LuCI nicht verfügbar ist)
    - Verbinden Sie sich per SSH mit Ihrem Router.
    - **Aktualisieren Sie die Paketlisten:** `opkg update`
    - **Installieren Sie ein Paket:** `opkg install <paketname>` (z.B. `opkg install luci-app-sqm`)
    - **Aktualisieren Sie ein installiertes Paket:** `opkg upgrade <paketname>`
    - **Deinstallieren Sie ein Paket:** `opkg remove <paketname>`

**Wichtige Hinweise:**

- **Speicherplatz:** Router haben oft begrenzten Flash-Speicher. Installieren Sie nur die Pakete, die Sie wirklich benötigen. Zu viele Pakete können den Speicherplatz füllen und die Performance beeinträchtigen. Achten Sie auf Router mit ausreichend Flash-Speicher, wenn Sie viele Addons planen.
- **RAM:** Einige Pakete (z.B. `snort`, `Node-RED`, `samba4-server`) benötigen mehr RAM. Router mit wenig RAM können bei der Nutzung solcher Pakete langsam oder instabil werden.
- **Kompatibilität:** Stellen Sie sicher, dass die Pakete, die Sie installieren, mit Ihrer OpenWrt Version kompatibel sind. In der Regel ist dies bei Paketen aus den offiziellen OpenWrt Repositories der Fall.
- **Dokumentation:** Lesen Sie die Dokumentation zu den Paketen, die Sie installieren möchten. Oft gibt es spezifische Konfigurationsschritte oder Hinweise zur Nutzung. Die OpenWrt Wiki ([https://openwrt.org/](https://www.google.com/url?sa=E&source=gmail&q=https://www.google.com/url?sa=E%26source=gmail%26q=https://openwrt.org/)) ist eine sehr gute Ressource.
- **"Wichtig" ist subjektiv:** Die "wichtigsten" Addons sind sehr individuell. Überlegen Sie sich, welche Funktionen Sie benötigen und suchen Sie gezielt nach den passenden Paketen. Die hier vorgestellte Auswahl ist nur ein Startpunkt und eine Orientierungshilfe. Es gibt noch viele weitere nützliche Pakete in den OpenWrt Repositories.