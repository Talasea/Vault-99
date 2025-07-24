
## Spiderfoot – Die Spinne im Netz der Daten

Auch wenn man bei einer offensiven Sicherheitsfirma, wie wir es sind, oftmals an den Angriff selbst denkt, also das Eindringen ins Netzwerk und das Hangeln und Springen über verschiedene Accounts, Computer und Server. Aber um solche Angriffe realistisch durchzuführen, sammeln unsere Analysten erstmal viele öffentlich verfügbare Daten aus dem Internet. Über diesen Prozess haben wir in den folgenden Artikeln schon ausführlich berichtet:

[Open Source Intelli](https://www.nsideattacklogic.de/open-source-intelligence-osint-im-red-teaming-bessere-taktische-erkenntnisse-fuer-mehr-sicherheit/)[g](https://www.nsideattacklogic.de/open-source-intelligence-osint-im-red-teaming-bessere-taktische-erkenntnisse-fuer-mehr-sicherheit/)[ence](https://www.nsideattacklogic.de/open-source-intelligence-osint-im-red-teaming-bessere-taktische-erkenntnisse-fuer-mehr-sicherheit/) [(](https://www.nsideattacklogic.de/open-source-intelligence-osint-im-red-teaming-bessere-taktische-erkenntnisse-fuer-mehr-sicherheit/)[OSINT)](https://www.nsideattacklogic.de/open-source-intelligence-osint-im-red-teaming-bessere-taktische-erkenntnisse-fuer-mehr-sicherheit/)

[Tar](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)[g](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)[eted Threat Intelli](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)[g](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)[ence](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/) [(](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)[TTI)](https://www.nsideattacklogic.de/was-ist-targeted-threat-intelligence-tti/)

Für diese Arten der Angriffsvorbereitung ist es oftmals erforderlich, eine Menge Daten aus vielen Quellen zu sammeln und geordnet zusammenzutragen. Dies erfordert unter Umständen eine große Menge manueller Arbeit und daher automatisieren wir in diesem Bereich gerne viel. In diesem Blogpost möchte ich einmal eines meiner Lieblingstools im Bereich OSINT-Automatisierung zeigen, nämlich Spiderfoot.

## Was ist Spiderfoot?

Spiderfoot ist eine Open-Source-Software, welche von einer sehr aktiven Community gewartet und stetig weiterentwickelt wird. Betrieben wird es von der Firma Intel471, welche auch eine kostenpflichtige Premiumversion des Tools anbietet. Allerdings ist schon die Open-Source-Version des Tools unglaublich mächtig. Das Prinzip Spiderfoot ist ganz einfach. Man gibt dem Tool einen Datenpunkt und Zugang zu Quellen und es sammelt alle Informationen, die es zu dem initialen Datenpunkt in den gegebenen Quellen finden kann und stellt diese dem Nutzer übersichtlich zur Verfügung.

Die ganze Dokumentation von Spiderfoot findet sich [hier](https://intel471.com/attack-surface-documentation).

## Wie installiert man Spiderfoot?

Die Anleitung zum Installieren von Spiderfoot findet man gemeinsam mit weiterer, ausführlicher Dokumentation auf [GitHub](https://github.com/smicallef/spiderfoot). Sie ist im Prinzip aber ganz einfach:

Copy to Clipboard

Syntax Highlighter

1

wget https://github.com/smicallef/spiderfoot/archive/v4.0.tar.gz

2

tar zxvf v4.0.tar.gz

3

cd spiderfoot-4.0

4

pip3 install -r requirements.txt

5

python3 ./sf.py -l 127.0.0.1:5001

Wenn man dabei die IP-Adresse auf 0.0.0.0 oder seine eigene ändert, ist das Web UI von Spiderfoot auch aus dem Internet erreichbar. Dann sollte aber diese aber passwortgeschützt sein indem die Datei `$HOME/.spiderfoot/passwd` angelegt wird, welche Zugangsdaten in folgendem Format enthält: `username:password`

## Feuer Frei!

Kommen wir jetzt endlich zum aufregenden Teil des Tools. Dem automatisierten Scannen von „Zielen“. Dafür bietet Spiderfoot eine einfach zu bedienende GUI, mit guter Dokumentation. Das Webinterface des Tools befindet sich auch dem in der Installation angegebenen Port, in unserem Fall ist die URL also `http://127.0.0.1:5001`. Mit einem Klick auf „New Scan“ landet man auf folgender Oberfläche:

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-1.png "spiderfoot-1")

Einen Scan „anzuschmeißen“ ist an der Stelle sehr einfach. Man gibt einen Namen und ein Ziel (eine Liste an möglichen Arten von Zielen befindet sich rechts oben im UI) an, wählt den gewünschten Scanmodus und Spiderfoot sammelt jede Menge Daten aus jeder Menge Quellen und stellt diese übersichtlich zur Verfügung.

Obwohl es natürlich verlockend ist, alles an Daten zu sammeln, was das Tool hergibt, sollte in den meisten Fällen jedoch ein Weg mit mehr Bedacht gewählt werden. Viele Daten zu haben, birgt natürlich auch das Risiko, dass wichtige Informationen in dem Datenberg untergehen.

Daher bietet Spiderfoot im Tab „By Required Data“ die Möglichkeit, nach gewünschten Daten zu selektieren. So ist sichergestellt, dass der Scan genau die Ergebnisse liefert, die gewünscht sind. Auf jeden Fall sollte man dabei den Punkt „Raw Data from RIRs/APIs“ auswählen. Denn APIs machen einen Großteil des Charmes von Spiderfoot aus.

## APIs in Spiderfoot nutzen

Ähnlich bequem wie das Einrichten des Tools und das Starten von Scans ist auch das Einbinden von diversen APIs. Da Spiderfoot eine großartige Community hat, die das Tool sehr aktiv weiterentwickelt, bietet es bereits fertige Module für viele APIs und andere Datenquellen.

Diese lassen sich über den Menüpunkt „Settings“ einsehen:

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-2.png "spiderfoot-2")

Bei allen Einstellungen mit einem Schloss an der rechten Seite ist ein API-Key nötig. Viele dieser Dienste bieten für ihre APIs eine kostenfreie Version an, also lohnt es sich definitiv einmal, die APIs zu erkunden und herauszufinden, welche Daten liefern, die einen Mehrwert bringen. Im GitHub Repository von Spiderfoot wird auch tabellarisch aufgelistet, welche der APIs eine kostenlose Version zur Verfügung stellen.

Hat man erst einmal alle API Keys in Spiderfoot eingepflegt, lohnt es sich diese über den „Export API Keys“ Button zu exportieren. Falls man einmal für ein anderes Projekt eine neue Spiderfoot Instanz aufsetzt, erspart dies viel Tipparbeit, da diese Datei über „Import API Keys“ wieder alle API-Keys in die Instanz lädt. Bei der Handhabung der Exportdatei ist jedoch Vorsicht geboten, da sie alle API Keys im Klartext beinhaltet.

## Deine Lieblings-API ist nicht dabei?

Kein Problem, Spiderfoot macht es super einfach, eigene Tools und APIs zu integrieren. Da es in Python geschrieben ist und einen sehr modularen Aufbau hat, lässt es sich sehr einfach erweitern.

## Die Scan-Ergebnisse

Spiderfoot stellt die Ergebnisse in verschiedenen Formaten zur Verfügung, die es je nach Menge der gefundenen Daten unterschiedlich gut geeignet sind.

Erst einmal sieht man ein Balkendiagramm, welches die Häufigkeit der gefundenen Datenarten aufschlüsselt. Hiermit lassen sich schon erste Anomalien erkennen, welche später genauer untersucht werden sollen. Zum Beispiel, wenn es zu einer Domain sehr viele Einträge in Daten, Leaks und Breaches gibt.

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-3.png "spiderfoot-3")

Natürlich stellt Spiderfoot die Ergebnisse auch in tabellarischer Form zur Verfügung. Hierbei werden die Daten unter dem Menüpunkt „Browse“ nach Art der Daten sortiert. Dies ist der einfachste Weg, sich durch die Daten selbst durchzuklicken.

Des Weiteren gibt es auch noch eine Aufstellung der Daten als Graph. Auch wenn dies sehr verlockend klingt, um Zusammenhänge zwischen den Daten zu erkennen, werden die Graphen bei größeren Scans jedoch sehr schnell, sehr unübersichtlich. Eine kleine Verbesserung ergibt der „Force Layout Button“, welcher für ein Mindestmaß an Struktur in den Daten sorgt.

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-4.png "spiderfoot-4")

