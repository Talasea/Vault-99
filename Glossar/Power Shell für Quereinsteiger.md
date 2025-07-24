
### Windows PowerShell für IT-Quereinsteiger – Schritt-für-Schritt-Erklärung

Für IT-Quereinsteiger ist die Windows PowerShell ein mächtiges Werkzeug, um Aufgaben zu automatisieren, Systeme zu verwalten und komplexe Probleme zu lösen. Hier wird die PowerShell einfach erklärt, ihre Unterschiede zur klassischen CMD aufgezeigt und die wichtigsten Befehle (Cmdlets) vorgestellt.

---

#### **1. Was ist die Windows PowerShell?**

Die PowerShell ist eine moderne **Skriptsprache und Befehlszeilenshell** von Microsoft. Im Gegensatz zur alten CMD (Command Prompt) basiert sie auf dem .NET-Framework und arbeitet mit **Objekten** statt reinem Text. Das macht sie deutlich flexibler und leistungsfähiger.

**Hauptmerkmale:**

- **Cmdlets** (Befehle) nach dem Schema _Verb-Noun_, z. B. `Get-Process`.
    
- **Objektorientiert**: Ergebnisse sind strukturierte Daten (z. B. Prozesse, Dateien) mit Eigenschaften.
    
- **Skripterstellung**: Automatisierung von Aufgaben durch Skripte (`.ps1`-Dateien).
    
- **Zugriff auf .NET-Bibliotheken**: Erlaubt tiefe Integration in Windows-Systeme.
    

---

#### **2. Unterschiede zwischen PowerShell und CMD**

| **Aspekt**          | **PowerShell**                                  | **CMD**                         |
| ------------------- | ----------------------------------------------- | ------------------------------- |
| **Ausgabe**         | Objekte (z. B. Prozesse mit Name, ID, Speicher) | Reiner Text (nur Zeichenketten) |
| **Befehle**         | Cmdlets (z. B. `Get-ChildItem`)                 | Einfache Befehle (z. B. `dir`)  |
| **Skripte**         | Leistungsstarke `.ps1`-Skripte                  | Einfache `.bat`/`.cmd`-Skripte  |
| **Pipeline**        | Übergabe von **Objekten** zwischen Befehlen     | Übergabe von **Text**           |
| **Erweiterbarkeit** | Integration von .NET und externen Modulen       | Sehr begrenzt                   |

**Beispiel:**

- **CMD:** `dir` zeigt Dateien als Text an.
    
- **PowerShell:** `Get-ChildItem` liefert Datei-**Objekte** mit Eigenschaften wie Name, Größe oder Erstellungsdatum.
    

---

#### **3. Die wichtigsten Cmdlets für den Einstieg**

PowerShell-Cmdlets folgen immer dem Muster **`Verb-Noun`** (z. B. `Get-Help`). Hier die wichtigsten Befehle:

##### **Grundlegende Cmdlets**

1. **`Get-Command`**
    
    - Listet alle verfügbaren Cmdlets auf.
        
    - _Beispiel:_ `Get-Command *-Service` findet alle Befehle zum Thema „Dienste“.
        
2. **`Get-Help`**
    
    - Zeigt Hilfe zu einem Cmdlet an.
        
    - _Beispiel:_ `Get-Help Get-Process -Examples` erklärt `Get-Process` mit Beispielen.
        
3. **`Get-Process`**
    
    - Listet alle laufenden Prozesse auf (wie der Task-Manager).
        
    - _Beispiel:_ `Get-Process -Name "chrome"` zeigt alle Chrome-Prozesse.
        
4. **`Get-Service`**
    
    - Zeigt alle Windows-Dienste an (z. B. Druckerdienste).
        
    - _Beispiel:_ `Get-Service -Name "Spooler"` prüft den Druckerdienst.
        

##### **Dateiverwaltung**

5. **`Get-ChildItem`**
    
    - Listet Ordnerinhalte auf (Ersatz für `dir` in CMD).
        
    - _Beispiel:_ `Get-ChildItem C:\ -Recurse` durchsucht das Laufwerk C: rekursiv.
        
6. **`New-Item`**, **`Remove-Item`**, **`Copy-Item`**
    
    - Erstellt, löscht oder kopiert Dateien/Ordner.
        
    - _Beispiel:_ `New-Item -Path "C:\Test" -ItemType Directory` legt einen Ordner an.
        

##### **Systemsteuerung**

7. **`Start-Service`** / **`Stop-Service`**
    
    - Startet oder stoppt Dienste.
        
    - _Beispiel:_ `Stop-Service -Name "Spooler"` hält den Druckerdienst an.
        
8. **`Set-ExecutionPolicy`**
    
    - Erlaubt das Ausführen von Skripten (Standard: blockiert).
        
    - _Beispiel:_ `Set-ExecutionPolicy RemoteSigned` aktiviert Skripte nach Bestätigung.
        

##### **Filter und Pipelines**

9. **`Where-Object`**
    
    - Filtert Objekte nach Eigenschaften.
        
    - _Beispiel:_ `Get-Process | Where-Object { $_.CPU -gt 50 }` zeigt Prozesse mit >50% CPU.
        
10. **`Select-Object`**
    
    - Wählt bestimmte Eigenschaften aus.
        
    - _Beispiel:_ `Get-Process | Select-Object Name, CPU` zeigt nur Name und CPU.
        

---

#### **4. Praxisbeispiel: PowerShell vs. CMD**

**Aufgabe:** Alle Textdateien im Ordner „Dokumente“ auflisten, die größer als 1 MB sind.

- **CMD:**
    
    cmd
    
    Copy
    
    dir C:\Users\Benutzer\Dokumente\*.txt | find "MB"  
    
    _Problem:_ Die Ausgabe ist ungenau, da `find` nur nach dem Text „MB“ sucht.
    
