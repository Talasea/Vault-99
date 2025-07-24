
Bei Verschlüsselung kann man grundsätzlich zwischen asymmetrischen und symmetrischen Verfahren unterscheiden. Bei beiden Verfahren müssen Schlüssel zwischen den Kommunikationspartnern getauscht werden, um zum Verschlüsseln und Entschlüsseln der Nachrichten genutzt werden zu können. Die Techniken unterscheiden sich darin, wie viele Schlüssel abhängig von der Anzahl der Kommunikationspartnerinnen und -partner erzeugt werden müssen und auf welche Weise die Schlüssel weitergegeben werden dürfen (offen oder auf abgesichertem Weg).

Wir erklären Ihnen im Folgenden, wo die Unterschiede liegen und was die Vor- und Nachteile der beiden Verfahren sind.

## Symmetrische Verschlüsselung

Bei symmetrischen Verschlüsselungsverfahren wird ein und derselbe Schlüssel für die Ver- und Entschlüsselung von Daten eingesetzt. Dieser Schlüssel muss vor der eigentlichen Kommunikation auf einem sicheren Weg zwischen Senderin bzw. Sender und Empfängerin bzw. Empfänger ausgetauscht und von beiden geheim gehalten werden. Für die Verschlüsselung von Nachrichten innerhalb großer und offener Nutzergruppen, wie dies z.B. beim E-Mail-Verkehr der Fall ist, ist die symmetrische Verschlüsselung wegen der problematischen Schlüsselverteilung nicht geeignet. Sie hat jedoch den Vorteil, auch große Datenmengen schnell ver- und entschlüsseln zu können.

## Caesar-Chiffre

Bereits aus der Antike ist die Verwendung verschiedener symmetrischer Verschlüsselungsverfahren überliefert. Die am besten bekannten dürften die durch die Spartaner genutzte Skytale und die nach ihrem bekanntesten überlieferten Nutzer benannte Caesar-Chiffre sein. Bei der Caesar-Chiffre handelt es sich um ein sehr einfaches Buchstabenersetzungs-Schema. Der folgende Text ist ein Beispiel für ein mögliches Chiffrat "**DQJULIILPPRUJHQJUDXHQ**".

Sobald man die Idee hat, ein Verschlüsselungsverfahren ähnlich der Caesar-Chiffre hinter diesem Chiffrat zu vermuten, erkennt man hier recht schnell: **jeder Buchstabe wurde durch den dritten im Alphabet auf ihn folgenden ersetzt**, wobei für die letzten Buchstaben des Alphabetes die Konvention eingeführt wird, dass sich das Alphabet nach Z wiederholt.  
Der verschlüsselte Text heißt in Klarschrift also: "**Angriff im Morgengrauen**".

Die Caesar-Chiffre kann allgemein definiert werden als folgendes Verfahren: gegeben sind ein Text bestehend nur aus Großbuchstaben und ein aus einem Buchstaben bestehenden Schlüssel (im Beispiel "D"). Ersetze nun jeden Buchstaben des Textes durch den Buchstaben, der ihm im Alphabet im gleichen Abstand folgt wie der Schlüssel dem A (im Beispiel drei Schritte).

### Ein sicheres Verfahren: das One-Time-Pad

Es gibt auch andere Chiffrier-Mechanismen, die nur sehr schwer oder überhaupt nicht geknackt werden können. Als Beispiel geben wir kurz ein - was den Schutz der Vertraulichkeit der übertragenen Informationen betrifft - absolut sicheres Verschlüsselungsverfahren an, das sich ohne technische Hilfsmittel einsetzen lässt.

Wir gehen dabei von der Caesar-Chiffre aus. Einer ihrer offensichtlichen Schwachpunkte ist die sehr kleine Anzahl möglicher Schlüssel: bei einem Alphabet von 26 Buchstaben gibt es nur 26 mögliche Schlüssel, die ein Angreifer einfach durchprobieren kann, bis er den Klartext findet. Ein erster Ansatz zur Verbesserung der Caesar-Chiffre läge daher in einer Vergrößerung des Schlüsselraumes. Ein Weg, dies zu erreichen, bestünde darin, anstatt eines Schlüsselbuchstabens ein Schlüsselwort zu verwenden und dieses buchstabenweise wie in der Caesar-Chiffre zum Klartext zu "addieren".

|   |   |
|---|---|
Beispiel
|**Klartext**|BBBBBBB|
|**Schlüssel**|CHIFFRE|
|**Chiffrat**|DIJGGSF|

In dem Beispiel kommt das **D** als **_erster Buchstabe des Chiffrats_** wie folgt zustande:  
an der **_ersten Stelle des Schlüssels_** steht ein "C". Daran liest man ab, dass an dieser Stelle ein "**A**" im **Klartext** durch ein "**C**" ersetzt werden soll, ein "B" durch ein "D", ein "C" durch ein "E" und so weiter.  
Im **Klartext** findet sich ein "B", folglich steht im **Chiffrat** an dieser Stelle ein "D".

