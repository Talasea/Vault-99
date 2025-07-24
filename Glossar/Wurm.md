### Was ist ein Computerwurm?

Der Begriff „Computerwurm“ wurde erstmals 1975 im Roman „The Shockwave Rider“ von John Brunner verwendet. In diesem Roman entwirft der Protagonist der Geschichte einen Daten sammelnden Wurm. In den frühen Tagen der Informatik waren Computerwürmer darauf ausgelegt, die Sicherheitslücken eines Systems auszunutzen. Anstatt die infizierten Computer ernsthaft zu beschädigen, vermehrten sie sich nur im Hintergrund. Heute hat sich der Zweck der Computerwürmer jedoch geändert. Sie werden heutzutage oftmals von den Angreifern benutzt, um vollständigen Zugang zu den Computern ihrer Opfer zu erhalten.

![computerwurm cover](https://www.hornetsecurity.com/app/uploads/2024/06/2020-09-28_Grafiken_Wissensdatenbank_700x350px13-jpg.webp)

Computer, die mit einem Netzwerk verbunden sind, sind anfällig für verschiedene Formen von Malware, darunter auch Computerwürmer. Bei einem Computerwurm handelt es sich um Schadsoftware, die sich selbstständig reproduziert und sich über Netzwerkverbindungen verbreitet.

Der Computerwurm infiziert dabei normalerweise keine Computerdateien, sondern einen anderen Computer im Netzwerk. Dies geschieht, in dem sich der Wurm repliziert. Diese Fähigkeit gibt der Wurm seinem Replikat weiter, wodurch auch dieser auf die gleiche Art und Weise andere Systeme infizieren kann. An der Stelle zeigt sich auch der Unterschied zwischen Computerwürmern und -viren. Computerwürmer sind eigenständige Programme, die sich selbst replizieren und im Hintergrund laufen, während Viren eine Host Datei benötigen, die sie infizieren können. Aus diesem Grund kommt es häufig vor, dass ein Computerwurm erst bemerkt wird, wenn das Programm Systemressourcen verbraucht, wodurch andere Aufgaben verlangsamt oder angehalten werden.

### Wie funktioniert ein Computerwurm?

Computerwürmer nutzen Schwachstellenin Netzwerken, um sich zu verbreiten. Der Wurm sucht also eine Hintertür, um unbemerkt in das Netzwerk einzudringen. Um Computerwürmer erstmalig in Umlauf zu bringen, versenden Hacker dazu häufig [Phishing-E-Mails](https://www.hornetsecurity.com/de/wissensdatenbank/was-ist-phishing/) oder Instant Messages mit schädlichen Anhängen. Cyberkriminelle versuchen hierbei den Wurm zu tarnen, damit der Empfänger gewillt ist, das Programm auszuführen. Hierfür werden zum Beispiel doppelte Dateiendungen genutzt und/oder ein Dateiname, der ungefährlich oder wichtig aussieht, wie z.B. „Rechnung“. Sobald der Benutzer den Anhang oder Link öffnet, lädt er die Malware (Computerwurm) sofort herunter oder wird auf eine gefährliche Webseite geleitet. Auf diese Weise findet der Wurm seinen Weg in das System des Benutzers, ohne dass dieser es bemerkt. Einmal ausgeführt sucht der Wurm einen Weg sich zu replizieren und in weitere Systeme einzudringen. Ein Weg ist hier zum Beispiel, dass der Wurm eine E-Mail an alle Kontakte des infizierten Computers schickt, in der Replikate des Wurmes enthalten sind. 

Viele Würmer tragen mittlerweile einen sogenannten Payload in sich. Payload ist übersetzt die „Nutzlast“ und in dem Fall ein Anhang, den der Wurm mit sich bringt. Der Wurm kann somit zum Beispiel [Ransomware](https://www.hornetsecurity.com/de/wissensdatenbank/ransomware/), Viren oder andere Malware in das System schleusen, die gravierende anrichten können. So können sie beispielsweise Dateien auf dem PC löschen oder bei einem Erpressungsangriff verschlüsseln. Ein Computerwurm kann zudem eine Hintertür installieren, die später von anderen Malware-Programmen ausgenutzt werden kann. Durch diese Sicherheitslücke erhält der Autor des Wurms die Kontrolle über den infizierten Computer.

Mittlerweile werden in Malware-Kampagnen oft Mischformen verschiedener Malware genutzt. So zum Beispiel bei der [WannaCry-Ransomware](https://www.hornetsecurity.com/de/wissensdatenbank/ransomware/#ransomware-beispiel) oder [Petya/Not-Petya-Ransomware](https://www.hornetsecurity.com/de/security-informationen/petya-vs-notpetya/). Diese besitzen eine Wurm Komponente, damit sich die Malware replizieren und durch Hintertüren in anderen Systemen im Netzwerk verbreiten kann. 

Da der Wurm, bzw. dessen Programmierer die Rechenleistung des infizierten Systems nutzen kann, werden diese oft zu einem Botnet zusammengeschlossen. Botnets werden dann von den Cyberkriminellen zum Beispiel für [DDoS-Angriffe](https://www.hornetsecurity.com/de/wissensdatenbank/ddos-attacke/) oder [Cyptominig](https://www.hornetsecurity.com/de/wissensdatenbank/crypto-mining/) genutzt.

### Welche Arten von Computerwürmern gibt es?

Computerwürmer lassen sich vor allem nach der Art der Verbreitung unterteilen:

#### Internet-Würmer

Hierbei handelt es sich um völlig eigenständige Programme. Sie verwenden einen infizierten Rechner, um das Internet nach anderen anfälligen Rechnern zu durchsuchen. Wird ein angreifbarer Computer gefunden, infiziert der Wurm ihn.

#### E-Mail-Würmer

Dieser Computerwurm wird am häufigsten über E-Mail-Anhänge verbreitet. Er besitzt in der Regel doppelte Dateiendungen (z.B. .mp4.exe oder .avi.exe), sodass der Empfänger denken könnte, dass es sich um Mediendateien und nicht um bösartige Computerprogramme handelt.

#### Filesharing-Würmer

Trotz der Illegalität werden Filesharing und Peer-to-Peer-Dateiübertragungen immer noch von Millionen von Menschen weltweit genutzt. Dabei setzen sie ihre Computer unwissentlich der Bedrohung durch Filesharing-Würmer aus. Wie E-Mail- und Instant-Messaging-Würmer sind diese Programme häufig als Mediendateien mit doppelter Endung getarnt.

#### Instant-Messaging-Würmer

Sie gleichen den E-Mail-Würmern, der einzige Unterschied besteht in ihrer Verbreitungsmethode. Sie sind als Anhänge oder anklickbare Links zu Webseiten getarnt. Oft wird dieser Computerwurm von kurzen Nachrichten wie „LOL“ oder „Das müssen Sie sich ansehen!“ begleitet, um dem Opfer vorzugaukeln, dass ein Freund ein lustiges Video zum Anschauen geschickt hat.

### Bekannte Computerwürmer

#### Morris Worm

Dieser Computerwurm wurde 1988 von Robert Morris auf den Weg gebracht. Er veröffentlichte einen Code, ohne zu wissen, dass dieser fehlerhaft war und den betroffenen Hosts eine Vielzahl von Problemen bereiten würde. Der Morris-Wurm führte zu Tausenden von überlasteten Computern, die unter UNIX liefen und einem finanziellen Schaden zwischen 10 Millionen und 100 Millionen Dollar.

#### Storm Worm

Der Storm Worm ist ein E-Mail-Wurm aus dem Jahr 2007. Die Opfer erhielten E-Mails mit einer falschen Nachrichtenmeldung. Diese berichtete von einer noch nie dagewesenen Sturmwelle, die bereits Hunderte von Menschen in ganz Europa getötet haben sollte. In einer Zeitspanne von 10 Jahren wurden mehr als 1,2 Milliarden E-Mails verschickt, die mit dem Storm Wurm infizierte waren. Experten gehen davon aus, dass es immer noch mindestens eine Million unwissentlich infizierte Computer gibt.

![Grafiken Wissensdatenbank](https://www.hornetsecurity.com/app/uploads/2024/06/2020-09-28_Grafiken_Wissensdatenbank_700x350px2-jpg.webp)

#### SQL Slammer Worm

Dieser Computerwurm war in seiner Verbreitungsmethode und -geschwindigkeit einzigartig. Er verbreitete sich geradezu wie eine Lauffeuer über einen ungepatchte Version von Microsoft SQL. Schon kurz nach der Verbreitung des SQL Wurms im Jahr 2003 waren mehr als 75.000 infizierte Computer unwissentlich an DDoS-Angriffen auf mehreren großen Webseiten beteiligt.

### Was unterscheidet einen Computerwurm von einem Virus?

Ein Computerwurm passt in vielerlei Hinsicht zur Beschreibung eines Computervirus. Wie ein normaler Virus kann sich ein Computerwurm selbst replizieren und sich über Netzwerke verbreiten. Aus diesem Grund werden Würmer oft auch als Viren bezeichnet, allerdings unterscheiden sie sich in einigen Aspekten voneinander.

Im Gegensatz zu Viren, die Host-Dateien benötigen, bevor sie den Computer infizieren können, existieren Würmer als separate Einheiten oder eigenständige Software. Sie können sich selbstständig replizieren und verbreiten, sobald sie das System durchbrochen haben. Sie benötigen keine Aktivierung oder menschliches Zutun, um ihren Code auszuführen und zu verbreiten. Im Vergleich dazu verbergen sich Viren oft in gemeinsam genutzten oder heruntergeladenen Dateien. Wenn die Host-Datei von einem Computer heruntergeladen wird, bleibt der Virus so lange inaktiv, bis die infizierte Datei aktiviert wird. Erst danach kann der Virus bösartige Codes ausführen und sich replizieren, um andere Dateien auf dem Rechner zu befallen.

Ein Computerwurm benötigt hingegen keine Aktivierung der Host-Datei. Sobald ein Computerwurm in das System eingedrungen ist, erstellt er mehrere Kopien von sich selbst, die sich dann über das Netzwerk oder über eine Internetverbindung verbreiten. Diese Kopien infizieren alle unzureichend geschützten Computer und Server, die sich über das Netzwerk mit dem ursprünglich befallenen Gerät verbinden. Da jede nachfolgende Kopie eines Wurms diesen Prozess der Selbstreplikation, Ausführung und Verbreitung wiederholt, können sich Computerwürmer sehr einfach und schnell über Netzwerke verbreiten.

### Wie erkennt man einen Computerwurm?

Benutzer sollten mit den Anzeichen eines Computerwurms vertraut sein, damit sie einen Befall schnell erkennen und den Computerwurm entfernen können. Typische Erkennungsmerkmale eines Computerwurms sind:

- Ungewöhnliches Verhalten des Computers (Nachrichten, Töne, Bilder)
- Programme, die automatisch geöffnet und ausgeführt werden
- Langsame Rechnerleistung
- Einfrieren und Abstürzen des Systems
- Betriebssystemfehler und Systemfehlermeldungen  
    

- E-Mails, die ohne Wissen des Benutzers an Kontakte gesendet werden
- Fehlende oder veränderte Dateien
- Firewall-Warnungen
- Ungewöhnliches Verhalten des Webbrowsers
- Auftreten seltsamer und unbeabsichtigter Desktop-Dateien und Symbole

Während auch andere Formen von Malware diese Probleme verursachen, deutet das Auftreten mehrerer dieser Anzeichen oder das wiederholte Auftreten dieser Symptome auf einen Computerwurm hin.

### Wie kann man einen Computerwurm entfernen?

Die folgenden Schritte sollten angewendet werden, um einen Computerwurm vollständig zu entfernen:

1.Zunächst sollte eine hochwertige Antiviren-Software installiert werden. Bei der Wahl der Software sollte auf seriöse Hersteller zurückgegriffen werden, da Malware oftmals mit gefälschten Antiviren-Programmen kommt.

2.Die Systemwiederherstellung deaktivieren, damit Windows keine Backups erstellt, die selbst mit dem Computerwurm infiziert sind.

3.Durchführung einer vollständigen Überprüfung des Systems mit dem Antiviren-Programm.

4.Wurden Computerwürmer gefunden, bietet die Software in der Regel an, diese zu entfernen.

5.Wenn das Antiviren-Programm den Wurm nicht automatisch entfernt, sollte mittels Suchmaschine, ein passendes Tool zum Entfernen des jeweiligen Wurms heruntergeladen und ausgeführt werden. Ebenso sollte die Antiviren-Software deaktiviert werden. Wenn sie ausgeführt wird, während der Computerwurm entfernt wird, kann sie mit den Entfernungsmethoden in Konflikt geraten und einen Systemfehler verursachen.

6.Nachdem der Wurm entfernt wurde, sollte das Antiviren-Programm wieder eingeschalten werden. Gleiches gilt für die Systemwiederherstellung.

### Wie kann man sich vor einem Computerwurm schützen?

Es gibt mehrere bewährte Verfahren, die Einzelpersonen sowie Unternehmen befolgen können, um ihre Rechner vor einem Computerwurm zu schützen. Die folgenden Schritte verringern das Infektionsrisiko und sorgen für eine leichtere Erkennung und Beseitigung von Computerwürmern:

#### Sicheres Verhalten

Anhänge und Links sollten nur dann geöffnet werden, wenn sie von einer vertrauenswürdigen und dem Nutzer bekannten Quelle stammen. E-Mails von unbekannten Absendern sollten nicht geöffnet werden, da sich viele Computerwürmer via E-Mail verbreiten. Unternehmen sollten mit ihren Mitarbeitern [Awareness-Schulungen](https://www.hornetsecurity.com/de/security-informationen/security-awareness/) durchführen, damit diese für Gefahren und Risiken im Internet sensibilisiert werden.

#### Regelmäßige Updates

Betriebssysteme und Softwares sollten mit regelmäßigen Updates auf dem neuesten Stand gehalten werden. Die Updates der Hersteller enthalten oft Sicherheits-Patches, die Computer vor neuen Würmern schützen und Fehler beheben. Dies ist wichtig, da ein Computerwurm von den Schwachstellen profitiert.

#### Antiviren-Software

Die Nutzung einer Antiviren-Software ist die erste präventive Maßnahme zur Vermeidung von Computerwürmern. Es ist ein Programm, das den Computer vor Viren, Würmern, Trojanern und Malware jeglicher Art schützt. Es scannt jede Datei auf dem Computer und hilft, Schäden vorzubeugen. Besonders wirkungsvoll sind Antiviren-Programme, die in der Lage sind, Downloads zu scannen und bereits Tools zum Entfernen der Computerwürmer beinhalten.

#### Firewall

Eine Firewall ist ein Sicherheitstool, das dazu dient, den ein- und ausgehenden Netzwerkverkehr auf der Grundlage von Sicherheitsregeln zu überwachen. Der Hauptzweck besteht darin, ein Hindernis zwischen dem internen und externen Netzwerk zu schaffen. So kann das Eindringen von Schadprogrammen in Netzwerke erschwert und minimiert werden.

#### Den E-Mail Posteingang schützen

Häufig befallen Computerwürmer den Computer via E-Mail. So können sie zum Beispiel über eine Phishing E-Mail auf den Computer gelangen. Hiervor kann man sich bereits schützen, bevor die Schadsoftware auf dem Computer ist. Dies funktioniert für Unternehmen zum Beispiel mit [Spam and Malware Protection](https://www.hornetsecurity.com/de/services/spamfilter-email-malware-protection/) oder [Advanced Threat Protection](https://www.hornetsecurity.com/de/services/schutz-vor-ransomware-advanced-threat-protection/) von Hornetsecurity.

Sie sehen gerade einen Platzhalterinhalt von **Youtube**. Um auf den eigentlichen Inhalt zuzugreifen, klicken Sie auf die Schaltfläche unten. Bitte beachten Sie, dass dabei Daten an Drittanbieter weitergegeben werden.

[Mehr Informationen](https://www.hornetsecurity.com/de/wissensdatenbank/computerwurm/#)

[Inhalt entsperren](https://www.hornetsecurity.com/de/wissensdatenbank/computerwurm/#)[Erforderlichen Service akzeptieren und Inhalte entsperren](https://www.hornetsecurity.com/de/wissensdatenbank/computerwurm/#)