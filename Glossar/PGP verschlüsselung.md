# Was ist PGP-Verschlüsselung und wie funktioniert sie?

PGP ist eine Verschlüsselungsmethode, die Sicherheit und Datenschutz für Online-Kommunikation bietet. Wir erläutern, wie PGP-Verschlüsselung funktioniert und wie Sie sie nutzen können.


![](https://www.varonis.com/hubfs/Imported_Blog_Media/how-does-pgp-encryption-work.png)

Contents

- [Wie funktioniert PGP-Verschlüsselung?](https://www.varonis.com/de/blog/pgp-encryption#wie-funktioniert-pgp-verschlsselung)
- [Anwendungsfälle von PGP-Verschlüsselung](https://www.varonis.com/de/blog/pgp-encryption#anwendungsflle-von-pgp-verschlsselung)
- [Brauche ich PGP-Verschlüsselung?](https://www.varonis.com/de/blog/pgp-encryption#brauche-ich-pgp-verschlsselung)
- [Wie richte ich die PGP-Verschlüsselung ein?](https://www.varonis.com/de/blog/pgp-encryption#wie-richte-ich-die-pgp-verschlsselung-ein)
- [Verschiedene PGP-Lösungen](https://www.varonis.com/de/blog/pgp-encryption#verschiedene-pgp-lsungen)
- [FAQ zu Pretty Good Privacy](https://www.varonis.com/de/blog/pgp-encryption#faq-zu-pretty-good-privacy)

Pretty Good Privacy (PGP) ist ein Verschlüsselungssystem, das sowohl zum Senden verschlüsselter E-Mails als auch zum Verschlüsseln vertraulicher Dateien verwendet wird. Seit seiner Erfindung im Jahr 1991 hat sich PGP zum De-facto-Standard für E-Mail-Sicherheit entwickelt.

PGP ist vor allem aus zwei Gründen so beliebt: Erstens war das System ursprünglich als Freeware erhältlich und verbreitete sich daher schnell unter Benutzern, die eine zusätzliche Sicherheitsebene für ihre E-Mails wollten. Zweitens verwendet PGP sowohl symmetrische Verschlüsselung als auch Verschlüsselung mit einem öffentlichen Schlüssel. Daher können Benutzer, die sich noch nie begegnet sind, einander verschlüsselte Nachrichten verschicken, ohne private Schlüssel auszutauschen.

### Holen Sie sich unser kostenlose eBook  
„Pen-Tests in Active Directory-Umgebungen“

Wenn Sie Ihren E-Mail-Verkehr sicherer gestalten möchten, ist PGP eine relativ einfache und kostengünstige Möglichkeit. In diesem Leitfaden zeigen wir Ihnen, wie das geht.

- [Anwendungsfälle von PGP-Verschlüsselung](https://www.varonis.com/de/blog/pgp-encryption#uses)
- [Pro und Kontra](https://www.varonis.com/de/blog/pgp-encryption#pros-cons)
- [PGP-Lösungen](https://www.varonis.com/de/blog/pgp-encryption#solutions)
- [FAQ ZU PGP](https://www.varonis.com/de/blog/pgp-encryption#faq)

## Wie funktioniert PGP-Verschlüsselung?

PGP hat einige Funktionen mit anderen Verschlüsselungssystemen gemeinsam, von denen Sie vielleicht schon gehört haben. Das sind beispielsweise die [Kerberos-Verschlüsselung](https://www.varonis.com/blog/kerberos-authentication-explained/?hsLang=de) (die zur Authentifizierung von Netzwerkbenutzern verwendet wird) und die [SSL-Verschlüsselung](https://www.thesslstore.com/blog/understanding-the-encryption-technology-behind-ssl/) (die zur Sicherung von Websites verwendet wird).

Grundsätzlich wird bei der PGP-Verschlüsselung eine Kombination aus zwei Verschlüsselungsformen verwendet: Symmetrische Verschlüsselung und Verschlüsselung mit einem öffentlichen Schlüssel.

Das folgende Diagramm kann die Funktionsweise von PGP gut veranschaulichen:

![Die Mathematik hinter der Verschlüsselung ist relativ komplex.](https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/how-does-pgp-encryption-work.png?width=1240&height=1200&name=how-does-pgp-encryption-work.png)

Der mathematische Unterbau dieser Verschlüsselungsmethoden ist relativ komplex (einen Einblick dazu erhalten Sie [hier](https://hackernoon.com/public-key-cryptography-simply-explained-e932e3093046), wenn Sie möchten). Deshalb beschränken wir uns hier auf die grundlegenden Konzepte. Auf der höchsten Ebene funktioniert die PGP-Verschlüsselung folgendermaßen:

- Zunächst erzeugt PGP einen zufälligen Sitzungsschlüssel mit einem seiner zwei (Haupt-)Algorithmen. Dieser Schlüssel ist eine große Zahl, die nicht erraten werden kann und nur einmal verwendet wird.
- Als Nächstes wird dieser Sitzungsschlüssel verschlüsselt. Das geschieht unter Verwendung des öffentlichen Schlüssels des Empfängers der Nachricht. Der öffentliche Schlüssel ist an die Identität einer bestimmten Person gebunden, und jeder kann ihn verwenden, um ihr eine Nachricht zu senden.
- Der Absender sendet seinen verschlüsselten PGP-Sitzungsschlüssel an den Empfänger und dieser kann ihn mit seinem privaten Schlüssel entschlüsseln. Mit diesem Sitzungsschlüssel kann der Empfänger nun die eigentliche Nachricht entschlüsseln.

Diese Vorgehensweise mag erst einmal seltsam wirken. Warum sollten wir den Verschlüsselungscode selbst verschlüsseln?

Nun, die Antwort ist ziemlich einfach. Die Kryptographie mit öffentlichen Schlüsseln ist viel langsamer als die symmetrische Verschlüsselung (bei der Absender und Empfänger denselben Schlüssel verwenden). Die Verwendung der symmetrischen Verschlüsselung erfordert jedoch, dass der Absender dem Empfänger den Schlüssel im Klartext mitteilt, was wiederum unsicher wäre. Durch die Verschlüsselung des symmetrischen Schlüssels mit dem (asymmetrischen) öffentlichen Schlüsselsystem kombiniert PGP die Effizienz der symmetrischen Verschlüsselung mit der Sicherheit von öffentlichen Schlüsseln.

### Ein Beispiel der PGP-Verschlüsselung in Aktion

In der Praxis ist das Versenden einer mit PGP verschlüsselten Nachricht einfacher, als man nach der obigen Erklärung meinen könnte. Schauen wir uns zum Beispiel [ProtonMail](https://protonmail.com/support/knowledge-base/how-to-use-pgp/) an.

ProtonMail unterstützt nativ PGP. Man muss lediglich auf „Mail signieren“ gehen, um seine E-Mails zu verschlüsseln. Dann wird ein Vorhängeschloss-Symbol in der Betreffzeile der E-Mails angezeigt. Die E-Mail sieht so aus (die E-Mail-Adressen wurden aus Datenschutzgründen verwischt):

[![PGP-Dateien senden, Screenshot von Windows-E-Mail](https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/sending-pgp-files-1.png?width=1240&height=800&name=sending-pgp-files-1.png)](https://info.varonis.com/hubfs/Imported_Blog_Media/sending-pgp-files-1.png?hsLang=de)

ProtonMail blendet die komplexen Vorgänge der Ver- und Entschlüsselung der Nachricht aus (wie die meisten E-Mail-Clients mit PGP). Wenn Sie mit Benutzern außerhalb von ProtonMail kommunizieren, müssen Sie ihnen zuerst Ihren öffentlichen Schlüssel senden.

[![PGP-Dateien empfangen, Screenshot von Windows-E-Mail](https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/receiving-pgp-files-1.png?width=1240&height=800&name=receiving-pgp-files-1.png)](https://info.varonis.com/hubfs/Imported_Blog_Media/receiving-pgp-files-1.png?hsLang=de)

Obwohl die Nachricht sicher versendet wurde, muss sich der Empfänger keine Gedanken darüber machen, wie das erfolgt.

## Anwendungsfälle von PGP-Verschlüsselung

![Es gibt im Wesentlichen drei Hauptverwendungszwecke für PGP](https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/pgp-encryption-uses.png?width=1240&height=780&name=pgp-encryption-uses.png)

Es gibt im Wesentlichen drei Hauptverwendungszwecke für PGP:

- Versenden und Empfangen von verschlüsselten E-Mails
- Überprüfung der Identität der Person, die Ihnen eine E-Mail gesendet hat
- Verschlüsselung von Dateien, die auf Ihren Geräten oder in der Cloud gespeichert sind

Von diesen drei Anwendungsfällen ist der erste – sicherer E-Mail-Verkehr – bei weitem der häufigste. Aber lassen Sie uns kurz einen Blick auf alle drei werfen.

### E-Mails verschlüsseln

Wie im obigen Beispiel verwenden die meisten Menschen PGP, um verschlüsselte E-Mails zu versenden. In den Anfangsjahren von PGP wurde es hauptsächlich von Aktivisten, Journalisten und anderen Personen verwendet, die mit vertraulichen Informationen arbeiten. Das PGP-System wurde ursprünglich sogar von einem Friedens- und Politikaktivisten namens Phil Zimmermann entwickelt, der seit Kurzem bei Startpage arbeitet, einer der beliebtesten privaten Suchmaschinen.

Heutzutage hat die Popularität von PGP deutlich zugenommen. Da die Benutzer zunehmend erkennen, wie viele Daten Unternehmen und Regierungen über sie sammeln, nutzen immer mehr Menschen jetzt diesen Standard, um ihre privaten Informationen auch privat zu halten.

### Überprüfung digitaler Signaturen

Ein ähnlicher Anwendungsfall von PGP ist die [E-Mail-Verifizierung](https://blog.sendinblue.com/why-you-need-email-verification/). Ist sich ein Journalist beispielsweise nicht sicher über die Identität einer Person, die ihm eine Nachricht schickt, kann er zusammen mit PGP auch eine digitale Signatur verwenden, um dies zu überprüfen.

Digitale Signaturen verwenden einen Algorithmus, der den Schlüssel des Absenders mit den gesendeten Daten kombiniert. So entsteht eine „Hash-Funktion“ – ein weiterer Algorithmus, der eine Nachricht in einen Datenblock mit fester Größe umwandeln kann. Dieser Hash wird dann mit dem privaten Schlüssel des Absenders verschlüsselt.

Der Empfänger der Nachricht kann diese Daten dann mit dem öffentlichen Schlüssel des Absenders entschlüsseln. Wenn auch nur ein Zeichen der Nachricht während der Übertragung verändert wurde, kann der Empfänger das sehen. Das kann beispielsweise darauf hindeuten, dass der Absender nicht die Person ist, für die er sich ausgibt, dass er versucht hat, eine digitale Signatur zu fälschen, oder dass die Nachricht manipuliert wurde.

### Verschlüsselung von Dateien

Eine dritte Anwendung von PGP ist die Verschlüsselung von Dateien. Da der von PGP verwendete Algorithmus – in der Regel der [RSA-Algorithmus](https://searchsecurity.techtarget.com/definition/RSA) – im Grunde „unknackbar“ ist, ist PGP eine extrem sichere Methode, um Dateien im Ruhezustand zu verschlüsseln. Insbesondere dann, wenn sie zusammen mit einer [Lösung zur Bedrohungserkennung und -bekämpfung](https://www.varonis.com/products/datalert/?hsLang=de) verwendet wird. Tatsächlich ist dieser Algorithmus so sicher, dass er sogar in fortschrittlicher Malware wie [der CryptoLocker-Malware](https://www.varonis.com/blog/cryptolocker/?hsLang=de) verwendet wird.

Im Jahr 2010 hat Symantec die PGP Corp. übernommen, der die Rechte am PGP-System gehörten. Seitdem hat sich Symantec mit Produkten wie Symantec Encryption Desktop und Symantec Encryption Desktop Storage zum führenden Anbieter von PGP-Dateiverschlüsselungssoftware entwickelt. Diese Software bietet PGP-Verschlüsselung für alle Ihre Dateien und blendet gleichzeitig die Komplexität der Ver- und Entschlüsselungsprozesse aus.

Live-Session am 4. Februar  
**Datensicherheit in der Cloud:**  
**AWS Best Practices**

[Mehr erfahren](https://info.varonis.com/de/webinar/cloud-data-security-aws-best-practices-2025-02-04/?utm_medium=display&utm_source=blog&utm_campaign=blog_post-emea_dach-active_directory&hsLang=de)

![CloudSecurity_White](https://www.varonis.com/hubfs/2024%20Website%20Redesign/02_Icon%20Library/Brand%20Icons/Light/SVGs/CloudSecurity_White.svg)

## Brauche ich PGP-Verschlüsselung?

![Ob Sie PGP-Verschlüsselung benötigen, hängt davon ab, wie sicher Ihre Kommunikation sein soll](https://www.varonis.com/hs-fs/hubfs/Imported_Blog_Media/pgp-encryption-pros-cons.png?width=1240&height=500&name=pgp-encryption-pros-cons.png)

Ob Sie PGP-Verschlüsselung benötigen, hängt davon ab, wie sicher Ihre Kommunikation (oder Ihre Dateien) sein soll(en). Wie jede Datenschutz- oder Sicherheitssoftware erfordert auch PGP ein wenig mehr Arbeit beim Senden und Empfangen von Nachrichten, kann aber auch die Resilienz Ihres Systems im Angriffsfall erheblich verbessern.

Schauen wir uns das einmal genauer an.

### Vorteile der PGP-Verschlüsselung

Der größte Vorteil der PGP-Verschlüsselung ist, dass sie im Grunde unknackbar ist. Daher wird sie immer noch von Journalisten und Aktivisten verwendet und gilt allgemein als die beste Methode zur [Verbesserung der Cloud-Sicherheit](https://www.infoq.com/articles/improving-cloud-security). Kurz gefasst: es kann im Grunde niemand – ob Hacker oder [oder sogar die NSA](https://twitter.com/Snowden/status/878686842631139334?s=20) – die PGP-Verschlüsselung knacken.

Obwohl es einige Nachrichtenmeldungen gab, die auf Sicherheitslücken in bestimmten Implementierungen von PGP hinwiesen, z. B. [die Efail-Schwachstelle](https://www.wired.com/story/efail-encrypted-email-flaw-pgp-smime/), muss man doch festhalten, dass PGP selbst immer noch sehr sicher ist.

### Vorteile der PGP-Verschlüsselung

Der größte Nachteil von PGP besteht darin, dass es nicht besonders benutzerfreundlich ist. Das ändert sich – dank der Standardlösungen, auf die wir gleich noch zu sprechen kommen werden. Dennoch kann die Verwendung von PGP zu einem erheblichen Mehraufwand an Arbeit und Zeit in Ihrem Tagesablauf führen. Darüber hinaus müssen die Benutzer des Systems wissen, wie es funktioniert, damit keine Sicherheitslücken durch unsachgemäße Verwendung entstehen. Daher müssen Unternehmen bei einer Umstellung auf PGP auch Schulungen anbieten.

Aus diesem Grund kommen für viele Unternehmen auch andere Alternativen in Frage. Es gibt beispielsweise verschlüsselte Messaging-Apps wie Signal, die benutzerfreundlichere Kryptographie bieten. Was die Speicherung von Daten betrifft, so kann die [Anonymisierung eine gute Alternative](https://www.varonis.com/blog/eu-gdpr-spotlight-pseudonymization-as-an-alternative-to-encryption/?hsLang=de) zur Verschlüsselung sein und eine effizientere Ressourcennutzung ermöglichen.

Schließlich sollten Sie wissen, dass PGP Ihre Nachrichten zwar verschlüsselt, Sie aber nicht anonym macht. Im Gegensatz zu [anonymen Browsern](https://www.varonis.com/blog/browsing-anonymously/?hsLang=de), die [Proxy-Server](https://www.varonis.com/de/blog/pgp-encryption#) oder einen VPN verwenden, um Ihren wahren Standort zu verbergen, können über PGP gesendete E-Mails zu einem Absender und Empfänger zurückverfolgt werden. Auch die Betreffzeilen sind nicht verschlüsselt, daher sollten Sie dort keine sensiblen Informationen angeben.

## Wie richte ich die PGP-Verschlüsselung ein?

In den allermeisten Fällen müssen Sie für die Einrichtung der PGP-Verschlüsselung ein Add-on für Ihr E-Mail-Programm herunterladen und dann die Installationsanweisungen befolgen. Solche Add-ons gibt es für Thunderbird, Outlook und Apple Mail. Im Folgenden werden sie beschrieben. In den letzten Jahren sind auch eine Reihe von Online-E-Mail-Systemen entstanden, die standardmäßig PGP verwenden (am bekanntesten ist ProtonMail).

Für diejenigen, die ihre Dateien mit PGP verschlüsseln möchten, gibt es eine Reihe umfangreicher Softwarelösungen. Symantec bietet beispielsweise PGP-basierte Produkte wie Symantec File Share Encryption für die Verschlüsselung von Dateien, die über ein Netzwerk geteilt werden. Außerdem gibt es Symantec Endpoint Encryption für die vollständige Festplattenverschlüsselung auf Desktop-PCs, mobilen Geräten und Wechseldatenträgern.

### PGP-Verschlüsselungssoftware

Wenn Sie PGP-Verschlüsselung verwenden möchten, müssen Sie in der Regel eine Software herunterladen, die den Ver- und Entschlüsselungsprozess automatisiert. Dafür gibt es eine Reihe von Produkten. Sie sollten jedoch wissen, worauf Sie achten müssen.

### Auswahl der PGP-Software

- Der Hauptgrund für PGP ist die Gewährleistung der Sicherheit Ihrer Korrespondenz. Bei der Suche nach PGP-Software sollte Sicherheit daher höchste Priorität haben. Obwohl PGP an sich unknackbar ist, hat es bereits Fälle gegeben, in denen bestimmte Implementierungen kompromittiert wurden. Sofern Sie kein erfahrener Entwickler sind, ist es praktisch unmöglich, diese Schwachstellen zu erkennen. Die beste Lösung ist daher, die Software jeweils auf bereits bekannte Schwachstellen zu überprüfen.
- Darüber hinaus hängt die Wahl der PGP-Software von Ihren persönlichen (oder geschäftlichen) Anforderungen ab. Es ist z. B. unwahrscheinlich, dass Sie jede von Ihnen gesendete E-Mail verschlüsseln müssen. Deshalb ist es vielleicht übertrieben, ein Add-on für Ihren gewöhnlichen E-Mail-Client herunterzuladen. Nutzen Sie stattdessen einen Online-PGP-Dienst, um wichtige E-Mails zu versenden.
- Schließlich sollten Sie sich für einen Softwareanbieter entscheiden, der eigenen Support anbietet – entweder durch ein Kundensupportteam oder durch die Benutzer-Community. PGP zu lernen ist oftmals frustrierend, wenn Sie sich zum ersten Mal im System zurechtfinden müssen. Irgendwo in dieser Phase werden Sie wahrscheinlich Unterstützung benötigen.

## Verschiedene PGP-Lösungen

Je nachdem, wozu Sie PGP verwenden und wie oft Sie es benutzen müssen, gibt es verschiedene Möglichkeiten zur Einrichtung. In diesem Abschnitt konzentrieren wir uns darauf, was die meisten Benutzer von PGP wollen: sichere E-Mails. Die verschlüsselte Datenspeicherung lassen wir hier außen vor, da das ein komplexeres Thema ist. Hier sind also fünf Lösungen für die Implementierung von PGP in Ihrem Heim- oder Geschäftsnetzwerk.

### 1. Outlook mit gpg4o

[Gpg4o](https://www.openpgp.org/software/gpg4o/) ist eine der beliebtesten PGP-Lösungen für Windows-Nutzer und ist auf die nahtlose Integration in Outlook 2010 – 2016 ausgelegt.

- Vorteile: Gpg4o bietet eine einfache Bedienung für E-Mails und ist gut in Outlook integriert. Für die meisten Windows-Benutzer ist es das einfachste und benutzerfreundlichste PGP-Add-on.
- Nachteile: Obwohl Gpg4o auf dem [OpenPGP](https://www.openpgp.org/)-Standard basiert – Open Source und frei überprüfbar –, ist das Add-on selbst proprietär. Darüber hinaus ist eine Unternehmenslizenz für das Add-on mit 56,36 € relativ teuer. Für diesen Preis erhält man jedoch auch einen eigenen Support.

### 2. Apple Mail mit GPGTools

Die Standardimplementierung der PGP-Verschlüsselung für Mac-Benutzer ist [GPGTools](https://www.openpgp.org/software/gpgtools/), eine Software-Suite zur Verschlüsselung aller Bereiche des Mac-Systems.

- Vorteile: GPGTools lässt sich gut mit Apple Mail integrieren, wie im obigen Beispiel. Außerdem bietet es einen Schlüsselmanager – eine Software, mit der Sie PGP in fast jeder Anwendung verwenden können – und ein Tool, mit dem Sie die Befehlszeile für die gängigsten Schlüsselmanagement-Aufgaben nutzen können.
- Nachteile: Obwohl GPGTools die einfachste PGP-Verschlüsselung für Mac-Benutzer bietet, kann durch die Verwendung für Ihr primäres E-Mail-Programm die Leistung von Apple Mail beeinträchtigt werden.

### 3. Thunderbird mit Enigmail

Wie bei den oben genannten Tools wurde auch [Enigmail](https://www.openpgp.org/software/enigmail/) für die Integration in einen bestimmten E-Mail-Client entwickelt, in diesem Fall Thunderbird.

- Vorteile: Enigmail bietet ein paar entscheidende Vorteile. Erstens ist das Add-on, wie auch Thunderbird selbst, plattformunabhängig. Zweitens ist das Add-on komplett Open Source und ist kostenlos erhältlich. Es wird auch regelmäßig aktualisiert und das Entwicklerteam reagiert schnell auf bekannte Malware.
- Nachteile: Wie bei den meisten Open-Source-Programmen gibt es auch bei Enigmail keinen eigenen Support. Andererseits ist die Benutzer-Community groß und aktiv und hat eine große Menge an Referenzmaterial zusammengestellt, das einem den Einstieg erleichtert.

### 4. ProtonMail

[ProtonMail](https://protonmail.com/) war einer der ersten Anbieter für sichere E-Mails und bleibt auch weiterhin einer der beliebtesten. Im Gegensatz zu den oben genannten Lösungen funktioniert ProtonMail über ein Web-Portal. Es lässt sich daher ganz einfach von Ihrem Alltagspostfach trennen.

- Vorteile: ProtonMail verwendet automatisch PGP-Verschlüsselung für Nachrichten, die zwischen zwei Nutzern des Dienstes gesendet werden, was die Einrichtung und Verwendung von PGP enorm vereinfacht. Solche Dienste – [Hushmail](https://www.hushmail.com/) und [Mailfence](https://www.mailfence.com/) funktionieren ähnlich – bieten eine einfache Möglichkeit, gelegentlich verschlüsselte E-Mails zu senden, ohne sein gesamtes System umzukrempeln.
- Nachteile: Da ProtonMail PGP über JavaScript implementiert, das in eine Website eingebettet ist, gilt es in [gewissen Kreisen](https://tonyarcieri.com/whats-wrong-with-webcrypto) als nicht absolut sicher. Dennoch nimmt ProtonMail die Sicherheit seines Systems sehr ernst und beteiligt sich äußerst aktiv an seiner Optimierung.

### 5. Android und FairEmail

Schließlich gibt es noch [FairEmail](https://www.openpgp.org/software/fairemail/), das die PGP-Verschlüsselung auf Android-Smartphones erweitert. Dabei handelt es sich um eine eigenständige E-Mail-Anwendung, die kostenlos genutzt werden kann.

- Vorteile: FairEmail ist die einfachste Lösung für Benutzer, die PGP-Verschlüsselung auf ihrem Android-Smartphone verwenden möchten. Damit lassen sich bestimmte Nachrichten optional verschlüsseln, anstatt standardmäßig alle. So können Sie auswählen, was verschlüsselt werden soll.
- Nachteile: Da die Nutzung von PGP über Android noch recht selten ist, ist die Benutzer-Community von FairEmail recht klein.

## FAQ zu Pretty Good Privacy

Selbst nach dieser Erklärung haben Sie möglicherweise noch einige Fragen. Hier finden Sie die Antworten auf die am häufigsten gestellten Fragen zu PGP.

### F: Ist PGP-Verschlüsselung sicher?

A: Ja. Obwohl PGP inzwischen mehr als 20 Jahre alt ist, wurden in der grundlegenden Implementierung des Systems keine Schwachstellen gefunden. Allerdings reicht die Verschlüsselung Ihrer E-Mails nicht aus, und Sie sollten PGP immer in Kombination mit einer vollständigen Cybersicherheitssuite mit [Bedrohungserkennungssoftware](https://www.varonis.com/products/edge?hsLang=de) verwenden.

### F: Wie funktioniert PGP-Verschlüsselung?

A: PGP verwendet eine Kombination aus symmetrischer Kryptographie und Kryptographie mit öffentlichem Schlüssel. Damit können Benutzer sicher Nachrichten aneinander versenden.

### F: Was ist die beste PGP-Software?

A: Die „beste“ PGP-Software hängt von Ihren Anforderungen ab. Die meisten Menschen müssen nicht alle ihre E-Mails verschlüsseln, sodass für sie ein webbasierter PGP-E-Mail-Anbieter die beste Lösung ist. Wenn Sie jedoch häufig verschlüsselte E-Mails versenden müssen, wäre ein PGP-Add-on für Ihr Standard-E-Mail-Programm eine Überlegung wert.

### F: Benötige ich eine Verschlüsselungssoftware?

A: Es kommt darauf an. Wenn Sie Kundeninformationen speichern, lautet die Antwort „Ja“. Die Verschlüsselung Ihrer persönlichen Dateien ist keine Notwendigkeit, kann aber Ihren Schutz vor Cyberangriffen erheblich verbessern. PGP-basierte Verschlüsselungssoftware ist in der Regel mit am einfachsten zu bedienen und ein guter Einstieg in die Verschlüsselung Ihrer Dateien.

PGP-Verschlüsselung kann als leistungsstarkes Tool für den Schutz Ihrer Daten, Ihrer Privatsphäre und Ihrer Sicherheit dienen. Sie bietet eine relativ einfache und vollständig sichere Methode zum Senden von E-Mails und ermöglicht es Ihnen auch, die Identität der Personen zu überprüfen, mit denen Sie kommunizieren. Da PGP-Zusatzprogramme auch für die meisten gängigen E-Mail-Programme verfügbar sind, ist diese Form der Verschlüsselung generell einfach zu implementieren.

Dennoch ist der sichere E-Mail-Verkehr nur ein Aspekt der Cybersicherheit. Sie sollten sicherstellen, dass Sie neben PGP auch eine robuste [Datensicherheitsplattform](https://www.varonis.com/products/data-security-platform/?hsLang=de) und [Software zur Datenverlustprävention](https://www.varonis.com/blog/what-is-data-loss-prevention-dlp/?hsLang=de) verwenden. So viele Tools wie möglich zu nutzen ist der beste Schutz für Ihre Privatsphäre und Sicherheit.

### Wie soll ich vorgehen?

Im Folgenden finden Sie drei Möglichkeiten, wie Sie das Datenrisiko in Ihrem Unternehmen verringern können:

1

[Vereinbaren Sie eine Demo mit uns](https://info.varonis.com/en/demo-request?hsLang=de "https://info.varonis.com/en/demo-request"), um Varonis in Aktion zu erleben. Wir passen die Session an die Datensicherheitsanforderungen Ihres Unternehmens an und beantworten alle Fragen.

2

[Sehen Sie sich ein Beispiel unserer Datenrisikobewertung an](https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en "https://info.varonis.com/hubfs/docs/DRA-sample.pdf?hsLang=en") und erfahren Sie, welche Risiken in Ihrer Umgebung lauern könnten. [Varonis DRA](https://info.varonis.com/en/data-risk-assessment?hsLang=de "https://info.varonis.com/en/data-risk-assessment") ist völlig kostenlos und bietet einen klaren Weg zur automatischen Sanierung.

3

Folgen Sie uns auf [LinkedIn](https://www.linkedin.com/company/varonis "https://www.linkedin.com/company/varonis"), [YouTube](https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg "https://www.youtube.com/channel/UCE9xUuH4lhIUDOFR1OHlNNg")und [X (Twitter)](https://twitter.com/varonis "https://twitter.com/varonis"), um kurze Einblicke in alle Themen der Datensicherheit zu erhalten, einschließlich Data Security Posture Management (DSPM), Bedrohungserkennung, KI-Sicherheit und mehr.



# 

PGP Funktionsweise Erklärt

PGP (Pretty Good Privacy) ist ein Programm zur Verschlüsselung und Signatur von Nachrichten, insbesondere E-Mails. Es verwendet asymmetrische Verschlüsselungsmethoden mit öffentlichen und privaten Schlüsseln.235

Der Prozess der Verschlüsselung und Signatur von Nachrichten mit PGP besteht aus mehreren Schritten:

1. Erzeugung eines Schlüsselpaares: Bei der ersten Einrichtung wird ein asymmetrisches Schlüsselpaar generiert, bestehend aus einem privaten und einem öffentlichen Schlüssel.35
    
2. Veröffentlichung des öffentlichen Schlüssels: Der öffentliche Schlüssel wird an potenzielle Kommunikationspartner übermittelt oder auf einem Schlüsselserver hochgeladen.5
    
3. Verschlüsselung der Nachricht: Der Absender verwendet den öffentlichen Schlüssel des Empfängers, um eine Nachricht zu verschlüsseln. Dabei wird ein sogenannter Sitzungsschlüssel erzeugt, der für diese Kommunikationssitzung verwendet wird. Dieser Sitzungsschlüssel wird dann mit dem öffentlichen Schlüssel des Empfängers verschlüsselt.35
    
4. Signierung der Nachricht: Die Nachricht wird mit dem privaten Schlüssel des Absenders signiert, um ihre Authentizität und Integrität zu gewährleisten.5
    
5. Übertragung der verschlüsselten und signierten Nachricht: Die verschlüsselte Nachricht wird an den Empfänger übertragen.5
    
6. Entschlüsselung der Nachricht: Der Empfänger verwendet seinen privaten Schlüssel, um den Sitzungsschlüssel zu entschlüsseln, und anschließend den Sitzungsschlüssel, um die Nachricht zu entschlüsseln.35
    
7. Überprüfung der Signatur: Der Empfänger überprüft die Signatur mit dem öffentlichen Schlüssel des Absenders, um sicherzustellen, dass die Nachricht unverändert und vom angegebenen Absender stammt.5
    

Diese Schritte gewährleisten, dass die Nachricht sowohl verschlüsselt als auch signiert wird, was die Sicherheit und Authentizität der Nachricht erhöht.