---
created: 1970-01-01T01:00
updated: 2025-02-21T10:21
---
Hier findet ihr den Python code vom Vormittag des 14.02.2025

program.py
```python
# check - c -> // f -> c
# check - "Beenden"
# check - Nutzer fragen 
# check - Eingaben vom Nutzer
#fahrenheit = (celsius * 9/5) + 32
#celsius = (fahrenheit - 32) * 5/9


# check - Menü ausgeben
# check - Nutzerentscheidung
# check - Entscheidung einlesen
# check - Jeweiligen Code ausführen
# check - zurück ins Menü

# Hier wird ein Menü ins Terminal ausgegeben
# Das Ganze über Print-Funktionen
def menu():
    print("\nWas möchtest du tun?")
    print("1) Celsius in Fahrenheit umrechnen")
    print("2) Fahrenheit in Celsius umrechnen")
    print("3) Programm beenden")

# Diese Funktion macht die Umrechnung
# Sie wird ohne Werte aufgerufen
# Die Werte werden in der ersten Zeile mit der Input-Funktion eingelesen
# Die Funktion berechnet und gibt den neuen Wert aus
def fahrenheit_in_celsius():
    eingabe_fahrenheit = input("\nBitte nenne mir einen fahrenheit wert: ")
    eingabe_fahrenheit_int = int(eingabe_fahrenheit)
    celsius = (eingabe_fahrenheit_int - 32) * 5/9
    print("Der wert in celsius ist: ") 
    print(celsius)    

# Siehe Funktion oben 
def celsius_in_fahrenheit():
    eingabe_celsius = input("\nBitte nenne mir einen Celsius wert: ")
    eingabe_celsius_int = float(eingabe_celsius)
    fahrenheit = (eingabe_celsius_int * 9/5) + 32
    print("Der wert in fahrenheit ist: ")
    print(fahrenheit)

# while True ist eine Endlosschleife
# Es wird so lange der Code im "Körper" der Schleife ausgeführt,
# bis es zum break kommt 
while True:
    menu()
    auswahl = input("Deine Auswahl bitte: ")
    if auswahl == "1":
        print("Jetzt wird Celsius in Fahrenheit umgerechnet")
        celsius_in_fahrenheit()
    if auswahl == "2":
        print("Jetzt wird Fahrenheit in Celsius umgerechnet")
        fahrenheit_in_celsius()             
    if auswahl == "3":
        print("\nDanke das Sie unsere Software nutzen. Schönen Tag noch.")
        break
    else:
        # Falls die Eingabe nicht 1, 2 oder 3 ist, kommen wir in die Else-Verzweigung
        print("\nBitte richtig lesen, und nur etwas von 1-3 eingeben")

```


program2.py
```python
def menu():
    print("\nWas möchtest du tun?")
    print("1) Celsius in Fahrenheit umrechnen")
    print("2) Fahrenheit in Celsius umrechnen")
    print("3) Programm beenden")

# Diese Funktion macht die Umrechnung
# Sie wird ohne Werte aufgerufen
# Die Werte werden in der ersten Zeile mit der Input-Funktion eingelesen
# Die Funktion berechnet und gibt den neuen Wert aus
def fahrenheit_in_celsius():
    try:
        eingabe_fahrenheit = input("\nBitte nenne mir einen fahrenheit wert: ")
        eingabe_fahrenheit_int = int(eingabe_fahrenheit) # Hier wird der String, welcher zuvor eingelesen wurde, in einen int umgewandelt - da wir nur damit rechnen können
        celsius = (eingabe_fahrenheit_int - 32) * 5/9
        print("Der wert in celsius ist: ") 
        print(celsius)
    except:
        print("Bitte gebt mir doch eine richtige Zahl")
        fahrenheit_in_celsius()    

def celsius_in_fahrenheit():
    # Falls es innerhalb des try-Blocks zu einem Python-Fehler kommt,
    # wird der Code im except-Block ausgeführt
    try:
        eingabe_celsius = input("\nBitte nenne mir einen Celsius wert: ")
        eingabe_celsius_int = float(eingabe_celsius)
        fahrenheit = (eingabe_celsius_int * 9/5) + 32
        print("Der wert in fahrenheit ist: ")
        print(fahrenheit)
    except:
        print("Bitte gebt mir doch eine richtige Zahl")
        celsius_in_fahrenheit() # Hier wird in der Fehlerbehandlung am Ende nochmal die Funktion aufgerufen, damit der Nutzer die Chance hat, nochmal den Code einzugeben


# while True ist eine Endlosschleife
# Es wird so lange der Code im "Körper" der Schleife ausgeführt,
# bis es zum break kommt 
while True:
    menu()
    auswahl = input("Deine Auswahl bitte: ")
    if auswahl == "1":
        print("Jetzt wird Celsius in Fahrenheit umgerechnet")
        celsius_in_fahrenheit()
    if auswahl == "2":
        print("Jetzt wird Fahrenheit in Celsius umgerechnet")
        fahrenheit_in_celsius()             
    if auswahl == "3":
        print("\nDanke das Sie unsere Software nutzen. Schönen Tag noch.")
        break
    else:
        # Falls die Eingabe nicht 1, 2 oder 3 ist, kommen wir in die else-Verzweigung
        print("\nBitte richtig lesen, und nur etwas von 1-3 eingeben")

```


try-except
```python
  try:
    eingabe = int(input("Bitte nenne mir eine Zahl: "))
    print("Deine Zahl war die: ")
    print(eingabe)
except:
    print("Nutzer, du bist doof, bitte nenne mir doch eine Zahl")

```

funktion.py
```python
#Diese Funktion nimmt einen Wert entgegen und gibt ihn via print aus
def funktion_zwei(eingabe):
    print("Die eingabe lautet: ")
    print(eingabe)

#Diese Funktion nimmt einen Wert entgegen, verdoppelt ihn und gibt ihn dann zurück    
def verdoppel(eingabe):
    doppel = eingabe * 2
    return doppel

#Diese Funktion nimmt einen Wert entgegen, verdoppelt ihn und gibt das Ergebnis via print aus
def alles_auf_einmal(input):
    ausgabe = input * 2
    print("Deine Ausgabe lautet: ")
    print(ausgabe)    


wert = int(input("Bitte nenne mir einen Wert: "))
zwischen = wert * 2
funktion_zwei(zwischen)


print("Diese Ausgabe ist das Resultat von der alles_auf_einmal_funktion")
alles_auf_einmal(wert)


print("Diese Ausgabe ist das Resultat von einem doppeltem funktionsaufruf")
funktion_zwei(verdoppel(wert))
```