
**Angreifen (Offensive Nutzung):**

Ein OpenWrt Router kann, entsprechend konfiguriert und mit den richtigen Werkzeugen ausgestattet, für verschiedene Arten von Angriffen verwendet werden. 

- **Man-in-the-Middle (MITM) Angriffe:**
    
    - **Prinzip:** Der Router wird so positioniert, dass er den Datenverkehr zwischen zwei Kommunikationspartnern abfängt, mitliest und gegebenenfalls manipuliert. Dies ist besonders in ungesicherten WLAN-Netzwerken relevant.
    - **OpenWrt Rolle:** OpenWrt bietet die nötige Flexibilität, um Netzwerk-Interfaces in den "Promiscuous Mode" zu versetzen, IP-Forwarding zu aktivieren und Werkzeuge zu installieren, die MITM-Angriffe ermöglichen.
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `ettercap`: Ein vielseitiges MITM-Framework für verschiedene Protokolle.
        - `mitmf (Man-in-the-middle framework)`: Ein weiteres Framework, das verschiedene MITM-Angriffe vereinfacht.
        - `bettercap`: Ein modernes und mächtiges Framework für MITM und WLAN-Angriffe.
    - **Angriffstechniken (beispielhaft):**
        - **ARP-Spoofing/ARP-Poisoning:** Der Angreifer manipuliert die ARP-Tabellen im Netzwerk, um den Datenverkehr des Opfers über den eigenen Router umzuleiten.
        - **DNS-Spoofing/DNS-Poisoning:** Der Angreifer fälscht DNS-Antworten, um das Opfer auf gefälschte Webseiten umzuleiten (z.B. für Phishing).
        - **HTTP-Session-Hijacking:** Das Abfangen von unverschlüsselten HTTP-Sessions und die Übernahme der Identität des Nutzers.
        - **HTTPS-Downgrade-Angriffe (SSL-Stripping):** Versuche, eine HTTPS-Verbindung zu einer unsicheren HTTP-Verbindung herunterzustufen, um den Verkehr mitlesen zu können (wird durch moderne Browser und HTTPS-Strict-Transport-Security – HSTS – erschwert, aber nicht unmöglich).
    - **Schutzmaßnahmen (für die Opferseite):**
        - **Verwendung von HTTPS:** Sicherstellen, dass Webseiten und Dienste über HTTPS (mit gültigem Zertifikat) aufgerufen werden.
        - **VPN-Nutzung:** Ein VPN verschlüsselt den gesamten Datenverkehr und schützt vor MITM-Angriffen im lokalen Netzwerk.
        - **WLAN-Verschlüsselung (WPA3):** Ein stark verschlüsseltes WLAN (WPA3 ist empfehlenswert) reduziert das Risiko von MITM-Angriffen im WLAN.
- **Denial of Service (DoS) und Distributed Denial of Service (DDoS) Angriffe:**
    
    - **Prinzip:** Das Ziel ist es, einen Dienst, ein Netzwerk oder ein System durch Überlastung unbrauchbar zu machen.
    - **OpenWrt Rolle:** OpenWrt kann als Plattform dienen, um DoS/DDoS-Angriffe zu starten, entweder von einem einzelnen Router (DoS) oder in einem Botnetz von kompromittierten OpenWrt Routern (DDoS).
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `hping3`: Ein vielseitiges Netzwerk-Tool, das für verschiedene Arten von DoS-Angriffen verwendet werden kann (SYN-Flood, UDP-Flood, etc.).
        - `nmap`: Kann für einfache DoS-Scans verwendet werden (`-T4 -A -p- --max-rate=X <Ziel>`).
        - `mflood`: Ein spezialisiertes Tool für UDP-Flood-Angriffe.
    - **Angriffstechniken (beispielhaft):**
        - **SYN-Flood:** Der Angreifer sendet eine große Anzahl von SYN-Paketen an das Ziel, ohne die TCP-Handshakes abzuschließen, wodurch der Server in einen Wartezustand versetzt und Ressourcen verbraucht werden.
        - **UDP-Flood:** Der Angreifer überschwemmt das Ziel mit einer großen Menge an UDP-Paketen.
        - **HTTP-Flood:** Der Angreifer sendet eine große Anzahl von HTTP-Requests an einen Webserver, um diesen zu überlasten.
        - **DNS-Amplification-Attack:** Der Angreifer nutzt öffentlich zugängliche DNS-Resolver aus, um DNS-Anfragen mit gefälschter Absenderadresse an das Ziel zu senden und so den Traffic zu verstärken.
    - **Schutzmaßnahmen (für die Opferseite):**
        - **Firewall-Konfiguration:** Firewalls können eingesetzt werden, um verdächtigen Traffic zu filtern und DoS-Angriffe zu mitigieren (Rate-Limiting, SYN-Cookies, etc.).
        - **Intrusion Detection/Prevention Systeme (IDS/IPS):** IDS/IPS können DoS-Angriffe erkennen und abwehren.
        - **DDoS-Protection-Dienste:** Spezielle Dienste von Drittanbietern, die vor großflächigen DDoS-Angriffen schützen können (oft für Webserver und Online-Dienste).
- **WLAN-Angriffe (Wi-Fi Hacking):**
    
    - **Prinzip:** Das Ausnutzen von Schwachstellen in WLAN-Protokollen oder -Konfigurationen, um unbefugten Zugriff zu erlangen oder Denial-of-Service zu verursachen.
    - **OpenWrt Rolle:** OpenWrt bietet eine exzellente Plattform für WLAN-Angriffe, da es die notwendigen Treiber und Werkzeuge unterstützt und den Wechsel des WLAN-Chips in den "Monitor Mode" (für das Abfangen von WLAN-Paketen) ermöglicht.
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `aircrack-ng suite`: Eine umfassende Sammlung von Werkzeugen für WLAN-Auditing und -Angriffe (z.B. `airodump-ng` für das Abfangen von Paketen, `aireplay-ng` für Deauthentication-Angriffe, `aircrack-ng` für das Knacken von WLAN-Passwörtern).
        - `reaver`: Ein Werkzeug, um WPS (Wi-Fi Protected Setup) PINs zu brute-forcen und so unter Umständen das WLAN-Passwort zu erlangen (WPS ist als unsicher bekannt und sollte deaktiviert werden).
    - **Angriffstechniken (beispielhaft):**
        - **Wi-Fi Deauthentication Angriff:** Der Angreifer sendet Deauthentifizierungs-Pakete, um Geräte aus dem WLAN zu werfen oder die Handshake-Prozedur (für das Knacken von Passwörtern) zu erzwingen.
        - **WLAN-Passwort-Cracking:** Abfangen des "Handshake" (4-Way-Handshake) beim Verbindungsaufbau eines Gerätes mit dem WLAN und anschließendes Offline-Knacken des WLAN-Passworts mit Wörterbuch- oder Brute-Force-Attacken (Tools wie `aircrack-ng`).
        - **Rogue Access Point (Evil Twin Attack):** Der Angreifer setzt einen gefälschten WLAN-Access-Point mit dem gleichen Namen (SSID) wie ein legitimes WLAN auf, um Benutzer anzulocken und deren Datenverkehr abzufangen.
    - **Schutzmaßnahmen (für WLAN-Betreiber):**
        - **Starke WLAN-Verschlüsselung (WPA3):** WPA3 ist deutlich sicherer als WPA2 und sollte verwendet werden, wenn alle Geräte es unterstützen.
        - **Starkes und zufälliges WLAN-Passwort:** Ein langes, komplexes Passwort ist schwerer zu knacken.
        - **WPS deaktivieren:** WPS ist unsicher und sollte grundsätzlich deaktiviert werden.
        - **MAC-Adressfilterung (mit Vorsicht):** MAC-Adressfilterung kann eine zusätzliche Hürde darstellen, ist aber leicht zu umgehen und kein wirklich sicherer Schutz.
        - **Regelmäßige Firmware-Updates des Routers:** Sicherheitslücken in der Router-Firmware können ausgenutzt werden.
