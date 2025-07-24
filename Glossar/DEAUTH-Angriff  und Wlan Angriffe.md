
**Was ist ein DEAUTH-Angriff (Deauthentication Attack)?**

"DEAUTH" steht für "Deauthentication" (Deauthentifizierung). Ein DEAUTH-Angriff ist eine Art von Denial-of-Service (DoS)-Angriff, der gezielt gegen WLAN-Netzwerke gerichtet ist. Der Angriff zielt darauf ab, die Verbindung zwischen einem oder mehreren Geräten und einem WLAN-Access Point (Router) **abzubrechen**.

**Kernprinzip:**

WLAN-Protokolle beinhalten Management-Frames, die für die Steuerung der WLAN-Verbindung unerlässlich sind. Einer dieser Management-Frames ist der "Deauthentication Frame". Dieser Frame wird normalerweise vom Access Point gesendet, um ein Gerät aus dem Netzwerk zu werfen, zum Beispiel wenn es inaktiv wird oder aufgrund von Netzwerkrichtlinien.

Ein DEAUTH-Angriff nutzt diese legitime Funktion **missbräuchlich** aus. Der Angreifer fälscht Deauthentication Frames und sendet sie an ein Zielgerät oder an den Access Point (oftmals gefälscht, als ob sie vom AP oder Gerät selbst stammen würden).

**Folgen eines erfolgreichen DEAUTH-Angriffs:**

- **Verbindungsverlust:** Das Zielgerät verliert sofort die WLAN-Verbindung.
- **Kein Internetzugriff:** Geräte können nicht mehr auf das Internet oder das lokale Netzwerk zugreifen.
- **Neuerliche Verbindungsversuche:** Geräte versuchen oft, sich automatisch wieder zu verbinden, was zu einer Schleife aus Verbindungsabbruch und Neuverbindungsversuchen führen kann, solange der Angriff andauert.
- **Denial of Service (DoS):** Im Extremfall kann ein DEAUTH-Angriff ein ganzes WLAN-Netzwerk lahmlegen, indem er die Verbindungen aller Geräte stört.

**Detaillierte Vorgehensweise eines DEAUTH-Angriffs (Schritt-für-Schritt):**

1. **Überwachung der WLAN-Umgebung (Monitoring Mode):**
    
    - Der Angreifer versetzt seine WLAN-Netzwerkkarte in den "Monitoring Mode" (auch "Monitor Mode" oder "Promiscuous Mode"). Dieser Modus erlaubt der Netzwerkkarte, **alle** WLAN-Pakete in der Umgebung zu empfangen, unabhängig davon, an welches Netzwerk oder welche MAC-Adresse sie gerichtet sind. Normalerweise würde eine Netzwerkkarte nur Pakete empfangen, die für ihre eigene MAC-Adresse bestimmt sind.
    - **Tools:** Für diesen Schritt werden oft Tools wie `airmon-ng` (Teil der Aircrack-ng Suite) verwendet.
    
    Bash
    
    ```
    sudo airmon-ng start <WLAN-Interface>
    ```
    
    _(Beispiel: `sudo airmon-ng start wlan0`)_
    
2. **Identifizierung von Zielnetzwerk und Zielgerät:**
    
    - Mit einem WLAN-Sniffer (z.B. `airodump-ng`, auch aus der Aircrack-ng Suite) scannt der Angreifer die Umgebung, um verfügbare WLAN-Netzwerke und die mit ihnen verbundenen Geräte zu identifizieren.
    - `airodump-ng` zeigt eine Liste von WLAN Access Points (BSSIDs), deren Namen (ESSIDs), Kanäle, Verschlüsselungstypen und die MAC-Adressen der verbundenen Geräte (STAs - Stations) an.
    - Der Angreifer wählt ein Zielnetzwerk (BSSID) und ein Zielgerät (STA-MAC-Adresse) aus, das er vom Netzwerk trennen möchte.
    
    Bash
    
    ```
    sudo airodump-ng <Monitor-Interface>
    ```
    
    _(Beispiel: `sudo airodump-ng wlan0mon`)_(Beispielhafte Ausgabe von airodump-ng, die WLAN-Netzwerke und verbundene Geräte zeigt)
    
    [![Bildmotiv: airodumpng output showing WLAN networks and connected devices](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSEEdNj25lH4HNi1S-Q93lS8OvwoHbtpKAi6cNRjOpSOq4j-3qsvIb_u6Gy2ErH)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Results-of-a-scan-using-Airodump-ng_fig2_327563071)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Results-of-a-scan-using-Airodump-ng_fig2_327563071)
    
    airodumpng output showing WLAN networks and connected devices
    
