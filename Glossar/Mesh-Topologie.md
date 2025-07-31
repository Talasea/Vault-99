- **Kerndefinition:** Eine **Mesh-Topologie** ist eine Netzwerktopologie, bei der die Netzwerkknoten (wie Computer, Switches oder Router) untereinander mit mehreren Verbindungen verknüpft sind. In einem vollständig vermaschten Netz ist jeder Knoten direkt mit jedem anderen Knoten verbunden, während in einem teilweise vermaschten Netz nur einige Knoten mehrfach verbunden sind.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Arten:**
        
        - **Vollständige Vermaschung (Full Mesh):** Bietet maximale Redundanz, da der Ausfall einer einzelnen Verbindung die Kommunikation zwischen zwei Knoten nicht unterbricht. Der Verkabelungsaufwand und die Anzahl der benötigten Ports sind jedoch extrem hoch (n * (n-1) / 2 Verbindungen für n Knoten).
            
        - **Teilweise Vermaschung (Partial Mesh):** Ein pragmatischer Kompromiss, bei dem nur kritische Knoten (z. B. Core-Router) mehrfach verbunden werden, um Redundanz an wichtigen Punkten zu schaffen, ohne die Kosten und Komplexität einer vollständigen Vermaschung zu verursachen.
            
    - **Prozess:** Daten können auf verschiedenen Wegen durch das Netz geleitet werden. Routing-Protokolle wie OSPF (Open Shortest Path First) sind entscheidend, um dynamisch den besten Pfad zu finden und bei einem Verbindungsausfall automatisch auf eine alternative Route auszuweichen.
        
- **Einordnung in den Gesamtkontext:** Die Mesh-Topologie steht im Gegensatz zu anderen Netzwerktopologien wie der **Stern-Topologie** (alle Knoten sind mit einem zentralen Punkt verbunden) oder der **Bus-Topologie** (alle Knoten teilen sich ein einziges Übertragungsmedium). Während ein Sternnetzwerk durch den Ausfall des zentralen Knotens komplett lahmgelegt wird, ist ein Mesh-Netzwerk weitaus robuster. Das Internet selbst ist das größte Beispiel für ein teilweise vermaschtes Netz.
    
- **Sicherheitsaspekte:** Die inhärente Redundanz der Mesh-Topologie erhöht die **Verfügbarkeit** und **Ausfallsicherheit** des Netzwerks, was ein zentrales Sicherheitsziel ist. Ein Denial-of-Service-Angriff, der eine einzelne Verbindung lahmlegt, hat eine deutlich geringere Auswirkung als in anderen Topologien. Die Komplexität des Routings kann jedoch auch eine Herausforderung darstellen und erfordert eine sorgfältige Konfiguration, um Routing-Schleifen oder andere Fehlkonfigurationen zu vermeiden.
    
- **Praxisbeispiel / Analogie:** Ein Mesh-Netzwerk ist wie das Straßennetz einer gut geplanten Stadt. Zwischen zwei wichtigen Punkten (z. B. dem Rathaus und dem Krankenhaus) gibt es mehrere mögliche Routen – über die Hauptstraße, durch Wohngebiete oder über eine Umgehungsstraße. Wird eine Straße wegen einer Baustelle gesperrt (Verbindungsausfall), kann der Verkehr einfach umgeleitet werden, und das Ziel bleibt erreichbar.
    
- **Fazit / Bedeutung für IT-Profis:** Die Mesh-Topologie ist das Fundament für den Aufbau hochverfügbarer und robuster Netzwerke. Netzwerkarchitekten nutzen sie für das Design von WAN-Backbones und den Kern von großen Unternehmensnetzwerken. Das Verständnis der Vor- und Nachteile von vollständiger und teilweiser Vermaschung ist entscheidend, um ein optimales Gleichgewicht zwischen Kosten, Komplexität und Ausfallsicherheit zu finden.