- **Ausnutzen von Schwachstellen (Exploits):**
    
    - **Prinzip:** Das Suchen und Ausnutzen von bekannten Sicherheitslücken in Netzwerkdiensten, Betriebssystemen oder Anwendungen, um unbefugten Zugriff zu erlangen oder Schaden anzurichten.
    - **OpenWrt Rolle:** OpenWrt kann verwendet werden, um Netzwerk-Scans durchzuführen (z.B. mit `nmap`) und Informationen über offene Ports und Dienste zu sammeln. In Kombination mit Exploits kann OpenWrt dann als Plattform für Angriffe dienen. **Es ist aber unrealistisch, auf einem ressourcenbeschränkten OpenWrt Router komplexe Exploit-Frameworks wie Metasploit laufen zu lassen.** Einfachere Exploits oder Skripte sind aber denkbar.
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `nmap`: Für Portscans und Service-Erkennung.
        - `Metasploit Framework (eher ressourcenhungrig, ggf. eingeschränkt nutzbar):` Ein umfassendes Framework für Penetrationstests und Exploits. Auf ressourcenarmen Routern aber limitiert.
        - Eigene Skripte (z.B. in Python, Bash): Für einfachere Exploits oder Automatisierungen.
    - **Angriffstechniken (beispielhaft):**
        - **Ausnutzung von Buffer Overflows:** Das Ausnutzen von Pufferüberlauf-Schwachstellen in Software, um eigenen Code einzuschleusen und auszuführen.
        - **Ausnutzung von Command Injection Schwachstellen:** Das Einschleusen von Befehlen in eine Anwendung, um diese auf dem System auszuführen.
        - **Ausnutzung von Authentifizierungs-Bypässen:** Das Umgehen von Authentifizierungsmechanismen, um unbefugten Zugriff zu erlangen.
    - **Schutzmaßnahmen (für Systemadministratoren):**
        - **Regelmäßige Sicherheitsupdates für alle Systeme und Geräte:** Schließen bekannter Sicherheitslücken.
        - **Härtung von Systemen und Diensten:** Deaktivierung unnötiger Dienste, starke Passwörter, restriktive Konfigurationen.
        - **Intrusion Detection/Prevention Systeme (IDS/IPS):** Erkennen und Abwehren von Exploits und Angriffen.
        - **Regelmäßige Penetrationstests und Sicherheitsaudits:** Identifizieren von Schwachstellen in der eigenen Infrastruktur.

**B. Ausspionieren (Surveillance Nutzung):**

Ein OpenWrt Router kann auch für verschiedene Formen der Überwachung und des Ausspionierens missbraucht werden. **Auch hier gilt der dringende Hinweis: Unbefugte Überwachung ist illegal und ethisch inakzeptabel.**

- **Traffic-Analyse und -Mitschnitt (Sniffing):**
    
    - **Prinzip:** Das Abfangen und Analysieren des Netzwerkverkehrs, um Informationen über die Kommunikation, das Verhalten und die Daten der Netzwerk-Nutzer zu gewinnen.
    - **OpenWrt Rolle:** OpenWrt ermöglicht das Abfangen des Datenverkehrs (z.B. im Promiscuous Mode auf WLAN oder durch MITM-Positionierung). Es bietet auch die Möglichkeit, Werkzeuge zur Analyse und Speicherung des Traffics zu installieren.
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `tcpdump`: Ein Kommandozeilen-Tool zum Abfangen von Netzwerkpaketen. Sehr mächtig und flexibel. Die Rohdaten der Pakete können aufgezeichnet und später analysiert werden.
        - `wireshark (tshark - Kommandozeilenversion):` Die Kommandozeilenversion von Wireshark (`tshark`) kann unter OpenWrt laufen und für detaillierte Protokollanalyse verwendet werden. Das grafische Wireshark ist auf den meisten Routern zu ressourcenhungrig.
        - `ngrep`: Ein Tool zum Durchsuchen des Netzwerkverkehrs nach Mustern (ähnlich `grep` für Dateien).
        - `iftop/iptraf`: Tools zur Echtzeit-Überwachung des Netzwerk-Traffics (Bandbreitennutzung pro Verbindung, Protokollverteilung etc.).
    - **Analyse-Möglichkeiten (beispielhaft):**
        - **Metadaten-Analyse:** Erfassung von Informationen über Kommunikationspartner, Zeitpunkte, Protokolle, Ports, übertragene Datenmengen (z.B. wer kommuniziert mit wem, wann, wie oft, wie lange).
        - **Content-Analyse (bei unverschlüsselten Verbindungen):** Das Mitlesen unverschlüsselter Inhalte, z.B. von HTTP-Webseiten, unverschlüsselten E-Mails, FTP-Übertragungen. **Bei HTTPS-verschlüsselten Verbindungen ist die Inhaltsanalyse ohne Weiteres nicht möglich.**
        - **Erstellung von Benutzerprofilen:** Die gesammelten Daten können verwendet werden, um Profile über das Surfverhalten, Kommunikationsmuster und Interessen der Nutzer zu erstellen.
    - **Ethische und rechtliche Grenzen:**
        - **Unbefugtes Abfangen und Analysieren des Datenverkehrs Dritter ist in den meisten Rechtsordnungen illegal und eine Verletzung der Privatsphäre.**
        - **In vielen Ländern gibt es Gesetze zum Datenschutz und zur Telekommunikationsüberwachung, die solche Aktivitäten verbieten.**
        - **Auch im privaten Kontext (z.B. Überwachung von Familienmitgliedern ohne deren Wissen) ist dies ethisch höchst fragwürdig und kann rechtliche Konsequenzen haben.**
    - **Schutzmaßnahmen (gegen Traffic-Analyse):**
        - **Ende-zu-Ende-Verschlüsselung:** Verwendung von HTTPS für Webseiten, verschlüsselten E-Mails (z.B. PGP/GPG), verschlüsselten Messaging-Diensten (z.B. Signal, WireGuard).
        - **VPN-Nutzung:** Ein VPN verschlüsselt den gesamten Datenverkehr zwischen dem Gerät und dem VPN-Server und schützt so vor lokaler Traffic-Analyse.
        - **Tor-Netzwerk:** Tor anonymisiert die Internetverbindung und erschwert die Rückverfolgung des Datenverkehrs.
