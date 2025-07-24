



CIDR-Notation, auch bekannt als Classless Inter-Domain Routing, ist eine Methode zur flexiblen Zuweisung von Internetadressen.24 Sie ermöglicht es, den IPv4-Adressraum effizienter auszunutzen, indem sie die feste Zuordnung einer IP-Adresse zu einer Netzklasse aufhebt.12 Stattdessen teilt eine Subnetzmaske die IP-Adresse in Netzwerk- und Hostbereich auf.1 Das CIDR-Suffix gibt an, wie viele Bits der IP-Adresse zum Netzteil gehören.2 Zum Beispiel entspricht die Subnetzmaske 255.255.255.0 der CIDR-Notation /24, da die ersten 24 Bits der IP-Adresse zum Netzteil gehören.2

- **/24**: Klassische Klasse-C-Netzmaske, ermöglicht 254 Hosts
    
- **/16**: Klassische Klasse-B-Netzmaske, ermöglicht 65.534 Hosts
    
- **/8**: Klassische Klasse-A-Netzmaske, ermöglicht über 16 Millionen Hosts




CIDR-Notation, auch bekannt als Classless Inter-Domain Routing, ist eine Methode zur effizienteren Nutzung des IPv4-Adressraums. Sie wurde 1993 eingeführt, um das Konzept der Netzklassen abzulösen und den Platzmangel im Internet zu bewältigen. Hier sind einige wichtige Punkte zur CIDR-Notation:

- **Verkürzte Schreibweise**: Die CIDR-Notation vereinfacht die Schreibweise von IP-Adressen und Subnetzmasken. Stattdessen von einer IP-Adresse und einer Subnetzmaske wird eine IP-Adresse mit einem CIDR-Suffix verwendet. Zum Beispiel wird die Schreibweise mit Subnetzmaske `10.0.0.1 / 255.0.0.0` in der CIDR-Notation zu `10.0.0.1/8`.
- **Flexibilität**: CIDR ermöglicht eine flexiblere Teilung des IPv4-Adressraums. Es ist nicht mehr notwendig, die Adressen in festen Klassen (A, B, C) zu unterteilen. Stattdessen kann man beliebige Subnetze definieren, die genau den Bedürfnissen eines Netzwerks entsprechen.
- **Reduzierung von Routingtabellen**: Durch die Verwendung von CIDR können Internetroutern Routingtabellen verkleinern, da mehrere Adressen zu einer Route zusammengefasst werden können. Dies reduziert die Komplexität und die Größe der Routingtabellen.
- **Verwendung von VLSM**: CIDR nutzt die Variable Length Subnet Mask (VLSM), die es ermöglicht, Subnetze mit variabler Länge zu erstellen. Dies bedeutet, dass man nicht nur festgelegte Netzgrößen wie Klasse A, B oder C verwenden muss, sondern auch kleinere oder größere Subnetze definieren kann.
- **Beispiel für CIDR-Suffixe**: Die CIDR-Notation verwendet ein Suffix nach dem Schrägstrich, um die Anzahl der Bits anzugeben, die zum Netzteil gehören. Ein Suffix von `/8` bedeutet, dass die ersten 8 Bits der IP-Adresse zum Netzteil gehören, während die restlichen Bits für den Host-Teil reserviert sind.
- **CIDR-Tabelle**: Es gibt eine Tabelle, die die Anzahl der möglichen IP-Adressen für verschiedene CIDR-Suffixe aufzeigt. Zum Beispiel ermöglicht ein Suffix von `/24` 254 mögliche IP-Adressen für Hosts, wobei zwei Adressen für die Netzadresse und die Broadcast-Adresse reserviert sind.
- **Supernetting**: CIDR ermöglicht auch das Supernetting, bei dem mehrere Netze zu einer Route zusammengefasst werden können. Dies ist nützlich, wenn ein Unternehmen mehrere Standorte hat und alle Rechner im gleichen Netz behandelt werden sollen.
- **Vereinfachung der Adressierung**: Die CIDR-Notation vereinfacht die Adressierung von IP-Adressen und Subnetzmasken, indem sie die Information über die Netzgrösse direkt in die IP-Adresse integriert.


https://www.ionos.de/digitalguide/server/knowhow/classless-inter-domain-routing/


https://aws.amazon.com/de/what-is/cidr/


### Broadcast Adresse 

Eine Broadcast-Adresse ist eine spezielle IP-Adresse, die verwendet wird, um Datenpakete an alle Teilnehmer eines lokalen Netzwerks zu senden, ohne dass die Empfänger explizit angegeben werden müssen. Sie dient dazu, Informationen und Dienste an alle Geräte und Komponenten innerhalb eines Netzwerks zu übertragen. Hier sind einige wichtige Punkte zur Broadcast-Adresse:

- **Funktion**: Eine Broadcast-Adresse ermöglicht es, Datenpakete an alle Netzwerk-Teilnehmer zu senden, ohne dass deren individuelle IP-Adressen bekannt sein müssen. Sie wird häufig in Netzwerkadministrationsprozessen wie DHCP, ARP oder Wake-On-LAN-Prozessen genutzt.
    
- **Zusammensetzung**: Die Broadcast-Adresse setzt sich aus der gültigen IP-Adresse und der Netzmaske zusammen. Wenn alle Host-Bits auf den Wert „1“ gesetzt sind, handelt es sich um die Broadcast-Adresse. Zum Beispiel, bei der IP-Adresse 192.168.0.7/24 ist die Broadcast-Adresse 192.168.0.255.
    
- **Arten von Broadcasts**:
    
    - **Limited Broadcast**: Zieladresse ist 255.255.255.255. Dieser Broadcast zielt auf alle existierenden Adressen ab, aber in der Realität erreicht er nur das eigene lokale Netz und wird nicht von Routern weitergeleitet.
    - **Directed Broadcast**: Ziel sind alle Empfänger eines bestimmten Netzes. Die Adresse wird durch die Kombination aus Zielnetz und dem Setzen aller Hostbits auf 1 angegeben. Wenn Quell- und Zielnetz unterschiedlich sind, wird das Datenpaket vom Router weitergeleitet.
- **Verwendung**: Netzwerkadministratoren nutzen Broadcast-Adressen, um die erfolgreiche Übertragung von Datenpaketen zu überprüfen. Netzwerkfähige Computer- und Spiele verwenden sie, um Listen mit offenen Spielen innerhalb des Netzwerkes zu finden.
    
- **Ermittlung**: Die Broadcast-Adresse kann durch die IP-Adresse und die Subnetzmaske des Computers berechnet werden. Sie kann auch über die Eingabeaufforderung (cmd) oder mit Online-Rechnern wie denen von Netways oder Heise Online ermittelt werden.
    

Die Broadcast-Adresse ist ein wesentlicher Bestandteil des Netzwerkkommunikationsprozesses und hilft dabei, Datenpakete effizient an alle Teilnehmer eines Netzwerks zu senden.

