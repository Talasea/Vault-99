---
created: 1970-01-01T01:00
updated: 2025-03-07T16:05
---
Hier findet ihr den Code zu der main.py also der Hauptdatei, und weiter unten den Code der verwaltung.py 

Falls ihr teile des Codes nicht mehr Nachvollziehen könnt, macht euch Notizen dazu und fragt uns dazu. 

##### main.py

```python
# Wir möchten sehen welche Bücher wir gespeicher haben
# Bücher hinzufügen
# Das ganze mit Autor
# Bücher sollen gelöscht werden können
# Wir möchten das ganze auf zwei datei verteilen

# 1) Datei 1 soll mir Sachen anzeigen und auf meine Eingaben reagieren   -- 1_Benutzerinteraktion
# 2) Datei 2 soll die funktionen haben welche die Bücher verwaltet       -- 2_Bücherverwaltung 


#Statisch im programm hinzugefügt - man nennt das hardcoded
#bücher_hinzufügen("Herr der Ringe")
#bücher_hinzufügen("Der Hobbit")
#bücher_hinzufügen("1984")

#Wärend der Laufzeit - dynamisch hinzugefügt 
#eingabe = input("Bitte nenne das Buch\n")
#bücher_hinzufügen(eingabe)

#Frage nach dem Buch das gelöscht werden soll
#eingabe_2 = input("Welches Buch soll gelöscht werden?\n")
#bücher_löschen(eingabe_2)

#bücher_auflisten()

from verwaltung import *

benutzer = "Ahmed"
print(f"Willkommen, {benutzer}")


#Das brauchen wir für die endloss Schleife
while True:
    print("Was möchtest du tun?\n")
    print("Optionen:")
    print("1: Bücher hinzufügen")
    print("2: Bücher löschen")
    print("3: Bücher auflisten")
    print("4: Anzahl der Bücher")
    auswahl = input("\nBitte nenne deine Auswahl\n")

    if auswahl == "1":
        buch_eingabe_hinzufügen = input("Bitte nenne das Buch das hinzugefügt werden soll\n")
        bücher_hinzufügen(buch_eingabe_hinzufügen)
    elif auswahl == "2":
        buch_eingabe_löschen = input("Bitte nenne das Buch welches du löschen willst\n")
        bücher_löschen(buch_eingabe_löschen)
    elif auswahl == "3":
        bücher_auflisten()
    elif auswahl == "4":
        print(f"Die Anzahl der Bücher beträgt {anzahl_der_bücher_funktion()}")
    else:
        print("\nBitte richtig lesen, und nur etwas zwischen 1-3 eingeben")   
```


###### verwaltung.py
```python
# Hier werde ich die Bücher verwalten
bücher = []
anzahl_der_bücher = int(0)

def bücher_hinzufügen(buch):
    bücher.append(buch)
    print(f"Das Buch {buch} wurde hinzugefügt.")
    global anzahl_der_bücher
    anzahl_der_bücher = anzahl_der_bücher + 1
    # Wir haben das genutz um zu sehen ob der Fehler schon hier war
    #print(f"testwert {anzahl_der_bücher}")

def bücher_auflisten():
    print("Das sind unsere Bücher")
    print(bücher)

def bücher_löschen(buch):
    try:
        bücher.remove(buch)
        print(f"Das Buch {buch} wurde gelöscht.")
        global anzahl_der_bücher
        anzahl_der_bücher = anzahl_der_bücher - 1
    except:
        print(f"Das Buch {buch} was du löschen möchtest gibt es nicht")

def anzahl_der_bücher_funktion():
    global anzahl_der_bücher
    return anzahl_der_bücher
```