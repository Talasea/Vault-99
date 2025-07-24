---
created: 2024-12-03T11:19
updated: 2024-12-03T11:35
---

Definiere die Basis-Domain (Bitte anpassen an deine Umgebung)

```powershell
$domain = "DC=awesome,DC=local"
```

Erstelle neue Organisationseinheiten (OUs) `Hogwarts` auf höchster Ebene

```powershell
New-ADOrganizationalUnit -Name "Hogwarts" -Path "$domain"
```

Erstelle eine neue Unter-OU `Große Halle` innerhalb von `Hogwarts`

```powershell
New-ADOrganizationalUnit -Name "Große Halle" \
-Path "OU=Hogwarts,$domain"
```

Neue Unter-Unter-OU `Lehrerpult` innerhalb der `Großen Halle`

```powershell
New-ADOrganizationalUnit -Name "Lehrerpult" \
-Path "OU=Große Halle,OU=Hogwarts,$domain"
```