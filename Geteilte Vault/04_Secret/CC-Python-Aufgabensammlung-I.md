---
title: Python Aufgabenset I
author:
  - Andreas Kellerer
date: 2024-05-28
subject: Markdown
keywords:
  - Markdown
  - Example
subtitle: Wiederholung zu Listen
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
code-block-font-size: \scriptsize
created: 2024-05-27T21:14
updated: 2024-06-27T15:53
---

# Aufgabe 1 - Numerisches Dreieck
(Wiederholung Schleifen)

Es soll ein numerisches Dreieck mithilfe der `print()`Funktion ausgegeben werden. Die Ausgabe soll wie folgt aussehen:

```python
1
22
333
4444
55555
......
```

Aufgabe:
Schreibe eine Funktion `print_numeric_triangle()`.

Die Funktion `print_numeric_triangle()` erwartet den folgenden Parameter:
- `N`: eine positive Ganzzahl.

Rückgabewert:
- Keiner. Die Funktion soll die Zeilen des Dreiecks direkt ausgeben.

Anforderungen:
* Verwende nur eine einzige for-Schleife und print-Anweisungen.

Ausgabeformat:
- Drucke N Zeilen wie oben gezeigt.

Beispiel-Ausgabe für den Aufruf `print_numeric_triangle(4):

```python
1
22
333
4444
```

Bonus: Verwende einen Format-String um die Ausrichtung des Dreiecks anzupassen, sodass die Ausgabe in die andere Richtung bündig ist.

```python
   1   
  22  
 333 