3. **Generierung und Versand von Deauthentication Frames:**
    
    - Mit einem Tool wie `aireplay-ng` (ebenfalls aus der Aircrack-ng Suite) generiert und versendet der Angreifer Deauthentication Frames.
    - Der Angriff kann gezielt gegen ein bestimmtes Gerät gerichtet werden, indem die MAC-Adresse des Zielgeräts im Deauthentication Frame angegeben wird.
    - Oder der Angriff kann als "Broadcast Deauthentication" gegen alle Geräte im Netzwerk gerichtet sein, indem die Broadcast-MAC-Adresse als Ziel verwendet wird.
    - Der Angreifer **fälscht** die MAC-Adresse des Access Points als Absenderadresse im Deauthentication Frame, damit es für das Zielgerät so aussieht, als ob der Befehl zum Trennen vom legitimen Access Point kommt.
    
    **Beispiele für `aireplay-ng` Befehle:**
    
    - **Gezielter Angriff auf ein Gerät (mit Angabe der Client-MAC-Adresse):**
    
    Bash
    
    ```
    sudo aireplay-ng --deauth 1 -a <BSSID des AP> -c <MAC-Adresse des Zielgeräts> <Monitor-Interface>
    ```
    
    _(Beispiel: `sudo aireplay-ng --deauth 1 -a AA:BB:CC:11:22:33 -c DD:EE:FF:44:55:66 wlan0mon`)_
    
    - **Broadcast Deauthentication (alle Geräte im Netzwerk trennen):**
    
    Bash
    
    ```
    sudo aireplay-ng --deauth 1 -a <BSSID des AP> <Monitor-Interface>
    ```
    
    _(Beispiel: `sudo aireplay-ng --deauth 1 -a AA:BB:CC:11:22:33 wlan0mon`)_
    
    - `--deauth 1`: Anzahl der Deauthentication Frames (1 reicht oft aus).
    - `-a <BSSID des AP>`: BSSID (MAC-Adresse) des Access Points des Zielnetzwerks.
    - `-c <MAC-Adresse des Zielgeräts>`: MAC-Adresse des Zielgeräts (optional, für gezielten Angriff).
    - `<Monitor-Interface>`: Das Monitor-Interface der WLAN-Karte.
4. **Wiederholung des Angriffs (optional):** Um den Denial-of-Service aufrechtzuerhalten, kann der Angreifer den Deauthentication-Angriff in einer Schleife wiederholen, indem er kontinuierlich Deauthentication Frames sendet.
    

**Wie kann ich Mitschnitte über WLAN verhindern?**

Es ist wichtig zu verstehen, dass das **vollständige Verhindern** von WLAN-Mitschnitten technisch **sehr schwierig, wenn nicht unmöglich** ist, da Funkwellen naturgemäß in der Luft übertragen werden und von jedem empfangen werden können, der über die entsprechende Ausrüstung verfügt. Jedoch können Sie das Risiko und die Auswirkungen von Mitschnitten **erheblich reduzieren** durch folgende Maßnahmen:

