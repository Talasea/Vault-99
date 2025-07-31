- **Kerndefinition:** Der **RSSI (Received Signal Strength Indicator)** ist ein Messwert, der die relative Stärke eines empfangenen Funksignals angibt. Er wird von drahtlosen Geräten, insbesondere im WLAN, verwendet, um die Qualität der Verbindung zu einem Access Point zu bewerten und Roaming-Entscheidungen zu treffen.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** RSSI misst die Leistung des Funksignals, das die Antenne eines Geräts erreicht. Der Wert wird in der Regel in Dezibel Milliwatt (dBm) angegeben, einer logarithmischen Skala, bei der die Werte negativ sind. Ein Wert näher an 0 ist besser (z. B. ist -55 dBm ein stärkeres Signal als -75 dBm).
        
    - **Zweck und Anwendungsfälle:** WLAN-Clients überwachen kontinuierlich den RSSI-Wert der verbundenen und benachbarten Access Points. Fällt der Wert unter einen bestimmten Schwellenwert, sucht das Gerät aktiv nach einem Access Point mit einem besseren Signal, um dorthin zu wechseln (Roaming). Netzwerk-Tools verwenden RSSI-Werte zur Erstellung von Heatmaps bei einer Funkausleuchtung.
        
- **Einordnung in den Gesamtkontext:** RSSI ist eine fundamentale Metrik der Bitübertragungsschicht (Layer 1) in der Funkkommunikation. Für eine aussagekräftige Bewertung der Verbindungsqualität wird der RSSI oft zusammen mit dem **Signal-Rausch-Verhältnis (SNR)** betrachtet, das die Signalstärke ins Verhältnis zum Hintergrundrauschen setzt. Ein hoher RSSI ist nutzlos, wenn auch das Rauschen sehr hoch ist.
    
- **Sicherheitsaspekte:** RSSI ist keine direkte Sicherheitsfunktion. Es kann jedoch zur Standortermittlung (Lokalisierung) von Geräten innerhalb eines Funknetzes verwendet werden. Sicherheits-Tools können RSSI-Werte auch nutzen, um die physische Nähe von potenziell bösartigen Geräten oder nicht autorisierten Access Points (Rogue APs) zu erkennen.
    
- **Praxisbeispiel / Analogie:** Der RSSI-Wert ist vergleichbar mit der Lautstärke, mit der man eine Person über eine Entfernung sprechen hört. Steht die Person direkt neben einem, ist die Stimme laut und klar (ein guter dBm-Wert wie -50 dBm). Entfernt sich die Person, wird die Stimme immer leiser (ein schlechterer dBm-Wert wie -80 dBm), bis man sie gar nicht mehr hört.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerk-Administratoren ist der RSSI-Wert ein entscheidendes Diagnosewerkzeug zur Fehlersuche bei WLAN-Problemen und eine Schlüsselmetrik bei der Planung und Überprüfung von Funknetzen (RF Survey). Das Verständnis der dBm-Skala und der idealen Signalstärken für verschiedene Anwendungen (z. B. Daten, VoIP) ist für den Aufbau eines performanten WLANs unerlässlich.