- **PowerShell:**
    
    powershell
    
    Copy
    
    Get-ChildItem -Path "C:\Users\Benutzer\Dokumente\*.txt" | Where-Object { $_.Length -gt 1MB }  
    
    _Vorteil:_ `$_.Length` nutzt die **objektbasierte** Eigenschaft „Größe“ für exakte Filterung.
    

---

#### **5. Tipps für den Einstieg**

- **Skripte ausführen:**  
    Starte PowerShell als Administrator und aktiviere `Set-ExecutionPolicy RemoteSigned`.
    
- **Aliase nutzen:**  
    Viele CMD-Befehle funktionieren als Alias (z. B. `dir` = `Get-ChildItem`).
    
- **Lernen mit `Get-Help`:**  
    Nutze `Get-Help <Cmdlet> -Online`, um die offizielle Dokumentation zu öffnen.
    

---

### **Warum lohnt sich die PowerShell?**

- **Automatisierung:** Wiederkehrende Aufgaben (z. B. Backups, Berichte) lassen sich in Skripten automatisieren.
    
- **Remote-Verwaltung:** Mit `Enter-PSSession` kann man andere Rechner fernsteuern.
    
- **Cloud-Integration:** Ideal für Azure, Office 365 oder AWS (via Module).
    

Mit der PowerShell hast du ein **Schweizer Taschenmesser** für die IT-Administration – mächtiger als die CMD und unverzichtbar für moderne Windows-Systeme! 🚀






### **Daten in der PowerShell filtern – Schritt-für-Schritt-Erklärung**

In der PowerShell kannst du Daten gezielt **filtern**, **sortieren** oder **auswählen**, um nur die Informationen zu erhalten, die du benötigst. Dies ist möglich, weil die PowerShell mit **Objekten** arbeitet, die strukturierte Eigenschaften (z. B. Name, Größe, Status) besitzen. Hier lernst du die wichtigsten Methoden für Quereinsteiger.

---

### **1. Grundprinzip: Die Pipeline und Objekte**

PowerShell-Befehle (Cmdlets) sind über die **Pipeline** (`|`) miteinander verbunden. Dabei werden **Objekte** (z. B. Dateien, Prozesse) von einem Befehl zum nächsten weitergegeben.

- **Beispiel:**
    
    powershell
    
    Copy
    
    Get-Process | Where-Object { $_.CPU -gt 50 }
    
    - `Get-Process` liefert alle Prozesse als Objekte.
        
    - `Where-Object` filtert die Objekte, bei denen die CPU-Auslastung über 50% liegt.
        

---

### **2. Filterung mit `Where-Object`**

`Where-Object` ist das wichtigste Cmdlet zum Filtern. Es prüft jedes Objekt in der Pipeline nach einer Bedingung.

#### **Syntax:**

powershell

Copy

Get-Objekt | Where-Object { $_.Eigenschaft -Operator Wert }

- `$_` steht für das aktuelle Objekt in der Pipeline.
    
- **Vergleichsoperatoren:**  
    `-eq` (gleich), `-ne` (ungleich), `-gt` (größer als), `-lt` (kleiner als), `-like` (Wildcards: `*`), `-match` (Reguläre Ausdrücke).
    

#### **Beispiele:**

1. **Prozesse filtern:**
    
    powershell
    
    Copy
    
    Get-Process | Where-Object { $_.Name -eq "chrome" }  # Nur Chrome-Prozesse
    
2. **Dateien nach Größe filtern:**
    
    powershell
    
    Copy
    
    Get-ChildItem -Path "C:\Docs\" | Where-Object { $_.Length -gt 1MB }  # Dateien >1 MB
    
3. **Dienste nach Status filtern:**
    
    powershell
    
    Copy
    
    Get-Service | Where-Object { $_.Status -eq "Running" }  # Nur laufende Dienste
    

---

### **3. Auswahl von Eigenschaften mit `Select-Object`**

Mit `Select-Object` wählst du gezielt Eigenschaften aus oder begrenzt die Anzahl der Ergebnisse.

#### **Syntax:**

powershell

Copy

Get-Objekt | Select-Object Eigenschaft1, Eigenschaft2, ...

#### **Beispiele:**

1. **Bestimmte Eigenschaften anzeigen:**
    
    powershell
    
    Copy
    
    Get-Process | Select-Object Name, CPU, Id  # Zeigt nur Name, CPU und Prozess-ID
    
2. **Erste 5 Ergebnisse begrenzen:**
    
    powershell
    
    Copy
    
    Get-ChildItem | Select-Object -First 5  # Nur die ersten 5 Dateien/Ordner
    

---

### **4. Filterung direkt im Cmdlet-Parameter**

Viele Cmdlets haben eingebaute Filterparameter, um Ergebnisse **frühzeitig** zu begrenzen (schneller als `Where-Object`).

#### **Beispiele:**

1. **Dateien nach Namen filtern:**
    
    powershell
    
    Copy
    
    Get-ChildItem -Path "C:\Logs\" -Filter "*.log"  # Nur .log-Dateien
    
2. **Prozesse nach Name filtern:**
    
    powershell
    
    Copy
    
    Get-Process -Name "explorer"  # Nur Explorer-Prozesse
    

---

### **5. Erweiterte Filterung mit logischen Operatoren**

Du kannst mehrere Bedingungen mit `-and`, `-or` oder `-not` kombinieren.

#### **Beispiel:**

powershell

Copy

Get-ChildItem | Where-Object { 
    $_.Name -like "*.txt" -and $_.LastWriteTime -gt (Get-Date).AddDays(-7) 
}

- Zeigt alle `.txt`-Dateien, die in den letzten 7 Tagen bearbeitet wurden.
    

