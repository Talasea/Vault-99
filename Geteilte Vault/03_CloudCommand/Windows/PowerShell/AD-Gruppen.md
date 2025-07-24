---
created: 2024-12-01T09:28
updated: 2024-12-03T11:17
---

🌐Minimum: SamAccountNamen, Name und Gruppentyp angeben

```powershell
New-ADGroup -Name "Tigers" -SamAccountName "Tigers" -GroupScope Global
```

Andere Flags
```powershell
-Path "OU=Groups,DC=domain,DC=com" 
-Description "Engineering Department Group"
-GroupCategory Security
```

✅ Add John to the EngineeringTeam group ✅

```powershell
Add-ADGroupMember -Identity "EngineeringTeam" -Members "jdoe"
```

❗Remove John from group ❗

```powershell
Remove-ADGroupMember -Identity "EngineeringTeam" -Members "jdoe" -Confirm:$false
```