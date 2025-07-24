
https://www.youtube.com/watch?v=5GSS1iSNrUQ
https://www.livewatch.de/de/tools/subnetz/rechner

https://teltonika-networks.com/de/newsroom/understanding-netmask-a-comprehensive-guide-to-network-subnetting


Subnetting ist eine Methode zur effizienten Organisation und Nutzung eines IP-Adressraums in einem Computernetzwerk. Es ermöglicht es Netzwerkadministratoren, ein größeres Netzwerk in kleinere, handhabbare Einheiten, sogenannte Subnetze, zu unterteilen. Hier sind einige wichtige Punkte zum Verständnis von Subnetting:

- **Netzwerkverkehr**: Ohne Subnetting würde das Internet unter der Datenlast in Sekunden zusammenbrechen, allein schon durch Hello-Pakete. Subnetting reduziert den Netzwerkverkehr, indem es Datenpakete innerhalb eines Subnetzes begrenzt.
- **IP-Adressverwaltung**: Große Netzwerke mit Tausenden von verbundenen Geräten können schnell unübersichtlich werden. Subnetting ermöglicht eine strukturierte Adressvergabe und erleichtert die Verwaltung.
- **Sicherheit**: Durch die Trennung von Subnetzen erhöht sich die Sicherheit, da Angriffe erst andere Netzabschnitte erreichen müssen, um sich weiter auszubreiten.
- **Flexibilität**: Subnetting ermöglicht eine flexible Netzwerkgliederung und optimiert die Nutzung der IP-Adressen.
- **CIDR-Notation**: Die CIDR-Notation (Classless Inter-Domain Routing) wurde eingeführt, um die Subnetzmasken flexibler zu gestalten und die IP-Adressierung an die spezifischen Anforderungen der Organisation anzupassen.
- **Subnetzmaske**: Eine Subnetzmaske ist eine 32-Bit-Zahl, die verwendet wird, um herauszufinden, welcher Teil der IP-Adresse das Netzwerk und welcher Teil den Host repräsentiert.
- **AND-Vergleich**: Der logische AND-Vergleich ist die mathematische Operation, die entscheidet, ob eine bestimmte IP-Adresse zu einem Subnetz gehört. Dies geschieht durch die Anwendung des AND-Operators auf die binäre Darstellung der IP-Adresse und der Subnetzmaske.
- **Netz- und Broadcast-Adresse**: Jedes Subnetz hat eine Netz-Adresse und eine Broadcast-Adresse, die für die Kommunikation innerhalb des Subnetzes verwendet werden.
- **Werkzeuge**: Tools wie ipcalc für Linux-Betriebssysteme oder Advanced IP Scanner für Windows bieten Netzwerkadministratoren die Möglichkeit, Subnetze effizient zu planen und zu verwalten.
- **Praktisches Beispiel**: Ein Unternehmen könnte eine IP-Adresse wie 192.168.1.0 mit einer Subnetzmaske von 255.255.255.0 haben und entscheiden, es in zwei Subnetze zu unterteilen, um die technische Abteilung von der Verwaltungsabteilung zu trennen.


Eine Subnetzmaske ist ein wichtiger Bestandteil des Netzwerkbegriffs, der in Verbindung mit der IP-Adresse verwendet wird, um festzulegen, welche IP-Adressen ein Gerät im eigenen Netzwerk erreichen kann, ohne dass ein Router benötigt wird. Hier sind einige wichtige Punkte zur Subnetzmaske:

- **Definition**: Eine Subnetzmaske ist eine Bitmaske, die im Netzprotokoll IPv4 verwendet wird, um den Netz- und Host-Anteil einer IP-Adresse zu definieren.
- **Funktion**: Sie bestimmt, ob eine Zieladresse innerhalb des gleichen Subnetzes liegt oder ob ein Router für die Weiterleitung benötigt wird.
- **Darstellung**: Eine Subnetzmaske kann in der punktierten Dezimalnotation (z.B. 255.255.255.0) oder in der CIDR-Notation (z.B. /24) dargestellt werden.
- **Bitweise UND-Operation**: Durch die bitweise UND-Operation der IP-Adresse mit der Subnetzmaske wird der Host-Teil der IP-Adresse maskiert, so dass nur die Netzwerkadresse übrig bleibt.
- **Netzanteil und Hostanteil**: Der Netzanteil der IP-Adresse erstreckt sich von links nach rechts, während der Hostanteil von rechts nach links beginnt.
- **Erste und letzte Adresse**: Die erste und letzte Adresse eines IP-Adressbereichs sind die Netzwerk- und Broadcast-Adresse und können nicht an Hosts zugewiesen werden.
- **Subnetzrechner**: Online-Tools helfen dabei, die passende Subnetzmaske für ein Netzwerk zu berechnen.
- **Vorteile**: Die Verwendung von Subnetzmasken verbessert die Adressnutzung, die Sicherheit und die Netzwerkverwaltung.
- **Anwendung**: Subnetzmasken sind besonders nützlich, wenn große Netzwerke in kleinere, verwaltbare Teile unterteilt werden.
- **Beispiel**: Die IP-Adresse 192.168.0.1 mit der Subnetzmaske 255.255.255.0 hat den Netzwerkanteil 192.168.0 und den Hostanteil 1.![[Screenshot 2025-01-02 120153.png]]

![[Screenshot 2025-01-02 124317.png]]