
# 

Border Gateway Protocol

Das Border Gateway Protocol (BGP) ist ein standardisiertes externes Gateway-Protokoll, das zum Austausch von Routing-Informationen zwischen verschiedenen autonomen Systemen (AS) im Internet verwendet wird Es ermöglicht eine effiziente und skalierbare Routingentscheidung, die sicherstellt, dass Datenpakete in komplexen Netzwerken den besten Weg zu ihren Zielen finden. BGP wird oft als Pfadvektorprotokoll bezeichnet und verwendet TCP-Port 179 für die Kommunikation zwischen BGP-Router. Es hilft dabei, den effizientesten Weg für den Datenverkehr zwischen autonomen Systemen zu wählen, ähnlich wie ein Sortierzentrum der Post, das den effizientesten Weg für den Transport von Daten bestimmt.



----




# Border Gateway Protocol (BGP): Das Rückgrat des Internets – Einblicke für IT-Profis

Der vorliegende Text liefert eine grundlegende Einführung in das Border Gateway Protocol (BGP). Für angehende IT-Experten ist es jedoch entscheidend, die immense Bedeutung und die komplexen Mechanismen dieses Protokolls zu verstehen, da es das Fundament des modernen Internets bildet.

**Definition: Das Protokoll der Protokolle für den globalen Datenaustausch**

Das Border Gateway Protocol (BGP) ist weit mehr als nur ein "standardisiertes externes Gateway-Protokoll". Es ist das **fundamentale Routing-Protokoll**, das die Kommunikation zwischen den unzähligen unabhängigen Netzwerken, den sogenannten **Autonomen Systemen (AS)**, ermöglicht, aus denen das Internet besteht. Ohne BGP würde das Internet, wie wir es kennen, nicht funktionieren.

- **Standardisiertes externes Gateway-Protokoll:** Dies bedeutet, dass BGP ein offener Standard ist (RFC 4271) und speziell für den Austausch von Routing-Informationen _zwischen_ verschiedenen administrativen Domänen (den AS) entwickelt wurde. Im Gegensatz dazu gibt es interne Gateway-Protokolle (IGPs) wie OSPF oder RIP, die innerhalb eines einzelnen AS verwendet werden.
- **Austausch von Routing-Informationen:** BGP tauscht Informationen über die **Erreichbarkeit von Netzwerken** (genauer gesagt, Präfixen oder IP-Adressbereichen) zwischen verschiedenen AS aus. Es teilt den anderen AS mit, welche Netzwerke ein bestimmtes AS erreichen kann und über welche Pfade.
- **Autonome Systeme (AS):** Ein AS ist eine Sammlung von IP-Netzwerken und Routern, die von einer einzigen administrativen Einheit oder Organisation (z. B. einem Internetdienstanbieter (ISP), einem großen Unternehmen oder einer Universität) unter einer gemeinsamen Routing-Policy betrieben werden. Jedes AS erhält eine eindeutige AS-Nummer (ASN).

**Funktionsweise im Detail: Pfadvektoren für komplexe Netzwerke**

BGP ermöglicht eine **effiziente und skalierbare Routingentscheidung** in den hochkomplexen Netzwerken des Internets.

- **Pfadvektorprotokoll:** Der Text erwähnt, dass BGP oft als Pfadvektorprotokoll bezeichnet wird. Dies ist ein wichtiger Unterschied zu anderen Routing-Protokollen. Anstatt nur die Distanz (z. B. in Hops) zu einem Ziel anzugeben (wie bei Distance-Vector-Protokollen wie RIP) oder eine vollständige topologische Karte des Netzwerks zu erstellen (wie bei Link-State-Protokollen wie OSPF), bewirbt BGP **Pfade** zu Zielnetzwerken. Diese Pfade enthalten die Liste der AS, die ein Datenpaket auf seinem Weg zum Ziel durchlaufen muss (den sogenannten **AS-Pfad**).
- **TCP-Port 179:** BGP verwendet den **TCP-Port 179** für die Kommunikation zwischen BGP-Routern (auch **BGP-Peers** genannt). Die Verwendung von TCP gewährleistet eine zuverlässige und geordnete Übertragung der Routing-Informationen.
- **Effizienter Weg für den Datenverkehr:** BGP hilft dabei, den **effizientesten Weg** für den Datenverkehr zwischen autonomen Systemen zu wählen. "Effizient" kann hier verschiedene Aspekte umfassen, wie z. B. die Anzahl der durchlaufenen AS, die Präferenzen des sendenden oder empfangenden AS (Routing-Policies) oder die Kostenvereinbarungen zwischen den AS.
- **Analogie zum Sortierzentrum der Post:** Die Analogie zum Sortierzentrum der Post ist sehr treffend. BGP-Router in verschiedenen AS fungieren wie große Postzentren, die Informationen darüber austauschen, wie man Pakete (Daten) am besten zu ihrem endgültigen Bestimmungsort (Zielnetzwerk) transportiert, wobei der Weg über verschiedene Zwischenstationen (andere AS) berücksichtigt wird.

