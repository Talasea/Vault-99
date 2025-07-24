
Eine Netzmaske, auch als Netzwerkmaske oder Subnetzmaske bezeichnet, ist ein wichtiger Bestandteil der IP-Adresse, die in Rechnernetzen verwendet wird, um festzulegen, welche IP-Adressen ein Gerät im eigenen Netz erreichen kann, und für welche Zielnetze Datenpakete an einen Router weitergeleitet werden müssen. Hier ist eine detaillierte Erklärung:

- **Funktion der Netzmaske**: Die Netzmaske ist eine Bitmaske, die im Netzprotokoll IPv4 verwendet wird, um den Netz- und Hostanteil einer IP-Adresse zu definieren. Sie legt fest, welche Bit-Positionen innerhalb der IP-Adresse für die Adressierung des Netzanteils und des Hostanteils genutzt werden sollen.
- **Darstellung der Netzmaske**: Eine IPv4-Netzmaske besteht aus 32 Bits und wird normalerweise in punktierter Dezimalschreibweise dargestellt, wie z.B. 255.255.255.0.
- **Bestimmung des Netzanteils**: Der Netzanteil einer IP-Adresse ergibt sich durch die bitweise logische UND-Verknüpfung der IP-Adresse mit der Netzmaske. Die Netzmaske kennzeichnet die Verwendung der Bits für die Adressierung von Netzen.
- **Bestimmung des Hostanteils**: Nach der bitweisen Negation der Netzmaske wird der Hostanteil abgetrennt. Die Bits, die in der Netzmaske als Nullen markiert sind, werden für die Adressierung des Geräteanteils verwendet.
- **Präfixlänge**: Anstelle einer Subnetzmaske kann der für die Adressierung des Netzanteils genutzte Bereich auch mit der Angabe einer Präfixlänge spezifiziert werden.
- **Effiziente Adressnutzung**: Netzmasken sind wichtig, um die IP-Adressen effizient zu nutzen, indem sie Subnetze definieren und sicherstellen, dass jedes Subnetz über genügend Adressen verfügt, um seine Geräte unterzubringen.
- **Verbesserung der Sicherheit**: Durch die Nutzung von Netzmasken kann die Sicherheit eines Netzwerks verbessert werden, da Datenpakete nur innerhalb des gleichen Netzwerks bleiben, wenn sie nicht an einen Router weitergeleitet werden müssen.
- **Netzwerkverwaltung**: Netzmasken erleichtern die Netzwerkverwaltung, indem sie die Verwaltung von großen Netzwerken in kleinere, leichter zu verwaltende Teile aufteilen.
- **Beispiel**: Für die IP-Adresse 192.168.1.129 und die Netzmaske 255.255.255.0 ergibt sich der Netzanteil 192.168.1.0 und der Hostanteil 0.0.0.129.
- **Subnetting**: Netzmasken werden oft bei der Subnetzierung verwendet, um große Netzwerke in kleinere, verwaltable Teile aufzuteilen, was sowohl die Effizienz als auch die Sicherheit erhöht.



https://www.livewatch.de/de/tools/subnetz/rechner

https://teltonika-networks.com/de/newsroom/understanding-netmask-a-comprehensive-guide-to-network-subnetting

**Was ist eine Netzwerkmaske?**

Eine Netzwerkmaske ist ein 32-Bit-Wert, der in der IP-Adressierung (IPv4) verwendet wird, um den Netzwerk- und Hostteil einer IP-Adresse zu trennen. Sie bestimmt, welche Geräte sich im selben lokalen Netzwerk befinden und welche Geräte über einen Router erreichbar sind.

**Funktionsweise**

- **Trennung von Netzwerk- und Hostteil**:
    - Die Netzwerkmaske "maskiert" im Prinzip den Netzwerkanteil einer IP-Adresse.
    - Bits in der Netzwerkmaske, die auf 1 gesetzt sind, kennzeichnen den Netzwerkteil der IP-Adresse.
    - Bits, die auf 0 gesetzt sind, kennzeichnen den Hostteil.
- **Bestimmung des Netzwerks**:
    - Durch eine bitweise UND-Verknüpfung der IP-Adresse mit der Netzwerkmaske wird die Netzwerkadresse ermittelt.
    - Geräte im selben Netzwerk haben die gleiche Netzwerkadresse.
- **Bestimmung der Host-Adressen**:
    - Der restliche Teil der IP-Adresse, wird dem Host zugewiesen.

**Aufbau einer Netzwerkmaske**

- **32-Bit-Wert**:
    - Eine Netzwerkmaske besteht aus 32 Bits, genau wie eine IPv4-Adresse.
- **Darstellung**:
    - Sie wird üblicherweise in der gleichen punktierten Dezimalschreibweise wie eine IP-Adresse dargestellt, z. B. 255.255.255.0.
    - Alternative dazu ist die CIDR Notation. /24 entspricht 255.255.255.0.
- **Aufbau der Bits**:
    - Die Bits in der Netzwerkmaske sind immer zusammenhängend. Das bedeutet, dass alle 1-Bits am Anfang stehen und alle 0-Bits am Ende.

**Beispiel**

Nehmen wir die IP-Adresse 192.168.1.100 und die Netzwerkmaske 255.255.255.0.

- **IP-Adresse (binär)**:
    - 11000000.10101000.00000001.01100100
- **Netzwerkmaske (binär)**:
    - 11111111.11111111.11111111.00000000
- **Netzwerkadresse (bitweise UND-Verknüpfung)**:
    - 11000000.10101000.00000001.00000000
    - entspricht 192.168.1.0

In diesem Beispiel:

- Die ersten 24 Bits (die 1-Bits in der Netzwerkmaske) kennzeichnen den Netzwerkteil (192.168.1).
- Die letzten 8 Bits der IP-Adresse kennzeichnen den Host.

**Wichtige Punkte**

- **Standard-Netzwerkmasken**:
    - Es gibt Standard-Netzwerkmasken für verschiedene Netzwerkklassen (A, B, C), aber diese Klassifizierung wird heute weitgehend durch CIDR (Classless Inter-Domain Routing) ersetzt.
- **Subnetting**:
    - Netzwerkmasken werden verwendet, um ein größeres Netzwerk in kleinere Subnetze zu unterteilen. Dies ermöglicht eine effizientere Nutzung von IP-Adressen.