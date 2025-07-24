
Ein Hash (auch Hashwert oder Hashcode genannt) ist ein eindeutiger, numerischer Wert, der aus einem beliebigen Datensatz (z.B. Text, Bild, Audio) berechnet wird. Der Hashwert ist eine kompakte Darstellung des ursprünglichen Datensatzes und dient als eindeutiger Fingerabdruck, um den Inhalt des Datensatzes zu identifizieren.

## Hashfunktion

Die Hashfunktion ist ein Algorithmus, der den Hashwert berechnet. Sie wandelt den Datensatz in einen fixen, kürzeren String um, indem sie die Eingabedaten durch eine Reihe von Operationen (z.B. Bitverschiebungen, Additionen, Multiplikationen) transformiert. Die Hashfunktion sollte folgende Eigenschaften aufweisen:

1. **Einwegfunktion**: Aus dem Hashwert kann nicht der ursprüngliche Datensatz rekonstruiert werden.
2. **Kollisionssicherheit**: Es sollte keine zwei verschiedenen Eingabedaten den gleichen Hashwert ergeben.

## Anwendungsbereiche

Hashwerte werden in vielen Bereichen eingesetzt, wie:

1. **Datenbanken**: Hashwerte ermöglichen schnelle Suche und Indexierung von Daten.
2. **Passwortverwaltung**: Hashwerte werden verwendet, um Passwörter sicher zu speichern und zu überprüfen.
3. **Digitalen Signatures**: Hashwerte dienen als Basis für digitale Signaturen, um die Authentizität von Daten zu garantieren.
4. **Dateiüberprüfung**: Hashwerte können verwendet werden, um die Integrität von Dateien zu überprüfen.

## Beispiel

Ein Beispiel für eine Hashfunktion ist die MD5-Hashfunktion. Sie wandelt einen Text in einen 32-Zeichen-Hashcode um, wie z.B. `d41d8cd9` für den Text “Hello World”. Der Hashcode ist eindeutig für den Text und kann verwendet werden, um ihn zu identifizieren oder zu überprüfen.

Insgesamt dient der Hash als ein effizientes Mittel, um Daten zu komprimieren und zu indexieren, während die Sicherheit und Integrität der Daten gewährleistet bleibt.