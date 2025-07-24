im osi model layer 4 

Das Transmission Control Protocol (TCP) ist ein zentrales Netzwerkprotokoll der Internetprotokollfamilie (TCP/IP). Es sorgt für eine zuverlässige und effiziente Datenübertragung zwischen Computern im Internet.

## Funktionen und Merkmale

- Verbindungsorientiert: TCP erstellt eine logische Verbindung zwischen zwei Endpunkten, bevor Daten übertragen werden.
- Paketvermittelt: TCP teilt Daten in Pakete auf und überträgt sie separat. Die Empfängerrechner müssen die Pakete korrekt zusammenfügen, um den ursprünglichen Datenstrom zu rekonstruieren.
- Flow Control: TCP reguliert den Datenstrom, um sicherzustellen, dass der Empfänger die Daten aufnehmen kann, ohne dass die Übertragung blockiert wird.
- Fehlerkorrektur: TCP überprüft die Pakete auf Fehler und fordert Wiederholung von fehlerhaft übertragenen Paketen an.
- Sequenznummerierung: TCP vergibt eine eindeutige Sequenznummer für jeden Paketteil, um sicherzustellen, dass die Pakete korrekt an ihrem richtigen Platz im Datenstrom platziert werden.

## Anwendungsbereiche

- Wide Area Networks (WANs): TCP ist speziell für die Übertragung von Daten über weite Entfernungen konzipiert und wird daher in WANs eingesetzt.
- Internet: TCP ist ein wichtiger Bestandteil des Internets und wird von nahezu allen modernen Betriebssystemen unterstützt.

## Entwicklungsgeschichte

- Entwickelt wurde TCP von Robert E. Kahn und Vinton G. Cerf in den 1970er Jahren.
- Die erste Standardisierung von TCP erfolgte 1981 als RFC 793.
- Seitdem wurden viele Erweiterungen und Verbesserungen vorgenommen, die in neuen RFCs dokumentiert sind.

## Zusammenfassung

Insgesamt ist TCP ein zuverlässiges, verbindungsorientiertes und paketvermitteltes Transportprotokoll, das für die Übertragung von Daten zwischen Computern im Internet eingesetzt wird. Seine Funktionen und Merkmale garantieren eine effiziente und fehlerfreie Datenübertragung, was für die meisten Anwendungen im Internet erforderlich ist.![[TCP UDP.png]]





TCP/IP steht für Transmission Control Protocol und Internet Protocol und ist eine Gruppe von Netzwerkprotokollen, die für den Datentransfer in dezentralen Netzwerken wie dem Internet zuständig sind. Es handelt sich dabei nicht um ein einzelnes Protokoll, sondern um eine Familie von Protokollen, die zusammenarbeiten, um Datenpakete zu übertragen und zu routen. Das IP-Protokoll adressiert und routet Datenpakete, während TCP für die Zuverlässigkeit und Reihenfolge der Datenpakete sorgt und sicherstellt, dass sie vollständig beim Empfänger ankommen. Zusammen ermöglichen diese Protokolle eine durchgängige Kommunikation von Host zu Host über Netzgrenzen hinweg.