
# Modem (analog)

Ein Modem ist eine Datenübertragungseinrichtung, um digitale Signale in analoge Signale umzuwandeln und über ein Kommunikationsnetz zu übertragen. Zusätzlich ist ein Modem mit einer Logik ausgestattet, um zu einer Gegenstelle (z. B. ein anderes Modem) ein Verbindung aufzubauen, Verbindungen anzunehmen und Daten zu übertragen. Zum Beispiel als Zugang zum Internet.

![Datenübertragung über das Telefonnetz](https://www.elektronik-kompendium.de/sites/kom/bilder/02121631.gif)

Im analogen Telefonnetz ist ein Modem eine technische Einrichtung, um digitale Signale von der Computerschnittstelle in analoge Signale per Modulation für das Telefonnetz umzuwandeln und umgekehrt die analogen Signale vom Telefonnetz in digitale Signale per Demodulation zur Computerschnittstelle zurückwandelt. Aus dieser Funktion heraus hat sich der Begriff Modem entwickelt (MOdulator/DEModulator).

- [DFÜ - Datenfernübertragung](https://www.elektronik-kompendium.de/sites/kom/1303281.htm)
- [Internet-Anschluss](https://www.elektronik-kompendium.de/sites/net/1403201.htm)

### Aufgabe eines Modems

- Umsetzen der binären Daten-, Steuer- und Meldesignale über die Schnittstelle
- Signalumsetzung für den Verbindungsaufbau und -abbau
- Erzeugen der Datenpakete
- Taktrückgewinnung in synchronen Netzen
- Anpassung der binären Datensignale an den Übertragungsweg

### Modulation

Die Modulation ist deshalb wichtig, um das zu übertragende Signal in eine Form zu bekommen, die sich für die Übertragung über weite Strecken und die Bedingungen durch das Übertragungsmedium eignet. Reine digitale Signale eignen sich nicht für die Übertragung. Schon bei einer kurzen Strecke wird ein digitales Signal stark verfälscht.  
Speziell bei Modems für die Übertragung im Telefonnetz muss das zu übertragende Signal so aufbereitet werden, dass es sich für die Übertragung im Frequenzbereich zwischen 300 und 3.400 Hz eignet.

### Modem-Standards im Telefonnetz

Die technische Mindestleistung von Modems wurde von der ITU in den V-Vorschriften für das analoge Telefonnetz und in den X-Vorschriften für das digitale Telefonnetz zusammengefasst.

|ITU-T-Standard|Betriebsart|Download|Upload|
|:--|---|---|---|
|V.21|vollduplex|je 300 Bit/s|   |
|V.22|vollduplex|je 1.200 Bit/s|   |
|V.22bis|vollduplex|je 2.400 Bit/s|   |
|V.23|halbduplex|1.200 Bit/s|   |
|vollduplex|1.200 Bit/s|75 Bit/s|
|vollduplex|75 Bit/s|1.200 Bit/s|
|V.32|vollduplex|je 9.600 Bit/s|   |
|V.32bis|vollduplex|je 14.400 Bit/s|   |
|V.34|vollduplex|je 28.800 Bit/s|   |
|V.34bis|vollduplex|je 33.600 Bit/s|   |
|V.90 / V.92|vollduplex|56.000 Bit/s|33.600 Bit/s|

Weil die Datenübertragung über das Telefonnetz ein Auslaufmodell ist und man ein gewisse technische Grenze erreicht hat, ist die Weiterentwicklung der Modem-Standards für das analoge Telefonnetz eingestellt worden.

- [CCITT/ITU-Empfehlungen](https://www.elektronik-kompendium.de/sites/kom/0411251.htm)
- [V.90 und V.92](https://www.elektronik-kompendium.de/sites/kom/0304281.htm)

### Modem-Steuerung

Ein Modem wird über die so genannten AT-Befehle gesteuert. Bei einem Wählprogramm wird das automatisch erledigt. Bei einem Terminal-Programm an einem Computer muss man die AT-Befehle manuell über die Tastatur eingeben.  
Die Anwahl wird über das Telefonnetz zu einem anderen Modem-Teilnehmer vorgenommen. Nimmt dieser den Anruf an, so versuchen sich die beiden Modems über wichtige Übertragungsparameter abzustimmen:

- Übertragungsgeschwindigkeit
- Fehlerkorrektur
- Datenkompression
- Protokolle

Wenn alle Parameter ausgetauscht sind und ein gemeinsamer Nenner der verwendeten Sprache (Modulation) abgestimmt ist, beginnt die eigentliche Datenübertragung.

### Fax-Modem

Fax-Modems sind in der Lage mit spezieller Software Dokumente zu verschicken und zu empfangen.  
Der Fax-Versand wird in einem Computer über einen Druckertreiber realisiert, der statt einem Drucker ein angeschlossenes Modem für den Ausdruck benutzt. Dabei wird das Dokument nicht gedruckt, sondern verschickt.  
Handschriftliche Dokumente oder Original-Vorlagen müssen allerdings vor dem Versand erst eingescannt werden.

### Softmodem

Softmodems sind Steckkarten (PCI / AMR / CNR / ACR) oder USB-Adapter (extern), deren Steuerung vom Prozessor übernommen werden muss. Diese Geräte sind meist sehr billig, weil die Herstellungskosten durch den geringeren Bauteilbedarf geringer ist.  
Ähnlich arbeiten auch ISDN-Karten-Treiber, die V.xx-Modems simulieren.  
Der Nachteil daraus ergibt sich aus der zusätzlich notwendigen Prozessorbelastung. Bei Softmodems geht man allerdings davon aus, dass der eingesetzte Computer über genügend Leistungsreserven verfügt.

### Anschlussmöglichkeiten

**Externe Modems haben in der Regel folgende Anschlussmöglichkeiten, die je nach Hersteller und Modell abweichen:**

- [Serielle Schnittstelle](https://www.elektronik-kompendium.de/sites/com/0310301.htm) oder [USB](https://www.elektronik-kompendium.de/sites/com/0312021.htm) (externe Geräte)
- Stromanschluss
- Anschluss ans Telefonnetz (analog)
- evt. Audio-Anschlüsse für Mikrofon- und Lautsprecher (z. B. Headset)
- evt. Anschluss für Telefon (durchgeschleift)

### Modem-Problem

Es gibt Modems, die nach dem Einstecken in die TAE-Dose das nachgeschaltete Telefon lahm legen. Das Problem ist, dass diese Modems die Leitung nicht durchschalten.

**Nach dem Einstecken des Modems in die TAE-Dose funktioniert das Telefon nicht mehr!**  
Entweder wurde nicht das Original-Anschlusskabel des Modems verwendet oder es handelt sich um ein Modem, welches die ab-Ader nicht weiterschaltet. In der Regel sollte das jedes Modem machen.

Wer schon ein Modem hat, das Probleme bereitet, dem ist eine AWADo (alt) oder eine AMS (neu) oder ein Umschalter T2 zu empfehlen. Diese Geräte, in Form von Anschlussdosen, erlauben den Betrieb von zwei oder mehr Endgeräten an einem Anschluss, ohne das sie sich gegenseitig stören.

- [TAE - Telekommunikationsanschlusseinheit](https://www.elektronik-kompendium.de/sites/kom/0302271.htm)