- **Log-Analyse und -Speicherung (Erweiterte Logging-Funktionen):**
    
    - **Prinzip:** OpenWrt bietet standardmäßig Logging-Funktionen (Syslog). Diese können erweitert werden, um detailliertere Informationen über Netzwerkereignisse, Benutzeraktivitäten und Systemzustände zu protokollieren und zu speichern.
    - **OpenWrt Rolle:** OpenWrt ermöglicht die Installation erweiterter Logging-Systeme und die Konfiguration detaillierter Log-Regeln. Logs können lokal auf dem Router gespeichert oder an einen externen Server (Syslog-Server) übertragen werden.
    - **Beispiel-Tools (unter OpenWrt installierbar):**
        - `syslog-ng` oder `rsyslog`: Erweiterte Syslog-Implementierungen mit mehr Funktionen und Konfigurationsmöglichkeiten als das Standard-Syslog.
        - `logrotate`: Tool zur automatischen Rotation und Archivierung von Logdateien, um den Speicherplatzverbrauch zu kontrollieren.
        - `Elasticsearch, Graylog, Loki (in komplexeren Szenarien mit externem Server):` Tools für zentrale Log-Verwaltung, -Analyse und -Visualisierung, wenn Logs von mehreren OpenWrt Routern oder anderen Systemen gesammelt werden sollen (eher für professionelle Umgebungen).
    - **Protokollierbare Informationen (beispielhaft):**
        - **Netzwerkverbindungen (Connections Logs):** Protokollierung von Verbindungsaufbauten und -abbauen (Source-IP, Ziel-IP, Ports, Protokolle). Kann verwendet werden, um Netzwerkaktivitäten nachzuvollziehen.
        - **DNS-Abfragen (DNS Query Logs):** Protokollierung von DNS-Anfragen. Kann Einblicke in das Surfverhalten der Nutzer geben (welche Domains werden aufgerufen?).
        - **Firewall-Ereignisse (Firewall Logs):** Protokollierung von geblockten und erlaubten Firewall-Regeln. Kann Angriffsversuche oder unerwünschten Traffic aufzeigen.
        - **System-Logs (System Logs):** Protokollierung von Systemereignissen, Fehlermeldungen, Benutzer-Logins etc. Für die Fehlersuche und Systemüberwachung nützlich, kann aber auch für die Überwachung von Benutzeraktivitäten missbraucht werden.
    - **Ethische und rechtliche Grenzen:**
        - **Vorratsdatenspeicherung (Data Retention) ist in vielen Ländern rechtlich stark eingeschränkt oder verboten.** Das unbefugte Protokollieren und Speichern von Kommunikationsdaten über einen längeren Zeitraum ist illegal und eine Verletzung der Privatsphäre.
        - **Auch hier gilt: Die Überwachung von Nutzern ohne deren Wissen und Zustimmung ist ethisch fragwürdig und kann rechtliche Konsequenzen haben.**
    - **Schutzmaßnahmen (gegen übermäßige Protokollierung):**
        - **Datenschutzrichtlinien und -gesetze beachten:** Sich über die rechtlichen Rahmenbedingungen informieren und diese einhalten.
        - **Transparenz und Zustimmung:** Nutzer transparent über die Protokollierung informieren und deren Zustimmung einholen (wenn rechtlich und ethisch erforderlich/sinnvoll).
        - **Datenminimierung:** Nur die wirklich notwendigen Daten protokollieren.
        - **Anonymisierung und Pseudonymisierung:** Personenbezogene Daten anonymisieren oder pseudonymisieren, wo möglich.
        - **Begrenzung der Speicherdauer:** Logdaten nur so lange speichern wie unbedingt notwendig und danach sicher löschen.
- **Installation von Malware (als hypothetisches Szenario – ethisch und legal inakzeptabel):**
    
    - **Prinzip:** OpenWrt Router könnten, wenn kompromittiert oder absichtlich manipuliert, als Plattform für die Verbreitung oder Ausführung von Malware dienen. Dies ist ein **äußerst gefährliches und illegales Szenario.**
    - **OpenWrt Rolle:** OpenWrt bietet die Flexibilität, beliebige Software zu installieren und auszuführen. Ein Angreifer könnte OpenWrt nutzen, um Malware auf dem Router zu installieren und von dort aus in das lokale Netzwerk einzudringen oder Angriffe zu starten. Dies ist aber eher ein **hypothetisches Szenario für fortgeschrittene Angriffe** und erfordert bereits Kompromittierung des Routers oder des Firmware-Images. Ein Standard-OpenWrt Router ist **nicht per se mit Malware vorinstalliert.**
    - **Beispiel-Malware (rein hypothetisch):**
        - **Backdoors:** Installation von Backdoors, um einen versteckten Zugang zum Router und zum Netzwerk zu ermöglichen.
        - **Keylogger:** Aufzeichnung von Tastatureingaben (eher unrealistisch auf einem Router, aber theoretisch denkbar, wenn administrative Oberflächen oder SSH-Zugänge abgefangen werden sollen).
        - **Botnet-Clients:** Der Router wird Teil eines Botnetzes und für DDoS-Angriffe oder andere illegale Aktivitäten missbraucht.
        - **Traffic-Redirector/Proxy:** Der Router wird als Proxy missbraucht, um den Traffic anderer Nutzer umzuleiten und zu manipulieren.
    - **Schutzmaßnahmen (gegen Malware-Infektion):**
        - **Sichere Firmware-Quelle verwenden:** OpenWrt Firmware nur von offiziellen und vertrauenswürdigen Quellen herunterladen und installieren.
        - **Firmware-Image auf Integrität prüfen:** Vor der Installation die Checksummen (SHA256, etc.) des Firmware-Images überprüfen, um sicherzustellen, dass es nicht manipuliert wurde.
        - **Starkes Root-Passwort setzen:** Verhindert unbefugten Zugriff auf den Router und die Installation von Malware.
        - **Firewall-Konfiguration:** Eine restriktive Firewall-Konfiguration kann das Eindringen von Malware erschweren.
        - **Regelmäßige Firmware-Updates:** Sicherheitslücken in der Firmware schließen.
        - **Regelmäßige Überprüfung des Routers:** Auf verdächtige Prozesse, ungewöhnlichen Netzwerkverkehr oder unbekannte Softwarepakete achten.

**Wichtiger abschließender Hinweis zur Legalität und Ethik:**

Ich möchte nochmals **dringend** darauf hinweisen, dass die hier dargestellten Informationen **ausschließlich zu Bildungs- und Demonstrationszwecken** dienen. Der **unbefugte Einsatz** von OpenWrt Routern oder den beschriebenen Techniken für Angriffe und Ausspähungen ist **illegal und ethisch absolut inakzeptabel**.

