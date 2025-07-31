**Prozess (DORA-Prozess):** Der Zuweisungsprozess erfolgt in vier Schritten, die oft mit dem Akronym **DORA** abgekürzt werden:

1. **Discover (Entdecken):** Der Client, der noch keine IP-Adresse hat, sendet eine **DHCPDISCOVER**-Nachricht als Broadcast in das lokale Netzwerk. Diese Nachricht fragt im Wesentlichen: "Gibt es hier einen DHCP-Server, der mir eine IP-Adresse geben kann?"
    
2. **Offer (Anbieten):** Alle DHCP-Server, die die Discover-Nachricht empfangen, antworten mit einer **DHCPOFFER**-Nachricht. Dieses Angebot enthält eine verfügbare IP-Adresse, die Subnetzmaske, die Lease-Dauer und die IP-Adresse des Gateways (Routers) und der DNS-Server.
    
3. **Request (Anfordern):** Der Client wählt eines der Angebote aus (normalerweise das erste, das er empfängt) und sendet eine **DHCPREQUEST**-Nachricht, ebenfalls als Broadcast. Diese Nachricht teilt allen DHCP-Servern mit: "Ich akzeptiere das Angebot von Server X und möchte die IP-Adresse Y anfordern."
    
4. **Acknowledge (Bestätigen):** Der ausgewählte DHCP-Server bestätigt die Zuweisung mit einer **DHCPACK**-Nachricht. Damit wird der Lease-Vorgang abgeschlossen, die IP-Adresse wird im Server als "vergeben" markiert und der Client konfiguriert seine Netzwerkschnittstelle mit den erhaltenen Informationen.



------

### 1. Kerndefinition

Das **Dynamic Host Configuration Protocol (DHCP)** ist ein fundamentales Netzwerkmanagement-Protokoll, das die automatische Zuweisung und Verwaltung von IP-Adressen und anderen wichtigen Netzwerkkonfigurationsparametern an Geräte (Clients) in einem IP-Netzwerk ermöglicht. Anstatt jedem Gerät manuell eine statische IP-Adresse zuzuweisen, kann ein DHCP-Server diesen Prozess zentralisieren und automatisieren. Dies vereinfacht die Netzwerkadministration erheblich und verhindert Adresskonflikte.

### 2. Detaillierte Erläuterung / Funktionsweise

**Schlüsselkomponenten:**

- **DHCP-Server:** Ein Server (oft ein Router, ein Windows/Linux-Server oder ein anderes Netzwerkgerät), der über einen Pool von verfügbaren IP-Adressen (einen "Scope") verfügt und diese an anfragende Clients vergibt.
    
- **DHCP-Client:** Jedes Gerät, das eine Netzwerkkonfiguration anfordert (z. B. ein PC, Smartphone, Drucker). Der DHCP-Client-Dienst ist in praktisch allen modernen Betriebssystemen integriert.
    
- **DHCP-Lease:** Eine IP-Adresse wird einem Client nicht permanent, sondern nur für eine bestimmte Zeitspanne ("Lease Time") "vermietet". Vor Ablauf dieser Zeit muss der Client eine Verlängerung beantragen, andernfalls wird die Adresse wieder für andere Clients freigegeben.
    

**Prozess (DORA-Prozess):** Der Zuweisungsprozess erfolgt in vier Schritten, die oft mit dem Akronym **DORA** abgekürzt werden:

1. **Discover (Entdecken):** Der Client, der noch keine IP-Adresse hat, sendet eine **DHCPDISCOVER**-Nachricht als Broadcast in das lokale Netzwerk. Diese Nachricht fragt im Wesentlichen: "Gibt es hier einen DHCP-Server, der mir eine IP-Adresse geben kann?"
    
2. **Offer (Anbieten):** Alle DHCP-Server, die die Discover-Nachricht empfangen, antworten mit einer **DHCPOFFER**-Nachricht. Dieses Angebot enthält eine verfügbare IP-Adresse, die Subnetzmaske, die Lease-Dauer und die IP-Adresse des Gateways (Routers) und der DNS-Server.
    
3. **Request (Anfordern):** Der Client wählt eines der Angebote aus (normalerweise das erste, das er empfängt) und sendet eine **DHCPREQUEST**-Nachricht, ebenfalls als Broadcast. Diese Nachricht teilt allen DHCP-Servern mit: "Ich akzeptiere das Angebot von Server X und möchte die IP-Adresse Y anfordern."
    
