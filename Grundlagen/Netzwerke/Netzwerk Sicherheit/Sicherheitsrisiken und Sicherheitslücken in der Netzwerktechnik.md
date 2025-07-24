
Sicherheitsrisiken und Sicherheitslücken geben immer wieder den Anlass über die Qualität und den Einsatz von Maßnahmen und Verfahren, die Datenschutz und Datensicherheit herstellen sollen, nachzudenken.  
Dabei kommt man in der Regel zu der Erkenntnis, dass man alles was wir über Sicherheit in der Computer- und Netzwerktechnik wissen als überholt ansehen kann. Man muss im Prinzip immer davon ausgehen, dass der Angreifer bereits Sicherheitslücken entdeckt hat und sich innerhalb der eigenen Organisation oder im Netzwerk befindet. Im Falle der Geheimdienste muss man sich bewusst sein, dass diese prinzipiell in der Lage sein können, wirksame Verschlüsselungen und Sicherheitssysteme auszuhebeln.

Absolute Sicherheit gibt es nicht. Alle im Einsatz befindlichen Sicherheitssysteme, -verfahren und -methoden weisen zwangsläufig Risiken auf, die man eingehen muss und deren man sich oft gar nicht bewusst ist. Sicherheitslücken entstehen immer dort, wo Sicherheitskonzepte oder Implementierungen fehlerhaft sind. Zum Nachteil der Anwender, die das nicht erkennen können.

Eine große Sicherheit bedeutet auch immer ein Komfortverlust und verhindert die Akzeptanz auf der Seite der Anwender. Der Anwender möchte es möglichst einfach haben und möchte sich nicht mit den Aspekten von Sicherheitskonzepten und deren Einschränkungen belasten. Deshalb ist Datenschutz und Datensicherheit bei der Nutzung von Netzwerk- und Internet-Diensten selten von großer Bedeutung. Hier muss man bedenken, dass der einzelne Anwender wenig zu verlieren hat. Bei Unternehmen und Organisationen sieht es schon ganz anders aus. Hier sind Daten in großer Menge gespeichert, die viel eher das Interesse von Kriminellen und Geheimdiensten wecken. Weshalb man hier öfters in den Medien hört, sieht oder liest, dass Kundendaten, Bankverbindungen und Zugangsdaten gestohlen wurden. Leider wird dann im Nachgang nicht darüber berichtet, dass die Kriminellen damit in größerem Stil auf Beutezug gegangen sind. Vermutlich, weil mit diesen Daten nicht wirklich etwas anzufangen ist.