**Jegliche Nutzung von OpenWrt oder diesen Informationen für illegale oder unethische Zwecke liegt in der alleinigen Verantwortung des Nutzers.** Ich übernehme keine Haftung für Schäden oder rechtliche Konsequenzen, die aus einem Missbrauch dieser Informationen entstehen.

**OpenWrt sollte verantwortungsvoll und im Einklang mit den Gesetzen und ethischen Grundsätzen eingesetzt werden.** Im professionellen Kontext (z.B. Penetrationstests, Security Audits) dürfen solche Techniken nur mit ausdrücklicher Genehmigung der betroffenen Parteien und im Rahmen klar definierter und legaler Aufträge eingesetzt werden.

**Statt für Angriffe und Ausspähungen kann OpenWrt auch hervorragend für die Verbesserung der eigenen Netzwerksicherheit und den Schutz der Privatsphäre eingesetzt werden.** Viele der oben genannten Werkzeuge und Techniken können in abgewandelter Form auch für defensive Zwecke genutzt werden, z.B. zur Erkennung von Angriffen im eigenen Netzwerk (Intrusion Detection), zur Analyse des eigenen Netzwerkverkehrs (Network Monitoring) oder zur Härtung der eigenen Router-Konfiguration.


MAn in The middel atacke Beispiel 

Diese Anleitung demonstriert eine einfache ARP-Spoofing-basierte MITM-Attacke, um unverschlüsselten HTTP-Traffic abzufangen und zu visualisieren.

**Voraussetzungen:**

- **OpenWrt Router:** Ein Router, auf dem OpenWrt installiert ist. Stellen Sie sicher, dass Ihr Router ausreichend Ressourcen (CPU, RAM, Speicher) für die benötigten Tools hat.
- **Zielnetzwerk:** Ein Netzwerk, in dem Sie die Demonstration durchführen können (idealerweise ein isoliertes Testnetzwerk).
- **Zielgerät:** Ein Gerät im Zielnetzwerk, dessen Traffic Sie abfangen möchten (z.B. ein Laptop oder ein Smartphone). Sie benötigen die IP-Adresse dieses Geräts.
- **Gateway-IP-Adresse:** Die IP-Adresse des Gateways (üblicherweise Ihr OpenWrt Router selbst oder ein anderer Router im Netzwerk).
- **WLAN-Adapter mit Monitor-Modus-Unterstützung (optional, für WLAN-basierte Angriffe):** Wenn Sie die Attacke über WLAN durchführen möchten, benötigen Sie einen WLAN-Adapter, der den Monitor-Modus unterstützt. In dieser Anleitung wird ein kabelgebundenes Szenario angenommen, um die Komplexität zu reduzieren.
- **Ethernet-Kabel:** Für die Verbindung Ihres Computers mit dem OpenWrt Router und idealerweise für eine kabelgebundene Verbindung zwischen dem OpenWrt Router und dem Zielnetzwerk/Zielgerät für eine stabilere Testumgebung.
- **Computer mit SSH-Client:** Um sich mit dem OpenWrt Router zu verbinden und Befehle auszuführen.

**Schritte:**

**1. Software auf OpenWrt installieren:**

Verbinden Sie sich per SSH mit Ihrem OpenWrt Router (z.B. über PuTTY oder den Terminal). Aktualisieren Sie zuerst die Paketlisten und installieren Sie die benötigten Tools: `ettercap` (ein vielseitiges MITM-Framework) und `driftnet` (um Bilder aus unverschlüsselten Webseiten zu extrahieren, als visuelle Demonstration).

Bash

```
opkg update
opkg install ettercap driftnet
```

**2. Netzwerk-Interface identifizieren:**

Finden Sie heraus, welches Interface Ihr LAN-Interface ist, über das der Datenverkehr in Ihrem lokalen Netzwerk läuft. Dies ist normalerweise `br-lan` oder `eth0` (oder ähnlich, abhängig von Ihrer OpenWrt Konfiguration). Sie können `ifconfig` oder `ip addr` verwenden, um die Interfaces aufzulisten. In den folgenden Befehlen verwenden wir `<interface>` als Platzhalter für Ihr LAN-Interface (z.B. `br-lan`).

**3. ARP-Spoofing mit Ettercap starten:**

Wir verwenden `ettercap` für ARP-Spoofing. ARP-Spoofing manipuliert die ARP-Tabellen im Netzwerk, um den Traffic des Zielgeräts über unseren OpenWrt Router umzuleiten.

Ersetzen Sie `<interface>`, `<ziel_ip>` (IP-Adresse des Zielgeräts) und `<gateway_ip>` (IP-Adresse des Gateways) in dem folgenden Befehl mit den entsprechenden Werten für Ihr Netzwerk.

Bash

```
ettercap -Tq -M arp:remote -i <interface> /<ziel_ip>// /<gateway_ip>//
```

- **`ettercap -Tq`**: Startet Ettercap im Textmodus (`-T`) und im Quiet-Modus (`-q`, unterdrückt ausführliche Ausgaben).
- **`-M arp:remote`**: Aktiviert den ARP-Spoofing-MITM-Angriff (`-M arp`) im "remote" Modus (Spoofing zwischen zwei Hosts).
- **`-i <interface>`**: Gibt das Netzwerk-Interface an, das für den Angriff verwendet werden soll (Ihr LAN-Interface).
- **`/ <ziel_ip> //`**: Definiert das Zielgerät als Ziel des ARP-Spoofings. Die doppelten Slashes `//` bedeuten, dass Ettercap alle Ports des Zielgeräts abfangen soll.
- **`/ <gateway_ip> //`**: Definiert den Gateway als zweites Ziel des ARP-Spoofings.

**Erläuterung ARP-Spoofing:** Dieser Befehl sendet ARP-Antworten an das Zielgerät und das Gateway, die fälschlicherweise behaupten, dass die MAC-Adresse des OpenWrt Routers sowohl die IP-Adresse des Zielgeräts als auch die IP-Adresse des Gateways repräsentiert. Dadurch wird der Traffic, der eigentlich zum Gateway gehen sollte, zum OpenWrt Router umgeleitet und umgekehrt.

**4. IP-Forwarding auf dem OpenWrt Router aktivieren:**

Standardmäßig leitet ein Router keinen Traffic weiter, der nicht für ihn selbst bestimmt ist. Um den abgefangenen Traffic auch tatsächlich weiterzuleiten (und nicht nur auf dem Router zu behalten und "aufzuhalten"), müssen wir IP-Forwarding aktivieren.

Bash

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Dieser Befehl setzt den Wert der Kernel-Variable `ip_forward` auf 1, was IP-Forwarding aktiviert. Diese Einstellung ist in der Regel **nicht permanent** und geht nach einem Router-Neustart verloren. Für permanente Aktivierung müssten Sie dies in der `/etc/sysctl.conf` konfigurieren oder eine Firewall-Regel hinzufügen. Für diese Demonstration ist das temporäre Aktivieren ausreichend.

**5. Unverschlüsselten HTTP-Traffic abfangen und Bilder mit Driftnet visualisieren (Demonstrationszweck):**

Starten Sie `driftnet` auf dem OpenWrt Router und geben Sie das gleiche Interface `<interface>` an wie beim Ettercap-Befehl.

