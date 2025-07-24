
Die Maximum Transmission Unit (MTU) ist ein wichtiger Parameter in Netzwerken, der die maximale Größe eines Datenpakets definiert, das ohne Fragmentierung übertragen werden kann. Hier sind einige wesentliche Punkte zur MTU:

- **MTU Definition**: Die MTU gibt die maximale Größe einer Übertragungseinheit einer Netzwerkschnittstelle an, gemessen in Bytes. Sie ist ein hardwareabhängiger Wert, der die Größe der Nutzlast (Payload) des Protokolls der Sicherungsschicht (Schicht 2) des OSI-Modells festlegt.
    
- **MTU Werte**: Die MTU-Werte variieren je nach Netzwerktyp. Zum Beispiel beträgt die MTU für Ethernet 1500 Byte, während sie für WLAN 2312 Byte beträgt.
    
- **PMTU**: Die Path MTU (PMTU) beschreibt die maximale Paketgröße, die entlang der gesamten Wegstrecke übertragen werden kann, ohne einer Fragmentierung zu unterliegen. Sie ist gleich der kleinsten MTU aller Schicht-2-Teilstücke im Pfad.
    
- **MTU und MSS**: Die MTU gibt die Größe des kompletten TCP/IP-Paketes an, während die MSS nur den Platz für die Nutzdaten im TCP/IP-Paket angibt. Beide sind eng miteinander verknüpft, da die MSS auf der MTU basiert.
    
- **Fragmentierung**: Wenn ein Datenpaket größer als die MTU ist, wird es in kleinere Einheiten aufgeteilt, was zu einer höheren Paketanzahl und einem höheren Protokoll-Overhead führt. Dies kann die Übertragungsgeschwindigkeit beeinträchtigen.
    
- **MTU Discovery**: Das Path MTU Discovery (PMTUD) ist ein Verfahren, um die PMTU automatisch zu ermitteln. Es ist in IPv6 Pflicht und in IPv4 optional.
    
- **MTU bei DSL**: Bei DSL-Verbindungen ist die MTU auf 1492 Byte begrenzt, da das PPPoE-Protokoll eine Header-Vergrößerung von 8 Byte erfordert. Dies kann zu Übertragungsproblemen führen, wenn der entfernte Server zu große Pakete sendet.
    

- **MTU-Ermittlung**: Mit dem Befehl `ping -c 1 -s $((1512-28)) -M do www.elektronik-kompendium.de` kann die optimale MTU ermittelt werden. Bei erfolgreicher Ausführung sollte die optimale MTU 1500 Byte betragen.