- [Grundlagen der Netzwerk-Sicherheit](https://www.elektronik-kompendium.de/sites/net/0908021.htm)
- [Sicherheitskonzepte in der Informations- und Netzwerktechnik](https://www.elektronik-kompendium.de/sites/net/1901181.htm)

### Beispiele für Angreifer

- Kriminelle Hacker: Suchen und nutzen Lücken in Software und Systemen, die weit verbreitet ist und viele nutzen. In der Regel geht es darum Daten abzugreifen oder Systeme zu stören.
- Geheimdienste und Strafverfolgungsbehörden: Verfügen über nahezu unbegrenzte Mittel und Zeit. Außerdem tauschen sie sich aus. Wollen vor allem personenbezogene Daten sammeln.
- Kommerzielle Datensammler: Klassische Datensammler (Tracking) zeichnen digitale Spuren von Personen auf und verkaufen sie an Datenhändler und Datenauswerter (Analyse).

Hierbei gilt es folgende Umstände zu beachten:

- Kriminelle Hacker machen keine Unterscheidung bei Ihren Angriffszielen und hacken deshalb auch Datensammler und Geheimdienste.
- Geheimdienste haben Zugriff auf Datensammler und hacken auch Hacker.
- Datensammler nutzen von Hackern veröffentlichte Daten.

Fazit: Wenn man da genau draufschaut, spielt es keine Rolle, welchen Angreifer man fürchtet. Abgegriffene Daten landen im Zweifel bei allen anderen. Es ist nur eine Frage der Zeit.

### Typische Angriffe im OSI-Schichtenmodell

- Schicht 7: Application: Exploit und Injections
- Schicht 6: Presentation: Phishing
- Schicht 5: Session: Hijacking
- Schicht 4: Transport: Reconnaissance
- Schicht 3: Internet: Man-in-the-Middle
- Schicht 2: Data Link: Spoofing
- Schicht 1: Physical: Sniffing

### Beispiele für Sicherheitslücken

Die folgenden Sicherheitslücken sind Beispiele, wo Sicherheitsrisiken durch Sicherheitslücken entstehen könnten. Sie sollen nur einen kurzen Einblick geben. Alle denkbaren Sicherheitslücken aufzulisten ist durch die Masse an Möglichkeiten und dem menschlichen Erfindungsreichtum praktisch unmöglich. Dementsprechend gibt es auch keinen absoluten Schutz vor Sicherheitslücken.

- Zero-Day-Exploit (Fehler in der Software)
- Geheime Hintertüren in Hardware und Software (Backdoor)
- unzureichende Zugangskontrolle zur Infrastruktur (temporär geöffnete Türen von EDV-Räumen)
- Konfigurationsoberflächen übers Internet erreichbar
- ungesicherte System- und Konfigurationsdateien
- fest einprogrammierte Administrationspasswörtern
- Möglichkeit zum Einschleusen von Befehlen oder Programmen
- unzureichende Begrenzung der Berechtigung (großzügig ausgelegte Berechtigungen)
- veraltete Hardware und Software mit unzureichenden Sicherheitsstandards
- [offene Ports in der Firewall](https://www.elektronik-kompendium.de/sites/net/1812041.htm)

### Beispiele für Angriffsszenarien

Das Infizieren von Systemen mit Schadsoftware oder Einbrechen (Umgehen von Authentifizierungsmaßnahmen) in Systeme und das anschließende Ausspionieren von weiteren verwertbaren Daten sind getrennte Aufgaben und werden in der Regel von unterschiedlichen Programmen ausgeführt.  
Dazu besorgen sich die Kriminellen aus unterschiedlichen Quellen die Komponenten zusammen, die teilweise auch kostenpflichtig sind. Zum Beispiel ein Exploit-Kit, das nach Sicherheitslücken sucht. Ein Trojaner, der vom Exploit-Kit nachgeladen wird. Dazu mietet man sich bei einem Hoster den Speicherplatz und Leitungskapazität. Alternativ lässt sich die URL per Mail an eine gekaufte Adressliste verschicken, in der Hoffnung, der Empfänger klickt drauf und installiert sich so den Trojaner auf den Rechner.

- Brute-Force-Attacke auf Konten und Logins
- [DoS - Denial of Service](https://www.elektronik-kompendium.de/sites/net/1412091.htm)
- [Man-in-the-Middle](https://www.elektronik-kompendium.de/sites/net/1710251.htm)
- [IP-Spoofing](https://www.elektronik-kompendium.de/sites/net/1412101.htm)
- [Drive-by](https://www.elektronik-kompendium.de/sites/net/1412111.htm)
- SQL-Injection
- Social Engineering
- Phishing
- APT - Advanced Persistent Threat
- Staatliche Überwachung

Im folgenden werden häufige und typische Angriffe beschrieben.

#### DDoS - Distributed Denial of Service

DDoS ist eine Form, um die Erreichbarkeit einer Infrastruktur durch Überlastung zu stören. In der Regel werden Server durch absichtlich herbeigeführte massenhafte Anfragen überlastet. Das Ziel ist, dass bei Dienstanbietern Umsatz- und Imageschäden entstehen.

- [DoS - Denial of Service](https://www.elektronik-kompendium.de/sites/net/1412091.htm)

#### Social Engineering

Unter Social Engineering versteht man eine Vorgehensweise, bei der ein Angreifer ein Opfer mit soziologischen und psychologischen Tricks dazu bringt, von sich aus Daten preiszugeben, um Schutzmaßnahmen umgehen zu können. Das Ziel ist, Schadprogramme auf den Rechner des Opfers zu bekommen. Oder das Opfer dazu zu bewegen eine Sicherheitslücke zu erzeugen.

#### Phishing

Beim Phishing geht es darum, nach „Passwörtern oder Zugangsdaten zu angeln“. In der Regel bekommt das Opfer täuschend echt aussehende E-Mails von ihm bekannte Personen oder Unternehmen mit der Bitte persönliche Daten oder sogar Zugangsdaten zu übermitteln oder auf manipulierten Webseiten einzugeben. Das Ziel ist, an Daten zu gelangen, um diese wiederum für Identitätsdiebstahl zu missbrauchen.

#### APT - Advanced Persistent Threat

Ein APT ist ein gezielter Angriff gegen Organisation, bei denen eine große und wertvolle Menge an Daten zu bekommen sind. Diese Art von Angriff zeichnet sich durch ein hohes Maß an Ressourceneinsatz und technisches Know-how aus, den man nur schwer erkennen kann. Das Ziel ist einen dauerhaften Zugriff auf ein Netzwerk und die Ressourcen zu bekommen.

### Beispiele für Schadsoftware

- Ransomware
- Malware
- Adware
- Bot

Im folgenden wird häufige und typische Schadsoftware beschrieben.

#### Ransomware

Ransomware ist ein Schadsoftware, die versucht Funktionen zu unterbinden oder Daten verschlüsselt, und deren Freischaltung oder Entschlüsselung durch Forderung eines Lösegeldes (ransom) anbietet. Das Ziel des Angreifers ist, die Verfügbarkeit einer Ressource einzuschränken, um Geld gegen Freigabe zu erpressen. Das Problem dabei ist, dass nach Zahlung des Lösegelds, meist in einer Kryptowährung, die Ressource nicht zwangsläufig freigeschaltet wird.

#### Malware

Unter Malware versteht man sämtliche Schadprogramme, wie Trojaner, Würmer, Adware, Spyware oder Viren. Das Ziel ist, sich in fremde Systeme einzuschleusen, um Zugriff auf Daten zu erhalten oder weitere Schadprogramme nachzuladen.

#### Adware

Adware ist Schadsoftware, die über Werbung auf Rechnern eingeschleust wird. Das Ziel ist Schadsoftware direkt auf Computern zu installieren.

#### Bot

Ein Bot ist ein fernsteuerbares Schadprogramm, die über Hacking, Ransomware, Malware oder Adware auf einen Computer kommt. Zusammen mit vielen anderen Bots bildet sich ein Netz von Rechnern, auch Botnetz genannt. Das Botnetz wird durch einen Botnetzbetreiber von einem Command-and-Control-Server gesteuert. Das Ziel ist, die Ressourcen von fremden Computern für eigene Zwecke zu nutzen oder zu vermieten. Beispielsweise für DDoS-Angriffe.

- [Botnetze](https://www.elektronik-kompendium.de/sites/net/1501041.htm)

### Wo Sicherheitsrisiken lauern können

- Anwender
- BYOD - Bring your own Device
- Zertifizierung
- Authentifizierung
- Verschlüsselung
- Schlüsselgenerierung

### Sicherheitsrisiko: Anwender

Der Anwender gilt als größtes Sicherheitsrisiko. Dabei ist er das nicht einmal mutwillig. In der Regel ist es reine Unwissenheit. Deshalb ist es notwendig, den Anwender für Sicherheitsrisiken zu sensibilisieren. Vor allem unbedarfte Anwender gehen oft naiv ans Werk, was EDV und IT angeht. Dabei liegt der Unterschied zwischen sicher und unsicher häufig nur einen Klick entfernt. Zum Beispiel wenn der Anwender sich einen Virus, Wurm oder Trojaner einfängt.

Einen Computerschädling fängt man sich im Prinzip nur über zwei Wege ein. Entweder ohne eigenes Verschulden über eine Sicherheitslücke im Betriebssystem oder einer installierten Software. Wobei man sich hier als Anwender schuldig macht, wenn man die regelmäßig angebotenen Sicherheitsupdates nicht einspielt. Selbst wenn die Hersteller Sicherheitslücken schließen, sind da noch die Anwender, die ihre Systeme nur unzureichend auf dem aktuellen Stand halten. So bleiben lange bekannte Sicherheitslücken offen. Nichts ist schlimmer, als veraltete Software (Virenscanner, Flash, Adobe-Reader, Java, etc.).

Eine andere Gefahrenquelle drängt sich durch E-Mails mit Anhang auf. Durch so manchen voreiligen Klick haben sich auch erfahrene Anwender schon Schädlinge auf den eigenen Rechner geladen. Da der Schädling möglichst nicht entdeckt werden will, erfolgt die Installation benutzerfreundlich im Hintergrund. Das was nicht stimmt, erfährt man als Anwender erst dann, wenn es zu spät ist. Manchmal überhaupt nicht.  
Der letztere Fall dürfte der Hauptinfektionsweg sein. Wobei der eine oder andere Anwender sich Sicherheitslücken und Schädlinge schon selber installiert hat. Wer auf die Schnelle ein nützliches Programm von einer nicht vertrauenswürdigen Quelle aus dem Internet lädt oder von "Freunden" installieren lässt, der ist selbst Schuld, wenn hinterher der eigene Computer infiziert ist.

Um sich vor Viren, Würmern und Trojanern zu schützen wird deshalb Antiviren-Software auf Computer installiert. Sie können über 90 Prozent der Schädlinge erkennen und sind in der Lage, bösartige Aktionen zu stoppen und sogar rückgängig machen.

##### Weitere typische Anwenderfehler:

- Verwendung von Standard-Passwörtern
- Verwendung unsicherer Passwörter
- versehentlich aktivierte Datenfreigaben

### Sicherheitsrisiko: BYOD - Bring your own Device

Bring your own Device, kurz BYOD, bezeichnet den Trend, dass Arbeitnehmer in Unternehmen ihre eigenen privaten elektronischen Geräte und die darauf befindliche Software innerhalb der Unternehmens-IT nutzen wollen. In der Regel handelt es sich um persönliche Geräte, wie Smartphones, Tablets und Notebooks, die der Anwender für seine privaten Zwecke individuell eingerichtet hat.  
BYOD ist die Reaktion der Arbeitnehmer auf die Unternehmens-IT, die mit den Erfordernisse nicht Schritt halten kann. Hierbei geht es nicht primär darum, Unternehmensanwendungen auf privaten Geräten zu nutzen, sondern um einen effektiven Austausch von Daten und Wissen zwischen Kunden und Kollegen zu ermöglichen. Dazu würden die Anwender gerne die Hilfsmittel verwenden, die Ihnen von ihrer IT-Abteilung bereitgestellt werden. Doch leider spielen hierbei Beschränkungen im Bereich der Sicherheit und der Kosten eine große Rolle.  
IT-Abteilungen hätten es gerne, wenn eine strenge Trennung von dienstlichen und privaten  
Geräten erfolgen würde. Nur so lassen sich die oftmals strengen Regeln für den Datenschutz einhalten. Die sind in der Regel nicht verhandelbar. Eine häufig Frage ist, wo die Daten gespeichert werden. Bei BYOD ist das nicht zweifelsfrei zu klären. Kundendaten, auch verschlüsselt, haben in einer Private Cloud nichts verloren. Bei BYOD kann man das aber nicht ausschließen.  
Letztendlich ist es immer auch eine Frage zwischen Sicherheit (BYOD ja) und Flexibilität (BYOD nein).

### Sicherheitsrisiko: Zertifizierung

In der Netzwerktechnik sind Zertifikate eine Möglichkeit, um den Kommunikationspartner zu identifizieren. Dazu befragt man eine Zertifizierungsstelle, die das jeweilige Zertifikat ausgestellt hat. Eine Zertifizierungsstelle ist also eine zentrale Instanz, der man vertraut.  
Ein Risiko entsteht, wenn es einem Angreifer gelungen ist, Zugriff auf eine Zertifizierungsstelle zu bekommen und beliebige Zertifikate erstellen kann.  
Der NSA-Skandal hat aufgedeckt, dass Geheimdienste bestrebt sind, Zertifizierungsstellen unter ihre Kontrolle zu bringen, um das "automatische" Vertrauen zu diesen zentralen Instanzen auf Benutzerseite zu erlangen. Auf diese Weise ist es nicht zwangsläufig möglich verschlüsselte Kommunikation zu entschlüsseln. Allerdings können die Geheimdienste sich Zertifikate ausstellen, die jede Verschlüsselungssoftware oder -bibliothek ungefragt akzeptiert. Man-in-the-Middle-Attacken sind damit leichter möglich. Einfache SSL/TLS-Verbindungen bieten somit keinen ausreichenden Schutz vor dem Zugriff der Geheimdienste.

### Sicherheitsrisiko: Authentisierung

Verschlüsselung wie zum Beispiel mit SSL ist nur so sicher, wie gut ein Programm die Identität der Gegenstelle, also deren Zertifikat, überprüft. Und wie zuverlässig und vertrauenswürdig die Zertifizierungsstelle ist. Angriffe funktionieren häufig nur deshalb, weil die Identität bei der Authentifizierung nur sehr nachlässig geprüft wird oder sogar fehlerhaft ist.  
Wenn zum Beispiel die Zertifizierungsstelle bei der Validierung eines Zertifikats nicht erreichbar ist, dann wird das Zertifikat trotzdem als gültig anerkannt, obwohl es das vielleicht gar nicht ist. Das ist einer der Fehler bei SSL/TLS. Den Fehler zu beheben ist praktisch unmöglich. Momentan begrenzt man nur die Laufzeit von Zertifikaten. So sind Zertifikate für SSL/TLS nur noch 39 Monate gültig.

### Sicherheitsrisiko: Schlüsselgenerierung

Ein Schwachpunkt bei der Verschlüsselung ist der Schlüssel an sich, der nicht vom Mensch, sondern von Zufallszahlengeneratoren (Kombination aus Hardware und Software) erzeugt wird. Wenn der Schlüssel nicht ganz so zufällig erzeugt wird, dann kann er durch einfaches Ausprobieren berechnet werden. Wenn die Anzahl der Zufallszahlen zu gering ist, dann schwächt das jedes kryptografische Verfahren. Es mag noch so gut sein. Wenn die darunterliegende Hardware und Software schwach ist, hilft die beste Verschlüsselung nichts. Solche Sicherheitslücken setzen natürlich entsprechendes Wissen voraus. Es ist davon auszugehen, dass Geheimdienste über entsprechende Spezialisten verfügen.

Eine konkrete Sicherheitslücke bei der Verschlüsselung könnte auch eine schlechte Initialisierung des Pseudozufallszahlen-Generators (Pseudo Random Number Generator, PRNG) sein. Beispielsweise liefert der PRNG korrelierende Zufallszahlen, was er nicht tun sollte. Oder aus immer gleichen Startwerten ergibt sich jedes mal die gleiche Folge. Wenn die Startwerte nicht weit genug auseinanderliegen, dann kann sich der Angreifer mit einer Brute-Force-Attacke auf einen bestimmten Wertebereich beschränken. Das bedeutet, die Verschlüsselung ist schneller geknackt.  
Ein anderes Szenario sieht vor, dass der Algorithmus des Zufallszahlen-Generators manipuliert ist und Hintertüren enthält. Im Zuge der NSA-Affäre kam heraus, dass die NSA bei der Entwicklung und Standardisierung von Algorithmen von Zufallszahlen-Generatoren eingegriffen hat. Die Algorithmen wurden mit Absicht geschwächt.

In der Regel wird empfohlen mehrere unterschiedlich generierte Zufallszahlen miteinander zu kombinieren und zusätzliche Parameter wie die Uhrzeit zum Starten des PRNG zu verwenden.  
Auf alle Fälle muss man verhindern, dass ein Angreifer nur durch den Versuch eine Zufallszahl zu erraten, an die kryptografisch gesicherten Informationen gelangt.

### Sicherheitsrisiko: Fernwartungsfunktionen

Wenn von Fernwartung oder Remote Control die Rede ist, dann meint man damit in der Regel Fernzugriffsmöglichkeiten auf Netzwerke oder Rechner. Meistens werden dafür entsprechende Zugänge eingerichtet mit begrenzenden Berechtigungen versehen und die Verbindungen verschlüsselt.

Was aber, wenn in Netzzugangssystemen versteckte Fernwartungsfunktionen schlummern und nur auf ihre Aktivierung warten? Beispielsweise integriert Intel seit 2006 in bestimmte Chipsätze und Prozessoren Fernwartungsfunktionen, wie Management Engine (ME) und Active Management Technology (AMT), die den Zugriff auf Computer aus der Ferne ermöglichen. Damit werden zum Beispiel Funktionen zum Fernlöschen von gestohlenen Notebooks realisiert.  
Diese Funktionen stehen auch dann zur Verfügung, wenn der Rechner vermeintlich ausgeschaltet ist, das Betriebssystem nicht starten kann oder gar keines installiert wurde. Wer denkt, dass dafür ein Netzwerkkabel eingesteckt sein muss, der irrt. Viele Funktionen sind auch per WLAN oder über eingebaute Mobilfunk-Modems nutzbar.

Hierbei muss man berücksichtigen, dass diese Funktionen nur in bestimmten Prozessoren und Chipsätzen integriert sind. Das bedeutet, dass sie nicht flächendeckend im Einsatz sind, sondern nur dort, wo Unternehmen ihre Rechner übers Netzwerk managen wollen.  
Es ist jedoch nicht von der Hand zu weisen, dass Fernwartungsfunktionen eine Hintertür in ein an sich sicheres System darstellt. Deshalb ist darauf zu achten, dass Fernwartungsfunktionen abschaltbar sind und jederzeit erkennbar ist, ob diese Funktion gerade aktiv ist. Noch besser, der Nutzer muss jede Fernwartungsverbindung explizit bestätigen.

### Beispiel für ein Sicherheitsrisiko: Outlook Web Access

Ein auf Microsoft Exchange Webmail basierendes System könnte ein Sicherheitsrisiko sein. Sofern ein Angreifer ein solches System und die dazugehörige Login-Oberfläche ausfindig gemacht hat, braucht er sich nur noch eine Liste mit zur jeweiligen Domain gehörenden E-Mail-Adressen besorgen. Häufig finden sich diese Adressen auf Webseiten oder in Verzeichnissen, die offen übers Internet erreichbar sind. Anschließend muss der Angreifer nur noch eine Wörterbuch- oder Brute-Force-Attacke auf die gesammelten E-Mail-Adressen starten.

### Beispiel für ein Sicherheitsrisiko: Windows XP

Windows XP ist ein äußerst stabiles und daher beliebtes und oft installiertes Betriebssystem. Die weite Verbreitung ist allerdings ein Problem. Hacker überprüfen systematisch geschlossene Sicherheitslücken in neueren Betriebssystemen, wie Windows 7 und 8, ob sie nicht auch bei Windows XP greifen. Zu den bekannten Lücken kommen also immer wieder neue hinzu, die dann aber nicht mehr durch Security Updates abgedeckt werden.

Hinweis: Ab 8. April 2014 gibt es von Microsoft für Windows XP keinen Support mehr. Das bedeutet, es gibt auch keine Sicherheitsupdates mehr. Sicherheitslücken werden nicht mehr geschlossen. Die Systeme und die darauf liegenden Daten sind möglicherweise durch Viren, Spyware und andere Schadsoftware gefährdet.

### Beispiel für ein Sicherheitsrisiko: HTTP Request Hijacking

HTTP Request Hijacking ist eine Methode, um per Man-in-the-Middle-Angriff, einem WWW-Anwender unbemerkt eine andere Webseite unterzujubeln. Auf diese Weise wäre es denkbar, den Anwender Schadcode ausführen zu lassen oder Daten auf seinem Computer auszuspähen.  
Das Verfahren basiert auf dem HTTP-Response-Code 301 "Moved Permanently" (Dauerhaft verschoben). Mit diesem Status-Code teilt der HTTP-Server (Webserver) dem HTTP-Client (Browser) mit, wenn eine Ressource unter einer anderen URL zu finden ist. Es findet eine Art Umleitung statt, die sich darin äußert, dass der HTTP-Client die neue URL automatisch aufruft. Gegen diese Umleitung kann der Anwender nichts machen. Es sei denn, er schaltet es ab. Aber das macht eigentlich nur wenig Sinn. 301er-Weiterleitungen sind im WWW eine gängige Methode, um Inhalte verfügbar zu halten, wenn sich URLs geändert haben. Insbesondere bei aktiven Inhalten ist das der Normalfall.  
Wenn nun ein Angreifer in der Lage ist, die neue URL gegen eine andere auszutauschen, dann könnte der Angreifer die Verbindung als Man-in-the-Middle übernehmen.

### Beispiel für ein Sicherheitsrisiko: RFC 3924

Im RFC 3924 steht: "Mechanisms should be in place to limit unauthorized personnel from performing or knowing about lawfully authorized intercepts." Gemeint ist damit, dass Mechanismen in Hardware und Software versteckt sind, welche es ermöglichen eine Kommunikation direkt abzugreifen ohne das der zu Belauschende davon etwas mitbekommt.  
Erwähnen muss man dazu, dass viele Länder, auch Deutschland, eine Schnittstelle von Internet Service Providern (ISPs) fordern. Dementsprechend müssen die Hersteller von Hardware und Software das entsprechend anbieten.  
Da viele Protokolle, Mechanismen und Leistungsmerkmale in der Netzwerktechnik als RFC veröffentlicht sind, ist diese Funktion logischerweise ebenfalls in einem RFC definiert.  
Das Problem dabei ist, dass Eingeweihte diese Zugänge für eigene Zwecke missbrauchen können.

### Beispiel für ein Sicherheitsrisiko: Debugging- und Monitoring-Funktion in Switche und Router

In Routern und Switche gibt es das "monitor"-Kommando, welches so oder ähnlich lautet. Damit kann man den Traffic eines Ports auf einen anderen Port "kopieren". Dabei bleibt der Original-Traffic unverändert und wird zusätzlich an einem anderen Port ausgeleitet. Auf diese Weise kann man Datenverkehr abgreifen.  
Dieses Portmirroring ist ursprünglich eine Monitoring bzw. Debugging-Funktion, um Fehler im Netzwerkverkehr zu finden. Um den Datenverkehr nicht zu verlangsamen, wird er kopiert und parallel ausgewertet. Selbstverständlich lässt sich diese Funktion auch für Überwachungszwecke nutzen.

### Aktuell werden folgende Sicherheitslücken als besonders problematisch angesehen

- Hintertüren in Sicherheits-Standard und kommerzieller Hardware und Software.
- Kompromittierung von Zertifikaten über Provider und Zertifikatsanbieter.
- Knacken älterer Verschlüsselungen durch hohe Rechenleistung.
- Generierung von Zufallszahlen, die nicht ganz so zufällig sind.

Die aktuellen Diskussionen gehen auf den NSA-Skandal zurück, der einige akute Sicherheitsprobleme aufgedeckt hat. Das gilt nicht nur in Bezug auf Geheimdienste, sondern auch für alle anderen Angreifer. Denn die Frage ist, wer alles noch daran interessiert ist, Sicherheitslücken auszunutzen. Deshalb werden folgende Maßnahmen empfohlen.

- Kontinuierliche Weiterentwicklung im Hinblick auf Sicherheit.
- Mehr Verbindlichkeit für existierende Sicherheitsoptionen.
- Erhöhte Diversität bei der Nutzung von Internet-Diensten.
- Diversifizierung durch Stärken nationaler Infrastrukturen und Netz.
- Abbau der Abhängigkeit von Netzwerkausrüstern und Hardwareproduzenten aus den USA.
- Klare Regeln und mehr Transparenz für den Zugriff auf Daten durch staatliche Behörden.

Zu hohen Erwartungen darf man an die zukünftigen Verbesserungen nicht haben. Auf jeden Fall wird es zu einem Rüstungswettlauf kommen, bei dem mal die eine, mal die andere Seite die Oberhand gewinnen wird. Ziel muss es sein, der Massenüberwachung einen Riegel vorzuschieben. Sowohl mit technischen Maßnahmen, wie auch politisch. Tatsächliche Sicherheitslücken sollten die Ausnahme bleiben und wenn dann nur mit hohem Aufwand auszunutzen sein.  
Ziel muss es auch sein, jegliche Zugriffe zu protokollieren. Auffälligkeiten, insbesondere widerrechtliche Zugriffe, müssen erkannt und gerichtsfest dokumentiert werden.