Bash

```
driftnet -i <interface>
```

`driftnet` fängt nun Bilder ab, die in unverschlüsselten HTTP-Webseiten gefunden werden, die über das angegebene Interface übertragen werden. Die abgefangenen Bilder werden in der Regel in einem separaten Fenster oder im Terminal angezeigt, in dem Sie `driftnet` gestartet haben.

**6. Zielgerät aktivieren und HTTP-Webseiten besuchen (Test):**

Starten Sie auf dem Zielgerät einen Webbrowser und besuchen Sie **unverschlüsselte** HTTP-Webseiten (Webseiten, die **nicht** mit `https://` beginnen, sondern mit `http://`). **Moderne Webseiten nutzen in der Regel HTTPS, daher wird diese Demonstration bei vielen Webseiten keine Bilder anzeigen.** Suchen Sie nach Webseiten, die bekanntermaßen noch HTTP verwenden (z.B. ältere Webseiten oder Testseiten).

Wenn die MITM-Attacke erfolgreich ist und Sie HTTP-Webseiten auf dem Zielgerät besuchen, sollten Sie in dem Fenster, in dem `driftnet` läuft, Bilder sehen, die von diesen Webseiten extrahiert wurden. Dies ist eine visuelle Bestätigung, dass der Traffic des Zielgeräts abgefangen und analysiert wird.

**7. Angriff stoppen:**

Um den ARP-Spoofing-Angriff zu stoppen, beenden Sie den `ettercap`-Prozess im SSH-Terminal durch Drücken von `Strg+C`. Beenden Sie auch `driftnet` mit `Strg+C`.

Deaktivieren Sie optional IP-Forwarding wieder:

Bash

```
echo 0 > /proc/sys/net/ipv4/ip_forward
```

**Wichtige ethische und rechtliche Hinweise (Wiederholung und Verstärkung):**

- **Diese Anleitung dient ausschließlich zu Demonstrations- und Lehrzwecken in einer kontrollierten Umgebung.**
- **Führen Sie diese Schritte niemals ohne ausdrückliche Genehmigung im Netzwerk Dritter oder gegen Geräte durch, für die Sie keine Erlaubnis haben.**
- **MITM-Angriffe sind illegal und ethisch nicht vertretbar, wenn sie unbefugt durchgeführt werden.**
- **Missbrauch dieser Informationen kann zu rechtlichen Konsequenzen führen.**
- **Seien Sie sich der Verantwortung bewusst und verwenden Sie diese Informationen nur für legale und ethische Zwecke, wie z.B. zur Verbesserung Ihrer eigenen Netzwerksicherheit oder im Rahmen von Penetrationstests mit Genehmigung.**

**Zusätzliche Hinweise für tiefergehende Analysen und erweiterte Szenarien (für fortgeschrittene Nutzer, nur für ethische Zwecke):**

- **Paket-Analyse mit Wireshark (tshark):** Anstatt `driftnet` für eine einfache visuelle Demonstration zu verwenden, könnten Sie den abgefangenen Traffic mit `tcpdump` aufzeichnen (`tcpdump -i <interface> -w mitm.pcap`) und die resultierende `mitm.pcap`-Datei mit Wireshark (oder `tshark` auf der Kommandozeile des OpenWrt Routers, wenn ausreichend Ressourcen vorhanden sind) detailliert analysieren. Dies ermöglicht eine umfassendere Untersuchung des Datenverkehrs und die Identifizierung von verschiedenen Protokollen, unverschlüsselten Daten etc.
- **HTTPS-Traffic und SSL-Stripping (mit Einschränkungen):** Moderne Webseiten verwenden fast ausschließlich HTTPS, um den Traffic zu verschlüsseln. Einfaches ARP-Spoofing und `driftnet` funktionieren bei HTTPS-Verbindungen nicht, da der Inhalt verschlüsselt ist. Für Demonstrationszwecke könnten Sie ältere Webseiten suchen, die noch HTTP verwenden, oder – **nur zu Lehrzwecken und in einer _sehr_ kontrollierten Umgebung mit _expliziter Genehmigung_** – Techniken wie SSL-Stripping (mit Tools wie `sslstrip` oder `mitmf`) demonstrieren. **Beachten Sie jedoch, dass SSL-Stripping durch moderne Browser und HSTS (HTTP Strict Transport Security) stark erschwert wird und in realen Szenarien oft nicht mehr funktioniert oder leicht erkennbar ist.** Es ist wichtig zu verstehen, dass SSL-Stripping **keine zuverlässige Methode ist, um HTTPS-Verschlüsselung zu brechen**, sondern eher eine Demonstration historischer Schwachstellen darstellt. **Die moderne Empfehlung ist immer, auf HTTPS zu vertrauen und es als sicheren Schutzmechanismus zu betrachten.**
- **Erweiterte MITM-Frameworks (wie `mitmf` oder `bettercap`):** Für komplexere MITM-Szenarien und Angriffe können Sie Frameworks wie `mitmf` (Man-in-the-middle framework) oder `bettercap` auf OpenWrt installieren. Diese Frameworks bieten eine Vielzahl von Modulen und Optionen für verschiedene Angriffsarten (z.B. Browser-Hijacking, Credential Sniffing, etc.). Die Installation und Konfiguration dieser Frameworks ist jedoch anspruchsvoller und erfordert ein tieferes Verständnis der Materie.




Wi-Fi Hacking mit OpenWrt


**Voraussetzungen:**

- **OpenWrt Router:** Ein Router, auf dem OpenWrt installiert ist. Stellen Sie sicher, dass Ihr Router über einen WLAN-Chip verfügt, der den Monitor-Modus unterstützt und genügend Ressourcen (CPU, RAM, Speicher) für die benötigten Tools hat.
- **Kompatibler WLAN-Adapter mit Monitor-Modus-Unterstützung (falls der interne WLAN-Chip nicht geeignet ist oder für fortgeschrittene Angriffe):** Einige interne WLAN-Chips von Routern unterstützen den Monitor-Modus nicht vollständig oder optimal. In diesem Fall benötigen Sie einen externen USB-WLAN-Adapter, der den Monitor-Modus und Packet Injection unterstützt. Beliebte Chipsätze sind Atheros AR9271 oder Ralink RT3070/RT5370/MT7601. Überprüfen Sie die Kompatibilität Ihres Adapters mit Aircrack-ng und OpenWrt.
- **Ziel-WLAN-Netzwerk:** Ein WLAN-Netzwerk, für das Sie die Erlaubnis haben, Penetrationstests durchzuführen (idealerweise Ihr eigenes Test-WLAN).
- **Zielgerät im WLAN (optional, aber hilfreich für die Demonstration):** Ein Gerät, das mit dem Ziel-WLAN verbunden ist, um den Handshake-Prozess zu beobachten und zu beschleunigen.
- **Computer mit SSH-Client:** Um sich mit dem OpenWrt Router zu verbinden und Befehle auszuführen.
- **Wortliste (Wordlist):** Eine Wortliste mit potenziellen WLAN-Passwörtern. Für Demonstrationszwecke können Sie kleine Beispiel-Wortlisten verwenden, aber für realistische Szenarien benötigen Sie umfangreichere Wortlisten (z.B. RockYou, oder selbst generierte Listen). Sie können Wortlisten auf dem OpenWrt Router speichern oder von einem externen Speicherort abrufen (beachten Sie den begrenzten Speicherplatz auf Routern). Alternativ können Sie die Wortliste auf einem separaten Computer erstellen und für den Cracking-Prozess zum OpenWrt Router übertragen (oder den Cracking-Prozess auf einem leistungsfähigeren Computer durchführen, wenn gewünscht – in dieser Anleitung demonstrieren wir das Cracking direkt auf dem OpenWrt Router).
- **Kontrollierte Testumgebung:** Es ist **absolut notwendig**, diese Demonstration in einer kontrollierten Umgebung durchzuführen, in der Sie die volle Kontrolle über das Netzwerk und die Geräte haben und die ausdrückliche Genehmigung aller Beteiligten vorliegt.

