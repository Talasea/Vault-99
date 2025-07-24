---
created: 2024-11-20T09:59
updated: 2024-12-01T08:41
---

`If/Else` Anweisung

```powershell
if ( $Bedingung ) {
	# Der Teil zwischen den geschweiften Klammern hier wird nur ausgeführt
	# wenn die Bedingung (das Statement in den Runden Klammern) erfüllt ist
	Write-Host "$Bedinung ist erfüllt"
} Else {
	# Ansonsten wird dieser Teil ausgeführt
	Write-Host "$Bedingung ist *nicht* erfüllt"
}
```

Erweiterbar mit einem zusätzlichen `Elseif` statement nach dem `If`
```powershell
} Elseif ( $ZweiteBedingung ) {
	Write-Host "$ZweiteBedinung ist erfüllt"
}
```