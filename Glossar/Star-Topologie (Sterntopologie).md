- **Kerndefinition:** Die **Sterntopologie** ist eine Netzwerktopologie, bei der jeder einzelne Netzwerkknoten (z. B. Computer, Drucker) über eine eigene, dedizierte Verbindung mit einem zentralen Verteilergerät, wie einem Switch oder Hub, verbunden ist. Alle Kommunikation zwischen den Endgeräten läuft über diesen zentralen Knotenpunkt.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Aufbau:** Die Struktur ähnelt einem Stern, wobei die Endgeräte die Spitzen und der zentrale Verteiler das Zentrum bilden.
        
    - **Vorteile:**
        
        - **Einfache Installation und Erweiterung:** Neue Geräte können einfach durch Anschluss an einen freien Port des zentralen Verteilers hinzugefügt werden.
            
        - **Fehlertoleranz:** Der Ausfall eines einzelnen Endgeräts oder dessen Kabels beeinträchtigt den Rest des Netzwerks nicht.
            
        - **Einfache Fehlersuche:** Probleme lassen sich leicht auf ein bestimmtes Kabel oder Gerät isolieren.
            
    - **Nachteil:** Der zentrale Verteiler stellt einen **Single Point of Failure** dar. Fällt dieses Gerät aus, ist das gesamte Netzwerksegment lahmgelegt.
        
- **Einordnung in den Gesamtkontext:** Die Sterntopologie ist die mit Abstand am weitesten verbreitete Topologie in modernen lokalen Ethernet-Netzwerken (LANs). Sie hat ältere Topologien wie die **Bus-Topologie** (alle Geräte an einem gemeinsamen Kabel) und die **Ring-Topologie** (Geräte in einem geschlossenen Ring) aufgrund ihrer überlegenen Skalierbarkeit und Zuverlässigkeit fast vollständig verdrängt.
    
- **Sicherheitsaspekte:** Die physische Sicherheit des zentralen Verteilers ist von entscheidender Bedeutung. Da der gesamte Datenverkehr über dieses Gerät läuft, muss es in einem gesicherten Bereich (z. B. einem verschlossenen Netzwerkschrank) untergebracht werden, um unbefugten Zugriff zu verhindern. Durch den Einsatz eines Switches anstelle eines Hubs wird die Sicherheit weiter erhöht, da der Switch den Verkehr nur an den jeweiligen Empfänger sendet und nicht an alle.
    
- **Praxisbeispiel / Analogie:** Die Sterntopologie ist wie ein Flugdrehkreuz (Hub-and-Spoke-System). Alle Passagiere, die von einer kleineren Stadt (Endgerät) in eine andere fliegen wollen, fliegen zuerst zum zentralen Drehkreuz (Switch) und steigen dort in den Anschlussflug zu ihrem endgültigen Ziel um.
    
- **Fazit / Bedeutung für IT-Profis:** Für Netzwerkplaner und -administratoren ist die Sterntopologie das Standarddesign für den Aufbau von LANs. Ihre einfache Struktur, Skalierbarkeit und leichte Wartbarkeit machen sie zur idealen Wahl für Büroumgebungen, Rechenzentren und Heimnetzwerke. Das Management des zentralen Verteilers ist eine Kernaufgabe jedes Netzwerkadministrators.