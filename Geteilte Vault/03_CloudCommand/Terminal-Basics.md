---
created: 2024-11-07T09:32
updated: 2024-11-15T11:38
---
# Grundlagen

Das Dateisystem navigieren (Ordner wechseln)

```bash
cd Desktop # in den Ordner Desktop wechseln
cd .. # einen Ordner "nach oben"
```

Inhalte in Ordnern anzeigen

```bash
ls # zeigt mir den Inhalt des aktuellen Ordners
ls Desktop # zeigt mir den Inhalt des Desktops (Desktop muss erreichbar sein)
```

# Wichtige Pfade

```bash
.  # signalisiert den aktuellen Ordner
.. # signalisieren den Ordner eine Ebene weiter oben
~/ # signalisiert den Homeordner des Benutzers
```

# Wichtige Funktionen

```bash
TAB # vervollständigt den Befehl oder Pfad
SHIFT + TAB # wechselt zum vorherigen Befehl
STRG + C # Aktuellen Prozess im Terminal zu beenden
PFEILTASTE HOCH # vorherigen Terminalefehl auswählen
PFEILTASTE RUNTER # nachfolgenden Terminalefehl auswählen
```

# Sonderzeichen

Asterisk/Malzeichen

```bash
* # Asterisk - oft ein Platzhalter für eine beliebige Zeichenkette
mv 2024-1* Tagesnotizen # Jede Datei die mit 2024-1 beginnt wird in den Ornder Tagesnotizen verschoben
```

Pipe
```bash
# Ausgabe von commando1 wird als Eingabe für commando2 verwendet
commando1 | commando2
```