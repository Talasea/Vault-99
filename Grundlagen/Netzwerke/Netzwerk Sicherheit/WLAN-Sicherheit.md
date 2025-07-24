
In Netzwerken mit Leitungen und Kabel setzt das Abhören der Kommunikation das physikalische Anzapfen der Leitung voraus. Da Netzwerkkabel in der Regel innerhalb gesicherter Gebäude und verdeckt verlaufen, ist das Abhören von Anfang an erschwert.  
In einem Funknetz sieht das ganz anders aus. Hier dient der freie Raum als Übertragungsmedium für die Funksignale. Die Reichweite der Datenübertragung wird hier nur durch die Stärke der Funksignale begrenzt. Sobald ein drahtloses Gerät seine Daten sendet, benötigt ein Angreifer nur ein Empfangsgerät, dass sich in Reichweite der Funksignale befindet, um Daten empfangen zu können.  
Gleichzeitig besteht die Gefahr, dass nicht autorisierte Personen die WLAN-Infrastruktur benutzen oder Zugang zu einem Netzwerk erhalten.  
Deshalb sind Sicherheitsvorkehrungen zu treffen. Konkret die Verschlüsselung der Datenpakete und die Authentifizierung von Benutzern und WLAN-Clients.

Am Anfang der WLAN-Entwicklung war der IEEE-Standard 802.11 ein einziges Sicherheitsrisiko. Der Zugang zum WLAN war offen, also ohne Authentifizierung des Benutzers und die Datenübertragung war unverschlüsselt und somit für jeden einsehbar. Beides ist aus Sicherheitsgründen völlig inakzeptabel.

Um ein WLAN sicher zu betreiben ist die Authentifizierung des Benutzers und die Verschlüsselung der Datenübertragung notwendig. Die deutsche Rechtsprechung sieht die Authentifizierung und Verschlüsselung eines WLANs zwingend vor. Der Betreiber eines unzureichend gesicherten WLANs gilt bei strenger Rechtsauslegung als Störer und wird demzufolge bei einer Rechtsverletzung über seinen Internet-Anschluss in Haftung genommen.  
Wer einen WLAN-Router oder Access Point betreibt, der sollte darauf achten, dass die Authentifizierung und Verschlüsselung immer eingeschaltet ist.


### Übersicht: WLAN-Sicherheit

Wegen der Erfordernis von Verschlüsselung und Authentifizierung in WLANs wurde in einem Schnellschuss WEP entwickelt. Doch schnell stellte sich heraus, dass es sich mit einfachen Mitteln knacken lässt. Die Schwachstellen wurden mit dem Nachfolger WPA Großteils eliminiert. Parallel entwickelte das IEEE den Standard IEEE 802.11i mit einem sicheren Verschlüsselungsverfahren auf Basis von AES. Aus dem Standard IEEE 802.11i ist WPA2 entstanden. WPA2 gilt als hinreichend sicher und ist gegenüber WEP und WPA zu bevorzugen.  
WPS dient der einfacheren Authentifizierung per Pin oder Button, um einen WLAN-Client an einem per WPA- oder WPA2-gesicherten WLAN anzumelden. Leider führt diese Vereinfachung dazu, dass die Authentifizierung unsicherer wird, solange WPS aktiviert ist.

