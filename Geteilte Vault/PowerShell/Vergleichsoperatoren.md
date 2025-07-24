---
created: 2024-12-01T08:27
updated: 2024-12-03T10:00
---

Kleiner als & größer als

```powershell
# testet ob linke Zahl kleiner ist (less then) als Rechte
( 1 -lt 10 ) -> True 
# testet ob linke Zahl größer ist (greater then) als Rechte
( 10 -gt 1 ) -> True 
```

Kleiner gleich & größer gleich

```powershell
# vergleicht ob Zahlen kleiner gleich (less/equal) sind
( 7 -le 7 )  -> True # 
# vergleicht ob Zahlen größer gleich (greater equal) sind
( 7 -ge 7 )  -> True 
```

Ist exakt gleich

```powershell
( "eins" -eq "zwei" ) -> False
( "zwei" -eq "zwei" ) -> True
( "zwei" -eq "ZwEi" ) -> True # Windows ist case insensitive
```

Auf einen Teilstring prüfen

```powershell
$meinString = "Luke, ich bin dein Vater"
( $meinString -like "*Luke*" ) -> True # Der String enhält "Luke"
```

Auf einen Datentyp prüfen

```powershell
( $meineZahl -is [int] ) -> True
( $meinString -is [string] ) -> True 
```