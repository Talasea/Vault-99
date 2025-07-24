

Die Einrichtung von pfSense kann in mehrere Schritte unterteilt werden. Zunächst benötigen Sie eine neu installierte pfSense-Instanz und Ihr bestehendes Heimnetzwerk. Sie haben als Gerät für den Internetanschluss entweder ein reines Modem oder einen Router (z.B. Fritzbox).

Nach der Installation öffnen Sie die Konfigurationsoberfläche durch Eingabe der IP-Adresse des pfSense-Geräts im Internetbrowser. Anmelden Sie sich mit dem Standardbenutzernamen "admin" und dem Passwort "pfsense". Nach der Anmeldung wird Sie der Einrichtungsassistent begrüßen. Es ist wichtig, einige grundlegende Einstellungen vorzunehmen, wie den Hostnamen, den Domainnamen, den Zeitserver und die Zeitzone einzutragen.

Für das WAN-Interface müssen Sie den Typ des Netzwerkaufbaus wählen. Wenn Sie einen reinen Modem haben, müssen Sie unter "Selected Type" "PPPoE" eingeben (PPPoE = Point to Point Protocol over Ethernet).

Nachdem Sie die grundlegenden Einstellungen vorgenommen haben, sollten Sie sicherstellen, dass der DHCP-Server für das LAN-Interface aktiviert ist und dass Sie den Adressbereich für die DHCP-Verteilung angegeben haben.46

Um sicherzustellen, dass Ihre pfSense erfolgreich eingerichtet ist, sollten Sie prüfen, ob Sie über einen Internetzugang verfügen und ob Sie Ihr pfSense-Gerät von einem Computer im internen Netzwerk erreichen können.

Es ist auch wichtig, das Passwort für den Web-Benutzer "admin" zu ändern, um die Sicherheit zu erhöhen.

Mit diesen Schritten ist Ihre pfSense-Instanz eingerichtet und bereit für weitere Konfigurationen und Anpassungen





# pfSense – Die erste Inbetriebnahme

**Ziel:** die Anleitung möchte kurz erklären, welche ersten Einrichtungsschritte nötig sind, um deine frisch installierte pfSense in Betrieb zu nehmen.

**Was du hast:** eine neuinstallierte pfSense. Außerdem dein bisher bestehendes privates Heimnetzwerk. Du hast als Gerät für den Internetanschluss entweder ein reines Modem oder aber vielleicht einen Router (z.B. Fritzbox).

**Was du willst:** deine pfSense ist nagelneu und wartet auf ihren Gebrauch. Du möchtest die pfSense in deinem Netzwerk integrieren.  
Dafür gibt es generell verschiedene Möglichkeiten. In dieser Anleitung gehe ich kurz auf zwei verschiedene Möglichkeiten ein.

- pfSense Betrieb hinter einem reinen Modem
- pfSense Betrieb hinter einem Router

Die ersten Schritte der Anleitung sind für beide Varianten aber gleich.

---

_**Exkurs: Netzwerkaufbau**  
Ein für sich sehr komplexes Thema, welches aber hier nur sehr kurz und schematisch abgehandelt wird.  
Die pfSense auf einem APU Board bietet dir die Möglichkeit, drei Interfaces zu nutzen:_

_

- 1 x WAN für den Anschluss an dein Modem oder Router
- 1 x LAN für den Anschluss an einen Switch, welcher dann die Geräte in deinem Heimnetz einbindet
- 1 x ein zusätzliches LAN für weitere Geräte, z.B. alle Geräte von Besucher*Innen und Gästen

