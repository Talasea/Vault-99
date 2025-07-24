---
created: 2024-12-05T11:24
updated: 2024-12-05T11:31
---
Einfache Freigabe mit Standardberechtigungen erstellen

```powershell
New-SmbShare -Name "Wichtelversteck" -Path "C:\Wichtel\Geheimversteck"
```

Zusätzliche Berechtigungen definieren

```powershell
 -FullAccess "Todesser"
 -ReadAccess "Albus"
 -ChangeAccess "Harry"
```