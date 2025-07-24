Der Begriff „Fully Qualified Domain Name“, kurz FQDN, bezeichnet die vollständige und eindeutige Adresse einer Internetpräsenz. Er setzt sich aus dem Hostname und der Domain zusammen und wird verwendet, um spezifische Hosts im Internet zu lokalisieren und mittels Namensauflösung aufzurufen.

Der Aufbau eines FQDN ist durch das Domain-Name-System (DNS) vorgegeben. Die Namen der einzelnen Ebenen im Domain-Namensraum bezeichnet man als „Label“ und trennt sie durch einen Punkt voneinander ab. Jedes Label muss dabei aus 1 bis 63 Zeichen bestehen und der gesamte FQDN darf die Zahl von insgesamt 255 Zeichen nicht überschreiten. Es dürfen nur Ziffern und Buchstaben sowie der Bindestrich verwendet werden. Zu Beginn jedes Labels muss entweder eine Ziffer oder ein Buchstabe stehen.

Der Fully Qualified Domain Name besteht aus drei oder mehr Labels: der **Top-Level-Domain**, dem **Domain-Namen**, **optionalen [Subdomains](https://www.ionos.de/digitalguide/domains/domainverwaltung/was-ist-eine-subdomain/ "Was ist eine Subdomain?")** und dem **Hostname**. Wenn bei einem Domain-Namen nicht alle Labels angegeben sind, die für den FQDN nötig sind, spricht man von „Partially Qualified Domain Names“ (PQDN) – also teilqualifizierten Domain-Namen. Oftmals ist damit gemeint, dass nur der [Hostname](https://www.ionos.de/digitalguide/hosting/hosting-technik/hostname/ "Hostname") angegeben ist. Der Oberbegriff für den FQDN und die zugehörige IP-Adresse ist „Fully Qualified Host Name“ (FQHN).

Im Folgenden erfahren Sie, wie der Fully Qualified Domain Name konkret aufgebaut ist.

Domain kaufen

Registrieren Sie Ihre perfekte Domain

- Inklusive Wildcard-SSL-Zertifikat
- Inklusive Domain Lock
- Inklusive 2 GB E-Mail-Postfach

Prüfen

Definition: Fully Qualified Domain Name

FQDN steht für Fully Qualified Domain Name, auf Deutsch „vollständig qualifizierter Domain-Name“ (auch: „vollständiger Domain-Name“). Mit FQDN ist die absolute Internetadresse einer Internetpräsenz gemeint. „Vollständig qualifiziert“ bezieht sich auf die eindeutige Identifikation, die dadurch gewährleistet ist, dass alle Domain-Levels angegeben werden. Der FQDN enthält den Hostname und die Domain inklusive der Top-Level-Domain und lässt sich eindeutig einer IP-Adresse zuordnen.

## Aufbau des FQDN

Wollen Sie die Namenshierarchie des FQDN besser verstehen, ist es sinnvoll, den Aufbau eines FQDN von rechts nach links zu betrachten. Je weiter rechts ein Label steht, desto höher liegt es im Baumdiagramm zur Darstellung der Hierarchie. **Auf der höchsten Hierarchieebene befindet sich das Root-Label, auch Null-Label genannt, also die „Wurzel“ des DNS-Systems**. Sie besteht aus einem leeren Bereich und wird deshalb nur durch einen Punkt ausgedrückt. In heutigen Browsern ist es allerdings nicht mehr nötig, den Punkt einzugeben, da er vom Browser selbst hinzugefügt wird.

Auf der darunterliegenden Hierarchieebene befindet sich die **Top-Level-Domain**, beispielsweise „de“, „com“ oder „net“. Damit der Nameserver die Adresse auflösen kann, wird das Verzeichnis der angegebenen TLD durchsucht, um dort die **Domain** auf der darunterliegenden Hierarchieebene zu finden. Wurde diese identifiziert, dann wird der Host, dessen **Hostname** im untersten Label steht, kontaktiert, um die angegebene Seite aufzurufen.

[![Aufbau des FQDN](https://www.ionos.de/digitalguide/fileadmin/_processed_/8/9/csm_fqdn-aufbau_0db8a82657.webp "Aufbau des FQDN")](https://www.ionos.de/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/fqdn-aufbau.png)

Schematische Darstellung des Aufbaus von Fully Qualified Domain Names.

## Beispiel für einen FQDN

Das folgende Beispiel verdeutlicht den Aufbau eines Fully Qualified Domain Name:

**www.ionos.de.**

[Hostname].[Domain].[TLD].[Root]

Im Verzeichnis eines Nameservers wird der Punkt ganz rechts im FQDN stets mitaufgeführt.

Das Root-Label hinter dem Punkt bleibt leer. Die Top-Level-Domain ist in unserem Beispiel die [länderspezifische Top-Level-Domain](https://www.ionos.de/digitalguide/domains/domainendungen/cctlds-laenderspezifische-top-level-domain-liste/ "ccTLDs: Länderspezifische Top-Level-Domain-Liste") „.de“. Länderspezifische TLDs fasst man auch unter der Abkürzung **ccTLD** für „country code top-level domain“ zusammen. Anders als generische TLDs wie .com oder .org, die man als **gTLD** (für „[generic top-level domain](https://www.ionos.de/digitalguide/domains/domainendungen/was-ist-eine-generische-top-level-domain-gtld/ "Was ist eine generische Top-Level-Domain (gTLD)?")“) bezeichnet. Nach der Top-Level-Domain folgt der Domain-Name, den man auch Second-Level-Label oder Second-Level-Domain nennt. In unserem Beispiel lautet er „IONOS“. Ganz links haben wir den [Hostname](https://www.ionos.de/digitalguide/hosting/hosting-technik/hostname/ "Hostname") als Third-Level-Label: In unserem Beispiel lautet er „hosting“.

Zwischen der Second-Level-Domain und dem Hostname kann man weitere Labels für **Subdomains** einfügen, die Unterbereiche der Domain bezeichnen und Third-Level-Domains, Fourth-Level-Domains und so weiter genannt werden. Ihre Anzahl wird lediglich durch die maximal zulässige Gesamtlänge des FQDN von 255 Zeichen begrenzt. Ein Beispiel: In der fiktiven FQDN **hosting.example.IONOS.de** wäre „example“ eine Subdomain von „IONOS.de“ und „hosting“ wäre wieder der Hostname.

Domain kaufen

Registrieren Sie Ihre perfekte Domain

- Inklusive Wildcard-SSL-Zertifikat
- Inklusive Domain Lock
- Inklusive 2 GB E-Mail-Postfach

Jetzt prüfen

## In Windows den FQDN herausfinden

In Windows finden Sie den FQDN Ihres Computers unter der Bezeichnung „Vollständiger Computername“. Um ihn in Windows 10 zu ermitteln, geben Sie in das Windows-Suchfeld einfach den Begriff „Systemsteuerung“ ein. Klicken Sie dort auf „System und Sicherheit“ und anschließend auf „System“. Im vorletzten Abschnitt dieser Seite finden Sie den vollständigen Computernamen Ihres Geräts, der sich aus dem ebenfalls dort angegebenen Computernamen (Hostname) und der Domain zusammensetzt. Ist der Rechner nicht mit einer Domain verbunden, wird Ihnen allerdings nur der lokale Hostname angezeigt. Unter Windows 7 gelangen Sie zu dieser Anzeige, indem Sie im Startmenü mit der rechten Maustaste auf „Computer“ klicken und dann „Eigenschaften“ auswählen.

[![Anzeige des FQDN in der Windows-Systemsteuerung](https://www.ionos.de/digitalguide/fileadmin/_processed_/7/a/csm_fqdn-anzeigen-windows-systemsteuerung_83a24aa48d.webp "Anzeige des FQDN in der Windows-Systemsteuerung")](https://www.ionos.de/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/fqdn-anzeigen-windows-systemsteuerung.jpg)

Der FQDN wird in der Systemsteuerung von Windows als „Vollständiger Computername“ angezeigt.

Sie können sich den **FQDN in Windows auch über die Kommandozeile anzeigen** lassen. Dazu geben Sie die folgende Zeile ein und drücken die Eingabetaste:

```none
echo %COMPUTERNAME%.%USERDNSDOMAIN%
```

Copy

Daraufhin bekommen Sie Ihren FQDN angezeigt. Wenn Ihr Computer nicht mit einer Domain verbunden ist, wird Ihnen hinter dem Computernamen nur die unveränderte Variable „%USERDNSDOMAIN%“ angezeigt.

[![FQDN in der Windows-Kommandozeile anzeigen](https://www.ionos.de/digitalguide/fileadmin/_processed_/3/0/csm_fqdn-anzeigen-windows-kommandozeile_93ac8c7c78.webp "FQDN in der Windows-Kommandozeile anzeigen")](https://www.ionos.de/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/fqdn-anzeigen-windows-kommandozeile.jpg)

Ausgabe des FQDN in Windows mit der Kommandozeile

## In macOS den FQDN herausfinden

Vorausgesetzt, dass Ihr Computer mit einer Domain verbunden ist, bekommen Sie den FQDN Ihres macOS-Geräts angezeigt, wenn Sie im Terminal die folgende Zeile eingeben und per Eingabetaste bestätigen:

```none
hostname -f
```

Copy

## In Linux den FQDN herausfinden

Unter **Linux** geben Sie im Terminal ebenfalls den bereits unter macOS genannten Befehl ein:

```none
hostname -f
```

Copy

Alternativ können Sie auch folgenden Befehl nutzen:

```none
hostname --fqdn
```

Copy

Nach dem Drücken der Eingabetaste wird Ihnen dann der **FQDN** ausgegeben. Falls Sie nicht mit einer Domain verbunden sind, wird Ihnen lediglich der Hostname angezeigt.

[![Linux: Anzeige des FQDN im Terminal](https://www.ionos.de/digitalguide/fileadmin/_processed_/e/c/csm_fqdn-anzeigen-linux-terminal_b06c9d66c3.webp "Linux: Anzeige des FQDN im Terminal")](https://www.ionos.de/digitalguide/fileadmin/DigitalGuide/Screenshots_2018/fqdn-anzeigen-linux-terminal.jpg)

Linux: Mit diesen Befehlen wird der FQDN im Terminal angezeigt.