4444
```


# Aufgabe 2 - Split and Join
(Umwandlung Strings/Listen)

In Python kann ein String anhand eines Trennzeichens aufgeteilt werden.

Beispiel:

```python
>>> a = "this is a string"
>>> a = a.split(" ") # a wird in eine Liste von Strings umgewandelt.
>>> print a
['this', 'is', 'a', 'string']
```

Das Verbinden von Strings ist einfach:

```python
>>> a = "-".join(a)
>>> print a
this-is-a-string
```

Aufgabe:
Schreibe eine Funktion `split_and_join()`

Die Funktion `split_and_join()` erwartet die folgenden Parameter:
- `zeichenkette`: ein String bestehend aus durch Leerzeichen getrennten Wörtern.
- `delimiter`: ein einzelnes Zeichen, welches als Delimiter verwendet werden soll, um die einzelnen Woerter wieder miteinander zu verbinden

Rückgabewert:
- `ret_string`: der resultierende String

Anforderungen:
* Die Funktion soll prüfen, dass beide parameter ein String sind
* Zusätzlich soll geprüft werden, dass`delimiter` nur exakt ein Zeichen lang ist

Teste deine Funktion an folgenden Teststrings:

```python
tstring1 = "Wenn ich einen Fehler mache, bleibt am Standort des Wohnquartiers nur noch ein Mark Watney Gedächtniskrater übrig (Der Marsianer)"
tstring2 = "Wir   testen immer    auch    Sonderfälle"
```

Wie verhält sich die Funktion im Falle von `tstring2` ?


# Aufgabe 3 - Verketten von zwei Listen
(Wiederholung Schleifen und Listen)

In dieser Aufgabe sollst du zwei Listen so miteinander verketten, dass jede Kombination der Elemente beider Listen entsteht.

Beispiel-Eingabe:
```python
list1 = ["Hello ", "Bye "]
list2 = ["Dear", "Sir"]
```

Beispiel-Ausgabe:
```python
['Hello Dear', 'Hello Sir', 'Bye Dear', 'Bye Sir']
```

Aufgabe:
Schreibe eine Funktion `concatenate_lists()`, die zwei Listen in einer bestimmten Reihenfolge verknüpft.

Die Funktion `concatenate_lists()` erwartet die folgenden Parameter:
- `list1`: die erste Liste mit Strings.
- `list2`: die zweite Liste mit Strings.

Rückgabewert:
- `combined_list`: eine neue Liste, die jede Kombination der Elemente aus `list1` und `list2` enthält.

Anforderungen:
* Stelle sicher, dass alle Kombinationen der Elemente beider Listen in der neuen Liste enthalten sind.

Teste deine Funktion mit verschiedenen lustigen und gut durchdachten Listen und stelle sicher, dass die Ausgabe korrekt ist.

Test 1

```python
list1 = ["Die Katze ", "Der Hund "]
list2 = ["springt", "läuft"]
# Erwartete Ausgabe:
# ['Die Katze springt', 'Die Katze läuft', 'Der Hund springt', 'Der Hund läuft']
```

Test 2

```python
list1 = ["Homer ", "Marge ", "Bart "]
list2 = ["isst Donuts", "ärgert Ned Flanders", "macht Hausarbeit"]
# Erwartete Ausgabe:
# ['Homer isst Donuts', 'Homer ärgert Ned Flanders', 'Homer macht Hausarbeit',
#  'Marge isst Donuts', 'Marge ärgert Ned Flanders', 'Marge macht Hausarbeit',
#  'Bart isst Donuts', 'Bart ärgert Ned Flanders', 'Bart macht Hausarbeit']
```


# Aufgabe 4 - Finde die zweitniedrigste Wertung

Gegeben ist eine Liste mit Schülern und Wertungen. Schreibe eine Funktion `find_second_best()` welche die Schüler/Wertung-Paare in einer verschachtelten Liste speichert und drucke den oder die Namen der Schüler, die die zweitniedrigste Wertung haben.

Hinweis: Wenn es mehrere Schüler mit der zweitniedrigsten Wertung gibt, sortiere ihre Namen alphabetisch und drucke jeden Namen in einer neuen Zeile.

Beispiel:

```python
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
```

Die geordnete Liste der Wertungen ist [20.0, 50.0], sodass die zweitniedrigste Wertung 50.0 ist. Es gibt zwei Schüler mit dieser Wertung: `["beta", "alpha"]`. Alphabetisch geordnet werden die Namen wie folgt gedruckt:

```
alpha
beta
```

Aufgabe:
Schreibe eine Funktion `concatenate_lists()`, die zwei Listen in einer bestimmten Reihenfolge verknüpft.

Die Funktion `find_second_best()` erwartet die folgenden Parameter:
- `list1`: die Liste mit Strings als Namen und Integer oder Float als Wertung.

Rückgabewert:
- Keiner. Die Funktion soll die Namen der Schüler direkt ausgeben.

Ausgabeformat:
- Drucke den oder die Namen der Schüler, die die zweitniedrigste Wertung haben. Wenn es mehrere Schüler gibt, sortiere ihre Namen alphabetisch und drucke jeden Namen in einer neuen Zeile.

Beispiel Liste:

```python
liste = ["Harry", 37.21, "Berry", 37.21, "Tina", 37.2, "Akriti", 41, "Harsh", 39]
```

Beispiel Ausgabe:

```
Berry
Harry
```

Erklärung:
Es gibt 5 Schüler in dieser Klasse, deren Namen und Wertungen wie folgt in einer Liste zusammengefasst werden:
```python
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
```

Die niedrigste Wertung von 37.2 gehört zu Tina. Die zweitniedrigste Wertung von 37.21 gehört sowohl Berry als auch Harry, daher sortieren wir ihre Namen alphabetisch und drucken jeden Namen in einer neuen Zeile.

Test 1 

```python
liste = ["Luke", 75.3, "Leia", 67.8, "Han", 92.1, "Yoda", 84.6, "Vader", 97.0, "Obi-Wan", 77.4, "Palpatine", 59.9, "Chewbacca", 67.8]
```

Test 2

```python
tlist1 = ["Harry", 55.5, "Hermione", 60.0, "Ron", 45.7, "Draco", 50.8, "Neville", 42.3, "Luna", 45.7, "Snape", 50.8, "$onderfall", 45.7]
```

