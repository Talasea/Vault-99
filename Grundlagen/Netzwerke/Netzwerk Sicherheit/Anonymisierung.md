
Unter Anonymisierung versteht man das Verschleiern des Start- und Zielpunktes einer Verbindung, die zur Kommunikation oder dem Datenaustausch besteht. Eine grundsätzliche Charaktereigenschaft der Anonymisierung ist das Entfernen von Merkmalen, die einen Rückschluss auf den Nutzer zulässt.

Die Erfordernis der Anonymisierung ist deshalb gegeben, weil es unter Umständen nicht ausreicht, die Kommunikation zu verschlüsseln, um sich im Internet wirksam zu schützen. Die Verbindungsdaten, zum Beispiel IP-Adressen, liegen weiterhin offen. Auch wenn Angreifer und Überwacher den Inhalt der Kommunikation nicht direkt sehen können, können sie immer noch erkennen, um welche Art der Kommunikation es sich handelt und mit wem die Kommunikation besteht oder woher die Informationen abgerufen wurden. Für einen wirksamen Schutz von Daten und der Kommunikation kann es deshalb notwendig sein, den Start- und Zielpunkt der Kommunikation zu verschleiern. Zu diesem Zweck greift man auf Anonymisierungsdienste oder -netzwerke zurück.

### IP-Adresse als Identifikationsmerkmal

Bei der Identifikation von Internet-Nutzern spielt die IP-Adresse eine zentrale Rolle. In der Internet-Kommunikation findet der Datenaustausch auf Basis von Datenpaketen statt, die zwischen Clients und Servern ausgetauscht werden. Dazu werden die Datenpakete mit den IP-Adressen von Sender und Empfänger versehen, damit auf beiden Seiten die empfangenen Datenpakete dem jeweiligen Kommunikationspartner zugeordnet werden kann. Bei der Übertragung der Datenpakete sind die IP-Adressen für die Wegfindung (Routing) zum Ziel ebenfalls erforderlich. Das bedeutet, die IP-Adresse ist für jeden, der das Datenpaket erhält, einsehbar. Da der Weg, den ein Datenpaket im Internet nimmt mehr oder weniger dem Zufall entspricht, kann man nie sicher sein, dass die Daten nicht irgendwo abgegriffen und analysiert werden. Selbst wenn die Daten an sich verschlüsselt sind, lassen sich über die IP-Adressen einige Informationen über die Kommunikationspartner ermitteln.

So führt eine sogenannte Whois-Abfrage zum genutzten Internet-Provider. Da Internet-Provider IP-Adressen lokal verwenden lässt sich unter Umständen in Kombination mit einem Geolocation-Service die Stadt, vielleicht sogar der Stadtteil, herausfinden. Werbenetzwerke benutzen bereits diese Dienste, um regionale Werbung zu schalten. Beim Online-Shopping wird auf Basis der Ortsinformationen die Kreditwürdigkeit berechnet.  
Zwar werden IP-Adressen häufig dynamisch vergeben, das heißt sie ändert sich unter Umständen mit jeder Sitzung. Allerdings gibt es noch weitere Möglichkeiten, mit denen sich eine sichere Identifikation eines Internet-Nutzers bewerkstelligen lässt.

### Verschleierungsmöglichkeiten der IP-Adresse

Weil die IP-Adresse bei der Identifikation von Internet-Nutzern eine zentrale Rolle spielt, versucht man mit Anonymisierungstechniken diese zu verschleiern. Bei der Verschleierung wird die richtige IP-Adresse wird durch eine andere ersetzt. Auf dem Weg ins Internet wird irgendwo ein oder auch mehrere Adresswechsel oder Adressübersetzungen vorgenommen. Dazu werden die Datenpakete über einen Weiterleitungsserver (Proxy), ein VPN-Gateway oder ein Anonymisierungsnetzwerk geleitet. Dort wird die Anonymisierung vorgenommen.

- Proxy
- VPN-Gateway
- Tor-Netzwerk
- JonDonym