Ein recht neues und sehr nützliches Feature sind die „Correlation Rules“, welche in Version 4.0 von Spiderfoot hinzugefügt wurden. Diese stellen, wie der Name vermuten lässt, Korrelationen zwischen verschiedenen Datenpunkten in den Scanergebnissen dar. Diese sorgen dafür, dass verschiedene relevante Findings sofort ins Auge fallen. So melden sie zum Beispiel offene Datenbanken und Cloud Buckets oder eine hohe Anzahl an bekannten Spam-Domains. Natürlich lassen sich, dank der modularen Natur von Spiderfoot, auch hier eigene Regeln sehr einfach schreiben und hinzufügen. Eine genauere Dokumentation dazu findet sich [hier](https://github.com/smicallef/spiderfoot/blob/master/correlations/README.md).

## Hat jemand KI gesagt?

Da mich persönlich gerade KI vor allem von der generativen Art sehr interessiert, konnte ich es natürlich nicht lassen, mich zu fragen, ob diese denn auch etwas mit einem Spiderfoot Scan anfangen kann.

Spiderfoot bietet netterweise die Möglichkeit, Scans sehr einfach exportieren zu lassen. Diesen Export kann man in ChatGPT oder andere Modelle hochladen. Exportieren lässt sich der Scan als CSV über den Download Button in der rechten oberen Ecke der Scanübersicht neben dem grünen Button zum neu Laden.

Leider ist das Hochladen von Dateien (außer Bildern) in allen mir bekannten ChatModellen ein Feature, welches ein kostenpflichtiges Abo benötigt. Außerdem sollte man natürlich auch den Datenschutz bedenken, denn ein Spiderfoot Scan kann unter Umständen sensible Daten enthalten, welche nicht ins Internet gelangen sollten. Andererseits sammelt Spiderfoot auch nur öffentlich verfügbare Daten, welche ja sowieso schon im Internet verfügbar sind. Abhilfe könnten hier lokale LLM-Modelle schaffen.

Der Hinweistext von [Google Gemini](https://gemini.google.com/) fasst es ganz gut zusammen:

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-5.png "spiderfoot-5")

Aber genug der Vorrede. In diesem Beispiel verwende ich ChatGPT. Hier kann der Spiderfoot Scan im CSV-Format über die Büroklammer rechts unten im Chatfenster hochgeladen werden:

![](https://www.nsideattacklogic.de/wp-content/uploads/2024/03/spiderfoot-6.png "spiderfoot-6")

Anschließend erzielt folgender Prompt recht gute Resultate:

Copy to Clipboard

Syntax Highlighter

1

You are an expert Cyber Threat Analyst holding many of the most

2

prestigious certifications in the industry.

3

Write a security report based on these findings in the SpiderFoot.csv

4

file from a Spiderfoot scan.

5

Start with a summary of the data and include different subsections that

6

explain the security risks you have identified in greater detail and

7

with actual examples from the scan.

8

Focus on security impact. Use the entire file content for your analysis.

9

This report is aimed at defenders of the organization to understand their attack surface.

10

Finish with a section that creates an action plan for defenders to

11

understand what findings and data points they should investigate closer.

12

Take a deep breath and think this step by step.

Das Ergebnis ist dabei leider nicht überragend, aber liefert einen guten Einstieg, gerade bei einer großen Datenmenge. Die Antwort kann durch einen Klick auf „+“ angezeigt werden:

#### [Antwort von ChatGPT](https://www.nsideattacklogic.de/spiderfoot#805f1c189c87247e1)

## Fazit

Spiderfoot ermöglicht es teilweise manuelle Tasks zu automatisieren. Allerdings sollte das Tool nicht als Ersatz für eine komplexe OSINT/Attack Surface Analyse gesehen werden, sondern nur als Unterstützung bei der Datensammlung. Die eigentliche Auswertung, Korrelation und Analyse der Daten muss dabei nach wie vor von sachkundigen Analysten durchgeführt werden.

## Sie möchten wissen was Ihre Attack-Surface ist?

Wir bieten Attack Surface Analysen als einzelne Dienstleistung oder in Kombination mit anderen OSINT oder Red Teaming Dienstleistungen an. Kontaktieren Sie uns gerne.
