
Die Windows-Registry ist eine zentrale hierarchische Datenbank, die Konfigurationen und Einstellungen für das Microsoft Windows-Betriebssystem und installierte Anwendungen speichert. Sie wurde 1992 mit Windows 3.1 eingeführt und ersetzt die früheren INI-Dateien, die Konfigurationen für einzelne Programme speicherten. Die Registry enthält Informationen zu Systemeinstellungen, Anwendungen und Hardware und kann von Administratoren und fortgeschrittenen Benutzern für Systemoptimierung und Troubleshooting verwendet werden.

Die Registry besteht aus Schlüsseln und Werten. Schlüssel sind Containerobjekte ähnlich wie Ordner und können Werte und Unterkeys enthalten. Werte sind nicht-containerähnliche Objekte, ähnlich wie Dateien. Schlüssel werden mit einem Syntax vergleichbar zu Windows-Pfadnamen referenziert, wobei Backslashes () die Hierarchieebenen anzeigen.

Um die Registry zu bearbeiten, kann der Registry-Editor (Regedit.exe) verwendet werden. Dieser Editor ermöglicht es Benutzern, Werte zu bearbeiten, zu exportieren und zu importieren. Registrierungsdateien (.REG) können verwendet werden, um Teile der Registry zu exportieren und wieder zu importieren. Ein Beispiel für die Syntax einer .REG-Datei lautet:

```
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Wikipedia]
"PathToExe"="C:\\Program Files (x86)\\ACME Corp\\ACE.exe"
"haenschen"=hex:
"klein"=dword:
"geht"=hex(0):
"allein"=hex(1):
"in"=hex(2):
"die"=hex(3): ; identisch mit "hex:"
"weite"=hex(4): ; Little-Endian
"Welt"=hex(5): ; Big-Endian
"hinein"=hex(7): ; getrennt durch Komma
"Stock"=hex(8): ; getrennt durch Komma
"und"=hex(a): ; getrennt durch Komma
"Hut"=hex(b): ; acht Hex-Werte, getrennt durch Komma
```

Die Registry kann auch über PowerShell-Befehle bearbeitet werden. Ein vorangestelltes Minus (-) entfernt einen Schlüssel oder einen Wert. Beispielsweise entfernt `[-HKEY_LOCAL_MACHINE\SOFTWARE\Wikipedia]` den gesamten Schlüssel.

Es ist wichtig, dass Änderungen an der Registry vorsichtig durchgeführt werden, da unzulängliche Änderungen das System und die Programme merkwürdig verhalten lassen können.

![[Pasted image 20250124120748.png]]



![[Pasted image 20250124120815.png]]

Die SAM (Security Accounts Manager) Datei ist ein wichtiger Bestandteil der Windows-Registry und speichert Informationen über Benutzerkonten und ihre Zugriffsberechtigungen. In der Registry ist die SAM-Datei unter `HKEY_LOCAL_MACHINE\SAM` zu finden. Diese Datei ist jedoch standardmäßig nicht sichtbar und kann nicht direkt gelesen werden, da sie verschlüsselt ist.

Um den Inhalt der SAM-Datei in der Registry sichtbar zu machen, muss die Registry über das “lokale System” gestartet werden. Dies kann durch den Befehl `AT` in der Eingabeaufforderung erreicht werden. Ein Beispiel dafür wäre `AT 15:55 /INTERACTIVE CMD.EXE`, wenn es etwa 15:53 Uhr ist. Dieser Befehl öffnet dann die Eingabeaufforderung im Kontext des Systems, was es ermöglicht, die Registry mit vollem Leserecht auf dem SAM-Schlüssel zu öffnen.

Die SAM-Datei selbst befindet sich im Verzeichnis `C:\Windows\System32\config` und trägt die Endung `.SAM`. Sie ist jedoch gesperrt und kann nicht bearbeitet oder gelöscht werden, solange das Betriebssystem läuft. Wenn der Computer von einer Live-Wiederherstellungs-CD wie ophcrack gebootet wird, ist die Datei jedoch vollständig zugänglich.

Es ist wichtig zu beachten, dass das Bearbeiten der SAM-Datei oder ihres Inhalts in der Registry ohne ausreichende Kenntnisse gefährlich sein kann und zu Problemen mit Benutzerkonten und Zugriffsberechtigungen führen kann.