1. **Starke Verschlüsselung verwenden (WPA3/WPA2 mit AES):**
    
    - **WPA3 ist der aktuell sicherste Standard und sollte bevorzugt werden.** WPA3-SAE schützt besser vor Wörterbuchangriffen und bietet Forward Secrecy.
    - **WPA2 mit AES/CCMP ist ein akzeptables Minimum.** Stellen Sie sicher, dass Sie AES und nicht TKIP als Verschlüsselungsalgorithmus verwenden.
    - **WEP und WPA mit TKIP sind unsicher und sollten niemals verwendet werden.**
    - Starke Verschlüsselung macht das **Entschlüsseln** des abgefangenen Datenverkehrs **extrem schwierig** ohne das korrekte WLAN-Passwort. Dies ist die **wichtigste Verteidigungslinie**.
2. **Starkes und einzigartiges WLAN-Passwort:**
    
    - Ein **komplexes, langes und zufälliges** Passwort ist entscheidend, um Brute-Force-Angriffe gegen das WLAN-Passwort zu erschweren.
    - Verwenden Sie einen **Passwort-Manager**, um sichere Passwörter zu generieren und zu verwalten.
    - **Regelmäßiger Passwortwechsel** erhöht die Sicherheit zusätzlich.
3. **WPS deaktivieren:** WPS (Wi-Fi Protected Setup) hat bekannte Sicherheitslücken und sollte **unbedingt deaktiviert** werden.
    
4. **Gast-WLAN für unsichere Geräte und Gäste:** Richten Sie ein separates Gast-WLAN ein, um Ihr Hauptnetzwerk von potenziell unsicheren Geräten oder Gastzugängen zu isolieren.
    
5. **VPN (Virtual Private Network) für sensible Daten:**
    
    - Verwenden Sie ein VPN, um den Datenverkehr **zusätzlich zu verschlüsseln**, der über WLAN übertragen wird, insbesondere wenn Sie sensible Daten übertragen oder in öffentlichen WLANs unterwegs sind.
    - Ein VPN erstellt einen **verschlüsselten Tunnel** zwischen Ihrem Gerät und einem VPN-Server, wodurch der gesamte Datenverkehr (auch innerhalb des WLANs) geschützt wird.
    - Dies schützt vor Mitschnitten **innerhalb** des WLANs selbst und auch auf dem Weg zum Internet.
6. **HTTPS verwenden:** Stellen Sie sicher, dass Webseiten und Online-Dienste, die Sie nutzen, HTTPS verwenden. HTTPS verschlüsselt die Kommunikation zwischen Ihrem Browser und der Webseite. Dies ist ein **grundlegender Schutz** im Internet.
    
7. **Aktuelle Software und Firmware:** Halten Sie die Firmware Ihres WLAN-Routers und die Software auf Ihren Geräten immer auf dem neuesten Stand, um Sicherheitslücken zu schließen.
    
8. **Physische Sicherheit des Routers:** Stellen Sie sicher, dass Ihr WLAN-Router physisch sicher ist und nicht für Unbefugte zugänglich ist, um Manipulationen zu verhindern.
    
9. **WLAN-Analyse-Tools verwenden (für Überwachung und Erkennung):** Setzen Sie WLAN-Analyse-Tools (wie Wireshark, Kismet, etc.) ein, um Ihr eigenes WLAN-Netzwerk regelmäßig zu überwachen und verdächtige Aktivitäten zu erkennen. Dies ist besonders relevant für Unternehmen und Organisationen.
    
10. **Aufklärung und Sensibilisierung der Benutzer:** Schulen Sie Benutzer im sicheren Umgang mit WLAN, z.B. Vermeidung unsicherer öffentlicher WLANs, Verwendung von VPNs, sichere Passwörter, etc.
    

**Wie funktionieren WLAN-Angriffe im Allgemeinen?**

WLAN-Angriffe lassen sich grob in verschiedene Kategorien einteilen:

