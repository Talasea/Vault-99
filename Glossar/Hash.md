Hashwerte und Hashfunktionen spielen bei der Verschlüsselung eine wichtige Rolle, jedoch nicht nur in der Kryptographie. Programmierer begegnen dem Hash bereits bei den grundlegenden Datentypen. Es gibt aber auch verwandte Konzepte, die leicht verwechselt werden.



![Hashwerte und Hashfunktionen werden an vielen Stellen in der Informatik eingesetzt, unter anderem in der Kryptografie und zum Schutz von Passwörtern.](https://cdn1.vogel.de/unsafe/540x0/smart/images.vogel.de/vogelonline/bdb/1273200/1273266/original.jpg "Hashwerte und Hashfunktionen werden an vielen Stellen in der Informatik eingesetzt, unter anderem in der Kryptografie und zum Schutz von Passwörtern.")

Hashwerte und Hashfunktionen werden an vielen Stellen in der Informatik eingesetzt, unter anderem in der Kryptografie und zum Schutz von Passwörtern.

(Bild: gemeinfrei / [CC0](https://creativecommons.org/publicdomain/zero/1.0/) )

Als Hash oder Hashwert bezeichnet die Informatik die Ausgabe einer Hashfunktion, als Hash aber auch einen listenartigen Datentyp, bei dem der Zugriff auf die Elemente über deren Hashwert erfolgt, die Hashtabelle.

Die Hashfunktion bildet allgemein einen beliebigen Datenraum auf Daten fester Größe ab. Ihre typischen Eigenschaften unterscheiden sich teilweise in verschiedenen Anwendungsbereichen. Der Name leitet sich vom englischen Begriff für Zerhacken und Gehacktem ab und bietet eine anschauliche Analogie für die Arbeitsweise einer Hashfunktion beim Berechnen von Hashes aus den Informationen der Eingabewerte.  
  
Für welche Anwendungen wird der Hash genutzt?  

- Datentyp Hashtabelle

- Caching

- Schutz sensibler Daten

- Auffinden von Duplikaten

- Suche nach ähnlichen Datensätzen oder Substrings in Zeichenketten

- Test auf Enthaltensein in einer Menge

- verschiedene Anwendungen in der Kryptographie

### Die Basisanforderungen an eine Hashfunktion

Jede Hashfunktion muss zunächst bei mehrfacher Anwendung für jede Eingabe immer wieder dasselbe Ergebnis liefern, sie muss deterministisch sein. Das unterscheidet sie von einer Randomisierungsfunktion. In die Berechnung von Hashwerten dürfen also keine zufälligen Elemente einfließen, es sei denn, diese bleiben für die Nutzungsdauer des Hashs konstant. Das ist beispielsweise bei der Programmiersprache Python der Fall, deren Interpreter beim Start einen Zufallswert für die Randomisierung der Hashwerte generiert, sodass diese nur innerhalb eines Programmmablaufs gültig sind.

Weiterhin sollten sich die Ergebnisse, die eine Hashfunktion für ihre erwartbaren Eingaben liefert, möglichst gleichmäßig auf ihren Wertebereich verteilen. Insbesondere unterschiedliche Datensätze mit demselben Hashwert, sogenannte Kollisionen, sind meist unerwünscht. Beim Datentyp Hash erhöhen sie den Aufwand für das Auffinden der entsprechenden Elemente. In der [Kryptographie](https://www.security-insider.de/was-ist-kryptographie-a-642288/) stellen sie potentielle Angriffsvektoren dar. Kollisionen lassen sich aber nur in Sonderfällen vollständig vermeiden, man spricht dann von einem perfekten Hash und mathematisch betrachtet ist die Hashfunktion injektiv. Bei manchen Anwendungen sind Kollisionen sogar nützlich. Das ist der Fall, wenn sie etwa unwesentliche Informationen wie Unterschiede in der Groß-Klein-Schreibung der Eingabewerte ausblenden. Ebenso beim Locality-sensitive Hashing (LSH), das bei der Suche nach ähnlichen Dokumenten zum Einsatz kommt, beispielsweise nach kopierten Inhalten im Web.

### Weitere charakteristische Hash-Eigenschaften

Neben der gleichmäßigen Verteilung der Hashwerte auf die Wertemenge der Hashfunktion, ist die Kontinuität ihrer Ergebnisse von Bedeutung, je nach Anwendungsfeld aber in unterschiedlicher Weise. In der Kryptographie sind Hashfunktionen erwünscht, die für verschiedene Eingaben möglichst unterschiedliche Werte liefern. Das erschwert [Brute-Force-Angriffe](https://www.security-insider.de/was-ist-ein-brute-force-angriff-a-677192/), die den Ursprungswert durch systematisches Ausprobieren möglicher Eingabewerte zu erraten versuchen. Wird der Hash dagegen zum Auffinden ähnlicher Elemente genutzt, dann sollte die Hashfunktion, gerade im Gegenteil, möglichst kontinuierliche Werte liefern. Jeder Hashwert sollte sich bei dieser Anwendung also von dem einer ähnlichen Eingabe möglichst wenig unterscheiden.

### Ein Hash ist keine Verschlüsselung!

Hashfunktionen werden häufig verwendet, um sensible Daten zu schützen. So sind zum Beispiel die Passwörter für den Shell-Zugang zu Unix und kompatiblen Systemen standardmäßig nur als Hashwert und nicht im Klartext in der Passwortdatei gespeichert. Dabei handelt es sich aber nicht um eine [Verschlüsselung](https://www.security-insider.de/was-ist-verschluesselung-a-618734/). Ein wesentlicher Unterschied besteht darin, dass eine Hashfunktion nicht invertierbar ist. Das heißt, es ist nicht möglich, den berechneten Hashwert wieder in den Ursprungswert zurückzurechnen, im genannten Beispiel in das [Passwort](https://www.security-insider.de/was-ist-ein-sicheres-passwort-a-572229/). Genau das ist aber bei einem Verschlüsselungsalgorithmus erforderlich, damit der legitime Empfänger einer verschlüsselten Nachricht den Originaltext wieder sichtbar machen kann. Beim Passworthash ist das Zurückrechnen dagegen nicht gewollt, aber auch nicht notwendig, denn eine korrekte Passworteingabe kann einfach durch den Vergleich des daraus berechneten mit dem gespeicherten Hashwert verifiziert werden.