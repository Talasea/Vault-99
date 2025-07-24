---
title: Python Aufgabenset III
author:
  - Andreas Kellerer
date: 2024-05-31
subject: Markdown
keywords:
  - Markdown
  - Example
subtitle: Aufgaben zu Datentypen
lang: en
colorlinks: "true"
titlepage: true
titlepage-background: background.pdf
titlepage-rule-color: "360049"
titlepage-text-color: FFFFFF
titlepage-rule-height: 0
header-includes:
  - \usepackage{xltabular}
book: true
classoption: oneside
code-block-font-size: \footnotesize
created: 2024-05-29T16:38
updated: 2024-05-31T14:08
---

# Aufgabe 1 - Einlesen einer Datei und Sätze sortieren

(Einführung in Dateioperationen und Listenmanipulation)

In dieser Aufgabe sollst du eine Funktion erstellen, die eine Datei einliest und deren Inhalt satzweise in eine Liste speichert. Anschließend sollen die Sätze der Länge nach geordnet werden.

Beispiel-Eingabe:

```python
# Inhalt der Datei "text.txt":
# Eine kleine Zeile.
# Das ist eine viel längere Zeile.
# Kurz.

filename = "text.txt"
```

Beispiel-Ausgabe:

```python
['Kurz.', 'Eine kleine Zeile.', 'Das ist eine viel längere Zeile.']
```

Aufgabe: Schreibe eine Funktion `read_and_sort_sentences`, die den Dateinamen als Parameter akzeptiert, die Datei einliest und die Sätze der Länge nach sortiert zurückgibt.

Die Funktion `read_and_sort_lines()` erwartet die folgenden Parameter:

* `filename`: der Name der Datei, die eingelesen werden soll.

Rückgabewert: 

* `sorted_lines`: eine Liste der Sätze, die der Länge nach aufsteigend sortiert sind.

Ergänzung:

* Die Funktion soll nun nicht nur den Text in einzelne Sätze sondern auch jeden Satz nochmals in seine einzelnen Wörter aufteilen. Es soll eine verschachtelte Liste in folgendem Format zurückgegeben werden:

```python
[['Kurz.'], ['Eine', 'Zeile.', 'kleine'], ['Das', 'ist', 'eine', 'viel', 'Zeile.', 'längere']
```


# Aufgabe 2 - Zählen der Wortvorkommen in einer Datei

(Wiederholung von Dateioperationen und Wörterbuchmanipulationen)

In dieser Aufgabe sollst du ein Programm erstellen, das einen Text aus einer Datei liest und zählt, wie oft jedes Wort vorkommt. Die Vorkommen jedes Wortes sollen in einem Wörterbuch gespeichert werden.

Beispiel-Eingabe-Datei (`text.txt`):

```python
Das ist ein Beispieltext. Dieser Text ist nur ein Beispiel.
```

Beispiel-Ausgabe:

```python
{
"Das": 1, "ist": 2, "ein": 2, "Beispieltext": 1, "Dieser": 1, "Text": 1,
"nur": 1, "Beispiel": 1, 
}
```

Aufgabe: Schreibe eine Funktion `count_words`, die eine Datei liest und die Häufigkeit jedes darin vorkommenden Wortes in einem Wörterbuch speichert.

Die Funktion `count_words()` erwartet die folgenden Parameter:

* `file_path`: der Pfad zur Datei, die den Text enthält.

Rückgabewert:

* `word_count`: ein Wörterbuch, das die Anzahl der Vorkommen jedes Wortes speichert.

Anforderungen:

* Ignoriere die Groß-/Kleinschreibung, d.h., "Das" und "das" sollten als dasselbe Wort gezählt werden.
* Entferne Satzzeichen aus den Wörtern, bevor du sie zählst.
* Sonderzeichen dürfen nicht entfernt werden (Wörter wie _Man-in-the-Middle_ sollen als ein zusammenhängendes Wort verstanden werden)

Erweiterungen: 

* Ändere die Funktion so ab, dass die Wörter alphabetisch sortiert im Wörterbuch gespeichert werden.
* Jedes Wort soll entweder groß- oder kleingeschrieben gespeichert werden, je nachdem wie es zuerst im Text vorgekommen ist (Beim dem Text "_Ein schöner Tag ist heute. Ist das ein Segen._" soll die Wörter 'ein' und 'ist' wie folgt abspeichern `{"Ein":2, "ist":2`)