Dieses Verfahren funktioniert so wie beschrieben nur, wenn das Schlüsselwort die gleiche wie oder eine größere Länge als die zu verschlüsselnde Nachricht hat. Es ist in der beschriebenen Form zunächst auch noch sehr unsicher. Wenn aber noch zusätzlich

- der Schlüssel aus einer vollkommen zufällig gewählten Buchstabenfolge passender Länge besteht und
- der Schlüssel nur zur Verschlüsselung einer einzigen Nachricht verwendet wird (beziehungsweise bereits einmal in einer Verschlüsselungsoperation benutzte Buchstaben des Schlüssels niemals wiederverwendet werden),

dann liefert die Kenntnis eines Chiffrats einem Angreifer, der keine Informationen über den Schlüssel hat, keinerlei Information über dessen Klartext.

Man bezeichnet dieses Verschlüsselungsverfahren auch als das One-Time-Pad.

Einschränkend zu beachten sind zusätzlich einige weitere Punkte, zum Beispiel:

- Nach einmaliger Verwendung muss der Schlüssel vernichtet werden (oder darf wenigstens nie mehr verwendet werden), da schon eine zweimalige Verwendung des gleichen Schlüssels mit verschiedenen Nachrichten das Verfahren unsicher macht. Auch bereits verwendete Teile eines Schlüssels dürfen nie mehr wiederverwendet oder bekannt werden!
- Ein Angreifer, der Teile des Schlüssels kennt, kann auch die entsprechenden Teile der Nachricht problemlos entschlüsseln.
- Die Integrität der übertragenen Nachrichten wird in keiner Weise durch das Verfahren geschützt.

Man sieht daran: auch ein Verschlüsselungsverfahren, das durch eine sehr starke theoretische Sicherheitsgarantie gestützt wird, kann noch nicht-optimale kryptographische Eigenschaften haben, zu denen die Sicherheitsgarantie keine Aussage macht. In der Entwicklung und wissenschaftlichen Bewertung moderner kryptographischer Systeme muss deshalb eine große Anzahl unterschiedlicher Sicherheitsziele und Angriffsszenarien berücksichtigt werden.

### Moderne symmetrische Chiffren

Ein Nachteil des One-Time-Pads ist die sehr große Menge an benötigtem Schlüsselmaterial: für jede verschlüsselte Verbindung zwischen zwei Parteien benötigt man einen Schlüssel, der genauso groß ist wie sämtliche Nachrichten, die sicher ausgetauscht werden sollen, zusammengenommen. Die sichere Verteilung dieser Schlüssel ist insbesondere dann, wenn mehrere Parteien miteinander kommunizieren können sollen, schwierig.

Dennoch ist das One-Time-Pad tatsächlich in wesentlichem Umfang eingesetzt worden. Eine moderne Variante sind quantenkryptographische Systeme, die das Problem des sicheren Schlüsselaustausches mit physikalischen Mitteln lösen. Es gibt auch andere in der Kryptographie wichtige Konstruktionen, die auf den Ideen hinter dem One-Time-Pad aufbauen.

Moderne symmetrische Kryptoverfahren benötigen im Gegensatz zum One-Time-Pad nur geringe Mengen an geheimen Schlüsseln, um zu funktionieren. Zumindest unter dem Vorbehalt, dass die meisten Sicherheitsgarantien der modernen Kryptographie nicht absolut sind und künftige wissenschaftliche Fortschritte heute als sicher geltende Verfahren brechen könnten, wird dabei ein sehr hohes Sicherheitsniveau erreicht. Das grundsätzliche Problem der Verteilung geheimen Schlüsselmaterials im Voraus bleibt bestehen.

## Asymmetrische Verschlüsselung

Bei der asymmetrischen Verschlüsselung gibt es im Gegensatz zur symmetrischen Verschlüsselung, bei der es nur **einen** (gemeinsamen) Schlüssel gibt, ein Schlüsselpaar aus **zwei sich ergänzenden Schlüsseln:**

1. Der öffentliche Schlüssel (engl. **Public Key)** dient zum Verschlüsseln von Nachrichten oder zur Verifikation digitaler Signaturen,
2. Der private Schlüssel (engl. **Private Key)** dient zum Entschlüsseln verschlüsselter Nachrichten sowie zur Erstellung digitaler Signaturen.

**Beide Schlüssel zusammen bilden ein Schlüsselpaar**.

