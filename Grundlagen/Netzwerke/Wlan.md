
**WLAN: Funktionsweise im Detail**

WLAN, oder Wireless Local Area Network, ermöglicht die drahtlose Kommunikation in einem lokalen Netzwerkbereich. Statt physischer Kabelverbindungen werden hier Funkwellen genutzt, um Daten zu übertragen. Hier ist die Funktionsweise im Detail:

1. **Grundprinzip: Funkwellen:** WLAN basiert auf dem IEEE 802.11-Standard, der verschiedene Frequenzbänder (2,4 GHz, 5 GHz, 6 GHz) für die Datenübertragung definiert. Geräte senden und empfangen Daten als elektromagnetische Wellen in diesen Frequenzbereichen.
    
2. **Access Point (AP):** Das zentrale Element eines WLANs ist der Access Point (oft auch WLAN-Router genannt, obwohl ein Router noch weitere Funktionen beinhaltet). Der AP fungiert als Basisstation und Schnittstelle zwischen dem drahtlosen und dem kabelgebundenen Netzwerk (z.B. dem Internet-Router).
    
    - **Signalabdeckung:** Der AP sendet WLAN-Signale aus und schafft so eine Funkzelle, die als "Wireless Network" oder "SSID" (Service Set Identifier) identifiziert wird. Geräte innerhalb dieser Funkzelle können sich mit dem WLAN verbinden.
    - **Datenweiterleitung:** Der AP empfängt Daten von drahtlosen Geräten, wandelt sie um und leitet sie ins kabelgebundene Netzwerk weiter (und umgekehrt). Er fungiert als Brücke.
3. **WLAN-Adapter in Geräten:** Geräte, die sich mit einem WLAN verbinden sollen (Laptops, Smartphones, Tablets, IoT-Geräte usw.), benötigen einen WLAN-Adapter. Dieser Adapter ist entweder integriert oder kann extern hinzugefügt werden (z.B. USB-WLAN-Adapter).
    
    - **Signalerkennung und Verbindung:** Der WLAN-Adapter sucht nach verfügbaren WLAN-Netzwerken (SSIDs) in der Umgebung. Der Benutzer wählt ein Netzwerk aus und gibt (falls erforderlich) das WLAN-Passwort (auch WLAN-Schlüssel oder Netzwerkschlüssel genannt) ein, um sich zu authentifizieren und zu verbinden.
    - **Datenübertragung:** Nach erfolgreicher Verbindung tauschen das Gerät und der AP Daten drahtlos aus. Der WLAN-Adapter moduliert die Daten in Funkwellen für den Versand und demoduliert empfangene Funkwellen in digitale Daten.
4. **Netzwerkprotokolle:** Wie in jedem Netzwerk, werden auch im WLAN Netzwerkprotokolle verwendet, um die Datenübertragung zu organisieren und sicherzustellen. Die wichtigsten sind:
    
    - **IP (Internet Protocol):** Für die Adressierung und das Routing von Datenpaketen.
    - **TCP (Transmission Control Protocol) oder UDP (User Datagram Protocol):** Für die zuverlässige (TCP) oder schnelle, aber potenziell unzuverlässige (UDP) Übertragung von Daten.
    - **802.11-Protokolle:** Die WLAN-spezifischen Protokolle, die die physikalische Schicht (Funkübertragung) und die Medienzugriffsschicht (MAC-Adresse, Kanalzugriff) definieren. Verschiedene 802.11-Standards (a/b/g/n/ac/ax/be etc.) bieten unterschiedliche Geschwindigkeiten, Frequenzbänder und Technologien.
5. **Kanäle und Frequenzbänder:** Um Interferenzen zu minimieren und die Leistung zu optimieren, werden WLANs in verschiedene Kanäle innerhalb der Frequenzbänder unterteilt.
    
    - **2,4-GHz-Band:** Bietet eine größere Reichweite, ist aber anfälliger für Interferenzen und hat weniger Kanäle.
    - **5-GHz-Band:** Bietet höhere Geschwindigkeiten und weniger Interferenzen, aber eine geringere Reichweite als 2,4 GHz.
    - **6-GHz-Band (Wi-Fi 6E / Wi-Fi 7):** Noch höhrere Geschwindigkeiten und Kapazitäten mit sehr geringen Interferenzen, aber die geringste Reichweite und erfordert neuere Geräte.