Als einfaches Bild kannst du dir den Aufbau etwa so vorstellen:  
[![pfSense im Heimnetz](https://www.heimnetz.de/wp-content/uploads/Bild1-pfsense-ersteinrichtung-netzwerk-300x235.png)](https://www.heimnetz.de/wp-content/uploads/Bild1-pfsense-ersteinrichtung-netzwerk.png "pfSense im Heimnetz")  
Dabei verwaltet dein bisheriger Router weiterhin die Zugangsdaten, um eine Internetverbindung mit deinem Internetanbieter (ISP) herzustellen. Die WAN Adresse bekommt dein Router von deinem ISP zugeteilt.  
Am Router wird dann an einem der LAN Ports die pfSense angeschlossen. Dazu wird das WAN Interface der pfSense genutzt. Somit hast du hier ein erstes Netzwerk, welches mindestens deinen Router und die pfSense beinhaltet, im Bild bekommt diese Netz beispielhaft Adressen aus dem Bereich **192.168.45.0/24** (der Router dann die .1 am Ende, die pfSense die .2).

Das LAN Interface der pfSense hast du bereits direkt nach dem Installationsprozess mit einer IP Adresse versorgt. Somit hat die pfSense am LAN Interface z. B. die IP Adresse **172.18.100.1** aus dem Adressraum **172.18.100.0/24**.

_

_Alternativ kannst du den Router im Bild auch durch ein reines Modem ersetzen. Dann werden die Zugangsdaten deines ISP allerdings auf der pfSense selbst eingetragen._

Soviel kurz zum Netzwerkaufbau und den beiden wesentlichen Einsatzmöglichkeiten für die pfSense. Du solltest also im Vorfeld bereits grundlegende Ideen und Informationen zu deinem individuellen Netzwerkaufbau und der Adressierungssystematik notieren, dann wird die eigentliche Konfiguration wesentlich erleichtert.  
Beginnen wir mit der Ersteinrichtung.

Zunächst öffnest du die Anmeldeseite der Konfigurationsoberfläche durch Eingabe deiner IP-Adresse im Internetbrowserfenster. Nach der Anmeldung mit Username und Passwort (in der Ersteinstellung User = admin, Passwort = pfsense) wirst du vom Einrichtungsassistenten begrüßt.

Nicht jede Einstellung muss nun hier bereits vorgenommen werden. Wichtig sind aber die nun folgenden Angaben:

- **Hostname**: hier gibst du den Hostname deiner pfSense ein, z.B. „**pfSense**“
- **Domainname**: z.B. „**mein.netz**“
- **Zeitserver**: damit die pfSense sich die aktuell korrekte Uhrzeit holen kann, muss hier die Adresse des Zeitservers eingegeben werden sowie die Zeitzone, in der du dich befindest, also z.B. „**0.pfsense.pool.ntp.org**“ und Zeitzone „**Europe/Berlin**“
- WAN Interface: jetzt kommt es auf deinen eigenen Netzwerkaufbau an.
    - **a: pfSense am reinen Modem**: du musst hier unter „**Selected Type**“ „**PPPoE**“ eingeben (PPPoE = Point to Point Protocoll over Ethernet). Dann trägst du im Feld „PPPoE Configuration“ deine Zugangsdaten für deinen Internetanschluss so ein, wie du sie von deinem Internetanbieter bekommen hast.
    - **b: pfSense am Router**: hier wählst du stattdessen als „**Selected Type**“ **DHCP** oder besser noch **Static** aus. Durch die Auswahl von Static bekommt das WAN Interface deiner pfSense immer dieselbe statische IP Adresse zugeteilt und ist somit immer unter dieser erreichbar. Die Angaben für PPPoE entfallen an dieser Stelle, da der Router vor der pfSense die Einwahlfunktion zum ISP übernimmt.
- Zum Schluss hast du die Möglichkeit, dein **Zugangspasswort** für die pfSense zu **ändern**, was du auch unbedingt tun solltest. Wähle hier ein ausreichende komplexes und langes Passwort aus, stell sicher, dass du dich an dieses erinnerst oder es sicher aufbewahrst. Ohne dieses Passwort kommst du NICHT mehr auf deine pfSense Oberfläche!
- Jetzt ist die Einrichtung mit dem Assistenten beendet. Damit deine Angaben gültig werden, bestätigst du am Ende mit der Schaltfläche „**Reload**“. Die pfSense lädt deine Konfiguration und nutzt diese in der weiteren Folge.

Damit sind die grundlegenden ersten Einrichtungsschritte erledigt!  
Die pfSense bietet in den Grundeinstellungen bereits einen funktionierenden Internetzugang. Es sind keine weiteren Firewallregeln für Zugriffe aus dem LAN ins Internet nötig.  
Während der Installation hast du bereits für das Netzwerk am LAN Interface den DHCP Server aktiviert und den Adressbereich angegeben, aus welchem IP-Adressen nach DHCP verteilt werden dürfen. Auch das Auflösen der DNS-Anfragen erfolgt im Grundzustand bereits ohne weiteres Zutun. Hierfür nutzt die pfSense den DNS Resolver unbound, welcher alle DNS-Anfragen direkt an die root-DNS-Server weiterleitet.