- [WEP](https://www.elektronik-kompendium.de/sites/net/0905251.htm) (unsicher und veraltet)
- [WPA](https://www.elektronik-kompendium.de/sites/net/2009011.htm) (veraltet)
- [WPA2](https://www.elektronik-kompendium.de/sites/net/0907111.htm) (veraltet)
- [WPS](https://www.elektronik-kompendium.de/sites/net/1801211.htm) (unsicher und aktuell)
- [WPA3](https://www.elektronik-kompendium.de/sites/net/2307251.htm) (sicher und aktuell)

### WLAN-Authentifizierung

Bei der WLAN-Authentifizierung geht es darum, dass sich der Benutzer gegenüber dem Wireless Access Point (WAP) authentifiziert. Also glaubhaft macht, dass er das WLAN benutzen darf. Dazu gibt es im wesentlichen zwei Verfahren. Das eine besteht aus einem Passwort, dem sogenannten Pre-shared Key. Also eine geheime Zeichenkette, die als Zugangsschlüssel oder Kennwort dient, und im Regelfall als WLAN-Passwort bezeichnet wird. Nur durch Eingabe dieses Passworts gewährt der Wireless Access Point dem betreffenden WLAN-Client Zugang zum WLAN.  
Eine andere Möglichkeit besteht darin, zentral gesteuert, Benutzername und Passwort des Benutzers abzufragen. Typischerweise per IEEE 802.1x. Das hat den Vorteil, dass jeder Benutzer eigene Zugangsdaten hat, die sich zentral aktivieren und deaktivieren lassen.

- [Pre-shared Key (Authentifizierung mit WLAN-Passwort)](https://www.elektronik-kompendium.de/sites/net/1101181.htm)
- [IEEE 802.1x (Authentifizierung per Benutzername und Passwort)](https://www.elektronik-kompendium.de/sites/net/1409281.htm)

### WLAN-Verschlüsselung

Unter Verschlüsselung versteht man Verfahren und Algorithmen, die Daten mittels digitaler bzw. elektronischer Codes oder Schlüssel inhaltlich in eine nicht lesbare Form umwandeln. Gleichzeitig wird dafür gesorgt, dass nur mit dem Wissen eines Schlüssels die geheimen Daten wieder entschlüsselt werden können.

- [Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/1907041.htm)
- [Kryptografie](https://www.elektronik-kompendium.de/sites/net/1901151.htm)

### Schwachstellen einer WLAN-Infrastruktur

- Default-Benutzer und -Passwörter in Access Points und WLAN-Routern
- Unsichere Grundkonfiguration von Access Points und WLAN-Routern
- Veraltete Sicherheitsstandards
- Fehlerhafte Implementierungen von WPA2 und WPS
- Angreifbarkeit durch Denial-of-Service (DoS)
- Evil Twin und MAC-Spoofing
- Unsichere Benutzer-Access-Points in Enterprise-Netzwerken

### Veraltete Sicherheitsstandards

Ein großes Problem sind veraltete Sicherheitsstandards, die immer noch von WLAN-Geräten unterstützt werden. Leichtsinnigerweise haben einige WLAN-Betreiber veraltete Standards unabsichtlich oder aus Kompatibilitätsgründen immer noch aktiviert. Sie stellen auf diese Weise sicher, dass auch alte Geräte Zugang zum WLAN bekommen. Zum Beispiel mit WEP und WPA mit TKIP. So macht man es einem Angreifer natürlich einfach, sich trotz Authentifizierung und Verschlüsselung Zugang zu verschaffen.  
Wer immer noch WEP verwendet, der handelt nach Ansicht von Sicherheitsexperten grob fahrlässig. WLAN-Komponenten mit WPA2 sind so günstig zu haben, dass es für den Austausch der veralteten Geräte mit WEP oder WPA gegen neue mit WPA2-Verschlüsselung keine Ausrede gibt.

Seit 2011 dürfen neue Wireless Access Points (WAP) kein TKIP mehr unterstützen. Seit 2012 gilt das für alle WLAN-Geräte (Clients und WAP). Seit 2014 dürfen neue Wirless Access Points nur noch WPA2-AES anbieten. In der Praxis sieht das leider anders aus.

### Sniffing und War-Driving

Sniffing und War-Driving sind gängige Bezeichnungen für das Ausspionieren von WLANs. Dabei werden spezielle WLAN-Adapter verwendet, die mittels eines Treibers zum Channel Hopping verwendet werden. So lässt sich das Frequenzspektrum nach WLANs absuchen. Über einen Monitor-Modus hören die WLAN-Adapter passiv mit, nehmen aber keine Verbindung auf.  
Im einfachsten Fall ist War-Driving das Umherfahren mit einem Auto in dem sich ein Laptop mit eingebautem WLAN-Adapter und externer Antenne befindet. In Kombination mit einem GPS-Empfänger lässt sich der Standort eines WLANs protokollieren, um ihn später auf einer Karte wiederzufinden. Mit einer speziellen Software, einem Sniffer, werden alle WLANs erkannt und protokolliert. Auch ob sie offen oder verschlüsselt sind, welches Access-Point-Equipment verwendet wird (bekannte Sicherheitslücken?) und welche Netzwerkgeschwindigkeit vorliegt. Offene WLANs ohne Verschlüsselung laden dann regelrecht zum Eindringen in das Netzwerk ein.  
War-Driving war in der Anfangszeit der WLANs ein beliebter Sport, weil viele WLANs nicht verschlüsselt waren. Heute ist War-Driving uninteressant, weil auch private WLANs standardmäßig verschlüsselt sind, was den Zugang mit einfachen Mitteln erschwert.

### Nutzung fremder WLANs

Für alle, die ein wenig Paranoia tanken wollen: Fremde WLANs zu nutzen ist riskant. Man weiß nicht, wer das WLAN betreibt und wer es noch parallel nutzt. Deshalb haben fremde WLANs einen völlig unbekannten Sicherheitsstatus. Dabei geht es gar nicht darum, dass man das WLAN von Freunden oder Bekannten nicht nutzen soll. Das Problem ist, dass sich der eigene WLAN-Client unter Umständen mit WLANs verbindet, die nur ein bekanntes WLAN vortäuschen. Also eines, an das man sich schon angemeldet hat und die selben Zugangsdaten auch bei dem unbekannten WLAN gelten. Im Regelfall sollten die gleichen Zugangsdaten in einem anderen WLAN nicht vorkommen. Es sei denn, das ist Absicht, weil man zur größeren Funkabdeckung mehrere Access Points betreibt, deren WLAN-Namen und -Passwörter bequemerweise identisch sind. Anders sieht es aus, wenn ein Angreifer ein WLAN dupliziert und auf diese Weise Zugangsdaten zu Webseiten oder unverschlüsselte Daten abgreift.

Aus Sicherheitsgründen sollte man nur das WLAN zu Hause benutzen und unterwegs über Mobilfunk. Wenn man unterwegs auf die Nutzung fremder WLAN nicht verzichten will, dann nur mit einer zusätzlichen VPN-Verbindung. Die sorgt dafür, dass auch unverschlüsselter Datenverkehr über eine gesicherte Verbindung übertragen wird.

### WPS - Wi-Fi Protected Setup

WPS ist eine Spezifikation des Industriekonsortiums Wi-Fi Alliance (WFA) hinter der sich eine Konfigurationsautomatik verbirgt. WPS erleichtert die WLAN-Konfiguration von WLAN-Clients. Die Konfiguration erfolgt entweder per Knopfdruck (WPS-PBC) oder Pin-Eingabe (WPS-PIN).  
Die Hauptschwierigkeit bei der Konfiguration eines WLAN-Clients ist die Eingabe des WLAN-Passworts (Pre-Shared-Key), welches im Access Point hinterlegt ist. WPS vereinfacht und automatisiert diese Umständlichkeit.

Leider wird mit aktiviertem WPS eine Schwachstelle erzeugt, weshalb WPS-Router ein lohnenswertes Ziel für Angreifer sind. Die Schwachstelle ergibt sich durch eine schwache Zufallszahlenerzeugung und die Möglichkeit per Brute-Force-Angriff die WPS-Pin innerhalb weniger Stunden oder sogar Minuten herauszubekommen. Diese Schwachstelle ist sogar so groß, dass ein Angriff auf ein per WPS-gesichertes WLAN in der Regel immer von Erfolg gekrönt ist (abhängig von der Implementierung).

- [WPS - Wi-Fi Protected Setup](https://www.elektronik-kompendium.de/sites/net/1801211.htm)

### WDS - Wireless Distribution System

Das Wireless Distribution System (WDS) lässt WLAN-Basisstationen den Datenverkehr ohne Umweg über ein LAN direkt miteinander austauschen. Viele Hersteller nutzen WDS für eine einfache Implementierung von WLAN-Repeatern. Ein WLAN-Repeater empfängt WLAN-Signale und sendet sie weiter. Auf diese Weise verlängert er den Funkweg bzw. erhöht die Reichweite eines WLANs.  
Leider ist WDS nicht genau genug spezifiziert. Das führte dazu, dass WDS zusammen mit WPA2, herstellerübergreifend nicht immer funktioniert. Hier besteht die Gefahr, dass die Nutzer auf funktionellen Gründen auf Authentifizierung und Verschlüsselung verzichten.

- [WDS - Wireless Distribution System (WLAN-Repeater)](https://www.elektronik-kompendium.de/sites/net/1407071.htm)

### Wie sicher ist WLAN-Sicherheit?

Fast alle Verfahren zur WLAN-Sicherheit weisen in irgendeiner Weise Schwachstellen auf. Sofern die Verfahren richtig implementiert sind, reicht deren Sicherheit im Privat-Bereich aus. Die Gefahr geht hier meist nur von einem Angreifer aus, der einen erfolgreichen Verbindungsaufbau mitschneidet und das Passwort mit einem Wörterbuch-Angriff errät. Bereits für wenige Dollar kann man die Rechenleistung mieten, um das Passwort eines WLAN-Mitschnitts in relativ kurzer Zeit zu errechnen.

Im kommerziellen oder großräumigen Einsatz sollte ein WLAN immer im Enterprise Mode mit IEEE 802.1x gesichert werden. Nur der Enterprise Mode von WPA2 bietet den sichersten Schutz, weil hier der WLAN-Schlüssel an individuelle Zugangsdaten gebunden ist. Allerdings verschiebt sich hier der Angriffsvektor auf diese Zugangsdaten, die man nur mit Zertifikaten vollständig absichern kann.  
Das Abhören und Entschlüsseln der Datenübertragung im WLAN ist dann nur mit unverhältnismäßig hohem Aufwand möglich. Wer ganz sicher gehen will, der lässt die Finger von WLAN und überträgt seine Daten ausschließlich über Kabelverbindungen.

Offene WLANs (ohne Authentifizierung und Verschlüsselung) sollte man nicht betreiben und eigentlich auch nicht nutzen. Auch wenn das sehr bequem ist. Man sollte sich darüber im Klaren sein, dass jeder andere WLAN-Nutzer den unverschlüsselten Datenverkehr abhören kann. Lässt sich die Nutzung eines unverschlüsselten WLANs nicht vermeiden, sollte die Datenübertragung mit zusätzlichen Maßnahmen geschützt werden. Mit SSL, SSH und IPsec lässt sich die Kommunikation zwischen Anwendungen sicherer machen.

### 6 einfache Maßnahmen für eine grundlegende WLAN-Sicherheit

1. Eigenes Admin-Passwort für den Access Point (Router, etc.) vergeben. Aufschreiben und an einem sicheren Ort aufbewahren ist erlaubt.
2. Eigenes WLAN-Passwort mit mindestens 16 Zeichen für den Access Point vergeben. Aufschreiben und an einem sicheren Ort aufbewahren ist erlaubt.
3. Schalten Sie das Gäste-WLAN ein oder ändern Sie Ihr WLAN-Passwort, wenn sie es Gästen gegeben haben.
4. Schalten Sie nur die WPA2-Verschlüsselung ein. Nicht "WPA/WPA2" oder "mixed".
5. Schalten Sie WPS immer ab, wenn Sie es nicht brauchen.
6. Schalten Sie die Auto-Update-Funktion ihres Routers ein, wenn er eine hat.

### 6 weitere Maßnahmen für eine starke WLAN-Sicherheit (optional)

- Verwenden Sie den Enterprise-Mode.
- Vergeben sie einen undefinierbaren WLAN-Namen (SSID), der nicht auf Sie zurück zu führen ist. Vermeiden Sie Namen und Bezeichnungen, die mit Ihnen persönlich oder Ihrem Standort zu tun haben.
- Trennen Sie WLANs von anderen Netzwerk-Segmenten (Gäste-WLAN).
- Installieren Sie eine Firewall zwischen WLAN und LAN.
- Stellen Sie ein IDS im WLAN auf.
- Führen Sie regelmäßige Audits mit aktuellen Hacker-Tools durch.

### 2 Maßnahmen auf die Sie verzichten können

- Setzen Sie einen MAC-Adressfilter auf Geräte-Ebene ein.
- Verhindern Sie die Bekanntgabe der SSID durch einen Broadcast (Hidden SSID).

### Warum ein MAC-Filter nicht mehr Sicherheit bringt

Ein MAC-Filter ist eine denkbare Maßnahmen, um die Sicherheit eines WLANs zu erhöhen. Allerdings eine eher zweifelhafte. Das Mehr an Sicherheit ist ein Trugschluss und wiegt den dabei entstehenden Komfortverlust nicht auf.  
Ein MAC-Filter verhindert grundsätzlich, dass sich jemand mit einem WLAN verbinden kann, wenn die Hardware-Adresse dessen WLAN-Adapters nicht vorher im Wireless Access Point registriert ist. Der Access Point wird dann jegliche Verbindungsversuche ablehnen. Auch dann, wenn der betreffende Client das richtige WLAN-Passwort hat.

Allerdings ist es in der Praxis so, dass wenn ein Angreifer in dem Wissen ist und die Fähigkeit hat, das richtige Passwort herauszufinden, dann stellt der MAC-Filter für ihn keine wirkliche Hürde dar. Das heißt, findet ein Angreifer das Passwort heraus, dann wird er sich vom MAC-Filter nicht aufhalten lassen.  
Er wird einfach seinen WLAN-Adapter mit der MAC-Adresse eines berechtigten WLAN-Adapters überschreiben. Und schon ist der MAC-Filter umgangen. Von daher kann man auf einen MAC-Filter verzichten.  
Im Prinzip zieht ein MAC-Filter nur einen Komfort-Verlust nach sich und stellt für die WLAN-Nutzung eine zusätzliche Fehlerquelle dar.

- [WLAN-Hacking: MAC-Filter umgehen](https://www.elektronik-kompendium.de/sites/net/2109161.htm)

### Warum das Verstecken des WLAN-Namens (Hidden SSID) nicht mehr Sicherheit bringt

Das Verstecken des WLAN-Namens in der Form "Hidden SSID aktivieren" oder "Broadcast SSID deaktivieren" ist eine denkbare Maßnahme, um die Sicherheit eines WLANs zu erhöhen. Denn der Angreifer braucht nicht nur das WLAN-Passwort, sondern auch den WLAN-Namen, um sich an einem WLAN authentifizieren zu können. Allerdings ist "Hidden SSID" als Sicherheitsmaßnahme eher zweifelhaft und auch nicht standardkonform. Das scheinbare Mehr an Sicherheit wiegt den Komfortverlust nicht auf.

1. Als Anwender muss man beim ersten Verbinden mit dem versteckten WLAN, die Verbindung manuell anlegen.
2. Manche WLAN-Clients, die den Access Point nicht sehen können, können sich dort auch nicht anmelden.
3. Weil manche WLAN-Adapter und -Clients mit versteckten SSIDs nicht klarkommen, erhöht sich die Fehlerrate und die Fehlersuche.

Auch das Argument, dass versteckte WLANs von War-Drivern und WLAN-Hackern nicht gefunden werden ist falsch. Selbstverständlich ist ein WLAN mit "Hidden SSID" sichtbar, nur ohne Namen. Ein tatsächlich interessierter Angreifer wird sich von einer versteckten SSID nicht abschrecken lassen. Er sieht das WLAN ohne Namen. Und sobald sich ein Client an einem WLAN mit versteckter SSID anmeldet, wird dabei die SSID übertragen.

Für einen WLAN-Hacker ist der WLAN-Name eigentlich irrelevant. Denn erstens benötigt der Angreifer für die meisten Angriffe den WLAN-Namen gar nicht. Und wenn doch, dann kann er per De-Authentication-Angriff die verbundenen WLAN-Clients zur erneuten Anmeldung zwingen. Im Rahmen der erneuten Authentifizierung eines WLAN-Clients kann der Angreifer die SSID ermitteln. Für einen Angreifer, der tatsächlich willens und in der Lage ist, das WLAN-Passwort herauszubekommen, ist das kein Hindernis, sondern eine leichte Fingerübung.

Wer jetzt trotzdem glaubt, dass das Verstecken der SSID eine sinnvolle Maßnahme ist, der sollte sich darüber im Klaren sein, dass es zu einer Sicherheitslücke führen kann. Normalerweise würde der WLAN-Access-Point regelmäßig über sein WLAN informieren. Wenn er das nicht tut, dann muss der WLAN-Client, der einmal damit verbunden war, aktiv nach diesem WLAN suchen. Deshalb broadcastet dieser Client regelmäßig die SSID von sich aus heraus. Er ruft praktisch ständig nach dem versteckten WLAN. Auch wenn das gar nicht in der Nähe ist.

Wenn nun ein WLAN-Hacker in ein WLAN mit versteckter SSID eindringen will, dann bringt er zuerst die SSID in Erfahrung. Das ist kein Problem, weil die Clients sehr gesprächig sind. Der Angreifer richtet dann einen eigenen Access Point mit der gleichen SSID ein. Irgendein WLAN-Client wird sich dann mit diesem vermeintlich bekannten WLAN verbinden. Beim Anmeldeversuch kann der Angreifer dann den WPA-Handshake abgreifen und durch Ausprobieren das Passwort herausfinden. Und das ganze ohne in der Nähe des WLANs sein zu müssen.

- [WLAN-Hacking: Hidden SSID/ESSID ermitteln](https://www.elektronik-kompendium.de/sites/net/2109151.htm)

### Schwachstelle: Rogue Access Point

Ein "Rogue Access Point" ist ein benutzerdefinierter Access Point, der ohne Authentifizierung (Open Authentication) und ohne Verschlüsselung (No Encryption) betrieben wird und WLAN-Clients eine Verbindung zu einem Netzwerk ermöglicht, das eigentlich eine Authentifizierung vorsieht.  
"Rogue Access Points" werden oftmals von technisch versierten Anwendern betrieben, denen die Sicherheitsmaßnahmen in einem Netzwerk zuwider und die bezüglich Sicherheitsanforderungen und kritischer Schwachstellen wenig sensibilisiert sind. Sie betreiben das offenes WLAN, um mehr Komfort zu bekommen und nehmen dabei in Kauf, die sinnvollen und notwendigen Sicherheitsmaßnahmen zu umgehen.  
"Rogue Access Points" lassen sich nicht ganz verhindern und sind nur im Rahmen eines Pentests zu ermitteln. Da der Standort nicht exakt bekannt ist, muss man meistens auf die Suche gehen.

### Rechtliche Bedeutung eines unverschlüsselten WLANs

Ein offenes WLAN stellt sich wie ein offenes Scheunentor dar. Beim Surfen über das offene WLAN hinterlässt die IP-Adresse des WLAN-Betreibers eine Spur im Netz. Diese IP-Adresse kann im nachhinein dem Anschlussinhaber zugeordnet werden. Der Anschlussinhaber wird daher im Rahmen einer Rechtsverletzung als erster Verdächtiger ermittelt. Schnell kann es vorkommen, dass man eine Straftat angehängt bekommt, obwohl Fremde den unverschlüsselten WLAN-Zugang missbraucht haben. Da hilft es dann auch nicht zu erklären, man habe nur seinen Nachbar ins Netz gelassen oder versehentlich die Verschlüsselung abgeschaltet. Wer einen WLAN-Router oder Wireless Access Point betreibt sollte darauf achten, dass die Verschlüsselung immer eingeschaltet ist.

### Übersicht: Grundlegende Maßnahmen zur WLAN-Sicherheit

- [WEP](https://www.elektronik-kompendium.de/sites/net/0905251.htm) (technisch veraltet und nicht mehr zeitgemäß)
- [WPA - Wi-Fi Protected Access](https://www.elektronik-kompendium.de/sites/net/2009011.htm) (technisch veraltet und nicht mehr zeitgemäß)
- [WPA2 - Wi-Fi Protected Access 2 / IEEE 802.11i](https://www.elektronik-kompendium.de/sites/net/0907111.htm)[](https://www.elektronik-kompendium.de/sites/net/0907111.htm)
- [WPS - Wi-Fi Protected Setup](https://www.elektronik-kompendium.de/sites/net/1801211.htm)
- [WPA3 - Wi-Fi Protected Access 3](https://www.elektronik-kompendium.de/sites/net/2307251.htm)