6. **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance):** WLAN verwendet CSMA/CA als Verfahren zur Medienzugriffskontrolle. Bevor ein Gerät sendet, "hört" es in den Funkkanal hinein, um sicherzustellen, dass er frei ist (Carrier Sense). Wenn der Kanal frei ist, sendet es. Um Kollisionen zu vermeiden (Collision Avoidance), wird ein zufälliger Wartezeitmechanismus verwendet, bevor ein Gerät erneut versucht zu senden, falls der Kanal belegt war.
    

**Aktuelle WLAN-Verschlüsselungen**

Die Sicherheit von WLANs hängt maßgeblich von der verwendeten Verschlüsselung ab. Aktuelle und empfohlene Verschlüsselungsprotokolle sind:

1. **WPA3 (Wi-Fi Protected Access 3):** Der aktuell sicherste Standard.
    
    - **SAE (Simultaneous Authentication of Equals):** Ersetzt den anfälligeren PSK (Pre-Shared Key) Austausch von WPA2 durch einen sichereren und robusteren Authentifizierungsmechanismus, der auch vor Wörterbuchangriffen besser schützt.
    - **192-Bit-Verschlüsselung im Enterprise-Modus:** Optional kann WPA3 im Enterprise-Modus (mit RADIUS-Server) eine noch stärkere 192-Bit-Verschlüsselung bieten.
    - **Protected Management Frames (PMF):** Schützt Management-Frames (die für die WLAN-Verwaltung wichtig sind) vor Abhören und Manipulation.
    - **Forward Secrecy:** Auch wenn ein Angreifer das aktuelle WLAN-Passwort kompromittiert, kann er nicht vergangene Sitzungen entschlüsseln.
2. **WPA2 (Wi-Fi Protected Access 2):** Immer noch weit verbreitet und als Minimum für akzeptable Sicherheit anzusehen, sollte aber nach Möglichkeit durch WPA3 ersetzt werden.
    
    - **AES (Advanced Encryption Standard) mit CCMP (Counter Mode Cipher Block Chaining Message Authentication Code Protocol):** Verwendet AES als starkes Verschlüsselungsalgorithmus. CCMP dient zur Integritätsprüfung der Daten.
    - **TKIP (Temporal Key Integrity Protocol):** Ein älterer Verschlüsselungsalgorithmus, der in WPA2 optional noch unterstützt wird, aber **NICHT MEHR EMPFOHLEN** wird, da er Schwachstellen aufweist. **AES/CCMP ist die sichere Wahl für WPA2.**

**Verschlüsselungen, die unbedingt vermieden werden sollten:**

- **WEP (Wired Equivalent Privacy):** Veraltet und **extrem unsicher**. Sollte **niemals** verwendet werden. Kann in Minuten mit frei verfügbaren Tools geknackt werden.
- **WPA (Wi-Fi Protected Access) mit TKIP:** Auch WPA mit TKIP gilt als **unsicher**. Sollte ebenfalls **nicht mehr verwendet** werden.

**Schwachstellen von WLAN**

Trotz der Fortschritte in der WLAN-Sicherheit gibt es weiterhin potenzielle Schwachstellen:

1. **Schwache Passwörter (PSK-Modus):** Wenn im WPA2/WPA3-PSK-Modus (Pre-Shared Key) ein zu einfaches oder häufig verwendetes Passwort gewählt wird, ist das WLAN anfällig für Brute-Force- oder Wörterbuchangriffe. Angreifer können versuchen, das Passwort durch Ausprobieren zu erraten.
    
2. **WPS (Wi-Fi Protected Setup):** WPS soll die WLAN-Verbindung vereinfachen, hat aber bekannte Sicherheitslücken. WPS-PIN-basierte Angriffe können relativ einfach das WLAN-Passwort kompromittieren. **WPS sollte deaktiviert werden.**
    