1. **Passwort-basierte Angriffe (gegen die Verschlüsselung):**
    
    - **Brute-Force-Angriffe:** Versuchen, das WLAN-Passwort durch systematisches Ausprobieren aller möglichen Kombinationen zu erraten. Effektiv gegen schwache Passwörter.
    - **Wörterbuchangriffe:** Verwenden Listen häufig verwendeter Passwörter (Wörterbücher), um das WLAN-Passwort zu knacken. Effektiv, wenn Benutzer häufige Passwörter verwenden.
    - **PMKID-basierte Angriffe (neuere, schnellere Methode):** Nutzen eine Schwachstelle im WPA/WPA2-Protokoll, um den "Pairwise Master Key ID" (PMKID) zu extrahieren. Dieser kann dann offline mit Brute-Force oder Wörterbüchern geknackt werden. Schneller als traditionelle Handshake-basierte Angriffe.
2. **Man-in-the-Middle (MitM) Angriffe:**
    
    - **Evil Twin/Rogue AP Angriffe:** Der Angreifer erstellt einen gefälschten WLAN-Access Point mit dem gleichen Namen (SSID) wie ein legitimes Netzwerk. Benutzer, die sich unwissentlich mit dem gefälschten AP verbinden, leiten ihren gesamten Datenverkehr über den Angreifer, der ihn abhören und manipulieren kann.
    - **ARP Spoofing im WLAN:** Innerhalb eines WLANs kann ARP Spoofing verwendet werden, um sich als Gateway (Router) auszugeben und den Datenverkehr anderer Geräte umzuleiten.
3. **Denial-of-Service (DoS) Angriffe:**
    
    - **DEAUTH-Angriffe:** Wie oben beschrieben, um WLAN-Verbindungen zu stören oder zu unterbrechen.
    - **Jamming:** Stören der WLAN-Funkfrequenzen durch starke Rauschsignale, um die Kommunikation unmöglich zu machen.
4. **Ausnutzung von Schwachstellen in Protokollen und Implementierungen:**
    
    - **FragAttacks:** Eine Sammlung von Schwachstellen in verschiedenen WLAN-Protokollen (802.11 Standards).
    - **KRACK Attack (Key Reinstallation Attacks):** Nutzen Schwachstellen in der WPA2-Verschlüsselung aus, um den Datenverkehr zu entschlüsseln oder zu manipulieren (betrifft aber in der Praxis meist nur sehr spezifische Szenarien).
    - **Schwachstellen in Router-Firmware:** Angriffe, die bekannte Sicherheitslücken in der Firmware von WLAN-Routern ausnutzen, um die Kontrolle über den Router zu übernehmen.
5. **Phishing-Angriffe (gegen Benutzer):** Soziale Manipulation, um Benutzer dazu zu bringen, ihr WLAN-Passwort preiszugeben (z.B. gefälschte Login-Seiten, E-Mails).
    

**Was hat Brute-Force mit WLAN-Angriffen zu tun?**

Brute-Force-Angriffe spielen eine **zentrale Rolle** bei vielen WLAN-Angriffen, insbesondere bei Angriffen, die darauf abzielen, die **WLAN-Verschlüsselung zu knacken** und das **WLAN-Passwort herauszufinden**.

- **Ziel von Brute-Force:** Das Ziel eines Brute-Force-Angriffs ist es, das **Pre-Shared Key (PSK)** zu finden, also das WLAN-Passwort, das für die WPA/WPA2/WPA3-Verschlüsselung verwendet wird (im "Personal"-Modus).
    