Test Eingaben zur Überprüfung (legt Euch die Dateien bitte selbst an):

Datei-Inhalt (`test1.txt`):

```python
Hallo Welt! Hallo Python-Welt.
```

```python
# Erwartete Ausgabe:
# {'Hallo': 2, 'Welt': 1, 'Python-Welt': 1}
```

Datei-Inhalt (`test2.txt`):

```bash
Klaus klaute Klaus' kleine Klausur. Kleine Klausuren klaut Klaus klar, kläglich klaglos. Klaus kann klaut Klausen, klar? Klar! Klaus' klauliches Klausur-Klauen klatscht keiner klein. Kleine Klausuren klaut Klaus, klar! Klaglos klaut Klaus kleine Klausuren!
```

```python
# Erwartete Ausgabe:
{'Klaus': 6, 'klaute': 1, 'kleine': 2, 'Klausur': 1, 'Kleine': 2, 'Klausuren': 3, 'klaut': 4, 'klar': 3, 'kläglich': 1, 'klaglos': 1, 'kann': 1, 'Klausen': 1, 'Klar': 1, "Klaus'": 1, 'klauliches': 1, 'Klausur-Klauen': 1, 'klatscht': 1, 'keiner': 1, 'klein': 1, 'Klaglos': 1}
```

Test 3 (Ergänzung)

Datei-Inhalt (`test3.txt`):

```python
Ein Man-in-the-Middle (MitM) Angriff ist eine ernsthafte Bedrohung für die Sicherheit in der digitalen Welt. Bei einem Man-in-the-Middle Angriff schaltet sich ein Angreifer zwischen die Kommunikation zweier Parteien. Diese Art von Angriff ermöglicht es dem Angreifer, vertrauliche Informationen abzufangen und zu manipulieren.
```

# Aufgabe 3 - Finden des Schülers mit der höchsten Punktzahl

(In dieser Aufgabe üben wir das Durchsuchen und Verarbeiten von Listen von Dictionaries.)

In dieser Aufgabe sollst du eine Funktion erstellen, die eine Liste von Dictionaries, die Schüler und ihre Punktzahlen repräsentieren, als Eingabe nimmt und den Schüler mit der höchsten Punktzahl zurückgibt.

Beispiel-Eingabe:

```python
schueler_liste = [{'name': 'Alice', 'score': 88}, {'name': 'Bob', 'score': 92}]
```

Beispiel-Ausgabe:

```python
{'name': 'Bob', 'score': 92}
```

Aufgabe: Schreibe eine Funktion `find_highest_score`, die eine Liste von Dictionaries als Parameter akzeptiert und das Dictionary mit dem Schüler, der die höchste Punktzahl hat, zurückgibt.

Die Funktion `find_highest_score()` erwartet den folgenden Parameter:

* `schueler_liste`: eine Liste von Dictionaries, wobei jedes Dictionary die Schlüssel `name` und `score` enthält.

Rückgabewert: 

* Ein Dictionary mit dem Schüler, der die höchste Punktzahl hat.

Anforderungen:

* Wenn die Liste leer ist, soll die Funktion `None` zurückgeben.

Ergänzungen:

* Ändere die Funktion so ab, dass alle Schüler mit der höchsten Punktzahl zurückgegeben werden, wenn mehrere Schüler die gleiche höchste Punktzahl haben.

Test Eingaben zur Überprüfung:

 Test 1
 
```python
schueler_liste = [{'name': 'Alice', 'score': 88}, {'name': 'Bob', 'score': 92}, {'name': 'Charlie', 'score': 87}]
# Erwartete Ausgabe:
# {'name': 'Bob', 'score': 92}
```

Test 2

```python
schueler_liste = [{'name': 'Alice', 'score': 95}, {'name': 'Bob', 'score': 92}, {'name': 'Charlie', 'score': 95}]
# Erwartete Ausgabe:
# [{'name': 'Alice', 'score': 95}, {'name': 'Charlie', 'score': 95}]
```

Test 3 (Ergänzung)

```python
schueler_liste = [{'name': 'Daniel', 'score': 85}, {'name': 'Eva', 'score': 90}, {'name': 'Frank', 'score': 90}, {'name': 'Grace', 'score': 88}]
# Erwartete Ausgabe:
# [{'name': 'Eva', 'score': 90}, {'name': 'Frank', 'score': 90}]
```