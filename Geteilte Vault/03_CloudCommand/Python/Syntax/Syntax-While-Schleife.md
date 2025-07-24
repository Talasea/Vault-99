---
created: 2025-02-21T10:04
updated: 2025-02-21T10:07
---

```python
# Wir starten mit dem Initialwert 0 für die Variable i.
i = 0  

# Die while-Schleife wird so lange ausgeführt, wie die Bedingung True ist.
# Hier lautet die Bedingung: i < 3. Das bedeutet, solange der Wert von i kleiner als 3 ist.
while i < 3:  
    # In jedem Schleifendurchlauf wird der aktuelle Wert von i ausgegeben.
    print("Durchlauf:", i)
    
    # Um sicherzustellen, dass die Schleife irgendwann endet, wird i um 1 erhöht.
    # Dadurch nähert sich i dem Wert 3 an und die Bedingung i < 3 wird irgendwann falsch.
    i += 1

# Beispiel einer Endlosschleife 
while True:
    print("Unendliche Schleife...")

#Ein Beispiel für eine Endlossschleifen war das Menü im [Temperatur-Umrechner]]
```