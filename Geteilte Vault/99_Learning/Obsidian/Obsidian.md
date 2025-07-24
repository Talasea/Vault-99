---
created: 2024-11-11T10:57
updated: 2024-11-17T20:30
---
[[Markdown-Syntax]]

# Ordnerstruktur
## 01_Journal

**Tagesnotizen** landen im Ordner `01_Journal/2024/Tagesnotizen`
(Konfigurierbar über `Einstellungen > Tägliche Notizen > Neuer Dateispeicherort`)

**Wochennotizen** (wenn erstellt über `Calendar` Plugin) landen im Ordner `01_Journal/2024/Wochennotizen`
(Konfigurierbar über `Calendar` Plugin in `Einstellungen > Calendar > Weekly note folder`)

## 02_Medien

**Screenshots** landen im Ordner `02_Medien/Bilder/Screenshots`
(Konfigurierbar über `Einstellungen > Dateien & Links > Standardordner für neue Anhänge`)

**Excalidraw** Dateien liegen im Ordner `02_Medien/Excalidraw`
(Konfigurierbar über `Excalidraw` Plugin in `Einstellungen > Excalidraw > BASIC > Excalidraw folder`)

## 99_Learning
### Templates

**Templates** liegen im Ordner `99_Learning/Obsidian/Templates`
(Konfigurierbar über `Templater` Plugin in `Einstellungen > Templater > Template folder location`)
**Template Skripte** liegen im Ordner `99_Learning/Obsidian/Templates/Skripte`
(Konfigurierbar über `Templater` Plugin in `Einstellungen > Templater > Script files folder location`)


# Konfiguration
## Individualiserung mit CSS
Mit einfachen CSS Codeschnippseln kann die Erscheinung und das Verhalten von Obisidan angepasst werden.

`Einstellungen -> Darstellung -> (ganz unten) CSS-Bausteine`

## Templates erstellen
Wir brauchen das zusätzlich Plugin `Templater`

1. Plugin `Templater` installieren
2. Ordner für unsere Templates anlegen
3. Definieren Templates
4. [optional] Wenn `Update time on edit` Plugin aktiv, Ausnahme für den Template Ordner hinzufügen
5. [Für Umschalter] Einen Ordner `Skripte` im Ordner `99_Templates` erstellen
6. [Für Umschalter] In `Templater` den Skript-Ordner definieren
7. [Für Umschalter] Das `getRelativeDay.js` Skript in den Ordner `Skripte` kopieren

# Plugins
* `Templater` um Templates zu verwenden
* `Excalidraw` um optisch ansprechende Diagramme zu erstellen
* `Dataview` um statistische Daten zu erfassen