- **Ablauf eines Brute-Force Angriffs auf WLAN (vereinfacht):**
    
    1. **WLAN-Handshake aufzeichnen:** Um das WLAN-Passwort offline zu knacken, muss der Angreifer zunächst den "4-Way-Handshake" aufzeichnen. Dieser Handshake findet statt, wenn sich ein Gerät neu mit dem WLAN verbindet. Der Handshake enthält kryptografische Informationen, die für den Brute-Force-Angriff benötigt werden. Ein DEAUTH-Angriff wird oft verwendet, um ein Gerät kurzzeitig vom WLAN zu trennen, damit es sich automatisch wieder verbindet und der Handshake aufgezeichnet werden kann.
    2. **Brute-Force oder Wörterbuchangriff offline:** Nachdem der Handshake aufgezeichnet wurde, kann der Angreifer den eigentlichen Brute-Force-Angriff **offline** durchführen. Das bedeutet, der Angriff findet nicht mehr aktiv im WLAN statt und ist schwerer zu erkennen. Tools wie `aircrack-ng` werden verwendet, um verschiedene Passwörter (aus Wörterbüchern oder durch Generierung von Kombinationen) auszuprobieren und zu prüfen, ob eines davon zum aufgezeichneten Handshake passt. Dies ist rechenintensiv und kann je nach Passwortstärke und Rechenleistung lange dauern (von Minuten bis zu Jahren).
    3. **Passwort gefunden:** Wenn der Brute-Force-Angriff erfolgreich ist, wird das WLAN-Passwort gefunden. Mit diesem Passwort kann der Angreifer sich mit dem WLAN verbinden und den verschlüsselten Datenverkehr entschlüsseln.
- **Je stärker das WLAN-Passwort, desto länger dauert der Brute-Force-Angriff:** Ein langes, komplexes und zufälliges Passwort macht Brute-Force-Angriffe erheblich aufwendiger und in vielen Fällen praktisch unmöglich in einer vernünftigen Zeit.
    

**Wie nutzt man Wireshark in diesem Zusammenhang?**

Wireshark ist ein mächtiges Netzwerkprotokoll-Analyse-Tool (Sniffer), das auch im Kontext von WLAN-Angriffen und -Sicherheitsanalysen eine wichtige Rolle spielt.

**Wireshark kann verwendet werden für:**

1. **Mitschnitt und Analyse von WLAN-Traffic:**
    
    - Wireshark kann im "Monitor Mode" WLAN-Pakete erfassen, ähnlich wie `airodump-ng`. Es bietet jedoch eine viel **detailliertere Analyse** der Pakete.
    - Sie können **alle** Arten von WLAN-Frames sehen: Management Frames (z.B. Beacons, Probe Requests, Deauthentication), Control Frames, Data Frames.
    - **Filterfunktionen:** Wireshark bietet umfangreiche Filterfunktionen, um den erfassten Traffic zu analysieren und relevante Pakete zu finden (z.B. Filter nach Protokolltyp, MAC-Adresse, SSID, etc.).
2. **Untersuchung von Deauthentication Attacks:**
    
    - Mit Wireshark können Sie **Deauthentication Frames** im WLAN-Traffic **erkennen** und **analysieren**.
    - Sie können sehen, **wer** die Deauthentication Frames sendet (Absender-MAC-Adresse), **an wen** sie gerichtet sind (Empfänger-MAC-Adresse) und den **Grund** für die Deauthentifizierung (Reason Code).
    - Dies hilft, DEAUTH-Angriffe zu **diagnostizieren** und zu **bestätigen**.
3. **Analyse des 4-Way-Handshakes (für Passwort-Cracking):**
    
    - Wireshark kann verwendet werden, um den **4-Way-Handshake** während der WLAN-Verbindungserstellung **aufzuzeichnen**.
    - Durch Filterung des WLAN-Traffics nach dem EAPOL-Protokoll (Extensible Authentication Protocol over LAN) können Sie die relevanten Handshake-Pakete identifizieren und extrahieren.
    - Diese Handshake-Datei kann dann an Tools wie `aircrack-ng` übergeben werden, um den Brute-Force-Angriff auf das WLAN-Passwort zu starten.