Aus einem Schlüssel lässt sich der dazugehörige zweite Schlüssel nicht so leicht erraten oder berechnen. Dadurch kann man einen Teil des Schlüsselpaares öffentlich zugänglich (engl. public) machen, ohne dass damit Rückschlüsse auf den zweiten, privaten Teil des Schlüssels gezogen werden können.

Das asymmetrische Verschlüsselungsverfahren lässt sich leicht begreifen, wenn man an einen Tresor mit einem Schnappschloss denkt. **Jeder kann dort etwas einschließen**, weil der Tresor sich automatisch schließt, wenn die Tür ins Schloss fällt. **Zum Öffnen ist allerdings ein Schlüssel nötig**. Das Schnappschloss entspricht dem Public Key, mit dem jede und jeder etwas einschließen kann. Weil aber nur die Empfängerin bzw. der Empfänger über den geheimen, Private Key verfügt, kann nur sie bzw. er den Tresor öffnen und die Nachricht entziffern.

### Ein bisschen Mathematik

Die asymmetrische Verschlüsselung beruht auf mathematischen Verfahren, sogenannten "Einwegfunktionen", die in der einen Richtung einfach, aber in der umgekehrten Richtung extrem schwierig durchzuführen sind. Multiplikation ist so ein Beispiel. Es ist vergleichsweise einfach, zwei große Zahlen (Primzahlen) zu multiplizieren:  
3 121 163 * 4 811 953 = 15 018 889 661 339

Die Rückrichtung, d.h. das Zerlegen des Produkts in die beiden ursprünglichen Faktoren, ist dagegen sehr mühselig. Kennt man nur das Produkt, ist es sehr schwierig herauszufinden, aus welchen Faktoren dieses ursprünglich gebildet wurde. Verkürzt dargestellt, entspricht der Public Key diesem Produkt. Es wird benötigt, um Informationen für Empfängerinnen und Empfänger zu verschlüsseln. Der zugehörige Private Key enthält die beiden Zahlen, aus denen das Produkt gebildet wurde. Diese sind für das Entschlüsselungsprogramm nötig, um die verschlüsselte Botschaft zu entschlüsseln.

Das Problem des sicheren Schlüsselaustauschs, das bei symmetrischen Verfahren besteht, ist daher elegant gelöst: **Der öffentliche Teil kann jedem zugänglich gemacht werden, ohne dass die Sicherheit darunter leidet. Man benötigt zur Entschlüsselung immer noch den geheimen Schlüssel**. Ein weiterer Vorteil des Verfahrens ist, dass sehr viel weniger Schlüssel benötigt werden als beim symmetrischen Verfahren, das schon für die Kommunikation von zwölf Menschen untereinander 66 Schlüssel erfordert. Bei der asymmetrischen Verschlüsselung benötigt jeder nur ein Schlüsselpaar.

Aber auch asymmetrische Verschlüsselungsverfahren haben Nachteile:

- **Hoher Rechenaufwand**  
    Asymmetrische Verfahren sind im Vergleich zu symmetrischen Verfahren sehr rechenaufwändig. Um kurze Nachrichten zu verschlüsseln, benötigt der Computer somit viel Zeit. Deshalb bedient man sich eines Tricks: Mit dem langsamen, asymmetrischen Verfahren werden nur die Schlüssel für ein schnelles symmetrisches Verfahren sicher und unkompliziert ausgetauscht. Die weitere Kommunikation erfolgt dann über die schnellere symmetrische Verschlüsselung. Wenn asymmetrische Verfahren dafür genutzt werden, die Schlüssel eines symmetrischen Verfahrens zu verschlüsseln, nennt man es hybride – also kombinierte – Verschlüsselung.
- **Mangelnde Authentizität**  
    Wer etwas mit dem Public Key einer Empfängerin oder eines Empfängers verschlüsseln möchte (also ihr oder ihm etwas "in den Tresor legen" möchte) muss sichergehen können, dass dieser Schlüssel auch wirklich der jeweiligen Person gehört. Im Internet ist es leicht, sich für jemand anderen auszugeben und es könnte jemand fälschlicherweise behaupten, er wäre die berechtigte Empfängerin oder der berechtigte Empfänger. Für die falsche Identität ließen sich problemlos Schlüsselpaare generieren und Public Keys in Umlauf bringen. Der Fälscher könnte dann vertrauliche Botschaften lesen, weil die Absender seinen Schlüssel benutzt haben, statt den des eigentlich gewollten Empfängers. Würde er die Botschaft danach, vielleicht auch noch manipuliert, an die richtige Empfängerin oder den richtigen Empfänger weiterleiten, bliebe das ganze wahrscheinlich auch noch unbemerkt.
    

## PKI und Digitale Signatur

### Grundlagen Public-Key-Infrastrukturen