**Schlüsselkonzepte im Detail: Das Herzstück von BGP**

- **Autonome Systeme (AS):**
    - Jedes AS hat eine eindeutige **AS-Nummer (ASN)**, die von einer regionalen Internetregistrierungsstelle (RIR) vergeben wird.
    - Es gibt verschiedene Arten von AS:
        - **Stub AS:** Ein kleines AS, das nur eine Verbindung zu einem anderen AS hat.
        - **Transit AS:** Ein AS, das Datenverkehr von einem AS zu einem anderen weiterleitet (typischerweise ISPs).
        - **Multi-homed AS:** Ein AS, das Verbindungen zu mehreren anderen AS hat, um Redundanz und bessere Leistung zu erzielen.
- **Pfadvektorprotokoll:**
    - BGP bewirbt **erreichbare Netzwerke (Präfixe)** zusammen mit dem **Pfad** (der Liste der AS-Nummern), den der Datenverkehr nehmen muss, um dieses Netzwerk zu erreichen.
    - Diese Pfadinformation ermöglicht es Routern, Routing-Loops zu erkennen und zu vermeiden, was in komplexen Netzwerken mit vielen Verbindungen entscheidend ist.
- **BGP-Peers:**
    - BGP-Router in verschiedenen AS bauen **TCP-Verbindungen** zueinander auf und werden so zu **BGP-Peers**.
    - Es gibt zwei Arten von BGP-Peering:
        - **Externes BGP (eBGP):** Peering zwischen Routern in verschiedenen AS.
        - **Internes BGP (iBGP):** Peering zwischen Routern innerhalb desselben AS. iBGP ist notwendig, um Routing-Informationen innerhalb eines AS zu verteilen, die über eBGP gelernt wurden.
- **BGP-Attribute:**
    - BGP verwendet eine Vielzahl von **Attributen**, die mit den beworbenen Routen assoziiert sind. Diese Attribute werden verwendet, um die besten Pfade für den Datenverkehr auszuwählen. Einige wichtige Attribute sind:
        - **AS-Pfad (AS_PATH):** Die Liste der AS-Nummern, die ein Präfix durchlaufen hat. Kürzere AS-Pfade werden in der Regel bevorzugt.
        - **Nächster Hop (NEXT_HOP):** Die IP-Adresse des Routers im benachbarten AS, der der nächste Hop auf dem Weg zum Zielnetzwerk ist.
        - **Lokale Präferenz (LOCAL_PREF):** Ein Attribut, das nur innerhalb eines AS verwendet wird, um die bevorzugten Ausgangspunkte für den Datenverkehr zu anderen AS zu bestimmen.
        - **Multi-Exit Discriminator (MED):** Ein Attribut, das verwendet werden kann, um Routen zu einem AS zu bevorzugen, wenn es mehrere Eintrittspunkte gibt.
        - **Community:** Ein optionales Attribut, das verwendet werden kann, um Routing-Policies zwischen verschiedenen AS zu kommunizieren.
- **Routen-Advertisements:**
    - BGP-Router tauschen **Routen-Updates** aus, um Informationen über erreichbare Netzwerke und die zugehörigen Attribute zu verbreiten.
    - Es gibt verschiedene Arten von BGP-Nachrichten, darunter:
        - **OPEN:** Wird verwendet, um eine BGP-Peering-Sitzung zu initiieren.
        - **UPDATE:** Enthält Informationen über neue oder geänderte Routen.
        - **KEEPALIVE:** Wird verwendet, um die BGP-Peering-Sitzung aktiv zu halten.
        - **NOTIFICATION:** Wird verwendet, um Fehler oder das Beenden einer BGP-Sitzung zu melden.

**Der BGP Path Selection Process: Die Kunst der Routenwahl**

BGP verwendet einen komplexen **Pfadauswahlprozess**, um die beste Route zu einem Zielnetzwerk zu bestimmen, wenn mehrere Routen verfügbar sind. Dieser Prozess umfasst mehrere Schritte, bei denen verschiedene BGP-Attribute berücksichtigt werden. Vereinfacht gesagt, werden Routen anhand einer Reihe von Regeln verglichen, um die präferierteste Route zu ermitteln.

**Sicherheitsaspekte von BGP: Eine Achillesferse des Internets?**