4. **Acknowledge (Bestätigen):** Der ausgewählte DHCP-Server bestätigt die Zuweisung mit einer **DHCPACK**-Nachricht. Damit wird der Lease-Vorgang abgeschlossen, die IP-Adresse wird im Server als "vergeben" markiert und der Client konfiguriert seine Netzwerkschnittstelle mit den erhaltenen Informationen.
    

### 3. Einordnung in den Gesamtkontext

DHCP ist ein Client-Server-Protokoll, das auf **UDP** (User Datagram Protocol) aufbaut und die Ports 67 (Server) und 68 (Client) verwendet. Es ist eine Weiterentwicklung des älteren **BOOTP**-Protokolls. In einem typischen LAN ist die DHCP-Server-Funktionalität oft direkt im Router integriert. In größeren Unternehmensnetzwerken werden dedizierte, oft redundante DHCP-Server eingesetzt. Da DHCP-Nachrichten standardmäßig Broadcasts sind und diese nicht über Router hinausgehen, werden in segmentierten Netzwerken **DHCP-Relay-Agents** (oft eine Funktion auf Routern) benötigt, um DHCP-Anfragen von Clients in einem Subnetz an einen zentralen DHCP-Server in einem anderen Subnetz weiterzuleiten.

### 4. Sicherheitsaspekte

DHCP ist von Natur aus ein vertrauensbasiertes Protokoll und daher anfällig für verschiedene Angriffe:

- **Rogue DHCP Server (Böswilliger DHCP-Server):** Ein Angreifer kann einen eigenen DHCP-Server im Netzwerk aufsetzen. Antwortet dieser schneller als der legitime Server, kann er Clients falsche Konfigurationsdaten unterschieben, z. B. ein Gateway und einen DNS-Server, die unter der Kontrolle des Angreifers stehen. Dies ermöglicht Man-in-the-Middle-Angriffe, bei denen der gesamte Netzwerkverkehr des Opfers mitgelesen oder manipuliert werden kann.
    
- **DHCP Starvation Attack (Aushungerungsangriff):** Ein Angreifer sendet massenhaft DHCPREQUEST-Nachrichten mit gefälschten MAC-Adressen. Dadurch wird der gesamte Adresspool des legitimen DHCP-Servers aufgebraucht, sodass keine Adressen mehr für legitime Clients zur Verfügung stehen (Denial-of-Service).
    
- **Gegenmaßnahmen:** Die wichtigste Gegenmaßnahme ist **DHCP Snooping**, eine Sicherheitsfunktion auf modernen Switches. Der Switch überwacht DHCP-Nachrichten, lässt DHCPOFFER-Pakete nur von vertrauenswürdigen (explizit konfigurierten) Ports zu und begrenzt die Anzahl der Anfragen pro Port, um die genannten Angriffe zu verhindern.
    

### 5. Praxisbeispiel / Analogie

**Analogie: Hotel-Rezeption** Stellen Sie sich ein großes Hotel vor, in dem die Zimmernummern die IP-Adressen sind.

1. **Discover:** Ein neuer Gast (Client) kommt in die Lobby (Netzwerk) und ruft laut: "Hallo, ich brauche ein Zimmer!"
    
2. **Offer:** Der Rezeptionist (DHCP-Server) antwortet: "Ich kann Ihnen Zimmer 305 (IP-Adresse) für eine Nacht (Lease Time) anbieten. Der Weg zum Aufzug (Gateway) ist dort drüben."
    
3. **Request:** Der Gast ruft zurück: "Großartig, ich nehme Zimmer 305!"
    
4. **Acknowledge:** Der Rezeptionist trägt den Gast in sein Buch ein, gibt ihm den Schlüssel (bestätigt den Lease) und sagt: "Willkommen, das Zimmer gehört Ihnen für eine Nacht."
    

Am nächsten Tag muss der Gast seinen Aufenthalt verlängern (Lease Renewal), sonst wird das Zimmer wieder als frei markiert.

### 6. Fazit / Bedeutung für IT-Profis

Für jeden Netzwerk- und Systemadministrator ist DHCP ein absolut grundlegendes und unverzichtbares Protokoll. Ein tiefes Verständnis seiner Funktionsweise, des DORA-Prozesses und der damit verbundenen Sicherheitsrisiken ist entscheidend für den Aufbau, die Verwaltung und die Absicherung von IP-Netzwerken jeder Größe. Die Fähigkeit, DHCP-Server korrekt zu konfigurieren, Fehler zu beheben (z. B. wenn Clients keine IP-Adresse erhalten) und Sicherheitsfunktionen wie DHCP Snooping zu implementieren, gehört zum Kernwissen eines jeden IT-Infrastruktur-Profis.