---

### **6. Sortieren mit `Sort-Object`**

Daten lassen sich nach einer Eigenschaft auf- oder absteigend sortieren.

#### **Beispiel:**

powershell

Copy

Get-Process | Sort-Object CPU -Descending  # Sortiert Prozesse nach CPU-Auslastung (absteigend)

---

### **7. Gruppieren mit `Group-Object`**

Gruppiere Objekte nach einer gemeinsamen Eigenschaft.

#### **Beispiel:**

powershell

Copy

Get-ChildItem | Group-Object Extension  # Gruppiert Dateien nach Endung (z. B. .txt, .exe)

---

### **8. Tipps für Quereinsteiger**

1. **Eigenschaften herausfinden:**  
    Nutze `Get-Member`, um verfügbare Eigenschaften eines Objekts anzuzeigen:
    
    powershell
    
    Copy
    
    Get-Process | Get-Member  # Zeigt alle Eigenschaften von Prozess-Objekten
    
2. **Aliase nutzen:**  
    Kurzschreibweisen wie `?` für `Where-Object` oder `%` für `ForEach-Object` sparen Zeit:
    
    powershell
    
    Copy
    
    Get-Process | ? { $_.CPU -gt 50 }  # Gleich wie Where-Object
    
3. **Filter früh anwenden:**  
    Filtere bereits im Cmdlet-Parameter (z. B. `-Name`), um Performance zu verbessern.
    

---

### **Praxisbeispiel: Alles kombiniert**

**Aufgabe:** Finde alle laufenden Dienste, die mit "Win" beginnen, und zeige nur Name und Status an.

powershell

Copy

Get-Service -Name "Win*" | 
    Where-Object { $_.Status -eq "Running" } | 
    Select-Object Name, Status

- **Schritt 1:** `Get-Service -Name "Win*"` holt alle Dienste, deren Name mit "Win" beginnt.
    
- **Schritt 2:** `Where-Object` filtert nur laufende Dienste.
    
- **Schritt 3:** `Select-Object` zeigt Name und Status an.
    

---

### **Zusammenfassung: Wichtige Cmdlets und Operatoren**

|**Cmdlet**|**Zweck**|**Beispiel**|
|---|---|---|
|`Where-Object`|Filtert Objekte nach Bedingungen|`Get-Process \| ? { $_.CPU -gt 50 }`|
|`Select-Object`|Wählt Eigenschaften aus|`Get-Process \| Select Name, Id`|
|`Sort-Object`|Sortiert Objekte|`Get-Process \| Sort CPU -Descending`|
|`Group-Object`|Gruppiert Objekte|`Get-ChildItem \| Group Extension`|
|**Operator**|**Zweck**|**Beispiel**|
|`-eq`, `-ne`|Gleich/Ungleich|`$_.Name -eq "explorer"`|
|`-gt`, `-lt`|Größer/Kleiner als|`$_.Size -gt 1MB`|
|`-like`, `-match`|Wildcards/Reguläre Ausdrücke|`$_.Name -like "*.log"`|

Mit diesen Methoden kannst du **präzise Daten filtern** und genau die Informationen extrahieren, die du brauchst – ob für die Fehlersuche, Berichte oder Automatisierung! 🛠️

https://www.stationx.net/powershell-cheat-sheet/



|                     |                                                                                     |
| ------------------- | ----------------------------------------------------------------------------------- |
| **Befehl**          | **Beschreibung**                                                                    |
| Get-Service         | Abrufen von Informationen über Dienste                                              |
| Get-Process         | Abrufen von Informationen über Prozesse                                             |
| Get-EventLog        | Abrufen von Informationen aus Ereignisprotokollen                                   |
| Set-ExecutionPolicy | Änderung der Richtlinie für die Skriptausführung                                    |
| Test-Connection     | Test der Konnektivität zu einem entfernten Computer                                 |
| Out-File            | Schreiben der PowerShell-Ausgabe in eine Datei                                      |
| Get-Help            | Anzeige der Informationen über Konzepte und Befehle                                 |
| Get-History         | Abrufen der letzten Befehle in der aktuellen Sitzung                                |
| Get-Command         | Abrufen aller verfügbaren PowerShell-Befehle                                        |
| ConvertTo-HTML      | Erstellung einer HTML-Datei aus der PowerShell-Ausgabe                              |
| Copy-Item           | Kopieren einer Datei an einen bestimmten Ort                                        |
| Clear-History       | Löschung der Einträge aus dem Befehlsverlauf                                        |
| Add-History         | Hinzufügen der Einträge zum Befehlsverlauf                                          |
| Format-Table        | Formatierung der PowerShell-Ausgabe als Tabelle                                     |
| Format-List         | Formatierung der PowerShell-Ausgabe als Liste                                       |
| Clear-Content       | Beibehaltung eines Elements, obwohl dessen Inhalt gelöscht wird.                    |
| Checkpoint-Computer | Einrichtung eines Wiederherstellungs-Punktes auf Ihrem Rechner                      |
| ForEach-Object      | Ausführung einer Operation für jedes Element in einer bestimmten Gruppe             |
| Where-Object        | Auswahl von Objekten mit einer bestimmten Eigenschaft                               |
| Select-Object       | Auswahl von bestimmten Eigenschaften eines Objekts oder einer Gruppe von Objekten   |
| Out-File            | Erstellung einer lokalen Datei zum Speichern der Cmdlet-Ausgabe                     |
| Write-Progress      | Anzeigen einer Fortschrittsleiste in einem PowerShell-Fenster                       |
| Debug-Process       | Anhängen eines Debuggers an einen laufenden Prozess                                 |
| Get-WinEvent        | Anzeigen von Windows-Ereignisprotokollen                                            |
| Wait-Job            | Unterdrückung der Eingabeaufforderung, bis die Hintergrund-Jobs abgeschlossen sind. |



