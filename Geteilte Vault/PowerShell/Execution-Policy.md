---
created: 2024-12-01T08:47
updated: 2024-12-01T08:47
---

PowerShell Skripte ausführbar machen durch Änderung der `Execution Policy`

```powershell
# Beispiel mit den möglichen Optionen (funktioniert nicht als Kommando!)
Set-ExecutionPolicy Bypass|Unrestricted|Restriced \
- Scope Process|CurrentUser|LocalMachine

# Die Execution Policy für den aktuellen Benutzer auf Bypass setzten
Set-ExecutionPolicy Bypass -Scope CurrentUser -Force

# Die Execution Policy für den aktuellen Prozess auf Unrestricted setzten
Set-ExecutionPolicy Unrestricted -Scope Process -Force
```