Obwohl BGP für das Funktionieren des Internets unerlässlich ist, weist es auch einige **Sicherheitslücken** auf:

- **BGP-Hijacking:** Ein böswilliges AS kann fälschlicherweise Routen zu IP-Adressbereichen anderer AS ankündigen. Dies kann dazu führen, dass Datenverkehr über den Angreifer geleitet wird, der ihn dann abfangen, manipulieren oder blockieren kann.
- **Route Leaks:** Fehlerhafte Konfigurationen können dazu führen, dass Routen, die nur für den internen Gebrauch innerhalb eines AS bestimmt sind, versehentlich an andere AS weitergegeben werden, was zu Routing-Problemen und Instabilität führen kann.
- **Man-in-the-Middle-Angriffe:** Da BGP-Peering-Sitzungen über TCP erfolgen, könnten Angreifer versuchen, diese Verbindungen abzufangen oder zu manipulieren.
- **Mangelnde Authentifizierung:** Ursprünglich fehlten in BGP starke Mechanismen zur Authentifizierung der Herkunft von Routen.

Um diese Sicherheitsrisiken zu mindern, wurden verschiedene **Sicherheitsmechanismen und Best Practices** entwickelt, darunter:

- **Route Origin Validation (ROV):** Eine Technik, die es ermöglicht, die Gültigkeit der Herkunft einer Route zu überprüfen, indem sie mit öffentlich verfügbaren Informationen (z. B. in der Resource Public Key Infrastructure - RPKI) abgeglichen wird.
- **BGPsec (BGP Security):** Eine Erweiterung des BGP-Protokolls, die kryptografische Signaturen verwendet, um die Authentizität und Integrität von BGP-Nachrichten zu gewährleisten.
- **Prefix Filtering:** Konfiguration von Filtern auf BGP-Routern, um nur erwartete und legitime Routen zu akzeptieren.
- **AS-Pfad-Filterung:** Überprüfung des AS-Pfads, um verdächtige oder unerwartete AS-Sequenzen zu erkennen.
- **Rate Limiting:** Begrenzung der Häufigkeit von BGP-Updates, um die Auswirkungen von Routing-Instabilität zu reduzieren.
- **Manuelle Überprüfung und Konfiguration:** Sorgfältige Konfiguration und Überwachung von BGP-Peering-Sitzungen.

**Analogie zur realen Welt (erweitert):**

Stellen Sie sich das Internet als ein riesiges Netzwerk von Straßen vor, und die AS sind einzelne Städte mit ihren eigenen internen Straßennetzen. BGP ist wie ein globales System von Wegweisern und Verkehrsleitzentralen, die den effizientesten Weg von einer Stadt zur anderen anzeigen. Jede Stadt (AS) tauscht Informationen mit ihren Nachbarstädten (anderen AS) darüber aus, welche anderen Städte sie erreichen kann und über welche Route (die Liste der durchlaufenen Städte). Die Verkehrsleitzentralen (BGP-Router) verwenden diese Informationen, um die besten Routen für den "Verkehr" (Datenpakete) zu bestimmen.

**Bedeutung für angehende IT-Experten:**

Das Verständnis von BGP ist für angehende IT-Experten, die in den Bereichen Netzwerktechnik, Internet Service Providing oder Cloud Computing arbeiten möchten, von entscheidender Bedeutung.

- **Grundlegendes Verständnis des Internets:** BGP ist ein Kernprotokoll, dessen Kenntnis unerlässlich ist, um zu verstehen, wie das Internet als Ganzes funktioniert.
- **Karrierechancen:** Expertise im Bereich BGP ist bei ISPs, großen Unternehmen mit eigenen Netzwerken und Cloud-Anbietern sehr gefragt.
- **Fehlerbehebung:** Bei Problemen mit der Erreichbarkeit von Websites oder Diensten ist oft das Routing zwischen AS involviert, und BGP-Kenntnisse sind für die Diagnose unerlässlich.
- **Netzwerkdesign:** Beim Entwurf großer Netzwerke, die mit dem Internet verbunden sind, müssen BGP-Prinzipien berücksichtigt werden.
- **Sicherheit:** Das Verständnis der Sicherheitsrisiken von BGP und der verfügbaren Gegenmaßnahmen ist entscheidend für den Schutz von Netzwerken vor Angriffen.

Indem Sie sich eingehend mit BGP beschäftigen, erwerben Sie ein fundamentales Wissen, das Ihnen in Ihrer zukünftigen IT-Karriere viele Türen öffnen wird. Es ist ein komplexes, aber faszinierendes Protokoll, dessen Beherrschung Sie zu einem wertvollen Experten im Bereich der Netzwerktechnik macht.