4. **Inspektion von WLAN-Protokollen und -Frames:**
    
    - Wireshark ermöglicht es, **detailliert in die WLAN-Protokolle und -Frames einzutauchen.** Sie können die Struktur verschiedener Frame-Typen, Felder und Flags untersuchen.
    - Dies ist wertvoll für das **tiefere Verständnis der WLAN-Technologie** und für **Fehlerdiagnose** in WLAN-Netzwerken.
5. **Erkennung von Anomalien und verdächtigem Verhalten:**
    
    - Durch die Überwachung des WLAN-Traffics mit Wireshark können Sie **ungewöhnliche Muster oder verdächtige Aktivitäten erkennen**, z.B. unerwartet viele Deauthentication Frames, Rogue AP Beacons, ARP Spoofing Traffic etc.
    - Dies kann helfen, **aktive Angriffe oder Fehlkonfigurationen** im WLAN zu identifizieren.
6. **Sicherheits-Audits und Penetrationstests (ethisches Hacking):**
    
    - Wireshark ist ein **wichtiges Werkzeug für White-Hat-Hacker und Sicherheitsexperten**, um die Sicherheit von WLAN-Netzwerken zu **testen und zu verbessern.**
    - Es kann verwendet werden, um **Schwachstellen zu identifizieren**, Angriffe zu simulieren und die Wirksamkeit von Sicherheitsmaßnahmen zu überprüfen.

**Schritt-für-Schritt Beispiel: DEAUTH Angriff mit Wireshark analysieren:**

1. **Starten Sie Wireshark** und wählen Sie Ihr Monitor-Interface (z.B. `wlan0mon`) zum Mitschneiden aus.
2. **Starten Sie einen DEAUTH-Angriff** mit `aireplay-ng` gegen ein Zielgerät (wie oben beschrieben).
3. **Beobachten Sie den Wireshark-Capture:**
    - **Filtern Sie nach "wlan.fc.type_subtype == 0x0c"** (dies filtert nach Deauthentication Frames). Geben Sie dies in das Filterfeld oben in Wireshark ein und drücken Sie Enter.
    - Sie sollten nun eine Liste von Deauthentication Frames sehen.
    - **Analysieren Sie die Frames:**
        - **Source Address:** Die MAC-Adresse, die als Absender des Deauthentication Frames angegeben ist (sollte die BSSID des Access Points sein, wenn der Angriff erfolgreich gefälscht wurde).
        - **Destination Address:** Die MAC-Adresse des Zielgeräts (oder Broadcast-Adresse für Broadcast-DEAUTH).
        - **Reason Code:** Der Grund für die Deauthentifizierung (z.B. "Class 3 frame received from nonassociated STA"). Der Reason Code kann zusätzliche Informationen liefern, ist aber für den grundlegenden DEAUTH-Angriff weniger relevant.
    - (Beispielhafte Darstellung von Wireshark, das Deauthentication Frames mit dem Filter "wlan.fc.type_subtype == 0x0c" zeigt)
        
        [![Bildmotiv: Wireshark showing Deauthentication Frames](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRSnoKE7luX3XY8pbJjySiYBh-eZAn_dYTiSZgF4IvbBZhUwjvlBR0i37fL5OM4)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Analyzing-Deauthentication-Attack-in-Wireshark-The-resulting-info-can-be-concluded-from_fig9_283354063)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Analyzing-Deauthentication-Attack-in-Wireshark-The-resulting-info-can-be-concluded-from_fig9_283354063)
        
        Wireshark showing Deauthentication Frames
        

**Wichtiger Hinweis:** Das Durchführen von WLAN-Angriffen ohne Erlaubnis ist **illegal und unethisch**. Die hier beschriebenen Informationen dienen **ausschließlich zu Lehr- und Analysezwecken** und sollten nur in **autorisierten Umgebungen** (z.B. im eigenen Testlabor, mit Zustimmung des Netzwerkbetreibers) verwendet werden. White-Hat-Hacker verwenden diese Techniken, um Sicherheitslücken zu finden und die Sicherheit zu verbessern, **nicht** um Schaden anzurichten.