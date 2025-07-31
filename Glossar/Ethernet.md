### 1. Kerndefinition

**Ethernet** ist die weltweit dominierende Technologie für kabelgebundene lokale Netzwerke (LANs). Es handelt sich um eine Familie von Netzwerkprotokollen und -standards, die definieren, wie Daten in einem LAN formatiert, adressiert und übertragen werden. Ursprünglich in den 1970er Jahren bei Xerox PARC entwickelt, ist Ethernet heute im Standard **IEEE 802.3** spezifiziert und deckt sowohl die Bitübertragungsschicht (Layer 1) als auch die Sicherungsschicht (Layer 2) des OSI-Modells ab.

### 2. Detaillierte Erläuterung / Funktionsweise

**Schlüsselkomponenten:**

- **MAC-Adresse (Media Access Control):** Eine weltweit eindeutige, 48-Bit lange Hardware-Adresse, die in die Netzwerkschnittstelle (NIC) eines Geräts "eingebrannt" ist. Ethernet verwendet MAC-Adressen, um Datenpakete (Frames) innerhalb eines lokalen Netzwerks an das korrekte Zielgerät zu adressieren.
    
- **Ethernet-Frame:** Die grundlegende Dateneinheit, die über ein Ethernet-Netzwerk gesendet wird. Ein Frame hat eine standardisierte Struktur, die unter anderem die Ziel-MAC-Adresse, die Quell-MAC-Adresse, ein Typ-Feld (das das Protokoll der höheren Schicht, z. B. IP, anzeigt), die eigentlichen Nutzdaten (Payload) und eine Prüfsumme (FCS - Frame Check Sequence) zur Fehlererkennung enthält.
    
- **Zugriffsverfahren:**
    
    - **CSMA/CD (historisch):** In alten, Hub-basierten Netzwerken wurde CSMA/CD verwendet, um den Zugriff auf das geteilte Medium zu regeln und Kollisionen zu handhaben.
        
    - **Full-Duplex (modern):** In modernen, geswitchten Netzwerken gibt es dedizierte Verbindungen zwischen dem Endgerät und dem Switch-Port. Dies ermöglicht den Full-Duplex-Betrieb, bei dem gleichzeitig gesendet und empfangen werden kann, wodurch Kollisionen eliminiert und CSMA/CD überflüssig gemacht wird.
        
- **Übertragungsmedien und Geschwindigkeiten:** Ethernet hat sich über die Jahre dramatisch weiterentwickelt:
    
    - **10BASE5/10BASE2 (historisch):** 10 Mbit/s über dicke/dünne Koaxialkabel.
        
    - **10BASE-T:** 10 Mbit/s über Twisted-Pair-Kabel.
        
    - **Fast Ethernet (100BASE-TX):** 100 Mbit/s über Twisted-Pair (Cat5).
        
    - **Gigabit Ethernet (1000BASE-T):** 1 Gbit/s über Twisted-Pair (Cat5e/Cat6).
        
    - **10-Gigabit-Ethernet (10GBASE-T)** und schneller (40 GbE, 100 GbE) über höherwertige Kupferkabel (Cat6a/Cat7) oder Glasfaserkabel.
        

### 3. Einordnung in den Gesamtkontext

Ethernet ist die De-facto-Standardtechnologie für **Layer 1 und 2** in fast allen kabelgebundenen LANs, von Heimnetzwerken bis hin zu riesigen Rechenzentren. Es bildet die Grundlage, auf der höhere Protokolle wie das **Internet Protocol (IP)** (Layer 3) und **TCP/UDP** (Layer 4) aufsetzen. Ein Switch, das zentrale Gerät in einem modernen Ethernet-LAN, arbeitet auf Layer 2 und trifft Weiterleitungsentscheidungen basierend auf den MAC-Adressen im Ethernet-Frame. Router, die Netzwerke miteinander verbinden (z. B. ein LAN mit dem Internet), arbeiten auf Layer 3 und verwenden IP-Adressen.

### 4. Sicherheitsaspekte

Da Ethernet die Basistechnologie ist, sind viele Netzwerkangriffe auf dieser Ebene angesiedelt:

- **MAC-Spoofing:** Ein Angreifer fälscht die MAC-Adresse seines Geräts, um sich als ein anderes, legitimes Gerät auszugeben und so z. B. Zugriffskontrollen zu umgehen.
    
- **MAC-Flooding:** Ein Angreifer überflutet einen Switch mit einer riesigen Anzahl von Frames mit unterschiedlichen Quell-MAC-Adressen. Dies überlastet die MAC-Adresstabelle des Switches, der daraufhin in einen "Fail-Open"-Modus schaltet und alle eingehenden Pakete an alle Ports sendet – er verhält sich wie ein Hub. Dies ermöglicht dem Angreifer, den gesamten Netzwerkverkehr mitzuschneiden (Sniffing). **Port Security** ist eine Gegenmaßnahme auf Switches, die dies verhindert.
    
- **ARP-Poisoning/Spoofing:** Ein Layer-2-Angriff, bei dem ein Angreifer gefälschte ARP-Antworten (Address Resolution Protocol) sendet, um den Verkehr zwischen zwei Geräten (z. B. einem Client und dem Gateway) über seinen eigenen Rechner umzuleiten (Man-in-the-Middle-Angriff).
    

### 5. Praxisbeispiel / Analogie

**Analogie: Ein lokales Postsystem in einem großen Gebäude** Stellen Sie sich ein großes Bürogebäude als ein LAN vor.

- **MAC-Adresse:** Die eindeutige Raumnummer jedes Büros (z. B. "A-101"). Diese ist fest und ändert sich nicht.
    
- **IP-Adresse:** Der Name der Person oder Abteilung, die gerade in diesem Raum arbeitet (z. B. "Buchhaltung"). Diese kann sich ändern, wenn jemand umzieht.
    
- **Ethernet-Frame:** Ein interner Umschlag für die Hauspost. Auf dem Umschlag steht "An: Raum B-205" (Ziel-MAC) und "Von: Raum A-101" (Quell-MAC). Im Umschlag befindet sich der eigentliche Brief ("An: Personalabteilung" - die IP-Information).
    
- **Switch:** Die zentrale Poststelle im Erdgeschoss. Die Poststelle hat eine Liste (MAC-Adresstabelle), in der steht, welcher Mitarbeiter (bzw. welche Raumnummer) über welchen Flur (Switch-Port) erreichbar ist. Sie schaut nur auf die Raumnummer auf dem Umschlag und leitet ihn gezielt in den richtigen Flur weiter, ohne den Brief darin zu lesen.
    
- **Hub (historisch):** Ein inkompetenter Postbote, der jeden Umschlag einfach in allen Fluren ausruft, in der Hoffnung, dass der richtige Empfänger ihn sich nimmt.
    

### 6. Fazit / Bedeutung für IT-Profis

Ein solides Verständnis von Ethernet ist für jeden IT-Profi, der mit Netzwerkinfrastruktur arbeitet, absolut fundamental. Es ist die unsichtbare, aber allgegenwärtige Grundlage der modernen digitalen Kommunikation. Kenntnisse über Ethernet-Standards, Frame-Aufbau, MAC-Adressierung und die Funktionsweise von Switches sind unerlässlich für die Planung, Implementierung, Fehlerbehebung und Absicherung von Netzwerken. Ohne ein Verständnis von Ethernet ist eine tiefgreifende Analyse von Netzwerkproblemen oder Sicherheitsvorfällen praktisch unmöglich.