**Schritte:**

**1. Software auf OpenWrt installieren:**

Verbinden Sie sich per SSH mit Ihrem OpenWrt Router (z.B. über PuTTY oder das Terminal). Aktualisieren Sie zuerst die Paketlisten und installieren Sie die Aircrack-ng Suite, die die notwendigen Tools für WLAN-Angriffe enthält.

Bash

```
opkg update
opkg install aircrack-ng
```

**2. WLAN-Interface in den Monitor-Modus versetzen:**

Um WLAN-Pakete abfangen zu können, muss das WLAN-Interface in den "Monitor-Modus" versetzt werden. Verwenden Sie das Tool `airmon-ng` aus der Aircrack-ng Suite, um dies zu tun.

Zuerst müssen Sie den Namen Ihres WLAN-Interfaces herausfinden. Verwenden Sie den Befehl `iw dev` oder `iwconfig`. Der Interface-Name ist typischerweise `wlan0`, `wlan0-1`, `phy0-ap0` oder ähnlich, abhängig von Ihrem Router-Modell und der OpenWrt Konfiguration. In dieser Anleitung verwenden wir `<wlan_interface>` als Platzhalter für Ihren WLAN-Interface-Namen (z.B. `wlan0`).

Um den Monitor-Modus zu aktivieren, verwenden Sie den Befehl `airmon-ng start <wlan_interface>`:

Bash

```
airmon-ng start <wlan_interface>
```

Beispiel: `airmon-ng start wlan0`

Der Befehl `airmon-ng start` erstellt in der Regel ein neues Monitor-Interface, dessen Name typischerweise `wlan0mon`, `mon0` oder ähnlich ist. `airmon-ng` gibt den genauen Namen des neuen Monitor-Interfaces aus. Notieren Sie sich diesen Namen. In den folgenden Schritten verwenden wir `<monitor_interface>` als Platzhalter für den Namen Ihres Monitor-Interfaces (z.B. `wlan0mon`).

**3. WLAN-Netzwerke in der Umgebung scannen:**

Verwenden Sie das Tool `airodump-ng` aus der Aircrack-ng Suite, um WLAN-Netzwerke in Ihrer Umgebung zu scannen und Informationen über diese Netzwerke zu sammeln.

Bash

```
airodump-ng <monitor_interface>
```

Beispiel: `airodump-ng wlan0mon`

`airodump-ng` startet nun den Scan und zeigt eine Liste der gefundenen WLAN-Netzwerke (Access Points) und der mit ihnen verbundenen Geräte (Clients) in Echtzeit an.

[![Bildmotiv: Airodumpng scanning output](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSEEdNj25lH4HNi1S-Q93lS8OvwoHbtpKAi6cNRjOpSOq4j-3qsvIb_u6Gy2ErH)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Results-of-a-scan-using-Airodump-ng_fig2_327563071)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Results-of-a-scan-using-Airodump-ng_fig2_327563071)

Airodumpng scanning output

Die Ausgabe von `airodump-ng` ist in zwei Bereiche unterteilt:

- **BSSID, PWR, Beacons, #Data, CH, ENC, CIPHER, AUTH, ESSID:** Informationen über die Access Points (WLAN-Netzwerke).
    
    - **BSSID:** Die MAC-Adresse des Access Points. Dies ist die eindeutige Kennung des WLAN-Netzwerks.
    - **PWR:** Signalstärke des Access Points (je höher der Wert, desto besser das Signal).
    - **Beacons:** Anzahl der Beacon-Pakete, die vom Access Point gesendet wurden.
    - **#Data:** Anzahl der Data-Pakete, die von Clients im Netzwerk aufgezeichnet wurden.
    - **CH:** WLAN-Kanal, auf dem der Access Point sendet.
    - **ENC:** Verschlüsselungstyp (z.B. OPN = offen, WEP, WPA, WPA2, WPA3). Wir konzentrieren uns hier auf WPA2.
    - **CIPHER:** Verschlüsselungsalgorithmus (z.B. CCMP, TKIP).
    - **AUTH:** Authentifizierungsmethode (z.B. PSK für Pre-Shared Key – das typische Passwort-basierte WLAN).
    - **ESSID:** Der WLAN-Name (SSID – Service Set Identifier), der Name des WLAN-Netzwerks, den Sie in der WLAN-Liste sehen.
- **BSSID, STATION, PWR, Rate, Lost, Packets, Probes:** Informationen über die mit den Access Points verbundenen Clients (WLAN-Geräte).
    
    - **BSSID:** Die BSSID des Access Points, mit dem der Client verbunden ist. `(not associated)` bedeutet, dass der Client noch nicht mit einem Access Point verbunden ist oder nur Probe Requests sendet.
    - **STATION:** Die MAC-Adresse des WLAN-Clients.
    - **PWR:** Signalstärke des Clients (vom Access Point aus gesehen).
    - **Rate:** Übertragungsrate.
    - **Lost:** Paketverluste.
    - **Packets:** Anzahl der Pakete, die von diesem Client aufgezeichnet wurden.
    - **Probes:** ESSIDs, nach denen der Client sucht (Probe Requests).

Lassen Sie `airodump-ng` einige Zeit laufen, um eine gute Übersicht über die WLAN-Netzwerke in Ihrer Umgebung zu bekommen.

**4. Ziel-WLAN-Netzwerk auswählen und Informationen notieren:**

Identifizieren Sie in der `airodump-ng`-Ausgabe Ihr Ziel-WLAN-Netzwerk (das Netzwerk, für das Sie die Erlaubnis zum Testen haben). Notieren Sie sich folgende Informationen für das Zielnetzwerk:

- **BSSID:** Die MAC-Adresse des Access Points (wichtig für die gezielte Erfassung des Handshakes und das Cracking).
- **CH:** Der Kanal des Access Points (wichtig, um `airodump-ng` auf den richtigen Kanal zu setzen).
- **ESSID:** Der WLAN-Name (optional, dient zur Identifizierung).

**5. Airodump-ng gezielt auf das Zielnetzwerk und den Kanal starten:**

