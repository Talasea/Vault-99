Capture Filter

<font color="#ff0000">Filter setzen heist das man vorher einstellt was aufgezeichnet wird.</font>

Wireshark verwendet zwei Arten von Filtern: Capture-Filter und Anzeigefilter. Capture-Filter werden verwendet, um die Menge der aufgezeichneten Pakete zu reduzieren, indem sie Pakete ausschließen, die nicht den Filterkriterien entsprechen. Diese Filter werden vor der Aufzeichnung angewendet und nutzen die BPF-Syntax, die auch von tcpdump verwendet wird.

Um einen Capture-Filter in Wireshark zu verwenden, können Sie ihn direkt in das Filterfeld eintragen. Einige Beispiele für Capture-Filter sind:

- `host IP-Adresse`: Dieser Filter beschränkt das Abfangen auf den Datenverkehr zu und von der angegebenen IP-Adresse.
- `net 192.168.0.0/24`: Dieser Filter erfasst den gesamten Datenverkehr im angegebenen Subnetz.
- `dst host IP-Adresse`: Dieser Filter erfasst nur Pakete, die an die angegebene IP-Adresse gesendet werden.
- `port 53`: Dieser Filter erfasst nur den Datenverkehr auf Port 53.
- `port not 53 and not arp`: Dieser Filter erfasst alle Datenverkehr außer DNS- und ARP-Verkehr.

Capture-Filter sind in ihrer Anwendung nicht ganz trivial, da sie eine Syntax aus Byte-Offsets, Hex-Werten und Masken verwenden, die mit Wahrheitswerten verknüpft werden, um die Daten zu filtern. Sie sind in ihrer Anwendung kryptischer als Anzeigefilter.


Display Filter 

Wireshark bietet eine eigene Sprache für Anzeigefilter, die es ermöglicht, die Anzeige von Paketen präzise zu kontrollieren. Diese Filter können verwendet werden, um nach der Anwesenheit eines Protokolls oder Feldes, dem Wert eines Feldes oder sogar dem Vergleich von zwei Feldern zu filtern. Diese Vergleiche können mit logischen Operatoren wie “und” und “oder” und Klammern zu komplexen Ausdrücken kombiniert werden.

Ein einfacher Anzeigefilter besteht darin, ein einzelnes Protokoll anzuzeigen. Zum Beispiel, um nur TCP-Pakete anzuzeigen, tippt man `tcp` in das Anzeigefilter-Feld von Wireshark ein. Ähnlich kann man auch nach einem bestimmten Feld filtern. Zum Beispiel, um nur HTTP-Anfragen anzuzeigen, tippt man `http.request` in das Anzeigefilter-Feld ein.

Für das Filtern nach bestimmten IP-Adressen oder MAC-Adressen gibt es spezielle Filter:

- Um nur Pakete anzuzeigen, die von oder an eine bestimmte IP-Adresse gesendet oder empfangen werden, verwendet man `ip.addr == 192.168.0.1`.
- Um nur Pakete anzuzeigen, die von oder an eine bestimmte MAC-Adresse gesendet oder empfangen werden, verwendet man `eth.addr == 00.07.0a.15.c3.fa`.

Es gibt auch Operatoren für logische Verknüpfungen:

- `&&` oder `and` für “und”
- `||` oder `or` für “oder”
- `!` oder `not` für “nicht”

Zusätzlich können reguläre Ausdrücke (`matches` oder `~`) verwendet werden, um Text in Feldern oder Protokollen zu suchen. Zum Beispiel, um HTTP-Anfragen zu filtern, bei denen die letzte Zeichenfolge in der URI “gl=se” ist, verwendet man `http.request.uri matches "gl=se$"`.

Wireshark bietet auch die Möglichkeit, Filter als Schaltflächen zu speichern, um sie schnell wiederzuverwenden.