3. **Rogue Access Points (Bösartige Zugangspunkte):** Ein Angreifer kann einen gefälschten WLAN-Access Point in der Nähe aufstellen, der den Namen (SSID) eines legitimen Netzwerks verwendet. Benutzer könnten sich unwissentlich mit diesem bösartigen AP verbinden und ihre Daten könnten abgefangen werden (Man-in-the-Middle-Angriff).
    
4. **Evil Twin Attack:** Eine Weiterentwicklung des Rogue AP. Der Angreifer klont ein legitimes WLAN komplett (SSID, Verschlüsselungstyp etc.), aber kontrolliert den gesamten Datenverkehr.
    
5. **Deauthentication Attacks:** Angreifer können Deauthentifizierungs-Pakete senden, um Geräte gezielt aus einem WLAN zu werfen. Dies kann für Denial-of-Service-Angriffe oder in Kombination mit anderen Angriffen (z.B. Evil Twin) genutzt werden.
    
6. **Abhören des Funkverkehrs (Eavesdropping):** Auch mit starker Verschlüsselung ist es technisch möglich, den Funkverkehr abzufangen. Wenn auch die Entschlüsselung ohne das Passwort sehr schwierig ist (bei WPA2/WPA3 mit AES), könnte ein Angreifer, der genügend Daten aufzeichnet und später das Passwort erlangt, den Verkehr nachträglich entschlüsseln.
    
7. **Schwachstellen in Geräten und Firmware:** Sowohl WLAN-Router als auch WLAN-Adapter in Endgeräten können Software-Schwachstellen in ihrer Firmware aufweisen. Regelmäßige Updates sind wichtig, um diese zu beheben.
    
8. **Menschliches Versagen:** Fehlkonfigurationen, unachtsame Nutzung von WLANs in öffentlichen Bereichen, Phishing-Angriffe auf WLAN-Passwörter – menschliches Verhalten ist oft die größte Schwachstelle.
    

**Pro und Contras von WLAN**

**Pros (Vorteile):**

- **Kabellose Freiheit und Flexibilität:** Keine Kabelverlegung notwendig, Geräte können flexibel positioniert und bewegt werden. Ideal für mobile Geräte und Umgebungen, in denen Kabel schwierig zu verlegen sind.
- **Einfache Installation und Erweiterung:** WLANs sind relativ einfach einzurichten und zu erweitern. Neue Geräte können schnell hinzugefügt werden.
- **Kosteneffizienz:** Weniger Kosten für Verkabelung.
- **Benutzerfreundlichkeit:** Einfacher Zugang zum Netzwerk für Benutzer.
- **Unterstützung für viele Geräte:** WLAN ist der Standard für drahtlose Vernetzung und wird von fast allen Geräten unterstützt.

**Contras (Nachteile):**

- **Sicherheitsrisiken:** WLAN ist potenziell anfälliger für Sicherheitsrisiken als kabelgebundene Netzwerke, wenn es nicht richtig konfiguriert und geschützt wird.
- **Geringere Geschwindigkeit und Zuverlässigkeit (in bestimmten Fällen):** Im Vergleich zu modernen kabelgebundenen Netzwerken (z.B. 10 Gigabit Ethernet) können WLANs in bestimmten Szenarien geringere Geschwindigkeiten und höhere Latenzzeiten aufweisen, insbesondere in stark frequentierten Umgebungen oder bei Hindernissen. Die neuesten WLAN-Standards (Wi-Fi 6/6E/7) verbessern dies jedoch erheblich.
- **Interferenzen:** WLAN-Signale können durch andere elektronische Geräte, Wände und andere Hindernisse gestört werden, was die Reichweite und Leistung beeinträchtigen kann.
- **Geteiltes Medium:** Alle Geräte im WLAN teilen sich das Funkmedium. Je mehr Geräte gleichzeitig aktiv sind, desto geringer kann die individuelle Bandbreite pro Gerät sein.
- **Reichweitenbegrenzung:** Die Reichweite von WLAN-Signalen ist begrenzt und hängt von der Umgebung und der Sendeleistung ab. Für größere Bereiche sind möglicherweise mehrere Access Points erforderlich.