Um die Datenerfassung zu optimieren und unnötigen Traffic aus anderen Netzwerken zu vermeiden, starten Sie `airodump-ng` erneut, diesmal gezielt auf das Zielnetzwerk und den Kanal.

Verwenden Sie die Optionen `-c <kanal>` (Kanal des Zielnetzwerks) und `--bssid <bssid>` (BSSID des Zielnetzwerks) und geben Sie einen Dateinamen für die Aufzeichnung der Daten an (z.B. `capture-01`). **Wichtig:** Lassen Sie die Dateiendung `.cap` weg, `airodump-ng` fügt diese automatisch hinzu.

Bash

```
airodump-ng -c <kanal> --bssid <bssid> -w capture <monitor_interface>
```

Ersetzen Sie `<kanal>`, `<bssid>`, `capture` und `<monitor_interface>` mit den entsprechenden Werten.

Beispiel: `airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon`

`airodump-ng` beginnt nun, Datenpakete vom Ziel-WLAN-Netzwerk auf Kanal `<kanal>` aufzuzeichnen und in Dateien mit dem Präfix `capture-01` (z.B. `capture-01.cap`, `capture-01.csv`, `capture-01.kismet.netxml`) zu speichern. Es zeigt weiterhin Informationen in Echtzeit an, aber jetzt gefiltert auf das Zielnetzwerk.

**6. Handshake erfassen (optional, aber dringend empfohlen für eine schnellere Demonstration):**

Um das WLAN-Passwort zu knacken, benötigen Sie den "Handshake" (genauer gesagt den 4-Way-Handshake). Der Handshake ist ein 4-Paket-Austausch, der stattfindet, wenn ein Client sich neu mit dem WLAN-Netzwerk verbindet. `aircrack-ng` benötigt diesen Handshake, um das Passwort offline zu knacken.

In vielen Fällen erfasst `airodump-ng` den Handshake automatisch irgendwann, besonders wenn neue Geräte sich mit dem Netzwerk verbinden oder bestehende Verbindungen neu aushandeln. In der `airodump-ng`-Ausgabe (im oberen Bereich, unter "BSSID") wird in der Spalte **"WPA handshake"** `<BSSID>` angezeigt, sobald der Handshake erfasst wurde.

Um den Handshake-Erfassungsprozess zu beschleunigen (für Demonstrationszwecke), können Sie einen **Deauthentication-Angriff** starten, um ein verbundenes Gerät (Client) kurzzeitig vom WLAN zu trennen. Wenn sich das Gerät automatisch wieder verbindet, wird idealerweise der Handshake erfasst. **Verwenden Sie Deauthentication-Angriffe nur in Ihrer eigenen Testumgebung und nur für Demonstrationszwecke, da sie in realen Szenarien als störend wahrgenommen werden können und unter Umständen auffällig sind.**

Um einen Deauthentication-Angriff zu starten, verwenden Sie das Tool `aireplay-ng` mit der Option `-0` (Deauthentication). Sie benötigen die BSSID des Access Points (`<bssid>`) und die MAC-Adresse des Clients (`<client_mac>`). Wenn Sie keinen spezifischen Client angeben möchten, können Sie `-a <bssid> -0 1` verwenden, um Deauthentication-Pakete an alle Geräte im Netzwerk zu senden (Broadcast Deauth). Dies ist aber weniger zielgerichtet. Es ist besser, einen spezifischen Client anzugeben, wenn in der `airodump-ng`-Ausgabe Clients unter "STATION" aufgelistet werden.

Öffnen Sie ein **zweites SSH-Terminal-Fenster** zum OpenWrt Router (lassen Sie `airodump-ng` im ersten Fenster weiterlaufen und Daten aufzeichnen). Führen Sie im **zweiten Terminal** den `aireplay-ng`-Befehl aus.

Bash

```
aireplay-ng -0 1 -a <bssid> -c <client_mac> <monitor_interface>
```

Ersetzen Sie `<bssid>`, `<client_mac>` (falls Sie einen spezifischen Client deauthentifizieren möchten) und `<monitor_interface>` mit den entsprechenden Werten. Wenn Sie einen Broadcast Deauth durchführen möchten (weniger zielgerichtet, aber für Demos manchmal einfacher, wenn kein Client direkt beobachtet wird):

Bash

```
aireplay-ng -0 1 -a <bssid> <monitor_interface>
```

Beispiel (Client-spezifisch): `aireplay-ng -0 1 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon`

Beispiel (Broadcast Deauth): `aireplay-ng -0 1 -a AA:BB:CC:DD:EE:FF wlan0mon`

- **`-0 1`**: Sendet 1 Deauthentication-Paket (Sie können auch mehr Pakete senden, z.B. `-0 10` für 10 Pakete).
- **`-a <bssid>`**: BSSID des Ziel-Access-Points.
- **`-c <client_mac>`**: MAC-Adresse des Ziel-Clients (optional, für gezielte Deauthentication eines Clients). Wenn weggelassen, wird ein Broadcast Deauth durchgeführt.
- `<monitor_interface>`: Name Ihres Monitor-Interfaces.

Beobachten Sie die `airodump-ng`-Ausgabe im **ersten Terminal-Fenster**. Sobald der Handshake erfolgreich erfasst wurde, sollte in der Spalte **"WPA handshake"** der BSSID des Zielnetzwerks angezeigt werden: `WPA handshake: <BSSID>`

`   [![Bildmotiv: Airodumpng output showing WPA handshake](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcToA66YPgraa8jc-4yTFhcm3kjfQlEfxnMn0AX9QxO2l9h2ZhZUmpgtGV6kfTAX)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Successful-four-way-handshake-packet-capture_fig4_327563071)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Successful-four-way-handshake-packet-capture_fig4_327563071)  Airodumpng output showing WPA handshake     `

.

Sobald der Handshake erfasst ist, können Sie `aireplay-ng` im **zweiten Terminal-Fenster** beenden (mit `Strg+C`). Lassen Sie `airodump-ng` im **ersten Terminal-Fenster** weiterlaufen (oder beenden Sie es auch, wenn Sie keine weiteren Daten erfassen möchten).

**7. WLAN-Passwort mit Aircrack-ng knacken:**

Nun verwenden Sie das Tool `aircrack-ng`, um das WLAN-Passwort offline zu knacken, indem Sie den erfassten Handshake und eine Wortliste verwenden.

Bash

```
aircrack-ng -w <wortliste_pfad> <capture_datei.cap>
```

Ersetzen Sie `<wortliste_pfad>` mit dem **absoluten Pfad** zu Ihrer Wortliste auf dem OpenWrt Router (z.B. `/root/wordlists/meine_wortliste.txt` oder `/mnt/usb-stick/wortliste.txt`, wenn Sie eine Wortliste auf einem USB-Stick haben). Ersetzen Sie `<capture_datei.cap>` mit dem Namen der Capture-Datei, die `airodump-ng` erstellt hat (z.B. `capture-01.cap`).

Beispiel: `aircrack-ng -w /root/wordlists/kleine_wortliste.txt capture-01.cap`

