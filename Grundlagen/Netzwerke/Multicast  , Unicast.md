**Unicast**

- **Definition**:
    - Unicast ist eine Eins-zu-Eins-Kommunikationsmethode in einem Netzwerk.
    - Daten werden von einem einzelnen Absender an einen einzelnen Empfänger gesendet.
- **Funktionsweise**:
    - Jedes Datenpaket, das in einem Unicast-Szenario gesendet wird, hat eine eindeutige Zieladresse.
    - Netzwerkgeräte (wie Router und Switches) leiten das Paket basierend auf dieser Zieladresse an den spezifischen Empfänger weiter.
- **Anwendungen**:
    - Webbrowsen (Anforderung einer Webseite von einem Server)
    - E-Mail (Senden einer E-Mail an einen bestimmten Empfänger)
    - Dateiübertragungen (Herunterladen einer Datei von einem Server)
- **Merkmale**:
    - Hohe Zuverlässigkeit für Einzelverbindungen.
    - Ineffizient für die Übertragung von Daten an mehrere Empfänger.

**Multicast**

- **Definition**:
    - Multicast ist eine Eins-zu-Viele-Kommunikationsmethode.
    - Daten werden von einem einzelnen Absender an eine Gruppe von Empfängern gesendet, die sich für den Empfang dieser Daten registriert haben.
- **Funktionsweise**:
    - Multicast verwendet spezielle Multicast-Adressen, um eine Gruppe von Empfängern zu identifizieren.
    - Netzwerkgeräte, die Multicast unterstützen, duplizieren die Datenpakete und senden sie nur an die Netzwerksegmente, in denen sich die registrierten Empfänger befinden.
- **Anwendungen**:
    - Videokonferenzen
    - IPTV (Internet Protocol Television)
    - Online-Spiele
    - Verteilung von Finanzdaten.
- **Merkmale**:
    - Effiziente Nutzung der Bandbreite für die Übertragung von Daten an mehrere Empfänger.
    - Erfordert spezielle Netzwerkunterstützung (z. B. Multicast-fähige Router und Switches).

**Hauptunterschiede auf einen Blick**

- **Kommunikation**: Unicast ist Eins-zu-Eins, während Multicast Eins-zu-Viele ist.
- **Bandbreitennutzung**: Multicast ist effizienter für die Übertragung von Daten an mehrere Empfänger.
- **Netzwerkanforderungen**: Multicast erfordert spezielle Netzwerkunterstützung, während Unicast die Standardmethode für die meisten Netzwerke ist.