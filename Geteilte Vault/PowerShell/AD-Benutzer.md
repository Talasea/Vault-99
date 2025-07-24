---
created: 2024-12-01T09:20
updated: 2024-12-03T11:12
---
 
🌐 Minumum: SamAccountName angeben und aktivieren

```powershell
New-ADUser -SamAccountName "jdoe" -Enabled $true
```

Direkt das Passwort setzen (aus Security Perspektive eine **ganz schlechte Idee!**)

```powershell
New-ADUser -SamAccountName "jdoe" -Enabled $true
-AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) 
```

Andere Flags

```powershell
-Name "John Doe" 
-GivenName "John" # Vorname
-Surname "Doe" # Nachname
-SamAccountName "jdoe" 
-UserPrincipalName "jdoe@domain.local"
-Path "OU=Auroren-Abteilung,OU=Ministerium fuer Zauberei,DC=awesome,DC=local" 
```

❗Remove User ❗

```powershell
Remove-ADUser -Identity "jdoe" -Confirm:$false
```

