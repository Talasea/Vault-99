- **Kerndefinition:** **Trunking** ist ein Verfahren in geswitchten Netzwerken, das es ermöglicht, den Datenverkehr von mehreren **VLANs (Virtual LANs)** über eine einzige physische Verbindung zu transportieren. Der **IEEE 802.1Q-Standard** definiert die Methode, wie die einzelnen Datenpakete (Frames) markiert werden, um ihre VLAN-Zugehörigkeit zu kennzeichnen.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Wenn ein Frame einen Switch über einen als "Trunk-Port" konfigurierten Port verlässt, fügt der Switch ein kleines, 4 Byte großes **Tag** in den Ethernet-Header ein. Dieses 802.1Q-Tag enthält unter anderem die **VLAN-ID**. Der empfangende Switch liest dieses Tag, weiß so, zu welchem VLAN der Frame gehört, entfernt das Tag und leitet den Frame an die entsprechenden Ports in diesem Ziel-VLAN weiter.
        
    - **Native VLAN:** Ein spezielles VLAN auf einem Trunk, dessen Frames ungetaggt übertragen werden. Dies dient der Abwärtskompatibilität, birgt aber auch Sicherheitsrisiken.
        
- **Einordnung in den Gesamtkontext:** Trunking ist eine Technologie der Schicht 2 (Sicherungsschicht) und eine zwingende Voraussetzung für den Betrieb einer VLAN-basierten Infrastruktur, die sich über mehrere Switches erstreckt. Ohne Trunking müsste für jedes VLAN eine separate physische Verbindung zwischen den Switches gelegt werden, was ineffizient und teuer wäre.
    
- **Sicherheitsaspekte:** Eine fehlerhafte Konfiguration von Trunk-Ports ist ein klassisches Sicherheitsrisiko. Bei einem sogenannten **VLAN-Hopping-Angriff** kann ein Angreifer speziell präparierte Frames senden, um die Grenzen seines eigenen VLANs zu überwinden und auf Daten in anderen VLANs zuzugreifen. Zu den Gegenmaßnahmen gehören die explizite Definition der erlaubten VLANs auf einem Trunk und die sorgfältige Konfiguration des Native VLANs.
    
- **Praxisbeispiel / Analogie:** Stellen Sie sich eine Autobahn vor, die zwei Städte (Switches) verbindet. Trunking ist diese Autobahn. Die verschiedenen VLANs sind wie Buslinien für verschiedene Stadtteile (z. B. Linie 10, Linie 20). Damit der Busfahrer in der Zielstadt weiß, in welchen Stadtteil er fahren muss, hat jeder Bus (Frame) eine gut sichtbare Liniennummer (das 802.1Q-Tag) auf der Anzeige.
    
- **Fazit / Bedeutung für IT-Profis:** Für jeden Netzwerkadministrator ist die Konfiguration von VLANs und Trunk-Ports eine grundlegende und alltägliche Aufgabe. Ein solides Verständnis von 802.1Q ist die Basis für den Aufbau von skalierbaren, segmentierten und sicheren lokalen Netzwerken.