
verbindungs los 

**Einführung in UDP**: Das User Datagram Protocol (UDP) ist ein verbindungsloses Netzwerkprotokoll, das zur Transportschicht der Internetprotokollfamilie gehört. Es ermöglicht Anwendungen den Versand von Datagrammen in IP-basierten Rechnernetzen.

- **Funktion**: UDP ermöglicht die Übertragung von Daten ohne vorherige Verbindungsaufnahme zwischen dem Sender und dem Empfänger. Dies ermöglicht eine schnelle Übertragung von Daten, aber es kann auch dazu führen, dass Pakete während der Übertragung verloren gehen.
- **Header**: Der UDP-Header enthält Informationen wie die Quell- und Ziel-Portnummern, die Paketlänge und eine optionale Prüfsumme.
- **Verbindungslosigkeit**: UDP ist ein verbindungsloses Protokoll, was bedeutet, dass der Absender nicht weiß, ob seine verschickten Datenpakete angekommen sind. Es gibt keine Bestätigungen beim Datenempfang.
- **Anwendungsbereiche**: UDP wird typischerweise bei DNS-Anfragen, VPN-Verbindungen, Audio- und Video-Streaming verwendet, da es eine schnelle und effiziente Übertragung von Daten ermöglicht.

**Vorteile und Nachteile**:

- **Vorteile**: Schnelle Übertragung von Daten, geringer Overhead, einfache Verarbeitung.
- **Nachteile**: Keine Garantie für die Zustellung von Paketen, Pakete können verloren gehen oder in einer anderen Reihenfolge empfangen werden, als sie gesendet wurden.![[TCP UDP.png]]