---
title: Python Aufgabenset II
author:
  - Andreas Kellerer
date: 2024-05-29
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
created: 2024-05-28T14:40
updated: 2024-05-31T08:55
---

# Aufgabe 1 - Einfügen von Elementen in eine Liste

(Wiederholung Listenmanipulation und String-Operationen)

In dieser Aufgabe sollst du eine Funktion erstellen, die eine Liste und zwei Strings als Eingabe nimmt. Der erste String soll in die Liste eingefügt werden, nachdem der zweite String in der Liste gefunden wurde.

Beispiel-Eingabe:

```python
liste = ["a", "b", "c"]
string1 = "x"
string2 = "b"
```

Beispiel-Ausgabe:

```python
["a", "b", "x", "c"]
```

Aufgabe: Schreibe eine Funktion `insert_after`, die eine Liste und zwei Strings als Parameter akzeptiert und den ersten String in die Liste einfügt, nachdem der zweite String in der Liste gefunden wurde.

Die Funktion `insert_after()` erwartet die folgenden Parameter:

* `liste`: die ursprüngliche Liste.
* `string1`: der einzufügende String.
* `string2`: der String, nach dem der einzufügende String platziert werden soll.

Rückgabewert: 

* `neue_liste`: eine neue Liste, in die `string1` nach dem Vorkommen von `string2` eingefügt wurde.

Anforderungen:

* Wenn `string2` nicht in der Liste gefunden wird, soll `string1` am Ende der Liste hinzugefügt werden.

Ergänzungen:

* Ändere die Funktion so ab, dass `string1` **nach jedem** Vorkommen von `string2` ergänzt wird

Test Eingaben zur Überprüfung:

 Test 1
 
```python
liste = ["Katze", "Hund", "Vogel"]
string1 = "Maus"
string2 = "Hund"
# Erwartete Ausgabe:
# ["Katze", "Hund", "Maus", "Vogel"]
```

Test 2

```python
liste = [1, "Iron Man", 3.5, "Thor", True, "Hulk"]
string1 = "Captain America"
string2 = "Thor"
# Erwartete Ausgabe:
# [1, "Iron Man", 3.5, "Thor", "Captain America", True, "Hulk"]
```

Test 3 (Ergänzung)

```python
liste = [1, "Thor", "Iron Man", 3.5, "Thor", True, "Hulk", "Thor"]
string1 = "Captain America"
string2 = "Thor"
# Erwartete Ausgabe:
# [1, "Thor", "Captain America", "Iron Man", 3.5, "Thor", "Captain America", True, "Hulk", "Thor", "Captain America"]
```


# Aufgabe 2 - Zerlegen eines Tupels

(Wiederholung Tupelmanipulation und Fehlerbehandlung)

In dieser Aufgabe sollst du eine Funktion erstellen, die ein Tupel und einen Index als Eingabe nimmt. Das Tupel soll an der angegebenen Stelle aufgeteilt werden, und die Funktion soll zwei separate Tupel zurückgeben: eines mit dem ersten Teil und eines mit dem zweiten Teil. Die Funktion soll Indexfehler (`IndexError`) korrekt behandeln.

Beispiel-Eingabe:

```python
tupel = (1, 2, 3, 4, 5)
index = 2
```

Beispiel-Ausgabe:

```python
((1, 2), (3, 4, 5))
```

Aufgabe: Schreibe eine Funktion `split_tuple`, die ein Tupel und einen Index als Parameter akzeptiert und das Tupel an der angegebenen Stelle aufteilt. Falls der Index außerhalb des gültigen Bereichs liegt, soll die Funktion eine entsprechende Fehlermeldung ausgeben.

Die Funktion `split_tuple()` erwartet die folgenden Parameter:

- `tupel`: das ursprüngliche Tupel.
- `index`: der Index, an dem das Tupel aufgeteilt werden soll.

Rückgabewert: 

- Ein Tupel mit zwei Tupeln: das erste enthält den ersten Teil des ursprünglichen Tupels, das zweite den zweiten Teil.

Anforderungen:

- Die Funktion soll `IndexError` behandeln und eine entsprechende Fehlermeldung ausgeben.

Beispielhafte Eingaben zur Überprüfung:

Test 1

```python
tupel = (1, 2, 3, 4, 5)
index = 2
# Erwartete Ausgabe:
# ((1, 2), (3, 4, 5))
```

Test 2

```python
tupel = ("Link", "Zelda", "Ganondorf", "Navi", "Midna", "Sheik", "Epona")
index = 4
# Erwartete Ausgabe:
# (("Link", "Zelda", "Ganondorf", "Navi"), ("Midna", "Sheik", "Epona"))
```

Test 3

```python
tupel = ("Harry", "Ron", "Hermine")
index = 5
# Erwartete Ausgabe:
# "IndexError: Index out of range. The tuple has only 3 elements."
```

# Aufgabe 3 - Zählen von Elementen in einer Liste

(Wiederholung von Schleifen und Dictionaries)

In dieser Aufgabe sollst du eine Funktion erstellen, die die Häufigkeit von Elementen in einer Liste zählt. Die Funktion soll ein Dictionary zurückgeben, das die Anzahl der Vorkommen jedes Elements in der Liste speichert.

Beispiel-Eingabe:

```python
items = ["apple", "banana", "apple", "orange", "banana", "banana"]
```

Beispiel-Ausgabe:

```python
{"apple": 2, "banana": 3, "orange": 1}
```

Aufgabe: Schreibe eine Funktion `count_frequencies`, die eine Liste als Parameter akzeptiert und ein Dictionary zurückgibt, das die Häufigkeit jedes Elements in der Liste speichert.

Die Funktion `count_frequencies()` erwartet die folgenden Parameter:

- `items`: eine Liste von Strings, deren Häufigkeit gezählt werden soll.

Rückgabewert: 

- Ein Dictionary, das die Anzahl der Vorkommen jedes Elements in der Liste speichert.

Beispielhafte Eingaben zur Überprüfung:

Test 1

```python
items = ["apple", "banana", "apple", "orange", "banana", "banana"]
# Erwartete Ausgabe:
# {"apple": 2, "banana": 3, "orange": 1}
```

Test 2

```python
items = ["Mario", 1, "Luigi", 2.5, "Mario", True, "Bowser", 1]
# Erwartete Ausgabe:
# {"Mario": 2, 1: 2, "Luigi": 1, 2.5: 1, True: 1, "Bowser": 1}
```

Test 3

```python
items = ["Löwe", "Elefant", 3.14, "Giraffe", "Löwe", "Giraffe", "Löwe", False]
# Erwartete Ausgabe:
# {"Löwe": 3, "Elefant": 1, 3.14: 1, "Giraffe": 2, False: 1}
```


# Aufgabe 4 - Zusatzaufgabe
(benötigt: `argparse` Modul, importieren von eigenen Funktionen)

Die drei oben erstellten Funktionen sollen in einer Datei `meineFunktionen` gespeichert sein. Diese soll in Eurer Hauptdatei (mit einem beliebigen Namen) importiert werden.
Verwende das `argparse` Modul, um für jede der drei Funktionen einen Parameter zu definieren, der die entsprechende Funktion aufruft.

**Wichtig**: Die Funktionen erwarten alle Parameter! Es müssen also auch `argparse` Parameter definiert werden um diese Funktionsparameter zu übergeben. Das Programm soll Logik beinhalten, sodass die Funktion nur aufgerufen wird, wenn die notwendigen Parameter für die Funktion auch auf der Kommandozeile eingegeben wurden.