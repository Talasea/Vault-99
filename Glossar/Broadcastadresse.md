
Eine Broadcast-Adresse ist eine spezielle IP-Adresse, die verwendet wird, um Datenpakete an alle Geräte eines lokalen Netzwerks zu senden.Diese Adresse ermöglicht es, Informationen und Dienste an alle Netzwerkteilnehmer ohne Kenntnis ihrer individuellen IP-Adressen zu übertragen.Im IPv4-Netzwerk wird die Broadcast-Adresse durch das Setzen aller Host-Bits auf den Wert „1“ definiert.Zum Beispiel ist für das Netzwerk 192.168.0.0/24 die Broadcast-Adresse 192.168.0.255.Broadcasts werden in der Regel verwendet, wenn die IP-Adresse des Empfängers unbekannt ist, wie bei ARP oder DHCP-Prozessen.



Über die Broadcast-Adresse lassen sich Datenpakete in IP-[Netzwerken](https://www.ionos.at/digitalguide/server/knowhow/was-ist-ein-netzwerk/ "Was ist ein Netzwerk?") an alle Teilnehmer eines lokalen Netzes verschicken. Die individuellen Adressen der einzelnen Netzwerkparteien müssen hierfür nicht bekannt sein. Bei Bedarf lässt sich die Broadcast-Adresse ganz einfach berechnen.

Domain kaufen

Registrieren Sie Ihre perfekte Domain

- Inklusive Wildcard-SSL-Zertifikat
- Inklusive Domain Lock
- Inklusive 2 GB E-Mail-Postfach

Prüfen

## Das steckt hinter der Broadcast-Adresse

Jedes Netz bzw. [Subnetz](https://www.ionos.at/digitalguide/server/knowhow/subnetting-wie-funktionieren-subnetze/ "Subnetting: Wie funktionieren Subnetze?") besitzt eine reservierte Broadcast-Adresse, über die alle Teilnehmer des Netzwerks einen [Broadcast](https://www.ionos.at/digitalguide/server/knowhow/broadcast/ "Broadcast") versenden können. Ein solcher ermöglicht es, Informationen und Dienste **an alle Geräte und Komponenten des Netzwerks zu übertragen**, ohne dass hierfür deren individuelle [IP-Adressen](https://www.ionos.at/digitalguide/server/knowhow/was-ist-eine-ip-adresse/ "Was ist eine IP-Adresse?") bekannt sein müssen. Unter anderem nutzen Router in einem lokalen Netzwerk die Broadcast-IP, um HELLO-Pakete an alle Endgeräte, Switches und andere Router zu versenden und so die Wechselbeziehungen im Netz aufrechtzuerhalten und benachbarte Geräte zu entdecken.

Definition Broadcast

[Broadcast](https://www.ionos.at/digitalguide/server/knowhow/broadcast/ "Broadcast"): eine Mehrpunktverbindung in IP-Netzwerken, die automatisch alle Teilnehmer des Netzwerks erreicht, ohne die Empfängeradressen zu kennen. Zu diesem Zweck existiert in jedem Netz bzw. Subnetz eine fest reservierte Broadcast-Adresse.

## Wie lässt sich die Broadcast-Adresse berechnen?

Jede IP-Adresse besteht aus 4 Dezimalzahlen – sogenannten Oktetten –, die durch Punkte getrennt sind. Ein Oktett beinhaltet 8 Bit, weshalb jede IPv4-Adresse automatisch eine 32-Bit-Adresse ist. Jedes Oktett kann eine Zahl zwischen 0 und 255 darstellen. Die Broadcast-Adresse wird immer im **abschließenden Bereich des Host-Anteils einer Adresse** (startet im dritten oder vierten Oktett) gekennzeichnet: Wenn alle Host-Bits auf den Binärwert „1“ gesetzt sind, handelt es sich um die Broadcast-Adresse.

Hinweis

Sind alle Host-Bits auf den Wert „0“ gesetzt, hat man es mit der Adresse für das entsprechende Subnetz zu tun.

Folgendes Beispiel soll die Zusammensetzung der einzelnen Bestandteile einer IP-Adresse inklusive der Berechnung der Broadcast-Adresse verdeutlichen:

```none
192.128.64.7/24
```

Copy

_192.128.64.7_ ist in diesem Fall die **IP-Adresse**, während das Suffix „/24“ die **Subnetzmaske** _255.255.255.0_ kennzeichnet.

[![Schematische Darstellung der IPv4-Adresse 192.128.64.7/24](https://www.ionos.at/digitalguide/fileadmin/_processed_/5/1/csm_schematische-darstellung-ipv4-adresse_a740c6ebb2.webp "Schematische Darstellung der IPv4-Adresse 192.128.64.7/24")](https://www.ionos.at/digitalguide/fileadmin/DigitalGuide/Schaubilder/schematische-darstellung-ipv4-adresse.png)

Am Beispiel der IPv4-Adresse 192.128.64.7/24 lassen sich Host- und Netzwerk-Anteil einer Adresse ablesen.

In jedem Netzwerk wird eine Broadcast-IP **nur einmal vergeben**. Sie ist immer **die letzte IP-Adresse** des Subnetzes. Die Broadcast-Adresse – bei der alle Host-Bits wie bereits erwähnt auf „1“ gesetzt sind – lautet in diesem Beispiel folglich: **_192.128.64.255_**.

![vuZZIqiNaak.jpg](https://de-at-digitalguide-ionos.guides.seo.server.lan/typo3temp/assets/_processed_/1/2/csm_vuZZIqiNaak_2827354eeb.jpg)Zur Anzeige dieses Videos sind Cookies von Drittanbietern erforderlich. Ihre Cookie-Einstellungen können Sie hier aufrufen und ändern.

## Broadcast-IP herausfinden: So funktioniert’s

Sie wollen die Broadcast-Adresse Ihres Netzwerks herausfinden? Hierfür bieten Ihnen gängige Betriebssystem mit nativen Kommandozeilenanwendungen und dem Netzwerkprogramm [ipconfig](https://www.ionos.at/digitalguide/server/konfiguration/ipconfig/ "ipconfig") (Windows) bzw. „ifconfig“ oder „ip“ (Linux, macOS) das passende Tool-Set.

In **Windows** gehen Sie beispielsweise folgendermaßen vor:

1. Starten Sie die Eingabeaufforderung, indem Sie die Tastenkombination **[Windows]** **+** **[R]** verwenden und den Befehl „**cmd**“ ausführen.
2. Geben Sie in das Kommandozeilen-Tool den [CMD-Befehl](https://www.ionos.at/digitalguide/server/knowhow/windows-cmd-befehle/ "Windows-CMD-Befehle") „**ipconfig /all**“ ein, um einen Überblick über alle wichtigen Eckdaten Ihres lokalen Netzwerks zu erhalten.

[![Windows-11-Eingabeaufforderung: Ausgabe für „ipconfig /all“](https://www.ionos.at/digitalguide/fileadmin/_processed_/b/d/csm_ausgabe-ipconfig-all_80ea71c138.webp "Windows-11-Eingabeaufforderung: Ausgabe für „ipconfig /all“")](https://www.ionos.at/digitalguide/fileadmin/DigitalGuide/Screenshots_2022/ausgabe-ipconfig-all.png)

Windows-11-Eingabeaufforderung: Ausgabe für „ipconfig /all“

Unter anderem präsentiert Ihnen die Eingabeaufforderung die IP-Adresse Ihres Geräts sowie die Subnetzmaske. Aus diesen Angaben können Sie die **Broadcast-IP ableiten**: In unserem Beispiel mit der IP-Adresse _192.168.2.34_ und der Subnetzmaske _255.255.255.0_ lautet die Broadcast-Adresse _192.168.2.255._

Wie genau Sie die Broadcast-Adresse in Linux und macOS herausfinden, hängt von dem verfügbaren Netzwerk-Tool der jeweiligen Distribution bzw. Version ab. In **Ubuntu 20.04** können Sie beispielsweise wie folgt vorgehen:

1. Öffnen Sie das Menü „**Anwendungen anzeigen**“.
2. Suchen Sie nach „**Terminal**“ und starten die Anwendung per Doppelklick.
3. Geben Sie das Kommando „**ifconfig**“ ein.

[![Ubuntu 20.04: Ausgabe für den Befehl „ifconfig“](https://www.ionos.at/digitalguide/fileadmin/_processed_/9/a/csm_ausgabe-fuer-den-befehl-ifconfig_95c5543577.webp "Ubuntu 20.04: Ausgabe für den Befehl „ifconfig“")](https://www.ionos.at/digitalguide/fileadmin/DigitalGuide/Screenshots_2022/ausgabe-fuer-den-befehl-ifconfig.png)

Ubuntu 20.04: Ausgabe für den Befehl „ifconfig“

Gleich **in der zweiten Zeile** präsentiert Ubuntu nach der Ausführung des Kommandos drei Werte:

- **inet**: die Internetadresse Ihres Geräts (hier: _172.18.166.193_)
- **netmask**: die Subnetzmaske des lokalen Netzwerks (hier: _255.255.250.0_)
- **broadcast**: die Broadcast-Adresse des lokalen Netzwerks (hier: _172.18.175.255_)