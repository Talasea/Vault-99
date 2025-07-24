---
created: 2025-01-21T09:35
updated: 2025-01-21T09:37
---
Dateien verschieben mit dem `Move-Item` Commandlet

```powershell
Move-Item -path $Quellpfad -destination $Zielpfad
Move-Item -path .\2024\Tagesnotizen\2025* -destination .\2025\Tagesnotizen\
```

Shortcut

```powershell
mv $Quellpfad $Zielpfad
```