**Wie konfiguriere ich mein WLAN richtig (Sicherheit im Fokus)?**

Eine korrekte Konfiguration ist entscheidend für die Sicherheit Ihres WLANs. Hier sind wichtige Schritte:

1. **Verschlüsselungsprotokoll:**
    
    - **WPA3 Personal oder Enterprise verwenden (empfohlen):** Wählen Sie WPA3 als Verschlüsselungsprotokoll, falls Ihre Geräte und Ihr Router dies unterstützen. WPA3-Enterprise bietet zusätzliche Sicherheit mit RADIUS-Authentifizierung für größere Organisationen.
    - **Wenn WPA3 nicht möglich, WPA2 mit AES/CCMP verwenden:** Wählen Sie WPA2-Personal oder Enterprise mit AES/CCMP als akzeptables Minimum.
    - **TKIP und WEP unbedingt vermeiden.**
    - (Beispielhafte Darstellung von WLAN-Verschlüsselungseinstellungen)
        
        [![[24dc5910a8b8094b3384bd679bfc8810_MD5.png]]Wird in einem neuen Fenster geöffnet](https://app-community.fs.com/blog/wep-vs-wpa-vs-wpa2-vs-wpa3.html)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcR4gn-1TdXG0tjavnL3au43CI9zr3eomm9JfjdAX7xaHFybECfLiUVovVtUj1IeAMP5AupFHB2SxpKF7DcXM5g3vSnpmoemY408lvLz_kg)app-community.fs.com](https://app-community.fs.com/blog/wep-vs-wpa-vs-wpa2-vs-wpa3.html)
        
        WLAN Encryption Settings WPA3 WPA2
        
2. **Starkes WLAN-Passwort (PSK-Modus):**
    
    - **Komplex und einzigartig:** Verwenden Sie ein starkes, zufälliges Passwort, das aus einer Kombination von Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen besteht.
    - **Mindestlänge:** Empfohlen sind mindestens 12 Zeichen, besser länger (16+).
    - **Passwort-Manager:** Nutzen Sie einen Passwort-Manager, um sichere Passwörter zu generieren und zu verwalten.
    - **Regelmäßiger Passwortwechsel:** Ändern Sie das WLAN-Passwort in regelmäßigen Abständen, besonders wenn Sie vermuten, dass es kompromittiert sein könnte.
3. **SSID (Netzwerkname):**
    
    - **Keine persönlichen Daten:** Vermeiden Sie es, persönliche Informationen (Name, Adresse usw.) oder Hinweise auf den Router-Hersteller im SSID zu verwenden.
    - **SSID Broadcast deaktivieren (optional, aber nicht immer empfohlen):** Sie können die SSID-Übertragung deaktivieren, sodass das WLAN nicht automatisch in der Liste verfügbarer Netzwerke angezeigt wird. Geräte müssen die SSID manuell eingeben, um sich zu verbinden. **Dies erhöht die Sicherheit aber nur geringfügig und kann die Benutzerfreundlichkeit beeinträchtigen.** Es ist kein Ersatz für starke Verschlüsselung.
4. **WPS deaktivieren:**
    
    - **WPS unbedingt deaktivieren.** Suchen Sie in den WLAN-Einstellungen Ihres Routers nach WPS und deaktivieren Sie es vollständig.
    - (Beispielhafte Darstellung einer WPS-Deaktivierungseinstellung)
        
        [![[3f11a755514480d06f84c538077808aa_MD5.png]]Wird in einem neuen Fenster geöffnet](https://www.wps.com/academy/how-to-remove-wps-office-as-default-in-pc-step-by-step-quick-tutorials-1877546/)[![[4526ac0958b9e16ef27f687952f74a1a_MD5.png]]www.wps.com](https://www.wps.com/academy/how-to-remove-wps-office-as-default-in-pc-step-by-step-quick-tutorials-1877546/)
        
        WPS Deactivate Setting
        
5. **MAC-Adressfilterung (mit Vorsicht):**
    
    - **MAC-Adressfilterung kann als zusätzliche, aber **nicht als primäre** Sicherheitsmaßnahme verwendet werden.** Sie können im Router einstellen, dass nur Geräte mit bestimmten MAC-Adressen Zugriff erhalten.
    - **Umgehung möglich:** MAC-Adressen können jedoch gespooft (gefälscht) werden. MAC-Adressfilterung ist also kein starker Schutz gegen erfahrene Angreifer.
    - **Verwaltungsaufwand:** Das Verwalten von MAC-Adressfiltern kann aufwendig sein, besonders wenn viele Geräte hinzugefügt oder entfernt werden.
6. **Gast-WLAN einrichten:**
    
    - **Separates Netzwerk für Gäste:** Richten Sie ein separates Gast-WLAN ein, falls Ihr Router dies unterstützt. Das Gast-WLAN sollte vom Hauptnetzwerk isoliert sein.
    - **Beschränkter Zugriff:** Gäste sollten nur Internetzugriff haben, aber keinen Zugriff auf Geräte oder Ressourcen im Hauptnetzwerk.
    - (Beispielhafte Darstellung einer Gast-WLAN-Einstellung)
        
        [![[f89662a0c5048ea10fd0e54acfce5f9f_MD5.jpg]]Wird in einem neuen Fenster geöffnet](https://www.tp-link.com/latam/support/faq/649/)[![[4212c9733020392534d8a20397923001_MD5.png]]www.tp-link.com](https://www.tp-link.com/latam/support/faq/649/)
        
        Guest WLAN Setting
        
7. **Router-Firmware aktuell halten:**
    
    - **Regelmäßige Updates:** Halten Sie die Firmware Ihres WLAN-Routers immer aktuell. Hersteller veröffentlichen regelmäßig Updates, die Sicherheitslücken schließen und die Leistung verbessern.
    - **Automatische Updates aktivieren (wenn möglich):** Aktivieren Sie automatische Firmware-Updates, falls Ihr Router dies unterstützt.
8. **Zugriff auf Router-Konfigurationsoberfläche sichern:**
    
    - **Standardpasswort ändern:** Ändern Sie das Standardpasswort für den Zugriff auf die Konfigurationsoberfläche des Routers **unbedingt** in ein starkes, einzigartiges Passwort.
    - **Fernzugriff deaktivieren (wenn nicht benötigt):** Deaktivieren Sie den Fernzugriff auf die Router-Konfigurationsoberfläche, falls Sie diesen nicht benötigen. Fernzugriff kann ein Sicherheitsrisiko darstellen.
    - **HTTPS verwenden (wenn möglich):** Stellen Sie sicher, dass der Zugriff auf die Router-Konfigurationsoberfläche über HTTPS (verschlüsselt) erfolgt.
9. **Firewall aktivieren:**
    
    - **Integrierte Firewall nutzen:** WLAN-Router haben in der Regel eine integrierte Firewall. Stellen Sie sicher, dass diese aktiviert ist und korrekt konfiguriert ist.
    - **Ausgehende Verbindungen prüfen (fortgeschritten):** In fortgeschrittenen Konfigurationen können Sie auch ausgehende Verbindungen überwachen und Regeln definieren, um unerwünschte Verbindungen zu blockieren.
10. **Regelmäßige Überprüfung und Sicherheits-Audits:**
    
    - **Einstellungen überprüfen:** Überprüfen Sie in regelmäßigen Abständen Ihre WLAN-Einstellungen, um sicherzustellen, dass sie noch den aktuellen Best Practices entsprechen.
    - **Sicherheits-Scans (optional, für fortgeschrittene Nutzer):** Führen Sie bei Bedarf Sicherheits-Scans Ihres WLANs durch, um Schwachstellen zu identifizieren (es gibt spezialisierte Tools dafür).

**Zusammenfassend** ist ein sicheres WLAN eine Kombination aus starker Verschlüsselung (WPA3/WPA2 mit AES), einem sicheren Passwort, deaktiviertem WPS, aktuellen Firmware-Updates und weiteren Sicherheitsmaßnahmen. Die richtige Konfiguration erfordert etwas Aufwand, ist aber unerlässlich, um Ihre Daten und Geräte im WLAN zu schützen.