https://www.ionos.de/digitalguide/server/knowhow/was-ist-arp-adressaufloesung-im-netzwerk/

Das Address Resolution Protocol (ARP) ist ein grundlegendes Netzwerkprotokoll, das dazu dient, IP-Adressen in MAC-Adressen umzuwandeln und umgekehrt.Jedes Gerät im Netzwerk hat sowohl eine IP-Adresse als auch eine MAC-Adresse. Die IP-Adresse identifiziert das Gerät im Netzwerk, während die MAC-Adresse seine physische Adresse ist.Wenn ein Gerät Daten an ein anderes Gerät im Netzwerk senden möchte, benötigt es dessen MAC-Adresse. Der ARP-Cache speichert die Zuordnung zwischen IP- und MAC-Adressen, um die Kommunikation effizient zu gestalten.Wenn die gewünschte Zuordnung im ARP-Cache vorhanden ist, kann das Paket direkt an die MAC-Adresse des Ziels gesendet werden. Falls die Zuordnung nicht vorhanden ist, sendet das Gerät eine ARP-Anfrage an alle Geräte im Netzwerk, um die MAC-Adresse zu ermitteln.

ARP ist ein wesentlicher Bestandteil von IP-Netzwerken und verbessert die Netzwerkeffizienz durch die Reduzierung von Overhead und Latenz.

- **Proxy-ARP**: Erweitert ARP über ein bestimmtes LAN hinaus, indem es als Proxy für ARP-Anfragen fungiert.
    
- **Gratuitous ARP**: Ein Gerät sendet seine IP/MAC-Adresszuordnung ohne Anfrage, um diese bekannt zu machen.
    
- **Reverse ARP (RARP)**: Wird von Geräten verwendet, die ihre IP-Adressen nicht kennen, um diese zu erkennen.
    
- **Inverse ARP (IARP)**: Kann verwendet werden, um die IP-Adresse eines Geräts anhand seiner MAC-Adresse zu erfahren.

ARP arbeitet zwischen den Netzwerkschichten 2 und 3 des OSI-Modells und ist entscheidend für die Weiterleitung von Daten innerhalb eines Subnetzes.