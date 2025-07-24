
Diese Anleitung beschreibt eine **Offline-Brute-Force-Attacke** auf ein WPA/WPA2-PSK-verschlüsseltes WLAN-Netzwerk. Der Angriff basiert darauf, den **4-Way-Handshake** während des Verbindungsaufbaus eines Clients mit dem WLAN aufzuzeichnen und diesen Handshake dann **offline** mit Hashcat gegen eine Wörterliste zu testen, um das WLAN-Passwort zu knacken. Wireshark dient in diesem Prozess hauptsächlich zur _optionalen_ Überprüfung des aufgezeichneten Handshakes, während Hashcat das eigentliche Knacken des Passworts übernimmt.

**Benötigte Werkzeuge und Voraussetzungen:**

1. **Computer mit Linux (empfohlen):** Eine Linux-Distribution wie Kali Linux ist ideal, da viele benötigte Tools bereits vorinstalliert sind.
2. **WLAN-Adapter, der den Monitor-Modus unterstützt:** Nicht jeder WLAN-Adapter kann in den Monitor-Modus versetzt werden, der für das Aufzeichnen des WLAN-Verkehrs erforderlich ist. Stellen Sie sicher, dass Ihr WLAN-Adapter kompatibel ist. Adapter mit Chipsätzen von Atheros oder Ralink sind oft gut geeignet.
3. **Aircrack-ng Suite:** Eine Sammlung von Tools für WLAN-Sicherheitsaudits, die wichtige Programme wie `airmon-ng`, `airodump-ng` und `aireplay-ng` enthält, die wir für die Handshake-Erfassung benötigen.
4. **Wireshark (optional):** Ein Netzwerkanalysator, der _optional_ zur Überprüfung des aufgezeichneten Handshakes verwendet werden kann.
5. **Hashcat:** Ein leistungsstarkes Passwort-Cracking-Tool, das wir für die Brute-Force-Attacke gegen den Handshake verwenden werden.
6. **Wörterliste (Wordlist):** Eine Textdatei mit einer Liste von möglichen Passwörtern. Je umfangreicher und relevanter die Wörterliste, desto höher die Wahrscheinlichkeit, das Passwort zu finden (falls es in der Liste enthalten ist). Es gibt verschiedene vorgefertigte Wörterlisten, wie z.B. `rockyou.txt`.

**Schritt-für-Schritt-Anleitung zur Brute-Force-Attacke auf WLAN mit Wireshark und Hashcat:**

**Schritt 1: WLAN-Adapter in den Monitor-Modus versetzen**

Der Monitor-Modus ermöglicht es Ihrem WLAN-Adapter, alle WLAN-Pakete in der Luft zu empfangen, unabhängig davon, mit welchem Netzwerk Sie verbunden sind. Dies ist für das Aufzeichnen des 4-Way-Handshakes unerlässlich.

1. **Terminal öffnen:** Starten Sie ein Terminal auf Ihrem Linux-System.
    
2. **WLAN-Schnittstelle überprüfen:** Geben Sie den Befehl `iwconfig` ein, um Ihre WLAN-Schnittstellen aufzulisten. Notieren Sie sich den Namen Ihrer WLAN-Schnittstelle (z.B. `wlan0`).
    
3. **Monitor-Modus starten:** Verwenden Sie `airmon-ng`, um den Monitor-Modus auf Ihrer WLAN-Schnittstelle zu aktivieren:
    
    Bash
    
    ```
    sudo airmon-ng start <Ihre WLAN-Schnittstelle>
    ```
    
    Ersetzen Sie `<Ihre WLAN-Schnittstelle>` durch den Namen Ihrer WLAN-Schnittstelle (z.B. `wlan0`). `airmon-ng` wird versuchen, Prozesse zu beenden, die den Monitor-Modus stören könnten, und eine neue Monitor-Schnittstelle erstellen (z.B. `wlan0mon`).
    
4. **Überprüfung des Monitor-Modus:** Geben Sie erneut `iwconfig` ein. Sie sollten nun eine neue Schnittstelle (z.B. `wlan0mon`) im "Monitor Mode" sehen. Notieren Sie sich den Namen dieser **Monitor-Schnittstelle**.
    