Wildcard in PowerShell

In PowerShell können Wildcards verwendet werden, um Muster in Befehlen zu erstellen. Diese Platzhalterzeichen helfen dabei, bestimmte Dateien oder Ordner basierend auf einem Muster zu finden oder zu bearbeiten. Die wichtigsten Wildcard-Zeichen sind:

- Das Sternchen (*) repräsentiert null oder mehr Zeichen. Es kann verwendet werden, um alle Dateien oder Ordner zu finden, die eine bestimmte Endung haben, z.B. `Get-ChildItem C:\Techdocs\*.ppt`.
    
- Das Fragezeichen (?) repräsentiert ein einzelnes Zeichen. Es kann verwendet werden, wenn man einige, aber nicht alle Zeichen kennt, z.B. `Get-ChildItem file?.doc`.
    

Wildcards können auch in Kombination mit dem `-like` Operator verwendet werden, um Muster zu vergleichen. Zum Beispiel kann man mit `Get-Process *word*` alle Prozesse finden, deren Namen das Wort "word" enthalten.

Es ist wichtig zu beachten, dass Wildcards in verschiedenen Kontexten unterschiedlich funktionieren können. Wenn Sie Wildcards in Befehlen verwenden, die sie nicht direkt unterstützen, können unerwartete Ergebnisse auftreten. In solchen Fällen können Sie Wildcards mit dem `Where-Object` Cmdlet kombinieren, um die gewünschten Muster zu filtern, z.B. `Get-Process | where { $_.Id -like '76*' }`.

Wildcards sind ein effizientes Werkzeug zur Suche und Filterung in PowerShell, ermöglichen aber auch das Risiko, dass mehr Dateien oder Ordner gelöscht werden, als beabsichtigt. Daher ist es ratsam, vor dem Ausführen von Löschbefehlen die Option `-WhatIf` zu verwenden, um eine Vorschau der Aktionen zu erhalten.


