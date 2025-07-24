
Durch die weltweite Vernetzung ist die Bedeutung der Computer- und Netzwerksicherheit stark gestiegen. Wo früher vereinzelt kleine Netze ohne Verbindungen nach außen für sich alleine standen, ist heute jedes noch so kleine Netzwerk mit dem Internet verbunden. So ist es möglich, dass aus allen Teilen der Welt unbekannte Personen, ob mit guter oder böser Absicht, eine Verbindung zu jedem Netzwerk herstellen können.

Die paketorientierte Protokoll-Familie TCP/IP ist speziell dafür ausgelegt, dass eine Ende-zu-Ende-Verbindung für alle am Netzwerk hängenden Hosts möglich ist. Die dabei vorherrschende dezentrale Struktur des Internets erlaubt jedoch kaum eine Kontrolle über den Weg den Datenpakete nehmen. Diese an sich vorteilhafte Eigenschaft, z. B. bei Ausfällen oder Überlastungen von Übertragungsstrecken, macht sich bei der Übertragung von Daten negativ bemerkbar.  
Grundsätzlich weiß man nie, wer die Daten, die über das unsichere Internet übertragen werden, in die Hände bekommt und was er damit machen kann. Deshalb gilt, dass Daten immer mit einem sicheren Übertragungsprotokoll geschützt sein sollten.

**Was heißt "sicheres Übertragungsprotokoll"?** Eine Verbindung kann immer dann als sicher angenommen werden, wenn die Gegenstellen einer Verbindung sich gegenseitig authentifiziert haben und die Übertragung der Daten verschlüsselt ist.

In diesem Zusammenhang steigen auch die Anforderungen an Unternehmensnetzwerke. Auf sie sollen externe Mitarbeiter von außen auf das Netzwerk zugreifen. Außendienst-Mitarbeiter, Home-Office, entfernte Filialen und WLANs sind bereits Alltag in Unternehmen. Die Mobilität verbessert die Produktivität, fordert dafür die Auseinandersetzung mit völlig neuen Sicherheitsfragen.  
Dabei stellt sich die Frage, welche Geräte werden mit welcher Applikation wo innerhalb und außerhalb des Unternehmens und wie und wann eingesetzt? Ein zentrales Problem ist dabei, dass viele mobile Geräte ursprünglich für den Privatgebrauch und nicht für Unternehmenszwecke entwickelt wurden. Das heißt, dass viele Sicherheitsverfahren in der Praxis mangels Software-Unterstützung nicht auf allen Geräten umgesetzt werden können.

Im Zuge dessen ist die Cloud-Nutzung sehr beliebt. Hier wird nicht nur der Betrieb von Anwendungen Diensten, sondern auch die Beantwortung von Sicherheitsfragen ausgelagert.


### Die 3 Pfeiler der Netzwerk-Sicherheit: Authentizität // Vertraulichkeit // Integrität   ( CIA- Triade)

Die Netzwerk-Sicherheit umfasst meist folgende drei Pfeiler: Authentizität, Vertraulichkeit und Integrität.

- Bei der **Authentizität** der Kommunikationspartner geht es darum festzustellen, ob der Kommunikationspartner auch tatsächlich der ist, für den er sich ausgibt.
- Bei der **Vertraulichkeit** einer Kommunikation geht es darum dafür zu sorgen, dass niemand Einblick in die Daten und Kommunikation erhält.
- Zur **Integrität** zählen Mechanismen und Verfahren, die die Echtheit von Daten prüfen und sicherstellen können und somit auch vor Manipulation schützen.

Vereinfacht kann man sagen, dass es bei der Netzwerk-Sicherheit immer um die Authentifizierung der Kommunikationspartner und die Verschlüsselung der Kommunikation geht. Die Integrität ist in diesen Verfahren integriert und muss deshalb nicht explizit betrachtet werden.

### Authentizität: Authentifizierung und Autorisierung

Im echten Leben weisen wir uns durch Unterschriften, Pässe und Karten aus. Im Internet fällt dies durch die räumliche Trennung weg. Auf Sicherheit zu achten bedeutet auch, niemals die Authentifizierung und Autorisierung zu vernachlässigen. Authentifizierung ist der Vorgang, bei dem eine Person oder Maschine auf ihre Identität geprüft wird. Autorisierung ist der Vorgang, bei dem ermittelt wird, was die Person oder Maschine machen darf (Berechtigung).

