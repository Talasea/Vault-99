---
created: 2024-12-03T09:47
updated: 2024-12-04T10:12
---
Durch jedes Element in einer Liste iterieren (durchgehen)

```powershell
$fruechte = ("Birnen","Kirschen","Bananen","Kiwi","Melone","Orange")

# Temporäre Variable $element nimmt der Reihe nach Werte der Liste an
foreach ( $element in $fruechte ) {
    Write-Output "Ich esse gerne $element"
}
```