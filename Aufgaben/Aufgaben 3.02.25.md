
### **Aufgabe 1: Zeige alle Dateien und Unterordner im aktuellen Verzeichnis an**

**Befehl:**

Get-ChildItem

![[Pasted image 20250203142101.png]]![[

 **Erklärung:**  
`Get-ChildItem` listet alle Dateien und Ordner im aktuellen Verzeichnis auf.  
_Alternativ Command :_  `ls` (Unix-Stil) oder `dir` (CMD-Stil) verwenden.


---

### **Aufgabe 2: Erstelle einen Ordner namens PowerShellTest**

**Befehl:**

New-Item -ItemType Directory -Name PowerShellTest


![[Pasted image 20250203142414.png]]




 **Erklärung:**  
`New-Item` erstellt ein neues Objekt. 
Mit `-ItemType Directory` sagst du, dass es ein Ordner sein soll.


---

### **Aufgabe 3: Erstelle eine leere Textdatei test.txt im PowerShellTest-Ordner**

**Befehl:**

New-Item -Path .\PowerShellTest\test.txt -ItemType File

![[Pasted image 20250203142548.png]]
 
 **Erklärung:**  
`-Path` gibt den Speicherort an. <font color="#ff0000">`-ItemType File`</font> erstellt eine leere Datei.


---

### **Aufgabe 4: Schreibe "Hallo PowerShell!" in test.txt**

**Befehl:**

Set-Content -Path .\PowerShellTest\test.txt -Value "Hallo PowerShell!"

![[Pasted image 20250203142707.png]]

![[Pasted image 20250203142753.png]]

**Erklärung:**  
`Set-Content` überschreibt den Inhalt einer Datei. 
Mit `-Value` fügst du den Text hinzu.


---

### **Aufgabe 5: Zeige den Inhalt von test.txt an**

**Befehl:**

Get-Content -Path .\PowerShellTest\test.txt

![[Pasted image 20250203142914.png]]

**Erklärung:**  
`Get-Content` liest den Inhalt einer Datei aus und zeigt ihn in der Konsole an.


---

### **Aufgabe 6: Erstelle einen Benutzer TestUser mit Passwort**

**Befehl:**

New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "Klasse123" -AsPlainText -Force) -FullName "Test User" -Description "Testbenutzer für PowerShell"

![[Pasted image 20250203143856.png]]

**Erklärung:**

`ConvertTo-SecureString` wandelt das Passwort in ein sicheres Format um.
 
`New-LocalUser` erstellt den Benutzer mit dem sicheren Passwort.  
 
PowerShell als Administrator starten, um Benutzer zu erstellen.
    

---

### **Aufgabe 7: Zeige alle laufenden Prozesse an**

**Befehl:**

Get-Process

![[Pasted image 20250203144045.png]]



**Erklärung:**  
`Get-Process` listet alle aktuell aktiven Prozesse auf (z. B. Apps, Hintergrunddienste).


---

### **Aufgabe 8: Beende Notepad.exe (starte ihn vorher, falls nicht aktiv)**

Starte Notepad, falls er nicht läuft

Start-Process notepad
oder  *grins* 
if (-not (Get-Process notepad -ErrorAction SilentlyContinue)) { Start-Process notepad }

Beende Notepad

Stop-Process -Name notepad

oder

Stop-Process -Name notepad -ErrorAction SilentlyContinue


Als script : 
if (-not (Get-Process notepad -ErrorAction SilentlyContinue)) { Start-Process notepad }
Stop-Process -Name notepad -ErrorAction SilentlyContinue


**Erklärung:**

 `Get-Process` prüft, ob Notepad läuft.

 `Start-Process` startet Notepad, falls er nicht aktiv ist.

 `Stop-Process` beendet den Prozess.


---

### **Aufgabe 9: Füge TestUser zur Gruppe Administrators hinzu**

**Befehl (als Administrator ausführen):**


Add-ADGroupMember -Identity "Administrators" -Members "BenutzerName"
![[Pasted image 20250203152749.png]]

![[Pasted image 20250203152809.png]]

Erklärung:  
Add-ADGroupMember fügt den Benutzer der Gruppe hinzu.  

Add-LocalGroupMember -Group "Administratoren" -Member "TestUser" würde eine lokale gruppe den user zuordnen




---

### **Aufgabe 10: Unterschiede zwischen CMD und PowerShell**

#### **1. Normale Kommandozeile (CMD) vs. PowerShell**

- **CMD:**

- Arbeitet mit **Textausgaben** (z. B. `dir` zeigt Text an).

- Eingeschränkte Skriptfähigkeiten.

- **PowerShell:**

- **Objektorientiert** (Befehle geben Objekte zurück, die du weiterverarbeiten kannst).

- **Mächtige Skriptsprache** mit Schleifen, Bedingungen und Fehlerbehandlung.

- **Cmdlets** (siehe unten) statt einfache Befehle.


#### **2. Was ist ein „Cmdlet“?**

- Ein **Cmdlet** (Commandlet) ist ein PowerShell-Befehl im Format **Verb-Noun** (z. B. `Get-ChildItem`).

- Beispiele:

- `Get-*` (Daten abrufen)

- `Set-*` (Daten ändern)

- `New-*` (Objekte erstellen)


- **Vorteil:** Cmdlets können Objekte weiterreichen (z. B. `Get-Process | Stop-Process`).


#### **3. Was ist ein PowerShell-Skript?**

- Eine **.ps1-Datei**, die PowerShell-Befehle enthält.

- **Einsatz:** Automatisierung von Aufgaben (z. B. mehrere Cmdlets hintereinander ausführen).

- **Beispiel:**



Skript.ps1
$Text = "Hallo Welt!"
Write-Output $Text

Ausführen: Im PowerShell-Fenster mit `.\Skript.ps1` (sofern die Ausführungsrichtlinie dies erlaubt).
    
