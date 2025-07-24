
Kurze Erklärung zur Wiederholung:
In der IT werden Zahlen oft in unterschiedlichen Zahlensystemen dargestellt. Die drei
am häufigsten genutzten sind:
• Dezimal (Basis 10): Unser gewöhnliches Zahlensystem mit Ziffern von 0 bis 9.
• Binär (Basis 2): Besteht nur aus den Ziffern 0 und 1. Jeder Stelle entspricht einer
Potenz von 2.
• Hexadezimal (Basis 16): Verwendet die Ziffern 0 bis 9 sowie die Buchstaben A bis
F für die Werte 10 bis 15. Jede Stelle entspricht einer Potenz von 16.
Wie wandle ich um?
1. Dezimal nach Binär:
• Teile die Dezimalzahl wiederholt durch 2.
• Notiere den Rest (0 oder 1) bei jedem Schritt.
• Lies die notierten Reste von unten nach oben (also in umgekehrter
Reihenfolge) ab. Diese Folge ist der Binärwert.
Beispiel:
Dezimal: 13
13 ÷ 2 = 6 Rest 1
6 ÷ 2 = 3 Rest 0
3 ÷ 2 = 1 Rest 1
1 ÷ 2 = 0 Rest 1
Binär: 1101 (Reste von unten nach oben gelesen)

2. Dezimal nach Hexadezimal:
• Teile die Dezimalzahl wiederholt durch 16.
• Notiere den Rest. Ist der Rest größer als 9, verwende A=10, B=11, C=12, D=13,
E=14, F=15.
• Lies die notierten Reste am Ende von unten nach oben ab.
Beispiel:
Dezimal: 255
255 ÷ 16 = 15 Rest 15 (F)
15 ÷ 16 = 0 Rest 15 (F)
Hexadezimal: FF

3. Binär nach Dezimal:
• Schreibe jede Binärziffer mit ihrer Wertigkeit (Potenz von 2) auf.
• Addiere die Werte, für die eine „1“ steht.
Beispiel:
Binär: 1010
Stellen von rechts nach links:
1 × 2 = 1 × 8 = 8 3
0 × 2 = 0 2
1 × 2 = 1 × 2 = 2 1
0 × 2 = 0 0
Summe = 8 + 2 = 10 (Dezimal)
4. Hexadezimal nach Dezimal:
• Ordne jeder Ziffer ihren Dezimalwert zu (0-9, A=10, B=11, ...).
• Multipliziere jede Stelle mit der entsprechenden Potenz von 16 und addiere
alles.
Beispiel:
Hexadezimal: 3A
3 = 3 (Dezimal)
A = 10 (Dezimal)
„3A“ = (3 × 16 ) + (10 × 16 ) = (3 × 16) + (10 × 1) = 48 + 10 = 58 (Dezimal) 1 0

Aufgaben:

1. Dezimal nach Binär:
a) 5

 5 : 2 = 2  Rest: 1
 2 : 2 = 1  Rest: 0
 1 : 2 = 0  Rest: 1

 Resultat: 101

b) 18
18 : 2 =  9  Rest: 0
  9 : 2 =  4  Rest: 1
  4 : 2 =  2  Rest: 0
  2 : 2 =  1  Rest: 0
  1 : 2 =  0  Rest: 1

 Resultat: 10010
 
c) 100
 100 : 2 =  50  Rest: 0
  50 : 2 =  25  Rest: 0
  25 : 2 =  12  Rest: 1
  12 : 2 =   6  Rest: 0
   6 : 2 =   3  Rest: 0
   3 : 2 =   1  Rest: 1
   1 : 2 =   0  Rest: 1

 Resultat: 1100100
 
d) 255

255 : 2 = 127  Rest: 1
 127 : 2 =  63  Rest: 1
  63 : 2 =  31  Rest: 1
  31 : 2 =  15  Rest: 1
   15 : 2 =   7  Rest: 1
7 : 2 =   3  Rest: 1
3 : 2 =   1  Rest: 1
1 : 2 =   0  Rest: 1

 Resultat: 11111111


2. Dezimal nach Hexadezimal:
a) 12 = c
b) 47

47 : 16 =  2  Rest: 15   = F
  2 : 16 =  0  Rest:  2   =  2

 Resultat: 2F

c) 175

  175 : 16 =  10  Rest: 15   = F
  10 : 16 =   0  Rest: 10   = A

 Resultat: AF

d) 256

256 : 16 =  16  Rest:  0   =Ziffer: 0
 16 : 16 =   1  Rest:  0  = Ziffer: 0
 1 : 16 =   0  Rest:  1   = Ziffer: 1

 Resultat: 100


3. Binär nach Dezimal:
a) 101

 1 · 1 =  1
 0 · 2 =  0
 1 · 4 =  4
 =
5

b) 1111

1 · 1 =  1
 1 · 2 =  2
 1 · 4 =  4
 1 · 8 =  8
 =
 15
 
 
c) 10010

0 ·  1 =   0
 1 ·  2 =   2
 0 ·  4 =   0
 0 ·  8 =   0
 1 · 16 =  16
 =
 18
 
d) 110011
1 ·  1 =   1
 1 ·  2 =   2
 0 ·  4 =   0
 0 ·  8 =   0
 1 · 16 =  16
 1 · 32 =  32
 =
 51


4. Hexadezimal nach Dezimal:
a) A = 10 
b) 1F

F= 15 ·  1 = 15
1=1 · 16 =16

15+16 = 31

Resultat = 31 


c) 2A
A=10 ·  1 = 10
2= 2 · 16 = 32
10+32 = 42

Resultat = 42

d) FF

F= 15 ·   1 = 15 
F= 15 ·  16  =240
240+15 = 255

Resultat= 255

5. Bonus (gemischte Aufgaben):
a) Wandle die dezimale Zahl 2023 in Binär und Hexadezimal um.

Hex: 
2023 : 16 =  126  Rest:  7  = 7
 126 : 16 =    7  Rest: 14    =E
7 : 16 =    0  Rest:  7         = 7

Resultat: 7E7

Binär:

2023 : 2 = 1011  Rest: 1
 1011 : 2 =  505  Rest: 1
  505 : 2 =  252  Rest: 1
  252 : 2 =  126  Rest: 0
126 : 2 =   63  Rest: 0
  63 : 2 =   31  Rest: 1
  31 : 2 =   15  Rest: 1
   15 : 2 =    7  Rest: 1
   7 : 2 =    3  Rest: 1
3 : 2 =    1  Rest: 1
1 : 2 =    0  Rest: 1

Resultat: 11111100111


b) Bestimme den Dezimalwert von 7B (Hexadezimal).

B:  11 ·   1 =   11
 7:   7 ·  16 =  112
 11+112 = 123



c) Wandle die Binärzahl 11010101 in Hexadezimal um (Tipp: In 4er-Gruppen
aufteilen).

4stellen = 4 Bit   

1101                                                            
1 · 1 =  1                           
0 · 2 =  0
1 · 4 =  4
1 · 8 =  8

= 13 

0101

1 · 1 =  1
 0 · 2 =  0
 1 · 4 =  4
 1 · 8 =  8

=5


13=D
5=5

Resultat : D5