**Schritt 2: 4-Way-Handshake erfassen mit Airodump-ng**

Wir verwenden `airodump-ng`, um den WLAN-Verkehr zu scannen und den 4-Way-Handshake des Ziel-WLAN-Netzwerks aufzuzeichnen.

1. **Airodump-ng starten:** Starten Sie `airodump-ng` und geben Sie Ihre Monitor-Schnittstelle an, um alle WLAN-Netzwerke in der Umgebung anzuzeigen:
    
    Bash
    
    ```
    sudo airodump-ng <Monitor-Schnittstelle>
    ```
    
    Ersetzen Sie `<Monitor-Schnittstelle>` durch den Namen Ihrer Monitor-Schnittstelle (z.B. `wlan0mon`).
    
2. **Zielnetzwerk identifizieren:** `airodump-ng` zeigt eine Liste der WLAN-Netzwerke an. Suchen Sie nach Ihrem Zielnetzwerk anhand des ESSID (Netzwerkname). Notieren Sie sich die **BSSID (MAC-Adresse des Access Points) und den Kanal (CH)** des Zielnetzwerks.
    
3. **Airodump-ng gezielt starten:** Starten Sie `airodump-ng` erneut, aber diesmal gezielt auf das Zielnetzwerk, um nur den relevanten Verkehr aufzuzeichnen:
    
    Bash
    
    ```
    sudo airodump-ng -c <Kanal> --bssid <BSSID> -w <Dateiname> <Monitor-Schnittstelle>
    ```
    
    - `<Kanal>`: Kanal des Zielnetzwerks (aus Schritt 2).
    - `<BSSID>`: BSSID des Zielnetzwerks (aus Schritt 2).
    - `<Dateiname>`: Ein Name für die Datei, in der die aufgezeichneten Daten gespeichert werden sollen (z.B. `handshake`).
    - `<Monitor-Schnittstelle>`: Name der Monitor-Schnittstelle.
    
    Beispiel:
    
    Bash
    
    ```
    sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w handshake wlan0mon
    ```
    
4. **Client deauthentifizieren (optional, aber oft notwendig):** Um den 4-Way-Handshake zu erzwingen, müssen wir ein Gerät (Client) vom WLAN trennen, damit es sich wieder neu verbindet. Verwenden Sie `aireplay-ng` in einem **neuen** Terminalfenster:
    
    Bash
    
    ```
    sudo aireplay-ng -0 1 -a <BSSID> -c <Client-MAC-Adresse> <Monitor-Schnittstelle>
    ```
    
    - `-0 1`: Sendet ein Deauthentifizierungs-Paket.
    - `-a <BSSID>`: BSSID des Zielnetzwerks.
    - `-c <Client-MAC-Adresse>`: MAC-Adresse eines Clients, der mit dem Zielnetzwerk verbunden ist. Beobachten Sie die untere Hälfte der `airodump-ng`-Ausgabe (STATION), um eine Client-MAC-Adresse zu finden. Wenn Sie keine Client-MAC-Adresse kennen, können Sie `-c` weglassen, um ein Broadcast-Deauthentifizierungs-Paket an alle Clients zu senden.
    - `<Monitor-Schnittstelle>`: Name der Monitor-Schnittstelle.
    
    Beispiel (Broadcast-Deauthentifizierung):
    
    Bash
    
    ```
    sudo aireplay-ng -0 1 -a AA:BB:CC:DD:EE:FF wlan0mon
    ```
    
