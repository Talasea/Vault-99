
**Was ist BGP? (Border Gateway Protocol)**

BGP ist ein **dynamisches Routing-Protokoll**, das primär für den **Datenaustausch zwischen autonomen Systemen (AS)** im Internet verwendet wird. Ein autonomes System ist ein Netzwerk oder eine Gruppe von Netzwerken, die unter einer einzigen technischen Administration betrieben werden und eine einheitliche Routing-Policy nach außen vertreten. Man kann sich AS als große Netzwerke von Internet Service Providern (ISPs), großen Unternehmen oder Universitäten vorstellen.

Im Gegensatz zu **Interior Gateway Protocols (IGPs)** wie OSPF oder RIP, die innerhalb eines einzelnen AS routen, ist BGP ein **Exterior Gateway Protocol (EGP)**, das für das Routing _zwischen_ verschiedenen AS konzipiert wurde.

**Die Hauptaufgaben von BGP:**

- **Austausch von Erreichbarkeitsinformationen:** BGP-Router (auch als BGP-Peers oder BGP-Speaker bezeichnet) tauschen Informationen über die erreichbaren Netzwerke (Präfixe) und die Pfade zu diesen Netzwerken aus.
- **Auswahl des besten Pfades:** Basierend auf einer komplexen Menge von Attributen und Richtlinien wählt jeder BGP-Router den besten Pfad zu einem bestimmten Zielnetzwerk aus.
- **Aufrechterhaltung der Routing-Informationen:** BGP überwacht die Erreichbarkeit von Pfaden und aktualisiert die Routing-Tabellen, wenn sich die Netzwerkstruktur ändert.

**Kernkonzepte im BGP-Routing:**

- **Autonomes System (AS):** Eine Sammlung von Routern unter einer gemeinsamen administrativen Kontrolle und mit einer kohärenten Routing-Policy. Jedes AS hat eine eindeutige AS-Nummer (ASN).
- **BGP-Peering:** Die Etablierung einer TCP-Verbindung (Port 179) zwischen zwei BGP-Routern in verschiedenen (oder manchmal auch im selben) AS, um Routing-Informationen auszutauschen. Es gibt zwei Haupttypen von Peering:
    - **EBGP (External BGP):** Peering zwischen Routern in verschiedenen AS.
    - **IBGP (Internal BGP):** Peering zwischen Routern innerhalb desselben AS.
- **Präfix (Prefix):** Eine IP-Adressbereichsangabe (z.B. 192.168.1.0/24), die ein erreichbares Netzwerk repräsentiert.
- **BGP-Attribute:** Informationen, die zusammen mit den Präfixen ausgetauscht werden und zur Pfadauswahl dienen. Einige wichtige Attribute sind:
    - **AS-Pfad (AS-Path):** Eine Liste der AS-Nummern, die ein Präfix auf seinem Weg zum aktuellen Router durchlaufen hat. Dies dient zur Vermeidung von Routing-Loops und zur Pfadauswahl (kürzere AS-Pfade werden oft bevorzugt).
    - **Next Hop:** Die IP-Adresse des Routers, der als nächster Hop auf dem Weg zum Zielnetzwerk dient.
    - **MED (Multi-Exit Discriminator):** Ein optionales Attribut, das innerhalb eines AS verwendet wird, um den bevorzugten Eintrittspunkt in dieses AS anzugeben, wenn es mehrere Verbindungen zu anderen AS gibt.
    - **Local Preference:** Ein Attribut, das nur innerhalb eines AS ausgetauscht wird und die Präferenz für einen bestimmten ausgehenden Pfad angibt. Höhere Werte werden bevorzugt.
    - **Community:** Ein optionales Attribut, das verwendet werden kann, um Routing-Richtlinien über AS-Grenzen hinweg zu kennzeichnen und anzuwenden.
    - **Origin:** Gibt an, wie ein Präfix in das BGP-System gelangt ist (IGP, EGP oder unvollständig).
- **BGP-Nachrichten:** BGP-Router kommunizieren über verschiedene Arten von Nachrichten:
    - **Open:** Wird verwendet, um eine BGP-Peering-Sitzung zu initiieren.
    - **Update:** Enthält Informationen über neue oder zurückgezogene Routen (Präfixe).
    - **Keepalive:** Wird regelmäßig gesendet, um die Lebendigkeit der BGP-Peering-Sitzung zu bestätigen.
    - **Notification:** Wird gesendet, um Fehler in der BGP-Kommunikation zu melden und die Peering-Sitzung zu beenden.
    - **Route-Refresh:** Ermöglicht einem BGP-Peer, die vollständige Routing-Tabelle von seinem Peer erneut anzufordern.