`aircrack-ng` startet nun den Cracking-Prozess und versucht, das WLAN-Passwort zu finden, indem es Passwörter aus der Wortliste gegen den erfassten Handshake testet.

[![Bildmotiv: Aircrackng cracking process](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTtlR5VV88lZ07lhmYuF7tlJIqW9waAbe0xGOjGCj_Wc8Cm-oxzO7VVd8EcdHCH)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Aircrack-ng-cracking-a-WPA2-key_fig3_366999411)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Aircrack-ng-cracking-a-WPA2-key_fig3_366999411)

Aircrackng cracking process

- **`-w <wortliste_pfad>`**: Gibt den Pfad zur Wortliste an.
- `<capture_datei.cap>`: Gibt den Pfad zur Capture-Datei an.

**Wichtige Hinweise zum Cracking-Prozess:**

- **Wortliste Qualität ist entscheidend:** Die Erfolgswahrscheinlichkeit des Cracking-Angriffs hängt stark von der Qualität und dem Umfang Ihrer Wortliste ab. Kleine oder schlecht gewählte Wortlisten werden in den meisten Fällen keine komplexen Passwörter knacken können. Für realistische Szenarien benötigen Sie sehr große und gut zusammengestellte Wortlisten (die aber auch sehr viel Speicherplatz benötigen).
- **Cracking-Zeit:** Das Knacken von WLAN-Passwörtern kann sehr zeitaufwendig sein, von Minuten bis zu Tagen oder sogar Wochen, abhängig von der Passwortstärke, der Wortliste und der Rechenleistung. Ein OpenWrt Router ist in der Regel nicht sehr leistungsstark für rechenintensive Cracking-Aufgaben. Für schnellere Ergebnisse können Sie den Handshake und die Wortliste auf einen leistungsstärkeren Computer übertragen und den Cracking-Prozess dort durchführen (z.B. mit Aircrack-ng auf Kali Linux oder einer GPU-basierten Cracking-Software, falls Sie eine GPU für das Cracking verwenden möchten). In dieser Demonstrationsanleitung führen wir das Cracking der Einfachheit halber direkt auf dem OpenWrt Router durch, was aber für realistische Szenarien oft nicht praktikabel ist.
- **Passwort gefunden (KEY FOUND!) oder nicht gefunden (KEY NOT FOUND):** Wenn `aircrack-ng` das Passwort in der Wortliste findet, zeigt es **"KEY FOUND! [ <WLAN-Passwort> ]"** an und gibt das gefundene Passwort aus. Wenn das Passwort nicht gefunden wird, zeigt es **"KEY NOT FOUND"** an, nachdem die gesamte Wortliste durchprobiert wurde. In diesem Fall können Sie es mit einer größeren oder anderen Wortliste erneut versuchen oder den Angriff abbrechen.

**8. Angriff stoppen und Monitor-Modus deaktivieren:**

Um den Angriff zu stoppen, beenden Sie `aircrack-ng` mit `Strg+C`. Beenden Sie auch `airodump-ng` (falls es noch läuft) mit `Strg+C`.

Deaktivieren Sie den Monitor-Modus auf Ihrem WLAN-Interface wieder mit `airmon-ng stop <monitor_interface>`:

Bash

```
airmon-ng stop <monitor_interface>
```

Beispiel: `airmon-ng stop wlan0mon`

Nachdem Sie den Monitor-Modus deaktiviert haben, kann es sein, dass Ihr ursprüngliches WLAN-Interface (z.B. `wlan0`) wieder aktiviert werden muss. Dies geschieht in der Regel automatisch, oder Sie müssen es manuell in der OpenWrt Webinterface oder über die Kommandozeile reaktivieren (z.B. `wifi up`).

**Wichtige ethische und rechtliche Hinweise (Erneute Verstärkung):**

- **Diese Anleitung dient ausschließlich zu Demonstrations- und Lehrzwecken in einer kontrollierten Umgebung.**
- **Führen Sie diese Schritte niemals ohne ausdrückliche Genehmigung im Netzwerk Dritter oder gegen Geräte durch, für die Sie keine Erlaubnis haben.**
- **Wi-Fi Hacking, insbesondere Passwort-Cracking, ist illegal und ethisch nicht vertretbar, wenn es unbefugt durchgeführt wird.**
- **Missbrauch dieser Informationen kann zu schweren rechtlichen Konsequenzen führen.**
- **Seien Sie sich der Verantwortung bewusst und verwenden Sie diese Informationen nur für legale und ethische Zwecke, wie z.B. zur Verbesserung Ihrer eigenen WLAN-Sicherheit oder im Rahmen von Penetrationstests mit Genehmigung.**
- **Erfolgreiches Knacken eines WLAN-Passworts in dieser Demonstration bedeutet _nicht_, dass WLAN-Verschlüsselung grundsätzlich unsicher ist.** Es zeigt, dass schwache oder häufig verwendete Passwörter ein Sicherheitsrisiko darstellen. **Verwenden Sie immer starke, zufällige und einzigartige Passwörter für Ihr WLAN und aktivieren Sie WPA3-Verschlüsselung, falls Ihre Geräte dies unterstützen.** Deaktivieren Sie WPS, da es bekanntermaßen unsicher ist.

**Zusätzliche Hinweise für weiterführende Studien (nur für ethische Zwecke):**

- **Erweiterte Aircrack-ng Optionen:** Aircrack-ng bietet viele weitere Optionen und Techniken, wie z.B. Brute-Force-Attacken (ohne Wortliste, sehr zeitaufwendig), PTK-Cracking, PMKID-Cracking (für bestimmte Szenarien), und verschiedene Optimierungsoptionen. Lesen Sie die Aircrack-ng Dokumentation für detailliertere Informationen.
- **GPU-basiertes Cracking:** Für schnellere Cracking-Ergebnisse können Sie GPU-basierte Cracking-Software wie Hashcat auf einem leistungsstarken Computer verwenden. Dies erfordert die Übertragung der Capture-Datei auf den Computer, auf dem Hashcat läuft. GPU-Cracking kann die Cracking-Geschwindigkeit im Vergleich zu CPU-basiertem Cracking erheblich beschleunigen.
- **Regenbogen-Tabellen (Rainbow Tables) und Pre-computation:** Für bestimmte Verschlüsselungsarten (WEP, ältere WPA/TKIP) können Regenbogen-Tabellen verwendet werden, um den Cracking-Prozess in bestimmten Fällen zu beschleunigen. Für moderne WPA2/WPA3-PSK mit starken Passwörtern sind Regenbogen-Tabellen jedoch weniger relevant.
- **Social Engineering und Phishing (ergänzend zu technischen Angriffen):** In realen Penetrationstests werden oft auch Social Engineering und Phishing-Techniken eingesetzt, um an WLAN-Passwörter zu gelangen (z.B. gefälschte WLAN-Login-Seiten, Ausnutzung von Benutzerfehlern). Diese Anleitung konzentriert sich jedoch auf den technischen Aspekt des Passwort-Crackings.