### Proxy

![Proxy](https://www.elektronik-kompendium.de/sites/net/bilder/18091611.gif)

Die Nutzung eines Proxys ist die einfachste Möglichkeit sich anonym im Internet zu bewegen. Hierzu muss man nur die IP-Adresse des Proxys in den Netzwerk-Einstellungen des Clients oder im Browser eintragen.  
Proxy bedeutet Stellvertreter. Er nimmt Anfragen von Clients entgegen und leitet sie stellvertretend an den Ziel-Server im Internet weiter. Dabei sieht der Server nur die IP-Adresse des Proxys und nicht des Clients. Auf dem umgekehrten Weg nimmt der Proxy die Datenpakete vom Server entgegen, tauscht die IP-Adresse aus und schickt sie an den Client weiter.

Bei dieser Konstellation muss man berücksichtigen, dass die zurückgelieferten Daten vom Proxy gespeichert und ausgewertet werden können. Ein Proxy ist ein "Man in the Middle", der zwar anonymisiert, dessen Betreiber man dafür aber bedingungslos vertrauen muss. Ein angeblich anonymisierender Proxy kann auch Passwörter ausspähen und angeforderte Webseiten umschreiben, ohne das der Benutzer auf der Seite des Clients etwas davon bemerkt.

### VPN-Gateway / VPN-Tunnel

![VPN-Gateway / VPN-Tunnel](https://www.elektronik-kompendium.de/sites/net/bilder/18091612.gif)

Eine weitere Möglichkeit zur Anonymisierung sind VPN-Dienste. Hierzu wird eine VPN-Software auf dem Client installiert, der den gesamten Datenverkehr an ein VPN-Gateway im Internet weiterleitet. Das Gateway tauscht dabei die IP-Adressen aus, so dass die Ziel-Server im Internet nur die IP-Adresse des VPN-Gateways sehen. Der Datenverkehr zwischen Client und Gateway ist dabei verschlüsselt. Aber zwischen Gateway und Server wird der Datenverkehr normal übertragen.  
Im Prinzip macht das VPN-Gateway nichts anderes als ein Proxy. Nur dass die Funktionen des VPN-Gateways meist auf Hardware basieren und deshalb schneller als Proxys arbeiten. Proxys sind typischerweise, als Dienst auf einem Server installiert. Die Geschwindigkeit ist dann nicht nur von der Netzanbindung, sondern auch von der Auslastung abhängig.

Typischerweise ist es nicht die Aufgabe eines VPN-Gateways Datenverkehr aufzuzeichnen. Das bedeutet aber nicht, dass der Betreiber es nicht doch tut. Beispielsweise auch Verbindungsdaten. Denkbar wäre auch, dass sich Geheimdienste, Strafermittler oder andere Angreifer in das VPN-Gateway einklinken und die Kommunikation überwachen oder Datenverkehr abgreifen.  
Damit die Daten vor fremden Augen nicht einsehbar sind, muss der Nutzer die Daten vor dem Versand über das VPN-Gateway verschlüsseln. Vorausgesetzt, der Empfänger kann die Daten entschlüsseln.

Zusätzlich sollte man statt des Standard-DNS-Servers des eigenen Providers einen Public-DNS-Server verwenden, weil Webseiten-Betreiber über eine erzwungene DNS-Anfrage, die durch ein auf einer Subdomain liegendes, eingebettetes Bild, die tatsächliche IP-Adresse des Besuchers herausfinden können.

- [VPN - Virtual Private Network](https://www.elektronik-kompendium.de/sites/net/0512041.htm)

### Tor - The Onion Router

![Tor - The Onion Router](https://www.elektronik-kompendium.de/sites/net/bilder/18091613.gif)

Wer ernsthaft anonymisieren will, der muss mehr Aufwand betreiben. Datenverkehr über einen Proxy oder ein VPN-Gateway zu leiten reicht nicht aus. Eine Möglichkeit wäre das Onion-Routing, wie es beim Anonymisierungs-Netzwerk Tor eingesetzt wird.

Tor verschleiert die IP-Adresse eines Internet-Nutzers durch mehrere verschachtelte Verschlüsselungen über mehrere Stationen hinweg. Für den Ziel-Server sieht es so aus, als kämen die Zugriffe von einem Rechner des Tor-Netzes, das zwischen den Anwender und den Server geschaltet ist. Wegen der verschachtelten Verschlüsselung sind Internet-Verbindungen über das Tor-Netzwerk deutlich langsamer. Videos schauen, VoIP-Telefonie und Online-Gaming sind damit kaum möglich.  
Das größere Problem ist jedoch, dass auch mit Tor keine absolute Anonymität möglich ist.

- [Tor - The Onion Router](https://www.elektronik-kompendium.de/sites/net/1809171.htm)

### Mixkaskaden mit JonDonym

![Mixkaskaden mit JonDonym](https://www.elektronik-kompendium.de/sites/net/bilder/18091614.gif)

Ein weiteres Prinzip der Anonymisierung sind Mixkaskaden. Das sind Ketten von Servern, die Datenpakete ineinander verschlüsseln, damit nur der Server am Ende der Kette sie entschlüsseln kann. Die Mixe, so werden die Server bezeichnet, sammeln die Datenpakete erst einmal ein, um sie in zufälliger Reihenfolge weiter zu leiten. Pseudo-Datenpakete zwischen den Mixen sollen das Abhören zusätzlich erschweren.

Mixkaskaden bei JonDonym (kommerzieller Dienst) sind festgelegt und ändern sich während der Dauer der Verbindung nicht. Der Nutzer darf die Mixe selber wählen und kann aus 2 oder 3 Servern bestehen, wobei einer davon im Ausland stehen sollte. Auf diese Weise ist es Ermittlungsbehörden erschwert in die vollständige Mixkaskade einzudringen. Eine grenzübergreifende Zusammenarbeit der Ermittlungsbehörden und Geheimdienste wäre notwendig, um an die Verbindungsdaten zu kommen.

Auch JonDonym bietet keine absolute Anonymität. Sobald der Angreifer Zugriff auf alle Mixkaskaden hat, die der Datenverkehr eines bestimmten Nutzers nimmt, ist die Anonymität gebrochen. Mixkaskaden mit JonDonym sind allerdings um einiges sicherer als Proxys oder VPN-Gateways. Die Mix-Betreiber sind alle bekannt und mit Zertifikaten ausgestattet. Auch bei JonDonym kann nicht ausgeschlossen werden, dass sich Angreifer und Überwacher Zugang zu den Mix-Servern verschaffen. Das Risiko ist jedoch geringer als beim Tor-Netzwerk.

### Was Anonymisierung nicht kann

Anonymisierungsdienste oder -netze kümmern sich primär um die Anonymisierung der Daten. Sie verschleiern die IP-Adresse bzw. tauschen sie einmal oder mehrfach aus. Die Daten sind dabei über den ganzen oder einen Teil der Übertragungsstrecke unverschlüsselt. Da Anonymisierungsdienste und -netze prinzipbedingt als Man-in-the-Middle agieren, besteht die Gefahr, dass die übertragenen Daten aufgezeichnet und ausgewertet werden. Aus diesem Grund müssen Daten vor der Weiterleitung an Anonymisierungsdienste verschlüsselt werden. Um die Verschlüsselung der Daten muss sich der Nutzer selber kümmern.

### Auswahl eines Anonymisierungsdienstes

Eine wirksame Anonymisierung steht und fällt mit der Integrität des Betreibers und mit dem Vertrauen des Nutzers. Der Betreiber des Anonymisierungsdienstes oder -netzes darf im Prinzip keinerlei Daten aufzeichnen oder auswerten. Im Prinzip auch keine Verbindungsdaten. Vor allem nicht über den Zeitraum, über die die Verbindung andauert.  
Während in Deutschland die Vorratsdatenspeicherung ausgesetzt ist, müssen TK-Anbieter, dazu zählen auch Anonymisierungsdienste, in anderen europäischen Ländern die Verbindungsdaten ihrer Kunden mehrere Monate lang speichern. Deshalb ist die Anonymisierung nur begrenzt gegeben. Wer eine Online-Straftat begeht sollte sich klar sein, dass er trotz Anonymisierung deanonymisiert werden kann.  
Um sich auch einigermaßen wirksam vor der Deanonymisierung durch Geheimdienste zu schützen empfiehlt es sich auf die Nutzung der Dienste von Anbietern mit Sitz oder Muttergesellschaften in den USA, Kanada, Großbritannien, Australien, Neuseeland und Schweden zu verzichten. Die Geheimdienste dieser Länder greifen Datenverkehr im Internet ab oder haben Zugriff auf personenbezogener Daten großer Internet-Dienste.

### Anonymisierung kann zum Sicherheitsrisiko werden

Datenverkehr zu anonymisieren ist ein extrem untypischer Vorgang. Im Vergleich dazu ist die Verschlüsselung von Daten für viele Internet-Nutzer, auch unwissentlich, üblich. Beispielsweise beim Online-Banking oder Online-Shopping.  
Wer dagegen zusätzlich anonymisiert muss sich darüber im Klaren sein, dass er damit auffällig agiert. Angreifer und Überwacher gehen davon aus, dass anonymisierte Kommunikation etwas zu verbergen hat. Gerade das kann für einen Angreifer oder Überwacher Anlass sein, die Kommunikation aufzuzeichnen und Maßnahmen zu ergreifen, um diese zu deanonymisieren. Die Nutzung von Techniken oder Diensten zur Anonymisierung, um mehr Sicherheit für die Daten oder Kommunikation zu bekommen, kann deshalb genau den umgekehrten Effekt haben. Sie vermindert die Sicherheit der Kommunikation und der Datenübertragung.

### Identifikation über Cookies / Deanonymisierung durch Cookies

Der Vollständigkeit halber muss erwähnt werden, dass IP-Adresse nicht das einzige Identifizierungsmerkmal sind. Sofern man einen Browser benutzt, dient weniger die IP-Adresse als Identifikationsmerkmal, sondern sogenannte Cookies, anhand der Webseiten wiederkehrende Besucher erkennen können. Cookies sind Datensätze, die auf dem Rechner des Nutzers gespeichert werden. In der Regel als Textdatei. Personalisierte Dienste sind auf die darin enthaltenen Daten angewiesen.  
Webseiten, auf denen Werbung eingeblendet wird, gehen noch einen Schritt weiter und legen Third-Party-Cookies auf den Rechnern ihrer Besucher ab. Auf diese Weise kann der Werbeanbieter den Nutzer über Webseiten hinweg verfolgen. Third-Party-Cookies sind generell zu blockieren. Sie dienen ausschließlich zum Tracking der besuchten Webseiten. Auf sie zu verzichten bedeutet keinen Komfortverlust.  

### Identifikation über aktive Inhalte / Deanonymisierung durch aktive Inhalte

Neben Cookies gibt es noch weitere Möglichkeiten Nutzer zu identifizieren. Aktive Inhalte, wie zum Beispiel Flash, Java und Javascript, können Maßnahmen zur Anonymisierung aushebeln. Beispielsweise wenn Proxy-Lösungen oder Anonymisierungsnetzwerke, wie JonDonym oder Tor, eingesetzt werden.  
Aktiviertes Javascript kann die echte IP-Adresse verraten, auch wenn sie über Tor oder JonDonym verschleiert wurde.  
Wirksame Anonymisierung setzt die Deaktivierung von aktiven Inhalten voraus. Leider ist es oft so, dass Webseiten ohne Javascript nicht oder nur schwer zugänglich sind.

### Browser-Anonymisierung

Insbesondere die Werbeindustrie lässt sich immer wieder neue Techniken einfallen, um einen Benutzer wiederzuerkennen. Typisches Beispiel ist das setzen von Cookies auf dem Rechner der Webseiten-Besucher. Doch auch wenn der Nutzer Cookies abgeschaltet hat, gibt es da noch den DOM-Storage und im Zweifelsfall das Fingerprinting (Browser-Version, Auflösung, Fenstergröße, Plugins, ...), anhand dem man den Nutzer wiedererkennen kann.

Hierzu gibt es das Konzept eines anonymisierenden Browsers. Dazu werden die Web-Inhalte nicht im Browser des Anwenders, sondern im Browser innerhalb einer Sandbox auf einem Anonymisierungs-Server gerendert. Von dort aus kommen die Webinhalt dann auf den Browser des Anwenders. Alle Elemente und Inhalte, die den Nutzer identifizieren oder gar gefährden könnten, werden verschleiert und auf dem Server ausgeführt. Dazu zählt die Verschleierung der IP-Adresse, das Setzen von Cookies und ausführen von Javascript auf dem Server.  
Allerdings dient der Server als Proxy, was dazu führt, dass die Daten über Dritte laufen. Das ist dann ein Problem, wenn man zum Beispiel Online-Banking betreibt oder sich anderweitig Authentifizieren muss.

### Sinn und Unsinn der Anonymisierung

Grundsätzlich besteht das Recht auf Meinungsfreiheit und informelle Selbstbestimmung. Weiterhin gibt es das Recht auf die anonyme Nutzung von Internetdiensten nach Paragraf 13 (6) des Telemediengesetzes: "Der Diensteanbieter hat die Nutzung von Telemedien und ihre Bezahlung anonym oder unter Pseudonym zu ermöglichen, soweit dies technisch möglich und zumutbar ist." Damit ist Anonymität ein Grundrecht und sogar gerichtlich bestätigt worden.

Aber, sich im Internet anonym zu bewegen ist nicht so einfach. Eine echte oder absolute Anonymität ist im Internet praktisch nicht möglich. Egal welche Technik, die Anonymität ist immer relativ. Das liegt an den IP-Adressen, die zur Adressierung von Sender und Empfänger genutzt werden. Anhand der IP-Adressen lassen sich Datenpakete einer Verbindung zuordnen und über den Inhalt einem konkreten Nutzer zuordnen, sofern darin personenbezogene Daten enthalten sind.

Die Verschleierung der IP-Adresse ist sinnlos, wenn die Gegenseite die Identität mit aktiven Web-Inhalten, wie Flash, Cookies oder Browser-Fingerabdrücken ermitteln kann. Die Nutzung von Anonymisierungsdiensten macht insbesondere dann gar keinen Sinn, wenn man sich bei der Gegenseite durch Benutzername und Passwort identifizieren muss. Ist man bei einem Dienst mit einem Nicknamen (Pseudonym) angemeldet, mit dem keine Identitätsmerkmale verknüpft sind (Geschlecht, Geburtsdatum, Klarnamen, Adressen, etc.), dann handelt es sich nur um Pseudonymität. In diesem Fall kann man sich die Anonymisierung sparen.

Je aufwendiger die Verschleierung der IP-Adresse, desto aufwendiger ist die Handhabung und problematischer die Nebenwirkungen. Zudem muss man mit Komfortverlust und langsamen Verbindungen leben. Auf manchen Dienst muss man ganz verzichten. Außerdem weisen Anonymisierungsnetze und -dienste verschiedene Schwachstellen auf, die eine Deanonymisierung ermöglichen.

Es ist fatal zu glauben durch Anonymisierung, zum Beispiel Tor, hätte man eine sichere Kommunikation. Das ist nur dann der Fall, wenn beide Seiten eine verschlüsselte Verbindung betreiben. Das gilt auch für eventuell anfallende Metadaten einer Kommunikation. Sicherheit und Anonymität existieren in diesem Moment nicht mehr. Die Anonymisierung funktioniert nur dann, wenn die zu anonymisierende Kommunikation vollständig verschlüsselt ist.