- **BGP-Tabelle (RIB - Routing Information Base):** Jeder BGP-Router verwaltet eine BGP-Tabelle, die alle gelernten Routen von seinen Peers enthält.
- **BGP-Pfadauswahlprozess:** Ein komplexer Algorithmus, der in mehreren Schritten den besten Pfad zu einem Zielnetzwerk aus der BGP-Tabelle auswählt und in die IP-Routing-Tabelle des Routers einfügt. Dieser Prozess berücksichtigt die verschiedenen BGP-Attribute und lokale Konfigurationen.

**Wie funktioniert BGP-Routing?**

1. **Peering-Aufbau:** Zwei BGP-Router in benachbarten AS konfigurieren ihre Peering-Parameter (z.B. Peer-IP-Adresse, ASN) und bauen eine TCP-Verbindung auf. Sie tauschen `Open`-Nachrichten aus, um die Peering-Sitzung zu etablieren.
2. **Austausch von Routing-Informationen:** Sobald die Peering-Sitzung etabliert ist, beginnen die BGP-Peers, `Update`-Nachrichten auszutauschen. Diese Nachrichten enthalten Informationen über die erreichbaren Präfixe und die zugehörigen BGP-Attribute, insbesondere den AS-Pfad.
3. **Pfadauswahl:** Jeder BGP-Router empfängt die Routing-Informationen von seinen Peers und speichert sie in seiner BGP-Tabelle. Anschließend führt er den BGP-Pfadauswahlprozess durch, um den besten Pfad zu jedem Zielnetzwerk zu ermitteln. Dieser Prozess berücksichtigt die konfigurierten Routing-Richtlinien und die Werte der BGP-Attribute.
4. **Weiterleitung von Datenverkehr:** Der ausgewählte beste Pfad für jedes Präfix wird in die IP-Routing-Tabelle des Routers eingetragen. Wenn der Router ein Datenpaket empfängt, das für ein bestimmtes Zielnetzwerk bestimmt ist, konsultiert er seine Routing-Tabelle und leitet das Paket über den Next Hop des besten BGP-Pfades weiter.
5. **Aufrechterhaltung und Aktualisierung:** BGP-Router senden regelmäßig `Keepalive`-Nachrichten, um die Lebendigkeit ihrer Peering-Sitzungen zu überprüfen. Wenn sich die Netzwerktopologie ändert (z.B. eine Verbindung fällt aus oder eine neue Route wird bekannt), senden die betroffenen BGP-Router `Update`-Nachrichten, um ihre Routing-Informationen zu aktualisieren.

**Warum ist BGP wichtig?**

- **Skalierbarkeit des Internets:** BGP ermöglicht das Routing zwischen der riesigen Anzahl von autonomen Systemen, aus denen das Internet besteht.
- **Richtlinienbasiertes Routing:** BGP erlaubt Administratoren, detaillierte Routing-Richtlinien zu definieren und zu implementieren, um den Datenverkehr über bestimmte Pfade zu lenken oder bestimmte Pfade zu vermeiden. Dies ist entscheidend für Traffic Engineering, Kostenkontrolle und Sicherheitsaspekte.
- **Stabilität und Redundanz:** Durch den Austausch von Pfadinformationen und die Möglichkeit, alternative Pfade zu lernen, trägt BGP zur Stabilität und Redundanz des Internets bei. Wenn ein Pfad ausfällt, können Router in der Regel automatisch auf einen alternativen Pfad umschalten.

**Referenzierung:**

BGP ist in mehreren RFCs (Request for Comments) der Internet Engineering Task Force (IETF) standardisiert. Die wichtigsten sind:

- **RFC 4271:** BGP-4 (die aktuelle Hauptversion von BGP)
- **RFC 4272:** BGP Security Vulnerabilities Analysis
- **RFC 4760:** Multiprotocol Extensions for BGP-4 (ermöglicht den Transport von Routing-Informationen für verschiedene Protokollfamilien wie IPv6)
- **RFC 7606:** Revised Route Refresh Mechanism for BGP

Darüber hinaus gibt es zahlreiche Bücher, Artikel und Online-Ressourcen, die detaillierte Informationen über BGP-Routing bieten. Die Konfiguration und das Troubleshooting von BGP sind auch wichtige Bestandteile von Netzwerkzertifizierungen wie Cisco CCIE oder Juniper JNCIE.

**Zusammenfassend lässt sich sagen, dass BGP das Fundament des globalen Internet-Routings bildet. Es ist ein komplexes, aber äußerst leistungsfähiges Protokoll, das den Austausch von Routing-Informationen zwischen autonomen Systemen ermöglicht und somit die Skalierbarkeit, Stabilität und Flexibilität des Internets gewährleistet.**

