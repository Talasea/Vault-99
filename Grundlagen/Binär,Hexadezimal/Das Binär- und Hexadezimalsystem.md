[[11.12.2024 Binärzahlen.pdf]]


# Binärsystem (Dual also immer 2  (2potenz ))

- **Binärsystem**: Das Binärsystem ist ein Zahlensystem zur Basis 2, das nur zwei Ziffern verwendet: 0 und 1. Es wird oft in der Informatik verwendet, da es einfach ist, binäre Zahlen in elektronischen Schaltkreisen zu verarbeiten.




## Hexadezimalsystem ( Hexa = 16 (16 Potenz))

- **Hexadezimalsystem**: Das Hexadezimalsystem ist ein Zahlensystem zur Basis 16, das 16 Ziffern verwendet: 0-9 und A-F. Es wird oft verwendet, um binäre Zahlen in einer komfortableren Form darzustellen, da eine hexadezimale Ziffer vier binäre Ziffern entspricht. Das Umrechnen zwischen dem Binärsystem und dem Hexadezimalsystem ist relativ einfach, da die Zahl 16 selbst eine Zweierpotenz ist (2^4 = 16). Dies bedeutet, dass je vier Ziffern im Binärsystem einer Ziffer im Hexadezimalsystem entsprechen. Eine Tabelle kann bei der Umrechnung von Binär- in Hexadezimalzahlen hilfreich sein. Wenn man eine Binärzahl in eine Hexadezimalzahl umrechnen möchte, unterteilt man die Binärzahl in Blöcke zu je vier Ziffern und liest die entsprechenden hexadezimalen Ziffern aus der Tabelle ab. Das Hexadezimalsystem wird in der Datenverarbeitung genutzt, um Informationen, die im Binärsystem viele Stellen brauchen, komfortabel mit wenigen Stellen darzustellen. Es wird oft in der Informatik verwendet, um binäre Zahlen in einer lesbareren Form darzustellen.



## Umrechnung 


## Hexadezimal-Tabelle zur Umwandlung in Dezimal- und Binärzahlen

Hexadezimalzahlen gehören einem komplexeren System an als das reine Binär- oder Dezimalsystem und werden oft im Zusammenhang mit Speicheradressen verwendet. Durch die Unterteilung einer binären Zahl in Gruppen von **4 Bits** kann jeder Bit-Satz von 4 Ziffern einen Wert zwischen „0000“ (0) und „1111“ (8+4+2+1 = 15) annehmen. Dies ergibt insgesamt 16 verschiedene Zahlenkombinationen von 0 bis 15. Hier ist zu beachten, dass auch „0“ auch eine gültige Ziffer ist.

| Dezimalzahl | 4 Bit-Binärzahl | Hexadezimalzahl |
| ----------- | --------------- | --------------- |
| 0           | 0000            | 0               |
| 1           | 0001            | 1               |
| 2           | 0010            | 2               |
| 3           | 0011            | 3               |
| 4           | 0100            | 4               |
| 5           | 0101            | 5               |
| 6           | 0110            | 6               |
| 7           | 0111            | 7               |
| 8           | 1000            | 8               |
| 9           | 1001            | 9               |
| 10          | 1010            | A               |
| 11          | 1011            | B               |
| 12          | 1100            | C               |
| 13          | 1101            | D               |
| 14          | 1110            | E               |
| ==15==      | ==1111==        | ==F==           |
| 16          | 0001 0000       | 10 (1+0)        |
| 17          | 0001 0001       | 11 (1+1)        |
| 18          | 0001 0010       | 12 (1+2)        |
| 19          | 0001 0011       | 13 (1+3)        |
| 20          | 0001 0100       | 14 (1+4)        |


Der Umrechnungstabelle nach sieht unsere vorherige binäre Zahlenreihe 1111 0101 1100 11112 im Hexadezimalsystem wie folgt aus: **F5CF** – diese Zahl ist nun einfacher zu lesen als die lange Bitfolge. Durch die Verwendung der hexadezimalen Notation wird ein digitaler Code also mit weniger Ziffern und einer deutlich **geringeren Fehlerwahrscheinlichkeit** geschrieben. Ebenso ist die Konvertierung von Hexadezimalzahlen zurück in Binärzahlen lediglich der umgekehrte Vorgang.

Um unsere Zahl von eben nun eindeutig als Hexadezimalzahl zu kennzeichnen, können Sie F5CF in der Form von **F5CF16**, **$F5CF** oder **#F5CF** angeben. Letztere Schreibweise, auch Hashwert genannt, kommt in der digitalen Farbkodierung zum Einsatz, denn Designer und Entwickler verwenden HEX-Farben im Webdesign. Eine HEX-Farbe wird als sechsstellige Kombination aus Zahlen und Buchstaben ausgedrückt, die durch ihre Mischung aus Rot, Grün und Blau ([RGB](https://www.ionos.de/digitalguide/websites/webdesign/rgb-farben/ "RGB-Farben")) definiert ist. #000000 beispielsweise steht für die Farbe Schwarz und #FFFFFF für die Farbe Weiß



#### Erklärungen 



## Dezimalzahl in Binärzahl umwandeln

Um eine Dezimalzahl in eine Binärzahl umzuwandeln, muss die Dezimalzahl nur durch die Zahl 2 dividiert und der Rest notiert werden.

Da eine Zahl dividiert durch 2 immer nur den Rest 0 oder 1 ergeben kann (da beim Rest 2 der Quotient um 1 erhöht werden müsste), entsteht daraus die äquivalente Binärzahl. Folgende Schritte müssen immer wieder durchgeführt werden:

