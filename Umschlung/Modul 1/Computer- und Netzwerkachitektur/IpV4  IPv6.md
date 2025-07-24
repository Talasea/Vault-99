
IPv4 ist das Internet-Protokoll, das zurzeit für die Adressierung von Geräten im Internet verwendet wird. Es wurde in den 1980er Jahren eingeführt und ermöglicht jedem Gerät, das an das Internet angeschlossen ist, eine eindeutige Adresse zu besitzen. Diese Adresse wird als IP-Adresse bezeichnet und ermöglicht es, dass Daten korrekt an ihr Ziel gelangen.

Die Struktur einer IPv4-Adresse besteht aus 32 Bits, die normalerweise in vier Oktetten (je 8 Bits) unterteilt sind, die durch Punkte getrennt sind. Jeder Oktett kann Werte zwischen 0 und 255 annehmen. Ein Beispiel für eine IPv4-Adresse ist 192.168.1.1.

IPv4-Adressen können in verschiedene Klassen unterteilt werden (A, B, C, D und E), wobei die Klassen A, B und C am häufigsten verwendet werden. Diese Klassen bestimmen, wie die Bits zwischen Netzwerk- und Host-Teil aufgeteilt werden. Die Subnetzmaske gibt an, welche Teile der IP-Adresse den Netzwerk- und welchen den Host-Teil repräsentieren.

Einige besondere Adressen innerhalb von IPv4 sind die Netzwerkadresse, bei der alle Host-Bits auf 0 gesetzt sind, und die Broadcast-Adresse, bei der alle Host-Bits auf 1 gesetzt sind. Die Adresse 127.0.0.1 ist für Testzwecke reserviert und bezeichnet immer das lokale Gerät.

Aufgrund der begrenzten Anzahl von IPv4-Adressen wurde das klassenlose Inter-Domain Routing (CIDR) eingeführt, um eine flexiblere und effizientere Nutzung des Adressraums zu ermöglichen. Mit CIDR kann ein Netzwerk beliebiger Größe definiert werden, was zu einer besseren Nutzung des Adressraums führt.

IPv4 wird derzeit noch für IP-Adressen von Domains verwendet, obwohl das Nachfolgeprotokoll IPv6 bereits in Verwendung ist, um die Erschöpfung des IPv4-Adressraums zu vermeiden.

https://simpleclub.com/lessons/elektronikerin-ip-adressen-und-subnetting

## IPv6

IPv6, das Internet Protocol Version 6, ist ein von der Internet Engineering Task Force (IETF) seit 1998 standardisiertes Verfahren zur Übertragung von Daten in paketvermittelnden Rechnernetzen, insbesondere dem Internet. Es löst das derzeit noch weit verbreitete IPv4-Protokoll ab und bietet eine erheblich größere Anzahl von Adressen. IPv6 stellt eine 128-Bit-Adressierung her, die über Teilnetze hinweg gültig ist und den Vorgang der Paketweiterleitung zwischen Netzwerken regelt.

- **Adressraum**: IPv6 bietet einen Adressraum von 2128 Adressen, im Vergleich zu 232 bei IPv4, was bedeutet, dass es deutlich mehr Adressen als IPv4 bietet.
- **Header-Format**: Der IPv6-Header ist einfacher und effizienter als der IPv4-Header, da er einige Felder entfernt hat und andere vereinfacht hat.
- **Automatische Konfiguration**: IPv6 ermöglicht die automatische Konfiguration von Adressen, was die Notwendigkeit von DHCP in vielen Fällen reduziert.
- **Routing**: IPv6 regelt den Vorgang der Paketweiterleitung zwischen Netzwerken und bietet verbesserte Unterstützung für Mobile IPv6.
- **Übergangsmechanismen**: Es gibt verschiedene Übergangsmechanismen, die IPv4 und IPv6 miteinander verbinden, wie z.B. Tunneling und Anycast.
- **Adressarten**: IPv6 unterscheidet zwischen globalen unicast-Adressen, die weltweit einzigartig sind, und verbindungslokalen Adressen, die nur im lokalen Netzwerk gültig sind.
- **Fragmentierung**: Im Gegensatz zu IPv4, bei dem Router die Paketfragmentierung durchführen, wird bei IPv6 der Absender gebeten, kleinere Pakete zu senden.
- **Zukunft**: Im Laufe der Zeit soll IPv6 die Version 4 des Internet Protocols (IPv4) vollständig ablösen, da die globale IPv4-Adressvergabe ausgelaufen ist.



https://bitjunkie.org/ipv6-erklaert/