5. **Handshake-Erfassung überprüfen:** Achten Sie in `airodump-ng` oben rechts auf die Meldung "**WPA handshake: &lt;BSSID>**". Wenn diese Meldung erscheint, wurde der Handshake erfolgreich aufgezeichnet.
    
    [![Bildmotiv: Airodumpng showing WPA handshake message](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcToA66YPgraa8jc-4yTFhcm3kjfQlEfxnMn0AX9QxO2l9h2ZhZUmpgtGV6kfTAX)Wird in einem neuen Fenster geöffnet](https://www.researchgate.net/figure/Successful-four-way-handshake-packet-capture_fig4_327563071)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQHnHFqVlgn9GP_QNJZJqp5p4tCYLbsP3aagcGHhOG1R5B49YpECY11Ifpa36Xt9B7B7i5sptMSQYILbaYUaLXDbBCp19SJHEuOmPv3eRw)www.researchgate.net](https://www.researchgate.net/figure/Successful-four-way-handshake-packet-capture_fig4_327563071)
    
    Airodumpng showing WPA handshake message
    
    Sobald der Handshake erfasst wurde, können Sie `aireplay-ng` und `airodump-ng` mit `Strg+C` beenden. Der Handshake ist nun in der `.cap`-Datei gespeichert (z.B. `handshake-01.cap`).
    

**Schritt 3 (Optional): Handshake in Wireshark überprüfen (optional, für Analyse)**

Dieser Schritt ist **optional**, aber er kann hilfreich sein, um den aufgezeichneten Handshake visuell zu überprüfen und den WLAN-Verkehr zu analysieren.

1. **Wireshark starten:** Starten Sie Wireshark.
2. **Capture-Datei öffnen:** Öffnen Sie die `.cap`-Datei, die von `airodump-ng` erstellt wurde (z.B. `handshake-01.cap`) in Wireshark über "Datei" -> "Öffnen".
3. **Filter anwenden:** Geben Sie in das Filterfeld von Wireshark `eapol` ein und drücken Sie Enter. Dies filtert den Verkehr, um nur EAPOL-Pakete (Extensible Authentication Protocol over LAN), die für den 4-Way-Handshake relevant sind, anzuzeigen.
    
    [![Bildmotiv: Wireshark EAPOL filter](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRPx9XqspXMMqiukTnYVNrL3dzCuH-pOKLcWvnBZgBnt-riExLJFvHWaDCQx76g)Wird in einem neuen Fenster geöffnet](https://osqa-ask.wireshark.org/questions/48811/capture-filter-for-eapol-packets-does-not-show-anything/)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQSkWcttvABrgJCXb2e-pKKiDCljcP4YjR2ihFr_W0jvv6i3Ej8_ckeM8RIY5HYw9FWJHF_ia_acC1-VQPC675Re9kIL6gZe9PNZfms5WFHBQ)osqa-ask.wireshark.org](https://osqa-ask.wireshark.org/questions/48811/capture-filter-for-eapol-packets-does-not-show-anything/)
    
    Wireshark EAPOL filter
    
4. **Handshake-Pakete überprüfen:** Sie sollten nun idealerweise vier EAPOL-Pakete sehen, die den 4-Way-Handshake repräsentieren. Diese Pakete zeigen die Kommunikation zwischen Access Point und Client während der Authentifizierung. Die genaue Analyse der Pakete ist für die Brute-Force-Attacke mit Hashcat nicht zwingend erforderlich, aber sie hilft, den Prozess zu verstehen.
    
    [![Bildmotiv: Wireshark showing 4Way Handshake Packets](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRDhYNkmzHVrJ1K7wJKsOLqqVq9VbCRncU-sOte4RnbFRuvAAf9-BzG0Iqe967D)Wird in einem neuen Fenster geöffnet](https://osqa-ask.wireshark.org/questions/60050/decrypt-80211-i-got-the-4-way-handshake/)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcQSkWcttvABrgJCXb2e-pKKiDCljcP4YjR2ihFr_W0jvv6i3Ej8_ckeM8RIY5HYw9FWJHF_ia_acC1-VQPC675Re9kIL6gZe9PNZfms5WFHBQ)osqa-ask.wireshark.org](https://osqa-ask.wireshark.org/questions/60050/decrypt-80211-i-got-the-4-way-handshake/)
    
    Wireshark showing 4Way Handshake Packets
    

**Schritt 4: Passwort mit Hashcat knacken**

Jetzt verwenden wir Hashcat, um eine Dictionary-Attacke gegen den aufgezeichneten Handshake durchzuführen und zu versuchen, das WLAN-Passwort zu knacken.

1. **Hashcat starten:** Öffnen Sie ein Terminal und starten Sie Hashcat mit dem folgenden Befehl:
    
    Bash
    
    ```
    hashcat -m 22000 -a 0 -o cracked.txt <handshake.cap> <Pfad zur Wörterliste>
    ```
    
    - `hashcat`: Der Befehl zum Starten von Hashcat.
    - `-m 22000`: Gibt den Hash-Modus an. `22000` ist der Modus für WPA/WPA2 (genauer gesagt, es ist der neuer empfohlene Modus für aktuellere Hashcat-Versionen. Für ältere Versionen kann `-m 2500` verwendet werden). Stellen Sie sicher, dass Sie den korrekten Modus für Ihre Hashcat-Version verwenden. Überprüfen Sie die Hashcat-Dokumentation für die aktuellsten Informationen.
    - `-a 0`: Gibt den Attackmodus an. `0` steht für "Straight Attack", was in diesem Fall bedeutet, dass jedes Wort aus der Wörterliste direkt als Passwort-Kandidat verwendet wird.
    - `-o cracked.txt`: Gibt den Namen der Ausgabedatei an (`cracked.txt`), in der Hashcat das geknackte Passwort speichern soll, falls es gefunden wird.
    - `<handshake.cap>`: Der Pfad zur Capture-Datei mit dem Handshake (z.B. `handshake-01.cap` oder einfach `handshake.cap`, je nachdem, wie `airodump-ng` die Datei benannt hat).
    - `<Pfad zur Wörterliste>`: Der vollständige Pfad zu Ihrer Wörterbuchdatei (z.B. `/usr/share/wordlists/rockyou.txt`). Stellen Sie sicher, dass die Wörterliste existiert und lesbar ist.
    
    Beispiel:
    
    [![Bildmotiv: Hashcat command](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT8H3UbNyia4MpNBcc03NqQwaboY0A5Xbu6BoaXIOl156UbOkvDAl7bTXV7XQuU)Wird in einem neuen Fenster geöffnet](https://hashcat.net/hashcat/)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcSgz9Nu7m561OhtnqNusWh4y9wYz_XbRq9JYQU2YrxJmbyaNHU1w66KC9jeVWdD5k8lKTpY8ZZyz5I62DHdNqTjAZuDsek)hashcat.net](https://hashcat.net/hashcat/)
    
    Hashcat command
    
    Bash
    
    ```
    hashcat -m 22000 -a 0 -o cracked.txt handshake.cap /usr/share/wordlists/rockyou.txt
    ```
    
2. **Hashcat-Ausgabe beobachten:** Hashcat beginnt nun, die Wörter aus der Wörterliste gegen den Handshake zu testen. Der Fortschritt und die Geschwindigkeit der Attacke werden im Terminal angezeigt.
    
    [![Bildmotiv: Hashcat output during cracking](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvefF0AzkwCK7BW4yFekCnHxxBuaRPmTMQVOmG4N8Exgj2yXYfSTetzZUhEZL-)Wird in einem neuen Fenster geöffnet](https://www.praetorian.com/blog/gladius-automatic-responder-cracking/)[![](https://encrypted-tbn3.gstatic.com/favicon-tbn?q=tbn:ANd9GcTXNyVpOhXF97oXGtEAO2Gjq8a3V8k4wcwbJHqF9HwOmJGW6OWP6aX0kgbzm-VtK19iNucM4z54NcJq8-YBvWuy7QOpcQQpBkWvjO9m)www.praetorian.com](https://www.praetorian.com/blog/gladius-automatic-responder-cracking/)
    
    Hashcat output during cracking
    
3. **Ergebnis überprüfen:**
    
    - **Passwort gefunden:** Wenn Hashcat das Passwort in der Wörterliste findet, wird es in der Ausgabe als "**Cracked: ...**" angezeigt und in der Datei `cracked.txt` gespeichert.
        
        [![Bildmotiv: Hashcat output  cracked password](https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS0vA3srJkIBc-0RSAAnJixsh8ddzO4Xed86bUngH68lmnlDpIgqWo-guXjYZed)Wird in einem neuen Fenster geöffnet](https://delinea.com/blog/5-most-popular-password-cracking-tools-and-how-to-protect-your-enterprise)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcTRXe0dNT3O-snOLV5hXj9yoLbKqDMY_2bF3ft1xOPuspkFvhRCFBIMBnBntoY1aB1iAxPEvPTy-OUsW-4gYdPXIbQpUEA)delinea.com](https://delinea.com/blog/5-most-popular-password-cracking-tools-and-how-to-protect-your-enterprise)
        
        Hashcat output cracked password
        
    - **Passwort nicht gefunden (Wörterbuch erschöpft):** Wenn Hashcat alle Wörter in der Wörterliste durchprobiert hat, ohne das Passwort zu finden, wird in der Ausgabe "**Status: Exhausted**" angezeigt und die Datei `cracked.txt` bleibt leer oder enthält keine relevanten Informationen.
        
        [![Bildmotiv: Hashcat output  password not found](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTh1crYQH4TmVJCYqy52XJZmCayay2aQ1VJVHgzXPlFR2HbMy_iH9bgRurAD7dk)Wird in einem neuen Fenster geöffnet](https://www.vaadata.com/blog/how-to-securely-store-passwords-in-database/)[![](https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcT9hlfuG9HfCcqVCFSSdh4lC6GZIPOA3aEfXmJqH8UOtdbyCtVjgQ-6wGrDkGFqse0eq_0nhgbcSAgFR5pUKXxp4kSHu3Cx5O8b)www.vaadata.com](https://www.vaadata.com/blog/how-to-securely-store-passwords-in-database/)
        
        Hashcat output password not found
        

**Schritt 5 (Optional): Geknacktes Passwort überprüfen (im Testnetzwerk)**

Wenn Hashcat erfolgreich ein Passwort gefunden hat, können Sie dieses Passwort (das in `cracked.txt` steht) verwenden, um zu überprüfen, ob Sie sich damit mit Ihrem Testgerät mit dem WLAN-Netzwerk verbinden können (ausschließlich im Testnetzwerk, **niemals in fremden Netzwerken ohne Genehmigung!**).

**Wichtige Hinweise und Sicherheitsvorkehrungen:**

- **Ethik und Legalität (wiederholte Warnung):** Das Durchführen dieser Schritte ohne ausdrückliche Genehmigung ist illegal und unethisch. Nutzen Sie dieses Wissen nur in autorisierten Umgebungen und zu rein edukativen Zwecken.
- **Stärke des Passworts entscheidend:** Der Erfolg einer Dictionary-Attacke hängt stark von der Stärke des WLAN-Passworts und der Qualität der verwendeten Wörterliste ab. Starke, zufällige Passwörter sind sehr schwer bis unmöglich mit Dictionary-Attacken zu knacken.
- **Zeitaufwand:** Das Knacken von Passwörtern kann sehr zeitaufwendig sein, abhängig von der Komplexität des Passworts, der Größe der Wörterliste und der Rechenleistung Ihrer Hardware.
- **Hashcat-Modus und Optionen:** Stellen Sie sicher, dass Sie den korrekten Hashcat-Modus für WPA/WPA2 (z.B. `-m 22000` oder `-m 2500`) und geeignete Attackmodi (`-a`) verwenden. Experimentieren Sie mit verschiedenen Optionen, um die Effizienz zu optimieren (in autorisierten Umgebungen!).
- **Schutzmaßnahmen:** Verwenden Sie immer starke Passwörter für Ihr WLAN, aktivieren Sie WPA3-Verschlüsselung (wenn möglich), deaktivieren Sie WPS und implementieren Sie weitere Sicherheitsmaßnahmen, um Ihr WLAN vor solchen Angriffen zu schützen (wie im vorherigen Abschnitt ausführlich beschrieben).

**Zusammenfassend:** Diese Schritt-für-Schritt-Anleitung demonstriert die Vorgehensweise einer Brute-Force-Attacke auf WLAN mit Wireshark und Hashcat. Wireshark spielt eine _optionale_ Rolle bei der Überprüfung des Handshakes, während Hashcat das eigentliche Passwort-Cracking durchführt. Es ist entscheidend, diese Informationen verantwortungsbewusst zu nutzen und sich der rechtlichen und ethischen Implikationen bewusst zu sein. Starke Passwörter und moderne Verschlüsselungsmethoden sind die beste Verteidigung gegen solche Angriffe.