- [Authentifizierung im Netzwerk](https://www.elektronik-kompendium.de/sites/net/1710241.htm)
- [AAA - Authentication Authorization Accounting](https://www.elektronik-kompendium.de/sites/net/0906151.htm)
- [Passwort, Pin und Passphrase](https://www.elektronik-kompendium.de/sites/net/2009021.htm)

### Vertraulichkeit: Verschlüsselung

Übertragungen von Informationen im Klartext, womöglich Benutzername und Passwort, sind immer ein Problem. Werden die Datenpakete auf ihrer Reise zum Empfänger von einem Angreifer gesammelt, kann er diese Informationen später missbrauchen. Ganz so wie der Empfänger es auch tut. Sind die Datenpakete verschlüsselt hat es der Angreifer schwerer Rückschlüsse auf die Original-Informationen zu ziehen.  
Neben dem reinen Abhören, also einfaches Duplizieren von Informationen, besteht die Möglichkeit Datenpakete abzufangen, ihre Weiterleitung zu verhindern oder manipulierte Datenpakete zu versenden.

- [Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/1907041.htm)
- [Verschlüsselungsverfahren](https://www.elektronik-kompendium.de/sites/net/0908071.htm)

### Besondere Gefahren

Eine besondere Gefahr geht von virtuellen Gewaltakten aus. Den Brute-Force-Angriffen, die durch Überfluten der Zielstation mit Anfragen und so am Erledigen der eigentlichen Aufgaben zu hindern. Ein Ausfall von Software und Hardware wird auf diese Weise provoziert und somit die Verfügbarkeit von Anwendungen und Diensten eingeschränkt. Viele Anwendungen sind für solche Ereignisse nicht ausgelegt und in der Regel nicht geschützt.

- [DoS - Denial of Service](https://www.elektronik-kompendium.de/sites/net/1412091.htm)

### Maßnahmen für die Netzwerk-Sicherheit

Ein Netzwerk auf Basis von TCP/IP teilt sich grob gesehen in die Anwendungsschicht, die Netzwerkschicht und Übertragungsschicht. Auf allen Schichten lassen sich Maßnahmen zur Verbesserung der Sicherheit einsetzen.  
Sicherheitsverfahren auf den niederen Schichten sind meist nur in Zugangsnetzen verfügbar. Sicherheitsverfahren auf den höheren Schichten sind an die Anwendung gebunden. Fast aller dieser Maßnahmen und Verfahren sind optional.

||Schicht|Beispiele|
|---|---|---|
|7|Application Layer  <br>Anwendungsschicht|HTTPS  <br>S-MIME  <br>SSL/TLS  <br>SSH  <br>OpenVPN|
|6|
|5|
|4|Network Layer  <br>Netzwerkschicht|IPsec (AH/ESP)|
|3|
|2|Data Link Layer  <br>Übertragungsschicht|PPTP  <br>L2TP  <br>PAP/CHAP  <br>IEEE 802.1x|
|1|

### Maßnahmen auf der Übertragungsschicht (Data Link Layer)

In der Übertragungsschicht kommen meist Tunneling-Protokolle zum Einsatz, die beliebige Netzwerk-Protokolle übertragen können. Auch für die Anwendung, die eine solche Verbindung nutzt, spielt das Protokoll auf der Übertragungsschicht keine Rolle. Die hohe Flexibilität wird mit einem großen Verarbeitungsaufwand wegen mehrfacher Header erkauft.  
In WLANs und Ethernet-basierten Netzwerken ist eine nutzerbasierte oder hostbasierte Authentifizierung möglich.

### Maßnahmen auf der Netzwerkschicht (Network Layer)

Auf der Netzwerkschicht werden häufig Paketfilter (Firewall) und Masquerading (NAT) verwendet. Das eine Verfahren um den Datenverkehr einzuschränken oder zu verhindern und das andere um Hsts gezielt zu verstecken. Diese Sicherheitsverfahren sind eng mit der Netzwerkschicht verwoben und funktionieren in diesem Fall nur mit TCP/IP. Auf der Netzwerkschicht arbeitet man auch gerne mit einer Firewall.  
Welche Protokolle oder Verfahren hier verwendet werden sind für die Anwendungsschicht und die Übertragungsschicht unerheblich. Allerdings schränken sie oft die Verbindung auf der Anwendungsebene ein, weshalb es viele Umgehungsverfahren gibt.

### Maßnahmen auf der Anwendungsschicht (Application Layer)

Sicherheitsmechanismen auf der Anwendungsschicht sind direkt mit dem Dienst, einer Anwendung oder einer Sitzung gekoppelt. Sie können also nicht einfach so anderweitig genutzt werden. Das ist jedoch kein Nachteil, sondern mit einer hohen Sicherheit verbunden. Sofern Anwendungen Sicherheitsprotokolle unterstützen, sind sie bei kurzzeitigen Verbindungen das sicherste Verfahren. Meist ist eine komplizierte Konfiguration der Anwendungen nicht erforderlich. Die Gegenstellen auf beiden Seiten einigen sich vollautomatisch ohne Eingriff des Anwenders. Allerdings muss man als Anwender darauf vertrauen, dass die Verbindung sicher ist.

### Sicherheitssoftware

Sicherheitssoftware soll vor unberechtigten Zugriffen durch Schadsoftware schützen. Die meisten Angriffe und Zugriffe erfolgen über den Versuch Schadsoftware durch Unachtsamkeit des Nutzers einzuschleusen, zu installieren und zu aktivieren und somit Zugriff auf das System zu bekommen.

- Virus
- Wurm
- Trojaner
- Malware
- Rootkit
- Fakeware/Ransomware

### Virenscanner

Virenscanner sind Bestandteil einer Sicherheitssoftware, die einen Computer im laufenden Betrieb auf Viren, Würmer und Trojaner untersucht. Dabei wird neben dem Arbeitsspeicher auch die Festplatte nach verdächtigen Datenfolgen durchsucht. Zusätzlich klinken sich Virenscanner dort im Betriebssystem ein, wo Daten zwischen Massenspeicher und Arbeitsspeicher übertragen werden, um zu verhindern, dass Schadsoftware zur Ausführung kommt. Weil sich Schadsoftware im Laufe der Zeit weiterentwickelt und von einem normalen Programm teilweise nicht zu unterscheiden ist, eignen sich herkömmliche Mittel, wie der klassische Virenscanner nicht mehr, um einen Großteil der Schadsoftware zu erkennen.  
Deshalb baut moderne Sicherheitssoftware immer öfter auf Verhaltenserkennung. Also typische Aktivitäten von Schadsoftware, die von normalen Programmen und deren Nutzung abweicht.  
Dynamic Malware Detection erkennt Schädlinge an ihrem Verhalten. Das hilft bei Malware, für die es noch keine Erkennung gibt. Die Verhaltenserkennung wertet protokollierte Aktivitäten von Prozessen aus und versucht Unregelmäßigkeiten zu erkennen.

### Was bringen Desktop-Firewalls, Security-Suiten und Virenscanner?

Grundsätzlich gilt, jede Software, die Daten aus unsicheren Quellen (z. B. Internet) liest, ist als Angriffsfläche missbrauchbar. Dazu zählen von außen erreichbare Server-Dienste, aber auch Client-Software wie Browser, Mail-Clients, Messenger und so weiter.

Auch jede Software, die eigentlich die Sicherheit erhöhen soll, vergrößert die Angriffsfläche. Ungeachtet ihrer Sicherheitsfunktionen fallen auch Personal Firewalls und Virenscanner darunter. Deshalb sollte man immer abwägen, wo die Vor- und Nachteile einer Sicherheitssoftware liegen. In der Regel macht ein Virenscanner Sinn. Eine Personal Firewall ist in der Regel unnötig und gaukelt nur Sicherheit vor. Die Firewall, die zum Beispiel in Windows, macOS oder Linux enthalten ist, ist schlank, fest ins System integriert und gilt als sicherer als so manche Security-Suite.  
Das bedeutet nicht, dass sich die Firewall eines Betriebssystems nicht verbessern lässt. Im Gegenteil. In der Regel darf sich jede Applikation bei der Installation selbst in die Ausnahmeliste der Firewall eintragen. Die Applikationen sind dabei sehr freigiebig bei der Eintragung. Eine zusätzliche Personal Firewall kann die Ausnahmen deutlich einschränken. Sofern sie gut gepflegt wird, spricht nichts gegen den Einsatz einer zusätzlichen Personal Firewall.

Mit steigender Komplexität einer Software nimmt die Wahrscheinlichkeit von Fehlern zu. Ab einer gewissen Komplexität ist eine Software nicht mehr fehlerfrei. Es ist davon auszugehen, dass "jede" Software fehlerhaft ist. Eine fehlerhafte Software, die mit Daten aus unsicheren Quellen arbeitet, ist mit einer besonders großen Angriffsfläche gleichzusetzen. Und diese Angriffsfläche steigt mit der Komplexität der Software.

Für jedes Betriebssystem, egal ob Windows, Linux oder macOS, gilt:

- Jede nicht in Gebrauch befindliche Software deinstallieren.
- Jeden nicht benötigten Server-Dienst abschalten.
- Anzahl der Software-Fehler durch regelmäßige Updates reduzieren.
- Bei Software-Alternativen diejenige mit den geringsten Fehlern wählen.
- Tendenziell die weniger komplexe Lösung einsetzen.

Bis hierher ist noch keine spezielle Sicherheitssoftware erforderlich. Das bedeutet, ein hohes Maß an Sicherheit kann "jeder" schon mit einfachen Maßnahmen erreichen.

### Das Hauptproblem ist der Nutzer

Das größte Sicherheitsproblem ist immer noch der Nutzer selber. Die wichtigste Maßnahme ist die Sensibilisierung für Sicherheitsprobleme. Dadurch reduziert sich die Angriffsfläche automatisch.  
Richtig böse ist es, wenn der Nutzer die Schadsoftware meist unwissentlich selbst installiert. Zum Beispiel durch das Öffnen eines E-Mail-Anhangs. Doch Otto-Normal-Nutzer ist sehr schwer von einem sehr vorsichtigen Umgang mit fremden Dateien zu überzeugen. Deshalb ist der Sicherheitsgewinn durch einen Virenscanner höher zu bewerten, als die zusätzlich entstehende Angriffsfläche durch den Virenscanner selber.

Doch Vorsicht, ein Virenscanner ist ein Tool zum Überprüfen von Dateien auf Schadsoftware. Mehr Sicherheit bietet er nicht. Er kommt immer nur dann zum Einsatz, wenn es eigentlich schon zu spät ist. Ein Virenscanner kann im Zweifelsfall den Virenbefall nicht verhindern, wenn er den Virus nicht kennt.

### Zero Trust

Zero Trust ist ein Sicherheitskonzept, bei dem generell jedem Netzwerkverkehr, unabhängig von seiner Herkunft, misstraut wird. Teil des Konzepts ist, dass jeder Zugriff einer Zugangskontrolle und jede Verbindung einer Verschlüsselung unterliegt.

- [Zero Trust](https://www.elektronik-kompendium.de/sites/net/2512031.htm)

### Was man über Sicherheit im Netzwerk wissen muss

Alles was wir über Sicherheit im Internet wissen kann man als überholt ansehen. Man muss im Prinzip immer davon ausgehen, dass sich der Angreifer innerhalb der eigenen Organisation oder Netzwerk befindet. Die internen Sicherheitsstrukturen müssen so angelegt sein, dass der Zugang zu wichtigen Daten ständig kontrolliert wird.

Angriffe auf Sicherheitsverfahren werden immer besser. Ist man den Schwächen eines Verfahrens auf der Spur, dann dauert es nur noch wenige Jahre, bis jemand einen weiteren Trick findet oder genug Rechenleistung zum Brechen zur Verfügung steht.

- [Sicherheitsrisiken und Sicherheitslücken in der Netzwerktechnik](https://www.elektronik-kompendium.de/sites/net/1811091.htm)
- [Sicherheitskonzepte in der Informations- und Netzwerktechnik](https://www.elektronik-kompendium.de/sites/net/1901181.htm)
- [Wie sicher ist ...?](https://www.elektronik-kompendium.de/sites/net/1811271.htm)

### Übersicht: Netzwerk-Sicherheit

- [Firewall](https://www.elektronik-kompendium.de/sites/net/0803051.htm)
- [VPN - Virtual Private Network](https://www.elektronik-kompendium.de/sites/net/0512041.htm)
- [WLAN-Sicherheit](https://www.elektronik-kompendium.de/sites/net/1403011.htm)
- [Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/1907041.htm)
- [Anonymisierung](https://www.elektronik-kompendium.de/sites/net/1809161.htm)
- [Authentifizierung im Netzwerk](https://www.elektronik-kompendium.de/sites/net/1710241.htm)

### Übersicht: Verschlüsseln und signieren von E-Mails

- [Sichere E-Mail](https://www.elektronik-kompendium.de/sites/net/1810081.htm)
- [S/MIME](https://www.elektronik-kompendium.de/sites/net/1810171.htm)
- [PGP - Pretty Good Privacy (OpenPGP)](https://www.elektronik-kompendium.de/sites/net/1810181.htm)
- [Sichere E-Mail mit PGP (OpenPGP/GnuPG)](https://www.elektronik-kompendium.de/sites/net/1811051.htm)
- [STARTTLS](https://www.elektronik-kompendium.de/sites/net/1811041.htm)

### Übersicht: Verschlüsselungsverfahren

- [Symmetrische Kryptografie](https://www.elektronik-kompendium.de/sites/net/1910101.htm)
- [Asymmetrische Kryptografie](https://www.elektronik-kompendium.de/sites/net/1910111.htm)
- [Hybride Verschlüsselungsverfahren](https://www.elektronik-kompendium.de/sites/net/1910141.htm)
- [Homomorphe Verschlüsselung](https://www.elektronik-kompendium.de/sites/net/2606151.htm)