In PowerShell, if you want to use a wildcard character without it being interpreted as a wildcard, you can escape it using the backtick (`) character. For example, if you want to match a literal asterisk (*) or question mark (?), you would use` * or `? respectively. This allows you to treat the wildcard characters as literal characters in your strings.

Here's an example of how to escape a square bracket for a wildcard comparison:

```
$One = "Found problem users: []"
$Two = "Log: Found problem users: []"
$Two -like "*$($One.Replace('[', '`[').Replace(']', '`]'))*"
```

In this example, the square brackets are escaped so that they are treated as literal characters rather than as wildcard characters.




### **PowerShell-Funktionen & Skripte für Quereinsteiger – Schritt-für-Schritt-Erklärung**

Funktionen und Skripte sind essenziell, um Code wiederzuverwenden, Aufgaben zu automatisieren und komplexe Abläufe zu strukturieren. Hier lernst du, wie du Funktionen erstellst, Skripte schreibst und welche Regeln zu beachten sind.

---

### **1. Was sind Funktionen?**

Eine **Funktion** ist ein wiederverwendbarer Codeblock, der eine bestimmte Aufgabe erledigt (z. B. Dateien kopieren, Dienste prüfen). Funktionen machen Code übersichtlicher und sparen Zeit.

#### **Einfachstes Beispiel:**

powershell

Copy

# Funktion ohne Parameter
function Begrüßung {
    Write-Output "Hallo, willkommen in der PowerShell!"
}

# Funktion aufrufen
Begrüßung

---

### **2. Funktionen erstellen – Syntax & Regeln**

#### **Grundgerüst einer Funktion:**

powershell

Copy

function <Name> {
    [CmdletBinding()]  # Optional: Ermöglicht erweiterte Parameter
    param (
        # Parameter definieren (optional)
        [Parameter(Mandatory=$true)]
        [string]$Name
    )
    # Codeblock
    Write-Output "Hallo, $Name!"
}

#### **Wichtige Regeln:**

- **Namen:** Verwende klare Namen nach dem Schema _Verb-Noun_ (z. B. `Get-DiskSpace`).
    
- **Parameter:** Definiere Parameter mit Datentypen (z. B. `[string]`, `[int]`).
    
- **Ausgabe:** Nutze `return` oder `Write-Output` für Ergebnisse. Vermeide direkte Ausgaben (wie `Write-Host`) in Funktionen.
    
- **Gültigkeitsbereich (Scope):** Variablen in Funktionen sind standardmäßig **lokal** (nicht außerhalb sichtbar).
    

---

### **3. Funktion mit Parametern – Beispiel**

powershell

Copy

function Get-DiskInfo {
    [CmdletBinding()]
    param (
        [Parameter(Mandatory=$true)]
        [string]$Laufwerk
    )
    # Codeblock
    $info = Get-Volume -DriveLetter $Laufwerk
    return $info.SizeRemaining / 1GB  # Größe in GB
}

# Aufruf mit Parameter
Get-DiskInfo -Laufwerk "C"

---

### **4. Skripte erstellen – Schritt für Schritt**

Ein **Skript** ist eine Sammlung von Befehlen in einer `.ps1`-Datei.

#### **Schritte:**

1. **Code schreiben:** In einem Editor (z. B. VS Code, Notepad).
    
2. **Speichern:** Als `.ps1`-Datei (z. B. `mein_skript.ps1`).
    
3. **Ausführen:**
    
    powershell
    
    Copy
    
    .\mein_skript.ps1
    

#### **Beispiel-Skript:**

powershell

Copy

# Skript: Service-Prüfung
function Test-ServiceStatus {
    param ([string]$ServiceName)
    $service = Get-Service -Name $ServiceName
    return $service.Status
}

# Funktion aufrufen
$status = Test-ServiceStatus -ServiceName "Spooler"
Write-Output "Druckerdienst-Status: $status"

---

### **5. Wichtige Regeln für Funktionen**

#### **A. Parameter-Validierung**

Sichere Eingaben mit Validierungsattributen:

powershell

Copy

param (
    [ValidateSet("Running", "Stopped")]  # Nur erlaubte Werte
    [string]$Status,

    [ValidateRange(1, 100)]  # Zahlen zwischen 1 und 100
    [int]$Prozent
)

#### **B. Pipeline-Eingabe**

Funktionen können Pipeline-Daten verarbeiten:

powershell

Copy

function Get-BigFiles {
    param (
        [Parameter(ValueFromPipeline=$true)]
        [string]$Pfad
    )
    process {
        Get-ChildItem $Pfad | Where-Object { $_.Length -gt 1MB }
    }
}

# Pipeline-Nutzung
"C:\", "D:\" | Get-BigFiles

#### **C. Hilfe-Kommentare**

Erkläre die Funktion mit Kommentaren:

powershell

Copy

<#
.SYNOPSIS
    Überprüft den Status eines Dienstes.
.DESCRIPTION
    Gibt "Running" oder "Stopped" zurück.
.PARAMETER ServiceName
    Name des Dienstes (z. B. "Spooler").
#>
function Test-ServiceStatus { ... }

---

### **6. Typische Funktionen für Administratoren**

#### **A. Dienst neu starten**

powershell

Copy

function Restart-ServiceSafe {
    param ([string]$ServiceName)
    $service = Get-Service -Name $ServiceName
    if ($service.Status -ne "Running") {
        Start-Service -Name $ServiceName
    } else {
        Restart-Service -Name $ServiceName
    }
}

#### **B. Dateien älter als X Tage löschen**

powershell

Copy

function Remove-OldFiles {
    param (
        [string]$Ordner,
        [int]$Tage
    )
    $limit = (Get-Date).AddDays(-$Tage)
    Get-ChildItem $Ordner | Where-Object { $_.LastWriteTime -lt $limit } | Remove-Item
}

#### **C. Netzwerk-Ping-Test**

powershell

Copy

function Test-NetworkHosts {
    param ([string[]]$IPs)
    foreach ($ip in $IPs) {
        $result = Test-NetConnection -ComputerName $ip
        [PSCustomObject]@{
            IP = $ip
            Pingable = $result.PingSucceeded
        }
    }
}

# Aufruf
Test-NetworkHosts -IPs "192.168.1.1", "192.168.1.10"

---

### **7. Häufige Fehler & Lösungen**

|**Fehler**|**Lösung**|
|---|---|
|**Parameter nicht erkannt**|Prüfe, ob `param()` korrekt definiert ist und der Parameter im Aufruf steht.|
|**Zugriff auf globale Variablen**|Nutze `$global:Variablenname` oder vermeide globale Variablen in Funktionen.|
|**Skript läuft nicht**|Starte PowerShell als Admin und setze `Set-ExecutionPolicy RemoteSigned`.|
|**Keine Ausgabe**|Füge `return` oder `Write-Output` hinzu – Funktionen geben sonst nichts zurück.|

---

### **Syntax-Zusammenfassung**

- **Funktion definieren:**
    
    powershell
    
    Copy
    
    function <Name> { param(...) ... } 
    
- **Parameter:**
    
    powershell
    
    Copy
    
    param ([Datentyp]$Parametername)  
    
- **Pipeline-Eingabe:**
    
    powershell
    
    Copy
    
    [Parameter(ValueFromPipeline=$true)]  
    
- **Ausgabe:**  
    `return` oder `Write-Output` verwenden.
    

---

### **Tipps für den Alltag**

1. **Teste Funktionen schrittweise:** Baue Code erst in der Konsole, bevor du ihn in eine Funktion packst.
    
2. **Logging:** Nutze `Write-Verbose` oder `Write-Debug` für Diagnoseausgaben.
    
3. **Module:** Packe oft genutzte Funktionen in Module (`.psm1`-Dateien).
    

Mit Funktionen und Skripten kannst du **Wiederholungen vermeiden** und komplexe Tasks automatisieren – ein Muss für jeden Admin! 🚀






####  **Sicherheit** 

Um PowerShell-Skripte auszuführen, muss man sicherstellen, dass die richtigen Sicherheitsrichtlinien auf deinem Computer konfiguriert sind. In Windows gibt es eine Einstellung namens **Execution Policy**, die bestimmt, wie und ob PowerShell-Skripte ausgeführt werden können. Ich erkläre dir Schritt für Schritt, was du tun musst:

### 1. **Überprüfen der aktuellen Execution Policy**

Zuerst müssen wir herausfinden, welche **Execution Policy** derzeit auf deinem Computer festgelegt ist. Dies geht folgendermaßen:

1. Öffne PowerShell. Klicke dazu mit der rechten Maustaste auf das Startmenü und wähle „Windows PowerShell (Administrator)“, um PowerShell mit Administratorrechten zu starten.
    
2. Gib folgenden Befehl ein und drücke Enter:
    
    ```powershell
    Get-ExecutionPolicy
    ```
    
    Dieser Befehl zeigt dir die aktuelle **Execution Policy** an. Es gibt verschiedene Optionen:
    
    - **Restricted**: Hier werden keine Skripte ausgeführt. Das ist die Standard-Einstellung.
    - **RemoteSigned**: Lokale Skripte dürfen ausgeführt werden, aber heruntergeladene Skripte müssen signiert sein.
    - **Unrestricted**: Skripte dürfen ohne Einschränkungen ausgeführt werden.
    - **Bypass**: Keine Einschränkungen, auch keine Warnungen.

### 2. **Ändern der Execution Policy**

Wenn du Skripte ausführen möchtest, musst du die Execution Policy anpassen. Das geht folgendermaßen:

1. In der PowerShell mit Administratorrechten gibst du diesen Befehl ein, um die Execution Policy zu ändern (z.B. auf „RemoteSigned“):
    
    ```powershell
    Set-ExecutionPolicy RemoteSigned
    ```
    
    Du kannst auch eine andere Option wie **Unrestricted** wählen, wenn du das möchtest:
    
    ```powershell
    Set-ExecutionPolicy Unrestricted
    ```
    
2. Bestätige mit „Ja“ (Y), wenn die PowerShell fragt, ob du die Änderung vornehmen möchtest.
    

### 3. **Arbeiten mit PowerShell-Skripten**

Nachdem du die Execution Policy angepasst hast, kannst du PowerShell-Skripte ausführen:

1. Öffne PowerShell und navigiere zu dem Ordner, in dem dein Skript gespeichert ist. Zum Beispiel:
    
    ```powershell
    cd "C:\Pfad\zum\Ordner"
    ```
    
2. Um das Skript auszuführen, gib den Namen des Skripts ein (z.B. `meinSkript.ps1`):
    
    ```powershell
    .\meinSkript.ps1
    ```
    

### 4. **Was du beachten musst**

- **Administratorrechte**: Manche Skripte erfordern Administratorrechte, insbesondere wenn sie Änderungen am System vornehmen. Du musst sicherstellen, dass PowerShell mit Administratorrechten ausgeführt wird.
    
- **Sicherheit**: Die **Unrestricted**-Einstellung ermöglicht es dir, alle Skripte auszuführen, was ein Sicherheitsrisiko darstellen kann, wenn du Skripte aus unsicheren Quellen ausführst. Stelle sicher, dass du Skripte nur aus vertrauenswürdigen Quellen ausführst.
    
- **Fehlermeldungen**: Wenn du eine Fehlermeldung bekommst, dass das Skript nicht ausgeführt werden kann, liegt das meist an der Execution Policy oder daran, dass das Skript nicht korrekt geschrieben wurde.
    

### 5. **Weitere Optionen für PowerShell-Skripte**

Wenn du spezielle Funktionen in deinem Skript nutzen möchtest, wie z.B. die Ausführung mit speziellen Rechten oder das Ausführen von Aufgaben im Hintergrund, kannst du verschiedene Parameter verwenden, wie z.B.:

- **Run as Administrator**: Manche Skripte erfordern Administratorrechte. Stelle sicher, dass du PowerShell mit Administratorrechten ausführst.
    
- **ExecutionPolicy für bestimmte Skripte**: Wenn du nur ein bestimmtes Skript ausführen möchtest, ohne die globale Policy zu ändern, kannst du dies direkt beim Ausführen tun:
    
    ```powershell
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    ```
    
    Dieser Befehl ändert die Execution Policy nur für die aktuelle PowerShell-Sitzung und nicht dauerhaft.
    

### Fazit

- Überprüfe die aktuelle Execution Policy mit `Get-ExecutionPolicy`.
- Ändere sie, wenn nötig, mit `Set-ExecutionPolicy` (z.B. auf **RemoteSigned**).
- Achte darauf, dass du PowerShell mit Administratorrechten startest, wenn es erforderlich ist.



### Module


Module in PowerShell sind eine Art von Sammlung von Funktionen, Cmdlets und Skripten, die als Einheit gespeichert sind und dir helfen, spezifische Aufgaben zu erledigen. Sie bieten eine praktische Möglichkeit, Code zu organisieren, wiederzuverwenden und zu erweitern. Ich werde dir Schritt für Schritt erklären, was Module in PowerShell sind, wofür sie verwendet werden und wie du sie nutzt.

### 1. **Was ist ein PowerShell-Modul?**

Ein PowerShell-Modul ist eine Sammlung von PowerShell-Funktionen, Cmdlets (Kommandozeilenbefehlen), Variablen und Skripten, die zusammen in einer Datei oder einem Ordner gespeichert sind. Module ermöglichen es dir, deine PowerShell-Umgebung zu erweitern und mehr Funktionen bereitzustellen, die du für bestimmte Aufgaben verwenden kannst.

Ein Modul kann aus mehreren Dateien bestehen oder nur eine einzelne Datei sein. Wenn du das Modul lädst, hast du Zugriff auf alle darin enthaltenen Funktionen und Cmdlets.

### 2. **Warum sind Module nützlich?**

- **Wiederverwendbarkeit**: Du kannst Code einmal in einem Modul schreiben und dieses Modul dann in verschiedenen PowerShell-Sitzungen oder Skripten wiederverwenden.
- **Organisation**: Module helfen dabei, Code zu strukturieren und zu organisieren, besonders wenn du viele Funktionen oder Skripte hast.
- **Erweiterbarkeit**: Viele PowerShell-Module kommen von Microsoft oder der Community und bieten zusätzliche Funktionen, die du in deinen eigenen Skripten verwenden kannst.

Beispiel: Wenn du mit Azure arbeitest, kannst du das **Az-Modul** verwenden, um Azure-Dienste zu steuern, ohne dass du alle Befehle selbst schreiben musst.

### 3. **Wie ein Modul in PowerShell geladen wird**

Bevor du ein Modul verwenden kannst, musst du es in deine PowerShell-Sitzung laden. Hier sind die Schritte:

#### a) **Modul laden**

Wenn das Modul bereits installiert und verfügbar ist, kannst du es so laden:

powershell

Kopieren

`Import-Module <Modulname>`

Beispiel: Wenn du das **Az**-Modul laden möchtest, um mit Azure zu arbeiten:

powershell

Kopieren

`Import-Module Az`

#### b) **Überprüfen, ob ein Modul verfügbar ist**

Um zu sehen, welche Module in deiner PowerShell-Umgebung installiert sind, kannst du den folgenden Befehl verwenden:

powershell

Kopieren

`Get-Module -ListAvailable`

Dies zeigt dir alle verfügbaren Module an.

### 4. **Wie du ein Modul verwendest**

Sobald das Modul geladen ist, kannst du die Funktionen oder Cmdlets des Moduls verwenden. Beispiel:

1. Nachdem du das **Az**-Modul geladen hast, kannst du Cmdlets wie `Get-AzResource` verwenden, um Ressourcen in Azure zu verwalten.
    
    powershell
    
    Kopieren
    
    `Get-AzResource`
    
2. Wenn du ein Modul mit eigenen Funktionen hast, kannst du diese Funktionen einfach aufrufen. Beispiel:
    
    Angenommen, das Modul enthält eine Funktion namens `Get-DiskInfo`, dann kannst du diese wie folgt verwenden:
    
    powershell
    
    Kopieren
    
    `Get-DiskInfo`
    

### 5. **Module installieren**

Es gibt viele Module, die über die **PowerShell Gallery** verfügbar sind. Du kannst Module einfach mit dem folgenden Befehl installieren:

powershell

Kopieren

`Install-Module <Modulname>`

Beispiel:

powershell

Kopieren

`Install-Module -Name Az -Force`

- **Hinweis**: Wenn du ein Modul installierst, benötigst du möglicherweise Administratorrechte. Stelle sicher, dass du PowerShell als Administrator ausführst.

### 6. **Modul entfernen**

Wenn du ein Modul nicht mehr benötigst, kannst du es mit dem folgenden Befehl entfernen:

powershell

Kopieren

`Uninstall-Module <Modulname>`

### 7. **Häufige Fehler und Hinweise**

- **Modul nicht gefunden**: Wenn PowerShell dir mitteilt, dass das Modul nicht gefunden wurde, könnte es daran liegen, dass es nicht richtig installiert wurde oder sich nicht im richtigen Verzeichnis befindet. Stelle sicher, dass du `Install-Module` verwendest, um das Modul korrekt zu installieren.
- **Admin-Rechte**: Manche Module oder Installationen erfordern Administratorrechte. Achte darauf, PowerShell als Administrator zu starten (rechte Maustaste → „Als Administrator ausführen“).
- **Modul nicht geladen**: Wenn du ein Modul nach der Installation nicht verwenden kannst, könnte es daran liegen, dass du es nicht mit `Import-Module` geladen hast. Überprüfe auch, ob das Modul korrekt installiert wurde.

### 8. **Beispiele für nützliche Module**

- **Az-Modul**: Für die Verwaltung von Microsoft Azure.
- **PSSQL**: Für SQL Server-Verwaltung.
- **PSReadline**: Für eine bessere Benutzeroberfläche und Autovervollständigung in PowerShell.
- **PSWindowsUpdate**: Für die Verwaltung von Windows-Updates.
- **Chocolatey**: Für das Verwalten von Software-Paketen auf deinem Computer.

### 9. **Zusammenfassung und Fazit**

- **Module** erweitern die Funktionalität von PowerShell, indem sie vordefinierte Cmdlets und Funktionen bereitstellen.
- **Import-Module** lädt das Modul in die aktuelle Sitzung.
- **Install-Module** ermöglicht es dir, Module aus der PowerShell-Gallery zu installieren.
- Achte auf häufige Fehler wie fehlende Administratorrechte oder falsche Pfade, wenn Module nicht geladen werden können.



### **Was ist `Try-Catch` in PowerShell und wofür wird es genutzt?**

`Try-Catch` ist eine Fehlerbehandlung in PowerShell. Es hilft dabei, Fehler in deinem Skript zu finden und zu kontrollieren, was passiert, wenn etwas schiefgeht. Wenn ein Fehler auftritt, sorgt `Try-Catch` dafür, dass das Skript nicht abrupt abbricht, sondern dir hilft, den Fehler zu behandeln oder anzuzeigen.

#### **Wie funktioniert `Try-Catch`?**

- **`Try`-Block**: Hier schreibst du den Code, der ausgeführt wird. Wenn dieser Code keinen Fehler erzeugt, läuft das Skript ganz normal weiter.
- **`Catch`-Block**: Hier definierst du, was passieren soll, wenn ein Fehler im `Try`-Block auftritt.

**Beispiel:**

powershell

Kopieren

`try {     # Code, der einen Fehler verursachen könnte     $x = 10 / 0 } catch {     # Wenn ein Fehler auftritt, wird dieser Block ausgeführt     Write-Host "Ein Fehler ist aufgetreten: $_" }`

**Erklärung:**

- Im `try`-Block versuche ich, 10 durch 0 zu teilen, was natürlich einen Fehler (Division durch Null) verursacht.
- Der Fehler wird im `catch`-Block abgefangen und eine Fehlermeldung wird angezeigt.

### **Warum ist `Try-Catch` wichtig?**

- **Fehler handhaben**: Es verhindert, dass dein Skript einfach stoppt, wenn ein Fehler auftritt.
- **Saubere Fehlerbehandlung**: Du kannst spezifische Fehlermeldungen geben, was für eine bessere Benutzererfahrung sorgt.
- **Protokollierung**: Du kannst Fehler in einer Log-Datei speichern oder sie an einen Administrator weiterleiten.

### **Was sind andere Hilfsmittel zur Fehlerbehebung in PowerShell?**

Neben `Try-Catch` gibt es noch andere nützliche Techniken, um Fehler zu erkennen und zu beheben.

#### 1. **`$Error`-Variable**

PowerShell speichert alle Fehler, die während der Ausführung eines Skripts auftreten, in der **$Error**-Variable. Diese Variable ist eine Liste, in der du die letzten Fehler nachschlagen kannst.

Beispiel:

powershell

Kopieren

`$Error[0]  # Zeigt den letzten Fehler an`

#### 2. **`Write-Host` und `Write-Error`**

- **`Write-Host`**: Wird genutzt, um Nachrichten auf der Konsole anzuzeigen. Zum Beispiel, um zu sehen, ob ein Teil des Skripts ausgeführt wird.
- **`Write-Error`**: Wird verwendet, um Fehler manuell zu erzeugen. Das ist nützlich, wenn du Fehler in deinem Skript absichtlich auslösen möchtest, um auf bestimmte Bedingungen zu reagieren.

Beispiel:

powershell

Kopieren

`Write-Host "Das Skript wird ausgeführt." Write-Error "Ein Fehler ist aufgetreten!"`

#### 3. **`$?` (Status des letzten Befehls)**

`$?` gibt an, ob der letzte Befehl erfolgreich war (`$true`) oder nicht (`$false`).

Beispiel:

powershell

Kopieren

`Get-Item "C:\NonExistentFile.txt" if ($?) {     Write-Host "Der Befehl war erfolgreich." } else {     Write-Host "Der Befehl ist fehlgeschlagen." }`

### **Was ist Debugging?**

**Debugging** ist der Prozess, bei dem du nach Fehlern in deinem Code suchst und versuchst, diese zu beheben. Das Ziel ist es, den Code so zu ändern, dass er korrekt funktioniert.

In PowerShell kannst du Debugging auf verschiedene Arten durchführen:

#### 1. **Verwendung des `Set-PSDebug`-Befehls**

Du kannst die Debugging-Option aktivieren, um mehr Details während der Ausführung zu sehen.

- **Aktivieren**:
    
    powershell
    
    Kopieren
    
    `Set-PSDebug -Trace 1`
    
    Dieser Befehl zeigt an, welche Befehle gerade ausgeführt werden.
    
- **Deaktivieren**:
    
    powershell
    
    Kopieren
    
    `Set-PSDebug -Trace 0`
    

#### 2. **Verwendung von Breakpoints**

Ein **Breakpoint** ist ein Punkt im Code, an dem die Ausführung angehalten wird, damit du den Zustand deines Programms überprüfen kannst.

- **Hinzufügen eines Breakpoints**: Um einen Breakpoint in einem bestimmten Skript oder einer Funktion zu setzen, kannst du den folgenden Befehl verwenden:
    
    powershell
    
    Kopieren
    
    `Set-PSBreakpoint -Script "C:\Pfad\zum\Script.ps1" -Line 10`
    
    Dies setzt einen Breakpoint in Zeile 10 des Skripts, sodass die Ausführung dort stoppt und du den Zustand des Codes untersuchen kannst.
    

#### 3. **`Get-Help` und `Get-Command`**

Beide Befehle sind sehr nützlich, um Informationen über Cmdlets und Funktionen zu erhalten, was besonders bei der Fehlersuche hilft.

- **`Get-Help`**: Zeigt die Dokumentation und Beispiele für ein Cmdlet.
    
    powershell
    
    Kopieren
    
    `Get-Help Get-Process`
    
- **`Get-Command`**: Zeigt dir alle verfügbaren Cmdlets an, die PowerShell kennt.
    
    powershell
    
    Kopieren
    
    `Get-Command`
    

### **Was muss ich bei der Fehlersuche beachten?**

Fehlersuche kann manchmal mühsam sein, aber hier sind einige Dinge, auf die du achten solltest:

1. **Lies Fehlermeldungen sorgfältig**: PowerShell gibt dir häufig eine gute Fehlermeldung, die dir hilft, das Problem zu identifizieren.
2. **Überprüfe die Syntax**: Viele Fehler entstehen durch Tippfehler oder falsche Syntax. Achte darauf, dass du die Befehle korrekt schreibst.
3. **Schrittweise testen**: Anstatt das ganze Skript auf einmal auszuführen, teste es in kleinen Teilen. Führe eine Funktion nach der anderen aus, um zu sehen, wo der Fehler auftritt.
4. **Fehlerprotokollierung**: Nutze `Write-Host`, `Write-Error` und die `$Error`-Variable, um genau zu sehen, was schiefgeht.

### **Was kann ich bei der Fehlersuche falsch machen?**

- **Fehlende oder falsche Verwendung von `Try-Catch`**: Wenn du den Fehler nicht richtig abfängst oder den `Catch`-Block nicht korrekt nutzt, kann das Skript weiterhin mit Fehlern stoppen.
- **Unzureichende Testmethoden**: Wenn du nur auf das Skript als Ganzes schaust, ohne einzelne Teile zu testen, kann es schwierig sein, herauszufinden, wo der Fehler liegt.
- **Unklare Fehlermeldungen**: Wenn du eine ungenaue Fehlermeldung bekommst, kann es sein, dass du nicht genug Informationen über den Fehler sammelst, wie z.B. mit `$Error` oder durch das Einsetzen von Debugging-Methoden wie Breakpoints.

### **Zusammenfassung**

- **`Try-Catch`** hilft dir, Fehler im Skript zu fangen und kontrolliert zu behandeln.
- **Debugging** ermöglicht es dir, deinen Code zu untersuchen und Fehler zu finden, bevor sie das Skript stoppen.
- **Breakpoints** erlauben dir, das Skript an bestimmten Stellen zu stoppen, um den Zustand zu überprüfen.
- **Hilfsmittel wie `Write-Host`, `$Error` und `$?`** geben dir zusätzliche Informationen, um Fehler zu erkennen.




