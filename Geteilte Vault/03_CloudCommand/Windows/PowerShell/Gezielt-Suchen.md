---
created: 2024-12-01T08:55
updated: 2024-12-01T08:56
---
Recursiv nach dem Inhalt "Hello World" in allen Dateien suchen

```powershell
Get-ChildItem -recurse | select-string -pattern "Hello World"
```

Ordner exkludieren

```powershell
Get-ChildItem -Recurse | Where-Object { $_.FullName -notmatch '.obsidian' }

Get-ChildItem -Exclude folder1,folder2 | Get-ChildItem -Recurse | 
```