1. ==Die Zahl durch 2 dividieren==
2. ==Den Rest der Division notieren==
3. ==Falls das Ergebnis nicht 0 ist, Schritt 1 und 2 wiederholen==

## Dezimalzahl in Binärzahl - Beispiel:

|Zahl|Quotient|Rest|
|---|---|---|
|190:2=|95|0|
|95:2=|47|1|
|47:2=|23|1|
|23:2=|11|1|
|11:2=|5|1|
|5:2=|2|1|
|2:2=|1|0|
|1:2=|0|1|

Die Dezimalzahl 190 ergibt daher die Binärzahl:

![190_{10}=10111110_2](https://www.mathe-lexikon.at/media/formulas/bf422d7d72498d5129200f538f8b8b9f.png "190_{10}=10111110_2")


Beispiel  10 in binär

10/2=5R0                            
  5/2=2R1
  2/2=1R0
  1/2=0R1
 



## Dezimalzahl in Hexadezimalzahl umwandeln

Um eine Dezimalzahl in eine Hexadezimalzahl umzuwandeln, muss die Dezimalzahl nur durch die Zahl 16 dividiert und der Rest notiert werden.

Da eine Zahl dividiert durch 16 immer nur einen Rest von 0 bis 15 ergeben kann (da beim Rest 16 der Quotient um 1 erhöht werden müsste), entsteht daraus die äquivalente Hexadezimalzahl. Folgende Schritte müssen immer wieder durchgeführt werden:

1. ==Die Zahl durch 16 dividieren==
2. ==Den Rest der Division notieren==
3. ==Falls das Ergebnis nicht 0 ist, Schritt 1 und 2 wiederholen==
4. ==Am Ende müssen nur alle Rest-Zahlen, die größer 9 sind durch die entsprechenden hexadezimalen Zahlen (A, B, C, D, E, F) ersetzt werden.==

## Dezimalzahl in Hexadezimalzahl - Beispiel:

|Zahl|Quotient|Rest|
|---|---|---|
|45791:16=|2861|15 = F|
|2861:16=|178|13 = D|
|178:16=|11|2|
|11:16=|0|11 = B|


Die Dezimalzahl 45791 ergibt daher die Hexadezimalzahl:

![45791_{10}=B2DF_{16}](https://www.mathe-lexikon.at/media/formulas/ca6e3fd53c9c512ce9bcb934263287a1.png "45791_{10}=B2DF_{16}")


Dezimal zu Hexa :
Die Dezimalzahl 14 wird ins Hexadezimalsystem umgewandelt

Gehe nach folgendem Verfahren vor:
 (1) Teile die Zahl mit Rest durch 16.
 (2) Der Divisionsrest ist die nächste Ziffer (von rechts nach links).
     Für Reste > 9 nimm die Buchstaben A, B, C, D, E, F
 (3) Falls der (ganzzahlige) Quotient = 0 ist, bist du fertig,
     andernfalls nimm den (ganzzahligen) Quotienten als neue Zahl 
     und wiederhole ab (1).

     14 : 16 =  0  Rest: 14   --> Ziffer: E

     Resultat: E


Die Dezimalzahl 47 wird ins Hexadezimalsystem umgewandelt

Gehe nach folgendem Verfahren vor:
 (1) Teile die Zahl mit Rest durch 16.
 (2) Der Divisionsrest ist die nächste Ziffer (von rechts nach links).
     Für Reste > 9 nimm die Buchstaben A, B, C, D, E, F
 (3) Falls der (ganzzahlige) Quotient = 0 ist, bist du fertig,
     andernfalls nimm den (ganzzahligen) Quotienten als neue Zahl 
     und wiederhole ab (1).

     ==47 : 16 =  2  Rest: 15   --> Ziffer: f
      2 : 16 =  0  Rest:  2   --> Ziffer:2

     Resultat: 2F
     

Dezimal zu Binär
https://www.arndt-bruenner.de/mathe/scripts/Zahlensysteme.htm

beispiel 63 :

Die Dezimalzahl 63 wird ins 2er-System umgewandelt

Gehe nach folgendem Verfahren vor:
 (1) Teile die Zahl mit Rest durch 2.
 (2) Der Divisionsrest ist die nächste Ziffer (von rechts nach links).
 (3) Falls der (ganzzahlige) Quotient = 0 ist, bist du fertig,
     andernfalls nimm den (ganzzahligen) Quotienten als neue Zahl 
     und wiederhole ab (1).

     63 : 2 = 31  Rest: 1
     31 : 2 = 15  Rest: 1
     15 : 2 =  7  Rest: 1
      7 : 2 =  3  Rest: 1
      3 : 2 =  1  Rest: 1
      1 : 2 =  0  Rest: 1

     Resultat: 111111



Beispiel 700 :

Die Dezimalzahl 700 wird ins 2er-System umgewandelt

Gehe nach folgendem Verfahren vor:
 (1) Teile die Zahl mit Rest durch 2.
 (2) Der Divisionsrest ist die nächste Ziffer (von rechts nach links).
 (3) Falls der (ganzzahlige) Quotient = 0 ist, bist du fertig,
     andernfalls nimm den (ganzzahligen) Quotienten als neue Zahl 
     und wiederhole ab (1).

     700 : 2 = 350  Rest: 0
     350 : 2 = 175  Rest: 0
     175 : 2 =  87  Rest: 1
      87 : 2 =  43  Rest: 1
      43 : 2 =  21  Rest: 1
      21 : 2 =  10  Rest: 1
      10 : 2 =   5  Rest: 0
       5 : 2 =   2  Rest: 1
       2 : 2 =   1  Rest: 0
       1 : 2 =   0  Rest: 1

     Resultat: 1010111100
 
     