Das Problem der sicheren Verteilung öffentlicher Schlüssel für Public-Key-Verschlüsselungs- und digitale Signaturverfahren wird durch Public-Key-Infrastrukturen (PKI) gelöst. Zentrale Instanz einer **Public-Key-Infrastruktur** ist die **Zertifizierungsstelle**. Das ist eine allgemein anerkannte Stelle, deren Aufgabe es ist, die jeweils einmaligen Schlüsselpaare (privater und öffentlicher Schlüssel) natürlichen Personen fest zuzuordnen und dies den (anderen) Benutzerinnen und Benutzern mittels Zertifikaten zu bestätigen.

Voraussetzung dafür ist, dass der öffentliche Signaturschlüssel der Zertifizierungsstelle auf fälschungssicherem Wege im Voraus an alle Teilnehmerinnen und Teilnehmer der PKI verteilt wird. Außerdem wird vorausgesetzt, dass die Zertifizierungsstelle die Identität aller Teilnehmerinnen und Teilnehmer zuverlässig verifizieren kann und dass sie selbst eine für alle Teilnehmerinnen und Teilnehmer vertrauenswürdige Institution ist.

**Vereinfacht funktioniert dann die Verteilung öffentlicher Schlüssel über die PKI so:**

Die Zertifizierungsstelle erstellt einen Text, in dem ein öffentlicher Schlüssel einer bestimmten Person zugeordnet wird, und verschlüsselt dies mit ihrem eigenen geheimen Schlüssel. Die Zertifizierungsstelle schreibt etwa: "_Public Key Nr. 1234 gehört peter@bsi.bund.de_" und signiert dies mit ihrem Private Key.

Weil der öffentliche Schlüssel der Zertifizierungsstelle allen bekannt ist, kann jeder damit überprüfen, dass dieser Text wirklich von der Zertifizierungsstelle unterschrieben und seither nicht verändert wurde. Sofern Sie der Zertifizierungsstelle vertrauen, können Sie dann auch darauf vertrauen, dass dieser Public Key einer ganz bestimmten Person gehört.

### Grundlagen digitaler Signaturen

Analog zu asymmetrischen Verschlüsselungsverfahren gibt es auch Signaturverfahren mit öffentlichem Schlüssel. Bei asymmetrischen Verschlüsselungsverfahren kann jede und jeder, die oder der den passenden öffentlichen Schlüssel besitzt, der Besitzerin oder dem Besitzer eines privaten Schlüssels verschlüsselte Nachrichten schicken, die nur sie oder er wieder entschlüsseln kann. Signaturverfahren haben allgemein das Ziel, die Funktionalität gewöhnlicher Unterschriften für digitale Dokumente nachzubilden. Erfüllt sein soll also:

- nur die Unterzeichnerin bzw. der Unterzeichner selbst soll in der Lage dazu sein, eine für sie bzw. ihn gültige Unterschrift zu erzeugen,
- jede und jeder soll in der Lage sein, diese Unterschrift zu verifizieren.

Anders als bei gewöhnlichen Unterschriften kommt noch hinzu, dass digitale Unterschriften das unterschriebene Dokument auch vor nachträglicher Veränderung schützen. Während bei einem auf Papier geschlossenen Vertrag zumindest denkbar ist, dass nach dessen Unterzeichnung ein Betrüger zum Beispiel noch Text hinzufügt oder löscht (durchstreicht) und dadurch in nur schwer nachweisbarer Weise den Inhalt des Vertrages ändert, soll die Verifikation einer digitalen Signatur fehlschlagen, wenn jemand an der unterschriebenen Datei nach ihrer Erstellung Veränderungen vorgenommen hat.

Moderne Signaturverfahren erreichen diese Ziele in folgendem Sinne:

- jede und jeder, die bzw. der den öffentlichen Signaturschlüssel des Signierers kennt, kann dessen digitale Signaturen mit relativ geringem Aufwand überprüfen,
- wer den privaten Signaturschlüssel des Signierers nicht kennt, ist praktisch nicht in der Lage, in dessen Namen Dokumente zu signieren und
- wer den privaten Signaturschlüssel des Signierers einer Datei nicht kennt, kann die Datei praktisch nicht verändern, ohne dass die Signatur dadurch ungültig wird.

Dabei beziehen sich - wie in der Kryptographie insgesamt üblich - alle Aussagen auf den gegenwärtigen wissenschaftlichen Kenntnisstand. Es ist durchaus möglich, dass heute übliche Signaturverfahren in der Zukunft gebrochen werden können; dazu lassen sich keine Aussagen machen.

Zum Teil lassen sich digitale Signaturverfahren relativ direkt aus asymmetrischen Verschlüsselungsverfahren ableiten, zum Beispiel im Fall des weitverbreiteten RSA-Verschlüsselungssystems. Es gibt aber auch Signaturverfahren, die kein Analogon in asymmetrischen Verschlüsselungsverfahren haben und umgekehrt.