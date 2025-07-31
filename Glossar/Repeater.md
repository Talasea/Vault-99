- **Kerndefinition:** Ein **Repeater** ist ein einfaches elektronisches Netzwerkgerät, das auf der untersten Schicht des OSI-Modells, der Bitübertragungsschicht (Layer 1), arbeitet. Seine einzige Funktion ist es, ein ankommendes elektrisches oder optisches Signal zu empfangen, es aufzubereiten, zu verstärken und neu zu senden, um die Reichweite eines Netzwerks über die physikalischen Grenzen eines einzelnen Kabelsegments hinaus zu erweitern.
    
- **Detaillierte Erläuterung / Funktionsweise:**
    
    - **Prozess:** Ein Repeater besitzt keinerlei Intelligenz oder Adressverständnis. Er analysiert weder die MAC- noch die IP-Adressen der Datenpakete. Er nimmt lediglich den an einem Port ankommenden Bitstrom, regeneriert ihn auf seine ursprüngliche Signalstärke und sendet eine exakte Kopie an den anderen Port weiter.
        
    - **Nachteile:** Da er keine Daten filtert, leitet er alles weiter – Nutzdaten, Broadcast-Nachrichten und auch fehlerhafte Pakete oder Datenkollisionen. Alle an einen Repeater angeschlossenen Segmente bilden eine einzige, große **Kollisionsdomäne** und **Broadcast-Domäne**.
        
    - **Zweck:** Der historische Zweck war die Überwindung der Längenbeschränkungen von Kabeln, z. B. bei Ethernet über Koaxialkabel (10BASE2) oder Twisted-Pair-Kabel (10BASE-T).
        
- **Einordnung in den Gesamtkontext:** Der Repeater ist die technologisch primitivste Form eines Netzwerk-Kopplungselements. Er wurde in modernen Netzwerken fast vollständig durch intelligentere Geräte abgelöst:
    
    - **Hubs:** Sind im Grunde Repeater mit mehreren Ports (Multi-Port Repeater).
        
    - **Bridges / Layer-2-Switches:** Arbeiten auf Schicht 2, verstehen MAC-Adressen, filtern den Verkehr und trennen Kollisionsdomänen.
        
    - **Router:** Arbeiten auf Schicht 3, verstehen IP-Adressen und trennen Broadcast-Domänen. In WLAN-Netzwerken findet das Konzept als **WLAN-Repeater** oder Range Extender weiterhin Anwendung.
        
- **Sicherheitsaspekte:** Ein Repeater hat keine eigenen Sicherheitsfunktionen. Indem er Netzwerksegmente zu einer großen Kollisionsdomäne verbindet, erhöht er das Risiko, dass ein Angreifer in einem Segment den gesamten Verkehr der verbundenen Segmente mithören kann (Sniffing), da alle Pakete überallhin weitergeleitet werden.
    
- **Praxisbeispiel / Analogie:** Ein Repeater ist wie ein Echo oder ein Papagei mitten in einem langen Flur. Alles, was er von der einen Seite hört, ruft er einfach mit lauter, frischer Stimme auf der anderen Seite wieder aus. Er versteht nicht, was er ruft, und er weiß auch nicht, für wen die Nachricht bestimmt ist.
    
- **Fazit / Bedeutung für IT-Profis:** In modernen kabelgebundenen LANs haben Repeater keine praktische Bedeutung mehr. Für IT-Profis ist das Wissen über ihre Funktionsweise jedoch wichtig für das historische Verständnis der Netzwerkentwicklung und um die fundamentalen Unterschiede zu Switches und Routern zu begreifen. Das Konzept lebt in Form von WLAN-Repeatern weiter, die jedoch oft mit ähnlichen Nachteilen (wie Leistungsreduktion) behaftet sind.